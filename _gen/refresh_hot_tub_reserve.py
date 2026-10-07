"""Scoped existing replacement-funding guide; no library/home generation."""
import re,json,html
import expand_hold_period as publisher
SLUG='hot-tub-replacement-reserve'
BODY='''<p class="lead">An STR hot-tub replacement reserve needs both a cost estimate and a cash date. Dividing an installed replacement quote by a chosen number of years can help plan saving, but it does not put money in the account before an earlier failure. Before buying a property with a hot tub, reconcile existing condition, complete replacement scope, cash already retained and contributions actually available before each invoice. Keep repairs and other property obligations separate.</p>
<p><a href="/apply/">Bring the installed quote and replacement-funding worksheet to a BNB Accelerator acquisition call</a>. We help evaluate the purchase plan within the acquisition agreement, not predict equipment life or guarantee replacement coverage.</p>
<h2>Verify the installed replacement scope before choosing a reserve</h2>
<p>Collect model and serial identity, documented age, service invoices, known defects, cover and connection condition, actual access constraints and the current provider's scope. Have qualified reviewers address condition, safety and any required permissions. A seller's description, a functioning control panel or a general inspection does not establish remaining useful life, regulatory compliance or suitability for the proposed use.</p>
<p>Request a complete property-specific installed bid: equipment, delivery, removal, access equipment, connection work, site preparation, applicable approvals, taxes and completion conditions. Identify exclusions and separately priced work. Remote access or additional electrical work can change the required amount; do not insert a national typical price or assume the vessel price is the invoice total.</p>
<p>Use the <a href="/blog/hot-tub-inspection-short-term-rental/">hot-tub inspection questions</a> for the condition review and the <a href="/blog/hot-tub-repair-replace-short-term-rental/">repair-or-replacement questions</a> for corrective alternatives. This page isolates replacement funding: when the bill could arrive and what cash would actually be available. It does not diagnose a unit or prescribe repair, electrical or water-care work.</p>
<h2>Use a funding register, not one annual percentage</h2>
<div class="table-wrap"><table><thead><tr><th>Input</th><th>Evidence to record</th><th>Cash treatment</th></tr></thead><tbody>
<tr><td>Complete installed amount</td><td>Dated bid, exclusions, access and payment terms</td><td>Use actual deposits and balance due dates</td></tr>
<tr><td>Cash already retained</td><td>Accessible funds assigned to this purpose</td><td>Count once, not again as unused household money</td></tr>
<tr><td>Planned contributions</td><td>Supported cash remaining after operating obligations</td><td>Count only amounts available before the invoice</td></tr>
<tr><td>Separate repair spending</td><td>Actual scope and whether it overlaps replacement work</td><td>Subtract distinct withdrawals without duplicating invoices</td></tr>
<tr><td>Earlier replacement case</td><td>Chosen sensitivity date, not a life prediction</td><td>Compare funds on that date with the complete bill</td></tr>
<tr><td>Retained balance after work</td><td>Buyer's separately chosen other-risk floor</td><td>Test remaining liquidity, not a second work expense</td></tr>
</tbody></table></div>
<p>Date every input and name the reviewer or document. A reserve contribution is an allocation of money, not another equipment invoice. In an operating worksheet, show contributions as retained cash consistently; do not deduct them as an expense and again deduct the same eventual replacement without explaining the different cash and expense views.</p>
<p>Keep this register alongside the broader <a href="/blog/hot-tub-budget-short-term-rental/">hot-tub budget questions</a>. Regular service, utilities and consumables still belong in the property budget even when replacement funding has its own account or ledger. Do not allocate the same balance to replacement, a weak operating month and another simultaneous acquisition.</p>
<h2>Keep the annual calculation, then test the date</h2>
<p>Retaining the original educational example: an assumed $11,000 installed replacement divided by a chosen four-year saving period is $2,750 per year before separate repairs. These figures are invented worksheet inputs, not a quote, manufacturer lifespan, recommended reserve, tax recovery period or forecast that the unit lasts four more years. Replace them with current scopes and adviser-reviewed condition evidence.</p>
<p>If four contributions are actually available, they total $11,000. If only two contributions have been made, they total $5,500. The annual calculation is unchanged, but the funding date is different. A planned contribution from next year's bookings cannot pay today's deposit. Use supported monthly operating cash rather than assuming all annual receipts arrive before the work.</p>
<p><a href="https://consumer.ftc.gov/articles/extended-warranties-and-service-contracts">FTC guidance dated March 2023</a> distinguishes paid extended warranties or service contracts from included warranties and recommends reviewing fees, limits, transfer terms and the claims process. It also notes that reimbursement delays can reduce the value of coverage. This consumer background does not establish coverage of STR use or your equipment. Obtain the actual contract and eligible use; do not subtract a hoped-for claim payment from independently required cash.</p>
<h2>Worked earlier-invoice test</h2>
<p>Hypothetical arithmetic only, not a client outcome or failure probability. Assume $3,000 of accessible replacement cash is retained at closing and $2,750 contributions are actually made at each year-end after all other stipulated operating obligations. A distinct $1,500 repair is paid after the first contribution, and an $11,000 replacement becomes payable after the second. Assume the repair is not included in that installed replacement scope.</p>
<div class="table-wrap"><table><thead><tr><th>Date or event</th><th>Replacement cash</th></tr></thead><tbody>
<tr><td>Closing allocation</td><td>$3,000</td></tr>
<tr><td>First actual year-end contribution</td><td>$3,000 + $2,750 = $5,750</td></tr>
<tr><td>Distinct repair paid</td><td>$5,750 − $1,500 = $4,250</td></tr>
<tr><td>Second actual contribution</td><td>$4,250 + $2,750 = $7,000</td></tr>
<tr><td>$11,000 replacement requirement</td><td>$4,000 additional funds required to pay in full</td></tr>
<tr><td>Also retain chosen $2,000 floor</td><td>$6,000 additional funds required in total</td></tr>
</tbody></table></div>
<p>The $2,000 floor is retained liquidity for another chosen risk, not another contractor bill or universal recommendation. Without new money, a worksheet balance after an $11,000 payment would be negative $4,000; that means a funding gap, not permission to overdraw. If the full installed quote instead becomes $14,000, the $7,000 balance requires $7,000 more to pay the bill, or $9,000 more to also preserve that floor.</p>
<p>A separate later scenario with the same initial $3,000, four actual $2,750 contributions, no intervening repair and the original $11,000 invoice leaves $3,000 after replacement. That exceeds the chosen $2,000 floor by $1,000 before omitted effects. It does not make the later timing certain or the earlier case unlikely. Interest, inflation, tax, financing and further work are omitted and need their own inputs.</p>
<h2>Carry the funding decision back to the offer</h2>
<p>In a separate hypothetical purchase budget, $300,000 of accessible funds support a $280,000 allocation including $40,000 retained for the property. Of that retained balance, $3,000 is assigned to the hot tub and $37,000 to other documented purposes. The total leaves $20,000 outside the acquisition. Increasing the hot-tub allocation to $9,000 while preserving the other $37,000 adds $6,000, raising assigned cash to $286,000 and leaving $14,000 outside.</p>
<p>If a separate household obligation requires $15,000, the revised plan is $1,000 short. Moving $6,000 from the other property reserve avoids raising the total but leaves those other risks less funded; it is a different decision, not free cash. Compare an accepted price or scope change, independently available additional capital, or another property without assuming a projected tax benefit or refinance supplies the difference.</p>
<p>The <a href="/blog/str-lender-reserve-requirements/">lender reserve guide</a> distinguishes qualification assets from spendable buyer cash. A retirement-account credit accepted by a lender does not itself fund this replacement. Use the property's actual monthly operating schedule to test contribution capacity; do not import a generic seasonality pattern or promised first-year shortfall.</p>
<h2>Approve a funded plan and assign its review</h2>
<p>Before removing purchase protections, resolve decisive condition, installed scope, permission and coverage questions with the appropriate professionals. Record who updates the quote, authorizes spending and reviews the balance after a repair or operating shortfall. Set review triggers using actual new findings, rather than treating the original reserve calculation as permanent.</p>
<p><a href="/apply/">Compare the shortlisted STR with the earlier-invoice funding case</a>, the <a href="/blog/amenity-roi-ranking/">broader amenity purchase comparison</a> and the <a href="/blog/buy-str-high-income-large-tax-bill/">high-income acquisition roadmap</a>. BNB Accelerator coordinates acquisition work within the agreed scope; independent professionals determine technical, insurance, lending, legal and tax conclusions. Keep seller service records and financial statements in agreed secure channels.</p>
<p class="small">FTC primary guidance reviewed October 7, 2026; source is dated March 2023. Educational information only, not inspection, engineering, insurance, legal, lending, tax or personalized investment advice. All examples are hypothetical. No equipment life, coverage payment, booking income, tax benefit or return is guaranteed.</p>'''
FAQ=[
('Does an annual hot-tub reserve fund an earlier replacement?', 'Not necessarily. Compare accessible cash already retained and contributions actually made before the invoice with the complete installed bill and any separately chosen retained balance.'),
('Is the four-year saving example a hot-tub lifespan forecast?', 'No. The assumed $11,000 divided by four years is an educational saving calculation, not a manufacturer life estimate, quote, tax recovery period or recommended reserve.'),
('Can a service contract replace my replacement cash?', 'Do not assume it can. Review actual eligible use, coverage, fees, transfer and payment timing; independently fund amounts needed before any confirmed payment is available.'),
('Can the same reserve cover replacement and other acquisition obligations?', 'Money cannot pay two simultaneous bills. Keep purpose allocations visible and test what remains for operating risks and household commitments if funds move between them.')]
if __name__=='__main__':
 source=(publisher.ROOT/'blog'/SLUG/'index.html').read_text();publisher.SLUG=SLUG
 publisher.TITLE=re.search(r'<title>(.*?)</title>',source)[1];publisher.H1=re.search(r'<h1>(.*?)</h1>',source)[1]
 publisher.DESC='Before buying an STR, fund hot-tub replacement by invoice date. Use an installed-cost register and an earlier-replacement cash-shortfall worksheet.'
 publisher.BODY=BODY;publisher.FAQ=FAQ
 publisher.main(expected_publication='2026-09-23',hub_attribute='data-hot-tub-reserve-link',hub_paragraph='Test <a href="/blog/hot-tub-replacement-reserve/">hot-tub replacement cash on an earlier invoice date</a> rather than assuming an annual reserve contribution will be available in time.')
 p=publisher.ROOT/'blog'/SLUG/'index.html';s=p.read_text()
 s=s.replace('<span>Updated October 6, 2026</span>','<span>Updated October 7, 2026</span>')
 if '"@type": "FAQPage"' not in s:
  faq={'@context':'https://schema.org','@type':'FAQPage','mainEntity':[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in FAQ]}
  s=s.replace('</head>','<script type="application/ld+json">'+json.dumps(faq,indent=2)+'</script>\n</head>',1)
 p.write_text(s)
 p=publisher.ROOT/'sitemap/index.html';s=p.read_text();s=re.sub(r'(<a href="/blog/'+SLUG+r'/">)[^<]+',lambda m:m[1]+publisher.H1,s);p.write_text(s)
