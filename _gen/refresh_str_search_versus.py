"""Develop canonical direct comparison, preserving design and original publication."""
import re
from pathlib import Path
R=Path(__file__).resolve().parents[1]
p=R/'compare/str-search/index.html';s=p.read_text()
assert '"dateModified": "2026-10-01"' in s
s=s.replace('"dateModified": "2026-10-01"','"dateModified": "2026-10-07"')
s=s.replace('Do you want a property-matching and analysis service, or a written purchase-to-launch coordination scope?', 'Compare property matching, purchase coordination and the work actually included in each written proposal.')
s=s.replace('<td>Sourcing, underwriting and purchase-to-launch coordination</td>', '<td>Published sourcing, underwriting and purchase-to-launch coordination; actual engagement defines inclusions</td>')
marker='<section class="section-sm"><div class="wrap wrap-narrow"><h2>Which option fits your first purchase?</h2>'
assert s.count(marker)==1
body='''<section class="section-sm"><div class="wrap wrap-narrow"><h2>What the current public offers establish—and what they do not</h2>
<p>STR Search’s <a href="https://go.strsearch.com/1" rel="noopener noreferrer">property-match page</a> describes screening data, evaluating market supply and demand, projecting revenue and analyzing amenities. Its <a href="https://strsearch.com/" rel="noopener noreferrer">homepage</a> advertises a 30-day matching promise and recommends at least $175,000 of investment capital. These are provider statements, not our independently verified results, a service fee, a maximum purchase budget or your eligibility. Its footer separately disclaims guaranteed financial performance. Obtain the actual matching conditions and remedy rather than interpreting a sales headline as guaranteed owner cash.</p>
<p>The <a href="https://strsearch.com/terms--conditions" rel="noopener noreferrer">public website terms</a> address website use and broad service conditions; this review has not examined a paid client agreement. Neither these terms nor an absence of detail here proves a task is excluded from the proposal you receive. Ask STR Search to identify included transaction and launch support directly.</p>
<p>BNB Accelerator’s <a href="/how-it-works/">published scope</a> describes market selection, sourcing, underwriting, offer/inspection/closing coordination and designer/operator introductions. It leaves purchase capital and the final decision with the client, lending with the lender, legal work with counsel, tax advice with independent advisers and day-to-day operation with the operator. An introduction is not a paid furnishing package or management contract. This comparison does not certify an unseen BNB agreement or promise a purchase, permit, tax benefit or return.</p>
</div></section><section class="section-sm"><div class="wrap wrap-narrow"><h2>Run the same handoff work sample with both teams</h2>
<div class="bc-docs"><ol>
<li><strong>Candidate memo:</strong> Ask each team to explain one address using source-dated permission evidence, selected revenue comparables, complete expenses and independently available cash. Record modeled versus verified inputs and the buyer's approval gate.</li>
<li><strong>Changed evidence:</strong> Give both teams the same inspection finding and revised quote. Ask who updates the offer ceiling, who negotiates, who approves added spending and who confirms that the property still fits. A new forecast is not permission to waive a contingency.</li>
<li><strong>Contract dates:</strong> Identify the licensed representative and named deadline monitor, required notices and escalation contact. Counsel and the transaction professionals determine actual rights; a search timeline does not extend purchase deadlines.</li>
<li><strong>Opening file:</strong> Identify who orders, pays and accepts furnishings, photos and operator work. Separate introductions, project coordination and executed vendor work, including exclusions and local coverage.</li>
<li><strong>Fee and exit register:</strong> Record amounts and signing, matching, closing or opening triggers. Ask about rejected candidates, termination, restart and refund conditions without assuming any remedy. Apply exactly the same questions to BNB.</li>
</ol></div>
<p>A buyer who already has suitable representation and launch vendors may need less coordination. A buyer with little available execution time should require a named handoff plan rather than assume a higher-priced package covers everything. Use the <a href="/guides/str-service-responsibility-matrix/">acquisition responsibility matrix</a> for the work record; inspect the actual specialist contracts separately.</p>
</div></section><section class="section-sm"><div class="wrap wrap-narrow"><h2>Two invented proposals: compare complete cash, not a fee headline</h2>
<p><strong>Hypothetical arithmetic only:</strong> These are neither STR Search nor BNB prices, contract terms, client results or forecasts. Assume $350,000 available and the same property/financing in both proposals: $220,000 down, $20,000 distinct closing bills, $30,000 furnishings, $15,000 repairs and $45,000 retained operating cash. The common allocation is $330,000. No provider service fees are inside it.</p>
<div class="bc-table-scroll" role="region" aria-label="Hypothetical proposal cash comparison" tabindex="0"><table><thead><tr><th scope="col">Service allocation</th><th scope="col">Fictional A</th><th scope="col">Fictional B</th></tr></thead><tbody>
<tr><th scope="row">Acquisition service</th><td>$8,000</td><td>$15,000</td></tr>
<tr><th scope="row">Identical specified launch coordination</th><td>$6,000 extra</td><td>Included</td></tr>
<tr><th scope="row">Identical specified transaction coordination</th><td>$4,000 extra</td><td>Included</td></tr>
<tr><th scope="row">Complete capital allocation</th><td>$348,000</td><td>$345,000</td></tr>
<tr><th scope="row">Cash outside allocation</th><td>$2,000</td><td>$5,000</td></tr>
</tbody></table></div>
<p>A's $7,000 lower acquisition headline does not mean $7,000 less total cash: its two distinct service extras make the complete proposal $3,000 higher. The coordination charges exclude the supplier invoices already in the $30,000 furnishings line; do not count those invoices again. This deliberately holds deliverables equal and says nothing about which actual provider has better quality.</p>
<p>For a separate inspection sensitivity, add $6,000 of new repair work not included in the original $15,000. A becomes $354,000, exceeding available cash by $4,000; B becomes $351,000, exceeding it by $1,000. Both fail the stipulated cash gate. An anticipated refund, a fast property match or a lower service headline does not fill either gap. The $45,000 reserve is already allocated; do not subtract it twice or quietly spend it to make the purchase pass.</p>
<p>Record payment dates as well as totals. A fee due when matched and one due at closing create different early-cash exposure even at equal totals; neither trigger or refund is assumed for either real provider. Use the <a href="/tools/first-str-purchase-budget/">first-STR cash planner</a> with actual quoted items and the <a href="/blog/str-property-management-fees/">management-fee worksheet</a> for the separate recurring operating agreement.</p>
</div></section><section class="section-sm"><div class="wrap wrap-narrow"><h2>Fair alternatives when neither proposal fits</h2>
<p>Compare the actual <a href="/compare/alternatives-to-str-insights/">STR Insights service tier</a> for analysis or acquisition needs. Investigate <a href="/compare/alternatives-to-the-short-term-shop/">The Short Term Shop</a> when specialist representation in a chosen market fits, confirming its training and vendor support rather than reducing it to showings. These are different buying paths, not equivalent packages or ranked endorsements. The <a href="/compare/alternatives-to-str-search/">STR Search alternatives owner</a> examines broader service selection and rejected-candidate costs; this direct comparison centers on the two proposals and handoff test.</p>
</div></section>'''
s=s.replace(marker,body+marker)
s=s.replace('Provider facts summarized from <a href="https://strsearch.com/" rel="noopener noreferrer">STR Search’s public material</a>, reviewed 2026-10-01.', 'Document-based analysis of the linked STR Search homepage, property-match page and public website terms, plus BNB’s published scope, reviewed October 7, 2026. This is not firsthand testing, an authenticated customer-experience review or an examination of either provider’s unseen client agreement.')
p.write_text(s)
p=R/'sitemap-core.xml';s=p.read_text()
s,n=re.subn(r'(<loc>https://www.bnbaccelerator.com/compare/str-search/</loc>\s*<lastmod>)[^<]+',lambda m:m[1]+'2026-10-07',s);assert n==1;p.write_text(s)
