# Decision-Maker Outreach

An agent skill for finding specific decision-makers (buyers, partners, execs, investors) and getting a warm conversation with them. It works for B2B sales and for B2C partnerships, with Claude Code, Codex, or another agent that supports skills.

## Install

```bash
npx skills add paulklayvc/skills --skill decision-maker-outreach
```

Choose your agent during setup, then ask it to use `decision-maker-outreach`. Add `-g` to install across all your projects. See the [full collection](../README.md) for the other skills.

## What it does

Your agent walks you through five stages:

1. **Define the ICP.** Role, company, trigger moment, pain, and budget owner.
2. **Customer development.** Talk to about 10 ICP-fit people and note the communities, events and names that keep coming up.
3. **Pick entry points.** Find natural, honest ways into the places where those people gather.
4. **Build relationships.** Make a good impression first, then drop one strong case and let them connect the dots.
5. **Growth hacks.** Niche communities, value-first offers (podcasts, reports, dinners), niche social networks, and good cold messages.

Ask for a full plan and it produces a **Reach Plan**: ICP, hypotheses, custdev script, scored entry points, pitch line, cold message drafts, and a 2-week action list.

## Structure

```
decision-maker-outreach/
├── README.md                     # overview, installation, example prompts
├── SKILL.md                      # workflow, guardrails, output format
└── references/
    └── playbook-assets.md        # question bank, templates, cold message examples
```

## Example prompts

- "I sell a compliance tool to mid-size European fintechs. How do I get in front of their Heads of Compliance?"
- "I run a B2C meditation app. Help me find partners who already have my audience."
- "Write a cold Telegram message to the CMO of a mobile gaming studio."
