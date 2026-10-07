"""One existing calculator refresh; preserve its independent purchase checks."""
import json,re
import expand_hold_period as page

page.SLUG='airbnb-cash-on-cash-return'
page.TITLE='Airbnb Cash-on-Cash Return: Purchase Worksheet'
page.H1='Airbnb Cash-on-Cash Return: A Purchase Worksheet'
page.DESC='Calculate Airbnb cash-on-cash return with supported costs, all-in purchase cash and a launch-year stress test. Keep tax estimates and reserves separate.'
page.FAQ=[
('How do you calculate Airbnb cash-on-cash return?', 'Divide annual pre-tax owner cash after recurring costs and full debt service by a stated cash-invested denominator. Include required purchase and setup cash, define reserve treatment and use the same period throughout.'),
('What is a good cash-on-cash return for an STR purchase?', 'There is no universal percentage that establishes suitability. Set buyer-specific distribution, liquidity and downside requirements, then evaluate property evidence and actual financing. A revenue-to-price shortcut does not replace underwriting.'),
('Should I use stabilized revenue for the first year?', 'Not without clearly labeling a separate stabilized scenario. Model actual closing, work, permission and launch dates; include the obligations due before receipts begin. Keep a first-year cash calendar alongside the annual calculation.'),
('Should tax savings be included in cash-on-cash return?', 'Keep the pre-tax operating calculation separate from adviser-reviewed tax effects. An estimated deduction is not an operating receipt or guaranteed refund, and prospective cash should not fund bills before it is available.')]
page.BODY='''<p class="lead">Airbnb cash-on-cash return is annual pre-tax owner cash divided by the cash invested under an explicitly stated definition. It is useful before a purchase only when both sides of the fraction are supported. A forecast is not a realized return, and a strong percentage does not establish lawful use, adequate reserves or an acceptable downside. Buyers planning to acquire an STR within zero to six months should request the underlying register, not just a target yield.</p>
<p>This worksheet separates launch-year cash, stabilized cash and retained reserves. It does not publish national market-return bands or a universal revenue-to-price cutoff. <a href="/apply/">Bring a candidate property's cash model and your purchase budget to an acquisition call</a>; the purpose is to decide whether the actual property fits your capital, distribution needs and responsibility plan.</p>
<h2>Build the Airbnb cash-on-cash calculation from source records</h2>
<p>Start with supportable collected receipts for the purchased address, not a listing's asking rate multiplied by every calendar night. Normalize personal-use blocks, unavailable rooms, refunds and missing operating periods. Reconcile the <a href="/blog/reconcile-airbnb-payout-export/">seller payout evidence</a> before using it as a forecast. Calendar occupancy alone does not prove paid demand or owner profit.</p>
<p>Subtract owner-paid recurring costs and full debt payments. Include property tax, insurance, utilities, management, platform fees, cleaning and ordinary repairs as applicable, each once. If a receipt is already net of a platform fee, do not deduct that fee again. If cleaning reimbursements are included in receipts, include the corresponding owner cost. Do not label the debt-inclusive balance NOI.</p>
<p><a href="https://www.airbnb.com/help/article/1857">Airbnb's current service-fee guidance</a> describes split and single fees and a migration to the single structure. Most single-fee hosts pay 15.5%, with exceptions; that is not every listing's guaranteed fee. Verify the prospective listing/manager arrangement, reservation timing and fee base. A seller's historical fee assumption may differ from the buyer's operation. This source was reviewed October 7, 2026.</p>
<div class="table-wrap"><table><thead><tr><th>Input register</th><th>Evidence required</th><th>Decision check</th></tr></thead><tbody>
<tr><td>Collected receipts</td><td>Property records, comparable support and available-night calendar</td><td>Distinguish observed collections from forecasts</td></tr>
<tr><td>Recurring owner costs</td><td>Current quotes, fee bases and management inclusions</td><td>Identify missing, reimbursed or duplicated costs</td></tr>
<tr><td>Financing</td><td>Actual use-appropriate payment, fees and conditions</td><td>Include full payment, not interest alone</td></tr>
<tr><td>Purchase/setup cash</td><td>Settlement inputs and required furnishing/work quotes</td><td>Credit earnest money once; include required setup</td></tr>
<tr><td>Timing and reserves</td><td>Launch calendar, property condition and accessible cash</td><td>Fund bills due before income and define retained allocations</td></tr>
</tbody></table></div>
<h2>Worked launch-year and stabilized-year comparison</h2>
<p>Hypothetical arithmetic only, not a market forecast, client result, loan quote or recommended reserve amount. Assume a January closing and an April rental launch. Required early cash is $125,000 purchase equity plus $15,000 cash-paid closing costs and $40,000 furnishing/required capital setup: $180,000 deployed. The setup amount excludes debt and recurring costs modeled below. Another $20,000 is funded retained cash, making total committed capital $200,000.</p>
<p>The launch case includes nine months of receipts and the full calendar year's modeled obligations. The stabilized case is a separate full operating year, not additional year-one income. Neither assumes appreciation, principal-paydown cash or tax receipts. The hypothetical recurring totals include all owner-paid operating costs and exclude the separately shown debt, capital setup and retained replacement allocation.</p>
<div class="table-wrap"><table><thead><tr><th>Illustrative annual line</th><th>Launch year</th><th>Stabilized year</th></tr></thead><tbody>
<tr><td>Collected receipts</td><td>$54,000</td><td>$72,000</td></tr>
<tr><td>Recurring nondebt owner costs</td><td>$32,000</td><td>$36,000</td></tr>
<tr><td>Full debt payment</td><td>$30,000</td><td>$30,000</td></tr>
<tr><td>Pre-tax owner cash before allocation</td><td>−$8,000</td><td>$6,000</td></tr>
<tr><td>Cash / $180,000 deployed, rounded</td><td>−4.44%</td><td>3.33%</td></tr>
<tr><td>Cash / $200,000 committed</td><td>−4.00%</td><td>3.00%</td></tr>
<tr><td>Distinct retained replacement allocation</td><td>$4,000</td><td>$4,000</td></tr>
<tr><td>After allocation</td><td>−$12,000</td><td>$2,000</td></tr>
</tbody></table></div>
<p>The stabilized 3.33% deployed-cash figure does not describe the launch year's −$8,000 operating cash or its $12,000 after-allocation funding requirement. Keeping a replacement allocation is a cash-retention policy, not an expense already incurred. The initial $20,000 reserve is committed cash; it is not another operating receipt. When work is actually paid, reconcile the expenditure to the reserve rather than subtracting both the allowance and the same repair twice.</p>
<p>The $20,000 initial reserve exceeds the modeled $12,000 launch funding requirement by $8,000 only if it is fully accessible, available for those uses and no other cash needs intervene. That arithmetic does not prove adequacy or lender permission. Build a monthly calendar: an annual total can hide a bill due before a payout. Show any required minimum balance, restricted funds and separate household obligations.</p>
<h2>Stress the numerator without improving the denominator</h2>
<p>For an independent stabilized downside, reduce receipts by $15,000 while only $3,000 of avoidable costs disappear. Owner cash becomes $6,000 − $15,000 + $3,000 = −$6,000; retaining the $4,000 allocation creates a $10,000 funding requirement. Keep the original purchase denominator for that comparison. Do not shrink invested cash just because the property performed poorly.</p>
<p>A revenue-to-price ratio cannot establish this result because it omits costs, financing, setup, timing and permission. Nor does a larger bedroom count or a luxury address guarantee higher usable returns or lower damage. Request property-specific demand and cost evidence. If considering another rental strategy, use the <a href="/blog/airbnb-vs-long-term-rental-roi/">two-strategy committed-capital comparison</a> rather than relabeling this calculator as a separate market promise.</p>
<p>Compare management proposals on the actual fee base, included tasks, extra costs and response coverage. A cheaper quoted percentage is not automatically the cheaper complete service. Owner work has a real responsibility burden even when this cash worksheet does not assign it a salary. Different leverage also changes both required equity and the payment; a higher headline percentage can carry a larger cash shortfall.</p>
<h2>Decide what a good return means for this buyer</h2>
<p>Write minimum spendable cash, uncommitted liquidity, acceptable downside funding and evidence deadlines before choosing a property. An affluent buyer's large tax bill does not establish a suitable property. Keep adviser-reviewed tax effects separate; no projected deduction or refund belongs in this pre-tax numerator. Use the <a href="/blog/str-tax-benefit-shortfall-purchase/">no-benefit funding case</a> and the <a href="/tools/first-str-purchase-budget/">purchase budget</a> before committing.</p>
<p>Cash-on-cash does not measure total holding-period return. Forecast appreciation, eventual sale costs, debt payoff and tax outcomes need a separately dated analysis. Principal reduction is not an annual distribution, and prospective cash is not cash received. Proceed only when lawful use, supported receipts, quoted costs, financing and launch funding meet your actual constraints. Reprice a viable plan when verified costs change; delay within valid protections for missing evidence; decline one that depends on omitted bills or an assured future result.</p>
<p><a href="/apply/">Discuss the property with its completed input register and monthly cash calendar</a>. BNB Accelerator assists within contracted acquisition scope; independent professionals decide tax, legal, lending and insurance conclusions. Keep sensitive records in agreed secure channels. Educational information only, not personalized investment, tax, legal or lending advice. Example numbers are hypothetical; no booking, financing, deduction, refund or return is guaranteed.</p>'''

if __name__=='__main__':
 p=page.ROOT/'blog'/page.SLUG/'index.html'; old=p.read_text()
 checks=re.search(r'<!-- preclosing-keywords:start -->.*?<!-- preclosing-keywords:end -->',old,re.S)[0]
 extra=[]
 for raw in re.findall(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',old,re.S):
  for n in json.loads(raw).get('@graph',[]):
   if n.get('@type')=='FAQPage':extra=[q for q in n['mainEntity'] if q['name'].startswith('How do I ')]
 assert len(extra)==5
 page.BODY+='\n'+checks
 page.main('2026-08-10','data-cash-return-review-link','Use the <a href="/blog/airbnb-cash-on-cash-return/">cash-on-cash input register and launch-year funding test</a> before accepting a market-wide return promise.')
 s=p.read_text()
 def schema(m):
  d=json.loads(m[2])
  for n in d.get('@graph',[]):
   if n.get('@type')=='FAQPage':n['mainEntity']+=extra
  return m[1]+json.dumps(d,indent=2)+m[3]
 s=re.sub(r'(<script[^>]*type="application/ld\+json"[^>]*>)(.*?)(</script>)',schema,s,flags=re.S)
 p.write_text(s)
