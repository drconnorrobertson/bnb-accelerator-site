"""Expand one existing Phase I decision section; preserve the rest of its body."""
import json
import re
import expand_hold_period as publisher

SLUG = 'phase-i-environmental-site-assessment-str-purchase'
TITLE = 'Phase I Environmental Assessment for an STR Purchase'
H1 = 'When should an STR buyer order a Phase I environmental site assessment?'
DESC = 'Review Phase I findings before buying an STR: use a cleanup-control handoff register and funded cash test without assuming environmental clearance.'
ADDITION = '''<h2 id="cleanup-control-handoff">Turn a controlled finding into an acquisition handoff</h2>
<p>A report that mentions a controlled condition is a starting point for document review, not permission to open a rental. <a href="https://www.epa.gov/superfund/superfund-institutional-controls">EPA's institutional-controls overview</a> distinguishes legal or administrative measures that limit exposure or protect a remedy from engineering measures. Controls can remain relevant after cleanup. Ask the environmental professional and counsel which actual remedy, instruments and program apply to this parcel and proposed use.</p>
<p>Do not call every recorded notice an enforceable covenant. EPA's <a href="https://cfpub.epa.gov/compliance/models/view.cfm?groupID=2&amp;model_ID=992">Notice of Contamination model overview</a> describes notices intended to inform title readers, including prospective purchasers; these generally do not themselves impose enforceable use restrictions. A notice may point to a decisive separate instrument or agency file. Obtain those records rather than concluding either that the notice prohibits STR use or that an informational notice means no duties remain.</p>
<div class="table-scroll"><table><thead><tr><th>Handoff question</th><th>Evidence to reconcile</th><th>Purchase decision</th></tr></thead><tbody>
<tr><td>What remedy and controls actually apply?</td><td>Complete agency correspondence, governing instruments, maps and current professional interpretation</td><td>Keep missing records unresolved, not marked as unrestricted</td></tr>
<tr><td>Does the intended rental fit the reviewed use?</td><td>Guest spaces, parking, water source and planned work compared with the actual control footprint</td><td>Require qualified conclusions before relying on capacity or an amenity</td></tr>
<tr><td>Who keeps each control effective?</td><td>Actual maintenance, inspection, reporting and access terms; accepted owner and contractor roles</td><td>Do not assume ordinary property management includes specialist work</td></tr>
<tr><td>What must happen at transfer?</td><td>Counsel-reviewed notices, approvals or other transaction-specific steps, where applicable</td><td>Assign evidence and a protected deadline before releasing conditions</td></tr>
<tr><td>What happens when a control needs attention?</td><td>Qualified operating instructions, contact and escalation plan, insurance and lender response</td><td>Price a bounded service scope; leave unknown repair exposure open</td></tr>
</tbody></table></div>
<p>This is an acquisition evidence register, not a technical operating manual. Do not disturb a protective cover, disconnect equipment, drill, sample or excavate to test a seller's claim. The qualified team must decide the appropriate investigation, safe work and required agency involvement. A maintenance invoice does not alone prove the remedy is effective, and a closure letter may have conditions that need separate review.</p>
<p>Ask whether a proposed change in use or site work needs further review before obtaining a construction price. A local rental permit and title coverage do not replace environmental conclusions. Conversely, identifying a control is not an automatic finding that the purchase is impossible. Compare a documented compatible plan with other properties rather than assuming a price discount purchases missing permission.</p>
<h2 id="control-cash-test">Worked cash test: a service quote is not a liability cap</h2>
<p>Original hypothetical arithmetic only. Assume $260,000 of accessible designated funds, $185,000 purchase and closing outflows, $35,000 distinct setup spending and $30,000 retained reserve. The allocations total $250,000, leaving $10,000 outside the plan. No tax refund, grant, insurance payment or early guest revenue is assumed.</p>
<p>Now assume $4,000 of additional specialist/document review and a separately confirmed $2,000 initial control-service scope, neither already in setup. Preserving the same reserve requires $256,000, leaving $4,000. If a professionally determined opening delay also creates $6,000 of distinct net carrying outflows not already budgeted, the requirement becomes $262,000: a $2,000 funding gap. Spending that amount from the reserve leaves $28,000, not the stated $30,000 cushion.</p>
<p>These inputs are invented, not cleanup estimates, market fees or environmental conclusions. A recurring service quote is not an estimate of every possible failure, repair or legal exposure. Keep any unbounded issue explicitly unresolved; do not declare it funded because the $2,000 service fits. If counsel and the environmental professional establish a feasible plan, reconcile the actual one-time work, recurring services and dated carrying outflows without counting the same scope twice. Use the <a href="/tools/first-str-purchase-budget/">all-in purchase budget</a> to test available cash, and the <a href="/blog/buy-str-high-income-large-tax-bill/">high-income buyer roadmap</a> to keep the acquisition independent of hoped-for tax benefits.</p>
<p class="small">Added control-handoff evidence reviewed October 7, 2026 using EPA's current AAI page, institutional-controls overview and Notice of Contamination overview. Their agency context is not a property-specific approval. Environmental professionals, local counsel, regulators, lenders and insurers determine their respective conclusions. All cash figures above are hypothetical; no safe-use finding, liability protection, financing or investment result is guaranteed.</p>
'''

if __name__ == '__main__':
    p = publisher.ROOT / 'blog' / SLUG / 'index.html'
    s = p.read_text()
    article = re.search(r'<article class="article">(.*?)</article>', s, re.S)[1]
    body = article.split('<h2 id="faq">Frequently asked questions</h2>')[0]
    assert '<div class="author-box">' not in body
    assert 'cleanup-control-handoff' not in body
    marker = '<h2>Worked example: converting a former roadside store</h2>'
    assert body.count(marker) == 1
    body = body.replace(marker, ADDITION + marker)
    nodes = [n for raw in re.findall(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>', s, re.S) for n in json.loads(raw).get('@graph', [json.loads(raw)])]
    faq = next(n for n in nodes if n.get('@type') == 'FAQPage')
    pairs = [(x['name'], x['acceptedAnswer']['text']) for x in faq['mainEntity']]
    pairs.append(('Does a quoted control service cap the environmental purchase risk?', 'No. A defined service quote does not price every possible failure, repair or legal exposure. Obtain professional conclusions and keep unresolved obligations explicit before committing.'))
    publisher.SLUG, publisher.TITLE, publisher.H1 = SLUG, TITLE, H1
    publisher.DESC, publisher.BODY, publisher.FAQ = DESC, body, pairs
    publisher.main('2026-09-24', 'data-phase-i-controls-link', 'A Phase I controlled finding needs more than a report label: review the <a href="/blog/phase-i-environmental-site-assessment-str-purchase/">cleanup-control handoff register and independently funded purchase cash test</a>.')
    s = p.read_text()
    anchor = '<span>Published September 24, 2026</span>'
    assert s.count(anchor) == 1
    s = s.replace(anchor, anchor + '<span>&middot;</span><span>Updated October 7, 2026</span>')
    p.write_text(s)
