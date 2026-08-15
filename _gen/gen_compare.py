#!/usr/bin/env python3
"""Build /compare/ and every "BNB Accelerator vs X" matchup page.

The index is a menu and nothing else: one card per competitor. Each matchup
page runs the same six beats, in order, with no long prose anywhere:

    hero -> quick verdict -> side-by-side table -> three differentiators
         -> client results from the deal tracker -> CTA

SEO titles, descriptions and the FAQ copy live in compare_data.json, lifted
verbatim from the pages this generator replaced. The new editorial content
(verdict, table rows, differentiators) is authored here.

Run order:  python3 _gen/gen_compare.py && python3 _gen/sitewide.py \
            && python3 _gen/gen_site_index.py && python3 build_assets.py
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tpl
from pillars import write

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = json.load(open(os.path.join(HERE, "compare_data.json"), encoding="utf-8"))
DEALS_DOC = json.load(open(os.path.join(HERE, "deals.json"), encoding="utf-8"))
AGG, DEALS = DEALS_DOC["aggregate"], DEALS_DOC["deals"]

PUB = "2026-08-10"
MOD = "2026-08-15"

TRADEMARK = ("Company and program names are the trademarks of their respective owners and are "
             "not affiliated with, endorsed by, or partnered with My BnB Accelerator, LLC. "
             "Descriptions reflect each provider's publicly available marketing materials at the "
             "time of writing. Verify current offerings directly before deciding.")

# --------------------------------------------------------------------- icons
# 24px stroke icons, currentColor, sized by .card-icon.
ICONS = {
    "buyside": '<path d="M12 3l7 3v5c0 4.4-2.9 8.4-7 10-4.1-1.6-7-5.6-7-10V6l7-3z"/><path d="M9 12l2 2 4-4"/>',
    "screen": '<path d="M3 5h18l-7 8v6l-4 2v-8L3 5z"/>',
    "tax": '<path d="M5 3h14v18l-3-2-2 2-2-2-2 2-2-2-3 2V3z"/><path d="M9 8h6M9 12h6M9 16h3"/>',
    "speed": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "deed": '<path d="M4 10l8-6 8 6v9a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1v-9z"/><path d="M9 20v-6h6v6"/>',
    "record": '<path d="M4 20h16"/><path d="M7 20v-7M12 20V6M17 20v-10"/>',
}

DIFFS = {
    "buyside": ("We are paid by you, not the seller",
                "We hold no inventory and take nothing from the sell side, which is what makes "
                "&ldquo;don't buy this one&rdquo; a sentence we can afford to say."),
    "screen": ("98% of what we screen gets killed",
               "Over 1,000 listings reviewed a week, underwritten against hand-picked comparables. "
               "You see the few that survive, with the full model attached."),
    "tax": ("The tax outcome drives the purchase",
            "Price point, closing date and management structure are set against what the deduction "
            "needs to do, with AE Tax Advisors handling the tax work as an independent firm."),
    "speed": ("About 45 days to a live listing",
              "We buy homes that already exist, so the timeline runs on closing and furnishing "
              "rather than on permits, contractors and a placed-in-service date that can slip."),
    "deed": ("You own the deed, not a unit or a lease",
             "Direct ownership is what makes depreciation, cost segregation and an offset against "
             "W-2 income possible at all. Every other structure gives that up."),
    "record": ("500+ homes closed since 2021",
               "More than 260 clients, 80% of whom come back for another property, and 25 deals "
               "published with every figure shown."),
}

ROW_LABELS = ["Approach", "Pricing Model", "Markets Covered", "Deal Support",
              "Tax Strategy", "Track Record", "Hands-On vs Course"]

# Our side of the table is the same argument on every page.
US = [
    ("yes", "Done-for-you acquisition, start to live listing"),
    ("yes", "One flat engagement fee, paid by you"),
    ("", "8 states: FL, TN, AZ, OK, PA, TX, CO, MO"),
    ("yes", "Sourcing, underwriting, negotiation, closing"),
    ("yes", "Designed in, with AE Tax Advisors"),
    ("yes", "500+ homes closed since 2021"),
    ("yes", "Hands-on service. Roughly 10-20 hours from you"),
]

# slug, display name, card initials, verdict, their column, three differentiators
COMPETITORS = [
    ("bnb-accelerator-vs-diy", "Doing It Yourself", "DIY",
     "BNB Accelerator does the acquisition for you in roughly 45 days. Doing it yourself costs no "
     "fee and roughly 150 to 300 hours, and it puts the three expensive mistakes &mdash; "
     "regulation, revenue assumptions and management structure &mdash; on your side of the table.",
     [("no", "You are the service"),
      ("partial", "No fee. 150-300 hours instead"),
      ("", "Whatever you can research alone"),
      ("no", "You source, model, negotiate and coordinate"),
      ("no", "Find your own CPA, usually in April"),
      ("no", "Your first deal"),
      ("no", "Fully hands-on. 4-8 months typical")],
     ["screen", "speed", "tax"]),

    ("bnb-accelerator-vs-bnb-mastery", "BNB Mastery Program", "BM",
     "BNB Accelerator buys a property you own outright. BNB Mastery teaches you to run the business "
     "yourself, historically with a heavy emphasis on arbitrage. One delivers an asset, the other "
     "delivers a skill set.",
     [("partial", "Education, coaching and community"),
      ("partial", "Program fee, plus your own deposits and setup"),
      ("", "You choose and research your own"),
      ("no", "You source, model and negotiate"),
      ("no", "Arbitrage has no basis to depreciate"),
      ("partial", "Student results, not closings"),
      ("no", "Course. 100-250 hours from you")],
     ["deed", "tax", "speed"]),

    ("bnb-accelerator-vs-robuilt", "Robuilt", "RO",
     "BNB Accelerator buys an existing cash-flowing home and gets it live in about 45 days. Robuilt "
     "teaches you to build a unique stay yourself &mdash; a higher ceiling, with construction, "
     "permitting and timeline risk attached.",
     [("partial", "Education and community around unique-stay builds"),
      ("partial", "Course and community fee"),
      ("", "Wherever you choose to build"),
      ("no", "You source, build and run the timeline"),
      ("partial", "General content. A slipped build moves the deduction a year"),
      ("partial", "Student results, not closings"),
      ("no", "Course plus build oversight. 6-18 months")],
     ["speed", "screen", "tax"]),

    ("bnb-accelerator-vs-airbnb-arbitrage", "Airbnb Arbitrage", "AA",
     "Arbitrage is the cheapest way into the business and it cannot offset W-2 income, because you "
     "hold a lease rather than an asset. BNB Accelerator buys the building, which is what makes "
     "depreciation and cost segregation possible.",
     [("partial", "Lease a unit, sublet it nightly"),
      ("yes", "Low entry: roughly $15K-$35K per unit"),
      ("", "Wherever landlords permit subletting"),
      ("no", "You find the unit and sign the lease"),
      ("no", "No ownership, so nothing to depreciate"),
      ("partial", "Varies entirely by operator"),
      ("no", "Fully hands-on operating business")],
     ["deed", "tax", "record"]),

    ("bnb-accelerator-vs-turnkey-providers", "Turnkey Providers", "TK",
     "Both routes end with you owning a property. The difference is which side of the table the "
     "provider sits on: a turnkey provider is generally selling its own inventory, while we are "
     "paid by you to negotiate against a third-party seller.",
     [("partial", "Sells you a finished property, frequently their own"),
      ("no", "Margin embedded in the purchase price"),
      ("", "Wherever their inventory happens to sit"),
      ("partial", "Sourcing done, but only from their stock"),
      ("partial", "Varies by provider"),
      ("partial", "Varies by provider"),
      ("yes", "Hands-off, and they are on the sell side")],
     ["buyside", "screen", "tax"]),

    ("bnb-accelerator-vs-property-manager", "A Property Manager", "PM",
     "These two do not compete: we buy the property, a manager runs it afterwards. The order "
     "matters, because a full-service agreement signed before you speak to a CPA can defeat the "
     "material participation the deduction depends on.",
     [("partial", "Operates the property after you own it"),
      ("no", "15-25% of gross revenue, ongoing"),
      ("", "The markets they already operate in"),
      ("no", "None. They engage after closing"),
      ("no", "Full service can defeat material participation"),
      ("partial", "Measured in doors managed"),
      ("yes", "Hands-off operations, near zero of your time")],
     ["tax", "buyside", "record"]),

    ("bnb-accelerator-vs-real-estate-agent", "A Real Estate Agent", "RE",
     "A good agent is paid to close a transaction; an acquisition service is paid to find a "
     "property that underwrites. Most of our purchases still involve a local agent &mdash; the "
     "difference is who runs the revenue model, the regulatory check and the average-stay analysis.",
     [("partial", "Represents you in the transaction"),
      ("partial", "Commission, customarily paid through the sale"),
      ("", "The market they are licensed in"),
      ("partial", "Sourcing and offers. Revenue modelling rarely included"),
      ("no", "Out of scope"),
      ("partial", "Ask how many STR closings in 24 months"),
      ("partial", "The underwriting still lands on you")],
     ["buyside", "screen", "tax"]),

    ("avery-carl-short-term-shop", "The Short Term Shop", "STS",
     "The Short Term Shop is a specialist brokerage with a considerably wider footprint than ours "
     "and no separate buyer fee. We are engaged and paid by you, which is what lets us kill roughly "
     "98% of what we screen and tell you to walk away.",
     [("partial", "Specialist real estate brokerage"),
      ("yes", "Commission, customarily from the seller side"),
      ("yes", "20+ markets nationwide, wider than ours"),
      ("partial", "Sourcing, showings, offers, transaction support"),
      ("no", "Outside a brokerage engagement"),
      ("yes", "Established brokerage, large closing volume"),
      ("partial", "Agent representation. Analysis stays with you")],
     ["buyside", "screen", "tax"]),

    ("techvestor", "Techvestor", "TV",
     "Techvestor is genuinely passive, and being passive is exactly why it generally cannot put "
     "depreciation against your salary. BNB Accelerator ends with the deed in your name, which is "
     "the structure the W-2 offset depends on.",
     [("partial", "Passive fund for accredited investors"),
      ("partial", "~$25K minimum, capital locked roughly 5 years"),
      ("", "Chosen by the fund, not by you"),
      ("no", "You do not select a property"),
      ("no", "Passive treatment. Generally no W-2 offset"),
      ("partial", "Fund-level, reported around 8-12% cash-on-cash"),
      ("yes", "Fully hands-off. You own units, not a deed")],
     ["deed", "tax", "record"]),

    ("michael-elefante", "Michael Elefante", "ME",
     "BNB Investor Academy teaches the whole business, including low-capital routes like arbitrage "
     "that we do not touch. BNB Accelerator does the acquisition for you and builds it around the "
     "tax outcome &mdash; capital required, learning curve optional.",
     [("partial", "Coaching and mentorship"),
      ("partial", "Program fee, typically quoted on a call"),
      ("", "You choose and research your own"),
      ("no", "You source, model and negotiate"),
      ("partial", "Taught in the curriculum, execution is yours"),
      ("partial", "Reports 3,000+ students"),
      ("no", "Course. Also covers arbitrage and co-hosting")],
     ["speed", "screen", "tax"]),

    ("str-profit-academy", "The STR Profit Academy", "PA",
     "STR Profit Academy is about running a property well. BNB Accelerator is about buying the "
     "right one. If you already own and are underperforming, the course is the better spend and we "
     "would tell you so.",
     [("partial", "Online course and community on operations"),
      ("partial", "Course fee, with a stated 30-day guarantee"),
      ("", "Not market-specific"),
      ("no", "Covers operations, not acquisition"),
      ("partial", "Not the focus of the curriculum"),
      ("partial", "Founded by established STR educators"),
      ("no", "Course. You run the property")],
     ["screen", "tax", "record"]),

    ("str-university", "STR University", "SU",
     "STR University teaches you to do this yourself in a cohort with real accountability. BNB "
     "Accelerator does it for you on your own timeline. If your gap is knowledge, buy the cohort; "
     "if your gap is time, buy the service.",
     [("partial", "Cohort-based training"),
      ("partial", "Cohort fee, varies by intake and tier"),
      ("", "You choose and research your own"),
      ("no", "You source, model and negotiate"),
      ("partial", "Covered conceptually"),
      ("partial", "Measured in students, not closings"),
      ("no", "Course, on the cohort's schedule")],
     ["speed", "screen", "tax"]),

    ("airdna", "AirDNA", "AD",
     "AirDNA sells the numbers; we sell the decision and the closing. They are not alternatives "
     "&mdash; plenty of our clients keep an AirDNA subscription to check our models independently, "
     "which we encourage.",
     [("partial", "Data and analytics platform"),
      ("yes", "Roughly $40 to $200+ a month by tier"),
      ("yes", "National data coverage"),
      ("no", "Stops at information"),
      ("no", "Not addressed"),
      ("partial", "A tool, not a transacting firm"),
      ("no", "You interpret the numbers and act")],
     ["screen", "buyside", "speed"]),

    ("rabbu", "Rabbu", "RB",
     "Rabbu is free and genuinely useful for early screening, and an automated estimate is not "
     "underwriting. Use Rabbu to explore, then use an acquisition service once you have decided to "
     "buy.",
     [("partial", "Free data platform and marketplace"),
      ("yes", "Free for core data"),
      ("yes", "Any US address, instantly"),
      ("partial", "Marketplace listings and related services"),
      ("no", "Not addressed"),
      ("partial", "A tool, not a transacting firm"),
      ("no", "You interpret the estimate and act")],
     ["screen", "buyside", "speed"]),

    ("awning", "Awning", "AW",
     "Awning covers a wider national footprint and leads with a platform experience. We stay in "
     "eight states on purpose, because negotiation leverage and management pairing run on local "
     "relationships that do not transfer between markets.",
     [("partial", "STR investment platform with services layered on"),
      ("partial", "Confirm the current fee structure directly"),
      ("yes", "Broad national coverage"),
      ("partial", "Platform-driven analytics plus services"),
      ("partial", "Generally left to your own advisor"),
      ("partial", "Confirm current scope directly"),
      ("partial", "Platform-first experience")],
     ["buyside", "screen", "tax"]),

    ("alpha-geek-capital", "Alpha Geek Capital", "AG",
     "A partnership lowers the capital per deal and shares the operational load, at the cost of "
     "control, exit timing and a tax position that cannot be assumed. Sole ownership costs more "
     "upfront and keeps all three with you.",
     [("partial", "Partnership and investment program"),
      ("partial", "Shared capital, governed by the agreement"),
      ("", "Chosen by the sponsor"),
      ("partial", "Sponsor-led, with shared control"),
      ("no", "Depends on structure. Never assume it transfers"),
      ("partial", "Sponsor track record, verify directly"),
      ("partial", "Shared. Exit is not unilateral")],
     ["deed", "tax", "record"]),

    ("real-estate-robinsons", "The Real Estate Robinsons", "RR",
     "The Robinsons are genuinely strong for beginners, including people who have not raised "
     "capital yet. We are built for buyers whose capital is already ready &mdash; if you are not "
     "there yet, education is the better spend and we would say so.",
     [("partial", "Coaching, bootcamp and live events"),
      ("partial", "Program and event fees"),
      ("", "You choose and research your own"),
      ("no", "You source, model and negotiate"),
      ("partial", "Covered conceptually in the curriculum"),
      ("partial", "Documented personal portfolio, student results"),
      ("no", "Course and community. Beginner friendly")],
     ["speed", "screen", "tax"]),

    ("rent-to-retirement", "Rent to Retirement", "R2R",
     "Rent to Retirement is strong for turnkey long-term rentals across a wide footprint. A "
     "long-term rental is a passive activity, so if the point is offsetting a large W-2 bill, the "
     "seven-day short-term structure is the one that does it.",
     [("partial", "Turnkey provider, predominantly long-term rentals"),
      ("no", "Margin embedded in the purchase price"),
      ("yes", "Wide national footprint"),
      ("partial", "You choose from inventory they prepared"),
      ("no", "Long-term rentals are passive. No W-2 offset"),
      ("partial", "Established turnkey volume"),
      ("yes", "Hands-off, management usually bundled")],
     ["buyside", "tax", "deed"]),

    ("zuubly", "Zuubly", "ZU",
     "Zuubly publishes reviews of other people's programs; it is not an investing service at all. "
     "Read it while you work out what kind of help you want, then engage someone to execute.",
     [("partial", "Review and comparison website"),
      ("yes", "Free to read. Commonly affiliate-funded"),
      ("", "Not applicable. It is a publisher"),
      ("no", "None. It publishes reviews"),
      ("no", "Not addressed"),
      ("partial", "A publisher, not a transacting firm"),
      ("no", "Reading. You still do everything")],
     ["screen", "buyside", "record"]),
]

# The buying guides live under /compare/ too but are roundups rather than
# matchups, so they sit in a plain link row instead of the card menu.
GUIDES = [
    ("/compare/best-done-for-you-airbnb-companies/", "Best done-for-you Airbnb companies"),
    ("/compare/best-str-investing-programs/", "Best STR investing programs"),
    ("/compare/best-airbnb-coaching-programs/", "Best Airbnb coaching programs"),
    ("/compare/best-str-markets-for-cash-flow/", "Best STR markets for cash flow"),
    ("/compare/best-states-for-str-investing/", "Best states for STR investing"),
    ("/compare/best-str-financing-options/", "Best STR financing options"),
]


def usd(n):
    return f"${n:,.0f}"


def mark(kind, text):
    """Wrap a cell in the check / cross / partial treatment."""
    return f'<span class="{kind}">{text}</span>' if kind else text


def icon(key):
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[key]}</svg>')


def table_html(name, them):
    rows = []
    for label, (uk, ut), (tk, tt) in zip(ROW_LABELS, US, them):
        rows.append(f"""            <tr>
              <th scope="row">{label}</th>
              <td class="us" data-label="BNB Accelerator">{mark(uk, ut)}</td>
              <td data-label="{tpl.esc(name)}">{mark(tk, tt)}</td>
            </tr>""")
    return f"""      <div class="table-scroll cmp-table-wrap" data-reveal>
        <table class="compare cmp-table">
          <caption class="sr-only">BNB Accelerator compared with {tpl.esc(name)} across approach, pricing, markets, deal support, tax strategy, track record and how hands-on each one is</caption>
          <thead>
            <tr>
              <th scope="col"><span class="sr-only">Feature</span></th>
              <th scope="col" class="us">BNB Accelerator</th>
              <th scope="col">{tpl.esc(name)}</th>
            </tr>
          </thead>
          <tbody>
{chr(10).join(rows)}
          </tbody>
        </table>
      </div>"""


def diffs_html(keys):
    cards = []
    for i, k in enumerate(keys):
        head, body = DIFFS[k]
        delay = f' data-reveal-delay="{i}"' if i else ""
        cards.append(f"""        <article class="card card-static" data-reveal{delay}>
          <div class="card-icon">{icon(k)}</div>
          <h3>{head}</h3>
          <p>{body}</p>
        </article>""")
    return "\n".join(cards)


# Deals with a documented double-digit return, used two per page so the proof
# is real rather than the same pair nineteen times. The aggregate line below
# them keeps the average honest.
PROOF_POOL = [d for d in DEALS if d["coc"] >= 12]


def proof_html(index):
    picks = [PROOF_POOL[(index * 2) % len(PROOF_POOL)],
             PROOF_POOL[(index * 2 + 1) % len(PROOF_POOL)]]
    out = []
    for i, d in enumerate(picks):
        yr = f'<span class="deal-year">{d["year"]}</span>' if d["year"] else ""
        delay = f' data-reveal-delay="{i}"' if i else ""
        out.append(f"""        <article class="deal-card" data-reveal{delay}>
          <div class="deal-head">
            <h3>{tpl.esc(d['client'])}</h3>
            {yr}
          </div>
          <a class="deal-market" href="/markets/{d['market_slug']}/">{tpl.esc(d['market'])}</a>
          <ul class="spec-list">
            <li><span class="k">Purchase price</span><span class="v">{usd(d['price'])}</span></li>
            <li><span class="k">Total entry cost</span><span class="v">{usd(d['entry'])}</span></li>
            <li><span class="k">Annual cash flow</span><span class="v green">{usd(d['cash_flow'])}</span></li>
            <li><span class="k">Cash-on-cash return</span><span class="v green">{d['coc']:.2f}%</span></li>
          </ul>
        </article>""")
    return "\n".join(out)


def faq_html(faqs):
    out = []
    for q, a in faqs:
        out.append(f"""        <details class="faq">
          <summary>{q}</summary>
          <div class="faq-answer"><p>{a}</p></div>
        </details>""")
    return "\n".join(out)


def page_body(name, verdict, them, keys, faqs, index):
    trail = [("Home", "/"), ("Compare", "/compare/"), (f"vs {name}", None)]
    crumb = ('<nav class="breadcrumb" aria-label="Breadcrumb">'
             '<a href="/">Home</a><span class="sep">/</span>'
             '<a href="/compare/">Compare</a><span class="sep">/</span>'
             f'<span>vs {tpl.esc(name)}</span></nav>')
    return f"""
  <section class="hero hero-page">
    <div class="wrap">
      {crumb}
      <div class="hero-inner">
        <span class="eyebrow">Comparison</span>
        <h1>BNB Accelerator vs {tpl.esc(name)}</h1>
      </div>
    </div>
  </section>

  <section class="section-sm">
    <div class="wrap wrap-narrow">
      <div class="verdict" data-reveal>
        <span class="verdict-label">Quick verdict</span>
        <p>{verdict}</p>
      </div>
    </div>
  </section>

  <section class="bg-alt">
    <div class="wrap wrap-narrow">
      <div class="section-head center" data-reveal>
        <span class="eyebrow">Side by side</span>
        <h2>The short version</h2>
      </div>
{table_html(name, them)}
      <p class="small text-muted mt-3" data-reveal>{TRADEMARK}</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="section-head center" data-reveal>
        <span class="eyebrow">What is different</span>
        <h2>Why buyers choose us</h2>
      </div>
      <div class="grid grid-3">
{diffs_html(keys)}
      </div>
    </div>
  </section>

  <section class="bg-alt">
    <div class="wrap wrap-narrow">
      <div class="section-head center" data-reveal>
        <span class="eyebrow">Client results</span>
        <h2>Two real closings</h2>
      </div>
      <div class="cmp-proof">
{proof_html(index)}
      </div>
      <p class="small text-muted mt-3 center" data-reveal>Across the {AGG['deals']} deals we publish with full financials, the average cash-on-cash return is {AGG['avg_coc']}% and the median is {AGG['median_coc']}%. Individual results are not typical or promised. <a href="/deals/">See all {AGG['deals']} deals</a>.</p>
    </div>
  </section>

  <section class="section-sm">
    <div class="wrap wrap-narrow">
      <h2 class="center" data-reveal>Questions buyers ask</h2>
      <div data-reveal>
{faq_html(faqs)}
      </div>
    </div>
  </section>
{tpl.cta_band("Ready to see the difference?",
              "Thirty minutes on the phone covers your income, your tax position, and whether a "
              "property in one of our markets actually fits what you are trying to do.",
              primary=("/apply/", "Book a Call"),
              secondary=("/compare/", "Compare another option"))}"""


def build_matchup(slug, name, verdict, them, keys, index):
    meta = DATA[slug]
    path = f"/compare/{slug}/"
    faqs = meta["faqs"]
    article = f"""    {{
      "@type": "Article",
      "headline": "BNB Accelerator vs {tpl.esc(name)}",
      "description": "{tpl.esc(meta['description'])}",
      "url": "{tpl.SITE}{path}",
      "mainEntityOfPage": {{ "@type": "WebPage", "@id": "{tpl.SITE}{path}" }},
      "datePublished": "{PUB}",
      "dateModified": "{MOD}",
      "image": "{tpl.SITE}/assets/og-image.svg",
      "articleSection": "Comparison",
      "inLanguage": "en-US",
      "author": {{ "@type": "Organization", "name": "My BnB Accelerator, LLC", "url": "https://mybnbaccelerator.com/" }},
      "publisher": {{ "@id": "https://mybnbaccelerator.com/#organization" }},
      "isPartOf": {{ "@id": "https://mybnbaccelerator.com/#website" }}
    }}"""
    schema = tpl.graph(
        article,
        tpl.breadcrumb_schema([("Home", "/"), ("Compare", "/compare/"), (f"vs {name}", path)]),
        tpl.ORG_SCHEMA,
    ) + "\n" + tpl.faq_schema([(q, a) for q, a in faqs])

    write(path, tpl.page(
        title=meta["title"],
        description=meta["description"],
        path=path,
        body=page_body(name, verdict, them, keys, faqs, index),
        extra_schema=schema,
        active="/compare/",
        transparent=True,
        og_title=f"BNB Accelerator vs {name}",
    ))


def build_index():
    cards = []
    for i, (slug, name, initials, *_ ) in enumerate(COMPETITORS):
        delay = f' data-reveal-delay="{i % 4}"' if i % 4 else ""
        cards.append(f"""        <a class="cmp-card" href="/compare/{slug}/" data-reveal{delay}>
          <span class="cmp-mark" aria-hidden="true">{initials}</span>
          <span class="cmp-card-body">
            <h3>{tpl.esc(name)}</h3>
            <span class="cmp-go">View Comparison</span>
          </span>
        </a>""")

    guides = "\n".join(f'        <li><a href="{u}">{t}</a></li>' for u, t in GUIDES)

    items = ",\n".join(
        f"""        {{ "@type": "ListItem", "position": {i}, "name": "BNB Accelerator vs {tpl.esc(name)}", "url": "{tpl.SITE}/compare/{slug}/" }}"""
        for i, (slug, name, *_ ) in enumerate(COMPETITORS, 1))
    itemlist = ('    {\n      "@type": "ItemList",\n'
                f'      "name": "BNB Accelerator comparisons",\n'
                f'      "numberOfItems": {len(COMPETITORS)},\n'
                '      "itemListElement": [\n' + items + "\n      ]\n    }")

    schema = tpl.graph(
        itemlist,
        tpl.breadcrumb_schema([("Home", "/"), ("Compare", "/compare/")]),
        tpl.ORG_SCHEMA,
    )

    body = f"""
  <section class="hero hero-page">
    <div class="wrap">
      <nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a><span class="sep">/</span><span>Compare</span></nav>
      <div class="hero-inner">
        <span class="eyebrow">Comparison</span>
        <h1>How BNB Accelerator Compares</h1>
        <p class="lead">Pick anyone you are weighing us against and see the two of us side by side.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="cmp-grid">
{chr(10).join(cards)}
      </div>
    </div>
  </section>

  <section class="section-sm bg-alt">
    <div class="wrap">
      <div class="section-head center" data-reveal>
        <span class="eyebrow">Buying guides</span>
        <h2>Sorting a whole category</h2>
      </div>
      <ul class="cmp-guides" data-reveal>
{guides}
      </ul>
    </div>
  </section>
{tpl.cta_band("Still deciding which model fits?",
              "Tell us your income, your timeline and your capital position, and we will tell you "
              "honestly whether we are the right answer.",
              primary=("/apply/", "Book a Call"),
              secondary=("/deals/", "See the deal tracker"))}"""

    write("/compare/", tpl.page(
        title="How BNB Accelerator Compares: 19 Honest Comparisons (2026)",
        description=("Compare BNB Accelerator against courses, coaching programs, turnkey "
                     "providers, brokerages, data platforms, funds and property managers. One "
                     "clean side-by-side page per option."),
        path="/compare/",
        body=body,
        extra_schema=schema,
        active="/compare/",
        transparent=True,
    ))


def main():
    build_index()
    for i, (slug, name, _initials, verdict, them, keys) in enumerate(COMPETITORS):
        build_matchup(slug, name, verdict, them, keys, i)
    print(f"compare: index + {len(COMPETITORS)} matchup pages")


if __name__ == "__main__":
    main()
