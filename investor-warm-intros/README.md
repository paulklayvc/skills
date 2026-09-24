# Investor Warm Intros

An agent skill for founders who want warm introductions to fitting VCs and angels. It works with Claude Code, Codex, or another agent that supports skills.

## Install

```bash
npx skills add paulklayvc/skills --skill investor-warm-intros
```

Choose your agent during setup, then ask it to use `investor-warm-intros`. Add `-g` to install across all your projects. See the [full collection](../README.md) for the other skills.

## What it does

Your agent starts with your company, traction, background, network, and what you can offer others. It researches investor fit and selects from four routes:

1. **Portfolio founders** — build a relationship by helping a founder, then ask for an introduction when they know your work.
2. **Content and social presence** — publish useful research or operating lessons relevant to an investor's thesis.
3. **Help a portfolio company** — offer specific help through an investor who can connect you to the company.
4. **Investor-mentors** — seek advice, apply it, and show progress over time.

The output is a **fit snapshot**, a **ranked investor shortlist**, an **action plan with a timeline**, and the **messages or posts needed for the first steps**. Templates cover first touches, later intro requests, advice follow-ups, content ideas, and a forwardable company blurb.

Ask for the full plan or a focused route to one fund. Research depends on available web access; unverified information and fit mismatches are called out.

## Example prompt

```text
Use investor-warm-intros to help me prepare for a seed round in six months. Start with my company and background, then shortlist fitting investors and build a warm-intro plan with drafts for the first steps.
```

## Structure

```text
investor-warm-intros/
├── README.md                      # overview, installation, example prompt
├── SKILL.md                       # investor-fit workflow and four intro routes
└── references/
    └── message-templates.md       # message structures, examples, forwardable blurb
```
