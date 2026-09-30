#!/usr/bin/env python3
"""Render the ten-question buying guide and connect its underlying articles."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import tpl

ROOT = Path(__file__).resolve().parent.parent
PATH = '/short-term-rental-questions/'
QUESTIONS = [
    ('How do I start an Airbnb business?', 'how-to-start-airbnb-business', 'Start with the operating model: buy a property, rent one with permission, or host a home you already own. For a purchase, set a total cash budget, screen markets and local rules, model a specific property, arrange financing, then plan furnishing, permits, insurance, pricing, and operations before the first booking. The sequence matters because a legal or financing constraint can disqualify an otherwise attractive listing.', 'How to start an Airbnb business'),
    ('How much does an Airbnb make per month?', 'how-much-do-airbnb-hosts-make', 'There is no useful national monthly income figure for an individual purchase. Gross booking revenue varies by market, property type, size, amenities, season and execution. Net cash flow also subtracts platform costs, cleaning, management, utilities, taxes, insurance, repairs, reserves and debt service. Compare a candidate with similar local listings across a full year, then stress test weaker occupancy and higher expenses.', 'See the revenue and expense breakdown'),
    ('Are short term rentals profitable?', 'is-airbnb-still-profitable', 'Some are, but profitability follows the purchase price and the full operating cost, not the popularity of the destination. Underwrite expected annual revenue, operating expenses, capital replacements and financing against the cash invested. A property that produces strong gross bookings can still lose money after debt service or a poor season. Test a long term rental or resale fallback as well.', 'Read the profitability analysis'),
    ('Where are the best places to buy an Airbnb?', 'best-airbnb-markets-2026', 'The best market depends on your budget, risk tolerance and operating plan. Look for durable guest demand, a workable revenue-to-price ratio, a clear legal path, realistic insurance, and enough cleaners and managers to operate reliably. A citywide average cannot establish that an individual parcel, HOA or building allows short stays. Screen the address before you make an offer.', 'Compare the 2026 markets'),
    ('How much does it cost to start an Airbnb?', 'how-much-money-to-start-airbnb', 'If you buy, count the down payment, lender and closing costs, inspections, furnishing, design, permits, launch costs, and cash reserves, not just the listing price. The amount varies sharply by market and financing. If you lease for arbitrage, the entry cost is lower but rent remains due during vacancies and you need the owner’s written permission plus a lawful operating path.', 'Build a total entry budget'),
    ('How do I find a profitable short term rental property?', 'how-to-analyze-airbnb-deal', 'Start with the address and rules, then select comparable listings that match location, capacity, property type, amenities and quality. Estimate annual revenue using seasonality, subtract the complete expense stack and debt service, and calculate cash flow on all cash invested. Check inspections, HOA documents, insurance, property taxes after sale, and downside scenarios before removing contingencies.', 'Use the deal analysis checklist'),
    ('How do I finance an Airbnb property?', 'how-to-finance-airbnb-investment-property', 'Common paths include conventional investment loans, certain second home loans where occupancy rules truly fit, DSCR loans, portfolio loans and cash or equity backed purchases. Terms and eligibility vary by lender and the intended use must be disclosed accurately. Compare the rate, down payment, reserves, closing costs and prepayment provisions together, then underwrite cash flow using the actual proposed loan.', 'Compare financing options'),
    ('What are the tax benefits of owning a short term rental?', 'str-tax-savings-guide', 'Owners may deduct eligible operating expenses and depreciate qualifying property. In some circumstances, losses may be nonpassive when the average customer use and material participation rules are met; cost segregation can accelerate part of the depreciation. The timing, basis, personal use, state rules and eventual recapture all matter. Have a qualified tax adviser model your facts before relying on a tax benefit in a purchase decision.', 'Review the tax guide'),
    ('How do I know if a city allows short term rentals?', 'str-regulations-before-you-buy', 'Check the current municipal code and permit office for the exact address, including zoning, license caps, minimum stays and transfer rules. Then check county requirements, HOA or condo restrictions, deed covenants and any lender or insurance conditions. Ask for written confirmation when the wording is unclear. An existing listing or seller claim does not establish that your future use will be permitted.', 'Follow the regulation checklist'),
    ('Is it better to buy an existing Airbnb or start one from scratch?', 'buy-existing-airbnb-vs-start-from-scratch', 'An operating property may offer booking history, furnishings and a faster launch, but verify the records, condition, permits and which assets or bookings transfer. Starting with a new property gives more control over design and positioning, with more launch cost and no listing history. Compare the two on verified net income, total entry cash, required work and the ability to operate legally after closing.', 'Compare both purchase paths'),
]


def render():
    items = []
    for n, (question, slug, answer, label) in enumerate(QUESTIONS, 1):
        assert (ROOT / 'blog' / slug / 'index.html').exists(), slug
        items.append(f'''      <section class="faq-group" id="question-{n}">
        <h2>{n}. {tpl.esc(question)}</h2>
        <div class="faq-answer"><p>{tpl.esc(answer)}</p>
        <p><a href="/blog/{slug}/">{tpl.esc(label)}</a></p></div>
      </section>''')
    body = f'''  <section class="hero hero-page"><div class="wrap">
    <nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a><span class="sep">/</span><a href="/blog/">Insights</a><span class="sep">/</span><span>STR questions</span></nav>
    <div class="hero-inner"><span class="eyebrow">Short term rental investing</span>
      <h1>10 questions to answer before buying a short term rental</h1>
      <p class="hero-sub">A practical starting point for comparing markets, properties, financing and operating costs. Each answer leads to a detailed guide.</p>
    </div></div></section>
  <section><div class="wrap"><article class="article">
    <p class="lead">Start with the property and its legal use, then test the numbers. These questions follow the decisions a buyer actually makes, from choosing a market through launch. They are topic priorities for prospective investors, not a measured ranking of Google search volumes.</p>
    {''.join(items)}
    <div class="callout"><h2>Put the answers to work</h2>
      <p>Use the <a href="/tools/str-revenue-calculator/">revenue calculator</a> for a first pass, review <a href="/case-studies/">real acquisition examples</a>, and check the relevant <a href="/regulations/">state regulation guide</a>. Confirm local rules and the loan terms for the property you choose.</p></div>
    {tpl.AUTHOR_BOX}
  </article></div></section>
  {tpl.cta_band('Review a property before you buy', 'Tell us your budget, timeline and target market. We can walk through the acquisition criteria with you.', primary=('/apply/', 'Book a Call'))}'''
    trail = [('Home', '/'), ('Insights', '/blog/'), ('STR questions', PATH)]
    schema = tpl.graph(tpl.breadcrumb_schema(trail), tpl.ORG_SCHEMA)
    html = tpl.page(title='10 Short Term Rental Questions to Ask Before You Buy | BNB Accelerator',
        description='Answers to 10 common short term rental investing questions on starting, profits, markets, costs, deal analysis, financing, taxes and regulations.',
        path=PATH, body=body, extra_schema=schema, active='/blog/')
    target = ROOT / PATH.strip('/') / 'index.html'
    target.parent.mkdir(exist_ok=True)
    target.write_text(html, encoding='utf-8')
    print(target)


if __name__ == '__main__':
    render()
