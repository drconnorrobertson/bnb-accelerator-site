#!/usr/bin/env python3
"""Add useful analysis and deal-buying paths to existing market pages.

No new near-duplicate city URLs: both intents live on the established canonical.
Run after the market generators, before sitewide.py.
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = json.loads((ROOT / '_gen/market_data.json').read_text())
from gen_local_markets import MARKETS  # noqa: E402
from gen_city_buying_guides import ROWS as BUYER_GUIDES

LOCAL = {m['slug']: m for m in MARKETS}
GUIDE_SLUGS = {row[0] for row in BUYER_GUIDES}
EXTRA = {
    'fort-walton-beach': ('Emerald Coast beach access and military travel', 'storm and flood insurance plus city versus county boundaries'),
    'jacksonville': ('specific medical, beach or business demand nodes', 'neighborhood-level comparables and exact jurisdiction'),
    'davenport': ('theme-park group travel and resort communities', 'HOA permission, resort fees and pool costs'),
    'sevierville': ('Smokies group cabin demand', 'road access, septic, wildfire and cabin supply'),
    'johnson-city': ('healthcare, university and outdoor travel', 'ordinary midweek demand versus a vacation-only forecast'),
    'mesa': ('winter visitors and spring training', 'summer demand, cooling and pool costs'),
    'gilbert': ('East Valley family and event travel', 'summer seasonality and HOA restrictions'),
    'chandler': ('corporate and family travel in the East Valley', 'summer demand, cooling and HOA restrictions'),
    'lake-harmony': ('lake, ski and waterpark demand', 'township, community and septic restrictions'),
    'jim-thorpe': ('rail excursions, trails and historic-town travel', 'parking, historic-building costs and municipal rules'),
    'tobyhanna': ('Poconos family travel and community amenities', 'community rental rules, septic and dues'),
    'manchaca': ('south Austin events and Hill Country travel', 'jurisdiction, water and septic capacity'),
}

START = '<!-- local-intent-start -->'
END = '<!-- local-intent-end -->'


def block(slug, name, demand, risk):
    name, demand, risk = map(html.escape, (name, demand, risk))
    buying_guide = (f'<p><a href="/markets/{slug}/best-short-term-rentals/">Compare the best STR property types in {name}</a> and <a href="/markets/{slug}/airbnb-real-estate-agent/">questions for a local Airbnb buyer agent</a>.</p>'
                    if slug in GUIDE_SLUGS else '')
    return f'''{START}
        <section id="market-analysis" aria-labelledby="market-analysis-title">
          <h2 id="market-analysis-title">How to analyze the {name} short-term rental market</h2>
          <p>Start with the demand pattern to test: {demand}. Choose five to ten currently bookable properties with similar sleeping capacity, location, amenities and legal use. Compare their available nights, actual booked nights where reliable records are available, nightly rates and full-year seasonality. A citywide average is only a screening clue.</p>
          <p>Ask for monthly reservation and payout records on an operating property. For a new listing, model a slower launch and compare a conservative case against the seller's or broker's forecast. Confirm the rules for the exact address, including zoning, permit eligibility, association documents, parking and occupancy. Pressure-test {risk} before calculating a maximum offer.</p>
          <p>Build a 12-month cash flow with taxes, insurance quotes, utilities, cleaning, management, maintenance, replacement reserves, debt service and furnishing. Compare the weakest months with your cash reserve. Use the <a href="/underwriting/">underwriting guides</a> and <a href="/revenue-projections/">revenue projection method</a> to check each assumption.</p>
        </section>
        <section id="buy-local-deal" aria-labelledby="buy-local-deal-title">
          <h2 id="buy-local-deal-title">Buying an Airbnb property in {name}</h2>
          <p>Send the listing address, asking price and any revenue history to the acquisition team. The first decision is whether legal use and the guest profile justify deeper diligence. The next is an offer ceiling based on current comparables, all-in setup costs and downside cash flow. If the seller has bookings, verify which obligations and deposits can transfer at closing.</p>
          <p>BNB Accelerator can help define a local buy box, screen candidate properties and coordinate the purchase and launch. You make the investment decision. <a href="/apply/">Book a {name} acquisition call on the BNB Accelerator calendar</a> to discuss a market or a specific deal.</p>
{buying_guide}
        </section>
{END}'''


count = 0
for file in sorted((ROOT / 'markets').glob('*/index.html')):
    slug = file.parent.name
    source = file.read_text()
    if slug in LOCAL:
        name = LOCAL[slug]['city']
        demand, risk = EXTRA[slug]
    elif slug in DATA:
        d = DATA[slug]
        name = d['name']
        demand = d['peak']
        risk = 'parcel-level STR permission, insurance and the local operating cost stack'
    else:
        raise RuntimeError(f'Missing local research inputs for {slug}')
    insert = block(slug, name, demand, risk)
    if START in source:
        source = re.sub(re.escape(START) + r'.*?' + re.escape(END), lambda _: insert, source, flags=re.S)
    else:
        source, n = re.subn(r'</article>', lambda _: insert + '\n        </article>', source, count=1)
        if n != 1:
            raise RuntimeError(f'No article in {file}')
    file.write_text(source)
    count += 1

hub = ROOT / 'markets/index.html'
source = hub.read_text()
hub_start, hub_end = '<!-- market-intent-hub-start -->', '<!-- market-intent-hub-end -->'
hub_block = '''<!-- market-intent-hub-start -->
  <section class="bg-alt" aria-labelledby="local-intent-heading"><div class="wrap wrap-narrow">
    <h2 id="local-intent-heading">Analyze a local STR market or bring us a deal</h2>
    <p>Open a city guide below to compare the guest demand, seasonal risk and property criteria. Each guide includes an address-level analysis checklist and a buying path. Have a listing already? Bring the address, asking price and seller's booking records to a call.</p>
    <p><a class="btn btn-accent" href="/apply/">Book a market or deal review</a></p>
  </div></section>
<!-- market-intent-hub-end -->'''
if hub_start in source:
    source = re.sub(re.escape(hub_start) + r'.*?' + re.escape(hub_end), lambda _: hub_block, source, flags=re.S)
else:
    source = source.replace('</main>', hub_block + '\n</main>', 1)
hub.write_text(source)
print(f'Enhanced {count} existing market pages and the market hub')
