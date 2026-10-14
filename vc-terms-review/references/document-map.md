# Document map

Where each term lives, what the model documents treat as the default, and the document-specific checks. Read the section for the documents in front of you; term-level standards and asks are in [term-benchmarks.md](term-benchmarks.md).

Contents: identifying the documents · US priced rounds (NVCA set) · SAFEs · convertible notes · lightweight seed documents · UK documents · continental Europe · side letters

## Identifying the documents

- Compare the documents with the model form they come from. A clause that departs from the model is where to look first; ask counsel for a redline against the model if one is not provided.
- A term sheet is mostly non-binding; the definitive documents control. Check that the definitive documents implement the term sheet and do not add terms it did not mention.
- Definitions decide outcomes. Read every defined term used in a material clause, even when the definition sits in another document.
- A typical US priced round has a term sheet, a restated charter (certificate of incorporation), a stock purchase agreement, an investors' rights agreement, a voting agreement, a ROFR and co-sale agreement, and often management rights letters, indemnification agreements, and side letters. A UK round usually has a term sheet, a subscription and shareholders' agreement (sometimes split), new articles of association, and a disclosure letter.

## US priced rounds: the NVCA document set

Most US venture rounds use the NVCA model documents or close derivatives. Current versions: Certificate of Incorporation (COI), Stock Purchase Agreement (SPA), and Investors' Rights Agreement (IRA) updated October 2025; Voting Agreement (VA) June 2026; Right of First Refusal and Co-Sale Agreement (ROFR) April 2026; Management Rights Letter (MRL) and Indemnification Agreement July 2020; Model Legal Opinion 2013. NVCA's model-documents page no longer lists a general VC term sheet; the NVCA 2020 Term Sheet is the latest, and its "Matters Requiring Preferred Director Approval" list now sits in COI §3.3.9.

The models offer bracketed alternatives and explain them in footnotes. Many thresholds are blanks, so "standard" usually means the structure, not a number. Section numbers below refer to the current models; derived documents renumber, so search by the term name. Charter references are to Article Fourth, Part B unless noted.

### Where the six founder risks live

| Risk | Where to look |
|---|---|
| Conflicts and information flow | "Competitor" definition (IRA §1, ROFR §1); Competitor gating of information (IRA §3.1), inspection (§3.2), observer (§3.3), and pro rata (§4.1) — all bracketed, not default; confidentiality carve-outs (IRA §3.5); "Right to Conduct Activities" (IRA §5.8); corporate opportunity waiver (COI Art. Eleventh); MRL board-materials access; transfers of investor shares to competitors (not prohibited; IRA §6.1) |
| Rights that can change | IRA §6.6 amendments and waivers, including the bracket that treats a deal-specific pro rata waiver as applying "in the same fashion"; COI §8 waiver of preferred rights; anti-dilution waiver (COI §4.4.2); DLE waiver (§2.3.1); mandatory conversion by vote (§5.1); VA §7.8 and ROFR §6.8 amendments |
| Cap table and shareholder data | IRA §3.1 (cap table with quarterly reports; upload to a portfolio-management platform on request), §3.5 confidentiality, §3.7(b) cap-table statements; ROFR on founder transfers and exempt transfers; platform terms sit outside the documents |
| Control | COI §3.2 board elections and "Requisite Directors"; COI §3.3 stockholder vetoes; COI §3.3.9 board-level vetoes; VA §1.2 designation, §1.4 removal, §3 drag-along, §4.2 irrevocable proxy |
| Liquidation preferences | COI §2.1–2.2 (non-participating, participating, capped; pari passu by default), §2.3 deemed liquidation events and escrow allocation; VA §3.3 and ROFR §2.2(d)(ii) route stock sales through the waterfall |
| One-sided protection | Full ratchet (COI §4.4.4 alternative); cumulative dividends (COI §1); redemption (COI §6); participating preferred (COI §2.2); pay-to-play and tranche penalties (COI §5A, SPA §1.2); founder re-vesting (term sheet "Founders' Stock"; COI §3.3.9(g)); CEO-seat and "Qualified Key Holder" mechanics (VA §1.2) |

### Term sheet

- Only no-shop and confidentiality are binding by default; a footnote warns that a "non-binding" term sheet can still create a duty to negotiate in good faith under Delaware law. Check which sections are binding, the no-shop length, and an expiry date. If expenses are binding, they should be capped and payable only at closing or if the company walks away.
- The pre-money includes an unallocated pool sized as a percentage of the post-money. Model the shuffle and tie the pool to a hiring plan.
- If SAFEs or notes convert in the round, check what the term sheet says about their shadow series, whether their conversion price below the round price could trigger anti-dilution (conversions should be exempted securities), and whether SAFE holders count toward Requisite Holder and Major Investor thresholds.
- Binding confidentiality should allow sharing the terms with existing investors (whose consent is often needed), advisers, and counsel.
- Founder asks at this stage: 1x non-participating, pari passu; non-cumulative dividends; broad-based weighted average with the full carve-out list; no redemption; no founder re-vesting; drag-along requiring a common or founder vote; Competitor definition and confidentiality limits settled now rather than in the definitive documents.

### Certificate of incorporation

- **Dividends (§1).** Three alternatives: as-converted only; non-cumulative "when, as and if declared"; cumulative "Accruing Dividends". Red flags: cumulative or compounding dividends, accruals added to the liquidation or redemption amount, payment in shares on conversion.
- **Liquidation preference (§2.1–2.2).** Default lists non-participating first: the greater of the multiple of the original issue price or the as-converted amount, pari passu across series. Participating and capped ("Maximum Participation Amount") are alternatives; seniority requires redrafting.
- **Deemed liquidation events (§2.3).** Mergers where pre-deal holders lose a majority, and sales or exclusive licenses of all or substantially all assets. Since October 2025 a pure preferred financing is not a DLE, and share transfers by holders are excluded. Red flags: DLE definitions that catch financings or stockholder transfers; a waiver threshold one fund controls. Escrow allocation: "Initial Consideration" spreads escrow losses pro rata; "Additional Consideration" guarantees the preferred its full preference and puts escrow losses on common — ask for the former. Non-cash consideration valued by a board including a Preferred Director gives investors a veto on valuation.
- **Board elections (§3.2).** Preferred elects its seats, common elects its seats, both elect at-large directors; class-elected directors are removable without cause only by that class. "Requisite Directors" may require a majority of, or each, Preferred Director. Red flags: more preferred than common seats, no common-elected seat, Requisite Directors defined as each Preferred Director.
- **Stockholder vetoes (§3.3).** Requisite Holders approve liquidation or DLEs, adverse charter or bylaw changes, senior (or pari passu, if bracketed) securities, changes to authorized shares, redemptions and dividends, non-wholly-owned subsidiaries, and board size. Red flags: the "adversely affects" qualifier removed, "pari passu" added so every future equal-ranking round needs consent, series-by-series vetoes for every new round, a threshold one fund meets alone.
- **Board-level vetoes (§3.3.9).** Bracketed list requiring Requisite Directors: debt above a threshold, equity plan changes, loans, guarantees, hiring and compensation of the CEO and direct reports, budget, equity grants to 1%+ holders without standard vesting, committees, large contracts, long leases. With Requisite Directors defined as each Preferred Director, one VC director vetoes budget, hiring, and compensation. Item (g) blocks founder acceleration and non-standard vesting. Ask for financial items with realistic thresholds and a simple board majority.
- **Anti-dilution (§4.4.4).** Default broad-based weighted average: CP2 = CP1 × (A + B) / (A + C), with A including common, options, and convertibles; the footnote ranks broad-based as most founder-friendly and full ratchet as most investor-friendly. Full ratchet can be time-limited. Exempted securities (§4.4.1) should be Board-approved, without caps or Preferred Director approval hiding a veto over pool top-ups.
- **Mandatory conversion (§5.1).** High qualified-IPO price or proceeds floors, or per-series conversion consent, give investors an IPO veto.
- **Pay-to-play (§5A).** Non-participating holders convert to common in a qualified financing; Requisite Holders can switch it off for a deal. Generally aligns investors to fund; check that waivers cannot selectively protect insiders.
- **Redemption (§6).** Default: not redeemable. The alternative gives investors a put after a date in three annual installments, with interest escalating on non-payment; footnotes note investors sometimes take board control on default. Any redemption right is investor-leaning; FMV pricing, escalating interest, or board control on non-payment are red flags.
- **Waivers (§8).** Any preferred right can be waived for all holders by the vote required to amend it.
- **Corporate opportunity waiver (Art. Eleventh).** The company renounces opportunities presented to non-employee directors and preferred holders unless presented solely in their director capacity; the footnote calls it "very pro-investor". Narrow it to opportunities outside the company's line of business or delete it, especially next to board or observer access.

### Stock purchase agreement

- **Reps and warranties.** Company-only, knowledge-qualified where the footnotes offer it; no founder reps or founder signature in the model. Founder personal reps, uncapped or joint liability, and M&A-style indemnities or escrows are red flags. The model has no indemnification article; reps survive closing without a stated limit, so a 12–18 month survival period is a reasonable ask.
- **Tranches (§1.2).** New October 2025 tranche mechanics: milestones judged by the Board including Preferred Directors or waivable by investors; defaulting investors convert at a penalty. Red flags: investor-judged milestones, a large share of the round in later tranches at today's price, material-adverse-change conditions. Ask for objective milestones, a board-majority determination, and a short outside date.
- **Conditions.** Legal opinion (often skipped or narrowed at early stages), board composition, indemnification agreements, management rights letter.
- **Fees.** Company pays lead investor counsel up to a cap; uncapped fees payable even if the deal does not close are off-market.

### Investors' rights agreement

- **Major Investor (§1).** Thresholds set so that small holders do not get information and pro rata rights. "Affiliate" includes funds with the same manager, which matters for sister funds holding competitors.
- **Information (§3.1).** Annual and quarterly financials, cap table, budget; monthly reporting and audits are bracketed options. Ask to keep the Competitor proviso, quarterly reporting, and unaudited statements until the board decides.
- **Inspection (§3.2) and observer (§3.3).** The company can withhold trade secrets, privileged material, and conflicted or competitive information; keep all exclusions and require a written confidentiality undertaking from observers.
- **Confidentiality (§3.5).** Use only to monitor the investment; disclosure allowed to professionals, prospective purchasers, and "[existing or prospective]" affiliates, partners, and stockholders. The footnotes call the "prospective" carve-out pro-investor and suggest barring disclosure to competitors. Ask to delete "prospective", bar disclosure to competitors and portfolio companies, and make investors liable for their recipients.
- **Pro rata (§4.1).** Major Investors only, fully diluted denominator, with over-allotment; options to terminate rights of investors who do not take their full share and to issue first and offer catch-up later. Super pro rata and pro rata for all holders complicate later rounds.
- **Right to conduct activities (§5.8).** Funds may invest in competitors and are not liable for helping them, subject to confidentiality and directors' fiduciary duties. Ask for disclosure of competitive holdings and recusal of investor directors and observers from competitive discussions.
- **Amendments (§6.6).** Requisite Holders amend generally; Major Investor rights by a majority of Major Investors; individual consent only when a change does not apply to all investors "in the same fashion". The pro rata bracket lets a deal-specific waiver bind everyone, optionally with a catch-up. A Key Holder bracket protects founders from disproportionate changes. Check whether one fund alone forms each majority.
- **Other.** Registration rights are low practical risk. Non-compete covenants are bracketed and unenforceable in California. Investor-counsel reimbursement in a sale and early sharing of management packages are bracketed. Indemnitor-of-first-resort language (§5.7) is standard for fund-appointed directors.

### Voting agreement

- **Board (§1.2).** Seats for named investors, a common director, the CEO, and a mutual director. Red flags: the common seat tied to a founder's continued employment ("Qualified Key Holder"), the CEO seat replacing a founder seat (a fired founder-CEO also loses the board seat), and a mutual director chosen by an investor-majority board. Ask for common seats designated by share ownership and independent directors approved by the common directors.
- **Removal (§1.4).** Designated directors are removed by their designators; "for cause" removal by an investor majority or removal on loss of employment are red flags.
- **Drag-along (§3).** Trigger by a preferred percentage, optionally with a common or Key Holder majority and the Board; the footnote says the drag is not meant to give investors a unilateral right to force a sale. Protections: title and authority reps only, several not joint, liability capped at proceeds, same consideration per class. The model exempts only stockholders who are not officers, directors, or employees from non-competes, so founder-employees are not protected by default. Ask for a common or founder approval prong, extend the covenant protection to founders, and consider a minimum price or preference-multiple floor.
- **Proxy (§4.2).** Limit to board-composition votes or a company-officer holder.
- **Amendments (§7.8).** The model requires the company, the Requisite Holders, and (bracketed) Key Holders holding a set percentage; Key Holder consent is not needed for changes that do not affect them differently. If the documents omit Key Holder consent, founders can lose their board-seat and drag protections by investor vote. Founder consent that disappears when founders leave or fall below a low ownership level is a red flag.

### ROFR and co-sale agreement

Restricts only Key Holders: company and then investors have a right of first refusal, and investors may tag along on founder sales. Founder asks: an all-or-nothing forfeiture bracket, shorter timelines, and a de minimis liquidity carve-out. Investors' own shares are generally freely transferable, including to competitors, unless the IRA says otherwise.

### Management rights letter and indemnification

- The MRL lets funds meet ERISA venture-capital-operating-company requirements; routine to grant. Clause 3 (board materials for funds without a seat) lacks the IRA observer exclusions for conflicts and competitors. Grant clauses 1–2 only, or conform the exclusions, and limit letters to funds that need them.
- The indemnification agreement is standard for directors. The bracket indemnifying the fund itself is a point the NVCA working group calls not established as market; delete it or limit it to advancement tied to board service.

## SAFEs

Baseline: the Y Combinator post-money SAFE (v1.2, February 2023). YC currently publishes three US forms — valuation cap only, discount only, and uncapped MFN — plus an optional pro rata side letter. YC removed the cap-and-discount form in 2021, so a "YC cap and discount SAFE" is a modified or obsolete form. Every YC form states that neither party has modified it except to fill in blanks; if that sentence is missing or the text differs, redline the document against the YC form.

- **Ownership:** with a cap, ownership sold equals purchase amount ÷ post-money valuation cap, measured against "Company Capitalization" — all shares, issued and promised options, the existing unissued pool, and all SAFEs and notes, but not the pool increase made in the priced round (unless promised options exceed the existing pool). Pre-money SAFEs are legacy: their capitalization excludes other SAFEs and includes the new pool increase.
- **Stacking:** post-money SAFEs do not dilute each other; every new SAFE dilutes only founders, employees, and other common. Report the total ownership sold before the priced round with `deal_math.py safes`, and model conversion in the priced round with `deal_math.py round`. As a rule of thumb (not market data), totals above roughly 20–25% deserve attention.
- **Conversion:** automatic at the next equity financing, with no minimum size, into the greater of standard preferred at the round price or "Safe Preferred" at the cap price. Safe Preferred has rights identical to the new series — including its liquidation multiple, participation, seniority, and dividends — but price-based amounts are calculated on the SAFE's conversion price, so the preference is based on the amount paid rather than the round price. The SAFE holder therefore gets no windfall from a low cap, but does inherit any heavy terms in the new series; include converted SAFEs in the waterfall with those terms (`deal_math.py round --emit-waterfall` does this).
- **Sale or IPO:** the holder gets the greater of the purchase amount or the as-converted amount. Dissolution: purchase amount, junior to debt, equal to preferred and other SAFEs, senior to common.
- **MFN:** applies only to later convertible securities, as a one-time election to adopt the whole later instrument. Close and fund low-cap SAFEs before issuing an uncapped MFN SAFE, or the MFN holder inherits the low cap.
- **Pro rata side letter:** a right to buy the holder's pro rata share in the financing where the SAFE converts, ending at that closing. Grant it to meaningful checks; it adds dilution in the conversion round.
- **No rights before conversion:** SAFEs carry no voting rights, no maturity, and no interest.
- **Amendment:** the company and a majority-in-interest of SAFEs with the same cap and discount can amend; a holder's purchase amount never changes without its consent. Transfers need company consent except to affiliates.
- **Lower-priced new SAFEs:** a new SAFE at a lower cap than earlier ones can trigger MFN rights in earlier SAFEs or their side letters, letting those holders re-price; check before agreeing.

Red flags:

| Deviation from the YC form | Why it hurts |
|---|---|
| The "not modified" sentence removed or text changed beyond the blanks | Hidden changes; request a redline |
| Board seat, observer, veto, or broad information rights inside the SAFE | YC advises keeping the SAFE unmodified and putting agreed rights in a side letter; in Europe, consent rights appeared in only 15% of convertibles and board rights in under 10% (Orrick Deal Flow 6.0) |
| Side letter changing economics (extra discount, lower cap, higher preference) | Not covered by the MFN carve-out, so it triggers MFN rights for earlier holders |
| Low cap combined with a high discount | Effectively a very large discount to the priced round |
| Conversion into full standard preferred at the cap price (no Safe Preferred) | Liquidation preference above the amount invested (a $3M cap into a $10M pre-money round gives about 3.3x) |
| MFN covering priced-round terms, options, or debt, or allowing repeated or cherry-picked elections | Broader than YC's one-time MFN on later convertibles |
| Maturity date, interest, redemption, or repayment on demand | Turns the SAFE into debt |
| Cash-out amount above 1x, or priority equal to debt | Departs from the form's non-participating, preferred-equivalent treatment |
| Minimum financing size or holder option not to convert | The YC form converts automatically in any equity financing |
| Labeled post-money but capitalization defined differently, especially including the round's pool increase | Ownership no longer equals amount ÷ cap; founders bear the new pool |
| Pro rata in every future round, super pro rata, or rights surviving the conversion round | The YC side letter covers only the conversion round |
| Mixing notes with SAFEs, or pre-money with post-money SAFEs | Notes rank ahead of SAFEs; mixed SAFE types make the cap table uncertain |

## Convertible notes

Baseline: Cooley's Series Seed notes (unsecured; prepayment only with majority holder consent).

| Term | Baseline | Red flag |
|---|---|---|
| Interest | 2–8%; the most common rate is 8% or below (WSGR 1H 2026) | Double-digit or compounding interest |
| Maturity | 12–24 months or more; repayment only on request of the majority holders; extensions are common | Short maturity with an individual holder's demand right |
| Conversion at maturity | Into common or a new preferred series at the cap, by majority election | Holder-only option to convert at a low valuation into senior preferred with full rights |
| Qualified financing | Threshold of one to two times the note principal | Threshold so high that the notes never convert automatically |
| Discount and cap | 15–25% discount; caps in about half of post-seed notes (WSGR 1H 2026) | Low cap plus high discount converting into full preferred |
| Change of control | Repay principal and interest, sometimes with a premium, or convert at the cap | 2x or higher payout that blocks small exits or acqui-hires |
| Security | Unsecured | Security over assets or IP, personal guarantees |
| Amendment | Majority of holders can amend and extend | No majority amendment clause, so a holdout can block an extension |
| Extras | Warrants and pro rata are uncommon; pro rata, if any, applies to the next round only | Warrants (when they appear on post-seed bridges, coverage is often above 25%), rights surviving beyond the next round, noteholder board seats |

## Lightweight seed documents

The Series Seed documents are the clean benchmark for a priced seed round: 1x non-participating preference; dividends only pari passu with common; no price-based anti-dilution in the original (Cooley's fork adds optional broad-based weighted average); seven protective provisions requiring a majority of preferred, lapsing below 25% of the original preferred; a drag-along requiring the common majority, the Series Seed majority, and the Board, with limited, several, capped liability; quarterly and annual unaudited financials to major purchasers only, withheld from competitors; founders on four-year vesting with double-trigger acceleration; flat investor legal fees. A priced seed round that adds participation, a preference above 1x, cumulative dividends, redemption, full ratchet, or a long veto list is above this baseline.

## UK documents

Baseline: the UK Private Capital (formerly BVCA) model documents for early-stage investments, relaunched February 2023 and revised February 2025: summary of terms, subscription agreement with a disclosure letter, shareholders' agreement, articles, and a registration rights agreement. They are drafted for Series A and described as not appropriate for seed rounds. The documents require a free login; positions below come from UK Private Capital's own summary and law-firm summaries.

| Topic | Model position | Market and negotiation notes |
|---|---|---|
| Warranties | Given by the company only; 18-month limitation period (bracketed) | Founder-backed warranties remain common: 29% of UK deals and 39% at pre-seed and seed (Orrick Deal Flow 6.0). Where founders give them, caps are typically a multiple of salary and claims are time-limited; flag uncapped or joint founder warranties |
| Investor consents | Investor Majority Consent and Investor Director Consent lists in a schedule, streamlined in 2023 | UK consent lists are longer than US protective provisions and often reach operating decisions (budget, hiring above a salary, contracts, borrowing). Push operating items to board level with materiality thresholds; check whether one investor alone is the Investor Majority |
| Class rights | Varying a class's rights needs a majority of the class (previously more than 75%) | — |
| Founder leavers | 48-month vesting, optional one-year cliff. Good leavers keep vested shares; bad leavers lose all shares, including vested ones (converted to deferred shares). Bad leaver triggers: gross misconduct, serious criminal conviction, breach of non-compete. Resignation was removed as a bad leaver trigger in 2025 | Harsher than US reverse vesting, which only lets the company buy back unvested shares. Red flags: resignation or a broad residual definition as bad leaver, vested shares bought back at nominal value |
| Founder board seats | Founder appointment rights only while employed or engaged | Founders hold two seats on average; founder appointment rights in 88% of European deals |
| Drag-along | Liability capped at proceeds; no business warranties or non-competes from dragged holders; escrow and earn-outs allowed | Founder veto over the drag in 43% of European seed deals and 50% of Series A |
| Pre-emption | Investors or Major Investors; disapplied by Investor Majority consent; no super pro rata on new issues | Statutory pre-emption is disapplied in the articles |
| Anti-dilution | Broad-based weighted average by default; waivable by the Investor Majority | Broad-based 80%, full ratchet 0% in 2025 European deals; narrow-based or full ratchet is a red flag in the UK too |
| Liquidation preference | Non-participating (greater of preference or as-converted); alternative waterfalls for EIS and VCT investors | 1x non-participating 77%, participating 1% (Europe 2025). Participating preference and cumulative dividends appear in the pre-2023 BVCA term sheet; treat them as red flags today |
| Information | Accounts and management reports; may be limited to Major Investors; board may withhold information from strategic investors' directors and observers (2025) | Monthly reporting in 59% of European seed deals |
| Restrictive covenants | Founders give non-compete, non-solicit, and confidentiality undertakings; breaching the non-compete makes a founder a bad leaver | Often one to two years. The UK government announced on 2026-10-09 that it will legislate to limit non-competes; whether this reaches shareholder-agreement covenants is unsettled |
| Other | 180-day IPO lock-up cap; investors may hold competing investments | Legacy forms charged monitoring and transaction fees to the company and break fees to founders; flag them |

**SEIS and EIS.** For three years, SEIS and EIS shares must be ordinary shares with no preferential right to assets on a winding up, no redemption right, and no preferential dividend that is variable or cumulative. They therefore cannot carry a liquidation preference; UK seed rounds often use ordinary shares and move to preferred shares at Series A. Advance subscription agreements qualify only if they cannot be refunded, varied, or assigned, bear no interest, and have a longstop date (HMRC expects no more than six months). SAFEs and convertible loan notes generally fail the no-refund test. If the founder needs SEIS or EIS relief, check every instrument and preference against these rules.

## Continental Europe

Documents vary by country and local corporate law changes how terms work (notarization, statutory pre-emption, mandatory board structures). Use the European data in [market-data.md](market-data.md) and the UK guidance above as the closest benchmark, and flag terms whose effect depends on local law. Founder-backed warranties are far more common in Germany (84% of deals) than in the UK.

## Side letters

Ask to see every side letter, including those with other investors. Typical content: management rights, information, observer seats, pro rata, MFN, and regulatory covenants. Red flags: rights that contradict or go beyond the main documents (vetoes, super pro rata, information rights for an investor with a competing position), side letters hidden from other investors, and MFN clauses that import every later concession. Schedule them, have company counsel review them, and ask for them to end at the next priced round.
