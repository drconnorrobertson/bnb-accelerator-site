"""One scoped existing-owner correction; never regenerate the library."""
import html, json, math, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SLUG='str-exit-strategy'
DESC='Compare STR exit triggers, sale cash, tax timing, buyer records and alternatives before buying or listing. No assumed sale price, refinancing or tax result.'
p=ROOT/'blog'/SLUG/'index.html'
s=p.read_text()
def replace(old,new,count=1):
 global s
 assert s.count(old)==count,(old,s.count(old))
 s=s.replace(old,new)
replace('Almost nobody buys a short-term rental with an exit plan, and almost everybody eventually needs one. Deciding in advance what would make you sell converts a stressful reactive decision into a scheduled one, and it materially changes how you handle the tax consequences.', 'Before buying a short-term rental, decide which operating, liquidity or personal changes would require an exit review. A review trigger is not an automatic instruction to sell. Compare the cash and responsibilities of holding, selling and any replacement purchase before committing to an offer or listing.')
replace('The five reasons people actually sell','Five possible exit-review triggers')
replace('Supply outgrew demand, or regulation tightened, and the property that underwrote at 16 percent now runs at 8.', 'New supply, operating restrictions or different revenue and expenses may change your original underwriting. Check actual records and applicable permissions; this is not a forecast of any market’s performance.')
replace('Relocation, divorce, health, a business sale, or a child\'s tuition. This is the most common reason and the least planned for.', 'Relocation, health, family obligations or a business transition may change the cash deadline or your capacity to oversee the property. Do not assume sale proceeds arrive before an obligation is due.')
replace('Equity that has grown to a large share of net worth in a single property is a concentration risk, not just an asset.', 'Compare the property’s exposure and liquidity with your other obligations. Use the <a href="/blog/str-portfolio-concentration-sale/">concentration-sale worksheet</a> to distinguish cash needs removed from new exposure added by a replacement.')
replace('The tax benefit was consumed.</strong> The large first year deduction is a one time event. Once it is used, the property has to justify itself on operating economics alone.', 'The expected tax benefit changed.</strong> Evaluate the purchase and continued ownership without an assumed refund or deduction. A different tax estimate does not establish that selling is better; operating cash and disposition costs still matter.')
replace('Real and rarely admitted. Usually an argument for changing the management structure rather than selling, but occasionally the honest answer is to exit.', 'Compare your actual responsibilities with the scope and cost of a different manager or co-host. A change in service may help, but neither that change nor a sale is automatically the right remedy.')
replace('Timing is a tax decision first','Compare cash, operating obligations and tax timing')
replace('Accelerated depreciation reduces basis, which increases gain on sale, and portions of that gain attributable to depreciation can be recaptured at rates above long term capital gains. That means the year you sell matters enormously, particularly if it coincides with other large income events.', '<a href="https://www.irs.gov/publications/p551">IRS Publication 551</a> explains that depreciation allowed or allowable reduces basis. <a href="https://www.irs.gov/publications/p544">Publication 544</a> describes asset-specific disposition and recapture treatment. Ask your CPA to calculate adjusted basis and recognized gain by asset; loan payoff and spendable sale cash are not tax basis or gain. Compare the actual income years without assuming a universal tax-first priority.')
replace('<strong>Do not stack income events.</strong> Selling in the same year as a business sale, a large bonus, or an equity event compounds the cost.', '<strong>Compare the relevant income years.</strong> Request buyer-specific tax and cash projections alongside debt maturities, carrying costs and personal obligations. Delaying a sale is not automatically cheaper or feasible.')
replace('It defers rather than eliminates, and the 45 day identification window is unforgiving.', 'Qualifying exchanges may defer gain, but do not assume every furnishing or depreciation component is deferred. Publication 544 describes a 45-day identification period after transfer; confirm the full transaction conditions and deadlines with your advisers.')
replace('The cost segregation report is the document your CPA needs at exit.', 'Provide the cost segregation report, depreciation schedules, purchase allocations, improvement records and proposed sale terms to your CPA.')
replace('Hold period, likely disposition route, and income timing all belong in the model on day one. We build them in during acquisition.', 'Ask what hold-period, disposition-cash and replacement-purchase analysis your actual acquisition engagement includes. Keep tax calculations and legal decisions with your independent professionals.')
replace('A short-term rental sells to one of two buyers, and they value completely different things.', 'A prospective buyer may be assessing investment use, personal use or a combination. Confirm that buyer’s intended use and transaction conditions instead of assuming there are only two mutually exclusive buyer types.')
replace('A property with organized records sells faster and closer to asking than an identical property with a spreadsheet the owner assembled last week.', 'Reconcile those records with payouts, refunds and expenses, and distinguish historical results from a seller forecast. Documentation supports review; it does not guarantee a sale time, asking price or future income.')
replace('In some markets this buyer pays more than the investor.', 'Do not assume that this buyer will pay a premium; evaluate actual offers and conditions.')
replace('Know which one you are selling to before you decide whether to keep the property booked through closing or take it dark and stage it. Both are defensible, and doing neither deliberately is what produces a long days on market.', 'Before changing bookings or staging, document outstanding guest obligations, management termination terms, any buyer conditions and who funds the transition. Do not promise that reservations, listings, reviews or operating permissions transfer. Verify those items independently; a proposed closing date is not a completed handoff.')
replace('Note that this changes the tax treatment going forward.', 'Verify permitted use, lease demand, transition costs and your own tax treatment before relying on the conversion.')
replace('<strong>Refinance rather than sell</strong> to access capital without triggering the tax event, at the cost of higher leverage.', '<strong>Evaluate refinancing separately.</strong> Obtain actual lender terms, net proceeds after costs, payment obligations and timing. Do not use unapproved refinancing as cash available for a replacement purchase; have your advisers evaluate transaction-specific tax consequences.')
answers=[
('The common triggers are a market that changed through supply or regulation, a life event, capital concentration in a single asset, exhaustion of the one time first year tax benefit, or operational fatigue. Deciding in advance what would trigger a sale converts a reactive decision into a planned one.', 'Review changed underwriting or permissions, personal cash deadlines, concentration, revised tax expectations and operating responsibilities. Compare holding, selling and replacement cash before deciding; none of these triggers automatically requires a sale.'),
('Considerably. Accelerated depreciation reduces basis and increases gain, and portions attributable to depreciation can be recaptured at rates above long term capital gains. Selling in the same year as a business sale, large bonus, or equity event stacks income exactly when it is most expensive.', 'The year can affect your tax calculation. Have your CPA compare asset-specific basis, recognized gain and income years alongside cash deadlines and holding costs. Do not assume postponement is always cheaper or that tax timing overrides other obligations.'),
('Trailing twelve months of gross revenue pulled from platform dashboards rather than a summary, a full expense ledger, monthly occupancy and average daily rate, review history, and written confirmation of whether the operating permit transfers on sale. Organized records sell faster and closer to asking.', 'Provide platform revenue and payout records, refunds, expenses, monthly occupancy and average daily rate, review history and independently verified operating permissions. Reconcile historical figures and document outstanding bookings and handoff conditions. Organized records do not guarantee price, timing or future income.'),
('Changing the management structure if operations are the problem, converting the property to mid-term or long-term use, which changes the tax treatment going forward, or refinancing to access capital without triggering a taxable disposition, at the cost of higher leverage.', 'Compare a different management arrangement, another permitted rental use or actual refinancing terms. Verify scope, costs, permissions, financing and your own tax treatment. None guarantees a solution or cleared cash for another purchase.')]
for old,new in answers:replace(old,new,2)
replace('<h2 id="faq">Frequently asked questions</h2>', '<p class="small">Accuracy sections reviewed October 7, 2026 using IRS Publication 551 (December 2025) and Publication 544 (2025), not a new 2026 edition. This scoped document-based correction is not a professional review of every rule or a firsthand client case. BNB Accelerator is the interested acquisition-service publisher. No sale price, closing date, tax benefit, financing, replacement property or investment result is guaranteed. Obtain independent tax, legal and lending advice; share private records only through agreed secure channels. For worked disposition comparisons, use the <a href="/blog/cost-seg-timing-and-hold-period/">hold-period cash guide</a>.</p>\n\n        <h2 id="faq">Frequently asked questions</h2>')
s=re.sub(r'(<meta property="article:published_time" content=")[^"]+',r'\g<1>2026-08-11',s)
for key in ['description','og:description','twitter:description']:
 s=re.sub(r'(<meta (?:name|property)="'+key+r'" content=")[^"]*',lambda m:m[1]+html.escape(DESC,quote=True),s)
body=re.search(r'<article class="article">(.*?)</article>',s,re.S)[1]
words=len(html.unescape(re.sub('<[^>]+>',' ',body)).split());minutes=math.ceil(words/220)
def schema(m):
 d=json.loads(m[2])
 for n in d.get('@graph',[d]):
  if n.get('@type')=='BlogPosting':
   assert n['datePublished']=='2026-08-11'
   n.update(description=DESC,dateModified='2026-10-07',wordCount=words)
 return m[1]+json.dumps(d,indent=2,ensure_ascii=False)+m[3]
s=re.sub(r'(<script[^>]*type="application/ld\+json"[^>]*>)(.*?)(</script>)',schema,s,flags=re.S)
s=re.sub(r'<span>\d+ min read</span>',f'<span>{minutes} min read</span>',s,count=1);p.write_text(s)
p=ROOT/'blog/index.html';a=p.read_text();changed=0
def card(m):
 global changed
 c=m[0]
 if '/blog/'+SLUG+'/' not in c:return c
 changed+=1
 title=html.unescape(re.search(r'<h3><a[^>]*>(.*?)</a></h3>',c,re.S)[1])
 c=re.sub(r'<p>.*?</p>','<p>'+DESC+'</p>',c,count=1,flags=re.S)
 c=re.sub(r'data-search="[^"]*"','data-search="'+html.escape((title+' '+DESC).lower(),quote=True)+'"',c)
 return re.sub(r'<span>\d+ min read</span>',f'<span>{minutes} min read</span>',c)
a=re.sub(r'<article class="post-card".*?</article>',card,a,flags=re.S);assert changed==1;p.write_text(a)
p=ROOT/'sitemap-blog.xml';x=p.read_text();x,n=re.subn(r'(<loc>https://www.bnbaccelerator.com/blog/'+SLUG+r'/</loc>\s*<lastmod>)[^<]+',r'\g<1>2026-10-07',x);assert n==1;p.write_text(x)
print(words,minutes)
