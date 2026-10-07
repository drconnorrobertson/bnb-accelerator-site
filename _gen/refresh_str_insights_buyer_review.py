"""Develop existing canonical direct comparison, preserving its useful substantive answer."""
import re,json,subprocess
from pathlib import Path
from refresh_dscr_purchase_methods import refresh
ROOT=Path(__file__).resolve().parents[1]
SLUG='bnb-accelerator-vs-str-insights-buyer'
ADDITION='''<h2>Original purchase work sample: change the candidate, not just the sales deck</h2>
<p>Ask each team to respond to the same invented discovery: the candidate's included furnishings are different from the inventory used in the model. This is a decision exercise, not an allegation about any seller or provider. Request a short revised memo rather than another headline return estimate.</p>
<div class="table-wrap"><table><thead><tr><th>Response</th><th>Record to request</th><th>Buyer decision right</th></tr></thead><tbody>
<tr><td>Establish the difference</td><td>Written conveyed inventory, excluded items and source/date</td><td>Accept or dispute the factual assumption before approving costs</td></tr>
<tr><td>Rebuild the launch scope</td><td>Distinct replacement, installation and disposal quotes</td><td>Approve vendors and spending; exclude items already budgeted</td></tr>
<tr><td>Revise the model</td><td>Opening payment dates and separate revenue/readiness assumptions</td><td>Reject a candidate dependent on unavailable capital or unsupported launch dates</td></tr>
<tr><td>Assign the transaction response</td><td>Named licensed representative, counsel where needed and valid deadline</td><td>Authorize a supported request, extension or other available response</td></tr>
<tr><td>Define service continuation</td><td>Agreement clauses for more analysis, a rejected candidate and fee treatment</td><td>Decide whether to continue under actual terms, not presumed refund rights</td></tr>
</tbody></table></div>
<p>Complete that sample for BNB as well as STR Insights. A consultant may explain a change while a licensed agent handles the seller request and a separate vendor performs installation. A higher-touch proposal may coordinate more of this sequence, but unseen contracts have not been checked here. Request the exact exclusions and payment trigger for each task. A brochure promise does not authorize a contingency release or create a cancellation right.</p>
<h2>Worked service-fee bridge: credited money is not a second invoice</h2>
<p><strong>Entirely fictional figures, not either provider's price or refund policy:</strong> Assume $280,000 accessible funds and a $260,000 complete purchase/launch allocation. The latter includes a stipulated $12,000 total service fee and $35,000 retained operating cash. Suppose $4,000 of that service fee is paid before the property is selected and credited against the same $12,000 fee. After payment, cash is $276,000 and remaining allocation is $256,000. The outside margin stays $20,000; do not charge another full $12,000 or add the paid $4,000 again.</p>
<p>If the inventory change genuinely requires a distinct $9,000 purchase/install expense, total allocation becomes $269,000; after the credited payment, remaining allocation is $265,000 against $276,000 cash, leaving $11,000. Keep the $35,000 reserve once. If that $9,000 is already covered by a quote in the original allocation, there is no additional amount to add.</p>
<p>For a separate rejected-candidate case, suppose the fictional upfront $4,000 has been spent, is not credited to the next engagement and cannot be recovered under its actual terms. If a new proposal independently requires the same $260,000 allocation, $276,000 cash leaves $16,000 outside it—not $20,000. This does not assert either firm's refund terms or justify buying the first property to avoid a sunk fee. Replace each assumption with the signed agreement and cleared payment evidence; pending refunds are not spendable cash. Use the <a href="/tools/first-str-purchase-budget/">purchase cash worksheet</a> and the <a href="/guides/str-insights-service-tiers/">service-tier contract questions</a>.</p>
<h2>Fair alternatives depend on the missing purchase work</h2>
<p><a href="https://go.strsearch.com/1">STR Search's public matching description</a> makes it a research option for property-matching and analysis assistance; use the <a href="/compare/str-search/">STR Search comparison</a> to examine actual scope rather than adopt advertised outcomes. <a href="https://theshorttermshop.com/">The Short Term Shop's local-agent description</a> makes it an option to investigate for a representation-led path; see the <a href="/compare/avery-carl-short-term-shop/">direct comparison</a>. These sources were checked October 7, 2026. Confirm address coverage, availability, professional roles and current terms directly.</p>
<p>Independent specialists can also fit a buyer who already directs the purchase and accepts coordination work. Neither named alternative is an interchangeable substitute for every portal or launch package. The <a href="/compare/alternatives-to-str-insights/">STR Insights alternatives owner</a> compares buying paths; the <a href="/compare/">crawlable comparison hub</a> connects the existing provider answers. Choose based on delivered work and funded responsibilities, not an invented review score.</p>'''

def main():
 original=subprocess.check_output(['git','show','HEAD:blog/'+SLUG+'/index.html'],cwd=ROOT,text=True)
 body=re.search(r'<article class="article">(.*?)<h2 id="faq">',original,re.S)[1]
 body=body.replace('reviewed September 25, 2026','reviewed October 7, 2026')
 disclosure='<p>BNB Accelerator publishes this comparison and has a commercial interest as an acquisition provider. This is document-based analysis, not firsthand testing, a verified customer-experience review, independent ranking or endorsement. Public descriptions do not verify either firm’s signed scope; no actual BNB engagement agreement was inspected for this page. Ask both providers for the applicable written terms.</p>'
 body=body.replace('<h2>First choose',disclosure+'\n<h2>First choose',1)
 body=body.replace('<h2>Make a purchase decision with clear stop rules</h2>',ADDITION+'\n<h2>Make a purchase decision with clear stop rules</h2>',1)
 nodes=[]
 for b in re.findall(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',original,re.S):
  d=json.loads(b);nodes.extend(d.get('@graph',[d]))
 faq=[(q['name'],q['acceptedAnswer']['text']) for q in next(n for n in nodes if n.get('@type')=='FAQPage')['mainEntity']]
 refresh(SLUG,'BNB Accelerator vs STR Insights for STR Buyers','BNB Accelerator vs STR Insights: which help do you need to buy an STR?','Compare BNB Accelerator and STR Insights purchase-service scope, fee credits and buyer decision rights. Use an original changed-candidate work sample.',body,faq,'2026-09-25','data-str-insights-buyer-review-link','Compare the <a href="/blog/bnb-accelerator-vs-str-insights-buyer/">BNB versus STR Insights changed-candidate work sample and fee-credit cash bridge</a>. Actual contract scope governs either service.')
 p=ROOT/'blog'/SLUG/'index.html';s=p.read_text()
 if 'Updated October 7, 2026' not in s:s=s.replace('<span>Published September 25, 2026</span>','<span>Published September 25, 2026</span><span>&middot;</span><span>Updated October 7, 2026</span>',1)
 p.write_text(s)

if __name__=='__main__':main()
