#!/usr/bin/env python3
"""Twenty city-specific buyer guides for local STR property and agent searches.

These are property-type guides, not a claim that particular active listings are
available or that BNB Accelerator acts as a licensed real estate broker.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import tpl
from gen_local_markets import MARKETS as LOCAL_MARKETS
from pillars import write, sections_html

# City, state, lead property profile, two alternatives, place-specific due diligence.
EXISTING = [
    ("panama-city-beach", "Panama City Beach", "Florida", "walkable beach homes with durable group layouts", "condos with explicitly permitted rentals", "homes farther inland with a meaningful basis discount", "beach distance, storm coverage, flood exposure and condominium reserves"),
    ("destin", "Destin", "Florida", "larger beach-access homes for family groups", "permitted condos with strong building finances", "homes serving nearby Emerald Coast access points", "the actual route to the beach, wind coverage, flood zone and HOA or condo rules"),
    ("nashville", "Nashville", "Tennessee", "homes with a valid path to non-owner-occupied STR use", "permitted group-oriented properties near demand nodes", "properties with a viable mid-term-rental fallback", "permit eligibility at the address, ownership change requirements and neighborhood rules"),
    ("scottsdale", "Scottsdale", "Arizona", "pool homes suited to winter and spring groups", "larger homes with outdoor entertaining space", "homes with a lower-cost summer operating plan", "pool safety, cooling expense, city registration and HOA restrictions"),
    ("broken-bow", "Broken Bow", "Oklahoma", "cabins with a distinctive guest amenity and workable access", "smaller couples cabins with efficient upkeep", "larger cabins only when group demand supports the basis", "septic, well, road maintenance, fire access and construction quality"),
    ("austin", "Austin", "Texas", "homes near a specific event or business demand node", "permitted group homes with parking", "homes with a credible long-term-rental exit", "the exact city or county jurisdiction, licensing, event dependence and property taxes"),
    ("denver", "Denver", "Colorado", "properties whose legal use fits the owner's occupancy plan", "well-located furnished-rental alternatives", "homes with a conventional resale or long-term-rental fallback", "primary-residence requirements, licensing and whether the proposed ownership structure qualifies"),
    ("branson", "Branson", "Missouri", "family homes close to a clear entertainment or lake demand node", "cabins with a genuine outdoor draw", "permitted resort inventory with transparent dues", "jurisdiction, HOA restrictions, seasonal demand and maintenance of guest amenities"),
]

LOCAL_ALTERNATIVES = {
    "fort-walton-beach": ("beach-access family homes with practical parking", "townhomes serving Okaloosa Island travelers", "storm, flood and salt-air costs"),
    "jacksonville": ("homes near a defined medical or business corridor", "beach-adjacent homes with verified guest demand", "micro-location and exact local jurisdiction"),
    "davenport": ("permitted resort-community pool homes", "smaller family homes with lower carrying costs", "HOA rules, resort fees and pool upkeep"),
    "sevierville": ("group cabins with reliable mountain access", "smaller cabins with a strong amenity proposition", "steep roads, septic and fire risk"),
    "johnson-city": ("homes near healthcare or campus demand", "homes near outdoor recreation with year-round use", "midweek demand and the difference between medical and leisure stays"),
    "mesa": ("pool homes serving winter visitors", "homes near a spring-training demand node", "summer cooling, pool costs and permit rules"),
    "gilbert": ("family homes near East Valley events", "larger homes with practical group layouts", "HOA permissions and summer demand"),
    "chandler": ("homes near corporate and healthcare demand", "family homes with work space and reliable internet", "HOA rules, cooling and distance to the actual trip driver"),
    "lake-harmony": ("homes with verified lake or ski access", "group homes with sufficient parking and septic", "township and community rules, winter access and septic limits"),
    "jim-thorpe": ("walkable character properties with parking", "homes with a clear trail or river-trip draw", "historic maintenance, parking and municipal STR permission"),
    "tobyhanna": ("homes in communities that explicitly allow STRs", "family homes with useful community amenities", "community bylaws, fees, septic and permit caps"),
    "manchaca": ("group homes serving south Austin trips", "homes near wedding and Hill Country demand", "jurisdiction, septic and water capacity"),
}

ROWS = list(EXISTING)
for m in LOCAL_MARKETS:
    first, second, checks = LOCAL_ALTERNATIVES[m['slug']]
    ROWS.append((m['slug'], m['city'], m['state'], m['fit'], first, second, checks))


def render(row):
    slug, city, state, primary, alternative, third, checks = row
    place = f'{city}, {state}'
    path = f'/markets/{slug}/best-short-term-rentals/'
    parent = f'/markets/{slug}/'
    trail = [('Home', '/'), ('Markets', '/markets/'), (city, parent), ('Best STR property types', path)]
    faqs = [
        (f'What are the best short-term rental properties to buy in {city}?',
         f'Start by comparing {primary}, {alternative}, and {third}. The best purchase is the individual property that passes legal-use checks and conservative underwriting at its actual price.'),
        (f'Can a local real estate agent find an Airbnb investment in {city}?',
         'A licensed local buyer agent can source and represent a property purchase. Ask about STR permit verification, comparable rental evidence, offer terms and the agent’s brokerage relationship. BNB Accelerator can coordinate acquisition analysis and launch planning; confirm the scope and fees of each role separately.'),
        (f'How do I review an STR listing in {city}?',
         f'Check the address-level rules, request reservation and payout records, quote insurance, inspect the property and stress-test twelve monthly cash flows. In this market, examine {checks}.'),
    ]
    sections = [
        (f'What “best” means in {city}', [
            f'The strongest candidate in {place} is not necessarily the listing with the most projected revenue. Compare the purchase price and total setup budget with evidence of guest demand, legal operating permission, insurance, cash reserves and an exit plan. A listing that wins on one metric can fail the complete purchase test.',
            f'Begin with {primary}. Then compare {alternative} and {third}. These are property profiles to investigate, not a list of homes currently for sale or a promise of returns. The <a href="{parent}">{city} market guide</a> explains the demand pattern and local market context.',
        ]),
        ('Build a comparable set before choosing a property', [
            f'Select five to ten bookable rentals competing for the same {city} guest. Match bedroom count, legal occupancy, location, parking and amenity tier. Note rates by month, available dates and whether the comparison property has reviews or an established ranking. Do not use a premium home to justify the revenue of an ordinary listing.',
            'For a property already operating, ask for reservation-level records, monthly platform payouts, cancellations, owner-blocked nights and an expense ledger. For a new property, model the launch period separately. Run a downside case with lower occupancy, higher insurance and an opening delay. Use the <a href="/revenue-projections/">revenue projection framework</a> to make assumptions visible.',
        ]),
        (f'Questions for a {city} real estate agent', [
            f'A local licensed buyer agent can help locate inventory, arrange showings, write offers and explain the local transaction process. Ask for written evidence of the exact parcel’s short-term-rental eligibility and identify who will confirm it with the authority. Ask the agent to distinguish verified seller revenue from a marketing estimate.',
            f'Ask how offer contingencies will protect investigation of {checks}. Discuss title, inspections, financing, association documents and any seller bookings separately. Representation and compensation depend on the agent and brokerage agreement; confirm them before signing. <a href="/blog/str-buyer-agent-vs-acquisition-team/">See how an agent and acquisition team divide the work</a>.',
        ]),
        ('Choose a deal, then set a maximum offer', [
            f'Price the entire project: purchase, closing, repairs, furnishings, permits, insurance, carrying costs and working capital. Check {checks}. Reconcile the seller’s numbers and speak with the relevant local authority and association before relying on permission to operate.',
            f'If you already have a {city} listing, bring its address, asking price, revenue history and your capital constraints to <a href="/apply/">the BNB Accelerator booking calendar</a>. The team can discuss the buy box, underwriting, sourcing and launch coordination. You approve the property and offer; licensed local professionals handle regulated representation and advice.',
        ]),
    ]
    body = f'''<section class="hero hero-page"><div class="wrap">{tpl.breadcrumb_html(trail)}<div class="hero-inner">
      <span class="eyebrow">{tpl.esc(place)} buyer guide</span>
      <h1>Best Short-Term Rentals to Buy in {tpl.esc(city)}</h1>
      <p class="hero-sub">Property types to compare, local agent questions and the checks to run before making an STR offer.</p>
      <div class="btn-row"><a class="btn btn-accent btn-lg" href="/apply/">Review a {tpl.esc(city)} deal</a><a class="btn btn-ghost-light btn-lg" href="{parent}">Market analysis</a></div>
    </div></div></section>
    <section><div class="wrap"><article class="article">
      <p class="lead speakable-answer">For a short-term rental purchase in {tpl.esc(place)}, compare {tpl.esc(primary)}, {tpl.esc(alternative)} and {tpl.esc(third)}. Verify address-level operating rules and month-by-month cash flow before treating any property as a good deal.</p>
      {sections_html(sections)}
      <div class="callout"><h3>Research the market and the purchase</h3><ul>
        <li><a href="{parent}#market-analysis">Analyze the {tpl.esc(city)} market</a></li>
        <li><a href="{parent}#buy-local-deal">Buying a property in {tpl.esc(city)}</a></li>
        <li><a href="/underwriting/">Underwriting a short-term rental</a></li>
      </ul></div>
      {tpl.faq_html(faqs)}{tpl.AUTHOR_BOX}
    </article></div></section>
    {tpl.cta_band(f'Bring us a {city} listing', 'Review the address, numbers and purchase constraints together before you make an offer.', ('/apply/', 'Book a Deal Review'), (parent, 'Market Guide'))}'''
    return tpl.page(title=f'Best Short-Term Rentals to Buy in {city} | Investor Guide',
                    description=f'Compare {city} STR property types, local agent questions, address-level checks and the purchase analysis before you buy.',
                    path=path, body=body,
                    extra_schema=tpl.graph(tpl.breadcrumb_schema(trail), tpl.ORG_SCHEMA) + '\n' + tpl.faq_schema(faqs),
                    body_class='blog', active='/markets/')


def render_agent(row):
    slug, city, state, primary, alternative, third, checks = row
    place = f'{city}, {state}'
    path = f'/markets/{slug}/airbnb-real-estate-agent/'
    parent = f'/markets/{slug}/'
    guide = f'/markets/{slug}/best-short-term-rentals/'
    trail = [('Home', '/'), ('Markets', '/markets/'), (city, parent), ('STR buyer agent', path)]
    faqs = [
        (f'Do I need a real estate agent to buy an Airbnb in {city}?',
         'A licensed buyer agent can provide local purchase representation, show properties and handle offers. The need and scope depend on your transaction and agreement. Confirm representation, compensation and local licensing before proceeding.'),
        (f'Is BNB Accelerator a {city} real estate brokerage?',
         'This page does not claim BNB Accelerator is a locally licensed brokerage. BNB Accelerator provides acquisition analysis and coordination; licensed local professionals provide regulated real estate representation as applicable.'),
        (f'What should an STR buyer agent verify in {city}?',
         f'Ask for an address-specific path to verify short-term-rental permission, association rules and {checks}. Revenue estimates should be supported by comparable properties and seller records.'),
    ]
    sections = [
        (f'What a {city} short-term-rental buyer agent should do', [
            f'Start with a buyer representation conversation: service scope, compensation, experience with {city} transactions and how the agent handles a short-term-rental contingency. A good agent can arrange showings, obtain disclosures and association documents, compare purchase prices and negotiate terms. Ask for concrete examples of how the agent checked permitted use on a prior deal, without treating past permission as proof for your address.',
            f'For {place}, ask how the agent will investigate {checks}. Get the parcel, municipal boundary and association identified before paying for deeper diligence. The seller or listing agent may describe a home as Airbnb-ready; request the underlying permits and current rules instead of relying on the label.',
        ]),
        ('Keep the agent and acquisition analysis roles clear', [
            'Local representation and investment analysis are related but different jobs. The agent handles the regulated purchase work under a brokerage agreement. An acquisition team can define the buy box, compare markets, challenge revenue assumptions, coordinate specialists and plan launch. Ask both parties who owns each task, what it costs and when you can stop a bad deal.',
            f'Before asking an agent to tour properties, compare {primary}, {alternative} and {third} against the budget. The <a href="{guide}">best {city} STR property types guide</a> lays out that selection. The <a href="/blog/str-buyer-agent-vs-acquisition-team/">buyer agent versus acquisition team guide</a> explains the distinction in more detail.',
        ]),
        ('The evidence to request before an offer', [
            'For an operating rental, request at least twelve months of reservation-level activity, platform payouts, fee and tax detail, owner blocks and management expenses. For a new rental, build a comparable set that matches location, guest capacity and amenity tier. Do not substitute a high-performing nearby listing for this home’s likely launch.',
            f'Confirm insurance and financing assumptions, inspection scope, transfer of any existing reservations and the right to operate after closing. In {city}, prioritize {checks}. Put these items on a dated diligence checklist with the agent, lender, insurer and appropriate local authority assigned to the relevant question.',
        ]),
        (f'How to start a {city} purchase search', [
            f'Bring your price ceiling, cash available for closing and setup, financing plan, timing and desired involvement. If you have a listing, bring its address and asking price. Use the <a href="{parent}">{city} market analysis</a> to decide whether the guest profile and seasonal downside fit your goals before touring.',
            f'<a href="/apply/">Book a BNB Accelerator call</a> to discuss sourcing, underwriting and coordination for a {city} deal. Confirm the role of any licensed local agent separately. No city guide can determine whether a particular property is suitable without current address-level evidence.',
        ]),
    ]
    body = f'''<section class="hero hero-page"><div class="wrap">{tpl.breadcrumb_html(trail)}<div class="hero-inner">
      <span class="eyebrow">{tpl.esc(place)} buyer representation</span>
      <h1>How to Find an Airbnb Real Estate Agent in {tpl.esc(city)}</h1>
      <p class="hero-sub">Questions for a local buyer agent, STR diligence responsibilities and the role of an acquisition team.</p>
      <div class="btn-row"><a class="btn btn-accent btn-lg" href="/apply/">Discuss a {tpl.esc(city)} purchase</a><a class="btn btn-ghost-light btn-lg" href="{guide}">Compare property types</a></div>
    </div></div></section>
    <section><div class="wrap"><article class="article">
      <p class="lead speakable-answer">A licensed {tpl.esc(city)} buyer agent can represent the real estate purchase. Ask how they verify STR use for the exact address, review seller income evidence and protect the diligence period. BNB Accelerator can support deal analysis and acquisition coordination alongside locally licensed professionals.</p>
      {sections_html(sections)}
      <div class="callout"><h3>Next steps for a buyer</h3><ul>
        <li><a href="{parent}#market-analysis">Analyze the {tpl.esc(city)} market</a></li>
        <li><a href="{guide}">Compare STR property types in {tpl.esc(city)}</a></li>
        <li><a href="/apply/">Bring a listing to the BNB Accelerator calendar</a></li>
      </ul></div>
      {tpl.faq_html(faqs)}{tpl.AUTHOR_BOX}
    </article></div></section>
    {tpl.cta_band(f'Review a {city} deal', 'Bring the property address, asking price and your investment criteria to the call.', ('/apply/', 'Book a Call'), (guide, 'Property Guide'))}'''
    return tpl.page(title=f'Airbnb Real Estate Agent in {city} | STR Buyer Guide',
                    description=f'Questions to ask a {city} Airbnb real estate agent, how to verify STR permission, and how acquisition support fits with local representation.',
                    path=path, body=body,
                    extra_schema=tpl.graph(tpl.breadcrumb_schema(trail), tpl.ORG_SCHEMA) + '\n' + tpl.faq_schema(faqs),
                    body_class='blog', active='/markets/')


if __name__ == '__main__':
    for row in ROWS:
        slug = row[0]
        write(f'/markets/{slug}/best-short-term-rentals/', render(row))
        write(f'/markets/{slug}/airbnb-real-estate-agent/', render_agent(row))
    print(f'Generated {len(ROWS)} city buying guides and {len(ROWS)} agent guides')
