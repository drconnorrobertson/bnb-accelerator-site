"""Scoped correction of existing monthly cash owner; no homepage/library generator."""
import re
import expand_hold_period as publisher
SLUG='str-cash-reserves-seasonality'
BODY='''<p class="lead">Size an STR seasonal cash reserve against dated receipts and obligations before buying, not an annual revenue average alone. Two equal annual totals can leave different amounts available when a mortgage payment, repair or household commitment is due. For a buyer investing within zero to six months, the decision is whether independently available capital funds the weakest point in the purchase plan without assuming future bookings, a refund or refinancing.</p>
<p><a href="/apply/">Bring the monthly cash schedule and purchase candidate to a BNB Accelerator acquisition call</a>. This guide isolates seasonal funding; the <a href="/blog/first-90-days-airbnb-launch/">first-90-days handoff guide</a> covers readiness responsibilities, and the <a href="/blog/closing-before-peak-season-str/">peak-season closing comparison</a> covers incremental rush costs.</p>
<span id="markets"></span><h2 id="size">Build the schedule from property records</h2>
<p>Request dated seller reservation and payout records, actual availability and owner blocks, achieved lodging receipts, cancellations, recurring bills and required work. Reconcile the property and period covered; a portfolio payout or a booked calendar is not automatically the buyer's cleared cash. Record evidence gaps instead of filling them with a generic beach, mountain, desert or urban season. Do not infer the buyer's opening performance from the seller's history alone.</p>
<div class="table-wrap"><table><thead><tr><th>Schedule input</th><th>Evidence to request</th><th>Funding decision</th></tr></thead><tbody>
<tr><td>Starting property cash</td><td>Accessible balance retained after acquisition and setup</td><td>Exclude restricted or already spent funds</td></tr>
<tr><td>Receipts by date</td><td>Reservation, payout and bank reconciliation</td><td>Separate earned, booked and cleared amounts</td></tr>
<tr><td>Outflows by date</td><td>Debt terms, insurance, tax, service and utility bills</td><td>Capture large due dates, not just annual averages</td></tr>
<tr><td>Required work</td><td>Condition evidence and complete installed scope</td><td>Count each invoice once and before payment</td></tr>
<tr><td>Owner withdrawals</td><td>Chosen household and investment commitments</td><td>Reduce property cash actually left available</td></tr>
<tr><td>Retained floor and stress</td><td>Buyer-chosen separate cushion and sensitivity cases</td><td>Test the lowest dated balance, not only year-end</td></tr>
</tbody></table></div>
<p>Assign a reviewer and source date to each row. Retained cash is not itself a contractor expense; moving it between accounts does not create more money. Keep property reserves, lender qualification assets and household liquidity distinct. The <a href="/blog/str-lender-reserve-requirements/">lender-reserve guide</a> explains why an accepted qualification asset need not be spendable acquisition cash.</p>
<h2 id="shape">Correct equal-total comparison: timing changes the draw</h2>
<p>Independent hypothetical arithmetic, not market data or client results. Replace the earlier inconsistent $110,000 example with two exactly equal $108,000 receipt cases: $9,000 in each of twelve months, or $21,000 in each of four stronger months and $3,000 in each of eight weaker months. The original twelve $9,000 months total $108,000, while four $22,000 plus eight $3,000 total $112,000; those were not equal totals.</p>
<p>For this simplified comparison only, assume variable cash outflows equal 25% of each month's receipts and distinct fixed operating and debt outflows total $6,500 monthly. All modeled receipts and outflows clear by month-end. Neither amount is a fee schedule or quote. Fixed outflows include the stipulated debt cash payment; do not add that payment again. Tax, setup, replacement, distributions and intramonth timing are omitted here and tested separately.</p>
<div class="table-wrap"><table><thead><tr><th>Hypothetical month</th><th>Receipts less 25% variable outflow</th><th>Less $6,500 fixed outflow</th></tr></thead><tbody>
<tr><td>Even case: twelve months at $9,000</td><td>$6,750 each</td><td>$250 each; $3,000 for the year</td></tr>
<tr><td>Seasonal case: eight months at $3,000</td><td>$2,250 each</td><td>−$4,250 each; −$34,000 combined</td></tr>
<tr><td>Seasonal case: four months at $21,000</td><td>$15,750 each</td><td>$9,250 each; $37,000 combined</td></tr>
</tbody></table></div>
<p>Both cases have $81,000 after the assumed variable outflow and $78,000 of fixed outflows, leaving $3,000 annual net cash before the omitted items. That arithmetic does not establish an attractive return or equal acquisition cost. The seasonal case can require a substantial early draw even though its final annual net amount is positive.</p>
<h2>Start the worksheet at the actual acquisition date</h2>
<p>Assume the seasonal buyer begins immediately before the eight weaker months, with $40,000 already retained after closing and setup. Each weak month reduces cash by $4,250. No distributions or additional contributions occur. The four stronger months then add $9,250 each. This deliberately chosen sequence is not a forecast or a universal season calendar.</p>
<div class="table-wrap"><table><thead><tr><th>End of month or event</th><th>Property cash</th></tr></thead><tbody>
<tr><td>Opening retained balance</td><td>$40,000</td></tr>
<tr><td>Month 1</td><td>$35,750</td></tr>
<tr><td>Month 4</td><td>$23,000</td></tr>
<tr><td>Month 8: weakest base month</td><td>$6,000</td></tr>
<tr><td>Month 9: first stronger month</td><td>$15,250</td></tr>
<tr><td>Month 12</td><td>$43,000</td></tr>
</tbody></table></div>
<p>If the buyer separately chooses a $10,000 minimum retained floor, the base plan is $4,000 short at month 8. Starting with $44,000 would preserve that floor under these stipulated monthly flows. The floor is money retained for another chosen risk, not another operating expense or a recommended reserve for all investors. Opening after a stronger period changes the sequence; rerun every month rather than assuming a surplus belongs to the new owner.</p>
<p>For a separate repair sensitivity, use the $44,000 starting balance and add a distinct $6,000 required repair in month 4, not already included in any other allowance. The month-8 balance becomes $4,000, or $6,000 below the chosen floor. Starting with $50,000 would restore the floor under that case. A quoted repair payable before a later receipt still requires cash on its invoice date. See the <a href="/blog/hot-tub-replacement-reserve/">earlier replacement-invoice worksheet</a> for a specific capital-item funding test; no universal equipment life is assumed.</p>
<h2>Stress cleared receipts, not just booked revenue</h2>
<p><a href="https://www.airbnb.com/help/article/425">Airbnb's payout guidance</a>, reviewed October 7, 2026, distinguishes payout release from payment-provider processing and describes possible transaction reviews and delays. Verify the actual account, method, reservation and banking timeline. This does not guarantee cash a fixed number of hours after check-in or establish a delay probability for this property. Other channels require their own verified terms.</p>
<p>In a separate invented timing case, keep the $44,000 opening balance, omit the repair, and move the first stronger month's $21,000 receipt from month 9 to month 10. Stipulate that month 9's $5,250 variable bills and $6,500 fixed bills are still payable in month 9. Month 8 ends with $10,000; paying $11,750 without that receipt produces a $1,750 funding deficit at month 9, not permission to overdraw.</p>
<p>To preserve the chosen $10,000 floor through this timing case, add $11,750 independently available starting cash, for $55,750 total. When the delayed receipt arrives, later cash recovers, but that does not pay the earlier bills retroactively. The example changes timing, not annual receipts; it is not the platform's promised payout schedule. Do not automatically combine it with the repair case or deduct missing cash twice as both lost receipts and another cost.</p>
<p>Monthly ending balances can still hide a bill due before a receipt within the same month. For the tight periods, extend the schedule to actual invoice and expected cleared-payment dates. Also test supported lower receipts, an opening delay and buyer-specific simultaneous obligations. A prospective insurance recovery, tax benefit or refinance is not independently available money until its actual conditions and timing are established.</p>
<h2 id="protect">Carry the reserve requirement into the offer</h2>
<p>Separate hypothetical capital comparison: $350,000 accessible funds support a $330,000 acquisition-and-launch allocation that already includes $40,000 retained property cash. That leaves $20,000 outside. Replacing the $40,000 allocation with the base-case $44,000 requirement raises assigned cash to $334,000 and leaves $16,000 outside. If another household commitment needs $18,000, this plan is $2,000 short.</p>
<p>Using the separate repair case's $50,000 retained amount instead raises assigned cash to $340,000 and leaves $10,000 outside, an $8,000 shortfall against that household commitment. These retained amounts replace the original $40,000, not add another entire reserve on top. A purchase price change, distinct additional cash or different property may resolve the gap; an intended owner distribution or projected deduction does not.</p>
<p>Before committing, approve the monthly evidence, responsible reviewer, complete acquisition cost and chosen downside. Revise withdrawals when they would consume money needed for the dated obligations; no universal quarterly distribution schedule is prescribed. Use the <a href="/blog/first-90-days-airbnb-launch/">launch handoff</a> to resolve readiness and the <a href="/blog/buy-str-high-income-large-tax-bill/">high-income buyer roadmap</a> for the broader acquisition decision. Keep seller and personal financial records in agreed secure channels.</p>
<p><a href="/apply/">Compare the shortlisted STR using its lowest dated cash balance</a>. BNB Accelerator assists within its contracted acquisition scope; independent lenders, insurers, operators and legal/tax professionals retain their respective decisions.</p>
<p class="small">Primary payout guidance reviewed October 7, 2026. All amounts, months and timing cases are hypothetical, not property forecasts or client results. Educational information only, not personalized financial, lending, insurance, legal or tax advice. No reserve sufficiency, booking, payout date, refund or investment return is guaranteed.</p>'''
FAQ=[
('How much seasonal cash should I retain before buying an STR?', 'Build dated cleared receipts and complete outflows from property evidence, then test the lowest cash balance and a separately chosen retained floor under supported downside cases. Do not apply a universal percentage.'),
('Can equal annual revenue require different initial cash?', 'Yes. Equal annual totals can arrive on different dates. The hypothetical seasonal example draws $34,000 before stronger months replenish cash, despite a positive $3,000 annual net amount before omitted items.'),
('Does booked guest revenue pay this month’s bills?', 'Not necessarily. Verify who receives the payment, when the payout is released and when it clears. Independently fund obligations due before receipts become accessible.'),
('Should I count the same reserve in my household budget?', 'No. Keep acquisition, retained property cash and household commitments separate. Moving cash between purposes changes which risks are funded; it does not create additional money.')]
if __name__=='__main__':
 p=publisher.ROOT/'blog'/SLUG/'index.html';original=p.read_text();publisher.SLUG=SLUG
 publisher.TITLE=re.search(r'<title>(.*?)</title>',original)[1];publisher.H1=re.search(r'<h1>(.*?)</h1>',original)[1]
 publisher.DESC='Before buying an STR, test seasonal reserves with a monthly cash worksheet, equal-revenue comparison and delayed-payout case. Fund the weakest cash date.'
 publisher.BODY=BODY;publisher.FAQ=FAQ
 si=publisher.ROOT/'sitemap/index.html';old_sitemap=si.read_text()
 publisher.main(expected_publication='2026-08-11',hub_attribute='data-seasonal-reserve-cash-link',hub_paragraph='Test the <a href="/blog/str-cash-reserves-seasonality/">seasonal reserve monthly cash worksheet</a> before assuming an annual surplus funds earlier invoices.')
 s=p.read_text()
 if '<span>Updated October 7, 2026</span>' not in s:s=s.replace('<span>Published August 11, 2026</span><span>&middot;</span>','<span>Published August 11, 2026</span><span>&middot;</span><span>Updated October 7, 2026</span><span>&middot;</span>',1)
 p.write_text(s)
 si.write_text(old_sitemap)
