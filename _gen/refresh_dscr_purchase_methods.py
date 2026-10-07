"""Two scoped existing-article refreshes; no homepage or library generation."""
import json, re, subprocess
import expand_hold_period as publisher

VACANCY_BODY = '''<p class="lead">Before buying an STR, ask the lender to show exactly how it turns rental evidence into qualifying income. A vacancy factor, projection discount and expense adjustment are not interchangeable, and the lender's ratio is not your owner-cash forecast. Preserve both calculations, with their different inputs, before deciding what to offer. A loan can qualify while the property's complete costs still require owner contributions.</p>
<p><a href="/apply/">Bring the lender's calculation and your independent STR purchase budget to an acquisition call</a>. BNB Accelerator assists within its contracted acquisition scope, not as a lender or a source of credit approval.</p>
<h2>Identify what the proposed income figure already includes</h2>
<p>Request the accepted document, listing or address, covered dates and definition of revenue. Distinguish completed accommodation receipts, future bookings, gross amounts including other charges, net platform payouts, long-term rent and a modeled annual projection. A market estimate is not verified seller history. An annual projection can already incorporate occupied nights; applying another adjustment changes that estimate rather than proving it was wrong.</p>
<p>Ask what each additional factor represents and where it enters the calculation. It might be a stipulated lender discount rather than a measured estimate of empty nights or the owner's complete expense allowance. Do not automatically reverse a factor to infer actual occupancy. If revenue already excludes vacant nights, a lender may nevertheless require its own further adjustment. Confirm the rule rather than silently removing it from the lender file or copying it into the buyer forecast.</p>
<p>The current <a href="https://www.hostfinancial.com/short-term-rental-loans-mortgages/">Host Financial STR program page</a> describes actual history, projections and market rents as possible income sources. Its FAQ describes a projection discount for some programs and different treatments of existing gross revenue or management costs. It also includes principal, interest, taxes, insurance and HOA in its stated denominator. These are provider-specific descriptions, not universal rules or an approval for this address. Obtain the applicable written calculation; no advertised rate, threshold or discount is assumed here.</p>
<h2>Use a calculation register, not a single ratio screenshot</h2>
<div class="table-wrap"><table><thead><tr><th>Field</th><th>Written evidence</th><th>Buyer question</th></tr></thead><tbody>
<tr><td>Income source and period</td><td>Accepted history, projection or rent schedule, address and version</td><td>Does it describe this buyer's actual intended use?</td></tr>
<tr><td>Revenue definition</td><td>Included charges, refunds, fees and occupied/available nights</td><td>Which amounts are already removed or are not owner revenue?</td></tr>
<tr><td>Adjustment sequence</td><td>Every factor, dollar subtraction and calculation order</td><td>Is it a lender rule, supported buyer cost or an unresolved assumption?</td></tr>
<tr><td>Payment denominator</td><td>Exact components, annual/monthly basis and effective quote</td><td>Are taxes, insurance or HOA already included elsewhere?</td></tr>
<tr><td>Decision and verification dates</td><td>Conditions, required reviewer and transaction deadline</td><td>What changes the loan amount or cash before funding?</td></tr>
<tr><td>Owner case</td><td>Property-level revenue, all distinct costs and dated receipts</td><td>Can the buyer fund downside even if the loan qualifies?</td></tr>
</tbody></table></div>
<p>Use matching periods: annual income divided by annual obligation, or monthly equivalents of both. Ask the lender to explain an interest-only period, rate change or new insurance quote rather than carrying the original denominator through every year. The <a href="/blog/reading-a-dscr-term-sheet/">complete term-sheet review</a> covers rate, fees, maturity and exit conditions; this register isolates the income bridge. The <a href="/blog/seller-proforma-vs-trailing-revenue/">seller uplift guide</a> addresses how much operational improvement deserves credit in an offer.</p>
<h2>Worked comparison: qualifying at 1.23 while owner cash is negative</h2>
<p>All numbers are invented arithmetic, not a lender program, appraisal, market forecast or client outcome. Assume $96,000 annual accommodation revenue. Stipulate that a fictional lender accepts that source, applies a 20% discount and divides by a $62,400 annual obligation including principal, interest, taxes, insurance and HOA. Accepted income is $76,800 and the ratio is $76,800 / $62,400 = 1.23, rounded. If the invented loan condition requires 1.20, this one calculation clears it; other underwriting conditions are not established.</p>
<p>Separately assume the buyer's independently supported full annual revenue is also $96,000. Distinct operating outflows are $42,000 for management, cleaning net of any properly reconciled reimbursements, utilities, repairs and other modeled items. Those outflows explicitly exclude the taxes, insurance and HOA already in the $62,400 obligation. Owner cash is $96,000 − $42,000 − $62,400 = negative $8,400 before any omitted capital work or tax consequences. The lender's $19,200 income discount is not another actual invoice to subtract from this owner calculation.</p>
<p>Now use an $84,000 buyer-revenue sensitivity while holding these two outflow totals unchanged solely to isolate the revenue effect. Annual owner cash becomes negative $20,400. Actual variable costs may change; replace that simplifying assumption with supported costs rather than claiming the scenario is a forecast. Neither the 1.23 qualifying ratio nor this annual deficit determines which month needs the cash.</p>
<h2>Test receipt timing before assigning the reserve</h2>
<p>For a separate, deliberately simplified three-month stress, assume $5,200 monthly loan-related obligation plus $3,500 distinct operating outflows, or $8,700 due each month. Actual cash receipts in those months are assumed to be $3,000, $5,000 and $7,000, received before the bills. Net flows are negative $5,700, $3,700 and $1,700, totaling negative $11,100. A starting $40,000 spendable reserve would fall to $28,900. These are receipt assumptions, not booked revenue or predicted seasonality.</p>
<p>Do not subtract another $11,100 from an annual case that already contains these flows, or call the retained $40,000 a recurring expense. This partial schedule omits other cash movements and cannot establish an adequate reserve. Review actual bill dates, deposits, capital work and cleared receipts using the <a href="/blog/str-lender-reserve-requirements/">lender-reserve eligibility guide</a> and the <a href="/tools/first-str-purchase-budget/">purchase-budget worksheet</a>. A qualification credit from a retirement account is not necessarily spendable launch cash.</p>
<h2>Use the two tests to make an offer decision</h2>
<p>Proceed only when the actual lending conditions and the independent property/cash plan both fit the buyer's limits. Reprice a viable acquisition when verified expenses or accepted income change its economics. Consider an actually available financing alternative, not a hypothetical refinance. Delay within valid contract protection while decisive evidence is missing; counsel determines notice and extension rights. Reject a transaction that requires inaccurate income, unavailable cash or unsupported bookings to work.</p>
<p><a href="/apply/">Compare the shortlist with the completed income register and dated downside</a>. For <a href="/blog/buy-str-high-income-large-tax-bill/">high-income buyers with a large tax bill</a>, personal capital or an expected refund does not validate rental income. Keep private seller, guest and lender records in agreed secure channels. Share the decision memo, not passwords or unnecessary personal data.</p>
<p class="small">Primary provider text reviewed October 7, 2026; program descriptions may change and are not commitments. Educational only, not lending, tax, legal or personalized investment advice. All figures are hypothetical. No approval, income, tax benefit, financing or return is guaranteed.</p>'''

GENERAL_BODY = '''<p class="lead">A DSCR loan can be a financing option for an Airbnb acquisition when the lender evaluates accepted property income rather than using W-2 income as the qualifying method. That does not make every buyer or STR financeable. Before offering, confirm the actual borrower, property eligibility, income method, complete payment, reserves and contractual exit costs. Then test whether the property works under your own purchase budget rather than treating approval as an investment recommendation.</p>
<p><a href="/apply/">Compare the STR shortlist with written financing terms and a funded launch budget</a>. BNB Accelerator assists with acquisition analysis within its agreement; independent financing professionals make credit and loan decisions.</p>
<h2>Property-income qualification is not borrower-free lending</h2>
<p>The <a href="https://www.hostfinancial.com/short-term-rental-loans-mortgages/">Host Financial STR page</a> describes property-income qualification without personal-income documentation, but also lists personal guarantees and an approval process involving identity, liquidity, insurance, title and appraisal records. Those provider-specific descriptions illustrate why no W-2 calculation is not the same as no borrower review or personal liability. They do not establish your eligibility or the terms of another lender.</p>
<p>Ask which people and entities must qualify, provide records and sign. An LLC on the deed does not by itself release an individual from a guarantee. Do not change the intended use, ownership or income representation merely to fit a product label. The <a href="/blog/personal-guarantee-llc-str-purchase-loan/">signer-and-obligation guide</a> addresses the actual legal exposure; obtain independent counsel's explanation of the proposed documents before accepting it.</p>
<h2>Get the income method before paying for reports</h2>
<p>Send the lender the actual address, property type, intended STR use, ownership structure and available seller evidence. Ask which history, projection or market-rent documentation is accepted, who orders it, how it is adjusted and what conditions remain. Do not assume a platform export is always sufficient, every lender accepts the same projection, or a long-term rent schedule makes the property impossible to finance. A different income source can change qualification without settling the owner's economics.</p>
<p>Request the numerator and denominator in dollars, not just a ratio. Include every payment component the lender uses, with consistent monthly or annual periods. The separate <a href="/blog/dscr-vacancy-factor-str/">vacancy-factor and owner-cash worksheet</a> reconciles discounts and expenses without treating a lender haircut as an actual invoice. Use <a href="/blog/seller-proforma-vs-trailing-revenue/">verified history versus seller upside</a> for the buyer's independent revenue case.</p>
<h2>Read the complete quote as an acquisition commitment</h2>
<div class="table-wrap"><table><thead><tr><th>Item</th><th>Request in writing</th><th>Stop condition</th></tr></thead><tbody>
<tr><td>Property and borrower</td><td>Eligible use/type, entity, signers and outstanding conditions</td><td>Required use representation is untrue or essential signer refuses</td></tr>
<tr><td>Income and loan size</td><td>Accepted source, factors, payment components and revised quote</td><td>Loan amount depends on undocumented revenue</td></tr>
<tr><td>Cash and reserves</td><td>Closing cash, acceptable assets, verification dates and restrictions</td><td>Same dollars are allocated to both retained cash and vendor bills</td></tr>
<tr><td>Rate and term</td><td>Lock, adjustments, amortization, interest-only period and maturity</td><td>Plan only works after an unavailable refinance</td></tr>
<tr><td>Fees and early exit</td><td>Points, third-party costs, penalty basis/dates and payoff examples</td><td>Actual costs exceed the buyer's accepted holding plan</td></tr>
</tbody></table></div>
<p>There is no universal down payment, rate premium, property-count limit, closing time or reserve rule supplied here. Get dated offers for the same assets and assumptions, and compare actual terms through the <a href="/blog/reading-a-dscr-term-sheet/">term-sheet and two-year payoff worksheet</a>. An indicative quote, locked rate, conditional approval and authorization to fund are distinct milestones; ask which you have. Counsel and the transaction team determine the valid financing-review window.</p>
<h2>Correctly recalculate higher insurance before an offer</h2>
<p>Hypothetical arithmetic only, not a quote, likely premium or client result: $6,500 monthly lender-accepted income divided by a $5,200 complete qualifying obligation equals 1.25. If an additional $600 monthly insurance cost enters that denominator with all other inputs unchanged, the obligation becomes $5,800 and the ratio is about 1.12—not 0.98. If the fictional requirement is 1.20, it falls short. That assumption is not a published lender minimum.</p>
<p>At unchanged $6,500 accepted income, a 1.20 stipulated requirement permits a maximum $5,416.67 obligation. The $5,800 case exceeds it by about $383.33 a month. A lower loan amount may change the payment, but the required principal reduction depends on actual loan terms; this division does not calculate a new down payment. Obtain the lender's revised quote and insurance treatment, then update the owner's full expense model once, without duplicating insurance.</p>
<h2>More down payment can fix one test and break another</h2>
<p>For a separate invented cash comparison, assume $250,000 genuinely available for a $600,000 purchase. A hypothetical $450,000 loan means $150,000 down. Add $12,000 distinct cash-paid closing charges, $35,000 setup and $40,000 retained operating cash: total allocation $237,000, leaving $13,000 outside the plan. Lender asset eligibility and retained-cash requirements must still be checked separately.</p>
<p>If an available alternative loan were $425,000, down payment would rise to $175,000. Holding the other three allocations unchanged solely for comparison gives $262,000, or a $12,000 gap to available funds. Do not call this alternative approved, assume its rate/payment or remove the $40,000 reserve to conceal the gap. Recalculate all terms and dated launch needs. The <a href="/tools/first-str-purchase-budget/">purchase-budget worksheet</a> and <a href="/blog/str-lender-reserve-requirements/">reserve guide</a> separate paid expenses, qualification credits and cash that must remain.</p>
<h2>Choose the property and financing together</h2>
<p>Proceed when address-specific permission, supported property economics, accepted borrower obligations and independently funded cash all work. Compare other genuinely available investment-financing options if the proposed product fails. Never use a second-home occupancy representation that does not reflect actual intended use. A buyer's salary, substantial assets or hoped-for tax benefit does not cure a weak property forecast.</p>
<p>Reprice when verified financing or property costs change a still-viable deal. Seek valid protection or a negotiated extension when material evidence is outstanding, not an assumed cancellation right. Reject a purchase dependent on inaccurate statements, an unacceptable guarantee, unapproved refinancing or missing launch cash. Bring the actual income calculation, marked term sheet, payer/date budget and unresolved conditions to the next discussion.</p>
<p><a href="/apply/">Discuss a financed STR purchase with complete terms and a no-refinance downside</a>. Continue through the <a href="/blog/buy-str-high-income-large-tax-bill/">high-income acquisition roadmap</a>; tax conclusions belong with qualified independent advisers, not the lending ratio. Keep identity, bank and seller records in authorized secure channels.</p>
<p class="small">Primary provider text reviewed October 7, 2026. No market-wide rates, eligibility statistics or typical loan terms are asserted. Educational only, not lending, legal, tax or personalized investment advice. Numerical examples are hypothetical. No financing, approval, permit, income, tax benefit, refinance or return is guaranteed.</p>'''

VACANCY_FAQ = [
 ('Is a DSCR vacancy factor the same as actual STR occupancy?', 'Not necessarily. Identify the accepted income source and what each factor represents. A lender discount is not automatically a measurement of vacant nights or the owner’s complete costs.'),
 ('Can an STR loan qualify while owner cash flow is negative?', 'Yes in a hypothetical case with different calculations. The lender’s qualifying income and payment definition can omit distinct owner costs. Build the full property cash case independently.'),
 ('Should I subtract the lender income discount as an owner expense?', 'Not automatically. A qualification adjustment is not an invoice. Use actual buyer revenue and supported distinct costs, avoiding duplicate taxes, insurance, HOA or vacancy effects.'),
 ('Does an annual DSCR result establish enough launch cash?', 'No. Review dated receipts and outflows, actual spendable reserves and other obligations. Annual calculations do not place projected income in the operating account.')
]
GENERAL_FAQ = [
 ('Does qualifying without W-2 income mean no borrower review?', 'No. Property-income qualification is separate from credit, identity, liquidity, ownership, guarantee and property conditions. Obtain the applicable lender requirements for the actual file.'),
 ('Do all DSCR lenders accept the same Airbnb revenue?', 'No universal method is assumed. Confirm accepted history, projections or rent documentation, adjustment order and the payment denominator in writing for your property and product.'),
 ('What are the typical DSCR loan terms in 2026?', 'Do not rely on a universal table. Compare dated written offers for rate, down payment, fees, reserves, maturity, property eligibility and payoff conditions; published program descriptions are not approval.'),
 ('Does more down payment always improve an STR purchase?', 'No. It can change qualification and payment but consume setup and retained cash. Recalculate the actual quote and complete dated acquisition budget rather than assuming a lower ratio or rate fixes the deal.')
]

def refresh(slug, title, h1, desc, body, faq, published, attribute, paragraph):
    original=subprocess.check_output(['git','show','HEAD:blog/'+slug+'/index.html'],cwd=publisher.ROOT,text=True)
    checks=re.search(r'<!-- preclosing-keywords:start -->.*?<!-- preclosing-keywords:end -->',original,re.S)
    extra=[]
    if checks:
        body += checks[0]+'\n'
        old_nodes=[]
        for block in re.findall(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',original,re.S):
            d=json.loads(block); old_nodes.extend(d.get('@graph',[d]))
        for node in old_nodes:
            if node.get('@type')=='FAQPage':
                for question in node['mainEntity']:
                    if question['name'] in checks[0]:
                        extra.append(question)
    publisher.SLUG, publisher.TITLE, publisher.H1 = slug, title, h1
    publisher.DESC, publisher.BODY, publisher.FAQ = desc, body, faq
    si=publisher.ROOT/'sitemap/index.html'; old=si.read_text()
    label=re.search(r'(<a href="/blog/'+slug+r'/">)[^<]+', old)[0]
    publisher.main(published, attribute, paragraph)
    si.write_text(re.sub(r'(<a href="/blog/'+slug+r'/">)[^<]+', lambda m:label, si.read_text()))
    p=publisher.ROOT/'blog'/slug/'index.html'; s=p.read_text()
    if checks:
        s=re.sub(r'<!-- preclosing-keywords:start -->.*?<!-- preclosing-keywords:end -->\s*','',s,flags=re.S)
        s=s.replace('<div class="author-box">',checks[0]+'\n<div class="author-box">',1)
    if extra:
        def align(m):
            d=json.loads(m[2])
            for node in d.get('@graph',[d]):
                if node.get('@type')=='FAQPage': node['mainEntity'].extend(extra)
            return m[1]+json.dumps(d,indent=2)+m[3]
        s=re.sub(r'(<script[^>]*type="application/ld\+json"[^>]*>)(.*?)(</script>)',align,s,flags=re.S)
    if 'FAQPage' not in s:
        schema={'@context':'https://schema.org','@type':'FAQPage','mainEntity':[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in faq]}
        s=s.replace('</head>', '<script type="application/ld+json">'+json.dumps(schema,indent=2)+'</script>\n</head>',1)
    s=s.replace('<span>Updated October 6, 2026</span>','<span>Updated October 7, 2026</span>',1).replace('property="og:type" content="website"','property="og:type" content="article"',1)
    p.write_text(s)

if __name__=='__main__':
    refresh('dscr-vacancy-factor-str','How Does a DSCR Lender Treat STR Vacancy | BNB Accelerator','How Does a DSCR Lender Treat STR Vacancy?', 'Before buying an STR, reconcile lender income discounts and payment terms with full owner costs. Use a qualifying-ratio and dated-cash worksheet.', VACANCY_BODY,VACANCY_FAQ,'2026-09-23','data-dscr-income-review-link','Compare the <a href="/blog/dscr-vacancy-factor-str/">lender income bridge and independent owner-cash worksheet</a>. A qualifying ratio does not establish profit or launch liquidity.')
    refresh('dscr-loans-for-airbnb','DSCR Loans for Airbnb: Qualify Without W-2 Income','DSCR Loans for Airbnb: How to Qualify Without W-2 Income','Before buying an Airbnb with a DSCR loan, verify borrower conditions, accepted income, guarantees and cash. Compare written terms, not universal promises.',GENERAL_BODY,GENERAL_FAQ,'2026-08-10','data-dscr-purchase-review-link','Use the <a href="/blog/dscr-loans-for-airbnb/">DSCR acquisition checklist and financing-cash comparison</a> alongside actual lender terms. Property-income qualification is not guaranteed eligibility.')
