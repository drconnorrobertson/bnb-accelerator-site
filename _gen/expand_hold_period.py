"""Scoped existing-page refresh. No old library/homepage generation."""
import html,json,math,re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SLUG='cost-seg-timing-and-hold-period'
DATE='2026-10-07'
TITLE='Cost Segregation and STR Hold Period: Before You Buy'
H1='How should your STR hold period affect cost segregation?'
DESC='Before buying an STR, compare usable tax timing, sale cash and a longer hold. Use an exit worksheet without assuming refunds or full exchange deferral.'
FAQ=[
('Does a cost segregation study guarantee a refund?', 'No. A deduction and a cash refund are different. Ask your CPA about eligibility, loss limitations, tax actually payable and timing; fund the purchase independently.'),
('Does holding an STR longer guarantee a better result?', 'No. Compare operating cash, future capital work, debt, liquidity needs and adviser-modeled disposition consequences. A longer hold is a scenario, not an assured return.'),
('Does a 1031 exchange defer every cost-segregation component?', 'Do not assume that. Current exchange rules apply to qualifying real property, and ordinary-income recapture can arise. Have qualified advisers analyze each asset and the actual exchange.'),
('What should I request before approving the purchase?', 'Request a funded purchase budget, supported operating downside, asset and basis records, study scope and fees, and CPA-reviewed short-sale, longer-hold and proposed-exchange comparisons.')]
BODY='''<p class="lead">An STR hold period matters before you buy because accelerated deductions, operating cash and sale liquidity occur on different dates. Cost segregation is not purchase money or a reason to accept an otherwise weak property. A high-income buyer should compare a shorter taxable sale, a longer hold and any genuinely feasible exchange with qualified advisers before relying on an estimated tax benefit. The purpose here is an acquisition decision: can you fund, operate and eventually dispose of this property under realistic alternatives?</p>
<p><a href="/apply/">Bring the intended hold period and independently funded purchase budget to an STR acquisition call</a>.</p>
<h2>Separate depreciation timing from usable buyer cash</h2>
<p>Ask the study provider and CPA to establish the actual asset classifications, basis allocations, recovery periods, placed-in-service facts, applicable depreciation elections and fees. Do not assign a building's recovery period from average guest stay alone or treat every furnishing and improvement as having the same tax character. This worksheet does not classify your building, quote a bonus-depreciation percentage or calculate a deduction.</p>
<p><a href="https://www.irs.gov/publications/p925">IRS Publication 925</a> describes separate passive-activity and at-risk limits and exceptions to rental-activity treatment. A seven-day average-use exception is not, by itself, proof that a loss offsets W-2 income. Have your CPA evaluate participation, other applicable limitations and your exact ownership and use. High income, a study invoice or hiring a manager does not establish the conclusion.</p>
<p>Request two different outputs: the estimated deduction under supported assumptions and the estimated change in tax payable for the relevant year. Then ask when any resulting cash would actually be available. Neither a deduction estimate nor an expected refund funds today's earnest money, down payment or furnishing bill. Use the <a href="/blog/str-tax-benefit-shortfall-purchase/">smaller-or-delayed-benefit purchase test</a> alongside the no-benefit case.</p>
<h2>Keep the basis and disposition file from acquisition onward</h2>
<p><a href="https://www.irs.gov/publications/p551">IRS Publication 551</a> explains that depreciation allowed or allowable reduces basis. Skipping a claim does not automatically preserve the original basis. Keep purchase allocations, closing records, study reports, depreciation schedules, improvements and disposed-component records for your CPA. A market price forecast and the loan payoff are not an adjusted tax basis.</p>
<p><a href="https://www.irs.gov/publications/p544">IRS Publication 544</a> explains different recapture rules for different property types; section 1245 ordinary-income recapture is subject to limits, including realized gain. It also describes ordinary-income recapture in some like-kind exchanges. Do not label the entire sale receipt as gain, apply one tax rate to every component or promise all prior depreciation is deferred by an exchange. The tax calculation requires the actual asset records and transaction.</p>
<p>Ask the CPA to compare the proposed study with the appropriate no-study depreciation case using the same property, ownership and operating assumptions. Identify incremental study fees, when a tax effect is usable, later disposition differences and state treatment. A favorable early-year estimate is not a complete lifetime result. The <a href="/blog/depreciation-recapture-str/">recapture overview</a> is background, not a substitute for an asset-specific calculation.</p>
<h2>Use a hold-period review register before setting the offer</h2>
<div class="table-wrap"><table><thead><tr><th>Scenario</th><th>Evidence and independent reviewer</th><th>Purchase consequence</th></tr></thead><tbody>
<tr><td>Shorter taxable sale</td><td>CPA tax estimate; realistic sale costs, loan payoff and liquidity timetable</td><td>Test cash needed for the next life or investment obligation</td></tr>
<tr><td>Longer hold</td><td>Supported operating downside; capital-work schedule; debt and management terms</td><td>Do not assume appreciation or that tax timing pays recurring bills</td></tr>
<tr><td>Proposed exchange</td><td>Qualified exchange/tax plan; asset eligibility; financing and replacement search</td><td>Separate restricted proceeds from household-accessible money</td></tr>
<tr><td>Earlier forced decision</td><td>Buyer-specific liquidity needs; sale-delay and permission-loss alternatives</td><td>Preserve an independently funded fallback</td></tr>
</tbody></table></div>
<p>Write the actual review dates and unresolved facts beside each scenario. An intended ten-year hold is not a binding forecast: employment, family needs, repairs or rental permission can change. Conversely, a possible early sale does not automatically mean a study has no value. Obtain a comparison rather than an all-or-nothing rule.</p>
<p>For exchange planning, Publication 544 limits like-kind nonrecognition to qualifying real property; non-real-property assets are not automatically included. Have advisers evaluate investment use, retained cash, debt, allocations and recapture. The <a href="/blog/1031-exchange-short-term-rental/">sell-first guide</a> and <a href="/blog/reverse-1031-buy-str-before-selling/">replacement-first cash bridge</a> address different sequences. This article does not supply exchange documents or guarantee a replacement property will be available.</p>
<h2>Worked exit-cash comparison: proceeds are not gain or return</h2>
<p>Hypothetical arithmetic only, not a client result, tax estimate, market forecast or recommended hold length. Assume a future taxable sale price of $700,000, $42,000 of distinct sale outflows and a $440,000 loan payoff. That leaves $218,000 before a tax provision and any other unpaid obligations. The payoff is a cash settlement item; it is not a substitute for adjusted basis in the CPA's tax calculation.</p>
<div class="table-wrap"><table><thead><tr><th>Illustrative input</th><th>Cash reconciliation</th></tr></thead><tbody>
<tr><td>Base sale cash before tax provision</td><td>$700,000 − $42,000 − $440,000 = $218,000</td></tr>
<tr><td>Hypothetical $45,000 tax provision</td><td>$218,000 − $45,000 = $173,000</td></tr>
<tr><td>Alternative $75,000 tax provision</td><td>$218,000 − $75,000 = $143,000</td></tr>
<tr><td>Second case plus $25,000 distinct required work</td><td>$143,000 − $25,000 = $118,000</td></tr>
</tbody></table></div>
<p>The tax-provision figures are invented sensitivity inputs, not rates, recapture calculations or amounts caused solely by cost segregation. Replace them with CPA estimates. The $25,000 work amount is separate from sale costs and is deducted once. If it must be paid before sale proceeds arrive, fund it separately; a projected $118,000 later balance cannot pay today's contractor.</p>
<p>If the buyer's future obligation needs $150,000, the first case exceeds it by $23,000, the second falls short by $7,000 and the work-stressed case falls short by $32,000. None measures total investment profit: original capital, operating cash, interim contributions and tax effects across the holding period are omitted. Compare those dated flows separately. Do not add an early projected refund twice or assume an exchange produces equally accessible sale cash.</p>
<h2>Proceed with a property plan, not a deduction promise</h2>
<p>Proceed when the property clears permission and diligence, acquisition and launch are funded without speculative tax receipts, the operating downside fits your risk limits and the disposition scenarios meet real liquidity needs. Reprice when verified recurring costs or future work change a still-viable acquisition. Delay under valid protection while a decisive adviser input remains unresolved. Decline a purchase that only works if a refund, appreciation or full exchange deferral occurs.</p>
<p><a href="/apply/">Discuss the acquisition shortlist with a bounded hold-period memo</a>: available early cash, intended use, financing conditions, operating downside, expected liquidity dates and adviser questions. Keep tax returns and asset records in agreed secure channels. BNB Accelerator assists within its contracted acquisition scope; independent professionals determine tax, legal, exchange and financing conclusions. See the <a href="/blog/buy-str-high-income-large-tax-bill/">high-income buyer roadmap</a> for the rest of the purchase path.</p>
<p class="small">IRS primary materials reviewed October 7, 2026; currently published editions above are 2025 materials, not newly issued 2026 editions. Educational information only, not legal, tax, lending or personalized investment advice. All example numbers are hypothetical. No deduction, refund, sale, exchange, financing or return is guaranteed.</p>'''

def main(expected_publication='2026-08-15', hub_attribute='data-hold-period-review-link', hub_paragraph='Before relying on an early deduction, compare the <a href="/blog/cost-seg-timing-and-hold-period/">hold-period review register and taxable-sale cash worksheet</a>. Future proceeds and projected tax benefits are not today’s acquisition cash.'):
 p=ROOT/'blog'/SLUG/'index.html';s=p.read_text();published=re.search(r'"datePublished":\s*"([^"]+)"',s)[1];assert published==expected_publication
 author=re.search(r'<div class="author-box">.*?</div>\s*</div>',s,re.S)[0]
 faq='<h2 id="faq">Frequently asked questions</h2>'+''.join('<div class="faq-group"><h3>'+html.escape(q)+'</h3><div class="faq-answer"><p>'+html.escape(a)+'</p></div></div>' for q,a in FAQ)
 body=BODY+faq+author;words=len(html.unescape(re.sub('<[^>]+>',' ',body)).split());minutes=math.ceil(words/220)
 s=re.sub(r'(<article class="article">).*?</article>',lambda m:m[1]+'\n'+body+'\n</article>',s,count=1,flags=re.S)
 s=re.sub(r'<title>.*?</title>','<title>'+TITLE+'</title>',s,count=1);s=re.sub(r'<h1>.*?</h1>','<h1>'+H1+'</h1>',s,count=1)
 s=re.sub(r'(<meta property="article:published_time" content=")[^"]*(")',lambda m:m[1]+published+m[2],s)
 for name,val in [('description',DESC),('og:description',DESC),('twitter:description',DESC),('og:title',TITLE),('twitter:title',TITLE)]:s=re.sub(r'(<meta (?:name|property)="'+name+r'" content=")[^"]*(")',lambda m:m[1]+html.escape(val,quote=True)+m[2],s)
 def schema(m):
  d=json.loads(m[2])
  for n in d.get('@graph',[d]):
   if n.get('@type') in ['Article','BlogPosting']:n.update(headline=H1,description=DESC,dateModified=DATE,wordCount=words)
   if n.get('@type')=='FAQPage':n['mainEntity']=[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in FAQ]
  return m[1]+json.dumps(d,indent=2)+m[3]
 s=re.sub(r'(<script[^>]*type="application/ld\+json"[^>]*>)(.*?)(</script>)',schema,s,flags=re.S)
 s=re.sub(r'<span>\d+ min read</span>',f'<span>{minutes} min read</span>',s,count=1);p.write_text(s)
 archive=ROOT/'blog/index.html';old=archive.read_text();count=0
 def card(m):
  nonlocal count
  c=m[0]
  if '/blog/'+SLUG+'/' not in c:return c
  count+=1;c=re.sub(r'(<h3><a[^>]*>).*?(</a></h3>)',lambda z:z[1]+H1+z[2],c,flags=re.S);c=re.sub(r'<p>.*?</p>','<p>'+DESC+'</p>',c,count=1,flags=re.S)
  c=re.sub(r'data-search="[^"]*"','data-search="'+html.escape((H1+' '+DESC).lower(),quote=True)+'"',c);return re.sub(r'<span>\d+ min read</span>',f'<span>{minutes} min read</span>',c)
 a=re.sub(r'<article class="post-card".*?</article>',card,old,flags=re.S);assert count==1;archive.write_text(a)
 hub=ROOT/'blog/buy-str-high-income-large-tax-bill/index.html';h=hub.read_text();h=re.sub(r'<p '+re.escape(hub_attribute)+r'>.*?</p>\s*','',h,flags=re.S)
 h=h.replace('<div class="author-box">','<p '+hub_attribute+'>'+hub_paragraph+'</p>\n<div class="author-box">',1);hub.write_text(h)
 sm=ROOT/'sitemap-blog.xml';xml=sm.read_text();url='https://www.bnbaccelerator.com/blog/'+SLUG+'/'
 xml,n=re.subn(r'(<loc>'+re.escape(url)+r'</loc>\s*<lastmod>)[^<]+',lambda m:m[1]+DATE,xml);assert n==1;sm.write_text(xml)
 si=ROOT/'sitemap/index.html';v=si.read_text();v=re.sub(r'(<a href="/blog/'+SLUG+r'/">)[^<]+',lambda m:m[1]+TITLE,v);si.write_text(v)
 print(f'Existing refresh:{words}words/{minutes}minutes; original publication {published}; no new URL')

if __name__=='__main__':main()
