#!/usr/bin/env python3
"""Deterministic deal math for reviewing venture financing terms.

Subcommands:
  waterfall    Exit proceeds by share class (liquidation preferences, participation,
               caps, seniority, cumulative dividends, conversion decisions, options).
  antidilution New conversion price and extra shares under broad-based weighted
               average, narrow-based weighted average, and full ratchet.
  round        Pro forma priced round: pre-money price per share, option pool
               top-up, SAFE and convertible note conversion, ownership table.
  safes        Ownership already sold through post-money SAFEs, before any priced
               round, and what an additional SAFE would add.

Run `deal_math.py <subcommand> --help` or `deal_math.py example <subcommand>` for an
input template. Standard library only. Results model the inputs given; they do not
interpret contract language, so check each input against the actual documents.
"""

import argparse
import json
import math
import sys

EPS = 1e-9


# ---------------------------------------------------------------- formatting

def money(x):
    sign = "-" if x < 0 else ""
    x = abs(x)
    if x >= 1e9:
        return f"{sign}${x / 1e9:,.2f}B"
    if x >= 1e6:
        return f"{sign}${x / 1e6:,.2f}M"
    if x >= 1e3:
        return f"{sign}${x / 1e3:,.1f}K"
    return f"{sign}${x:,.2f}"


def pct(x):
    return f"{x * 100:.1f}%"


def table(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


def parse_amounts(text):
    """Parse '5M,20M,1.5B,750000' into floats."""
    mult = {"K": 1e3, "M": 1e6, "B": 1e9}
    values = []
    for part in text.split(","):
        part = part.strip().replace("$", "").replace("_", "")
        if not part:
            continue
        suffix = part[-1].upper()
        values.append(float(part[:-1]) * mult[suffix] if suffix in mult else float(part))
    return values


def load_json(path):
    with open(path) if path != "-" else sys.stdin as f:
        return json.load(f)


# ---------------------------------------------------------------- waterfall

def preference_base(c):
    """Original issue price x shares; differs from cash invested for SAFE shadow series."""
    return c.get("preference_base", c["invested"])


def preference_amount(c):
    """Liquidation preference claim for a non-converting preferred class."""
    base = preference_base(c)
    amount = base * c.get("pref_multiple", 1.0)
    div = c.get("cumulative_dividend")
    if div:
        rate, years = div["rate"], div["years"]
        if div.get("compound"):
            amount += base * ((1 + rate) ** years - 1)
        else:
            amount += base * rate * years
    return amount


def distribute_residual(residual, participants):
    """Split residual proceeds per as-converted share.

    participants: list of dicts with shares, optional strike (options/warrants),
    optional cap_room (max additional amount for capped participating preferred).
    Returns (price_per_share, {name: amount}).
    """
    otm, frozen = set(), set()
    p = 0.0
    for _ in range(200):
        pool = residual - sum(participants[i]["cap_room"] for i in frozen)
        shares = 0.0
        for i, part in enumerate(participants):
            if i in otm or i in frozen:
                continue
            shares += part["shares"]
            pool += part.get("strike", 0.0) * part["shares"]  # exercise proceeds
        p = pool / shares if shares > EPS else 0.0
        new_otm = {i for i, part in enumerate(participants)
                   if part.get("strike", 0.0) > 0 and part["strike"] >= p - EPS}
        new_frozen = {i for i, part in enumerate(participants)
                      if part.get("cap_room") is not None and i not in new_otm
                      and part["shares"] * p > part["cap_room"] + EPS}
        if new_otm == otm and new_frozen == frozen:
            break
        otm, frozen = new_otm, new_frozen
    payout = {}
    for i, part in enumerate(participants):
        if i in otm:
            amt = 0.0
        elif i in frozen:
            amt = part["cap_room"]
        else:
            amt = part["shares"] * (p - part.get("strike", 0.0))
        payout[part["name"]] = payout.get(part["name"], 0.0) + max(amt, 0.0)
    return p, payout


def as_converted(c):
    """As-converted shares, including penalty or bonus shares that carry no preference."""
    return c["shares"] * c.get("conversion_ratio", 1.0) + c.get("extra_shares", 0.0)


def run_waterfall(classes, proceeds, converting):
    """Distribute proceeds given the set of preferred classes that convert."""
    payout = {c["name"]: 0.0 for c in classes}
    remaining = proceeds
    prefs = [c for c in classes if c["type"] == "preferred" and c["name"] not in converting]
    for rank in sorted({c.get("rank", 1) for c in prefs}):
        tier = [c for c in prefs if c.get("rank", 1) == rank]
        claims = {c["name"]: preference_amount(c) for c in tier}
        total = sum(claims.values())
        paid = min(remaining, total)
        for name, claim in claims.items():
            payout[name] += paid * claim / total if total > 0 else 0.0
        remaining -= paid

    participants = []
    for c in classes:
        if c["type"] == "common":
            participants.append({"name": c["name"], "shares": c["shares"],
                                 "strike": c.get("strike", 0.0)})
        elif c["name"] in converting:
            participants.append({"name": c["name"], "shares": as_converted(c)})
        elif c.get("participation", "none") in ("full", "capped"):
            part = {"name": c["name"], "shares": as_converted(c)}
            if c["participation"] == "capped":
                cap_total = preference_base(c) * c["cap_multiple"]
                counted = payout[c["name"]]
                if not c.get("cap_includes_dividends", True):
                    full = preference_amount(c)
                    no_div = preference_base(c) * c.get("pref_multiple", 1.0)
                    counted *= no_div / full if full else 0.0
                part["cap_room"] = max(cap_total - counted, 0.0)
            participants.append(part)
    price, residual_payout = distribute_residual(max(remaining, 0.0), participants)
    for name, amt in residual_payout.items():
        payout[name] += amt
    return payout, price


def solve_conversions(classes, proceeds):
    """Best-response iteration: each preferred class converts only if it gets more."""
    prefs = [c["name"] for c in classes if c["type"] == "preferred"]
    converting = set()
    for _ in range(100):
        changed = False
        for name in prefs:
            stay = run_waterfall(classes, proceeds, converting - {name})[0][name]
            conv = run_waterfall(classes, proceeds, converting | {name})[0][name]
            want = conv > stay + 1e-6
            if want != (name in converting):
                converting = converting | {name} if want else converting - {name}
                changed = True
        if not changed:
            break
    payout, price = run_waterfall(classes, proceeds, converting)
    return payout, price, converting


def normalize_classes(raw):
    classes = []
    for c in raw:
        c = dict(c)
        c.setdefault("type", "common")
        if c["type"] == "preferred":
            if "invested" not in c:
                c["invested"] = c["price"] * c["shares"]
            c.setdefault("participation", "none")
            if c["participation"] == "capped" and "cap_multiple" not in c:
                raise SystemExit(f"{c['name']}: capped participation needs cap_multiple")
        classes.append(c)
    return classes


def cmd_waterfall(args):
    data = load_json(args.input)
    classes = normalize_classes(data["classes"])
    exits = parse_amounts(args.exits) if args.exits else data.get("exits", [])
    if not exits:
        raise SystemExit("Provide exit values with --exits or an 'exits' list in the input.")
    costs = data.get("transaction_costs", 0.0)
    carve = data.get("carve_out_percent", 0.0)
    founder_names = set(data.get("founder_classes", []))
    if args.dividend_years is not None:
        for c in classes:
            if c.get("cumulative_dividend"):
                c["cumulative_dividend"] = dict(c["cumulative_dividend"], years=args.dividend_years)
    shares_ac = {c["name"]: as_converted(c) for c in classes}
    total_fd = sum(shares_ac.values())

    results = []
    for exit_value in exits:
        net = max(exit_value - costs, 0.0)
        carve_amt = net * carve
        payout, price, converting = solve_conversions(classes, net - carve_amt)
        results.append({"exit": exit_value, "net": net, "carve_out": carve_amt,
                        "payout": payout, "common_price": price,
                        "converting": sorted(converting)})

    if args.json:
        print(json.dumps(results, indent=2))
        return

    print("# Exit waterfall\n")
    print(f"As-converted shares modeled: {total_fd:,.0f} (unissued pool counts only if listed)")
    if args.dividend_years is not None:
        print(f"Cumulative dividends accrued for {args.dividend_years:g} years")
    if costs:
        print(f"Transaction costs / debt paid first: {money(costs)}")
    if carve:
        print(f"Management carve-out: {pct(carve)} of net proceeds")
    print()
    headers = ["Class", "% of shares modeled"] + [money(r["exit"]) for r in results]
    rows = []
    for c in classes:
        row = [c["name"], pct(shares_ac[c["name"]] / total_fd)]
        for r in results:
            amt = r["payout"][c["name"]]
            share = amt / r["exit"] if r["exit"] else 0.0
            row.append(f"{money(amt)} ({pct(share)})")
        rows.append(row)
    if founder_names:
        row = ["**Founders total**", pct(sum(shares_ac[n] for n in founder_names) / total_fd)]
        for r in results:
            amt = sum(r["payout"][n] for n in founder_names)
            row.append(f"**{money(amt)} ({pct(amt / r['exit'] if r['exit'] else 0)})**")
        rows.append(row)
    if carve:
        rows.append(["Carve-out pool", "-"] + [money(r["carve_out"]) for r in results])
    print(table(headers, rows))
    print()
    print("Preferred decisions (pref = takes liquidation preference, conv = converts to common):")
    for c in classes:
        if c["type"] != "preferred":
            continue
        cells = []
        for r in results:
            amt = r["payout"][c["name"]]
            decision = "conv" if c["name"] in r["converting"] else "pref"
            cells.append(f"{money(r['exit'])}: {decision}, {amt / c['invested']:.2f}x")
        print(f"- {c['name']} ({money(c['invested'])} invested): " + "; ".join(cells))
    print()
    print("Common value per share: " + "; ".join(
        f"{money(r['exit'])}: ${r['common_price']:,.4f}" for r in results))


# ---------------------------------------------------------------- anti-dilution

def cmd_antidilution(args):
    cp1, new_price = args.cp1, args.new_price
    oip = args.oip or cp1
    if new_price >= cp1:
        print(f"New price ${new_price} is not below the conversion price ${cp1}; "
              "price-based anti-dilution is not triggered.")
        return
    c = args.new_shares
    b = new_price * c / cp1  # shares the new money would have bought at CP1
    methods = []
    if args.a_broad:
        methods.append(("Broad-based weighted average", cp1 * (args.a_broad + b) / (args.a_broad + c)))
    if args.a_narrow:
        methods.append(("Narrow-based weighted average", cp1 * (args.a_narrow + b) / (args.a_narrow + c)))
    methods.append(("Full ratchet", new_price))

    rows = []
    for name, cp2 in methods:
        before = args.pref_shares * oip / cp1
        after = args.pref_shares * oip / cp2
        rows.append([name, f"${cp2:,.4f}", f"{after / args.pref_shares * cp1 / oip:,.4f}x",
                     f"{after:,.0f}", f"{after - before:,.0f}",
                     money((after - before) * new_price)])
    print("# Anti-dilution adjustment\n")
    print(f"Old conversion price ${cp1:,.4f}; new issue price ${new_price:,.4f}; "
          f"new shares issued {c:,.0f} (new money {money(new_price * c)}).")
    print("Formula: CP2 = CP1 x (A + B) / (A + C), B = new money / CP1, C = new shares.\n")
    print(table(["Method", "New conversion price", "Conversion ratio vs before",
                 "As-converted shares", "Extra shares", "Extra value at new price"], rows))
    print("\nExtra shares come out of everyone not protected (usually founders, employees,"
          " and earlier holders without the protection). Check the charter's definition of"
          " A and the excluded issuances before relying on these numbers.")


# ---------------------------------------------------------------- priced round

def note_amount(n):
    years = n.get("years", 0.0)
    rate = n.get("interest_rate", 0.0)
    principal = n["principal"]
    if n.get("compound"):
        return principal * (1 + rate) ** years
    return principal * (1 + rate * years)


def cmd_round(args):
    d = load_json(args.input)
    pre = d["pre_money"]
    investment = d["investment"]
    target_pool = d.get("target_pool_post_percent", 0.0)
    pool_in_pre = d.get("pool_in_pre_money", True)
    converting_in_pre = d.get("converting_in_pre_money", True)
    existing = d["existing"]
    safes = d.get("safes", [])
    notes = d.get("notes", [])

    e_total = sum(h["shares"] for h in existing)
    unissued0 = sum(h["shares"] for h in existing if h.get("pool"))
    instruments = [dict(s, kind="SAFE", amount=s["amount"]) for s in safes]
    instruments += [dict(n, kind="Note", amount=note_amount(n)) for n in notes]

    price = pre / e_total
    x = 0.0
    conv_shares = [0.0] * len(instruments)
    basis = [""] * len(instruments)
    for _ in range(10000):
        s_total = sum(conv_shares)
        new_conv = []
        for i, inst in enumerate(instruments):
            candidates = [(price, "round price")]
            if inst.get("discount"):
                candidates.append((price * (1 - inst["discount"]), "discount"))
            if inst.get("cap"):
                cap_type = inst.get("type", "post" if inst["kind"] == "SAFE" else "pre")
                capitalization = e_total + s_total if cap_type == "post" else e_total + x
                candidates.append((inst["cap"] / capitalization, f"{cap_type}-money cap"))
            conv_price, how = min(candidates, key=lambda t: t[0])
            new_conv.append(inst["amount"] / conv_price)
            basis[i] = f"{how} @ ${conv_price:,.4f}"
        conv_shares = new_conv
        s_total = sum(conv_shares)
        new_money_shares = investment / price
        post_total = e_total + x + s_total + new_money_shares
        new_x = max(target_pool * post_total - unissued0, 0.0)
        denom = e_total + new_x * pool_in_pre + s_total * converting_in_pre
        new_price = pre / denom
        if abs(new_price - price) < 1e-12 * price and abs(new_x - x) < 1e-6:
            price, x = new_price, new_x
            break
        # damped update keeps the fixed point stable when caps and pool interact
        price, x = 0.5 * (price + new_price), 0.5 * (x + new_x)
    else:
        raise SystemExit("Round model did not converge; check inputs.")

    new_money_shares = investment / price
    s_total = sum(conv_shares)
    post_total = e_total + x + s_total + new_money_shares
    investors = d.get("investors") or [{"name": "New investors", "amount": investment}]
    if abs(sum(i["amount"] for i in investors) - investment) > 0.5:
        raise SystemExit("investors[] amounts must add up to investment.")
    post_money = price * post_total
    effective_pre = pre - price * (x * pool_in_pre + s_total * converting_in_pre)
    effective_pre_issued = effective_pre - price * unissued0

    print("# Priced round pro forma\n")
    print(f"Headline pre-money: {money(pre)}; new money: {money(investment)}")
    print(f"Price per share: ${price:,.4f}")
    print(f"Post-money (price x post shares): {money(post_money)}")
    print(f"Option pool increase: {x:,.0f} shares"
          f" ({'in pre-money' if pool_in_pre else 'post-money'}); unissued pool after round:"
          f" {pct((unissued0 + x) / post_total)} of post")
    print(f"Effective pre-money (headline minus whatever pool increase and converting"
          f" securities are counted in the pre-money): {money(effective_pre)}; also excluding"
          f" the existing unallocated pool: {money(effective_pre_issued)}\n")

    rows = []
    for h in existing:
        label = h["name"]
        if h.get("pool") and "pool" not in label.lower():
            label += " (unissued pool)"
        rows.append([label, f"{h['shares']:,.0f}", pct(h["shares"] / e_total),
                     pct(h["shares"] / post_total), money(h["shares"] * price)])
    if x > 0:
        rows.append(["Pool increase", f"{x:,.0f}", "-", pct(x / post_total), money(x * price)])
    for inst, sh, how in zip(instruments, conv_shares, basis):
        rows.append([f"{inst['name']} ({inst['kind']}, {money(inst['amount'])}; {how})",
                     f"{sh:,.0f}", "-", pct(sh / post_total), money(sh * price)])
    for inv in investors:
        sh = inv["amount"] / price
        rows.append([inv["name"], f"{sh:,.0f}", "-", pct(sh / post_total), money(inv["amount"])])
    rows.append(["**Total**", f"{post_total:,.0f}", "100.0%", "100.0%", money(post_money)])
    print(table(["Holder", "Shares", "Before % (existing shares only)", "After %",
                 "Value at round price"], rows))
    founders = [h for h in existing if h.get("founder")]
    if founders:
        f_shares = sum(h["shares"] for h in founders)
        line = f"\nFounders: {pct(f_shares / e_total)} of existing shares"
        if instruments:
            line += (f"; {pct(f_shares / (e_total + s_total))} once SAFEs and notes convert"
                     " (before new money and pool increase)")
        print(line + f"; {pct(f_shares / post_total)} after the round.")
    classes = waterfall_classes(d, existing, instruments, conv_shares, investors, price)
    pref = [c for c in classes if c["type"] == "preferred"]
    if pref:
        pref_total = sum(c["shares"] * c.get("conversion_ratio", 1.0) for c in pref)
        new_total = sum(inv["amount"] / price for inv in investors)
        print("\nPreferred voting blocs (as converted) — compare with the documents' majority"
              " definitions, e.g. Requisite Holders:")
        for c in pref:
            share = c["shares"] * c.get("conversion_ratio", 1.0) / pref_total
            in_new = any(c["name"] == inv["name"] for inv in investors)
            extra = ""
            if in_new:
                extra = f"; {pct(c['shares'] / new_total)} of the new-money series"
                if instruments:
                    extra += f" ({pct(c['shares'] / (new_total + s_total))} if converted SAFEs and notes vote with it)"
            print(f"- {c['name']}: {pct(share)} of all preferred{extra}")
        if instruments:
            inv_total = sum(c["shares"] for c in pref if c["name"] in {i["name"] for i in investors}
                            or c["name"] in {h["name"] for h in existing})
            print("  Excluding converted SAFEs and notes (if the documents give them no vote): "
                  + "; ".join(f"{c['name']} {pct(c['shares'] / inv_total)}" for c in pref
                              if c["name"] not in {i["name"] for i in instruments}))
    if args.emit_waterfall:
        if args.include_pool is not None:
            classes.append({"name": "Unallocated pool (assumed granted)", "type": "common",
                            "shares": unissued0 + x, "strike": args.include_pool})
        stack = sum(preference_amount(c) for c in pref)
        exits = sorted({round(stack, -3)} | {round(post_money * m, -3) for m in (0.5, 1, 2, 5)})
        out = {"exits": exits,
               "founder_classes": [h["name"] for h in existing if h.get("founder")],
               "classes": classes}
        with open(args.emit_waterfall, "w") as f:
            json.dump(out, f, indent=2)
        pool_note = ("unallocated pool included as granted at the given strike"
                     if args.include_pool is not None else
                     "unallocated pool left out; rerun with --include-pool STRIKE to compare")
        print(f"\nWaterfall input written to {args.emit_waterfall} (exits at the total preference"
              f" stack of {money(stack)} and 0.5x, 1x, 2x, 5x post-money; {pool_note})."
              " Check each class's terms before running it.")
    print("\nCheck the documents' own definitions (fully diluted capitalization, Company"
          " Capitalization in each SAFE, note conversion terms) before relying on these numbers.")


WATERFALL_FIELDS = ("type", "invested", "price", "preference_base", "pref_multiple",
                    "participation", "cap_multiple", "cap_includes_dividends", "rank",
                    "conversion_ratio", "cumulative_dividend", "strike")
SERIES_FIELDS = ("pref_multiple", "participation", "cap_multiple", "cap_includes_dividends",
                 "rank", "cumulative_dividend", "conversion_ratio")


def waterfall_classes(d, existing, instruments, conv_shares, investors, price):
    """Build waterfall classes from the pro forma round."""
    series = d.get("new_series", {})
    classes = []
    for h in existing:
        if h.get("pool"):
            continue
        c = {"name": h["name"], "shares": h["shares"]}
        c.update({k: h[k] for k in WATERFALL_FIELDS if k in h})
        c.setdefault("type", "common")
        classes.append(c)
    for inst, sh in zip(instruments, conv_shares):
        c = {"name": inst["name"], "type": "preferred", "shares": sh, "invested": inst["amount"]}
        c.update({k: series[k] for k in SERIES_FIELDS if k in series})
        # YC Safe Preferred: preference based on the conversion price, i.e. the amount paid
        c["preference_base"] = sh * price if inst.get("full_preference") else inst["amount"]
        classes.append(c)
    for inv in investors:
        c = {"name": inv["name"], "type": "preferred", "shares": inv["amount"] / price,
             "invested": inv["amount"]}
        c.update({k: series[k] for k in SERIES_FIELDS if k in series})
        classes.append(c)
    return classes


# ---------------------------------------------------------------- SAFE stack

def cmd_safes(args):
    d = load_json(args.input)
    existing = d["existing"]
    e_total = sum(h["shares"] for h in existing)
    safes = d["safes"]
    post = [s for s in safes if s.get("cap") and s.get("type", "post") == "post"]
    other = [s for s in safes if s not in post]
    k = sum(s["amount"] / s["cap"] for s in post)
    if k >= 1:
        raise SystemExit("Post-money SAFEs claim 100% or more of the company; check the inputs.")
    total_after = e_total / (1 - k)

    print("# SAFE stack before a priced round\n")
    print("Each post-money SAFE owns amount / post-money cap of the company capitalization that"
          " includes all SAFEs; SAFEs do not dilute each other, so every new SAFE dilutes only"
          " existing holders.\n")
    rows = []
    for h in existing:
        rows.append([h["name"], f"{h['shares']:,.0f}", pct(h["shares"] / e_total),
                     pct(h["shares"] / total_after)])
    for s in post:
        own = s["amount"] / s["cap"]
        rows.append([f"{s['name']} ({money(s['amount'])} at {money(s['cap'])} post-money cap)",
                     f"{own * total_after:,.0f}", "-", pct(own)])
    rows.append(["**Total**", f"{total_after:,.0f}", "100.0%", "100.0%"])
    print(table(["Holder", "Shares (as converted at cap)", "Before SAFEs", "After SAFEs"], rows))
    print(f"\nTotal sold through post-money SAFEs: {pct(k)}.")
    founders = [h for h in existing if h.get("founder")]
    f_shares = sum(h["shares"] for h in founders)
    proposed = [s for s in post if s.get("proposed")]
    if proposed:
        k0 = k - sum(s["amount"] / s["cap"] for s in proposed)
        print(f"Without the proposed SAFE(s): {pct(k0)} sold"
              + (f"; founders {pct(f_shares * (1 - k0) / e_total)}" if founders else "") + ".")
    if founders:
        print(f"Founders: {pct(f_shares / e_total)} -> {pct(f_shares / total_after)} before any priced round.")
    if other:
        names = ", ".join(s["name"] for s in other)
        print(f"\nNot included (ownership depends on the next round's price): {names}."
              " Model them with the round subcommand.")
    print("\nA priced round dilutes everyone, including SAFE holders, and usually adds a pool"
          " increase; use the round subcommand for ownership after it.")


# ---------------------------------------------------------------- examples

EXAMPLES = {
    "waterfall": {
        "exits": [10_000_000, 30_000_000, 60_000_000, 150_000_000],
        "transaction_costs": 0,
        "carve_out_percent": 0,
        "founder_classes": ["Founders"],
        "classes": [
            {"name": "Founders", "type": "common", "shares": 6_000_000},
            {"name": "Employee options", "type": "common", "shares": 1_000_000, "strike": 0.25},
            {"name": "Seed", "type": "preferred", "shares": 1_000_000, "invested": 2_000_000,
             "pref_multiple": 1, "participation": "none", "rank": 2},
            {"name": "Series A", "type": "preferred", "shares": 2_000_000, "invested": 10_000_000,
             "pref_multiple": 1.5, "participation": "capped", "cap_multiple": 3, "rank": 1,
             "cumulative_dividend": {"rate": 0.08, "years": 3, "compound": False}},
        ],
    },
    "safes": {
        "existing": [
            {"name": "Founders", "shares": 9_000_000, "founder": True},
            {"name": "Unissued pool", "shares": 1_000_000, "pool": True},
        ],
        "safes": [
            {"name": "Existing SAFEs", "amount": 900_000, "cap": 9_000_000, "type": "post"},
            {"name": "Proposed SAFE", "amount": 600_000, "cap": 6_000_000, "type": "post",
             "proposed": True},
        ],
    },
    "round": {
        "pre_money": 16_000_000,
        "investment": 4_000_000,
        "target_pool_post_percent": 0.10,
        "pool_in_pre_money": True,
        "converting_in_pre_money": True,
        "existing": [
            {"name": "Founders", "shares": 8_000_000, "founder": True},
            {"name": "Issued options", "shares": 600_000},
            {"name": "Unissued pool", "shares": 400_000, "pool": True},
        ],
        "safes": [{"name": "Angel SAFE", "amount": 1_000_000, "cap": 10_000_000,
                   "discount": 0.2, "type": "post"}],
        "notes": [{"name": "Bridge note", "principal": 500_000, "interest_rate": 0.06,
                   "years": 1, "cap": 12_000_000, "discount": 0.2}],
        "investors": [{"name": "Lead", "amount": 3_500_000},
                      {"name": "Other investors", "amount": 500_000}],
        "new_series": {"pref_multiple": 1, "participation": "none", "rank": 1},
    },
}

FIELD_NOTES = {
    "waterfall": """Fields:
  classes[].type: "common" (founders, employees, option pool; optional strike) or "preferred"
  preferred: invested (or price x shares), pref_multiple (1 = 1x), participation:
    "none" | "full" | "capped" (+ cap_multiple = total return cap incl. preference;
    accrued dividends count toward the cap unless "cap_includes_dividends": false),
    rank (1 = paid first; equal ranks share pari passu), conversion_ratio (default 1),
    cumulative_dividend {rate, years, compound} (override with --dividend-years),
    extra_shares (penalty or bonus shares that add to the as-converted count but carry no
    preference), preference_base (original issue price x
    shares when it differs from the cash invested, e.g. a SAFE converting into full preferred)
  transaction_costs: fees or debt paid before equity; carve_out_percent: management carve-out
  founder_classes: class names summed into a founders row
Unissued pool: run once without it and once with it as a common class with an assumed
  strike when future grants change the answer.
Unconverted post-money SAFEs at a sale: model as preferred with invested = purchase amount,
  pref_multiple 1, participation "none", and shares = amount / cap x capitalization
  (the safes subcommand prints this share count).""",
    "safes": """Fields:
  existing[]: fully diluted shares (founders, options, unissued pool); "founder": true
  safes[]: amount, cap, type "post" (default), "proposed": true for a SAFE under discussion
    (the output then also shows the position without it). Pre-money, discount-only, and MFN SAFEs
    have no fixed ownership until the priced round; model them with the round subcommand.""",
    "round": """Fields:
  existing[]: shares on a fully diluted basis; mark "pool": true for unissued pool and
    "founder": true for founder holdings
  target_pool_post_percent: unissued pool required after the round (e.g. 0.10)
  pool_in_pre_money / converting_in_pre_money: whether the pool increase and converting
    SAFEs/notes are counted in the pre-money share count (the usual term sheet position)
  safes[]: amount, cap, discount (0.2 = 20%), type "post" (YC post-money) or "pre"
  notes[]: principal, interest_rate, years, compound, cap, discount, type "pre"|"post"
  investors[] (optional): name and amount for each new investor (must sum to investment)
  new_series (optional): terms of the new preferred for --emit-waterfall (pref_multiple,
    participation, cap_multiple, rank, cumulative_dividend). SAFEs and notes convert into a
    shadow series with the same terms but a preference based on the amount paid; set
    "full_preference": true on an instrument if it converts into the full new series.
  existing[] may carry waterfall fields (type "preferred", invested, pref_multiple, ...;
    "strike" for issued options) so --emit-waterfall can include earlier preferred series.
Pre-money caps here use pre-round capitalization including the pool increase; check each
instrument's own capitalization definition.""",
}


def cmd_example(args):
    if args.which == "antidilution":
        print("python3 scripts/deal_math.py antidilution --cp1 1.00 --new-price 0.50 \\\n"
              "  --new-shares 2000000 --pref-shares 1000000 --a-broad 10000000 --a-narrow 3000000",
              flush=True)
        print("\nFlags: --cp1 current conversion price; --new-price and --new-shares of the"
              " dilutive issuance; --pref-shares protected preferred; --a-broad / --a-narrow"
              " base A per the charter; --oip original issue price (default --cp1).", file=sys.stderr)
        return
    print(json.dumps(EXAMPLES[args.which], indent=2), flush=True)
    print("\n" + FIELD_NOTES[args.which], file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)

    w = sub.add_parser("waterfall", help="exit proceeds by share class")
    w.add_argument("--input", required=True, help="JSON file (or - for stdin)")
    w.add_argument("--exits", help="comma-separated exit values, e.g. 10M,50M,200M")
    w.add_argument("--dividend-years", type=float,
                   help="override the accrual period of every cumulative dividend")
    w.add_argument("--json", action="store_true", help="machine-readable output")
    w.set_defaults(func=cmd_waterfall)

    a = sub.add_parser("antidilution", help="anti-dilution adjustment comparison",
                       description="Run once per protected series with that series' own"
                                   " conversion price (a SAFE shadow series has a lower one and"
                                   " may not be triggered at all).")
    a.add_argument("--cp1", type=float, required=True, help="current conversion price")
    a.add_argument("--new-price", type=float, required=True, help="price of the dilutive issuance")
    a.add_argument("--new-shares", type=float, required=True, help="shares issued in that issuance")
    a.add_argument("--pref-shares", type=float, required=True, help="protected preferred shares")
    a.add_argument("--a-broad", type=float,
                   help="base A per the charter: NVCA broad-based counts common, preferred as"
                        " converted, and outstanding options and convertibles; check whether the"
                        " unissued pool and SAFE shadow series are included")
    a.add_argument("--a-narrow", type=float, help="narrow base (e.g. outstanding preferred or stock only)")
    a.add_argument("--oip", type=float, help="original issue price (default: cp1)")
    a.set_defaults(func=cmd_antidilution)

    r = sub.add_parser("round", help="priced round pro forma with pool and SAFEs/notes")
    r.add_argument("--input", required=True, help="JSON file (or - for stdin)")
    r.add_argument("--emit-waterfall", metavar="FILE",
                   help="write a waterfall input built from the pro forma cap table")
    r.add_argument("--include-pool", type=float, metavar="STRIKE",
                   help="with --emit-waterfall, add the unallocated pool as granted options")
    r.set_defaults(func=cmd_round)

    s = sub.add_parser("safes", help="ownership sold through post-money SAFEs before a priced round")
    s.add_argument("--input", required=True, help="JSON file (or - for stdin)")
    s.set_defaults(func=cmd_safes)

    e = sub.add_parser("example", help="print an input template")
    e.add_argument("which", choices=sorted(list(EXAMPLES) + ["antidilution"]))
    e.set_defaults(func=cmd_example)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
