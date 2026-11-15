# Comparison and alternatives improvements - November 15, 2026

Buyers arriving on an alternatives page previously met a question and a long
explanation before reaching other named options. The updated pages show a named
research shortlist near the top, identify the work to compare, and link to the
established direct-comparison owner. Direct comparisons surface the proposal
records needed to make the decision. All 24 provider paths retain their existing
URLs, including established blog comparison owners.

The two hubs now organize all 24 paths by acquisition/brokerage, education,
ownership/investment models, and data/research. They retain links to existing
proposal worksheets, pairwise comparisons and market research. The unordered
ItemList represents the visible directory, not a quality ranking. No customer
scores, review ratings, new synonym pages or performance guarantees were added.

## Evidence

`search-baseline.json` records the authenticated Search Console browser export
on November 15, selected period Last 3 months; the chart spans September 18 to
November 13. It includes the exported rows for this cohort and original
publication timestamps. Missing export rows do not establish zero visibility.

Priority observations included the Short Term Shop alternatives owner (137
impressions, no clicks, position 1.26), BNB Mastery alternatives (33 impressions,
one click, position 2.61), Techvestor alternatives (20 impressions, no clicks,
position 4.65), and Kleer Circle's blog comparison (49 impressions, three clicks,
position 8.88). These are small samples and period averages, not proof of fixed
live ranks or a forecast of gains. Prompt-shaped search rows were excluded from
the query selection rather than used to claim ordinary customer demand.

## Official provider pages rechecked in Chrome on November 15

- The Short Term Shop: https://theshorttermshop.com/how-to-buy-a-short-term-rental/
- BNB Mastery: https://bnbmastery.com/
- Techvestor: https://www.techvestor.com/
- Rent to Retirement: https://www.renttoretirement.com/turnkey-properties
- Kleer Circle: https://kleercircle.com/
- Elk Ridge Investments: https://www.elkridgeinvestments.com/service/
- STR Search: https://strsearch.com/
- STR Insights: https://www.strinsights.com/introduction

The changes summarize published scope without adopting providers' returns,
guarantees or tax promises. Elk Ridge's current page describes an active
partnership with operating support, so the older passive/sponsor-only framing
was corrected in both owners. Other providers retain their existing dated
source analysis; a refreshed navigation or title does not claim their terms
were freshly verified.

## Maintenance and validation

`python3 scripts/refresh_comparison_intent.py` is idempotent and runs before the
production build. It refreshes 50 existing owners, preserves original
publication dates, and advances modification/sitemap dates only for this
substantive cohort. It does not touch the property noindex selection policy.

Run the repository content audit, full release build, existing nonhome/blog
checks, and `python3 scripts/check-comparison-intent.py public`. Verify the
directory -> alternatives -> direct comparison -> pricing/application path
in desktop and mobile browser views. After release, compare a settled 28-day
window with the preceding equivalent window for the recorded owners; inspect
query, device and country context before attributing any CTR change to titles.
