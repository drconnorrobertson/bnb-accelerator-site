# BNB Accelerator Site

Static marketing site for **My BnB Accelerator, LLC**, done-for-you short-term rental acquisition for high-income earners.

Built as plain HTML/CSS/JS with no build step. Deploys to Vercel as-is.

## Stack

- Static HTML, one `index.html` per route directory
- Single stylesheet: `assets/style.css`
- Single script: `assets/main.js` (sticky header, mobile nav, scroll reveals, animated stat counters, FAQ deep-linking, application form handler)
- Inter via Google Fonts
- No framework, no bundler, no dependencies

## Structure

```
/                          Home
/how-it-works/             The 5-stage process + Reverse Offset Method
/markets/                  8 states, 20+ submarkets with price/revenue/ROI
/case-studies/             Documented client results
/tax-strategy/             7-day rule, material participation, cost seg, AE Tax partner
/faq/                      30+ questions with FAQPage schema (SEO centerpiece)
/testimonials/             Client quotes, Trustpilot, video placeholders
/apply/                    Application form
/compare/                  vs DIY / BNB Mastery / Robuilt
/blog/                     Index + 10 posts
404.html                   Custom 404
robots.txt                 Allow all + sitemap reference
sitemap.xml                All 20 URLs
<key>.txt                  IndexNow key file
vercel.json                Clean URLs, trailing slash, caching, security headers
assets/                    style.css, main.js, favicon.svg, og-image.svg
```

## Blog posts

1. Is BNB Accelerator Worth It? An Honest Review (2026)
2. How to Buy Your First Airbnb Investment Property in 2026
3. The Complete Guide to STR Tax Savings for High-Income Earners
4. Best Airbnb Markets for 2026: Where We're Buying Now
5. BNB Accelerator vs Doing It Yourself: Time, Risk, and ROI
6. How One Client Made $20K in Cash Flow in a Single Month
7. The 7-Day Rule Explained: How STR Losses Offset W-2 Income
8. Cost Segregation for Airbnb Properties: The Tax Strategy You're Missing
9. Why We Don't Invest in California (And Where We Invest Instead)
10. From W-2 to Wealth: How High Earners Are Building STR Portfolios

Posts 7 and 8 cross-link to aetaxadvisors.com per the partner arrangement.

## SEO

Every page carries:

- Unique `<title>` and meta description
- Canonical URL
- Open Graph + Twitter Card tags
- JSON-LD: `Organization`, `WebSite`, `Service`, `BreadcrumbList`, `FAQPage`, `BlogPosting`, `HowTo`, `ItemList`, `AggregateRating`

The FAQ page carries a full 32-question `FAQPage` block. Blog posts each carry `BlogPosting` + `BreadcrumbList` + a targeted `FAQPage`.

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
- [ ] Wire the `/apply/` form to a real endpoint (GoHighLevel, Formspree, or a Vercel serverless function). Currently `assets/main.js` stores the submission in `sessionStorage` and shows a confirmation, it does **not** transmit anywhere.
- [ ] Replace the AE Tax booking iframe URL in `/tax-strategy/` with the live calendar embed
- [ ] Replace the three video placeholders in `/testimonials/` with real embed URLs
- [ ] Confirm the Trustpilot profile URL in `/testimonials/`
- [ ] Submit `sitemap.xml` to Google Search Console and Bing Webmaster Tools
- [ ] Submit the IndexNow key file to Bing/IndexNow
- [ ] Have counsel review the disclaimers in the footer and the illustrative tax figures

## Content notes

- All tax content is written as explanation, not advice, with disclaimers on every page. AE Tax Advisors is presented as an **independent partner firm**, not an owner or affiliate.
- Client results are labeled as specific outcomes, not typical or guaranteed.
- Competitor comparisons include trademark disclaimers.
- Copy uses `--` rather than em dashes throughout.

## Contact

My BnB Accelerator, LLC
3635 Montana Ave, Billings, MT 59101
