# Term benchmarks

For each term: the standard position for a US priced round, what is investor-leaning but seen, red flags, and what to ask for. Items listed as red flags are terms to push back on; rate each one on the SKILL.md scale by its impact in this deal — off-market when it is uncommon but limited in effect, red flag when it shifts substantial economics or control. Prevalence figures and their sources are in [market-data.md](market-data.md); document locations and model-form alternatives are in [document-map.md](document-map.md). UK and European norms differ on several points — see the jurisdiction notes at the end.

Contents: valuation and option pool · SAFEs and convertible notes · liquidation preference · dividends · anti-dilution · redemption · pay-to-play · conversion and IPO · protective provisions · board · drag-along · founder vesting and removal · information, observers, and confidentiality · competing investments · pro rata · amendments and waivers · transfers and secondaries · reps, warranties, and indemnities · process terms · warrants, tranches, and milestones · combinations · side letters · jurisdiction notes

## Valuation and option pool

- **Standard:** pre-money on a fully diluted basis, including the option pool increase and conversion of SAFEs and notes. Median dilution per round is under 20% (seed and Series A about 19%, Series B about 13%, Carta Q2 2026).
- **Option pool shuffle:** a pool increase counted in the pre-money dilutes only existing holders. Effective pre-money = headline pre-money − value of the pool increase − value of converting SAFEs and notes, all at the round price; `deal_math.py round` also shows the figure excluding the existing unallocated pool. Say which definition you use.
- **Pool sizing:** size the pool to an 18-month hiring plan — each planned role with a seniority-appropriate grant plus a small refresh reserve — not to a convention ([Alder VC](https://aldervc.com/blog/startup-option-pool/)). 10–15% of post-money is most common, with 10% the single most frequent size (HSBC Innovation Banking 2026 term sheet guide, via [HSBC](https://www.hsbcinnovationbanking.com/hk/en/resources/understanding-employee-option-pools)); Osler's Canadian 2025 median available pool after closing was 8% at seed and 7.5% at Series A. A 20% requirement at seed is usually too large. Existing unallocated options should count toward the target.
- **Red flags:** a pool far larger than the hiring plan; pool counted in the pre-money and also a large post-money top-up; "fully diluted" defined to include shares that do not exist yet in a way that lowers the price.
- **Ask:** a hiring plan–based pool; any excess counted post-money; or a higher headline valuation to offset the shuffle. Compare competing offers on founders' fully diluted ownership after closing, not on headline valuation, and ask for a pro forma cap table as a term sheet exhibit.
- **Warrants:** warrants in a priced round lower the effective valuation; negotiate the price instead.
- **Rating price terms:** valuation and caps are commercial terms. Judge them against the company's own earlier pricing, the founder's alternatives, and market ranges for the stage, sector, and geography; call a price "investor-leaning" with the reason rather than "off-market" unless comparable data supports it. A new instrument priced below the company's earlier SAFEs or round signals a lower value to future investors and can trigger MFN re-pricing for earlier holders.

## SAFEs and convertible notes

- **Standard:** YC post-money SAFE with a valuation cap and no discount (about 64–73% of SAFEs in 1H 2026); when a discount appears, 20% is the norm. MFN-only SAFEs are for cases with no agreed price. Notes: interest at or below 8%, 12–24 month maturity, majority-holder amendment, unsecured.
- **Total sold:** add up amount ÷ post-money cap across all outstanding post-money SAFEs with `deal_math.py safes`. As a practitioner rule of thumb, not a market statistic, more than about 20–25% sold before the first priced round leaves founders thin for later rounds.
- **Side-letter rights for SAFE investors:** pro rata in the conversion round is reasonable for a meaningful check; observer seats and monthly reporting are investor-leaning — acceptable for a large early check with confidentiality, exclusion, and termination protections, ending at the priced round. US prevalence data for these rights is not available; in Europe, director or observer rights appeared in 9% of convertible rounds and information rights in 41% (Orrick Deal Flow 6.0).
- **Red flags:** MFN covering priced rounds or "any terms granted to any investor", or allowing term-by-term cherry-picking; pro rata in every future round; low cap combined with a high discount; maturity, interest, or repayment rights in a SAFE; any change from the YC text that is not shown in a redline. See the SAFE and note tables in [document-map.md](document-map.md).
- **Earlier instruments:** check whether earlier SAFEs or their side letters have MFN clauses that a new, cheaper SAFE would trigger.
- **Amendments:** YC SAFEs can be amended by the company and a majority-in-interest of SAFEs with the same cap and discount (most Canadian SAFEs and notes use majority amendment, per Osler 2025); a holder with its own terms usually controls its own instrument, and side letters change only with both parties' consent.

## Liquidation preference

- **Standard:** 1x non-participating (greater of the original price or the as-converted amount), pari passu across series. About 96% of US deals are non-participating and about 96% are 1x (Cooley Q2 2026; WSGR 1H 2026).
- **Investor-leaning but seen:** seniority of the new series (16% of WSGR Series B+ deals in 1H 2026; far more in down rounds); capped participation in difficult rounds.
- **Red flags:** any multiple above 1x; full participation; participation with a high cap; cumulative dividends added to the preference; a new senior series stacked on existing preferences; DLE definitions broad enough to trigger the preference in financings or partial sales.
- **Why it matters:** combined preferences can wipe out common in exits below or near the post-money valuation. Always model the full stack at several exit values, including below the last post-money.
- **Existing investors:** a new senior series usually needs consent from earlier preferred holders under their protective provisions; check, and use their position in the negotiation.
- **Ask:** 1x non-participating, pari passu. If participation is unavoidable, a cap of 3x total or less (caps are typically 3–5x and include the preference); if seniority is unavoidable, concede it to keep 1x non-participating and resist stacking in later rounds.

## Dividends

- **Standard:** non-cumulative, only when declared, or none; most startups never pay dividends.
- **Red flags:** cumulative or accruing dividends (about 1–4% of deals), especially compounding and added to the liquidation or redemption amount. 8% compounding for five years adds about 47% to the preference.
- **Ask:** non-cumulative, as declared, pari passu with common.

## Anti-dilution

- **Standard:** broad-based weighted average (98% in WSGR 1H 2026), with a full list of exempted issuances (employee equity, conversions, approved strategic and debt-related issuances).
- **Red flags:** full ratchet (about 1%), even time-limited; narrow-based weighted average; exemptions capped or requiring Preferred Director approval; ratchets tied to milestones.
- **Why it matters:** full ratchet reprices the investor's entire investment to any lower price, and the extra shares come from common. Model it with `deal_math.py antidilution`.
- **Ask:** broad-based weighted average with the broadest base and Board-approved exemptions.

## Redemption

- **Standard:** none. Present in about 5–7% of deals.
- **Red flags:** investor put after a fixed period at original price plus accrued dividends; fair-market-value pricing; escalating interest or board control on non-payment. Redemption turns equity into a debt-like claim that can force a sale or recapitalization. Under Delaware law redemptions can be paid only from legally available funds, which is why investors add penalty interest or control triggers.
- **Ask:** delete; if unavoidable, a long period (seven years or more), installments, payable only from legally available funds, no penalty interest, no control shift.

## Pay-to-play

- **Seen:** about 8% of deals overall (Cooley Q2 2026), far more in down rounds.
- **Founder view:** usually aligns investors to support future rounds; it hurts investors who do not follow on, not founders. Check that the waiver mechanism cannot selectively protect insiders.

## Conversion and IPO

- **Standard:** optional conversion at any time; automatic conversion at a qualified IPO or by majority preferred vote.
- **Red flags:** high IPO price or proceeds floors, or series-by-series conversion votes, which give a single investor an IPO veto.

## Protective provisions (investor vetoes)

- **Standard:** a single preferred class vote for fundamental matters: liquidation or sale, charter changes adverse to the preferred, senior securities, changes to share capital, dividends and redemptions, board size, material debt.
- **Investor-leaning but seen:** separate series votes in later rounds; debt thresholds.
- **Red flags:** operational vetoes over the budget, hiring, firing and pay of executives, spending above low thresholds, new lines of business, or commercial contracts; vetoes over any charter change without an adverse-effect qualifier; board-level approvals requiring each investor director.
- **Investor-leaning, common:** a veto over securities that rank "pari passu" with the preferred as well as senior ones (every future round then needs consent); a lead that meets the voting threshold alone, which is normal at seed and Series A — what matters is what the threshold controls.
- **Ask:** fundamental matters only, a class vote, realistic dollar thresholds, and a Board majority (not each investor director) for operating decisions; a sunset when the preferred falls below a share of the originally issued amount (Series Seed uses 25%).

## Board

- **Standard at Series A:** five seats with two investor directors, two common (often including the CEO), and one independent agreed by both sides; or three seats with two common and one investor at seed. These are practitioner norms and NVCA examples; no US survey tracks board composition (Osler's Canadian 2025 data shows an average of 4.9 directors and common losing its majority after Series A).
- **Red flags:** investors appointing a majority, including via an "independent" they choose; the common seat tied to a founder's continued employment; investor director removal rights over common designees.
- **CEO seat:** a seat for the current CEO is standard (NVCA). The problem arises when it is the founder's only route to the board: removing the founder as CEO then also removes them as director. Ask for a separate seat designated by common holders.
- **Investor-leaning:** an investor observer on top of its board seats.
- **Simulate:** board composition after the next two rounds if each new lead takes a seat.
- **Ask:** common or founder seats designated by share ownership, an independent approved by common directors, and a board size that keeps common at least equal to investors.

## Drag-along

- **Standard:** triggered by the Board, the majority preferred, and a majority of common (often common held by employee founders); sellers give only title and authority reps, several not joint; liability capped at proceeds; same consideration per class.
- **Red flags:** triggered by investors alone; no common or founder approval; no minimum price or preference floor in an early sale; founders required to give broad reps, uncapped indemnities, or multi-year non-competes.
- **Watch:** a common approval prong limited to common held by current employees: a founder who leaves loses the vote but is still dragged. Ask for founders' shares to count regardless of employment.
- **Ask:** a common or founder approval prong, the model protections, a minimum price floor where possible, and no new restrictive covenants for founders beyond their existing agreements.

## Founder vesting and removal

- **Standard:** founders' existing vesting continues with credit for time served; double-trigger acceleration on a change of control is common and reasonable.
- **Red flags:** full re-vesting from closing without credit; repurchase of unvested shares at the lower of cost or fair market value on any termination; single "cause" definitions controlled by investors; performance milestones that let investors replace the CEO or take extra equity; founder board seats lost on termination.
- **Ask:** credit for time served, double-trigger acceleration, repurchase only of genuinely unvested shares at fair value for good leavers, a narrow "cause" definition, and no automatic CEO removal or equity transfer tied to metrics.
- **Tax:** re-vesting already-vested founder shares can have tax consequences (for US founders, whether a new 83(b) election is needed); flag it for counsel.

## Information, observers, and confidentiality

- **Standard:** annual and quarterly financials and the budget to Major Investors above a meaningful threshold; inspection rights subject to confidentiality; information rights withheld from competitors.
- **Investor-leaning but seen:** monthly reporting; an observer seat for a lead that has no board seat. Observers owe no fiduciary duties, so their access depends entirely on contractual confidentiality and exclusion rights.
- **Watch:** the October 2025 NVCA investors' rights agreement expanded the carve-out that keeps large venture funds out of the "Competitor" definition, so a fund holding a competing stake can still receive information. Read the definition against the investor's actual portfolio.
- **Red flags:** information rights for every holder; KPI, pipeline, or roadmap packages without confidentiality limits; confidentiality carve-outs allowing disclosure to portfolio companies or "prospective" limited partners; observers without confidentiality undertakings or exclusion rights for competitive or privileged matters; management rights letters that give board materials without those exclusions.
- **Ask:** a meaningful Major Investor threshold, quarterly reporting, a competitor exclusion, confidentiality without portfolio-company carve-outs, observer exclusion rights, and recusal from competitive discussions.

## Competing investments and corporate opportunities

- **Standard in the NVCA forms:** funds may invest in competitors and are not restricted by the agreement, subject to confidentiality and directors' fiduciary duties. Founders cannot usually remove this entirely.
- **Red flags:** acknowledgments that release investors from liability for use of company information or for helping competitors without the confidentiality and fiduciary carve-backs; a corporate opportunity waiver covering opportunities in the company's own line of business; no disclosure of existing competitive investments.
- **Ask:** disclosure of current competitive holdings, information barriers and recusal, a competitor exclusion for information and observer rights, and a narrow corporate opportunity waiver.

## Pro rata

- **Standard:** Major Investors may buy their pro rata share of future rounds, with customary exclusions; rights end at IPO or sale.
- **Off-market:** super pro rata (more than the investor's share); rights for all holders; a right of first refusal to lead or match the next round, which deters new leads.
- **Ask:** pro rata for Major Investors only; use-it-or-lose-it; no super pro rata or rights to lead or match.

## Amendments and waivers

- **Standard:** most rights can be amended or waived by a defined majority of preferred, but changes that treat an investor differently need that investor's consent. Founders' protections should need founder consent.
- **Red flags:** a single fund that forms the majority alone; any provision, including individual investors' rights, amendable by the majority without a "same fashion" or disproportionate-effect protection; founder protections amendable without founder consent; side letters granting rights that other investors cannot see.
- **Watch:** "spring-back" clauses that restore waived pro rata rights when any investor receives allocation, and promises about rights made in negotiations or side letters rather than the agreement. Both caused the Valar Atomics–Day One dispute (see [founder-risk-cases.md](founder-risk-cases.md)).
- **Map:** for each important right, who can change it after closing and whether the founder can block it.

## Transfers and secondaries

- **Standard:** company and investor right of first refusal and co-sale on founder transfers, with exceptions for estate planning and small transfers; investors' shares are mostly freely transferable.
- **Red flags:** total bans on founder secondaries or investor approval of any founder sale; no restriction on investors transferring to competitors; no company control over shareholder data used for secondary solicitations.
- **Ask:** a de minimis liquidity carve-out, short timelines, and company approval or a right of first refusal on transfers to competitors.

## Reps, warranties, and indemnities

- **Standard US:** company reps only, knowledge-qualified, without founder liability or an indemnity article.
- **UK:** the current model documents have company-only warranties, but founder-backed warranties still appear in about 29% of UK deals (39% at seed); where founders give them, expect caps (typically a multiple of salary) and time limits.
- **Red flags:** founder personal reps with joint and several, uncapped liability; long survival; M&A-style indemnities or escrows in a financing.
- **Ask:** company reps only; if founders must give warranties (common in the UK and Germany), cap them, time-limit them, and allow disclosure against them.

## Process terms

- **Binding confidentiality:** should allow sharing terms with existing investors, advisers, and counsel; existing investors' consent is often needed.
- **No-shop:** usually 30–60 days (Brad Feld describes 45–60 as typical; Osler's Canadian 2025 average exclusivity was 43 days). Longer periods, automatic renewal, no release if the investor changes terms, or obligations to disclose competing bidders' identities and terms are investor-leaning. The no-shop should end if the investor re-trades material terms or misses the closing date.
- **Expenses:** company pays the lead's counsel up to a cap; uncapped fees or fees payable if the deal fails are off-market.
- **Conditions:** due diligence at the investor's "sole discretion" plus a long no-shop gives the investor a free option; ask for a short timeline and an expiry date. "Partnership approval" as a condition means the fund has not approved the deal yet. Settle founder employment terms before signing.

## Warrants, tranches, and milestones

- **Red flags:** warrants or extra shares issued to investors for free when metrics are missed; tranches whose milestones the investor alone judges; a large share of the round deferred at today's price; milestone failure triggering CEO replacement. Evaluate these together with preferences, anti-dilution, and redemption: together they can shift most of the downside to founders.
- **Ask:** objective milestones decided by a board majority, a short outside date, and no penalty equity.

## Combinations to check together

1. High valuation + preference above 1x or participating + full ratchet: founders are underwater in any sale below the last post-money.
2. Pool increase + SAFEs and notes converting in the pre-money: the effective price is well below the headline.
3. Investor board majority + CEO-only common seat + founder re-vesting + broad "cause": founder removal becomes cheap.
4. Investor backing a direct competitor + board or observer seat + broad information rights + a carve-out from "Competitor": information leakage risk.
5. Rights amendable by a majority without disproportionate-effect protection + spring-back or side-letter promises: dispute risk.
6. Investor-only drag-along + large senior preference stack: a forced sale that pays common nothing.
7. Return guarantee or redemption + full ratchet + extra equity + founder removal right: the investor keeps the upside with little downside.
8. Full ratchet + SAFEs or notes converting below the round price, or penalty shares issued inside the ratchet window: the ratchet may fire on the company's own conversions unless they are exempted securities.
9. A deemed-liquidation definition covering financings or a "series of transactions": preferences can be triggered by ordinary fundraising.

## Side letters

Common for management rights, information, pro rata, and observer seats. Ask to see every side letter, including those with other investors; MFN clauses can import side-letter rights into later instruments.

## Jurisdiction notes

- **UK (UK Private Capital, formerly BVCA, model documents):** economics match US norms — 1x non-participating preference and broad-based weighted-average anti-dilution are the defaults, and full ratchet did not appear in 2025 European data. The differences are in control and founder terms: longer investor consent lists reaching operating decisions, good and bad leaver provisions under which a bad leaver can lose vested shares, founder warranties in a minority of deals, and founder non-competes. SEIS and EIS shares cannot carry a liquidation preference, redemption, or preferential cumulative dividends, so UK seed rounds often use ordinary shares. See [document-map.md](document-map.md).
- **Continental Europe:** documents vary by country and local corporate law changes how terms work. Use the European data in [market-data.md](market-data.md); flag terms whose effect depends on local law.
