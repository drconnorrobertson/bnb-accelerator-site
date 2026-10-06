# BNB Accelerator internal-link inventory and first mapping list

Prepared before any new content or internal-link edits for the second buyer-intent batch.
Baseline remote main: `438d2cb11e60d938562f098a86857f569c5b25cd`.

## Complete orphan list

**Zero true canonical orphans. Zero homepage-unreachable canonical routes.
Zero sitemap-only canonical routes.** There are no orphan URLs to promote.

The complete [public route inventory](orphan-audit-before/public-route-inventory.csv)
contains all 2,413 rendered HTML resources: 2,412 eligible self-canonical routes
and the excluded noindex `404.html` utility. The separate
[redirect exclusion list](orphan-audit-before/redirect-exclusions.csv) contains
all 277 configured redirect rules, including patterns; these are not orphan
content pages. No other rendered noindex, test or noncanonical HTML resource
was found in this build. Generator inputs and editorial records are excluded
from the public build rather than counted as pages.

## Discovery versus useful context

The graph counts distinct eligible same-site source URLs, excluding self links,
fragment-only anchors, nofollow anchors and outgoing links on nofollow pages.
It uses the deployed public-build transformations, including the first release's
disclosures and resource-link normalization. Homepage reachability is measured
by following this eligible graph, independently of XML sitemaps.

**1,215 eligible routes have zero structurally contextual inbound source URLs.**
That is a separate weak-linking screen, not an orphan count. The CSV includes
every such route and its current other inbound counts. "Contextual" here means
an anchor in a main-content paragraph or table, outside navigation, recognized
indexes, author blocks and related-reading callouts. Useful list-based links
can fall into the other-main category. The categories can overlap for one
source URL, so their counts should not be summed. Manual relevance and content
review remain necessary.

The full weak-linking inventory is deliberately **unreviewed / repair-first**.
A long page, a crawlable page or a generated sibling link does not establish
content quality. No bulk links or removals are proposed. Pages with contradictory
financial claims, generic matrix copy or unverified market/service claims should
be repaired before stronger pages point readers to them.

## Bounded contextual-link mapping, listed before implementation

These are useful existing-page relationships within the planned buyer-intent
cohort. They repair contextual weakness or connect distinct buyer questions;
none is presented as an orphan rescue. Each source and destination will be
reviewed or rewritten before the proposed link is applied. Existing links that
already serve the same question should be retained rather than duplicated.

| Destination URL / current title | Current inbound / contextual | Buyer intent and readiness | Relevant same-site source | Source GSC evidence actually supplied | Anchor and placement | Decision / reason |
|---|---:|---|---|---|---|---|
| [/guides/str-investment/beach-house/investment-cost/](https://www.bnbaccelerator.com/guides/str-investment/beach-house/investment-cost/) — Beach House STR Investment Cost Guide | 6 / 0 | Full cash to acquire and launch a coastal STR; generic worksheet needs a distinct cost ledger | [/pricing/](https://www.bnbaccelerator.com/pricing/) | Page clicks, impressions and position not supplied | “beach-house acquisition cash example” in the paragraph separating service fees from property cash | **Repair first, then link.** Do not send buyers to the current generic matrix copy |
| [/guides/str-investment/beach-house/furnishing-budget/](https://www.bnbaccelerator.com/guides/str-investment/beach-house/furnishing-budget/) — Beach House STR Furnishing Budget Guide | 6 / 0 | Room-level furnishing scope, installation and contingency; generic worksheet | [/guides/str-investment/beach-house/investment-cost/](https://www.bnbaccelerator.com/guides/str-investment/beach-house/investment-cost/) | Page: 0 clicks / 19 impressions / 7.74 average position | “itemized coastal furnishing budget” after the setup allowance in the cost ledger | **Repair both, then link.** Distinct detail behind one acquisition-cost intent owner |
| [/guides/str-investment/fourplex/break-even-occupancy/](https://www.bnbaccelerator.com/guides/str-investment/fourplex/break-even-occupancy/) — Fourplex STR Break-Even Occupancy Guide | 6 / 0 | Four-unit night inventory, contribution, mixed lease use and downside; generic worksheet | [/blog/airbnb-occupancy-rates-explained/](https://www.bnbaccelerator.com/blog/airbnb-occupancy-rates-explained/) | Page: 0 clicks / 44 impressions / 36.41 average position | “fourplex break-even occupancy worksheet” after the distinction between an occupancy forecast and the minimum paid nights needed | **Repair both, then link.** Forecast versus buyer cash threshold are separate questions |
| [/markets/chandler/](https://www.bnbaccelerator.com/markets/chandler/) — Chandler Short-Term Rental Investment | 4 / 3 | Parcel use and comparable-set screening; current generator repeats unsupported market figures and active-service claims | [/blog/arizona-str-investing/](https://www.bnbaccelerator.com/blog/arizona-str-investing/) | Page: 0 clicks / 7 impressions / 3.57 average position | “Chandler address-specific purchase checks” in an East Valley research-routing paragraph, preserving supported historical acquisition facts | **Repair both before linking.** Educational coverage must not certify active Chandler service or a return |
| [/answers/what-is-revpar/](https://www.bnbaccelerator.com/answers/what-is-revpar/) — What Is RevPAR? | 4 / 1 | Lodging revenue per available unit-night; add period/denominator and cost limits | [/blog/airbnb-occupancy-rates-explained/](https://www.bnbaccelerator.com/blog/airbnb-occupancy-rates-explained/) | Page: 0 clicks / 44 impressions / 36.41 average position | “RevPAR definition and worked comparison” beside the passage explaining why occupancy alone is insufficient | **Repair and keep or replace existing relevant link.** One definition owner; avoid duplicating the formula everywhere |
| [/blog/airbnb-occupancy-rates-explained/](https://www.bnbaccelerator.com/blog/airbnb-occupancy-rates-explained/) — Airbnb Occupancy Rates Explained | 22 / 7 | Paid nights, owner/maintenance blocks and seasonal forecasts; replace unsupported “realistic” ranges | [/answers/what-is-revpar/](https://www.bnbaccelerator.com/answers/what-is-revpar/) | Page: 0 clicks / 54 impressions / 20.13 average position | “reconcile paid, available and calendar nights” after the consistent-denominator comparison | **Repair and keep or replace existing relevant link.** Send denominator detail to the occupancy owner |
| [/pricing/](https://www.bnbaccelerator.com/pricing/) — What does BNB Accelerator cost? | 23 / 10 | Quote, deliverables and capital remaining after reserves; existing scope questions useful | [/guides/str-investment/beach-house/investment-cost/](https://www.bnbaccelerator.com/guides/str-investment/beach-house/investment-cost/) | Page: 0 clicks / 19 impressions / 7.74 average position | “request the actual service fee and scope” beside the excluded or separately quoted acquisition-service fee | **Improve and link.** A planning example supplies no BNB service quote |

The [25 supplied GSC source candidates](gsc-link-source-shortlist.json) are now
recorded with exact page metrics in the route inventory where a row was supplied.
All are sparse BNB signals; none is described as a high-traffic authority page.
Metrics not supplied, including pricing, remain blank. The observed query and
page samples are small prioritization clues, not demand proof or
a forecast of rankings. The supplied Sep 6–Oct 3 window has daily coverage only
from Sep 18; site totals were 4 clicks, 1,422 impressions and 32.84 average
position. Missing page metrics do not establish absent indexing.

The [source-candidate decision list](gsc-source-candidate-decisions.csv) evaluates
all 25 supplied GSC source URLs against the current inventory. The historical
`/blog/regulation-2025/` URL is excluded: it currently returns HTTP 308 to
`/regulations/`. The Vrbo-handoff source already links to the first release's
management guide; that useful link is retained. Other unrelated or unreviewed
sources are excluded from this bounded batch rather than forced into its links.

## Live checks before link edits

[Eleven sampled public responses](orphan-audit-before/live-samples.json) were
checked without submitting forms or changing settings. All six sampled buyer
pages return HTTP 200, have a matching self-canonical and index/follow meta
directive, have no X-Robots noindex header, and match the baseline public build
byte for byte. `/results/` redirects to `/case-studies/`; the historical 2025
regulation post redirects to `/regulations/`. Vercel's clean-URL behavior redirects
`/404.html` to `/404/`; that utility returns 200 with both meta and header noindex.
A nonexistent route returns a noindex 404. Utility aliases are not canonical
orphan content pages.

The existing content/schema/link/sitemap audit and public build pass. Targeted
parser checks passed for relative URLs, self fragments, uppercase nofollow,
related-reading versus contextual links and redirect patterns. These checks
establish the graph and sampled public eligibility; they do not establish
Google's indexing decisions or the relevance of every proposed destination.

## Reproduce and compare after the batch

```sh
node build_public.mjs
python3 audit_content.py
python3 _gen/audit_internal_inbound.py
```

Preserve the committed baseline inventory when making the after report. Report
actual true-orphan, reachability and weak-context counts separately. Verify
sampled live HTTP responses, self-canonicals and robots eligibility against the
baseline; a local graph alone is not a live indexing report.

## Implemented outcome, October 6, 2026

The eight pages were reviewed and rewritten before the seven listed
relationships were applied. See the [implementation and verification
record](buyer-intent-batch-two-review.md) and [complete after
inventory](orphan-audit-after/public-route-inventory.csv). The before files
above remain the delivered baseline.

| Measure | Before | After |
|---|---:|---:|
| Eligible self-canonical routes | 2,412 | 2,412 |
| True canonical orphans | 0 | 0 |
| Homepage-unreachable | 0 | 0 |
| Sitemap-only | 0 | 0 |
| Zero structurally contextual inbound | 1,215 | 1,213 |

Investment cost, furnishing budget and fourplex break-even gained contextual
sources. Chandler's rewritten guide also stopped promoting its unreviewed
agent derivative, which remains reachable but now has zero contextual sources.
That explains the net change of two routes. No new route or bulk linking was
introduced, and these structural changes supply no ranking or indexing result.
