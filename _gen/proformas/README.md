# Native pro forma intake

Store one JSON record per property here. Internal records are excluded from Vercel output. Start with `template.json`; set a stable slug, fill sources and assumptions, then change `publication_status` from `draft` to `published` after editorial review. No draft has a public route, directory card or sitemap entry.

Public routes are `/proformas/{slug}/`. Prefer `123-main-street-city-state` when the public street address is supplied and permitted for publication. Keep the slug stable when assumptions change. A rejected deal is a useful educational review, not a claim the property is defective. Explain why it fails the specific modeled purchase.

A PDF/spreadsheet/email can be ingested by extracting fields into this record. Retain the original privately and add approved public source links. Reconcile numbers and ask about missing definitions before publishing; never convert blanks to zero. Do not copy private borrower, tenant or seller details onto the page. Documents remain internal unless separately approved for public linking.

`good` / `bad` / `watch` are editorial verdicts with a reason, not an automatic investment recommendation. `projected` and `actual` records stay labeled, with a covered period. Use dollar amounts in annual terms. Expense rows exclude debt service; debt service is shown separately. Invested cash is the sum of the provided cash components, including retained reserve. If reserves are excluded from a provider return denominator, explain the distinction rather than silently substituting it.

Run `python3 scripts/build_proformas.py` and `python3 scripts/test_proformas.py`. The Vercel public build regenerates the directory and approved detail pages. Removed or unpublished records remove their previously generated pages and sitemap entries; the generator only owns routes recorded in its manifest. For a previously live withdrawal, add an appropriate redirect or intentional removal response.
