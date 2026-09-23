#!/usr/bin/env python3
"""Build dedicated service-area pages for every active BNB Accelerator market.

The market hub names 20 cities/submarkets. Several older pages cover a wider
region (Phoenix and Mesa, the Smokies, or the Poconos), which leaves city-level
searches without a page that answers the local acquisition question. This file
adds the missing city pages without claiming a local office or using
LocalBusiness schema. Service schema identifies the city as areaServed and the
national BNB Accelerator organization as the provider.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tpl
from pillars import sections_html, write

PUB = "2026-09-22"

MARKETS = [
    dict(slug="fort-walton-beach", city="Fort Walton Beach", state="Florida", state_slug="florida",
         price="$545K", revenue="$8.6K", roi="15–19%", guest="families and military-connected travelers using the Emerald Coast",
         demand="Gulf beaches, Okaloosa Island, Eglin Air Force Base, youth sports and regional drive-to trips",
         fit="three- and four-bedroom homes or townhomes with simple beach access, practical parking and durable finishes",
         risk="storm insurance, flood exposure, salt-air maintenance and the exact city-versus-county jurisdiction",
         edge="a lower acquisition basis than Destin while serving much of the same beach-going audience"),
    dict(slug="jacksonville", city="Jacksonville", state="Florida", state_slug="florida",
         price="$425K", revenue="$6.4K", roi="13–17%", guest="business travelers, relocating families, medical visitors and beach guests",
         demand="health systems, corporate travel, port activity, sports, universities and the Atlantic beaches",
         fit="well-located two- to four-bedroom homes with parking, reliable internet and access to a specific demand node",
         risk="a very large metro where neighborhood selection matters more than the citywide average",
         edge="diversified demand and a lower entry price than Florida's best-known vacation corridors"),
    dict(slug="davenport", city="Davenport", state="Florida", state_slug="florida",
         price="$515K", revenue="$8.1K", roi="14–18%", guest="families and groups visiting the Orlando theme-park corridor",
         demand="Walt Disney World, youth sports, reunions and purpose-built resort communities",
         fit="four- to eight-bedroom pool homes in communities that expressly support vacation-rental use",
         risk="HOA restrictions, resort fees, pool costs, heavy competition and address-specific zoning",
         edge="group capacity and purpose-built inventory at a lower basis than many closer-in Orlando locations"),
    dict(slug="sevierville", city="Sevierville", state="Tennessee", state_slug="tennessee",
         price="$975K", revenue="$16.2K", roi="15–20%", guest="drive-to family groups visiting the Great Smoky Mountains",
         demand="the national park, Dollywood, weddings, reunions and a long regional leisure season",
         fit="amenity-rich cabins with views, usable roads, sufficient parking and layouts designed for groups",
         risk="steep access, wildfire and storm exposure, septic capacity, well performance and cabin supply growth",
         edge="large-group cabin revenue with access to one of the country's deepest drive-to leisure audiences"),
    dict(slug="johnson-city", city="Johnson City", state="Tennessee", state_slug="tennessee",
         price="$385K", revenue="$5.9K", roi="14–18%", guest="medical, university, business and outdoor-recreation travelers",
         demand="ETSU, regional healthcare, the Appalachian Highlands, family visits and outdoor events",
         fit="two- to four-bedroom homes near healthcare, campus or regional recreation with straightforward year-round access",
         risk="overestimating vacation demand in a market whose strongest thesis is diversified ordinary travel",
         edge="a modest basis and less dependence on one tourism season than a pure mountain-resort market"),
    dict(slug="mesa", city="Mesa", state="Arizona", state_slug="arizona",
         price="$625K", revenue="$8.9K", roi="13–17%", guest="winter visitors, spring-training fans, families and outdoor travelers",
         demand="Cactus League baseball, winter sun, golf, healthcare, events and access to the East Valley",
         fit="three- to five-bedroom pool homes with shaded outdoor areas, practical cooling systems and group-friendly layouts",
         risk="summer carrying costs, pool and HVAC maintenance, water use, licensing and neighborhood compatibility",
         edge="access to Phoenix-area demand at a basis that can be more favorable than Scottsdale"),
    dict(slug="gilbert", city="Gilbert", state="Arizona", state_slug="arizona",
         price="$695K", revenue="$9.6K", roi="12–16%", guest="families, relocating households, event travelers and winter visitors",
         demand="East Valley employment, youth sports, weddings, healthcare, dining and warm-weather travel",
         fit="larger suburban homes with pools, garages, shade and easy access to the guest's specific trip driver",
         risk="summer seasonality, pool and cooling expense, local registration duties and HOA restrictions",
         edge="a polished suburban guest experience and larger homes suited to family groups"),
    dict(slug="chandler", city="Chandler", state="Arizona", state_slug="arizona",
         price="$695K", revenue="$9.6K", roi="12–16%", guest="corporate travelers, relocating families, winter visitors and event guests",
         demand="technology employers, healthcare, golf, weddings and the wider Phoenix event calendar",
         fit="three- to five-bedroom homes with pools, work areas, fast internet and simple freeway access",
         risk="summer demand, cooling and pool expense, HOA language and the distance to the guest's actual destination",
         edge="a diversified corporate-and-leisure demand profile within the East Valley"),
    dict(slug="lake-harmony", city="Lake Harmony", state="Pennsylvania", state_slug="pennsylvania",
         price="$585K", revenue="$9.4K", roi="14–18%", guest="New York and Philadelphia groups seeking lake, ski and waterpark trips",
         demand="Lake Harmony, Jack Frost, Big Boulder, waterparks, race weekends and four-season drive-to travel",
         fit="group homes with legal occupancy, adequate parking, septic capacity and real access to lake or ski demand",
         risk="township rules, community bylaws, septic limits, winter access and insurance",
         edge="four-season demand inside one of the country's largest drive-to population catchments"),
    dict(slug="jim-thorpe", city="Jim Thorpe", state="Pennsylvania", state_slug="pennsylvania",
         price="$445K", revenue="$7.1K", roi="13–17%", guest="couples, families and outdoor travelers drawn to the historic town",
         demand="rail excursions, whitewater rafting, trails, festivals, weddings and fall foliage",
         fit="character properties with parking, walkability or a clear outdoor-recreation connection",
         risk="historic-building maintenance, parking, exact municipal rules and assuming generic homes will price like distinctive ones",
         edge="a recognizable destination identity where thoughtful design can separate a listing from commodity inventory"),
    dict(slug="tobyhanna", city="Tobyhanna", state="Pennsylvania", state_slug="pennsylvania",
         price="$375K", revenue="$6.2K", roi="14–18%", guest="regional family and friend groups using the central Poconos",
         demand="state parks, waterparks, lakes, ski areas and access from New York and Philadelphia",
         fit="affordable group homes with community amenities, clear rental permission, parking and verified septic capacity",
         risk="community-level STR restrictions, dues, permit caps, septic limits and uneven neighborhood quality",
         edge="one of the lower acquisition bases in the Poconos when the community and rule stack are right"),
    dict(slug="manchaca", city="Manchaca", state="Texas", state_slug="texas",
         price="$685K", revenue="$9.8K", roi="12–16%", guest="Austin event groups, weddings, families and Hill Country leisure travelers",
         demand="Austin events, wedding venues, breweries, outdoor recreation and access to the southern metro",
         fit="larger homes with outdoor space, pools or gathering amenities and a clear path to the guest's trip",
         risk="jurisdiction, water and septic capacity, event-related wear, heat, insurance and unincorporated-area rules",
         edge="more space and group utility than central Austin while remaining connected to metro demand"),
]


def market_page(m):
    path = f'/markets/{m["slug"]}/'
    city = m["city"]
    place = f'{city}, {m["state"]}'
    trail = [("Home", "/"), ("Markets", "/markets/"), (city, path)]
    description = (f"BNB Accelerator short-term rental acquisition in {place}: market fit, typical entry metrics, "
                   "property criteria, local diligence and the buyer process.")
    service = f'''    {{
      "@type": "Service",
      "@id": "{tpl.SITE}{path}#service",
      "name": "Short-term rental acquisition in {tpl.esc(place)}",
      "serviceType": "Short-term rental property acquisition and launch coordination",
      "provider": {{ "@id": "https://www.bnbaccelerator.com/#organization" }},
      "areaServed": {{ "@type": "City", "name": "{tpl.esc(place)}" }},
      "url": "{tpl.SITE}{path}",
      "description": "{tpl.esc(description)}"
    }}'''
    faqs = [
        (f"Does BNB Accelerator help investors buy short-term rentals in {city}?",
         f"Yes. {city} is one of the active markets listed by BNB Accelerator. The team helps qualified clients define a buy box, source and underwrite properties, negotiate, coordinate diligence and prepare for launch. The client approves every material decision."),
        (f"What type of Airbnb property works in {city}?",
         f"The working buy box emphasizes {m['fit']}. A real candidate still has to pass address-specific regulation, insurance, inspection and downside underwriting."),
        (f"What is the biggest STR risk in {city}?",
         f"The first issue to pressure-test is {m['risk']}. No citywide estimate replaces property-level verification."),
        (f"How do I start an STR search in {city}?",
         "Start with capital, financing, target cash flow, personal-use expectations and risk tolerance. BNB Accelerator uses those constraints to decide whether the market fits before presenting properties."),
    ]
    sections = [
        (f"Why investors search {city}", [
            f"The investable case for {place} begins with {m['demand']}. That demand mix matters because a short-term rental cannot manufacture a trip. The property can only win a share of trips that already exist, so the first underwriting question is which guest is traveling, why the trip occurs and how sensitive that trip is to price or season.",
            f"The primary guest is often {m['guest']}. That profile should shape bedroom count, parking, amenity choices, photography and minimum-stay strategy. A property that is attractive in general but poorly aligned with the market's actual booking party can underperform a simpler home with a clearer use case.",
            f"The local advantage is {m['edge']}. That is a research thesis, not a performance promise. BNB Accelerator still screens the individual address against comparable listings, regulation, total entry cost and a downside case before recommending that a client proceed.",
        ]),
        ("Working acquisition metrics", [
            ("table", ["Current market marker", "Typical figure", "How to use it"], [
                ["Average purchase price", m["price"], "A screening benchmark, not a target or appraisal"],
                ["Average monthly gross revenue", m["revenue"], "An observed market marker, not a property projection"],
                ["Illustrative return range", m["roi"], "Requires property-specific financing and full expenses"],
            ]),
            "These figures summarize the current market hub and are estimates assembled from BNB Accelerator closings and active underwriting. They do not describe every property. Bedroom count, exact location, legal occupancy, amenities, condition, management, financing and seasonality can move the result substantially.",
            "A useful analysis rebuilds the income month by month, loads all operating costs, includes management even if the owner initially expects to self-manage, and reserves for replacement items. Purchase price is only one part of total entry cost; closing, furnishing, repairs, permits and cash reserves belong in the same decision.",
        ]),
        (f"The {city} buy box", [
            f"A starting property profile is {m['fit']}. The point of the buy box is not to make every listing look comparable. It is to remove properties that solve the wrong guest problem before time and diligence money are spent.",
            ("ul", [
                "Confirm that short-term rental use is lawful for the exact parcel and ownership structure.",
                "Match legal occupancy to bedrooms, parking, septic or sewer capacity and life-safety requirements.",
                "Use a comparable set with the same guest capacity, micro-location and amenity tier.",
                "Price insurance before the offer becomes difficult to unwind.",
                "Model the weakest consecutive months and a disruption case, not only the annual average.",
                "Keep a credible long-term, mid-term or resale exit where the property type allows it.",
            ]),
        ]),
        ("Local diligence before an offer", [
            f"The main diligence concern is {m['risk']}. The right answer may differ across a city line, township, subdivision, condominium declaration or HOA. A listing described as Airbnb-ready is not evidence that a permit transfers or that a new owner can continue the same use.",
            f"Review the <a href=\"/regulations/{m['state_slug']}/\">{m['state']} STR regulation guide</a>, then verify the current rule with the city, county, tax office, HOA, insurer and qualified local advisers. Save the source, date and name of the person who confirmed the interpretation. Regulation and insurance are pass-or-fail gates, not details to solve after closing.",
            "The property inspection should also follow the market thesis. A beach home needs corrosion, moisture and storm-resilience review. A mountain or lake property needs access, drainage, well and septic scrutiny. A pool home needs mechanical and safety records. The inspection scope should follow how the property will be used rather than a generic residential checklist alone.",
        ]),
        ("How BNB Accelerator supports the purchase", [
            "The process begins with a defined client buy box: available cash, financing, income objective, desired involvement, timing, tax context and risk boundaries. The team narrows approved markets, screens listings and presents a deal analysis with visible assumptions. The client decides whether to tour, offer, renegotiate or walk away.",
            "After an accepted offer, coordination covers inspection, appraisal, lender and title milestones. Renovation, furnishing, photography, listing setup and a local operating handoff can then be organized against a launch plan. BNB Accelerator is not the buyer's lawyer, CPA, lender or property manager; those professional boundaries remain explicit.",
            "A local page cannot tell you whether a particular home is a good investment. It can make the first question more precise: does this market and guest profile fit the buyer's capital and operating plan? The property-level answer comes only after current evidence is assembled.",
        ]),
    ]
    schema = tpl.graph(tpl.breadcrumb_schema(trail), service, tpl.ORG_SCHEMA) + "\n" + tpl.faq_schema(faqs)
    body = f'''
  <section class="hero hero-page">
    <div class="wrap">
      {tpl.breadcrumb_html(trail)}
      <div class="hero-inner">
        <span class="eyebrow">{tpl.esc(m["state"])} acquisition market</span>
        <h1>Short-Term Rental Investment in {tpl.esc(city)}</h1>
        <p class="hero-sub">Local market fit, property screening and acquisition coordination for investors evaluating {tpl.esc(place)}.</p>
        <div class="btn-row"><a class="btn btn-accent btn-lg" href="/apply/">Apply for a strategy call</a><a class="btn btn-ghost-light btn-lg" href="/markets/">Compare markets</a></div>
      </div>
    </div>
  </section>
  <section><div class="wrap"><article class="article">
    <p class="lead speakable-answer">BNB Accelerator actively helps qualified investors evaluate and acquire short-term rentals in {tpl.esc(place)}. The local thesis is {tpl.esc(m["edge"])}; every property still has to clear current rules, insurance, total-entry-cost and downside tests.</p>
{sections_html(sections)}
    <div class="callout"><h3>Continue your research</h3><ul><li><a href="/markets/">Compare all active STR markets</a></li><li><a href="/blog/how-to-analyze-airbnb-deal/">How to analyze an Airbnb deal</a></li><li><a href="/underwriting/">STR underwriting library</a></li><li><a href="/case-studies/">Review documented client deals</a></li></ul></div>
{tpl.faq_html(faqs)}
{tpl.AUTHOR_BOX}
  </article></div></section>
{tpl.cta_band(f"Build a {city} buy box", "Start with capital, risk and the guest you intend to serve. The property search follows from those constraints.", ("/apply/", "Apply Now"), ("/markets/", "Compare Markets"))}'''
    return tpl.page(title=f"{city} Short-Term Rental Investment | BNB Accelerator",
                    description=description, path=path, body=body,
                    extra_schema=schema, body_class="blog", active="/markets/")


def link_hub():
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
    path = os.path.join(root, "markets", "index.html")
    source = open(path, encoding="utf-8").read()
    links = {
        "Panama City Beach": [("/markets/panama-city-beach/", "Panama City Beach STR guide")],
        "Destin": [("/markets/destin/", "Destin STR guide")],
        "Fort Walton Beach": [("/markets/fort-walton-beach/", "Fort Walton Beach STR guide")],
        "Jacksonville": [("/markets/jacksonville/", "Jacksonville STR guide")],
        "Davenport": [("/markets/davenport/", "Davenport STR guide")],
        "Sevierville": [("/markets/sevierville/", "Sevierville STR guide")],
        "Nashville": [("/markets/nashville/", "Nashville STR guide")],
        "Johnson City": [("/markets/johnson-city/", "Johnson City STR guide")],
        "Scottsdale": [("/markets/scottsdale/", "Scottsdale STR guide")],
        "Mesa": [("/markets/mesa/", "Mesa STR guide")],
        "Gilbert &amp; Chandler": [("/markets/gilbert/", "Gilbert STR guide"), ("/markets/chandler/", "Chandler STR guide")],
        "Broken Bow": [("/markets/broken-bow/", "Broken Bow STR guide")],
        "Lake Harmony": [("/markets/lake-harmony/", "Lake Harmony STR guide")],
        "Jim Thorpe": [("/markets/jim-thorpe/", "Jim Thorpe STR guide")],
        "Tobyhanna": [("/markets/tobyhanna/", "Tobyhanna STR guide")],
        "Austin": [("/markets/austin/", "Austin STR guide")],
        "Manchaca": [("/markets/manchaca/", "Manchaca STR guide")],
        "Denver": [("/markets/denver/", "Denver STR guide")],
        "Branson": [("/markets/branson/", "Branson STR guide")],
    }
    found = set()
    card_re = re.compile(r'<article class="market-card".*?</article>', re.S)

    def add_links(match):
        card = match.group(0)
        heading = re.search(r'<h3>(.*?)</h3>', card, re.S)
        if not heading:
            return card
        name = heading.group(1).strip()
        if name not in links:
            return card
        found.add(name)
        if 'local-market-links' in card:
            return card
        links_html = '<p class="local-market-links">' + ' &middot; '.join(
            f'<a href="{href}">{label}</a>' for href, label in links[name]) + '</p>'
        return card[:-len('</article>')] + "  " + links_html + "\n        </article>"

    source = card_re.sub(add_links, source)
    missing = set(links) - found
    if missing:
        raise SystemExit(f"market hub cards not found: {', '.join(sorted(missing))}")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(source)


if __name__ == "__main__":
    for market in MARKETS:
        write(f'/markets/{market["slug"]}/', market_page(market))
    link_hub()
    print(f"local markets: wrote {len(MARKETS)} city pages and linked the market hub")
