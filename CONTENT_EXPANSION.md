# BNB Accelerator content expansion

Baseline on 22 September 2026: 632 public HTML routes before this batch. Doubling the route count would require roughly 632 additional pages. The goal is more useful search coverage, not a URL quota. Google may omit repetitive or low-value pages from Search even when they are in a sitemap.

## Editorial audit before further scale

The September 22 review found substantial repeated passages in several older year-by-year and quarterly blog series. The Q3 and Q4 2026 retrospective market updates were published before those quarters ended; both were removed and redirected. The remaining annual and quarterly variants need individual checks for genuinely distinct evidence, accurate publication dates, and a search intent that merits its own URL. Consolidate or rewrite weak variants before adding another generated series. The technical audit below checks crawlability; it does not certify editorial quality or guarantee indexing.

The follow-up review traced the generated archive to the August 15, 2026 repository commit titled “Backdate the archive to 2021.” It retired all 208 remaining market-by-year, topic-by-year, and quarterly variants and redirected each to the closest surviving guide. It also corrected the publication metadata and visible dates on 213 surviving blog posts to their first repository commit date. This leaves 424 public HTML routes, including 243 blog articles. Those dates are repository evidence, not a guarantee of when each URL first became publicly reachable. More content should be added only after the distinct-value gate below is met.

The September 22 expansion brings the library to 679 public routes and exactly 486 blog articles. It adds 12 city-level service-area pages so every one of the 20 active markets named on the market hub has a dedicated URL, plus 243 property-system guides. The blog batch is organized as 27 physical and operating systems crossed with nine separate owner decisions: budget, acquisition, inspection, design, operations, maintenance, insurance, revenue and repair-versus-replace. New articles use their actual September 22, 2026 release date and are not backdated.

## Publishing order

1. **Recover old search demand.** Keep a redirect ledger for former WordPress URLs. Redirect each retired URL to the closest current answer, with no homepage catch-all. Check Search Console's Not found report and add exact mappings for discovered 404s. The first 24 source paths are in `vercel.json`.
2. **Measure the current index.** Record Search Console totals for indexed pages, discovered but not indexed, crawled but not indexed, impressions, and queries. Use these numbers to decide whether expansion or consolidation is the next best move. A 200 response and sitemap inclusion establish eligibility, not indexing.
3. **Publish evidence-backed clusters.** Give each new page a distinct reader task, a concrete method, a worked example or original source, and links to the parent hub and relevant existing pages. Update information that depends on platform policy, local law, loan terms, or tax rules from current primary sources.
4. **Consolidate overlaps.** If a new query can be fully answered by improving an existing page, update that page rather than create a near-duplicate URL. Use a redirect when replacing an older page.

## Candidate inventory to reach a 2x library

| Cluster | Candidate ceiling | Evidence needed before publishing |
| --- | ---: | --- |
| Acquisition decisions and contract due diligence | 80 | Deal documents, checklists, attorney or lender review where needed |
| Operating economics and owner reporting | 80 | Worked models, invoices, actual operator workflows |
| Guest operations and service recovery | 80 | Current platform rules, real SOPs, examples |
| Financing and capital planning | 60 | Current lender term sheets and clear example assumptions |
| Property type and amenity decisions | 70 | Costed bids, booking comparables, maintenance tradeoffs |
| Market and submarket decisions | 120 | Dated comparable data and local demand evidence |
| Local regulation and permit checks | 90 | Current municipal primary sources, parcel-level caveats |
| Documented client deal follow-ups | 60 | Client permission, source records, realized-vs-projected labels |
| Calculators and downloadable decision tools | 25 | Tested calculations and useful interaction |
| **Maximum candidates** | **665** | Each must pass the distinct-value gate below |

This is a research backlog, not permission to generate 665 templated pages. Some candidates will collapse into existing content. A smaller set that attracts qualified visitors is preferable to 1,264 weak URLs.

## Distinct-value gate for every page

- Search intent and reader decision are different from the closest existing page.
- At least one original useful element: a worked calculation, primary-source interpretation, documented example, comparison framework, checklist, or tool.
- Date-sensitive claims cite or link to current primary sources and carry a checked date.
- Title, H1, description, canonical, structured data, and internal links accurately describe the visible page.
- The page is accessible with JavaScript off, returns 200, is not `noindex`, and appears once in the XML sitemap.
- A human can answer what the reader learned that was unavailable on the parent page.

Run `python3 audit_content.py` before every release. It checks all routes, sitemap coverage, duplicate metadata, canonical URLs, JSON-LD, internal links, and redirect targets.

## Release measurement

After each cluster, inspect Search Console over several weeks for discovery, indexation, impressions, and queries. Merge or improve pages that Google declines to index when they overlap. Track qualified applications and assisted conversions, not just route count.
