"""Add bounded acquisition support to the existing ADA guide; no library generator."""
import json
import re
import expand_hold_period as publisher

SLUG = 'does-ada-apply-short-term-rental'
TITLE = 'Does the ADA Apply to a Short-Term Rental? | BNB'
H1 = 'Does the ADA apply to a short-term rental?'
DESC = 'Before buying an STR, review ADA coverage, alteration scope and separately funded access work. Use a specialist evidence register and purchase cash test.'
ADDITION = '''<h2 id="alteration-scope-register">Turn a renovation plan into a reviewed access scope</h2>
<p>After qualified counsel addresses coverage, give the accessibility professional the actual proposed work, not just a listing description or finish allowance. Separate the altered room or feature, any associated path work, existing conditions and other duties. A contractor's cosmetic quote may not include the full reviewed scope. Conversely, do not order a blanket rebuild based only on the property's age.</p>
<p>The <a href="https://www.access-board.gov/ada/guides/chapter-2-alterations-and-additions/">U.S. Access Board's alterations guide</a> distinguishes altered-element or space requirements from additional path-of-travel work. It is introductory guidance, not a complete technical specification. Ask the qualified team to identify applicable provisions and document measurements, design limits and outstanding questions for this facility.</p>
<div class="table-scroll"><table><thead><tr><th>Before-offer record</th><th>Reviewer output</th><th>Cash or timing decision</th></tr></thead><tbody>
<tr><td>Intended operating model and actual planned alterations</td><td>Counsel's scoped applicability analysis and designer's work classification</td><td>Do not treat an unreviewed finish allowance as a complete project</td></tr>
<tr><td>Route, entrance and facilities serving the affected area</td><td>Measured findings, relevant standards and proposed feasible response</td><td>Obtain an itemized scope, not an unsupported accessibility label</td></tr>
<tr><td>Prior work, permits and dated project records</td><td>Professional assessment of relevant history and related undertakings</td><td>Leave missing records open; do not assume phasing removes duties</td></tr>
<tr><td>Design, construction and operating responsibilities</td><td>Accepted owner/vendor roles, approvals and completion evidence</td><td>Schedule actual payments and readiness gates before guest promises</td></tr>
</tbody></table></div>
<p><a href="https://www.ada.gov/law-and-regs/regulations/title-iii-regulations/">DOJ §§36.402–36.403</a> separate altered-feature accessibility from additional primary-function path duties. Section36.403(f)'s 20% comparison concerns the cost of the primary-function alteration, not the property purchase price. The rule retains prioritized path work when full path work is disproportionate; it is not a universal cap on all accessibility spending. The regulation also addresses related smaller alterations and certain three-year histories. Have counsel and the design professional determine applicability, exceptions, scope and cost treatment; do not privately split work to evade obligations.</p>
<p>Keep separately applicable existing-barrier, operating, state/local and new-construction duties outside any unsupported shortcut. A seller's past project may require records review, not automatic attribution of a new bill to the buyer. Preserve who controls each area and what can actually be changed. Obtain professional conclusions before using a price reduction, an unconfirmed exception or a future guest's workaround as the acquisition solution.</p>
<h2 id="access-work-cash-test">Worked purchase cash test: quote scope before funding it</h2>
<p>Original hypothetical arithmetic only, not a legal determination, access design, current quote, client outcome or expected project timeline. Assume qualified reviewers establish the specific feasible acquisition/renovation plan. A buyer has $400,000 accessible designated funds, $320,000 purchase/closing outflows, $45,000 distinct setup spending and a separately retained $25,000 reserve. The total commitment is $390,000, leaving $10,000 outside the plan. No tax refund or guest receipts fund it.</p>
<p>Suppose an additional $5,000 professional-review/design scope is not included in the $45,000. The plan becomes $395,000, leaving $5,000. A subsequently defined $12,000 correction quote, also expressly additional rather than already in setup, raises committed capital to $407,000: a $7,000 funding gap if the reserve is preserved. An independent $4,000 of net carrying outflows during a documented opening delay raises it to $411,000, an $11,000 gap. None of these invented costs is derived from the 20% provision or estimates every possible duty.</p>
<p>Reconcile actual overlapping quotes before adding them; do not charge the same doorway work in both the original setup and correction total. A possible seller reimbursement does not pay an early invoice until amount, terms and timing are established. Reprice a feasible purchase using verified scope, obtain permitted funding, or consider a different property. Delay only with actual valid protection while decisive professional findings remain unresolved. The <a href="/tools/first-str-purchase-budget/">all-in purchase budget</a> helps test the dated cash requirement, not regulatory compliance.</p>
<p><a href="/apply/">Bring the reviewed scope register and funded alternatives to an acquisition call</a>. BNB Accelerator assists within its contracted acquisition scope; qualified counsel and accessibility/design professionals determine coverage and technical requirements. Keep private guest or complaint records in agreed secure channels, with unnecessary identifying details removed. See the <a href="/blog/buy-str-high-income-large-tax-bill/">high-income buyer roadmap</a> for independent permission, financing and operating gates.</p>
<p class="small">Added alteration-scope materials checked October 7, 2026 against current official DOJ regulations and U.S. Access Board guidance; this does not redate the original September24 source review below or certify the property. All cash figures are hypothetical. No legal exemption, approval, accessible-use certification, financing, tax benefit or investment result is guaranteed.</p>
'''

if __name__ == '__main__':
    p = publisher.ROOT / 'blog' / SLUG / 'index.html'
    s = p.read_text()
    article = re.search(r'<article class="article">(.*?)</article>', s, re.S)[1]
    body = article.split('<h2 id="faq">Frequently asked questions</h2>')[0]
    assert '<div class="author-box">' not in body and 'alteration-scope-register' not in body
    marker = '<h2>Failure modes that create avoidable risk</h2>'
    assert body.count(marker) == 1
    body = body.replace(marker, ADDITION + marker)
    nodes = [n for raw in re.findall(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>', s, re.S) for n in json.loads(raw).get('@graph', [json.loads(raw)])]
    faq = next(n for n in nodes if n.get('@type') == 'FAQPage')
    pairs = [(x['name'], x['acceptedAnswer']['text']) for x in faq['mainEntity']]
    assert len(pairs) == 5
    pairs.append(('Is the 20% path-of-travel rule a cap on every accessibility cost?', 'No. It concerns specified additional path-of-travel work tied to a primary-function alteration, not all altered-feature, operating or other legal duties. Qualified professionals must review the actual scope and applicable rules.'))
    publisher.SLUG, publisher.TITLE, publisher.H1 = SLUG, TITLE, H1
    publisher.DESC, publisher.BODY, publisher.FAQ = DESC, body, pairs
    publisher.main('2026-09-24', 'data-ada-alteration-budget-link', 'An unusual lodging model or remodel needs a reviewed scope: use the <a href="/blog/does-ada-apply-short-term-rental/">accessibility evidence register and independently funded alteration-cost test</a>, without treating a percentage rule as a universal budget cap.')
    s = p.read_text()
    anchor = '<span>Published September 24, 2026</span>'
    assert s.count(anchor) == 1 and '<span>Updated' not in s
    s = s.replace(anchor, anchor + '<span>&middot;</span><span>Updated October 7, 2026</span>')
    p.write_text(s)
    # Keep the existing public HTML sitemap label; its title is unchanged.
    sitemap = publisher.ROOT / 'sitemap/index.html'
    v = sitemap.read_text()
    v = v.replace('<a href="/blog/'+SLUG+'/">'+TITLE+'</a>', '<a href="/blog/'+SLUG+'/">'+H1+'</a>')
    sitemap.write_text(v)
