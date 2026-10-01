#!/usr/bin/env python3
"""Three distinct buyer resources plus contextual discovery links; rerunnable."""
from pathlib import Path
import sys, re, json
sys.path.insert(0, str(Path(__file__).parent))
import tpl
from pillars import sections_html
ROOT=Path(__file__).resolve().parents[1]
DATE='2026-10-01'
PAGES=[
('/short-term-rental-investment-service/', 'Short-Term Rental Investment Service | BNB Accelerator',
 'Compare short-term rental investment services, understand BNB Accelerator’s acquisition scope, and review ownership, fees, due diligence and launch responsibilities.',
 'Short-term rental investment service for property buyers',
 'BNB Accelerator coordinates the search, evaluation, purchase and launch planning for a short-term rental you own. Start by deciding which work you want help with and which decisions you will retain.', [
 ('Choose the service that matches your purchase',[
 'The phrase short-term rental investment service can describe very different arrangements. An acquisition coordinator helps you assemble and execute a purchase plan. An agent handles work covered by a representation agreement. A manager operates the property. A course provides education. A pooled investment has a different ownership structure. Compare the written engagement rather than treating these labels as interchangeable.',
 ('table',['Service','Deliverable to verify','Your decision'],[
 ['Acquisition coordination','Property shortlist, analysis, milestone tracking and launch handoff','Approve the property, assumptions, budget and vendors'],
 ['Buyer representation','Search, offers and transaction services stated in the agency agreement','Select the agent and approve contractual commitments'],
 ['Property management','Guest operations, pricing, maintenance and owner reporting','Approve spending limits and monitor performance'],
 ['Education','Lessons, coaching or resources','Perform or separately contract the acquisition work']])]),
 ('What BNB Accelerator coordinates',[
 'Our acquisition model combines market research, sourcing, underwriting, purchase coordination and launch planning. Review the <a href="/done-for-you-airbnb/">done-for-you Airbnb service scope</a> and the <a href="/how-it-works/">acquisition sequence</a>. Independent agents, lenders, attorneys, designers, managers and tax advisers perform their separately contracted services. Confirm the scope for your engagement in writing.',
 'You supply the capital and make the final purchase decision. Ask who prepares each analysis, who checks the evidence, who has authority to commit money and who handles the operating handoff. A coordinated process does not eliminate property risk or the need for independent diligence.']),
 ('Price the complete engagement, not just the fee',[
 'The service fee is separate from down payment, closing costs, improvements, furnishings and reserves. BNB Accelerator does not publish a fixed public service fee. Request a current itemized proposal covering payment milestones, cancellation terms, exclusions and vendor charges. Start with the <a href="/pricing/">pricing guide</a> and <a href="/buy-a-short-term-rental/acquisition-budget-worksheet/">purchase budget worksheet</a>.',
 'Illustrative budget: $80,000 down payment + $12,000 closing costs + $35,000 setup + $18,000 reserves = $145,000 before any acquisition service fee. Adding a hypothetical $15,000 fee produces $160,000 total cash required. These invented inputs demonstrate the method; they are not a quote or an estimate for your property. A cheaper fee does not compensate for an unsupported revenue model or an incomplete setup budget.']),
 ('Ask for a property decision file before approval',[
 'A useful file connects every consequential assumption to evidence: seller statements for historical income, independent comparable listings for a forecast, vendor quotes for setup, and written address-specific checks for permitted use. Keep <a href="/guides/str-deal-evidence-register/">an evidence register</a> so unresolved items remain visible.',
 'Compare a base case and a downside case using the same expense categories. Separate historical revenue from projected revenue and identify what could change after transfer. Read the <a href="/airbnb-investment-property/">investment property evaluation guide</a> and <a href="/case-studies/">specific client examples</a>; another property’s outcome is not your expected return.']),
 ('Put launch and owner oversight in writing',[
 'Closing is one milestone. Keys, utilities, insurance, furnishings, cleaning, photography, listing access, vendor accounts and management reporting need assigned owners. Use the <a href="/guides/str-service-responsibility-matrix/">service responsibility matrix</a> to define each deliverable and its acceptance evidence.',
 'Agree with the selected manager on reporting frequency, maintenance authorization and escalation before the first guest. Discuss any tax eligibility with your own CPA. Neither an acquisition service nor a management agreement establishes a tax deduction.']),
 ('Review the evidence and discuss fit',[
 'Read <a href="/reviews/">public reviews</a>, <a href="/testimonials/">direct client stories</a> and the <a href="/compare/">comparison library</a>. Ask for references whose purchase and operating arrangement resemble yours. Bring the budget, timeline and unresolved evidence to a <a href="/apply/">purchase planning call</a>.'])]),
('/guides/str-service-responsibility-matrix/', 'STR Acquisition Service Responsibility Matrix | BNB Accelerator',
 'Use a deliverable-by-deliverable matrix to compare an STR acquisition proposal, assign approvals, document excluded costs and prepare the operating handoff.',
 'Build an STR acquisition service responsibility matrix',
 'Turn a service proposal into a working purchase plan: one accountable owner, one approval authority, a due date and acceptance evidence for each deliverable.', [
 ('Start with outputs instead of job titles',[
 'Done-for-you is a service description, not a complete specification. A buyer can have a coordinator, agent, lender, designer and manager involved while still discovering that nobody owns a particular deliverable. Ask for an output you can review rather than a promise that a task will be handled.',
 'Create the matrix before committing to a service proposal. Use names or contracted firms in the owner column; team is too vague when a deadline slips. Keep the signer or spending approver separate from the person doing the work. This is an operating checklist, not a substitute for the signed contracts.']),
 ('Copy this matrix into your purchase file',[
 ('table',['Deliverable','Proposed owner to confirm','Acceptance evidence','Buyer approval'],[
 ['Buy box and budget','Buyer with acquisition coordinator','Written criteria and total cash limit','Approve criteria'],
 ['Revenue and cost analysis','Named analyst or coordinator','Sources, assumptions and downside model','Approve investment decision'],
 ['Legal-use verification','Appropriate local authority and advisers','Address-specific written findings and open issues','Decide with advisers'],
 ['Offer and deadlines','Retained buyer agent or attorney','Executed documents and milestone calendar','Authorize commitments'],
 ['Inspection follow-up','Buyer agent with qualified inspectors','Reports, repair scope and quotes','Approve negotiation'],
 ['Loan and insurance','Selected lender and insurer','Written terms and coverage documents','Accept terms'],
 ['Furnishing and setup','Selected designer and vendors','Approved scope, invoices and inventory','Approve budget changes'],
 ['Operating handoff','Selected property manager','Access checklist and reporting agreement','Accept handoff']]),
 'These are proposed role assignments to confirm, not a claim that a BNB Accelerator fee includes every row. Record exclusions, vendor payment terms and handoffs in the actual engagement.']),
 ('Add five fields to every row',[
 ('ol',['Accountable owner: who follows the task through to acceptance?','Approval authority: who may sign or authorize spending?','Due date: which purchase or launch milestone makes this time-sensitive?','Cost treatment: included service fee, separate invoice or buyer expense?','Escalation: who is contacted when evidence is incomplete or the deadline is at risk?']),
 'Example: photography is assigned to the manager, the buyer approves the $900 quote, delivery is required before listing review, the invoice is a separate setup expense, and a missed date escalates to the coordinator. The $900 is an invented example, not a market rate. Listing access and image-use rights remain separate acceptance items.']),
 ('Check what happens when a purchase falls through',[
 'Ask which fees remain payable, which services transfer to another property and which vendor commitments can be cancelled. Have the appropriate advisers review contractual terms. Do not infer refund rights from a sales conversation.',
 'Document who archives the inspection reports and closes out vendor requests. A failed purchase should leave a clear record of the decision and the remaining cash obligations, not an unassigned list of tasks.']),
 ('Accept the handoff with evidence',[
 'At launch, confirm the manager has the agreed access, approved inventory, cleaning contacts, emergency contacts and reporting schedule. Reconcile the final budget to approved changes. Keep unresolved items in an open-issues log with an owner and due date.',
 'Read the <a href="/short-term-rental-investment-service/">investment service overview</a>, <a href="/done-for-you-airbnb/">acquisition scope</a> and <a href="/management/">management options</a>. Use the <a href="/guides/str-deal-evidence-register/">deal evidence register</a> for investment assumptions, rather than mixing unresolved evidence with routine task completion.'])]),
('/guides/str-deal-evidence-register/', 'STR Deal Evidence Register: Verify Assumptions | BNB Accelerator',
 'Build an STR deal evidence register linking revenue, expenses, condition and launch assumptions to source records, verification owners and unresolved purchase decisions.',
 'Build an evidence register for an STR purchase',
 'An attractive pro forma becomes useful only when its assumptions can be checked. Keep a register that links each consequential claim to its source, date, reviewer and unresolved decision.', [
 ('One row for each claim that could change the decision',[
 'Do not store an unlabeled pile of documents and assume that diligence is complete. Separate the claim from the source: seller annual revenue is a claim; a booking report is one piece of evidence. Record what the report covers, who reconciled it and what remains excluded.',
 'Use three statuses: verified for the stated purpose, provisional, and unresolved. Verified means the named reviewer completed a specific check; it does not guarantee future performance. Preserve the original source and record the date reviewed.']),
 ('Use this register structure',[
 ('table',['Claim or assumption','Source to request','Check','Decision if unresolved'],[
 ['Historical booking revenue','Booking export, payout records and owner statements for the same period','Reconcile cancellations, fees and dates','Do not treat seller headline as verified income'],
 ['Projected nightly rate','Dated comparable set with capacity and amenity notes','Explain adjustments and seasonality','Run a lower-rate case'],
 ['Management cost','Written proposal and sample owner statement','Check fee base, minimums and add-on charges','Model the complete fee stack'],
 ['Setup budget','Itemized bids and furnishing inventory','Separate included items from new purchases','Reserve for unquoted work'],
 ['Permitted rental use','Address-specific authority and adviser findings','Check restrictions and transfer requirements','Resolve before relying on rental income'],
 ['Insurance cost','Property-specific insurer quote','Confirm intended use and exclusions with insurer','Rework cash flow if unavailable'],
 ['Launch timing','Vendor schedule and manager checklist','Identify dependencies and approval dates','Model delayed first bookings']]),
 'Add a source link or filename, covered period, checked date, reviewer, status and next action to each row. Do not publish private seller or client documents; keep the register in your own deal file.']),
 ('Reconcile a claim instead of accepting a screenshot',[
 'Illustrative reconciliation: seller reports $120,000 bookings; the same-period export contains $8,000 cancellations and $12,000 cleaning charges. Booking revenue after cancellations is $112,000, of which $100,000 is accommodation revenue. If cleaning is modeled separately, using $120,000 as accommodation revenue overstates that category by $20,000.',
 'All figures are invented. Real exports may use different definitions, include taxes or refunds, and record bookings and payouts in different periods. Document the mapping before applying this calculation. The purpose is to make definitions explicit, not assume every platform reports identically.']),
 ('Separate evidence quality from investment approval',[
 'A complete historical record can support an unattractive deal; an attractive forecast can rest on weak evidence. Keep these questions separate. Ask whether the record verifies the claim, then whether the purchase still meets your cash, risk and operating criteria.',
 'For a forecast, write the assumption and sensitivity. If annual accommodation revenue falls from an illustrative $100,000 to $80,000 and variable costs equal 20% of that revenue, cash contribution falls by $16,000 before changes in fixed costs. Use your actual fee bases and expense structure, not this simplified percentage.']),
 ('Close out the register at each milestone',[
 'Before an offer, identify assumptions that need verification. Before the relevant contractual deadlines, have your retained advisers explain unresolved risks and options. Before launch, replace estimates with final invoices, access checks and approved operating agreements where available.',
 'Preserve an unresolved item with a decision, owner and follow-up date. Do not change provisional to verified simply because the transaction closed. Use the <a href="/airbnb-investment-property/">property evaluation guide</a>, <a href="/underwriting/">underwriting library</a> and <a href="/guides/str-service-responsibility-matrix/">responsibility matrix</a> to connect evidence to the purchase workflow.'])])]
for path,title,description,h1,lead,sections in PAGES:
 trail=[('Home','/'),('Guides','/guides/'),(h1,path)] if path.startswith('/guides/') else [('Home','/'),(h1,path)]
 body='<section class="hero hero-page"><div class="wrap">'+tpl.breadcrumb_html(trail)+'<span class="eyebrow">Purchase planning</span><h1>'+h1+'</h1></div></section>'
 body+='<section><div class="wrap wrap-narrow"><article class="article"><p class="lead">'+lead+'</p><p>Published October 1, 2026 · BNB Accelerator editorial team</p>'+sections_html(sections)+'</article></div></section>'
 body+=tpl.cta_band('Discuss your short-term rental purchase','Bring your budget, timeline and open questions to a purchase planning call.')
 schema=tpl.graph(tpl.ORG_SCHEMA,tpl.breadcrumb_schema(trail))+tpl.article_schema(h1,description,tpl.SITE+path,DATE)
 p=ROOT/path.strip('/')/'index.html';p.parent.mkdir(parents=True,exist_ok=True)
 p.write_text(tpl.page(title=title,description=description,path=path,body=body,extra_schema=schema),encoding='utf-8')
links='<h2>Connect the proposal to the purchase evidence</h2><p>Review the <a href="/short-term-rental-investment-service/">short-term rental investment service</a>, assign outputs with the <a href="/guides/str-service-responsibility-matrix/">service responsibility matrix</a>, and verify assumptions with the <a href="/guides/str-deal-evidence-register/">STR deal evidence register</a>.</p>'
block='<!-- purchase-evidence:start --><section><div class="wrap wrap-narrow">'+links+'</div></section><!-- purchase-evidence:end -->'
for file in ['guides/index.html','done-for-you-airbnb/index.html','airbnb-investment-company/index.html','airbnb-investment-property/index.html','pricing/index.html','underwriting/index.html','short-term-rental-investment/index.html']:
 p=ROOT/file;s=p.read_text();s=re.sub(r'<!-- purchase-evidence:start -->.*?<!-- purchase-evidence:end -->','',s,flags=re.S);s=s.replace('</main>',block+'\n</main>',1);p.write_text(s)
print('Generated three buyer resources and linked seven relevant hubs.')
