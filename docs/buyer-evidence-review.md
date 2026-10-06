# Buyer evidence review — October 6, 2026

Baseline: remote `main` at `3f8efe7774c3d772f75be27a6b2efd26d0d8ec66`.
The implementation uses a clean clone and branch; the other local checkout's
uncommitted changes were preserved. This is a draft for editorial review.

## Scope

Nine existing routes, no expansion of the 2,412-route inventory:

| Route | Decision supported |
| --- | --- |
| `/case-studies/adam-florida-panhandle/` | Acquisition facts with an unresolved return basis |
| `/case-studies/ashley-billy-fort-walton-beach/` | Reported bookings with an unreconciled entry total |
| `/case-studies/` | Evidence-aware introduction and corrected cards for those two records |
| `/blog/reconcile-airbnb-payout-export/` | Guest charges, fees, refunds, unpaid payouts and bank timing |
| `/financing/closing-costs-and-reserves/` | Down payment, settlement, outside costs, launch carry and retained cash |
| `/financing/dscr-loans/` | A lender's qualifying ratio versus owner cash flow |
| `/blog/permits-that-do-not-transfer/` | Buyer eligibility, HOA restrictions and capacity |
| `/blog/str-purchase-to-launch-timeline/` | Dependency gates and delayed-opening cash |
| `/management/` | Reservations, payouts, guest obligations, fee scope and controls |

The six buyer examples use invented, explicitly hypothetical inputs. They do
not represent client outcomes, program quotes, market averages or forecasts.
Publication dates remain unchanged; reviewed articles record October 6, 2026
as their modification date. Only the nine routes' sitemap dates change.
The current header, footer, asset URLs and `/apply/` funnel are preserved.

## Public source evidence

All sources below were read from public pages on October 6, 2026. No private
client files, addresses, guest data, pro formas or unpublished notes were used.

| Source | Supported use and limit |
| --- | --- |
| [BNB acquisition evidence library](https://www.bnbacceleratorreviews.co/case-studies) | 86 sanitized records, 29 process stories; first-party evidence, not independently verified operating performance |
| [Sedona closing balance story](https://www.bnbacceleratorreviews.co/case-studies/sedona-az-2025-46) | Cash-to-close reconciliation; a recorded concession does not establish its final application |
| [Sevierville capacity and reservation story](https://www.bnbacceleratorreviews.co/case-studies/sevierville-tn-42) | Permit/capacity documentation and handoff coordination; does not establish current buyer permission or income |
| [Broken Bow reservation handoff](https://www.bnbacceleratorreviews.co/case-studies/broken-bow-ok-46) | Incoming/outgoing manager coordination alongside closing; no post-close income claim |
| [Albrightsville closing extension](https://www.bnbacceleratorreviews.co/case-studies/albrightsville-pa-47) | Repair discussions and an extension; no claim about subsequent launch timing or realized equity |
| [BNB public deal tracker](https://www.bnbaccelerator.com/deals/) and the two case-study pages at the baseline commit | Existing company-reported acquisition, cost and booking fields; reporting periods, expense coverage and return denominators remain unverified |
| [Airbnb earnings instructions](https://www.airbnb.com/help/article/3632) | Listing/date-filtered reports and exports; a payout is not owner profit |
| [Visio's DSCR explanation](https://visiolending.com/resources/what-is-a-dscr-loan-how-rental-property-investors-qualify/) | A specific lender's rent-to-PITIA definition; not a universal underwriting rule or a current quote |
| [Denver licensing authority](https://www.denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Business-Licensing/Business-licenses/Short-term-rentals) | Primary-residence restriction; educational and historical coverage does not establish active BNB service availability |

The public review library and tracker pages returned readable HTML using HTTP
retrieval. Airbnb, Visio and Denver guidance were also checked with web retrieval.
Visio rejected command-line retrieval, but its official text was available via
web retrieval. An attempted reviews `/results` page did not provide usable
content and is not cited or used as evidence.

## Reconciliation decisions

Adam's acquisition fields: $645,000 purchase, $129,000 down, $24,188 closing and
$42,581 design. The latter three sum to the listed $195,769. The previous
$19,893 annual cash-flow label and 7.93% percentage do not reconcile with that
entry cost. No new percentage is asserted. Acquisition fields do not prove a
complete buyer budget or independently verified settlement.

Ashley/Billy's fields: $630,000 purchase, $63,000 down, $1,950 closing and
$159,750 design. Components sum to $224,700, against the recorded $220,800
total, leaving a $3,900 unexplained difference. Both are labeled as reported
fields; neither total is promoted to a corrected client outcome. Nearly 80
nights booked within 21 days after launch remains a reported booking milestone, not proof
of completed stays, payouts, the closing-to-opening interval or annual profit.
The earlier $43,946/17.52% fields are described only as unresolved source claims.
The 21 days are labeled as the booking observation period after launch,
and the hub retains the roughly 80 booked nights alongside that period. The
source does not establish a 21-day interval from closing to opening.

To restore any definitive return, reviewers need dated property-level income
and expense records, debt service, realized-versus-projected status and the
cash-investment ledger for the same period. To resolve Ashley/Billy's entry
cost, reviewers need the settlement statement and itemized outside-closing
costs explaining the $3,900 difference and any omitted costs. This PR requests
no private records and sends no outreach.

## Validation and limits

Local validation passed:

- `python3 audit_content.py`: 2,412 HTML/sitemap routes, unique metadata,
  valid JSON-LD, internal links/assets, homepage reachability and 277 redirects.
- `python3 _gen/test_buyer_evidence.py`: eight tests covering case-study
  evidence gaps, hypothetical arithmetic, lender/owner distinctions,
  generator persistence, unchanged publication dates, shared design and funnel.
- `python3 _gen/audit_scenarios.py`: 750 scenarios, metadata, canonicals,
  finite inputs and required decision elements.
- `node --check assets/main.js` and `node build_public.mjs`: public build with
  all 2,412 sitemap routes and internal source files excluded.
- Repeating `refresh_buyer_evidence.py` produced byte-identical HTML/sitemaps.
- `git diff --check` passed.
- Local Chrome page checks: all nine routes rendered one H1 and their call
  links; no page-level horizontal overflow at the effective 520px narrow
  viewport, with tables contained at 484px. Adam's desktop view was checked
  at 1360px. The browser viewport override was reset afterward.

Scenario template similarity remains high (adjacent five-gram Jaccard median
0.715, max 0.727). That broader library is unchanged. Other case studies and the
aggregate deal tracker still require a separate source/period review; this
cohort is not a claim that the full inventory has verified returns. No ranking,
search volume or indexing improvement is claimed from these code checks.
Search Console baseline and prioritization are being handled by the parent.

Adding the focused regression/scenario/build commands to GitHub Actions was
blocked because the available Git push token lacks `workflow` scope. The
existing workflow is unchanged. These checks remain runnable locally via the
commands above; CI integration is a separate maintainer decision.

No production deployment or promotion, merge, domain/DNS/GHL change, indexing
submission or team/client contact is part of this work. Existing automatic PR
checks and protected preview behavior are retained without settings changes.
