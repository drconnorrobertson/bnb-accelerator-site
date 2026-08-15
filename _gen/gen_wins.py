#!/usr/bin/env python3
"""Build /wins/ from the client win graphics.

Captions are transcribed from the graphics themselves, so every figure on the
page is a figure the client's own card already displays. Nothing is inferred
and nothing is rounded up. Images are never cropped: the cards are a fixed
aspect box with object-fit: contain over the graphic's own edge colour.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tpl
from pillars import write

HERE = os.path.dirname(os.path.abspath(__file__))

# slug -> (client, location, headline, [stat, stat, ...], optional case study slug)
WINS = {
    "adam-shar": ("Adam Shar", "Sevierville, Tennessee",
                  "4.72 star rating with over 90 reviews",
                  ["4.72 stars", "90+ reviews"], "adam-sevierville-tn-4br"),
    "alfredo-and-millie": ("Alfredo &amp; Millie Nuno", "Sevierville, Tennessee",
                           "Guest Favorite with a 5 star rating and over $59,000 in annual revenue",
                           ["5.0 stars", "$59,000+ annual revenue", "Guest Favorite"],
                           "alfredo-millie-sevierville-tn-4br"),
    "antonio": ("Antonio", "Fort Myers, Florida",
                "From launch to fully booked, performing like a veteran listing",
                ["4.82 stars", "39 reviews", "6BR, sleeps 16+"],
                "antonio-fort-myers-fl-6br"),
    "antonio-alvarez": ("Antonio Alvarez", "Santa Rosa Beach, Florida",
                        "Over $172,000 in annual revenue at 51% occupancy",
                        ["$172,000+ annual revenue", "51% occupancy", "4.79 stars"], None),
    "bao-le": ("Bao Le", None, "Two Airbnbs in seven months",
               ["2 properties", "7 months"], None),
    "barry": ("Barry McPherson", None, "Two Airbnbs in four months",
              ["2 properties", "4 months"], None),
    "ben-feldman": ("Ben Feldman", None, "Two Airbnbs in seven months",
                    ["2 properties", "7 months"], None),
    "dr-jonathan-goodwin": ("Dr. Jonathan Goodwin", None,
                            "Two Airbnbs in nine months",
                            ["2 properties", "9 months"], None),
    "dr-marcos": ("Dr. Marcos Naccarati", None, "Nineteen Airbnbs in three years",
                  ["19 properties", "3 years"], None),
    "dustin": ("Dustin Ward", "Branson West, Missouri",
               "Zero vacancies from day one, launched fully booked",
               ["Fully booked at launch"], "dustin-branson-west-mo-8br"),
    "eino": ("Eino", "Bennington, Nebraska",
             "Superhost at 61% occupancy on a $332 average daily rate",
             ["4.82 stars", "61% occupancy", "$332 ADR", "Superhost"], None),
    "ganesh-joshi": ("Ganesh Joshi", None,
                     "Guest Favorite with a 5 star rating and a 66% occupancy rate",
                     ["5.0 stars", "66% occupancy", "Guest Favorite"], None),
    "hari-mukkala": ("Hari Mukkala", "Ridgedale, Missouri",
                     "Almost $200,000 in annual revenue at a $691 average daily rate",
                     ["~$200,000 annual revenue", "54% occupancy", "$691 ADR", "4.95 stars"], None),
    "james-brezinski": ("James Brezinski", None,
                        "Guest Favorite with a 4.89 star rating and over $88,000 in annual revenue",
                        ["4.89 stars", "$88,000+ annual revenue", "Guest Favorite"], None),
    "james-green": ("James Green", None, "Two Airbnbs in three months",
                    ["2 properties", "3 months"], None),
    "jason-hoop": ("Jason Hoop", "Branson, Missouri",
                   "Over $123,000 in annual revenue at 62% occupancy",
                   ["$123,000+ annual revenue", "62% occupancy", "4.97 stars"], None),
    "joe-sangiovanni": ("Joe Sangiovanni", "Kissimmee, Florida",
                        "Booked out quickly and cash-flowing from launch",
                        ["Cash-flowing at launch"], None),
    "joseph": ("Joseph Sangiovanni", None, "Two Airbnbs in eight months",
               ["2 properties", "8 months"], None),
    "jonathan-nassos": ("Jonathan Nassos", None,
                        "Guest Favorite with a 5 star rating and over $120,000 in annual revenue",
                        ["5.0 stars", "$120,000+ annual revenue", "Guest Favorite"], None),
    "jonathan-nassos-branson": ("Jonathan Nassos", "Branson, Missouri",
                                "A $424 average daily rate in a tourism hub",
                                ["$424 ADR", "4.67 stars"], None),
    "jonathan-nassos-broken-bow": ("Jonathan Nassos", "Broken Bow, Oklahoma",
                                   "Over $60,000 in annual revenue at a $388 average daily rate",
                                   ["$60,000+ annual revenue", "$388 ADR", "4.94 stars"],
                                   "joe-s-broken-bow-ok-and-destin-fl"),
    "joseph-yi": ("Joseph Yi", None,
                  "50% occupancy with over $100,000 in annual revenue",
                  ["$100,000+ annual revenue", "50% occupancy"], None),
    "josiah": ("Dr. Josiah Fitzsimmons", None, "Twenty-three Airbnbs in three years",
               ["23 properties", "3 years"], None),
    "justin-thompson": ("Justin Thompson", "Broken Bow, Oklahoma",
                        "Upscale price tier, Guest Favorite at 58% occupancy",
                        ["$61,000+ annual revenue", "58% occupancy", "Guest Favorite"], None),
    "kenneth-mcpherson": ("Kenneth McPherson", "South Padre Island, Texas",
                          "Over $144,000 in annual revenue at 71% occupancy",
                          ["$144,000+ annual revenue", "71% occupancy", "Guest Favorite"], None),
    "levi": ("Levi", None, "A $16,037.98 booking in month four",
             ["$16,037.98 single booking", "Month 4"], None),
    "manasa-and-som": ("Manasa &amp; Som", "Ridgedale, Missouri",
                       "Over $62,000 in annual revenue at a $576 average daily rate",
                       ["$62,000+ annual revenue", "44% occupancy", "$576 ADR", "4.95 stars"], None),
    "manasa-dintyala": ("Manasa Dintyala", None,
                        "50% occupancy with over $100,000 in annual revenue",
                        ["$100,000+ annual revenue", "50% occupancy"], None),
    "mario-sanchez": ("Mario Sanchez", None,
                      "66% occupancy with over $77,000 in annual revenue",
                      ["$77,000+ annual revenue", "66% occupancy"], None),
    "max": ("Max Rosenblatt", None,
            "4.85 star rating with over $50,000 in annual revenue",
            ["4.85 stars", "$50,000+ annual revenue"], None),
    "michael-bishop": ("Michael Bishop", None, "Two Airbnbs in five months",
                       ["2 properties", "5 months"], None),
    "mohammad-amin": ("Mohammad Amin, PhD", None, "First Airbnb live",
                      ["First property"], None),
    "murali": ("Murali", "Boone, North Carolina",
               "Fully booked in August on a $1,200 average daily rate",
               ["$185,000+ annual revenue", "$1,200 ADR", "5.0 stars"], None),
    "peter-eck": ("Peter Eck", None,
                  "An IBM Associate Partner on his sixth property with us",
                  ["6 properties", "4 years"], "peter-eck-ibm-partner-six-properties"),
    "peter-eck-santa-rosa-beach": ("Peter Eck", "Santa Rosa Beach, Florida",
                                   "68% occupancy in one of the top five US coastal ADR markets",
                                   ["$100,000+ annual revenue", "68% occupancy", "4.83 stars"],
                                   "peter-eck-ibm-partner-six-properties"),
    "prince-joseph": ("Prince Joseph", "Charlotte, North Carolina",
                      "Over $65,000 in annual revenue at a $492 average daily rate",
                      ["$65,000+ annual revenue", "44% occupancy", "$492 ADR"], None),
    "rachel-withers": ("Rachel Withers", None,
                       "A $1,765,000 purchase, featured on a historic society garden tour",
                       ["$1,765,000 property"], None),
    "randy-and-lorelai": ("Randy &amp; Lorelai", "Mesa, Arizona",
                          "Twelve months in, still cash-flowing and holding Superhost status",
                          ["12 months", "Superhost", "Still cash-flowing"], None),
    "randy-lansang": ("Randy Lansang", None,
                      "Guest Favorite with a 4.96 star rating and over $110,000 in annual revenue",
                      ["4.96 stars", "$110,000+ annual revenue", "Guest Favorite"], None),
    "sara-olson": ("Sara Olson", "Panama City Beach, Florida",
                   "$141,000 in annual revenue at 50% occupancy",
                   ["$141,000 annual revenue", "50% occupancy", "48 market score"], None),
    "shardul": ("Shardul", "Panama City Beach, Florida",
                "$35,900 in bookings in under 67 days, tracking above projection",
                ["$35.9K in 67 days", "72% occupancy", "$748 ADR", "Guest Favorite"],
                "shardul-mayanka-panama-city-beach-fl"),
    "tom": ("Tom", "Freeland, Pennsylvania",
            "A 77 market score luxury home at a $1,100 average daily rate",
            ["77 market score", "$1,100 ADR"], None),
    "vina-rodriguez": ("Vina Rodriguez", None,
                       "Closing day, adding a Georgia property to the portfolio",
                       ["Portfolio addition"], None),
    "ac-blast": ("Four clients", None,
                 "88%, 93% and 96% occupancy across four client properties",
                 ["88% occupancy", "93% occupancy", "96% occupancy"], None),
    "client": (None, None,
               "$23,035.17 in a single month at 93% occupancy",
               ["$23,035.17 in a month", "93% occupancy", "$799.70 ADR"], None),
    "win": ("James", None,
            "This property transformed our relationship with money",
            ["Client testimonial"], None),
}

# Cards leading the grid, in this order. Strong numbers and named clients first.
FEATURED = ["hari-mukkala", "murali", "antonio-alvarez", "sara-olson",
            "kenneth-mcpherson", "jason-hoop", "randy-lansang", "shardul",
            "peter-eck-santa-rosa-beach", "james-brezinski", "dr-marcos", "josiah"]


def card(slug, m, featured=False):
    client, loc, headline, stats, cs = WINS[slug]
    who = client or "BNB Accelerator client"
    alt = f"{who} client result: {headline}"
    if loc:
        alt = f"{who}, {loc}. {headline}"
    chips = "".join(f'<span class="win-stat">{s}</span>' for s in stats)
    meta = f'<span class="win-loc">{loc}</span>' if loc else ""
    link = (f'<a class="win-cs" href="/case-studies/{cs}/">Read the full case study</a>'
            if cs else "")
    cls = "win-card"
    return f"""        <figure class="{cls}" style="--win-bg:#{m['bg']}">
          <button class="win-shot" type="button" data-win-open
                  data-full="/assets/wins/{slug}.jpg"
                  data-caption="{tpl.esc(who + (' - ' + loc if loc else '') + '. ' + headline)}"
                  aria-label="Enlarge: {tpl.esc(alt)}">
            <img src="/assets/wins/{slug}-card.jpg" alt="{tpl.esc(alt)}"
                 width="{m['card_w']}" height="{m['card_h']}" loading="lazy" decoding="async">
          </button>
          <figcaption class="win-body">
            <h3>{who}</h3>
            {meta}
            <p>{headline}</p>
            <div class="win-stats">{chips}</div>
            {link}
          </figcaption>
        </figure>"""


def main():
    man = json.load(open(os.path.join(HERE, "wins_manifest.json")))
    by_slug = {m["slug"]: m for m in man}
    missing = [s for s in by_slug if s not in WINS]
    if missing:
        print(f"  no caption for: {missing}")

    order = [s for s in FEATURED if s in by_slug]
    order += [s for s in sorted(by_slug) if s not in order]

    cards = [card(s, by_slug[s], featured=(i < 2)) for i, s in enumerate(order)]
    n = len(cards)

    trail = [("Home", "/"), ("Client Wins", "/wins/")]
    faqs = [
        ("Are these results typical?",
         "No. Each graphic shows the actual reported result for one specific property, published with that client's permission. They are not typical, not projections, and not a promise of what any other property will do. Results depend on purchase price, financing, market performance, management quality and your own tax situation."),
        ("Where do these numbers come from?",
         "From the clients' own listing dashboards and booking platforms. Revenue, occupancy, average daily rate and review scores are the figures the platform reported for that property over the stated period."),
        ("Can I speak to any of these clients?",
         "Yes. Ask for references on your first call and we will connect you with clients who bought in situations comparable to yours. Our repeat buyer rate is about 80%, and several of the people on this page have bought more than once."),
        ("Why do some cards show no revenue figure?",
         "Because we only publish what the client authorised and what their dashboard supports. Some cards show a milestone, such as a second or nineteenth property, rather than a revenue number."),
    ]

    schema = tpl.graph(
        tpl.breadcrumb_schema(trail),
        f"""    {{
      "@type": "CollectionPage",
      "name": "BNB Accelerator Client Wins",
      "description": "{n} documented client results: revenue, occupancy, average daily rate and review scores from BNB Accelerator client properties.",
      "url": "{tpl.SITE}/wins/",
      "isPartOf": {{ "@id": "https://mybnbaccelerator.com/#website" }}
    }}""",
        tpl.ORG_SCHEMA,
    ) + "\n" + tpl.faq_schema(faqs) + "\n" + tpl.graph(
        '    {\n      "@type": "ImageGallery",\n      "name": "BNB Accelerator Client Wins",\n'
        '      "url": "' + tpl.SITE + '/wins/",\n      "associatedMedia": [\n' +
        ",\n".join(
            f'        {{ "@type": "ImageObject", "contentUrl": "{tpl.SITE}/assets/wins/{s}.jpg", '
            f'"caption": "{tpl.esc((WINS[s][0] or "BNB Accelerator client") + ". " + WINS[s][2])}" }}'
            for s in order) +
        "\n      ]\n    }")

    body = f"""
  <section class="hero hero-page">
    <div class="wrap">
      {tpl.breadcrumb_html(trail)}
      <div class="hero-inner">
        <span class="eyebrow">Client Wins</span>
        <h1>{n} client results, straight from their dashboards</h1>
        <p class="hero-sub">Revenue, occupancy, average daily rate and review scores from real BNB Accelerator properties, published with each client's permission. Every number below is one the client's own listing reported.</p>
        <div class="btn-row">
          <a class="btn btn-accent btn-lg" href="/apply/">Apply Now</a>
          <a class="btn btn-ghost-light btn-lg" href="/case-studies/">Read the full case studies</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section-sm">
    <div class="wrap">
      <div class="stats-bar">
        <div class="stat"><span class="stat-num">500+</span><span class="stat-label">Homes closed</span></div>
        <div class="stat"><span class="stat-num">260+</span><span class="stat-label">Clients served</span></div>
        <div class="stat"><span class="stat-num">80%</span><span class="stat-label">Repeat buyer rate</span></div>
        <div class="stat"><span class="stat-num">{n}</span><span class="stat-label">Results on this page</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="win-grid">
{chr(10).join(cards)}
      </div>
      <p class="disclaimer mt-4">Each graphic shows the actual reported result for one specific property, published with that client's permission. These are not typical, not projections, and not a promise of what any other property will do. Real estate involves risk, including loss of principal.</p>
    </div>
  </section>

  <section class="bg-alt">
    <div class="wrap wrap-narrow">
      <article class="article">
{tpl.faq_html(faqs)}
        <div class="callout">
          <h3>Keep reading</h3>
          <ul>
            <li><a href="/case-studies/">The full case studies, with purchase prices and underwriting</a></li>
            <li><a href="/testimonials/">Written testimonials and Trustpilot reviews</a></li>
            <li><a href="/how-it-works/">How the acquisition process works</a></li>
            <li><a href="/markets/">The markets these properties are in</a></li>
          </ul>
        </div>
      </article>
    </div>
  </section>

  <div class="win-lightbox" data-win-lightbox hidden>
    <button class="win-lightbox-close" type="button" data-win-close aria-label="Close">&times;</button>
    <figure>
      <img src="" alt="" data-win-img>
      <figcaption data-win-cap></figcaption>
    </figure>
  </div>
{tpl.cta_band(
    "Want your own numbers on this page?",
    "A thirty minute call covers your income, your tax position, and which markets actually fit what you are trying to do.",
    ("/apply/", "Apply Now"),
    ("/case-studies/", "See the case studies"))}"""

    write("/wins/", tpl.page(
        title=f"Client Wins: {n} Real BNB Accelerator Results (2026)",
        description=f"{n} documented BNB Accelerator client results with revenue, occupancy, ADR and review scores, published with each client's permission.",
        path="/wins/",
        body=body,
        extra_schema=schema,
        active="/wins/",
        transparent=True,
        og_title="Client Wins | Real BNB Accelerator Results",
        og_desc="Revenue, occupancy and review scores from real client properties.",
    ))
    print(f"wins: {n} cards")
    return order, by_slug


if __name__ == "__main__":
    main()
