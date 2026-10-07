"""Scoped existing occupancy owner correction; no old or homepage generator."""
import re
import expand_hold_period as publisher
SLUG='airbnb-occupancy-rates-explained'
BODY='''<p class="lead">Airbnb occupancy rates help an STR buyer understand how often nights were booked, but do not establish profit, cash availability or a fair purchase price. Before committing within the next zero to six months, reconcile the seller's dates, available nights, lodging revenue and costs. A high-income buyer with a large tax bill still needs an independently viable acquisition; a projected deduction does not repair weak operating cash.</p>
<p><a href="/apply/">Bring the property candidate and seller metrics worksheet to an acquisition call</a>. This guide tests the numbers behind an occupancy claim, not a universal market benchmark or a promise that pricing changes will fill a calendar.</p>
<h2 id="definition">Name the denominator before comparing occupancy</h2>
<p><a href="https://www.airbnb.com/help/article/2715">Airbnb's professional-hosting metrics guidance</a>, reviewed October 7, 2026, defines average occupancy using booked nights divided by nights available to book across the relevant listings. It separately describes blocked nights, unbooked calendar nights, check-ins and length of stay. Its average nightly rate uses nightly revenue divided by booked listing nights. Verify the selected listings and reporting dates; this definition does not establish every seller spreadsheet's method.</p>
<p>For a single property, record booked nights, available nights and all calendar nights separately. In an invented 180-night period, 60 nights are blocked, leaving 120 available. If 96 are booked, available-night occupancy is 96 / 120 = 80%; booked nights as a share of the full calendar are 96 / 180 = 53.33%. The remaining 24 available nights are unbooked. These figures describe the same assumed calendar, not two different demand forecasts.</p>
<p>Ask why each block existed: owner use, maintenance, permission restrictions or another reason. Removing 60 blocks in a buyer's spreadsheet does not prove 60 additional nights will sell. Request evidence for a changed-use scenario and check that intended stays are permitted. Neither a blocked calendar nor a modeled market estimate is a substitute for seller reservation and revenue records.</p>
<h2>Build a seller-metrics evidence register</h2>
<div class="table-wrap"><table><thead><tr><th>Input</th><th>Evidence and reconciliation</th><th>Buyer consequence</th></tr></thead><tbody>
<tr><td>Property and period</td><td>Address, listing/channel identifiers, exact reporting dates and source date</td><td>Exclude portfolio totals and mismatched seasons</td></tr>
<tr><td>Night counts</td><td>Reservation ledger, availability, blocks and cancellation history</td><td>Separate booked, completed and canceled stays</td></tr>
<tr><td>Lodging revenue</td><td>Reservation amounts, adjustments, payouts and bank reconciliation</td><td>Identify fees, taxes, refunds and cleared cash separately</td></tr>
<tr><td>Turnovers and variable costs</td><td>Check-ins, cleaning invoices, consumables and management terms</td><td>Do not infer cleaning count from occupancy alone</td></tr>
<tr><td>Fixed costs and financing</td><td>Insurance, property tax, utilities, service and actual loan terms</td><td>Compare recurring obligations and complete purchase capital</td></tr>
<tr><td>Buyer changes</td><td>Owner-use plan, launch timing, required work and operating scope</td><td>Model differences rather than inheriting the seller's result</td></tr>
</tbody></table></div>
<p>Assign a reviewer to unresolved rows. When combining channels, reconcile duplicate bookings and do not count the same night's revenue twice. A confirmed reservation is not necessarily a completed stay or cleared receipt; show cancellation adjustments explicitly. Keep personal guest details and seller financial documents in agreed secure channels. Unknown evidence stays unknown, rather than becoming a favorable assumption.</p>
<h2 id="revpar">RevPAR combines rate and occupancy, not costs</h2>
<p>For this worksheet, revenue per available night, or RevPAR, means lodging revenue divided by available nights, excluding cleaning receipts and taxes. With the same revenue scope and period, average lodging rate multiplied by available-night occupancy produces that figure. Choose and disclose the scope instead of mixing lodging-only rates with fee-inclusive totals.</p>
<p>RevPAR is not immune to denominator changes and is not net cash. A price reduction may increase bookings, but whether total lodging revenue improves depends on the actual response. There is no guarantee any property reaches 90% occupancy at a sufficiently low price. Compare revenue per calendar night as a separate normalization when availability differs, while retaining the explanation for legitimate blocks.</p>
<h3>Worked comparison: higher RevPAR can coexist with lower cash</h3>
<p>Independent hypothetical arithmetic, not actual cabins, market evidence, client results or a forecast. Both candidates have exactly 100 available nights in the same assumed period. Candidate A books 82 nights at $310; B books 61 at $520. Stipulate A has 41 two-night stays, while B has 61 one-night stays. Thus the lower-occupancy candidate has more turnovers in this example.</p>
<div class="table-wrap"><table><thead><tr><th>Stipulated measure for the period</th><th>Candidate A</th><th>Candidate B</th></tr></thead><tbody>
<tr><td>Occupancy</td><td>82 / 100 = 82%</td><td>61 / 100 = 61%</td></tr>
<tr><td>Lodging revenue</td><td>82 × $310 = $25,420</td><td>61 × $520 = $31,720</td></tr>
<tr><td>Revenue per available night</td><td>$254.20</td><td>$317.20</td></tr>
<tr><td>Less stipulated 20% non-cleaning variable outflow</td><td>$20,336 remains</td><td>$25,376 remains</td></tr>
<tr><td>Less cleaning at stipulated $150 per turnover</td><td>41 × $150 = $6,150</td><td>61 × $150 = $9,150</td></tr>
<tr><td>Contribution after those outflows</td><td>$14,186</td><td>$16,226</td></tr>
<tr><td>Less distinct fixed operating and debt cash outflows</td><td>$12,000</td><td>$18,000</td></tr>
<tr><td>Remaining cash before omitted items</td><td>$2,186</td><td>−$1,774</td></tr>
</tbody></table></div>
<p>The 20% and $150 inputs are invented, not platform fees, operator quotes or recommendations. The cleaning outflow is excluded from the 20% assumption and counted once; cleaning receipts are not included. Fixed amounts include the stipulated debt cash payments, not a second debt deduction. Required capital work, income taxes, distributions, acquisition costs and intraperiod payment timing are omitted.</p>
<p>B has higher RevPAR and contribution but lower remaining cash under these deliberately different fixed-cost assumptions. This does not automatically make A the better investment: purchase price, required capital, permission, condition and risk still need comparison. Replace every input with property evidence and financing terms; do not rank two offers using occupancy or RevPAR alone.</p>
<h2 id="ranges">Use matched evidence, not a universal good range</h2>
<p>This guide does not prescribe 60–75% annual occupancy or a fixed peak-season threshold as a verified benchmark. Establish a relevant comparison period and explain differences in capacity, condition, permitted use, owner blocks and achieved rate. A seller's best weeks cannot stand in for an entire year. Historical comparable results inform scenarios; they do not guarantee the buyer's opening performance.</p>
<p>Request the source methodology and uncertainty behind modeled figures, including how unavailable nights and active listings are treated. Evaluate actual supply and permission evidence rather than assuming every new permit will become a competing listing or that more supply alone establishes declining demand. Use the <a href="/blog/how-to-analyze-airbnb-deal/">property underwriting guide</a> for the broader offer decision.</p>
<h2 id="seasonality">Carry monthly cash and lender methods into the offer</h2>
<p>The same annual occupancy can be distributed differently across months. Whether weak months require a reserve depends on rates, receipts, costs and dated obligations, not occupancy alone. Build the <a href="/blog/str-cash-reserves-seasonality/">monthly seasonal cash worksheet</a> and the <a href="/blog/how-much-money-to-start-airbnb/">complete entry-cost budget</a>. Annual averages cannot pay a bill before a receipt clears.</p>
<p>For financing, ask the actual lender which rental evidence, expense assumptions and vacancy treatment its program accepts. Do not assert every DSCR lender uses the same annual occupancy method. The <a href="/blog/dscr-loans-for-airbnb/">DSCR purchase-method guide</a> separates property cash analysis from lender qualification.</p>
<h2 id="raise">Treat proposed improvements as funded scenarios</h2>
<p>Photography, pricing changes, minimum stays or amenities are hypotheses to evaluate, not automatic occupancy improvements. Obtain scope and cost, confirm permission and operating responsibility, and compare a no-uplift case with an evidence-supported alternative. A review target does not guarantee search placement or bookings; a hot tub is not universally superior to a game room.</p>
<p>Use the <a href="/blog/first-90-days-airbnb-launch/">first-90-days readiness handoff</a> to assign launch tasks and the <a href="/blog/amenity-roi-ranking/">amenity contribution worksheet</a> before spending. Minimum-stay choices require permission, economics and adviser review where tax treatment is relevant; a dashboard percentage alone establishes none of them.</p>
<p><a href="/apply/">Discuss the acquisition shortlist with a reconciled occupancy and cash memo</a>: source dates, denominator, lodging revenue, turnovers, actual costs, funded launch and unresolved evidence. BNB Accelerator assists within its contracted acquisition scope; independent lenders and legal, tax and operating professionals retain their decisions. Continue through the <a href="/blog/buy-str-high-income-large-tax-bill/">high-income buyer roadmap</a>.</p>
<p class="small">Primary platform definitions reviewed October 7, 2026. Educational information only, not personalized investment, lending, tax or legal advice. All worked figures are hypothetical. No occupancy, booking, ranking, deduction, cash sufficiency or investment return is guaranteed.</p>'''
FAQ=[
('What is a good Airbnb occupancy rate?', 'There is no universal threshold established here. Verify the period, denominator, achieved lodging rate, permission, costs and buyer use; compare supported property scenarios instead of treating one percentage as proof of profit.'),
('What is RevPAR for a short-term rental?', 'In this worksheet it is lodging revenue divided by available nights, with cleaning receipts and taxes excluded. It combines rate and occupancy but does not deduct costs or establish net cash.'),
('Why do occupancy numbers differ between sources?', 'They can use different periods, listings and denominators. Separate booked, available, blocked and calendar nights and verify each source methodology before comparing percentages.'),
('Does high occupancy mean a property is profitable?', 'No. Profit and cash depend on rates, costs, financing and other obligations. Occupancy alone does not establish turnover count, and reducing price does not guarantee a full calendar.')]
if __name__=='__main__':
 p=publisher.ROOT/'blog'/SLUG/'index.html';publisher.SLUG=SLUG
 publisher.TITLE="Airbnb Occupancy Rates: Buyer Underwriting Worksheet"
 publisher.H1='Airbnb Occupancy Rates Explained'
 publisher.DESC='Verify Airbnb occupancy before buying an STR. Compare booked and available nights, RevPAR, turnovers and net cash with an original buyer worksheet.'
 publisher.BODY=BODY;publisher.FAQ=FAQ
 si=publisher.ROOT/'sitemap/index.html';old_sitemap=si.read_text()
 publisher.main(expected_publication='2026-08-10',hub_attribute='data-occupancy-cash-review-link',hub_paragraph='Reconcile the <a href="/blog/airbnb-occupancy-rates-explained/">occupancy denominator and RevPAR-to-cash worksheet</a> before treating a seller percentage as proof of a viable acquisition.')
 s=p.read_text()
 if '<span>Updated October 7, 2026</span>' not in s:
  s,n=re.subn(re.escape('<span>Published August 10, 2026</span><span>&middot;</span>'),'<span>Published August 10, 2026</span><span>&middot;</span><span>Updated October 7, 2026</span><span>&middot;</span>',s,count=1);assert n==1
 p.write_text(s);si.write_text(old_sitemap)
