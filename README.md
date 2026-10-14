# Agent skills from a VC

I'm [Paul Klay](https://x.com/PaulKlayVC), a venture capitalist. These are the agent skills I actually use: to research companies, find opportunities, reach decision-makers, and build relationships with customers, partners, and investors. I'm sharing the workflows behind how I work and how I've joined projects myself.

Use them with Claude Code, Codex, or another agent that supports skills.

## Skills

| What you want to do | Skill |
|---|---|
| Get warm introductions to VCs and angels for a fundraise | [Investor Warm Intros](./investor-warm-intros) |
| Check whether a VC's term sheet or financing documents are good before you sign | [VC Terms Review](./vc-terms-review) |
| Reach buyers, partners, or executives | [Decision-Maker Outreach](./decision-maker-outreach) |
| Attract customers and partners with little upfront cash | [Bootstrap Growth](./bootstrap-growth) |
| Find a role or consulting opportunity by proving your value | [High-Leverage Job Hunt](./high-leverage-job-hunt) |

### [Investor Warm Intros](./investor-warm-intros)

Build a path to investors who fit your company through portfolio founders, useful content, help for portfolio companies, or investor-mentors. Built for founders preparing a fundraise or seeking an introduction to a specific fund.

**What you get:**

- **Investor-fit snapshot** — how your sector, stage, traction, geography, and background match investors' current theses and the founder profiles they tend to back.
- **Ranked investor shortlist** — roughly 5–10 fitting funds or angels, with sourced theses, relevant partners, portfolio companies, and a recommended introduction route.
- **Warm-intro action plan** — concrete next steps and a timeline for the routes that fit what you can offer and whom you already know.
- **Messages and content drafts** — first-touch messages, later intro requests, advice follow-ups, relevant posts, and a forwardable company blurb as needed for your chosen routes.

Ask for a full fundraising outreach plan or a focused route to one fund. The skill flags fit mismatches and unverified information instead of inventing investor relationships.

### [VC Terms Review](./vc-terms-review)

Check a term sheet, SAFE, or full set of financing documents before you sign. Compares every material term with the NVCA, YC, Series Seed, and UK model documents and current deal-term data, and runs the math on who gets paid in an exit.

Built on [my post on X about the top mistakes founders make when dealing with VCs](https://x.com/PaulKlayVC/status/2110000227138589171): conflicts of interest, investor rights that can change without your consent, cap table access, control, liquidation preferences, and terms that leave investors protected and founders exposed.

**What you get:**

- **Verdict** — Clean, Acceptable with fixes, Negotiate before signing, or Serious concerns.
- **Ranked issues** — each with the clause, its practical effect, its cost in numbers, the market benchmark, and what to ask for.
- **Term table** — every material term rated against the standard for your stage and jurisdiction.
- **Numbers** — ownership after the round, the option pool shuffle, SAFE conversion, and who gets what at different exit values.
- **Control map and negotiation plan** — who controls the board now and after future rounds, what to push on, and what to accept.
- **Questions for your lawyer** and investor diligence, including reference calls with founders whose companies struggled.

Ask for a full review of your documents or a quick check of one clause. It is not legal advice; it prepares you for the conversation with your lawyer and your investor.

### [Decision-Maker Outreach](./decision-maker-outreach)

Find the people who can say yes, learn where they spend time, and build a natural path to a conversation. Built for B2B sales, B2C partnerships, customer interviews, and founder-led outreach.

**What you get:**

- **Ideal customer profile (ICP)** — a specific role and company profile, trigger moment, current problem, and budget owner.
- **Customer interview kit** — 3–5 assumptions to validate, 8–12 tailored questions, a response log, and a plan for landing the first 10 conversations.
- **Scored entry-point table** — communities, events, and other places to meet your targets, assessed for density, quality, access, and intimacy, with guesses distinguished from validated options.
- **Relationship and outreach kit** — a concise “what I do” line, a case story, relevant ways to offer value first, and 1–3 draft messages for your strongest channels.
- **Two-week action plan** — a short, dated list of next steps.

Ask for the full **Reach Plan**, or just the piece you need: a customer profile, communities to research, or a first message.

### [Bootstrap Growth](./bootstrap-growth)

Design founding customer, influencer, and ambassador partnerships when acquisition cash is limited. Match the offer to what each partner values and what the team can deliver.

**What you get:**

- **Ranked partner shortlist** — researched candidates with sources, evidence of fit, and realistic contact routes.
- **Partner offer** — a concrete exchange with clear contributions and obligations for both sides.
- **Sustainable incentives** — access, referrals, revenue share, and selective shared upside tied to meaningful results.
- **Economic check** — delivery costs, commissions, cash timing, and break-even based on supplied numbers or labeled assumptions.
- **Bounded pilot** — target partners, tracking, success criteria, stop criteria, and a decision date.

Ask for a full acquisition plan with researched partners, a specific partner shortlist or offer, or a review of one deal.

### [High-Leverage Job Hunt](./high-leverage-job-hunt)

Find companies where your experience can solve a specific business problem, reach the founder, and propose a small pilot without a large upfront payment. Built for senior roles, partnerships, cofounder opportunities, and consulting work.

Distilled from [my original post on X](https://x.com/PaulKlayVC/status/2101356736560951576), which reached **425k+ views**.

**What you get:**

- **Positioning brief** — your specific edge, the evidence behind it, questions to validate it with past colleagues, and claims to drop.
- **Scored target table** — researched companies ranked on seven criteria, each scored 0–2: a visible gap, proof the approach works, fit with your track record, revenue impact, founder access, speed of decision-making, and whether anyone owns the problem.
- **Outreach kit for each company** — a warm-intro request and a direct message grounded in that company's opportunity.
- **One-page call plan** — an opening line, 5–7 questions in order, relevant cases to show, what to avoid, and how to close.
- **One-page pilot proposal** — a hypothesis, scope, timeline, success metrics, price, and terms for both success and failure.

Start at the stage you need. The skill asks for your context, researches the companies, and produces the relevant artifacts.

## Get started

Just send this to Claude Code, Codex, or another agent with terminal access:

```text
Run `npx skills add paulklayvc/skills` and help me choose and set up the skills for this agent.
```

Your agent can handle the setup for you.

### Prefer the terminal?

```bash
npx skills add paulklayvc/skills
```

Choose the skills and your agent during setup. Add `-g` to install across all your projects.

To install a specific skill:

```bash
npx skills add paulklayvc/skills --skill investor-warm-intros
```

```bash
npx skills add paulklayvc/skills --skill vc-terms-review
```

```bash
npx skills add paulklayvc/skills --skill decision-maker-outreach
```

```bash
npx skills add paulklayvc/skills --skill high-leverage-job-hunt
```

```bash
npx skills add paulklayvc/skills --skill bootstrap-growth
```

### Try it

**Investor Warm Intros:**

```text
Use investor-warm-intros to help me prepare for a seed round in six months. Start with my company and background, then shortlist fitting investors and build a warm-intro plan with drafts for the first steps.
```

**VC Terms Review:**

> Use vc-terms-review to check this Series A term sheet against market terms. Our cap table is below. Tell me how good the deal is, model what we get at different exit values, and what we should push back on.

**Decision-Maker Outreach:**

> Use decision-maker-outreach to help me reach Heads of Compliance at mid-size European fintechs. Start with my ideal customer profile, then build a Reach Plan with entry points, first messages, and a two-week action list.

**Bootstrap Growth:**

> Use bootstrap-growth to design an acquisition pilot for our AI implementation agency. Assume service businesses with 10–50 employees, a $3,000 project price, two existing clients, capacity for two new clients per month, and a $500 monthly acquisition budget. Propose clear offers, sustainable referral incentives, and a 60-day pilot. Flag additional assumptions.

**High-Leverage Job Hunt:**

> Use high-leverage-job-hunt to help me find companies where my experience is valuable. Start with my positioning, then build a scored target list and outreach kits for the strongest matches.

Already have a call booked? Ask for a call plan. Already have interest? Ask for a pilot proposal.

Use them, adapt them, and make them your own.
