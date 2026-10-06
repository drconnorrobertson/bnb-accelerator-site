"""Add a worked offer test to an existing substantive guide; preserve FAQ/body."""
import html
import json
import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'str-maximum-offer-price-from-revenue'
TITLE = 'STR Maximum Offer Price: Revenue, Debt and Cash Worksheet'
DESC = 'Set an STR purchase-price ceiling with verified revenue, full costs, a worked financing and cash-hurdle comparison, and a separate downside test.'
WORKSHEET = '''<h3>A worked maximum-offer worksheet</h3>
<p>All inputs below are hypothetical, not a current loan quote, required down payment, appraisal or client outcome. Assume $100,000 of annual accommodation revenue, $25,000 of fixed operating costs and variable costs equal to20% of accommodation revenue. Operating expenses total $45,000 and NOI is $55,000. A separate $5,000 annual replacement allocation leaves $50,000 before principal and interest. Taxes and property insurance are already in operating costs.</p>
<p>Assume a fully amortizing30-year loan at7.5%, loan amount75% of the purchase price, closing costs3% of price, $30,000 setup and $20,000 retained initial reserves. Thus cash committed equals28% of price plus $50,000. No mortgage insurance, additional loan fee or other charge is assumed; add actual missing items. Initial reserves are committed cash in the return denominator, not an annual expense. The annual replacement allocation is deducted once in the owner cash-flow numerator.</p>
<div class="table-scroll"><table><thead><tr><th>Same property, different offer</th><th>$500,000 price</th><th>$550,000 price</th></tr></thead><tbody>
<tr><td>Loan amount</td><td>$375,000</td><td>$412,500</td></tr>
<tr><td>Annual principal and interest, rounded</td><td>$31,465</td><td>$34,611</td></tr>
<tr><td>Total buyer cash committed</td><td>$190,000</td><td>$204,000</td></tr>
<tr><td>Annual cash after replacement allocation and principal/interest</td><td>$18,535</td><td>$15,389</td></tr>
<tr><td>Modeled pre-tax cash-on-cash</td><td>9.76%</td><td>7.54%</td></tr>
</tbody></table></div>
<p>For an illustrative8% buyer hurdle, $500,000 clears the baseline return test while $550,000 does not. The amortizing monthly payment is loan amount times r / [1 - (1 + r)^(-n)], with r=0.075/12 and n=360. Use unrounded values in the spreadsheet. With these fixed assumptions the8% hurdle binds near $539,088. A separate $200,000 cash limit binds near $535,714 because0.28times price plus $50,000 cannot exceed that limit. Neither is a complete approved offer ceiling: legal use, actual lender limits, unlevered return and downside requirements can lower it further.</p>
<p>In a separate hypothetical downside, revenue falls to $85,000, variable costs become $17,000 and fixed costs stay $25,000. NOI is $43,000; after the same $5,000 replacement allocation, $38,000 remains before principal and interest. At the $500,000 price, cash flow is approximately $6,535, or3.44% of committed cash. The baseline9.76% is not a guaranteed return or proof that this downside meets your requirements. Use a monthly launch model too; a positive annual result can hide an early funding gap.</p>
<p><a href="https://www.consumerfinance.gov/ask-cfpb/on-a-mortgage-whats-the-difference-between-my-principal-and-interest-payment-and-my-total-monthly-payment-en-1941/" rel="noopener">CFPB distinguishes principal and interest from the total mortgage payment</a>, which can include escrowed taxes, insurance and mortgage insurance. In this worksheet, property taxes and insurance are already operating expenses, so deducting a full escrow-inclusive payment again would count them twice. Still fund their actual payment dates. Ask your lender for its specific underwriting definitions and written terms; this owner model does not establish loan approval or require a business-purpose loan to use a consumer disclosure form.</p>'''.replace('equal to20%', 'equal to 20%').replace('amortizing30-year', 'amortizing 30-year').replace('at7.5%', 'at 7.5%').replace('amount75%', 'amount 75%').replace('costs3%', 'costs 3%').replace('equals28%', 'equals 28%').replace('illustrative8%', 'illustrative 8%').replace('the8%', 'the 8%').replace('because0.28times', 'because 0.28 times').replace('or3.44%', 'or 3.44%').replace('baseline9.76%', 'baseline 9.76%')

def main():
    path = ROOT / 'blog' / SLUG / 'index.html'
    s = path.read_text()
    assert 'A worked maximum-offer worksheet' not in s
    s = s.replace('<h2>Step four: stress the answer before you write the offer</h2>', WORKSHEET+'\n<h2>Step four: stress the answer before you write the offer</h2>', 1)
    s = s.replace('</p>\n\n        <h2>Why the list price', '</p>\n<p><a href="/apply/">Book an STR acquisition call to test your offer ceiling against verified revenue and total cash</a>.</p>\n\n        <h2>Why the list price', 1)
    s = s.replace('New listings often need several months to build reviews and ranking.', 'Model a new listing month by month; do not assume a fixed time to mature demand or inherited reviews.')
    s = s.replace('property taxes at the post-sale assessed value', 'property taxes using address-specific post-sale estimates verified with the local authority')
    s = s.replace('Short-term rentals wear faster than long-term rentals because of turnover.', 'Use the property condition, replacement schedule and intended use rather than assuming a universal wear rate.')
    s = s.replace('decide the minimum debt service coverage ratio', 'decide the minimum debt service coverage ratio')
    marker = 'The <a href="/financing/dscr-loans/">DSCR loan guide</a> explains how lenders typically view that ratio.'
    s = s.replace(marker, 'This NOI-to-principal-and-interest test is an owner underwriting metric, not necessarily the lender\'s DSCR. Ask the lender which rent, payment, tax, insurance and other items it uses. If down payment is a percentage, solve loan and equity together; do not add a fixed down payment to an unrelated loan ceiling. The <a href="/financing/dscr-loans/">DSCR loan guide</a> provides further lender questions.')
    s = s.replace('Run the same math with revenue 15 to 20 percent lower and costs 10 percent higher.', 'Run explicitly labeled revenue and cost sensitivities appropriate to the evidence; reductions such as 15% or 20% and a 10% cost increase are illustrative tests, not measured market risks. Separate fixed costs from costs that change with bookings.')
    s = s.replace('A seller credit toward furniture, an extended inspection period, or inclusion of existing bookings can each be worth real money.', 'A proposed seller credit, inspection extension or documented future-booking benefit needs transaction-specific approval and valuation. Credits are not automatically unrestricted setup cash; existing Airbnb reservations are not transferable buyer assets. Use the <a href="/blog/future-booking-calendar-value/">calendar-premium comparison</a> before paying for that claim.')
    old = 'Estimate supportable annual revenue from comparable listings, subtract a full operating budget including a capital reserve to get NOI, then solve for price using your required debt coverage, cash-on-cash return and unlevered yield. Use the lowest result.'
    new = 'Verify supportable revenue and subtract recurring operating expenses to estimate NOI. Track replacement allocations separately, then test debt terms, total cash committed, cash-on-cash return, unlevered yield and downside. Use the most restrictive supported limit, subject to legal use and actual lender approval.'
    assert s.count(old) == 2
    s = s.replace(old, new)
    s = s.replace('Seller figures often reflect a peak year or exclude costs such as management and capital replacement.', 'Check whether seller figures reflect a peak period or omit management, replacement needs or other costs.')
    s = re.sub(r'<title>.*?</title>', '<title>'+TITLE+'</title>', s, count=1)
    for key,val in [('description',DESC),('og:description',DESC),('twitter:description',DESC),('og:title',TITLE),('twitter:title',TITLE)]:
        s=re.sub(r'(<meta (?:name|property)="'+key+r'" content=")[^"]*(")',lambda m:m.group(1)+html.escape(val,quote=True)+m.group(2),s)
    def schema(m):
        d=json.loads(m.group(2))
        if d.get('@type')=='Article': d.update(description=DESC,dateModified='2026-10-06')
        return m.group(1)+json.dumps(d,indent=2)+m.group(3)
    s=re.sub(r'(<script[^>]*type="application/ld\+json"[^>]*>)(.*?)(</script>)',schema,s,flags=re.S)
    s=s.replace('<span>Published September 24, 2026</span><span>&middot;</span>', '<span>Published September 24, 2026</span><span>&middot;</span><span>Updated October 6, 2026</span><span>&middot;</span>',1)
    s=s.replace('<div class="author-box">','<p class="small">Worksheet source checked October 6, 2026. Educational information only, not lending, tax, legal, appraisal or personalized investment advice. All worked figures are hypothetical. No financing, income, tax benefit or investment result is guaranteed.</p>\n<div class="author-box">',1)
    article=re.search(r'<article class="article">(.*?)</article>',s,re.S).group(1)
    words=len(re.findall(r'\b\w+\b',html.unescape(re.sub('<[^>]+>',' ',article))));minutes=math.ceil(words/220)
    s=re.sub(r'<span>\d+ min read</span>',f'<span>{minutes} min read</span>',s,count=1);path.write_text(s)
    archive=ROOT/'blog/index.html';count=0
    def card(m):
        nonlocal count
        c=m.group()
        if '/blog/'+SLUG+'/' not in c:return c
        count+=1
        c=re.sub(r'<p>.*?</p>','<p>'+DESC+'</p>',c,count=1,flags=re.S)
        c=re.sub(r'data-search="[^"]*"','data-search="'+html.escape((TITLE+' '+DESC+' maximum offer worksheet cash hurdle').lower(),quote=True)+'"',c)
        return re.sub(r'<span>\d+ min read</span>',f'<span>{minutes} min read</span>',c)
    a=re.sub(r'<article class="post-card".*?</article>',card,archive.read_text(),flags=re.S);assert count==1;archive.write_text(a)
    for xml in ROOT.glob('sitemap*.xml'):
        t=xml.read_text()
        t=re.sub(r'(<loc>https://www.bnbaccelerator.com/blog/'+SLUG+r'/</loc>\s*<lastmod>)[^<]+',r'\g<1>2026-10-06',t)
        if t!=xml.read_text():xml.write_text(t)
    print(f'Offer worksheet: {words} words; {minutes} min; September24publication retained')

if __name__=='__main__':main()
