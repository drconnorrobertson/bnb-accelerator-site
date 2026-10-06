"""Refresh an existing purchase guide; preserve original publication and design."""
import html
import json
import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'reading-a-dscr-term-sheet'
TITLE = 'DSCR Term Sheet: Compare Loans Before Buying an STR'
DESC = 'Compare STR purchase loan quotes with a two-year payoff worksheet, income-method checks, cash requirements and written closing conditions.'
FAQ = [
('What is the most important question on a DSCR term sheet?', 'Ask which property income evidence the lender accepts and how it calculates the qualifying ratio. Confirm the answer for your address, intended short-term rental use and borrower before relying on the quoted loan amount.'),
('Can I negotiate a DSCR prepayment penalty?', 'Ask the lender for available alternatives and their rates, points and written payoff rules. Availability depends on the lender, product and applicable requirements; a shorter or absent penalty is not guaranteed.'),
('Does a DSCR approval mean the deal is good?', 'No. Loan approval does not establish your owner cash flow, lawful rental use or purchase return. Underwrite full expenses, launch liquidity and downside independently of the lender qualifying ratio.')]
BODY = '''<p class="lead">Before buying a short-term rental, compare DSCR term sheets as complete purchase commitments, not interest-rate screenshots. Verify the income the lender will accept, the cash you must retain, the conditions still outstanding and the cost of paying off the loan on your actual timeline. A cheaper monthly payment can conceal a more expensive exit.</p>
<p><a href="/apply/">Book an STR acquisition call to compare your property underwriting and lender quotes before committing to an offer</a>.</p>
<h2>Turn each quote into a written purchase checklist</h2>
<p>Ask each lender to fill the same fields for the same property, borrower, loan amount and intended use. An indicative quote, rate lock, conditional approval and authorization to fund are different milestones. Ask which one you have, which terms may change and when a payment or deposit becomes nonrefundable. Do not remove a financing protection merely because a rate appears on a PDF; have your transaction professional review the contract and deadlines.</p>
<div class="table-scroll"><table><thead><tr><th>Term to document</th><th>Exact question before buying</th></tr></thead><tbody>
<tr><td>Income and qualifying ratio</td><td>Which seller records, market estimate or rent schedule will you accept? What numerator, denominator and adjustments apply to this address?</td></tr>
<tr><td>Loan amount and appraisal</td><td>What happens if the accepted income or appraised value is lower? Are furniture and other personal property excluded from collateral value?</td></tr>
<tr><td>Rate and payment</td><td>Fixed or adjustable? What amortization, interest-only period, adjustment index/caps and maturity apply? Is this rate locked through funding?</td></tr>
<tr><td>Points and fees</td><td>Which charges are percentages of the loan, flat fees, third-party costs or refundable deposits? What changes if the purchase fails?</td></tr>
<tr><td>Reserves and cash</td><td>How much must remain after closing, in which accounts, and can the same funds satisfy multiple requirements?</td></tr>
<tr><td>Payoff and ownership</td><td>What triggers a penalty, on which balance and dates? Which borrower entity, guarantors, title and insurance must match?</td></tr>
<tr><td>Closing conditions</td><td>Which appraisal, income, title, insurance, entity and other approvals remain, who clears them and by what deadline?</td></tr>
</tbody></table></div>
<h2>Separate lender income from the owner's purchase case</h2>
<p><a href="https://visiolending.com/dscr-loans/" rel="noopener">Visio's published DSCR explanation</a> uses monthly rental income divided by principal, interest, taxes, insurance and association dues. That is a provider-specific definition, not proof every lender uses the same formula. Ask for the actual accepted rental amount and payment components on your term sheet. A qualifying ratio can omit management, utilities, repairs, replacement spending and launch gaps that still affect your investment.</p>
<p>Do not assume a market estimate is universally accepted, seller history produces the best result or a rent schedule proves an STR is uneconomic. Each is evidence with different limits. Reconcile seller documents through the <a href="/blog/seller-proforma-vs-trailing-revenue/">trailing-revenue review</a> and test your owner budget using the <a href="/financing/dscr-loans/">DSCR underwriting guide</a>. Ask the lender to recalculate the quote if accepted rent falls or association dues and insurance rise. Obtain address-specific written confirmation before your contract deadline.</p>
<h2>A two-year payoff worksheet: lower rate, higher exit cost</h2>
<p>Every figure below is hypothetical, not a current lender offer, available product or forecast. Both loans fund $450,000, fully amortize over 30 years, make 24 scheduled monthly payments and are paid off immediately afterward. Quote A has a 7.25% fixed rate and two upfront points; Quote B has a 7.75% fixed rate and one upfront point. For this example only, A's contract charges 3% of the remaining principal at that exact payoff date; B has no payoff penalty. Confirm the actual contract's dates, calculation basis and exceptions instead of assuming these terms.</p>
<div class="table-scroll"><table><thead><tr><th>Hypothetical comparison, rounded</th><th>Quote A</th><th>Quote B</th></tr></thead><tbody>
<tr><td>Monthly principal and interest</td><td>$3,070</td><td>$3,224</td></tr>
<tr><td>Upfront points</td><td>$9,000</td><td>$4,500</td></tr>
<tr><td>Principal remaining after payment 24</td><td>$440,963</td><td>$441,784</td></tr>
<tr><td>Interest paid across 24 payments</td><td>$64,638</td><td>$69,156</td></tr>
<tr><td>Illustrative payoff penalty</td><td>$13,229</td><td>$0</td></tr>
<tr><td>Interest + points + penalty</td><td>$86,867</td><td>$73,656</td></tr>
</tbody></table></div>
<p>A saves about $154 in monthly principal and interest, yet costs about $13,211 more on this two-year financing-cost comparison. Principal repayment is not included as an expense: show the payoff balance separately. Without the penalty, A's interest plus points would be about $73,638, only about $18 below B. A simple points-divided-by-payment-savings shortcut misses differing principal balances and contractual exit costs.</p>
<p>Reproduce the worksheet with monthly rate r = annual rate / 12, n = 360 and payment = loan amount × r / [1 − (1 + r)<sup>−n</sup>]. After each month, interest equals beginning balance × r and principal reduction equals payment minus interest. Use unrounded amounts internally. Add any unequal origination, broker, third-party or extension fees. Common costs, taxes, insurance, time value of money and tax effects are excluded here; this is not an APR calculation or a complete investment return.</p>
<p><a href="https://www.limaone.com/loan-prepayment-penalty-real-estate-rental/" rel="noopener">Lima One's published prepayment guide</a> describes several penalty durations and structures, including no-penalty alternatives. These illustrate why written terms matter, not guaranteed availability or pricing for you. Ask for payoff examples at your planned refinance date, a later date and an early sale. Also test a hold with no refinance: future approval, valuation, interest rates and cash-out proceeds are not assured.</p>
<h2>Fund the purchase without confusing reserves and fees</h2>
<p>Build a separate cash bridge: down payment + cash-paid closing charges + setup + launch funding + retained reserves. A lender's reserve requirement is not automatically an expense, nor automatically freely spendable launch cash. Ask whether funds are merely evidenced, restricted or deposited into an account, and what releases them. Do not count the same dollar as both required retained liquidity and furniture money.</p>
<p>For an illustrative $600,000 purchase with the $450,000 loan above, the down payment is $150,000. If other cash-paid closing charges are $12,000, setup is $30,000 and retained reserves are $20,000, A requires $221,000 including its $9,000 points; B requires $216,500 including $4,500 points. These are invented budgets and exclude additional launch funding; replace every input and check fee overlap. A $220,000 available-cash limit fails A's example even before an omitted launch gap. Check the <a href="/blog/new-listing-ramp-underwriting/">monthly launch cash bridge</a>, not just annual income.</p>
<h2>Proceed, renegotiate, delay or reject the financing path</h2>
<ul><li><strong>Proceed:</strong> the income method, final cash, ownership and outstanding conditions are documented; the property works under your independent owner budget and conservative exit plan.</li>
<li><strong>Renegotiate:</strong> ask for an available fee/penalty alternative or lower purchase price when a documented cost breaches your budget. Recalculate rather than assuming a small rate change pays for itself.</li>
<li><strong>Delay:</strong> accepted income, appraisal, rate-lock expiry, entity documents or funding approval remain unresolved. Coordinate any extension with the seller and transaction professionals.</li>
<li><strong>Reject:</strong> financing requires an occupancy/use representation that is untrue, total cash is unavailable, or the purchase works only through an unapproved refinance.</li></ul>
<p>Before selecting a quote, send the lender the marked checklist, requested payoff scenarios and unresolved closing conditions. Confirm the named borrower and any personal guarantee with your attorney; entity title alone does not determine debt liability. Then update the <a href="/blog/str-maximum-offer-price-from-revenue/">maximum-offer worksheet</a> with actual financing rather than increasing your offer to match a loan approval.</p>
<p><a href="/apply/">Book a call to evaluate an STR purchase with your lender's written terms, total cash and downside plan</a>.</p>
<p class="small">Primary lender sources checked October 6, 2026. Educational information, not personalized lending, legal, tax or investment advice. Consult your lender and qualified advisers. Examples are hypothetical; no approval, refinance, rental income, tax benefit or investment result is guaranteed.</p>
<h2 id="faq">Frequently asked questions</h2>'''

def main():
    p=ROOT/'blog'/SLUG/'index.html';s=p.read_text()
    start=s.index('<p class="lead">');end=s.index('<div class="author-box">',start)
    body=BODY+''.join('<div class="faq-group"><h3>'+q+'</h3><div class="faq-answer"><p>'+a+'</p></div></div>' for q,a in FAQ)+'\n'
    s=s[:start]+body+s[end:]
    s=re.sub(r'<title>.*?</title>','<title>'+TITLE+'</title>',s,count=1)
    s=re.sub(r'<h1>.*?</h1>','<h1>'+TITLE+'</h1>',s,count=1,flags=re.S)
    for key,val in [('description',DESC),('og:description',DESC),('twitter:description',DESC),('og:title',TITLE),('twitter:title',TITLE)]:
        s=re.sub(r'(<meta (?:name|property)="'+key+r'" content=")[^"]*(")',lambda m:m.group(1)+html.escape(val,quote=True)+m.group(2),s)
    def schema(m):
        d=json.loads(m.group(2))
        if d.get('@type')=='Article':d.update(headline=TITLE,description=DESC,dateModified='2026-10-06');assert d['datePublished']=='2026-08-15'
        if d.get('@type')=='FAQPage':d['mainEntity']=[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in FAQ]
        return m.group(1)+json.dumps(d,indent=2)+m.group(3)
    s=re.sub(r'(<script[^>]*type="application/ld\+json"[^>]*>)(.*?)(</script>)',schema,s,flags=re.S)
    s=re.sub(r'<span>Updated [^<]*</span>','<span>Updated October 6, 2026</span>',s,count=1)
    if 'Updated October 6, 2026' not in s:s=s.replace('<span>Published August 15, 2026</span>','<span>Published August 15, 2026</span><span>&middot;</span><span>Updated October 6, 2026</span>',1)
    words=len(re.findall(r'\b\w+\b',html.unescape(re.sub('<[^>]+>',' ',body))));minutes=math.ceil(words/220)
    s=re.sub(r'<span>\d+ min read</span>',f'<span>{minutes} min read</span>',s,count=1);p.write_text(s)
    archive=ROOT/'blog/index.html';count=0
    def card(m):
        nonlocal count
        c=m.group()
        if '/blog/'+SLUG+'/' not in c:return c
        count+=1;c=re.sub(r'<h3>.*?</h3>','<h3><a href="/blog/'+SLUG+'/">'+TITLE+'</a></h3>',c,count=1,flags=re.S)
        c=re.sub(r'<p>.*?</p>','<p>'+DESC+'</p>',c,count=1,flags=re.S)
        c=re.sub(r'data-search="[^"]*"','data-search="'+html.escape((TITLE+' '+DESC).lower(),quote=True)+'"',c)
        return re.sub(r'<span>\d+ min read</span>',f'<span>{minutes} min read</span>',c)
    a=re.sub(r'<article class="post-card".*?</article>',card,archive.read_text(),flags=re.S);assert count==1;archive.write_text(a)
    for xml in ROOT.glob('sitemap*.xml'):
        t=xml.read_text();n=re.sub(r'(<loc>https://www.bnbaccelerator.com/blog/'+SLUG+r'/</loc>\s*<lastmod>)[^<]+',r'\g<1>2026-10-06',t)
        if n!=t:xml.write_text(n)
    print(words,minutes)

if __name__=='__main__':main()
