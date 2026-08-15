#!/usr/bin/env python3
"""Compose one post per market per year, 2021 to 2026.

Each post draws on three independent sources so no two cells argue the same
thing: the year block in era.py, the market's own performance ranges pulled
from its market page, and the per-market per-year arc in market_arcs.py.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import era
from market_arcs import ARCS

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = json.load(open(os.path.join(HERE, "market_data.json")))

# Which property-type guide and state regulation page each market belongs to.
MARKET_META = {
    "austin": ("lake", "texas", "Texas"),
    "big-bear": ("ski", "california", "California"),
    "branson": ("lake", "missouri", "Missouri"),
    "broken-bow": ("mountain", "oklahoma", "Oklahoma"),
    "cape-coral": ("beach", "florida", "Florida"),
    "denver": ("city", "colorado", "Colorado"),
    "destin": ("beach", "florida", "Florida"),
    "gatlinburg": ("mountain", "tennessee", "Tennessee"),
    "gulf-shores": ("beach", "alabama", "Alabama"),
    "joshua-tree": ("desert", "california", "California"),
    "kissimmee": ("beach", "florida", "Florida"),
    "lake-tahoe": ("ski", "california", "California"),
    "nashville": ("city", "tennessee", "Tennessee"),
    "panama-city-beach": ("beach", "florida", "Florida"),
    "park-city": ("ski", "utah", "Utah"),
    "phoenix-mesa": ("desert", "arizona", "Arizona"),
    "poconos": ("lake", "pennsylvania", "Pennsylvania"),
    "scottsdale": ("desert", "arizona", "Arizona"),
    "sedona": ("desert", "arizona", "Arizona"),
    "smoky-mountains": ("mountain", "tennessee", "Tennessee"),
}

PT_LABEL = {"beach": "Beach property", "mountain": "Mountain cabin",
            "lake": "Lake house", "city": "Urban rental",
            "ski": "Ski property", "desert": "Desert property"}


def build(slug, year):
    d = DATA[slug]
    y = era.YEARS[year]
    arc = ARCS[slug][year]
    pt, state_slug, state_name = MARKET_META[slug]
    place = d["place"]
    name = d["name"]
    prev = ARCS[slug].get(year - 1)
    nxt = ARCS[slug].get(year + 1)

    lead = (f"{arc} This is what {name} looked like in {year}, what the numbers "
            f"supported, and what a buyer should have been asking before writing an offer.")

    sections = [
        (f"What {year} was, across the whole asset class", [
            f"{year} was {y['headline']}.",
            y["summary"],
            y["market_mood"],
        ]),
        (f"Where {name} sat that year", [
            arc,
            (f"The structural facts of the market did not change much across the period. "
             f"Peak season in {place}: {d['peak'] or 'an established seasonal pattern'}. "
             f"Entry prices for the kind of property we underwrite have sat in the "
             f"{d['entry']} band. What moved between {year - 1 if prev else year} and now was "
             f"the cost of financing it and the depth of the competition."),
            ("The mistake in any single year is reading that year as the trend. "
             + (f"{prev} That was the year before, and it is not the same market."
                if prev else
                "2021 was the first year of the period we track, and it was an outlier rather than a baseline.")),
        ]),
        ("The numbers the market supports", [
            "These are the ranges a well-positioned property in this market supports. They are "
            "estimates for illustration rather than a projection for any specific property, and "
            "the spread inside each range is mostly explained by basis, amenity fit and management.",
            ("table", ["Metric", "Estimated range"], [
                ["Entry price", d["entry"] or "Varies"],
                ["Average daily rate", d["adr"] or "Varies"],
                ["Annual occupancy", d["occ"] or "Varies"],
                ["Gross annual revenue", d["gross"] or "Varies"],
                ["Net cash flow after debt service", d["net"] or "Varies"],
                ["Peak season", d["peak"] or "Established seasonal pattern"],
            ]),
            ("A property at the bottom of those ranges and one at the top are rarely different "
             "properties. They are usually the same property bought at a different basis and run "
             "to a different standard."),
        ]),
        (f"What the {year} tax position did to the maths", [
            y["bonus_note"],
            y["tax_angle"],
            ("None of that changes the two conditions the strategy actually rests on. The property "
             "has to clear a seven-day average period of customer use, and the owner has to "
             "materially participate. Miss either and the loss is passive regardless of what the "
             "bonus depreciation percentage was that year."),
            ("warn", "This is an explanation of how the rules worked in that year, not tax advice. "
                     "My BnB Accelerator, LLC is a real estate acquisition firm, not a CPA firm. "
                     'Our independent partner firm is <a href="https://aetaxadvisors.com/short-term-rentals/" '
                     'target="_blank" rel="noopener">AE Tax Advisors</a>.'),
        ]),
        ("What the risk actually was", [
            y["risk"],
            (f"In {name} specifically, the thing to have checked was the regulatory position for "
             f"the exact parcel. {state_name} rules are covered in detail on the state page, and "
             f"the local layer underneath them is where deals are won or lost."),
            "We run the same six verification steps on every property before an offer, in every "
            "state and in every year: parcel zoning, whether short-term rental is an allowed use, "
            "whether permits are capped or transferable, the full association declaration, lodging "
            "tax registration, and written confirmation from the jurisdiction.",
        ]),
        ("What a buyer should have done", [
            y["advice"],
            ("The underwriting discipline does not change with the year. Twelve individual monthly "
             "revenue figures built from a comparable set you assembled yourself, a complete "
             "expense stack including reserves, and a stress test at 75% of projection that still "
             "covers debt service."),
            (f"{nxt} That is what came next, and a buyer in {year} could not have known it. "
             if nxt else
             "That is where the market stands now, and the next year is unknown in exactly the way "
             "every year on this page was unknown at the time. ") +
            "Which is the argument for a basis that survives being wrong.",
        ]),
    ]

    faqs = [
        (f"How much could you make on an Airbnb in {name} in {year}?",
         f"A well-positioned property in {place} supports gross revenue in the {d['gross']} range "
         f"at an average daily rate of {d['adr']} and occupancy of {d['occ']}. Those are estimates "
         f"for illustration rather than a projection for any specific property."),
        (f"What was bonus depreciation in {year}?",
         y["bonus_note"]),
        (f"What was the main risk in {name} in {year}?",
         y["risk"]),
    ]

    related = [
        f'<a href="/markets/{slug}/">{name} market analysis and current numbers</a>',
        f'<a href="/property-types/{pt}/">{PT_LABEL[pt]} investing guide</a>',
        f'<a href="/regulations/{state_slug}/">{state_name} short-term rental regulations</a>',
        '<a href="/revenue-projections/">Building a revenue projection you can defend</a>',
        '<a href="/topics/market-analysis/">All market analysis</a>',
    ]

    return dict(
        slug=f"{slug}-str-market-{year}",
        cluster="market-analysis",
        category="Market Analysis",
        year=year,
        title=f"{name} Short-Term Rental Market in {year}",
        h1=f"The {name} Short-Term Rental Market in {year}",
        title_tag=f"{name} STR Market {year}: Revenue, Rates and Risk",
        description=(f"What the {name} short-term rental market looked like in {year}: "
                     f"{d['gross']} gross revenue, {d['occ']} occupancy, the bonus depreciation "
                     f"position that year, and the risk buyers were carrying."),
        lead=lead,
        sections=sections,
        faqs=faqs,
        related=related,
    )


def all_posts():
    out = []
    for slug in sorted(DATA):
        if slug not in ARCS:
            continue
        for year in sorted(era.YEARS):
            out.append(build(slug, year))
    return out


if __name__ == "__main__":
    p = all_posts()
    sys.path.insert(0, HERE)
    import blog
    wc = [blog.word_count(x) for x in p]
    print(f"{len(p)} market-year posts, {min(wc)}-{max(wc)} words, avg {sum(wc)//len(wc)}")
