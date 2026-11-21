"""Build one crawlable catalog for the existing purchase and operating tools."""
from pathlib import Path
import hashlib
import html
import json
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = 'https://www.bnbaccelerator.com'
DATE = '2026-11-21'


def esc(value):
    return html.escape(str(value), quote=True)


def main():
    operating = json.loads((ROOT / 'content/operating-calculators.json').read_text())
    groups = [
        ('purchase', 'Plan a purchase', 'Start with available cash, then model income and a downside case.', [
            ('first-str-purchase-budget', 'First STR purchase budget', 'Separate down payment, closing costs, setup, service fees and reserves.'),
            ('str-revenue-calculator', 'STR revenue and cash flow', 'Model nightly rate, occupancy, operating costs and financing together.'),
            ('str-downside-calculator', 'Downside and break-even', 'Test lower occupancy and nightly rates before committing to a property.'),
        ]),
        ('payments', 'Reconcile bookings and payouts', 'Match the booking, platform statement and bank deposit for the same period.', [
            ('payout-reconciliation-bridge', 'Payout reconciliation', 'Bridge gross charges, deductions and adjustments to the bank deposit.'),
            ('reservation-change-cash-difference', 'Reservation changes', 'Compare the original and revised reservation cash amounts.'),
            ('booking-channel-net-proceeds', 'Booking-channel net proceeds', 'Compare channel charges and expected proceeds on a consistent basis.'),
            ('payout-currency-reconciliation', 'Payout currency reconciliation', 'Compare source currency, conversion and received funds.'),
            ('payment-installment-balance', 'Payment installment balance', 'Reconcile a scheduled amount with payments and remaining balance.'),
            ('owner-cash-allocation-worksheet', 'Owner cash allocation', 'Allocate available cash while keeping operating reserves visible.'),
        ]),
        ('turnovers', 'Organize turnovers and supplies', 'Check timing, stock and cost assumptions before the next guest arrival.', [
            ('same-day-turnover-window', 'Same-day turnover window', 'Compare checkout, cleaning, inspection and check-in timing.'),
            ('linen-par-inventory-gap', 'Linen inventory gap', 'Compare the linen needed for the operating cycle with stock on hand.'),
            ('consumable-reorder-planner', 'Consumable reorder planner', 'Estimate replenishment needs from stock, use and lead time.'),
            ('turnover-contract-break-even', 'Turnover contract break-even', 'Compare a fixed contract with the costs tied to each turnover.'),
            ('stay-length-turnover-cost', 'Stay length and turnover cost', 'Compare how stay length changes turnover frequency and cost.'),
        ]),
        ('maintenance', 'Budget for maintenance and projects', 'Compare the same scope, reporting period and reserve needs.', [
            ('maintenance-quote-cost-comparison', 'Maintenance quote comparison', 'Compare quoted costs and allowances without losing scope differences.'),
            ('rental-replacement-reserve', 'Replacement reserve', 'Organize future replacement costs and reserve contributions.'),
            ('rental-project-budget-variance', 'Project budget and contingency', 'Compare the budget with commitments, actual costs and remaining headroom.'),
            ('utility-usage-period-normalizer', 'Utility usage by period', 'Put utility usage from different reporting periods on a comparable basis.'),
            ('maintenance-backlog-capacity', 'Maintenance backlog capacity', 'Compare outstanding work with the labor time available.'),
        ]),
    ]
    entries = [entry for _, _, _, items in groups for entry in items]
    slugs = [entry[0] for entry in entries]
    assert len(slugs) == len(set(slugs)) == len(operating) + 3
    assert set(item['slug'] for item in operating) <= set(slugs)
    for slug in slugs:
        assert (ROOT / 'tools' / slug / 'index.html').is_file(), slug

    body = '''<main id="main">
<section class="hero hero-page"><div class="wrap"><nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a><span class="sep">/</span><span>Tools</span></nav><div class="hero-inner"><span class="eyebrow">Free buyer and operator tools</span><h1>Airbnb investment and rental calculators</h1><p class="lead">Choose a calculator for the decision in front of you: funding a purchase, checking rental cash flow, reconciling a payout or planning the next turnover.</p><p>Start with your purchase budget, then review the revenue and downside models. For an operating property, choose the task below.</p></div></div></section>
<section class="tool-catalog wrap" aria-labelledby="catalog-title"><h2 id="catalog-title">Choose from ''' + str(len(entries)) + ''' free calculators</h2>
<nav class="tool-jumps" aria-label="Calculator categories">'''
    body += ''.join('<a href="#' + key + '">' + esc(title) + '</a>' for key, title, _, _ in groups)
    body += '''</nav><div class="tool-search" id="tool-search-controls" hidden><label for="tool-search">Find a calculator</label><div class="tool-search-row"><input id="tool-search" type="search" placeholder="Try payout, linen or budget" autocomplete="off" aria-controls="tool-groups"><button id="tool-search-clear" type="button">Clear search</button></div><p id="tool-search-status" role="status" aria-live="polite"></p></div><div id="tool-groups">'''
    for key, title, intro, items in groups:
        body += '<section class="tool-group" id="' + key + '" aria-labelledby="' + key + '-title"><h2 id="' + key + '-title">' + esc(title) + '</h2><p>' + esc(intro) + '</p><div class="tool-cards">'
        for slug, title, description in items:
            body += '<article class="tool-card" data-tool-card><h3><a href="/tools/' + slug + '/">' + esc(title) + '</a></h3><p>' + esc(description) + '</p></article>'
        body += '</div></section>'
    body += '''</div><p id="tool-search-empty" hidden>No calculator matches that search. Try a shorter task name, or clear the search to browse all tools.</p></section>
<section class="section bg-alt"><div class="wrap wrap-narrow"><h2>Use the same evidence behind every number</h2><p>These tools organize your inputs; they do not verify a property, predict a return or replace professional review. Use the same dates and definitions when comparing results, and keep forecasts separate from collected revenue.</p><ol><li>Record the source and period for revenue, expenses and available nights.</li><li>Use current lender estimates and written vendor quotes in the purchase budget.</li><li>Reconcile platform statements with bank deposits before treating a payout as profit.</li><li>Keep cash reserves and unresolved assumptions visible in the downside case.</li></ol><p>Continue with <a href="/revenue-projections/">the revenue evidence guide</a>, the <a href="/answers/what-is-revpar/#revpar-calculator">RevPAR formula and calculator</a>, or <a href="/resources/str-investor-library/">the investor resource library</a>.</p><h2>Want help evaluating an acquisition?</h2><p>Bring your purchase budget, property details and unanswered questions. Review the <a href="/pricing/">service fee and scope</a> before deciding which work you want help with.</p><p><a class="btn btn-primary" href="/apply/">Discuss your STR purchase</a></p></div></section></main>'''

    path = ROOT / 'tools/index.html'
    source = path.read_text()
    source, count = re.subn(r'<main\b[\s\S]*?</main>', lambda _: body, source, count=1)
    assert count == 1
    title = 'Free Airbnb & Rental Calculators | BNB Accelerator'
    description = f'Find {len(entries)} free Airbnb and short-term rental calculators for purchase budgets, cash flow, payouts, turnovers and reserves. Choose a tool by task.'
    source = re.sub(r'<title>.*?</title>', lambda _: '<title>' + esc(title) + '</title>', source, flags=re.S)
    for key, value in [('description', description), ('og:title', title), ('twitter:title', title), ('og:description', description), ('twitter:description', description)]:
        source = re.sub(r'(<meta\s+(?:name|property)="' + key + r'"\s+content=")[^"]*', lambda m: m[1] + esc(value), source)

    def schema(match):
        data = json.loads(match[2])
        nodes = data.get('@graph', [data])
        nodes[:] = [node for node in nodes if node.get('@type') != 'ItemList']
        for node in nodes:
            if node.get('@type') in ['WebPage', 'CollectionPage']:
                node.update(name=title, description=description, dateModified=DATE)
        nodes.append({'@type': 'ItemList', 'name': 'Airbnb investment and rental calculators', 'numberOfItems': len(entries), 'itemListElement': [{'@type': 'ListItem', 'position': i, 'name': label, 'url': ORIGIN + '/tools/' + slug + '/'} for i, (slug, label, _) in enumerate(entries, 1)]})
        return match[1] + json.dumps(data).replace('<', '\\u003c') + match[3]

    source = re.sub(r'(<script[^>]*type="application/ld\+json"[^>]*>)(.*?)(</script>)', schema, source, flags=re.S)
    source = re.sub(r'<link[^>]+href="/assets/buyer-discovery[^\"]*"[^>]*>', '', source)
    source = re.sub(r'<script[^>]+src="/assets/tool-catalog[^\"]*"[^>]*></script>', '', source)
    css = 'assets/buyer-discovery.v1.css'
    js = 'assets/tool-catalog.v1.js'
    revision = lambda file: hashlib.sha256((ROOT / file).read_bytes()).hexdigest()[:12]
    source = source.replace('</head>', '<link rel="stylesheet" href="/' + css + '?v=' + revision(css) + '"></head>')
    source = source.replace('</body>', '<script src="/' + js + '?v=' + revision(js) + '" defer></script></body>')
    source = re.sub(r'(property="article:modified_time" content=")[^"]*', lambda m: m[1] + DATE, source)
    path.write_text(source)
    sitemap = ROOT / 'sitemap-core.xml'
    tree = ET.parse(sitemap)
    for row in tree.getroot():
        if row.find('{*}loc').text == ORIGIN + '/tools/':
            lastmod = row.find('{*}lastmod')
            if lastmod is not None:
                lastmod.text = DATE
    tree.write(sitemap, encoding='utf-8', xml_declaration=True)
    print(json.dumps({'toolsCatalog': len(entries), 'categories': len(groups), 'newPages': 0}))


if __name__ == '__main__':
    main()
