# Second buyer-intent batch: implementation and review evidence

Eight existing pages now have distinct buyer questions, worked hypothetical
calculations and document checks. Seven contextual relationships from the
delivered list-first mapping are implemented. No routes were added. The first
release's case-study caveats, seller-income, DSCR, permit-transfer, reserves,
launch-delay and management guides remain byte-identical.

Baseline remote main: `438d2cb11e60d938562f098a86857f569c5b25cd`. This work is in
draft PR 2 for independent review; the implementation has not been merged or
published to production. See the preserved [before inventory and proposed
mapping](internal-linking-plan.md) and the [after inventory](orphan-audit-after/public-route-inventory.csv).

## Intent owners and distinct questions

1. `/guides/str-investment/beach-house/investment-cost/`: **How much cash does a
   beach-house STR purchase require?** Own acquisition cost. Use an all-in
   sources-and-uses ledger and separate the earnest-money credit from total
   invested cash. An assumed $800,000 purchase with 25% down needs $200,000 down,
   $28,000 closing/prepaid cash, $18,000 immediate repairs, $42,000 furnishing
   allowance, $5,000 launch, $30,000 operating reserve and $12,000 deductible
   liquidity: **$335,000** total committed cash. A $20,000 deposit credited at
   closing produces a **$208,000 closing wire**, not a second $20,000 cost.
   Service fees and unquoted extras remain separate. Require a lender/settlement
   ledger, STR-use insurance and flood/wind terms, inspection bids, legal-use
   file and dated furniture quotes. Do not present the example as a price range
   or a current coastal return.
2. `/guides/str-investment/beach-house/furnishing-budget/`: **What is inside the
   setup allowance?** Own room-level furnishing scope, not acquisition cost.
   Four bedrooms at an assumed $4,000 each plus $6,500 living/dining, $3,500
   outdoor, $3,500 kitchen/linens, $2,000 technology/safety and $4,500 freight/
   installation sum to **$36,000**; a 10% contingency gives **$39,600**.
   Capacity must come from legal-use evidence. Distinguish buying from installation
   acceptance, duplicate stock and delay replacement. Request an included-item
   inventory if the seller offers furnishings; title and value need their own
   evidence. This independent quote example is not a BNB design price.
3. `/guides/str-investment/fourplex/break-even-occupancy/`: **How many paid
   unit-nights cover the building's cash obligations?** Own multifamily
   break-even. Four units with 355 available nights each have **1,420 unit-nights**,
   rather than 365 building nights. At assumed $150 realized ADR, 20% revenue-linked
   fees and $30 variable cost, each paid unit-night contributes **$90**. Annual
   debt $72,000, tax/insurance $14,000, fixed utilities/common services $6,000
   and replacement reserve $6,000 total **$98,000**: round required paid nights
   up to **1,089**, or **76.7%** of available inventory. At $135 ADR the threshold
   becomes **1,257 / 88.5%**. Losing another 90 unit-nights moves the original
   threshold to **81.9%**. With one unit leased and an assumed $17,280 contribution
   after incremental leased-unit costs not already in the fixed stack, the three
   STR units need **897 of 1,065 available unit-nights / 84.2%**. Legal unit use,
   leases and lender treatment must be verified individually; this is not DSCR
   qualification or a market forecast.
4. `/markets/chandler/`: **Can this Chandler address fit a buyer's use and
   downside plan?** Own local purchase screening. Remove inherited unsupported
   $695K/$9.6K/12–16% averages and definitive active-service language. Cite the
   city license workflow, then ask for buyer-specific eligibility, HOA documents,
   actual emergency coverage, insurance and tax setup. Review same-capacity
   comparables near the actual trip destination, not a Phoenix-wide average.
   An independent hypothetical cash ledger of $162,500 down, $22,500 closing,
   $12,500 repairs, $35,000 furniture, $4,500 launch and $28,000 reserve is
   **$265,000**. An assumed weak month with 12 nights at $160, 18% revenue-linked
   charges, $22 night-variable costs and $4,400 fixed cash obligations loses
   **$3,089.60** before any additional replacement funding. Neither calculation
   certifies Chandler demand, a lending quote, coverage or a return.
5. `/blog/arizona-str-investing/`: **Which local file should an Arizona buyer
   assemble?** Support local intent owners; avoid copying the Chandler math.
   Route the Chandler subquestion to its own canonical. Distinguish statewide
   educational coverage, address-specific rules, current service availability
   and historical company acquisition stories. Preserve supported acquisition
   evidence; remove unsupported aggregate returns or forecasts if present.
   Request 12 monthly reservation and expense periods and an independent fallback
   use before picking a city. Reuse the first release's seller-income, permits,
   DSCR, reserves and manager handoff guides instead of recreating them.
6. `/answers/what-is-revpar/`: **What does RevPAR mean for a whole-property
   rental buyer?** Own the definition. Specify lodging revenue / available
   unit-nights, equivalent to realized ADR × paid occupancy only with matching
   periods and denominators. A whole house is one rentable unit, not one unit per
   bedroom. Exclude pass-through taxes/cleaning and future unearned bookings.
   Over 30 available nights, 18 paid nights at $200 yield **$120 RevPAR**; 24
   nights at $160 yield **$128**. With 20% distribution/management charges and
   respective night-variable costs of $25 and $40, their contributions before
   fixed costs, debt and reserves are **$2,430 versus $2,112**. Higher RevPAR alone
   does not establish higher owner cash flow. Link denominator and underwriting
   questions to their owners rather than turn the definition page into a full
   buying guide.
7. `/blog/airbnb-occupancy-rates-explained/`: **How do paid, available and
   calendar nights reconcile?** Own denominator/seasonality. In an assumed
   30-night month with six owner and four maintenance blocks, 16 paid nights are
   **80% of 20 available nights** and **53.3% of calendar nights**. Both should
   stay visible. An independent four-quarter example totals 365 calendar nights,
   346 available, 190 paid and **$36,145 lodging revenue**, yielding **54.9%
   available-night occupancy** and **52.1% calendar utilization**. Use weighted
   totals; no unsupported “good occupancy” range. Buyer forecast, break-even
   threshold, earned results and booked future nights are separate records.
8. `/pricing/`: **Does the service scope fit the buyer's cash and responsibilities?**
   Own quote and fit. Keep the existing useful scope/refund/vendor questions.
   An assumed $200,000 available less $165,000 property commitment and $25,000
   preserved reserve leaves **$10,000 headroom for the actual service quote and
   all still-unquoted extras**. It is not a published service price or a minimum
   client capital requirement. Require written price, milestones, exclusions,
   authority and failure/termination remedies; name retained buyer decisions.

## Public sources and evidence limits

- [Chandler short-term rental licensing](https://www.chandleraz.gov/business/tax-and-license/short-term-rental): city workflow reviewed Oct 6, 2026. It lists a city license, state tax license, county registration, neighbor notice, emergency information and advertisement requirements. Check actual current eligibility and ownership changes; do not promise timing or approvals.
- [Arizona Revised Statutes 9-500.39](https://www.azleg.gov/ars/9/00500-39.htm): reviewed Oct 6, 2026. State restrictions on municipal regulation coexist with specified local requirements and exceptions. The guide sends readers to current local instructions and address-specific evidence rather than certifying a parcel or HOA use.
- [CFPB Closing Disclosure explainer](https://www.consumerfinance.gov/owning-a-home/closing-disclosure/): cash to close is separate from total closing charges and reflects money already paid and credits. Use the closing professional's actual form for a financed purchase; loan documentation can differ by product.
- [FloodSmart / NFIP](https://www.floodsmart.gov/): standard homeowners policies generally exclude flood damage. A coastal buyer needs the actual insured rental use, coverages, deductibles and exclusions, not a generic premium assumption.
- [Amadeus RevPAR definition and formula](https://www.amadeus-hospitality.com/insight/what-is-revpar-formula-calculate/): lodging revenue per available room or ADR multiplied by occupancy, with costs outside the metric. The whole-listing unit-night example above is our explicit STR adaptation.
- [Public acquisition/process library](https://www.bnbacceleratorreviews.co/case-studies) and [Sedona closing-balance story](https://www.bnbacceleratorreviews.co/case-studies/sedona-az-2025-46): publicly fetched Oct 6, 2026. The company-operated library reports purchase and coordination records. The Arizona guide preserves the Sedona tracker’s $993,000 purchase, November 21, 2025 closing field and $25,000 seller concession, with the story’s insurance, lender/title and final-wire coordination. A tracker marked closed is not independent deed or credit-application evidence. The story supplies no verified rental income, rental return or buyer tax outcome.
- Existing first-release public evidence links and caveats remain the source for reported acquisition/process stories. Neither the historical evidence nor this educational Arizona coverage establishes present acquisition-service availability. No Colorado page was expanded.

## Source precedence and scoped regeneration

`_gen/buyer_intent.py` owns exactly these eight routes. The shared `tpl.page`
consults the reviewed payload only for an exact route match, preventing legacy
investor, blog and local renderers from restoring generic copy. The late market
enhancer skips reviewed market routes. Tests exercise those source priorities
and verify that an unreviewed route still uses its original renderer input.

`_gen/buyer_intent_inputs.py` owns the explicit invented numbers and independent
Decimal arithmetic. `_gen/refresh_buyer_intent.py` refreshes only the eight
existing pages and their lastmod fields in four sitemap segments. Repeating the
refresh produces identical bytes. It preserves current shared headers, footers,
hashed assets and the three existing Article publication dates (Arizona August
11, occupancy August 10 and RevPAR August 15, 2026). Other reviewed pages receive
an update date without an invented original publication date. Chandler's old
Service/areaServed schema is replaced with educational WebPage/FAQ metadata.

Tables use the existing contained scroll design with a keyboard-focusable,
named region. Page titles, descriptions, hero summaries, lead copy, examples,
document lists and FAQs serve each route's distinct question. No shared CSS,
JavaScript, application destination or tracking configuration changed.

## Implemented contextual relationships and measured change

| Source | Destination | Purpose |
|---|---|---|
| Pricing | Beach-house investment cost | Separate the service quote from property cash |
| Beach-house investment cost | Beach-house furnishing budget | Replace the setup allowance with an itemized scope |
| Occupancy | Fourplex break-even | Separate a demand forecast from a cash threshold |
| Arizona overview | Chandler | Route local address checks to their intent owner |
| Occupancy | RevPAR | Add rate to a consistently defined occupancy metric |
| RevPAR | Occupancy | Reconcile available, paid and calendar nights |
| Beach-house investment cost | Pricing | Request the actual service fee and deliverables |

Existing relevant links were refined instead of duplicated. Supporting links
refer to the first release's reviewed diligence guides and public sources.

Both reports contain 2,412 eligible self-canonical routes and one excluded
noindex 404 utility; 277 redirect rules are listed separately. True canonical
orphans, homepage-unreachable routes and sitemap-only routes remain **zero**.
The structurally zero-contextual screen changes from **1,215 to 1,213**:
investment cost gains two distinct contextual source URLs, furnishing gains
one, and fourplex break-even gains two. These are the three routes moving out
of that screen. The revised Chandler guide no longer promotes its unreviewed
`/markets/chandler/airbnb-real-estate-agent/` derivative, which moves from one
contextual inbound source to zero while retaining other links and homepage
reachability. The net improvement is two routes, not seven orphan rescues.

The automated readiness column remains a conservative unreviewed screen; this
document records the manual review of these eight routes. Counts measure
structure, not content quality, Google indexing or ranking. Supplied GSC metrics
are preserved as sparse observations; missing metrics remain blank.

## Verification

- Full content, metadata, internal-link, schema, redirect and sitemap audit:
  2,412 routes pass; 277 redirects resolve.
- Public build: 2,522 files, matching 2,412 sitemap routes; internal editorial
  and generator records stay outside public output.
- Nine focused buyer-intent checks: independent arithmetic, fractional-night
  round-up and infeasible thresholds, denominators and periods, Chandler claim
  limits, seven contextual relationships, legacy and late-generator precedence,
  publication/design/prior-page preservation, distinct prose and byte-identical
  regeneration.
- Eight first-release buyer-evidence checks pass; prior reviewed case/hub,
  management, financing and application files remain byte-identical to main.
- Scenario audit: 750 scenarios pass. Its unchanged sibling similarity screen
  remains a limitation of the broader unreviewed library.
- JavaScript syntax and `git diff --check` pass. HTML diff is limited to eight
  existing routes; XML changes are the same routes' lastmod fields.
- Isolated Chrome browser checks cover all eight pages at 1,366 × 900 desktop
  and actual 390 × 844 narrow sizes: HTTP 200, one H1, self-canonical, parseable
  JSON-LD, preserved /apply CTA, no document overflow, named table regions,
  keyboard scrolling where necessary and zero page JavaScript exceptions.
  Viewport contact sheets and full-page screenshots were manually reviewed.
  The [browser report](_buyer-intent-verification/browser-checks.json),
  [desktop contact sheet](_buyer-intent-verification/desktop.jpg) and
  [narrow contact sheet](_buyer-intent-verification/narrow.jpg) are review-only
  artifacts excluded from public output. Their 01–08 order follows the intent
  owners above. These are local draft renderings, not production screenshots.

```sh
python3 _gen/refresh_buyer_intent.py
python3 _gen/test_buyer_intent.py
python3 _gen/test_buyer_evidence.py
python3 audit_content.py
python3 _gen/audit_scenarios.py
node --check assets/main.js
node build_public.mjs
python3 _gen/audit_internal_inbound.py
git diff --check
```

The focused checks ran locally. The existing GitHub validation workflow is
unchanged; adding these checks to Actions requires a credential with workflow
write scope, which the available push credential does not have.

## Remaining review decisions

Review this exact PR head before merge and publication. Current service prices,
coverage and contract terms remain quote-specific. Any definitive client return
or corrected disputed entry total still needs dated evidence of the period,
expenses and denominator. The large generated library and other case/local
pages remain outside this bounded review. Do not treat this change as a
sitewide quality endorsement or ranking improvement. No indexing submission,
DNS/GHL change, team contact or customer contact was performed.
