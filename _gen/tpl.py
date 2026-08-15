#!/usr/bin/env python3
"""Shared page shell for generated pages.

Every generated page renders through `page()` so the head, header, footer,
and schema graph stay identical to the hand-written pages. Asset hashes are
placeholders, build_assets.py stamps the real ones after generation.
"""

SITE = "https://mybnbaccelerator.com"

ORG_SCHEMA = """    {
      "@type": "Organization",
      "@id": "https://mybnbaccelerator.com/#organization",
      "name": "BNB Accelerator",
      "legalName": "My BnB Accelerator, LLC",
      "alternateName": ["My BnB Accelerator", "My BnB Accelerator, LLC", "BNB Accelerator LLC"],
      "url": "https://mybnbaccelerator.com/",
      "logo": "https://mybnbaccelerator.com/assets/favicon.svg",
      "image": "https://mybnbaccelerator.com/assets/og-image.svg",
      "description": "BNB Accelerator is a done-for-you short-term rental acquisition firm that finds, underwrites, negotiates and closes cash-flowing Airbnb investment properties on behalf of high-income earners. Founded in 2021, it has closed more than 500 homes for over 260 clients across roughly 20 US markets.",
      "foundingDate": "2021",
      "founder": {
        "@type": "Person",
        "@id": "https://mybnbaccelerator.com/about/#founder",
        "name": "Nicholas Korom",
        "alternateName": "Nick Korom",
        "jobTitle": "Founder"
      },
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "3635 Montana Ave",
        "addressLocality": "Billings",
        "addressRegion": "MT",
        "postalCode": "59101",
        "addressCountry": "US"
      },
      "sameAs": ["https://www.trustpilot.com/review/mybnbaccelerator.com"],
      "areaServed": {
        "@type": "Country",
        "name": "United States"
      },
      "knowsAbout": [
        "Short-term rental investing",
        "Airbnb investment property acquisition",
        "Cost segregation",
        "Bonus depreciation",
        "Material participation",
        "Short-term rental tax strategy",
        "Short-term rental market analysis",
        "Short-term rental regulation"
      ],
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.5",
        "reviewCount": "27",
        "bestRating": "5",
        "worstRating": "1"
      }
    },
    {
      "@type": "WebSite",
      "@id": "https://mybnbaccelerator.com/#website",
      "url": "https://mybnbaccelerator.com/",
      "name": "My BnB Accelerator",
      "publisher": { "@id": "https://mybnbaccelerator.com/#organization" },
      "inLanguage": "en-US"
    }"""

NAV_ITEMS = [
    ("/how-it-works/", "How It Works"),
    ("/markets/", "Markets"),
    ("/deals/", "Deals"),
    ("/wins/", "Wins"),
    ("/case-studies/", "Case Studies"),
    ("/tax-strategy/", "Tax Strategy"),
    ("/compare/", "Compare"),
    ("/blog/", "Blog"),
    ("/about/", "About"),
]

BOOK_SITES = [
    ("https://drconnorrobertson.github.io/bnb-your-first-str/", "Your First STR"),
    ("https://drconnorrobertson.github.io/bnb-case-study/", "BNB Case Study"),
    ("https://drconnorrobertson.github.io/bnb-top-places-str-2026/", "Top STR Places 2026"),
    ("https://drconnorrobertson.github.io/bnb-value-add-str-guide/", "Value Add STR Guide"),
    ("https://drconnorrobertson.github.io/bnb-acquisition-system/", "The Acquisition System"),
]

DISCLAIMER = (
    "My BnB Accelerator, LLC is not a licensed tax, legal, or investment advisory firm. "
    "Nothing on this site is tax, legal, or investment advice, and no result described here "
    "is a guarantee of future performance. Real estate involves risk, including loss of principal. "
    "Tax outcomes depend entirely on your individual facts and circumstances, so consult your own "
    "CPA or attorney before acting. AE Tax Advisors is an independent partner firm and is not owned "
    "by or affiliated with My BnB Accelerator, LLC beyond a referral relationship. Client results "
    "shown are actual outcomes for specific properties and are not typical or promised. Revenue and "
    "occupancy figures are estimates for illustration and are not projections for any specific property."
)


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;")
             .replace(">", "&gt;").replace('"', "&quot;"))


def header(active=None, transparent=False):
    ds = ' data-start="transparent"' if transparent else ""
    links = []
    for href, label in NAV_ITEMS:
        cur = ' aria-current="page"' if href == active else ""
        links.append(f'      <a class="nav-link" href="{href}"{cur}>{label}</a>')
    links.append('      <a class="btn btn-primary btn-sm nav-cta" href="/apply/">Apply Now</a>')
    return f"""<a class="skip-link" href="#main">Skip to content</a>

<header class="site-header"{ds}>
  <div class="wrap">
    <a class="logo" href="/">
      <span class="logo-mark" aria-hidden="true">BA</span>
      <span class="logo-text">BNB <span>Accelerator</span></span>
    </a>
    <button class="menu-toggle" aria-label="Toggle navigation" aria-expanded="false" aria-controls="site-nav">
      <span></span><span></span><span></span>
    </button>
    <nav class="nav" id="site-nav" data-open="false" aria-label="Primary">
{chr(10).join(links)}
    </nav>
  </div>
</header>"""


def footer():
    books = "\n".join(
        f'          <li><a href="{u}" target="_blank" rel="noopener">{t}</a></li>'
        for u, t in BOOK_SITES)
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-brand">
        <a class="logo" href="/">
          <span class="logo-mark" aria-hidden="true">BA</span>
          <span class="logo-text">BNB Accelerator</span>
        </a>
        <p>Done-for-you short-term rental acquisition for high-income earners. Find it, buy it, launch it, without giving up your career.</p>
        <p class="footer-proof"><strong>500+</strong> homes closed &middot; <strong>260+</strong> clients &middot; <strong>4.5/5</strong> on Trustpilot</p>
      </div>
      <div class="footer-col">
        <h2>Company</h2>
        <ul>
          <li><a href="/about/">About BNB Accelerator</a></li>
          <li><a href="/how-it-works/">How It Works</a></li>
          <li><a href="/markets/">Markets</a></li>
          <li><a href="/deals/">Deal Tracker</a></li>
          <li><a href="/wins/">Client Wins</a></li>
          <li><a href="/case-studies/">Case Studies</a></li>
          <li><a href="/testimonials/">Testimonials</a></li>
          <li><a href="/compare/">Compare</a></li>
          <li><a href="/partners/">Partners</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h2>Property types</h2>
        <ul>
          <li><a href="/property-types/beach/">Beach STRs</a></li>
          <li><a href="/property-types/mountain/">Mountain Cabins</a></li>
          <li><a href="/property-types/lake/">Lake Houses</a></li>
          <li><a href="/property-types/ski/">Ski STRs</a></li>
          <li><a href="/property-types/desert/">Desert STRs</a></li>
          <li><a href="/property-types/city/">City STRs</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h2>Tax strategy</h2>
        <ul>
          <li><a href="/tax-strategy/">STR Tax Strategy</a></li>
          <li><a href="/tax-strategy/cost-segregation/">Cost Segregation</a></li>
          <li><a href="/tax-strategy/material-participation/">Material Participation</a></li>
          <li><a href="/tax-strategy/7-day-rule/">The Seven Day Rule</a></li>
          <li><a href="/regulations/">STR Rules by State</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h2>Playbooks</h2>
        <ul>
          <li><a href="/financing/">STR Financing</a></li>
          <li><a href="/design/">Design &amp; Furnishing</a></li>
          <li><a href="/management/">Property Management</a></li>
          <li><a href="/revenue-projections/">Revenue Projections</a></li>
          <li><a href="/tools/str-revenue-calculator/">Revenue Calculator</a></li>
          <li><a href="/data/">Market Data</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h2>Free books</h2>
        <ul>
{books}
        </ul>
      </div>
      <div class="footer-col">
        <h2>Resources</h2>
        <ul>
          <li><a href="/blog/">Blog</a></li>
          <li><a href="/answers/">Answers</a></li>
          <li><a href="/guides/">Guides</a></li>
          <li><a href="/tools/">Tools</a></li>
          <li><a href="/faq/">FAQ</a></li>
          <li><a href="/ask/">Common Questions</a></li>
          <li><a href="/topics/">Topics</a></li>
          <li><a href="/apply/">Apply</a></li>
          <li><a href="/sitemap/">Site Index</a></li>
        </ul>
      </div>
    </div>

    <div class="footer-bottom">
      <span>&copy; <span data-year>2026</span> My BnB Accelerator, LLC. All rights reserved.</span>
      <address>3635 Montana Ave, Billings, MT 59101 &middot; Serving clients nationwide</address>
    </div>

    <p class="disclaimer">{DISCLAIMER}</p>
  </div>
</footer>

<div class="sticky-cta" data-sticky-cta>
  <div class="sticky-cta-inner">
    <div class="sticky-cta-text">
      <strong>Ready to run your numbers?</strong>
      <span>Free strategy call &middot; No obligation</span>
    </div>
    <a class="btn btn-accent btn-sm" href="/apply/">Book a Call</a>
  </div>
</div>

<script src="/assets/main.js?v=36bec762" defer></script>
</body>
</html>
"""


def breadcrumb_schema(trail):
    """trail: list of (name, path) with path relative to site root."""
    items = []
    for i, (name, path) in enumerate(trail, 1):
        items.append(
            f'        {{ "@type": "ListItem", "position": {i}, '
            f'"name": "{esc(name)}", "item": "{SITE}{path}" }}')
    return ('    {\n      "@type": "BreadcrumbList",\n'
            '      "itemListElement": [\n' + ",\n".join(items) + "\n      ]\n    }")


def faq_schema(faqs):
    qs = []
    for q, a in faqs:
        qs.append(f"""    {{
      "@type": "Question",
      "name": "{esc(q)}",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "{esc(a)}"
      }}
    }}""")
    return """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
""" + ",\n".join(qs) + """
  ]
}
</script>"""


def article_schema(title, desc, url, published, modified=None, section="Short-Term Rental Investing"):
    modified = modified or published
    return f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{esc(title)}",
  "description": "{esc(desc)}",
  "datePublished": "{published}",
  "dateModified": "{modified}",
  "articleSection": "{esc(section)}",
  "inLanguage": "en-US",
  "mainEntityOfPage": {{ "@type": "WebPage", "@id": "{url}" }},
  "author": {{ "@type": "Organization", "name": "My BnB Accelerator, LLC", "url": "https://mybnbaccelerator.com/" }},
  "publisher": {{ "@id": "https://mybnbaccelerator.com/#organization" }},
  "isPartOf": {{ "@id": "https://mybnbaccelerator.com/#website" }}
}}
</script>"""


def breadcrumb_html(trail):
    """trail: list of (name, path). Last entry renders as plain text."""
    out = ['<nav class="breadcrumb" aria-label="Breadcrumb">']
    parts = []
    for name, path in trail[:-1]:
        parts.append(f'<a href="{path}">{name}</a>')
    parts.append(f"<span>{trail[-1][0]}</span>")
    out.append('<span class="sep">/</span>'.join(parts))
    out.append("</nav>")
    return "".join(out)


def page(*, title, description, path, body, extra_schema="", body_class="",
         active=None, transparent=False, og_title=None, og_desc=None):
    """Render a complete page. `path` is the site-root path with trailing slash."""
    url = SITE + path
    og_title = og_title or title
    og_desc = og_desc or description
    schema_blocks = extra_schema.strip()
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta name="theme-color" content="#1B2541">

<meta property="og:type" content="website">
<meta property="og:site_name" content="My BnB Accelerator">
<meta property="og:title" content="{esc(og_title)}">
<meta property="og:description" content="{esc(og_desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/og-image.svg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(og_title)}">
<meta name="twitter:description" content="{esc(og_desc)}">
<meta name="twitter:image" content="{SITE}/assets/og-image.svg">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap"></noscript>
<link rel="preload" as="style" href="/assets/style.min.css">
<link rel="stylesheet" href="/assets/style.min.css">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">

{schema_blocks}
</head>
<body{' class="' + body_class + '"' if body_class else ''}>
{header(active=active, transparent=transparent)}

<main id="main">
{body}
</main>

{footer()}"""


def graph(*blocks):
    inner = ",\n".join(b for b in blocks if b)
    return """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
""" + inner + """
  ]
}
</script>"""


def cta_band(heading, sub, primary=("/apply/", "Apply Now"),
             secondary=("/case-studies/", "See client results")):
    return f"""
  <section class="cta-band">
    <div class="wrap center">
      <h2 data-reveal>{heading}</h2>
      <p data-reveal data-reveal-delay="1">{sub}</p>
      <div class="btn-row center" data-reveal data-reveal-delay="2">
        <a class="btn btn-accent btn-lg" href="{primary[0]}">{primary[1]}</a>
        <a class="btn btn-ghost-light btn-lg" href="{secondary[0]}">{secondary[1]}</a>
      </div>
    </div>
  </section>
"""


def faq_html(faqs):
    out = ['        <h2 id="faq">Frequently asked questions</h2>']
    for q, a in faqs:
        out.append(f"""          <div class="faq-group">
            <h3>{q}</h3>
            <div class="faq-answer"><p>{a}</p></div>
          </div>""")
    return "\n".join(out)


AUTHOR_BOX = """        <div class="author-box">
          <div>
            <h3>My BnB Accelerator, LLC</h3>
            <p>We find and close the property. <a href="https://aetaxadvisors.com/" target="_blank" rel="noopener">AE Tax Advisors</a>, our independent partner firm, handles the tax strategy and filing.</p>
          </div>
        </div>"""
