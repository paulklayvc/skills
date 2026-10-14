# VC Terms Review

An agent skill for founders who received a term sheet, SAFE, or financing documents from a VC or angel and want to know how good the terms really are before they sign. It works with Claude Code, Codex, or another agent that supports skills.

Built on [my post on X about the top mistakes founders make when dealing with VCs](https://x.com/PaulKlayVC/status/2110000227138589171), the NVCA, YC, Series Seed, and UK model documents, and current deal-term data from Cooley, Wilson Sonsini, Carta, PitchBook-NVCA, Osler, and Orrick.

## Install

```bash
npx skills add paulklayvc/skills --skill vc-terms-review
```

Choose your agent during setup, then ask it to use `vc-terms-review`. Add `-g` to install across all your projects. See the [full collection](../README.md) for the other skills.

## What it does

Your agent reads all the documents together, extracts every material term with the exact clause, and compares it with the model documents and current market data for your stage and jurisdiction. It checks the six areas where founders get hurt most:

1. **Conflicts of interest** — what investors can see and whom they can share it with, especially when they back your competitors.
2. **Investor rights that can change** — which rights a majority can amend or waive without each investor's consent.
3. **Cap table and shareholder data** — who can access it and contact your shareholders.
4. **Control** — who appoints and removes directors, which decisions need investor approval, and how that changes after future rounds.
5. **Liquidation preferences** — who actually gets paid in an exit, across all existing preferred series.
6. **One-sided protection** — combinations that remove the investor's downside while keeping the upside, especially with founder-removal rights.

It runs the math with a bundled calculator: exit waterfalls, the option pool shuffle, SAFE and note conversion, and down-round anti-dilution.

**What you get:**

- **Verdict** — Clean, Acceptable with fixes, Negotiate before signing, or Serious concerns.
- **Ranked issues** — each with the clause, its practical effect, its cost in numbers, the market benchmark, and what to ask for.
- **Term table** — every material term rated against the standard.
- **Numbers** — ownership after the round and who gets what at different exit values.
- **Control map and negotiation plan** — what to push on, what to trade, and what to accept.
- **Questions for your lawyer** and investor diligence, including reference calls with founders whose companies struggled.

It is not legal advice; it prepares you for the conversation with your lawyer and your investor.

## Structure

```
vc-terms-review/
├── README.md                       # overview, installation, example prompts
├── SKILL.md                        # workflow, six risk areas, output format, guardrails
├── references/
│   ├── document-map.md             # where each term lives in NVCA, SAFE, note, and UK documents
│   ├── term-benchmarks.md          # standard positions, red flags, and asks for each term
│   ├── market-data.md              # deal-term statistics by stage, with sources and dates
│   ├── founder-risk-cases.md       # the real cases behind the six risk areas
│   └── sources.md                  # model documents, data reports, and term guides
└── scripts/
    └── deal_math.py                # waterfall, round pro forma, anti-dilution calculator
```

## Example prompts

- "Use vc-terms-review to check this Series A term sheet. Our cap table is attached. How good are these terms, and what should we push back on?"
- "An investor wants a SAFE with a side letter giving them a board observer seat and full information rights. Is that normal?"
- "We have two offers: $20M pre with a 1x non-participating preference, or $28M pre with a 2x participating preference. Which is better for us at different exit values?"
