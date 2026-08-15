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
/blog/                     Index + 140 posts
/sitemap/                  Human-readable site index
404.html                   Custom 404
robots.txt                 Crawl rules + AI crawler allowances
sitemap.xml                All 203 indexable URLs with lastmod and priority
<key>.txt                  IndexNow key file
build_assets.py            Minify CSS, stamp hashed asset URLs
submit_indexnow.py         Submit sitemap URLs to IndexNow
vercel.json                Clean URLs, trailing slash, caching, security headers
assets/                    style.css, style.min.css, main.js, favicon.svg, og-image.svg
```

## Content

Around 200 indexable pages: 140 blog posts, 20 market earnings pages, 14
comparison pages, 8 definition pages under `/answers/`, operational guides,
two datasets, and a revenue calculator.

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

- [ ] Point `mybnbaccelerator.com` at the Vercel deployment
- [ ] Wire the `/apply/` form and the two `/guides/` lead-magnet forms to a real endpoint (GoHighLevel, Formspree, or a Vercel serverless function). Currently `assets/main.js` stores the submission in `sessionStorage` and shows a confirmation, it does **not** transmit anywhere.
- [ ] Replace the AE Tax booking iframe URL in `/tax-strategy/` with the live calendar embed
- [ ] Replace the three video placeholders in `/testimonials/` with real embed URLs
- [ ] Confirm the Trustpilot profile URL in `/testimonials/`
- [ ] Submit `sitemap.xml` to Google Search Console and Bing Webmaster Tools
- [ ] Run `python3 submit_indexnow.py` once the new pages are live
- [ ] Have counsel review the disclaimers in the footer and the illustrative tax figures

## Content notes

- All tax content is written as explanation, not advice, with disclaimers on every page. AE Tax Advisors is presented as an **independent partner firm**, not an owner or affiliate.
- Client results are labeled as specific outcomes, not typical or guaranteed.
- Competitor comparisons include trademark disclaimers.
- Copy uses `--` rather than em dashes throughout.

## Contact

My BnB Accelerator, LLC
3635 Montana Ave, Billings, MT 59101
