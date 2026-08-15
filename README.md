# BNB Accelerator Site

Static marketing site for **My BnB Accelerator, LLC**, done-for-you short-term rental acquisition for high-income earners.

Plain HTML/CSS/JS. Two small Python scripts handle asset minification and
search-engine submission; there is no bundler and no dependencies. Deploys to
Vercel as-is.

## Stack

- Static HTML, one `index.html` per route directory
- Source stylesheet: `assets/style.css`; served build: `assets/style.min.css`
- Single script: `assets/main.js` (sticky header, mobile nav, scroll reveals, animated stat counters, FAQ deep-linking, sticky conversion bar, lead-magnet and application form handlers)
- Inter via Google Fonts
- No framework, no bundler, no dependencies

## Structure

```
/                          Home
/how-it-works/             The 5-stage process + Reverse Offset Method
/markets/                  8 states, plus 20 market earnings pages
/markets/<market>/         "How much can you make on Airbnb in X" + data table
/case-studies/             Documented client results
/tax-strategy/             7-day rule, material participation, cost seg
/partners/                 AE Tax Advisors, and where our work stops
/answers/                  Short definition pages for AI overview capture
/data/                     Revenue and occupancy datasets across 20 markets
/guides/                   Operational guides + two free lead magnets
/tools/str-revenue-calculator/   Interactive cash-flow and tax model
/faq/                      Questions with FAQPage schema
/testimonials/             Client quotes, Trustpilot
/apply/                    Application form
/compare/                  vs DIY / BNB Mastery / Robuilt / agents / managers
/case-studies/<client>/    18 client case studies from the live site
/property-types/           beach, mountain, lake, city, ski, desert
/regulations/<state>/      STR rules for 20 states
/financing/                DSCR, conventional, down payments, entry cost
/design/                   Furnishing and design playbook
/management/               Self vs co-host vs full service
/revenue-projections/      Building a projection that survives contact
/wins/                     46 client win graphics with a lightbox gallery
/topics/                   Ten topic cluster pillars
/blog/                     Index + 453 posts, 2021 to 2026
/sitemap/                  Human-readable site index
404.html                   Custom 404
robots.txt                 Crawl rules + AI crawler allowances
sitemap.xml                All 598 indexable URLs with lastmod and priority
<key>.txt                  IndexNow key file
build_assets.py            Minify CSS, stamp hashed asset URLs
submit_indexnow.py         Submit sitemap URLs to IndexNow
_gen/                      Page generators, see below
vercel.json                Clean URLs, trailing slash, caching, security headers
assets/                    style.css, style.min.css, main.js, favicon.svg, og-image.svg
```

## Content

598 indexable pages: 453 blog posts, 46 client wins, 20 market earnings pages,
20 state regulation pages, 18 client case studies, 25 comparison pages, ten topic
cluster pillars, 6 property type guides, 4 financing guides, 8 definition pages
under `/answers/`, three playbooks, operational guides, two datasets, and a
revenue calculator.

The 18 case studies were taken from the client case studies page on the live
site. Every client name, market, bedroom count, purchase price and cash flow
figure comes from there. Where that page published property details without a
revenue number, the case study says so rather than filling the gap.

## Generators

`_gen/` is the source of truth for everything generated. Regenerating is
cheaper than hand-editing 598 files, and it is how the footer, the schema
graph and the site index stay consistent.

```
_gen/tpl.py                Shared page shell: head, header, footer, schema
_gen/pillars.py            guide() and hub() renderers for section pages
_gen/blog.py               Post renderer + blog index rebuilder
_gen/case_studies.py       18 case studies + the hub
_gen/gen_property_types.py 6 property type guides + hub
_gen/gen_regulations.py    20 state pages + hub
_gen/gen_playbooks.py      financing, design, management, revenue, tax sub-pages
_gen/posts_*.py            104 hand-written blog posts as data, by category
_gen/era.py                Per-year context: market, rates, risk, bonus depreciation
_gen/market_arcs.py        One line per market per year, 2021 to 2026
_gen/market_data.json      Revenue and ADR ranges scraped from the market pages
_gen/gen_market_year.py    120 posts: each market in each year
_gen/gen_topic_year.py     66 posts: each topic in each year
_gen/gen_market_updates.py 24 quarterly market updates
_gen/gen_topics.py         Ten cluster pillar pages plus the /topics/ hub
_gen/gen_wins.py           /wins/ from the client win graphics
_gen/home_wins.py          The Client Wins strip on the home page
_gen/run_archive.py        Dates every post across 2021 to 2026 and builds them
_gen/crosslink_markets.py  Adds the related-links block to each market page
_gen/gen_site_index.py     Rebuilds /sitemap/ from what is on disk
_gen/sitewide.py           Stamps the footer everywhere, rebuilds sitemap.xml
```

Run order after any content change:

```
python3 _gen/run_archive.py      # every blog post + cluster pillars + blog index
python3 _gen/sitewide.py         # footer + sitemap.xml
python3 _gen/gen_site_index.py   # /sitemap/
python3 build_assets.py          # minify and stamp asset hashes
```

`run_archive.py` is the entry point for anything blog-related. It regenerates
all 453 posts, assigns their dates, builds the ten cluster pillars and rewrites
the blog index in one pass.

Blog post dates are assigned in `run_archive.py`, not stored per post. The
archive runs from 4 January 2021 to 13 August 2026 and publishes on Mondays and
Thursdays: 453 posts across 586 available slots, evenly spread at 79 or 80 a
year through 2025 and 57 in the eight months of 2026 so far.

A year in a post's H1 pins it to that year, because that is genuine era content.
A year appearing only in the `<title>` tag is the "(2026)" SEO suffix the older
posts were written with; those are dated on merit and the suffix is dropped
rather than rewritten, because some bodies discuss law that did not exist in the
assigned year.

Era accuracy matters most for the tax posts, and the bonus depreciation spine in
`era.py` is factual: 100% through 2022, 80% in 2023, 60% in 2024, then the 2025
split where property acquired on or before 19 January stayed at 40% and OBBBA
restored 100% permanently for property acquired and placed in service after that
date.

### Client wins

`assets/wins/` holds 46 client result graphics, deduped from 93 files in
Connor's Drive folder. They are designed compositions whose content is the text,
so they are never cropped: the cards are a fixed 4:3 box with `object-fit:
contain` over each graphic's own sampled edge colour. Captions in `gen_wins.py`
are transcribed from the graphics, so every figure on the page is one the
client's own card already displays.

Tax-related pages cross-link to aetaxadvisors.com per the partner arrangement,
and `/partners/` states the boundary explicitly: we are an acquisition firm,
not a CPA firm.

## SEO

Every page carries a unique title and meta description, a canonical URL, full
Open Graph and Twitter Card tags, and a JSON-LD graph containing at minimum
`Organization`, `WebSite`, `SiteNavigationElement` and `BreadcrumbList`.
Content pages add `Article`/`BlogPosting` and a targeted `FAQPage`; guides add
`HowTo`; definition pages carry `speakable` pointing at the opening answer.

`Organization` is used deliberately in place of `LocalBusiness`. The business
operates nationally, so nothing on the site should signal local intent:
`areaServed` is the United States, and the market pages exist to demonstrate
expertise in those markets rather than to target them geographically.

Market figures are estimates assembled from closings and active comparables,
and every page carrying them says so.

## Editing assets

`assets/style.css` is the source of truth. After changing it, or `main.js`:

```
python3 build_assets.py
```

That minifies the stylesheet to `assets/style.min.css` and rewrites every
page's `<link>`/`<script>` to a content-hashed URL, so a deploy invalidates
the previously cached copy. `main.js` is deliberately left unminified: it is
small, and a hand-rolled JS minifier is a correctness risk for no real gain.

## Deployment blocker: the domain does not serve this repo

As of 15 August 2026, `mybnbaccelerator.com` resolves to a GoHighLevel /
LeadConnector funnel behind Cloudflare, not to this site. Every path 301s to
`/home`, the live `robots.txt` is empty, and the live `sitemap.xml` is
GoHighLevel's own index. Verify with:

```
curl -sI https://mybnbaccelerator.com/blog/          # 301 -> /home
curl -s  https://mybnbaccelerator.com/sitemap.xml    # GHL sitemapindex
```

Nothing in this repo is publicly reachable until DNS points at the Vercel
deployment. That is also what blocks IndexNow: submission requires the key
file to be readable at `https://mybnbaccelerator.com/<key>.txt`, and today
that URL returns the funnel's HTML. A forced attempt on 15 August 2026 was
rejected by the endpoint with:

```
403 {"errorCode":"SiteVerificationNotCompleted", ...}
```

Do not submit to IndexNow before the cutover. Pushing 215 URLs that all
redirect to `/home` feeds redirect and soft-404 signals to Bing, Yandex,
Seznam and Naver, which is worse than not submitting at all.

## Search engine submission

After deploying, push the URL set to IndexNow (Bing, Yandex, Seznam, Naver;
Google does not participate):

```
python3 submit_indexnow.py --dry-run     # inspect first
python3 submit_indexnow.py               # submit
python3 submit_indexnow.py --since 2026-08-15   # only recently changed URLs
```

The script refuses to submit unless `https://mybnbaccelerator.com/<key>.txt`
is live and serves the matching key, so deploy before running it.

## Deploying to Vercel

No build configuration needed. Import the repo and deploy, Vercel serves it as a static site.

```
Framework Preset:  Other
Build Command:     (leave empty)
Output Directory:  (leave empty / root)
```

`vercel.json` handles clean URLs, trailing slashes, asset caching, and security headers.

## Before going live

- [ ] **Point `mybnbaccelerator.com` at the Vercel deployment.** Blocks everything below.

  Re-checked 15 August 2026, after the expansion to 598 pages: the apex domain
  still serves the previous funnel site. Every path 301s to
  `https://mybnbaccelerator.com/home`, and the IndexNow key file returns 403
  there, so `submit_indexnow.py` correctly refuses the batch. It has not been
  forced, and it should not be: submitting 598 URLs that redirect away is worse
  than not submitting, because it teaches the participating engines that this
  host serves redirects.

  The Vercel deployment is live and current at
  `https://bnb-accelerator-site.vercel.app/`, serving all 598 URLs including
  the key file. Nothing else on this list can be finished until DNS moves.

- [ ] Wire the `/apply/` form and the two `/guides/` lead-magnet forms to a real endpoint (GoHighLevel, Formspree, or a Vercel serverless function). Currently `assets/main.js` stores the submission in `sessionStorage` and shows a confirmation, it does **not** transmit anywhere.
- [ ] Replace the AE Tax booking iframe URL in `/tax-strategy/` with the live calendar embed
- [ ] Replace the three video placeholders in `/testimonials/` with real embed URLs
- [ ] Confirm the Trustpilot profile URL in `/testimonials/`
- [ ] Submit `sitemap.xml` to Google Search Console and Bing Webmaster Tools
- [ ] Run `python3 submit_indexnow.py` once the cutover is done and the key file resolves
- [ ] Have counsel review the disclaimers in the footer and the illustrative tax figures

## Content notes

- All tax content is written as explanation, not advice, with disclaimers on every page. AE Tax Advisors is presented as an **independent partner firm**, not an owner or affiliate.
- Client results are labeled as specific outcomes, not typical or guaranteed.
- Competitor comparisons include trademark disclaimers.
- Copy uses `--` rather than em dashes throughout.

## Contact

My BnB Accelerator, LLC
3635 Montana Ave, Billings, MT 59101
