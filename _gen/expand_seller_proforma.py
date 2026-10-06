"""Scoped meaningful expansion; preserve current homepage, dates and design.
Run only this refresh, not legacy full-library generators. Airbnb3632 reviewed
Oct6; original uplift bridge differs from payout reconciliation/comparing two
properties: it sets the amount of unimplemented upside credited in ONE offer.
"""
import html, json, math, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'seller-proforma-vs-trailing-revenue'
TITLE = 'Seller Pro Forma vs Trailing STR Revenue Before an Offer'
H1 = "When should an STR buyer credit a seller's pro forma over trailing revenue?"
DESCRIPTION = 'Before buying an STR, reconcile seller history and price only evidenced improvements. Use an uplift bridge, launch-cost test and downside offer decision.'
BODY = '''<p class="lead">Credit a seller's projection only when a specific change is supported, legally usable and executable under your acquisition budget. For an STR purchase in the next six months, keep verified history, supported improvement and unproven upside separate. A better property may justify a different forecast, but the seller's optimistic forecast is not the amount you must pay.</p>
<p><a href="/apply/">Book an STR purchase call to review the seller's revenue bridge and your offer ceiling</a> before committing capital.</p>
<h2>First reconcile the same property and covered period</h2>
<p>Request twelve-month seller records where available, identified by listing and covered dates. Match booking exports, adjustments, payout records and manager statements before using a headline number. Separate accommodation revenue, cleaning charges, taxes, refunds and costs; do not mistake net payouts for gross bookings or count upcoming stays as completed history.</p>
<p><a href="https://www.airbnb.com/help/article/3632" rel="noopener">Airbnb's current earnings-report guidance</a> describes listing/date filters, monthly and annual reports, gross earnings, adjustments, fees, withheld taxes and net pay. It also distinguishes Upcoming and Paid reports. Ask the seller for appropriate exports through a secure channel; access to an account does not establish buyer ownership of its future cash.</p>
<p>The <a href="/blog/reconcile-airbnb-payout-export/">payout reconciliation guide</a> handles matching records. This worksheet starts after that step: how much improvement should an STR buyer credit when making an offer? Preserve private guest, seller and financial details outside public documents.</p>
<h2>Build an uplift bridge instead of replacing the trailing year</h2>
<div class="table-wrap"><table><thead><tr><th>Claimed change</th><th>Evidence needed</th><th>Offer treatment if unresolved</th></tr></thead><tbody>
<tr><td>Additional guest capacity</td><td>Address-specific permitted use, completed scope and appropriately matched comps</td><td>Do not price a room as rentable before the intended use is cleared</td></tr>
<tr><td>Better pricing or management</td><td>Historical rate/stay pattern, specific operating plan and full new fee quote</td><td>Model the existing outcome and test the proposed lift separately</td></tr>
<tr><td>Restored availability after downtime</td><td>Dated closure evidence, completed repairs and realistic reopening schedule</td><td>Include remaining work and zero-revenue carrying costs</td></tr>
<tr><td>Different guest positioning</td><td>Comparable guest proposition, installation budget and opening timeline</td><td>Keep unproved rate and occupancy increases out of the offer's supported case</td></tr>
</tbody></table></div>
<p>For each row record the trailing baseline, incremental revenue, incremental cost, permission status, implementation date and sensitivity if the change fails. Do not add the same benefit twice as both a rate increase and occupancy improvement without explaining how they interact. A favorable market estimate does not verify the seller's specific claim.</p>
<h2>Price one supported improvement, not the whole seller story</h2>
<p>Illustrative arithmetic only: reconciled annual accommodation revenue is $100,000; the seller proposes $150,000. Assume buyer-reviewed evidence supports only an $18,000 full-year increase. The remaining $32,000 stays unproven. At an assumed 25% incremental variable cost, the supported $18,000 produces $13,500 of incremental contribution, not $18,000 of owner cash.</p>
<p>Assume baseline annual cash flow after all modeled expenses and debt is $12,000 on $180,000 of total buyer cash. The improvement needs $30,000 of additional setup, making total cash $210,000. The supported stabilized model becomes $25,500 divided by $210,000, or 12.1%. It is not the 23.6% result obtained by crediting the entire $50,000 seller uplift at the same assumed cost fraction.</p>
<p>Now assume only six months of the improvement are available in the first modeled year and $3,000 of additional carrying costs arise during implementation. Supported incremental contribution is $6,750 less $3,000, or $3,750. First-year modeled cash flow becomes $15,750, or 7.5% of $210,000. These constructed assumptions are not market statistics, a loan quote, promised rates or client results.</p>
<p>Test a no-uplift outcome too. If the $30,000 is spent but the revenue improvement does not occur, $12,000 divided by $210,000 is only 5.7%, before any further cost overruns. Decide whether that capital exposure fits your requirements before agreeing to a purchase priced for success.</p>
<h2>Write the offer around evidence and an executable budget</h2>
<p>Proceed when documented use, actual financing, insurer acceptance, setup funding and conservative economics support the proposed price. Renegotiate when a still-viable purchase requires a lower price to meet your hurdle. A discount does not cure unavailable legal use, and a seller credit does not automatically create cash or change lender rules.</p>
<p>Delay while a decisive record or approval remains unresolved; discuss appropriate contractual protection and deadlines with your retained agent and counsel. Reject a purchase that only works after accepting unverified seller upside. Use the <a href="/blog/str-maximum-offer-price-from-revenue/">maximum-offer framework</a> with your actual terms and the <a href="/underwriting/downside-scenario/">downside worksheet</a>, not this example's assumptions.</p>
<p>Your offer memo should identify the reconciled period, each credited change, excluded upside, complete cash through launch, first-year and stabilized cases, and the fact that would change the decision. For buyers with large deployable capital or tax exposure, <a href="/blog/buy-str-high-income-large-tax-bill/">separate acquisition suitability from a hoped-for tax benefit</a>. Neither a tax estimate nor personal liquidity repairs an unsupported property forecast.</p>
<p><a href="/apply/">Book a call to compare the seller's supported revenue bridge with an STR purchase price worth offering</a>. BNB Accelerator can help source, underwrite and coordinate an acquisition within its contracted scope; independent lenders, attorneys and tax advisers determine their respective matters.</p>
<p class="small">Primary source reviewed October 6, 2026. Educational information only, not personalized investment, tax, lending or legal advice. All worked figures are hypothetical. No approval, permit, revenue, tax benefit, booking or return is guaranteed.</p>'''

def main():
    path=ROOT/'blog'/SLUG/'index.html';s=path.read_text()
    published=re.search(r'"datePublished":\s*"([^"]+)"',s).group(1)
    author=re.search(r'<div class="author-box">.*?</div>\s*</div>',s,re.S).group()
    s=re.sub(r'(<article class="article">).*?</article>',lambda m:m.group(1)+'\n'+BODY+'\n'+author+'\n</article>',s,count=1,flags=re.S)
    s=re.sub(r'<title>.*?</title>','<title>'+TITLE+'</title>',s,count=1)
    s=re.sub(r'<h1>.*?</h1>','<h1>'+html.escape(H1)+'</h1>',s,count=1)
    for name in ['description','og:description','twitter:description']:
        s=re.sub(r'(<meta (?:name|property)="'+name+r'" content=")[^"]*(")',lambda m:m.group(1)+html.escape(DESCRIPTION,quote=True)+m.group(2),s)
    for name in ['og:title','twitter:title']:
        s=re.sub(r'(<meta (?:name|property)="'+name+r'" content=")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),s)
    def schema(m):
        data=json.loads(m.group(2))
        def walk(n):
            if isinstance(n,dict):
                if n.get('@type') in ['Article','BlogPosting']:
                    n.update(headline=H1,description=DESCRIPTION,dateModified='2026-10-06')
                if n.get('@type')=='FAQPage':raise AssertionError('Unexpected old FAQ schema requires manual review')
                for value in n.values():walk(value)
            elif isinstance(n,list):
                for value in n:walk(value)
        walk(data)
        return m.group(1)+json.dumps(data,indent=2)+m.group(3)
    s=re.sub(r'(<script[^>]*type="application/ld\+json"[^>]*>)(.*?)(</script>)',schema,s,flags=re.S)
    words=len(re.findall(r'\b\w+\b',html.unescape(re.sub('<[^>]+>',' ',BODY))));minutes=math.ceil(words/220)
    s=re.sub(r'<span>\d+ min read</span>',f'<span>{minutes} min read</span>',s,count=1)
    assert re.search(r'"datePublished":\s*"([^"]+)"',s).group(1)==published
    path.write_text(s)
    archive=ROOT/'blog/index.html';a=archive.read_text();matches=0
    def card(m):
        nonlocal matches
        c=m.group()
        if '/blog/'+SLUG+'/' not in c:return c
        matches+=1
        c=re.sub(r'(<h3><a[^>]*>).*?(</a></h3>)',lambda z:z.group(1)+html.escape(H1)+z.group(2),c,flags=re.S)
        c=re.sub(r'<p>.*?</p>','<p>'+DESCRIPTION+'</p>',c,count=1,flags=re.S)
        c=re.sub(r'data-search="[^"]*"','data-search="'+html.escape((H1+' '+DESCRIPTION+' revenue evidence uplift offer').lower(),quote=True)+'"',c)
        c=re.sub(r'<span>\d+ min read</span>',f'<span>{minutes} min read</span>',c)
        return c
    a=re.sub(r'<article class="post-card".*?</article>',card,a,flags=re.S);assert matches==1
    archive.write_text(a)
    hub=ROOT/'blog/buy-str-high-income-large-tax-bill/index.html';h=hub.read_text()
    block='<p data-proforma-evidence-link>Considering a seller-priced improvement story? Use the <a href="/blog/seller-proforma-vs-trailing-revenue/">seller pro forma uplift bridge</a> to isolate supported changes, launch cash and a no-uplift purchase case.</p>'
    h=re.sub(r'<p data-proforma-evidence-link>.*?</p>','',h,flags=re.S)
    h=h.replace('<div class="author-box">',block+'\n<div class="author-box">',1);assert block in h
    hub.write_text(h)
    print(f'Scoped refresh: {words} words, {minutes} min; original publication {published}; homepage untouched')

if __name__=='__main__':main()
