#!/usr/bin/env python3
"""Buyer decision worksheets. Authored September 26, 2026; no invented results."""
import json
from pathlib import Path
import tpl
from pillars import sections_html, write

DATE = '2026-09-26'
BASE = '/buy-a-short-term-rental/'
ORG = json.dumps({'@context':'https://schema.org','@type':'Organization','@id':tpl.SITE+'/#organization','name':'BNB Accelerator','legalName':'My BnB Accelerator, LLC','url':tpl.SITE+'/'})
PAGES = [
{
'slug':'investment-readiness', 'title':'Are You Ready to Buy a Short-Term Rental?',
'desc':'Use a practical STR buyer readiness worksheet to separate available cash, borrowing capacity, operating responsibilities and the conditions for starting a search.',
'lead':'Being able to make a down payment is only one part of being ready to buy a short-term rental. You also need enough liquidity to open the property, a financing path that fits its intended use, and a workable plan for operating it. This worksheet helps you decide whether to start searching, change the purchase budget, or resolve a missing piece first. It is a planning framework, not a lender approval or a recommendation to invest.',
'sections':[
('Define the job the property must do',[
'Write one primary objective before selecting a market: current cash flow, a property you can also use personally, long-term ownership, or a combination with explicit priorities. Personal stays during peak weeks can compete with the revenue goal. A home that suits your family may be a poor match for the operating plan. Record intended owner-use nights alongside the cash-flow target so the model does not silently assume year-round guest availability.',
'Choose a maximum amount of cash you are willing to expose to this purchase. Keep household emergency money and other committed funds outside that amount. Treat a possible future refinance, bonus or tax benefit as unavailable until it is actually supportable. The property should have a viable purchase and operating plan without a speculative funding event.']),
('Complete the readiness worksheet', [('table',['Question','Evidence to collect','If unresolved'],[
['What cash is genuinely available?','Current liquid balances less other commitments','Reduce the search budget'],
['Can the intended property be financed?','Lender discussion covering use, borrower and property type','Resolve eligibility before bidding'],
['Who handles guest operations?','Named manager or documented self-management plan','Price and staff the work'],
['Can you fund a delayed launch?','Monthly carrying-cost and reserve schedule','Add liquidity or reduce scope'],
['Who can stop the transaction?','Decision-maker and written purchase criteria','Agree on approval rules first']])]),
('Test the operating responsibility',[
'List the tasks that still belong to you if you hire a manager: approving repairs, reviewing statements, funding shortfalls, renewing insurance and deciding on capital replacements. Ask the prospective manager which expenses require advance approval and how emergency spending works. Delegation changes who performs the task; it does not eliminate the owner’s cost or responsibility.',
'For a hypothetical buyer with $180,000 available, a $150,000 closing and launch budget leaves $30,000. That remaining amount is not automatically an adequate reserve. Compare it with this property’s debt payments, fixed expenses, seasonal shortfalls, deductibles and repair exposure. If the same $30,000 is already needed for household commitments, the acquisition budget is overstated. These are illustrative planning amounts, not recommended reserve levels.']),
('Make a start, pause or resize decision',[
'Start a targeted search when the capital boundary, financing path and operating owner are clear. Pause when the deal relies on money you cannot access or on a manager you have not priced. Resize when the property type requires more setup or reserves than your budget supports. A smaller purchase price does not necessarily mean lower operating complexity, so revise the whole plan rather than only the down payment.'])],
'links':[('/blog/short-term-rental-buy-box/','Define your property buy box'),('/underwriting/cash-needed-to-buy/','Calculate cash needed to buy'),('/management/','Understand the management plan')]
},
{
'slug':'acquisition-budget-worksheet','title':'Short-Term Rental Acquisition Budget Worksheet',
'desc':'Build an STR purchase budget that tracks deposits, closing cash, setup, carrying costs and reserves without double-counting earnest money or expenses.',
'lead':'An acquisition budget should answer two different questions: how much cash the project needs in total, and when that cash leaves your account. Keep a project-cost ledger and a payment schedule. This prevents an earnest-money deposit from being counted twice and prevents a lender’s cash-to-close figure from being mistaken for the entire cost of launching a vacation rental.',
'sections':[
('Separate uses of cash from dates paid',[
'Begin with the down payment and transaction costs, then add repairs, furnishings, setup, initial supplies and any advisory fee actually payable under your agreement. Keep the operating reserve as a separate allocation. It is cash committed to the project, but it is not automatically an expense on day one. Ask your accountant how acquisition, loan and setup costs should be recorded; this worksheet is a liquidity plan rather than a tax classification.',
'Assign each line an amount, source, payment date and status. Mark estimates differently from signed quotes. Earnest money that is credited at settlement reduces the remaining amount due there. Do not add it to a closing figure that already includes the same contribution. Likewise, check whether insurance prepayments and tax escrows are already in the lender’s estimate.']),
('Use a dated cash ledger', [('table',['Cash use','Evidence','Timing question'],[
['Deposit','Executed contract and escrow receipt','When does it become due?'],
['Remaining closing cash','Settlement estimate with deposit credit','When must funds be available?'],
['Repairs and installation','Written scope and payment milestones','What is due before completion?'],
['Furniture and supplies','Itemized order, freight and assembly','When do deposits and balances clear?'],
['Carry before opening','Loan, utilities, insurance and other fixed costs','How many no-revenue months?'],
['Operating reserve','Monthly downside cash schedule','What remains after the last setup payment?']])]),
('Walk through the arithmetic',[
'Illustrative example: $125,000 down payment, $15,000 transaction costs, $30,000 furnishings, $10,000 repairs, $5,000 pre-opening carrying costs and $25,000 reserve require $210,000 of project cash. A $10,000 earnest-money payment credited toward the down payment leaves $200,000 still to fund; it does not raise the total to $220,000. These numbers do not represent a typical project, quote or promised result.',
'Now test timing. If furniture requires a large deposit before closing, that cash may leave while your purchase is still conditional. Ask whether the order can be canceled and who carries storage or failed-closing risk. Do not assume a seller credit can fund every post-closing purchase. Confirm permitted uses with the lender and settlement team before incorporating it.']),
('Reconcile the budget at each decision point',[
'Update the ledger after inspection, final lender terms and vendor selection. Keep the earlier version so you can see exactly why total cash changed. If the reserve is being consumed to keep the purchase price unchanged, explicitly revisit the offer or scope. Review the CFPB’s <a href="https://www.consumerfinance.gov/owning-a-home/loan-estimate/">Loan Estimate explainer</a> for consumer mortgage line items; business-purpose financing may use different disclosures, so request an itemized statement from that lender.'])],
'links':[('/underwriting/cash-needed-to-buy/','Review acquisition cash categories'),('/pricing/','Review BNB Accelerator pricing'),('/financing/','Explore financing considerations')]
},
{
'slug':'listing-screening-scorecard','title':'Short-Term Rental Listing Screening Scorecard',
'desc':'Screen vacation rental listings with evidence gates for intended use, all-in cost, guest fit and operating feasibility before spending money on full diligence.',
'lead':'A listing scorecard should help you reject unsuitable properties quickly and identify what still needs proof. Use hard gates before a weighted score. A beautiful home with an unresolved rental restriction should not beat a feasible property because its photos earn more points. The result of this first screen is a shortlist for investigation, not permission to waive inspections or offer protections.',
'sections':[
('Write the gates before browsing listings',[
'Use the same five gates for every listing: plausible permission for the intended rental use, plausible financing and insurance, an all-in cash range you can fund, a guest proposition supported by comparable properties, and an operating plan you can execute. At this stage some answers will be unknown. Label them as unknown rather than awarding a passing score based on the seller’s wording.',
'Distinguish a fixable feature from a property constraint. Paint and furniture may be priced and replaced. Road access, bedroom legality, a restrictive association or a weak location may require a different decision entirely. A low asking price does not compensate for a use that cannot be approved. Delegate property-specific legal determinations to the appropriate local professionals.']),
('Record one row per listing', [('table',['Field','What to record','Why it changes the screen'],[
['Address and jurisdiction','Exact parcel and governing authorities','Nearby properties may follow different rules'],
['All-in cash range','Purchase contribution, setup and reserve','Asking price misses launch costs'],
['Evidence of guest fit','Comparable size, location and amenities','Broad market averages can mislead'],
['Known constraints','HOA, access, capacity, condition','Some limits cannot be solved with decor'],
['Next unanswered question','Specific document or quote required','Keeps diligence focused'],
['Status','Reject, investigate or ready for deeper analysis','Stops unknowns becoming assumed approvals']])]),
('Use a small number of comparable candidates',[
'Compare a manageable shortlist using consistent definitions. For example, one listing may advertise six bedrooms while another offers four legally documented bedrooms and two bonus rooms. Do not compare projected revenue until you establish the actual guest capacity and permissible use for each. Record where every important fact came from and when it was checked.',
'When an agent says a property is already an Airbnb, ask what that proves: an active listing, historical revenue, current owner authorization, or the right for a new owner to operate. These are separate questions. The listing can enter the investigation stage while the answer remains open, but it should not become an unconditional purchase recommendation.']),
('Turn the screen into the next action',[
'Reject clear mismatches and preserve the reason so the same property does not re-enter the search under a different sales pitch. Investigate listings with a specific resolvable question. Move to detailed underwriting only when the basic gates are credible. If every listing fails, adjust a deliberate part of the buy box, such as market or property size, rather than quietly lowering every standard after several weeks of searching.'])],
'links':[('/blog/how-to-find-str-properties-for-sale/','Find properties for sale'),('/blog/compare-two-str-properties-before-offer/','Compare two purchase candidates'),('/markets/','Research markets')]
},
{
'slug':'property-tour-checklist','title':'STR Property Tour Checklist for Buyers',
'desc':'Run a buyer property tour around guest arrival, room usability, turnovers, utilities and expensive unknowns, with a clear handoff to professional inspectors.',
'lead':'An STR property tour should test how the home will function from guest arrival through cleaning and the next check-in. This checklist helps you collect useful observations and questions. It does not replace a professional inspection, specialist review or confirmation of legal rental capacity. Use it to make the inspection scope and launch budget more accurate.',
'sections':[
('Walk the actual guest journey',[
'Approach the property as a first-time visitor. Can a driver identify the entrance, turn around and park without relying on a neighbor’s land? Walk from parking to the entry with luggage in mind. Note steps, lighting, weather exposure and unclear access. Visit different times when practical, because a quiet midday tour may not reveal evening noise or difficult nighttime arrival.',
'Then walk every sleeping area, bathroom and shared space in the order a guest would use them. Record measured room dimensions, door locations and storage, but do not certify occupancy or code compliance yourself. Ask the relevant inspector or authority to confirm legal sleeping areas, emergency escape provisions and applicable safety requirements. Marketing labels are not a substitute for that verification.']),
('Use a room-by-room observation sheet', [('table',['Area','Observation to record','Follow-up owner'],[
['Arrival and parking','Access, slopes, lighting, vehicle fit','Agent and local access professional'],
['Sleeping areas','Dimensions, windows, doors, documented use','Qualified inspector or local authority'],
['Kitchen and dining','Usable capacity, appliances, wear','Designer and maintenance provider'],
['Laundry and storage','Linen flow, drying time, locked supplies','Cleaner or manager'],
['Outdoor amenities','Condition, boundaries, service access','Appropriate specialist'],
['Connectivity and systems','Service availability and visible equipment','Provider and inspector']])]),
('Tour with the operating team in mind',[
'Ask the cleaner where dirty linens, replacement supplies and trash will go. A photogenic layout can still require expensive turnovers if laundry capacity is inadequate or the supply closet is inaccessible. Ask the manager where maintenance vendors park and how they enter when the home is occupied. Put those observations into the launch plan before you price the property’s operating margin.',
'Test what can reasonably be demonstrated with the seller’s permission, and note what cannot. An internet speed result during one tour is a snapshot, not proof of reliability under full guest use. A running HVAC system does not establish remaining life. Capture model information and service records for the specialist instead of converting a brief demonstration into a long-term assumption.']),
('Leave with a scope, not just photographs',[
'Organize the tour into immediate purchase risks, launch work and optional improvements. Price required work first. Send the questions to the right inspector, contractor or manager while there is still time to act under the contract. If a key area was inaccessible, mark the review incomplete. Avoid filling the gap with a contingency allowance so small that the purchase only works if nothing is wrong.'])],
'links':[('/blog/str-due-diligence-checklist/','Use the full diligence checklist'),('/design/','Plan furnishings and setup'),('/blog/buy-str-sight-unseen/','Evaluate an out-of-state purchase')]
},
{
'slug':'due-diligence-document-tracker','title':'STR Buyer Due Diligence Document Tracker',
'desc':'Organize STR purchase evidence by decision, owner and deadline so permit, lender, inspection and revenue questions are resolved before commitments harden.',
'lead':'The useful output of due diligence is a supported purchase decision. A folder full of documents is not enough if nobody knows which assumption each file verifies. Build a tracker that connects each open question to an evidence source, responsible person, deadline and decision. Keep this tracker separate from your legal contract, and have the transaction professionals confirm the actual notice requirements and dates.',
'sections':[
('Track questions rather than vague tasks',[
'Replace “check permit” with “obtain written confirmation of the new owner’s approval path for this parcel and intended use.” Replace “review financials” with “reconcile the seller’s stated room revenue to booking-level records for the stated period.” A specific question tells the assigned person what completion means and makes unsupported conclusions easier to spot.',
'Every entry needs an evidence location and a reviewer. Receiving a document is one status; accepting it as sufficient is another. A permit issued to the seller may arrive promptly without answering whether you can operate after closing. A vendor quote may omit installation. Keep the item open until the reviewer has addressed the actual purchase assumption.']),
('Copy these tracker columns', [('table',['Column','Example entry','Purpose'],[
['Decision affected','May buyer open for nightly stays?','Names the actual risk'],
['Evidence needed','Written parcel-specific approval path','Defines a usable answer'],
['Requested from','Local office through transaction team','Identifies the source'],
['Accountable reviewer','Buyer’s designated professional','Prevents unreviewed uploads'],
['Deadline','Date and time confirmed from contract','Protects the decision window'],
['Status and consequence','Open; do not approve waiver yet','Connects delay to an action']])]),
('Separate missing, conflicting and stale evidence',[
'Missing evidence calls for a request. Conflicting evidence calls for reconciliation. Stale evidence calls for an update. These are different tasks. If a listing description conflicts with an association document, ask the appropriate professional to resolve the conflict instead of choosing the version that supports the deal. If an insurance quote predates a change in guest capacity, send the updated facts back to the insurer.',
'Use a short daily review as the decision deadline approaches: what changed, what is still open, who owns it, and what must happen before the next commitment? Avoid a status column filled with “in progress” without dates. Request extensions or amended terms through the authorized transaction team where appropriate; an internal spreadsheet does not extend a contractual deadline.']),
('Close the tracker with a decision record',[
'Before proceeding, record which items were verified, which were accepted as risks, and who approved those exceptions. Keep copies of the actual evidence alongside the summary. A risk should not disappear because the document request was marked complete. If the decisive information cannot be obtained within an adequately protected period, the choice may be to renegotiate, pause or exit under the available contractual rights.'])],
'links':[('/blog/str-due-diligence-checklist/','Review what needs investigating'),('/underwriting/permit-transfer/','Check the new-owner permit path'),('/underwriting/seller-financials/','Review seller financial evidence')]
},
{
'slug':'investment-memo-template','title':'Short-Term Rental Investment Memo Template',
'desc':'Write an STR purchase decision memo with sources, total cash, base and downside cash flow, unresolved conditions and an explicit maximum offer.',
'lead':'A short-term rental investment memo is the decision document you would want to read if you had not attended any of the sales calls. It should explain why the property fits, where the numbers came from, what could invalidate them, and what price and conditions you are willing to accept. Keep evidence, assumptions and conclusions visibly separate.',
'sections':[
('Start with the decision you are requesting',[
'Use a direct opening: approve an offer up to a stated price subject to specified conditions, request additional evidence, or decline the purchase. Include the exact property, intended use and buyer’s objective. Avoid beginning with a long market narrative while hiding the cash requirement and open risks at the end.',
'For every major number, show its source and date. Distinguish seller history from comparable-property observations and from your own modeled performance. Historical results under a different host, manager or availability pattern do not automatically become your forecast. Record which operating changes you assume and what they cost.']),
('Use a consistent memo structure', [('table',['Memo section','Required content'],[
['Decision','Price ceiling, conditions and approval requested'],
['Property fit','Address, guest use, legal-use status and buy-box fit'],
['Capital','Cash through launch and separately identified reserve'],
['Operating case','Revenue basis, expenses and financing assumptions'],
['Downside','Lower revenue, delayed opening and major cost exposures'],
['Open gates','Evidence still needed, reviewer and deadline'],
['Recommendation','Proceed, renegotiate, investigate or reject']])]),
('Show the arithmetic and its limits',[
'Illustrative only: assume $100,000 annual revenue, $45,000 operating costs, $35,000 debt service and $5,000 planned replacement-reserve contribution. The modeled owner cash remaining is $15,000. With $180,000 total initial cash committed, that is an 8.3% simple cash-on-cash measure under this definition. Label whether the denominator includes reserves and whether cash flow includes reserve contributions so another reviewer can reproduce the calculation.',
'If revenue falls to $80,000, costs do not necessarily fall by $20,000. Recalculate variable expenses while retaining fixed obligations. If operating costs become $41,000 with unchanged debt service and reserve contribution, modeled cash remaining becomes negative $1,000. This is an arithmetic example, not a forecast or an acceptable-return recommendation. Financing approval alone does not validate the owner’s investment case.']),
('Identify what would reverse your conclusion',[
'Finish with the facts that would make you change your mind: a lower supported revenue range, an unavailable permit, a materially higher insurance quote, or repair work that consumes the reserve. An approval that cannot be reversed by new evidence is not a useful decision framework. Keep the original memo and issue a revised version when terms change so enthusiasm does not quietly replace the original investment criteria.'])],
'links':[('/blog/str-maximum-offer-price-from-revenue/','Work backward to an offer ceiling'),('/underwriting/downside-scenario/','Build the downside case'),('/case-studies/','Review specific client examples')]
},
{
'slug':'furnished-property-inventory','title':'Furnished STR Purchase Inventory Checklist',
'desc':'Verify what conveys with a furnished vacation rental using room-level inventory, condition evidence, replacement costs and closing confirmation.',
'lead':'“Fully furnished” is not an inventory. When buying an operating vacation rental, document which items are included, their condition, whether the seller owns them and what still needs replacement. The practical goal is a room-by-room record your transaction team can incorporate into the appropriate documents and your launch team can verify before guests arrive.',
'sections':[
('Separate property, equipment and accounts',[
'Ask your agent and attorney which fixtures, personal property and exclusions need to be described in the purchase documents. Do not assume a photographed item conveys. Furniture may belong to a staging company, equipment may be leased, and the seller may intend to remove personal pieces. Confirm ownership and any continuing payment obligations instead of assigning value from listing photos.',
'Keep software subscriptions, locks, websites and booking accounts on a separate schedule. A physical device and the account controlling it are different assets. The sale of a furnished home does not itself establish transfer rights for platform accounts, listing reviews or photography. For example, <a href="https://www.airbnb.com/help/article/1431">Airbnb states that account ownership cannot be transferred to another host</a>. Plan the platform transition separately.']),
('Create a room-level inventory', [('table',['Field','What to capture'],[
['Location','Bedroom 1, living room, garage or owner closet'],
['Item and quantity','Specific description, count and identifying detail'],
['Condition','Observed defects, wear and working status'],
['Ownership','Owned, rented, financed or excluded'],
['Evidence','Dated photo and relevant receipt or warranty'],
['Action','Conveys, replace, repair or clarify before closing']])]),
('Price usable condition rather than replacement fantasy',[
'A room can contain the listed number of beds while still needing mattresses, protectors, linens, lamps and storage to operate well. Count backup sets and consumables separately from the core furniture. Ask the cleaner and manager what must be replaced before the first stay. A seller’s original purchase price is not necessarily current market value or the amount you would spend to obtain a usable substitute.',
'For a hypothetical purchase, $20,000 of included furnishings might still require $7,000 of replacement and setup to match the intended guest offering. That $7,000 belongs in your launch budget even if the property is advertised as turnkey. Do not count the same items as both included inventory and new furnishing purchases. Obtain actual quotes for the important gaps.']),
('Verify the inventory again before closing',[
'Compare the final walkthrough with the agreed inventory, photographs and repair list. Record missing or substituted items and ask the transaction team to resolve them under the contract. Do not rely on a promise to drop off replacements after possession. Keep a copy for the manager’s opening inventory, then reset access credentials and document the equipment handoff before accepting guests.'])],
'links':[('/blog/buying-an-operating-str/','Evaluate an operating rental'),('/design/','Plan furnishing and design'),('/blog/seller-airbnb-photos-purchase-rights/','Verify listing photo rights')]
},
{
'slug':'vendor-quote-comparison','title':'Compare STR Launch Quotes Before You Buy',
'desc':'Compare furnishing, repair and setup proposals on a common scope, including freight, installation, exclusions, milestones and delayed-launch costs.',
'lead':'Two furnishing or renovation proposals are only comparable when they deliver the same usable result. A low merchandise total can hide freight, assembly, disposal, storage and project-management charges. Before using a vendor quote in your acquisition model, normalize the scope and identify what happens if the closing or installation date changes.',
'sections':[
('Define the finished condition',[
'Write what “guest-ready” means for this property: furniture installed, waste removed, beds dressed, supplies stocked, systems tested and photographs completed where included. Use room counts and quantities rather than a broad package label. Ask each bidder to identify exclusions explicitly. A scope that stops at curbside delivery should not be compared directly with one that includes installation and final cleaning.',
'For repairs, separate investigation from the approved work. A contractor may quote a visible repair without pricing concealed damage or permit requirements. Record allowances as allowances, not fixed commitments. Have the appropriate professional determine what inspections, permits or engineering are needed for the actual project.']),
('Normalize the quote comparison', [('table',['Comparison item','Question for every bidder'],[
['Scope','Exactly what items and work are included?'],
['Logistics','Who pays freight, storage, stairs or remote access charges?'],
['Installation','Who assembles, tests and removes packaging?'],
['Schedule','What starts the clock and what dependencies remain?'],
['Payment','What is due at order, delivery and acceptance?'],
['Changes','How are substitutions and extra work approved?'],
['Completion','What evidence confirms the job is finished?']])]),
('Compare cash and timing together',[
'Illustrative example: Proposal A lists $28,000 for furniture, then $4,000 shipping, $3,000 assembly and $1,000 disposal. Its comparable total is $36,000 before any other exclusions. Proposal B’s $34,000 installed total may be less expensive if it truly covers the same specification. This example compares scope, not vendor quality or prevailing prices.',
'A lower total can still be unattractive if it misses the target opening date. Model extra carrying costs and the possibility of a slower launch without assuming every delayed night would have sold. Confirm product availability, delivery access, substitution rights and who signs off on completion. Do not pay a premium for a schedule that the proposal does not actually commit to.']),
('Use the accepted scope in the purchase decision',[
'Attach the chosen quote and exclusions to your launch budget. Keep contingency cash for genuine unknowns, but do not use a blanket percentage to conceal known missing work. If the complete scope breaks your capital limit, reduce optional improvements, renegotiate the purchase or reconsider the deal. The right time to discover an unfunded launch is before the purchase becomes difficult to unwind.'])],
'links':[('/design/','Review the design process'),('/blog/furnishing-budget-by-bedroom-count/','Evaluate furnishing scope'),('/blog/str-purchase-to-launch-timeline/','Map the purchase-to-launch timeline')]
},
{
'slug':'final-walkthrough-checklist','title':'Final Walkthrough Checklist for an STR Purchase',
'desc':'Check a vacation rental before closing against the agreed condition, repair evidence, inventory, possession terms and operating handoff.',
'lead':'The final walkthrough is your opportunity to compare the property’s current condition with what the purchase documents require. For a vacation rental, also check the included inventory and possession plan. It is not a replacement for inspections and does not create rights outside your contract. Schedule it with your agent and leave enough time to escalate discrepancies before closing.',
'sections':[
('Bring the agreed baseline',[
'Use the executed inventory, inspection-related agreements, repair receipts and dated photographs. A memory of the first tour is not a reliable checklist. If the seller agreed to a specific repair, ask whether its completion needs professional verification rather than just a receipt. Confirm access to every area that matters, including owner storage and outbuildings included in the purchase.',
'Check for changes since the inspection: leaks, damage, removed equipment, substituted furniture or a loss of utility service. Arrange reasonable demonstrations with permission and document what could not be checked. Avoid calling a system satisfactory merely because it was inaccessible. If utilities must remain active for the walkthrough, coordinate that requirement through the transaction team.']),
('Check the STR-specific items', [('table',['Check','Evidence or confirmation'],[
['Condition and agreed repairs','Photographs, receipts and specialist confirmation as appropriate'],
['Included furnishings','Inventory counts and agreed item descriptions'],
['Possession','Occupants, seller access and agreed vacancy timing'],
['Keys and devices','Physical keys, remotes, locks and equipment list'],
['Guest calendar','Written plan for any remaining reservations'],
['Utilities and services','Cutover dates and active owner accounts'],
['Unresolved discrepancy','Written notice to the responsible transaction professional']])]),
('Keep the financial and physical checks separate',[
'Confirm final purchase amounts with the settlement team; do not infer that a correct walkthrough means the settlement statement is also correct. For applicable consumer mortgages, the CFPB’s <a href="https://www.consumerfinance.gov/owning-a-home/closing-disclosure/">Closing Disclosure explainer</a> provides a line-by-line reference. Investment and business-purpose financing may involve different documents. Ask your lender which disclosures and figures control your transaction.',
'An unresolved missing item or failed repair should go to the agent and attorney for a contractual solution. A credit, delay or other arrangement needs appropriate documentation and any necessary lender approval. Do not assume you can simply hold back part of the closing funds on your own. Record the agreed resolution and who will confirm completion.']),
('Finish with a possession and launch handoff',[
'After the authorized closing and possession process, update access, establish your own operational accounts and hand the manager the verified inventory. Separate “the purchase closed” from “the property is ready to host.” Local approvals, insurance, cleaning, listing setup and staffing may still be open. Keep those gates visible before accepting a guest arrival date.'])],
'links':[('/blog/future-reservations-at-closing/','Review future reservations'),('/blog/airbnb-house-right-after-closing/','Understand the post-closing opening steps'),('/blog/str-purchase-to-launch-timeline/','Plan the full timeline')]
},
{
'slug':'launch-handoff-checklist','title':'STR Acquisition-to-Launch Handoff Checklist',
'desc':'Move from closing to a guest-ready rental with assigned owners for approvals, insurance, access, inventory, listings, cleaning and the first guest arrival.',
'lead':'A successful closing transfers a property. A successful launch requires a separate operational handoff. Give every remaining item a named owner, evidence of completion and an opening condition. The acquisition team, manager, cleaner and owner should all know which tasks are finished and which still prevent the first guest stay.',
'sections':[
('Set opening gates before setting the first arrival',[
'Confirm the required new-owner approvals and coverage for the actual operation with the relevant professionals. Then verify utilities, access, furnishings, safety work, cleaning and support coverage. These are dependencies, not a list of optional improvements. A photographer’s availability or a desirable weekend should not determine the opening date while an essential approval remains unresolved.',
'Keep the booking transition separate from the property transfer. <a href="https://www.airbnb.com/help/article/1431">Airbnb does not support transferring account ownership between hosts</a>. Have the platform and transaction team help establish a compliant plan for listings and reservations. Do not assume you own an account, reviews or guest data because you bought the home.']),
('Assign the handoff by deliverable', [('table',['Deliverable','Completion evidence','Typical responsible role'],[
['Approval and coverage','Confirmed operating permissions and effective insurance','Owner with qualified advisers'],
['Physical readiness','Closed punch list and tested equipment','Contractor or setup lead'],
['Access','Documented keys, codes and emergency entry plan','Owner and manager'],
['Inventory','Room list, spares and locked supplies','Setup lead and cleaner'],
['Guest operations','Cleaning schedule and escalation contacts','Manager'],
['Listing readiness','Accurate details, authorized photos and configured availability','Listing operator'],
['Opening approval','Written confirmation that all essential gates are met','Owner']])]),
('Run a rehearsal before the first guest',[
'Walk through the arrival instructions using the same entrance and code the guest will use. Confirm Wi-Fi details, appliance instructions, trash handling and emergency contacts. Ask the cleaner to complete a full turnover sequence and flag supply shortages. Check that the listing’s promised amenities are present and working, and remove claims that cannot be supported.',
'If the rehearsal finds a problem, assign a specific repair and recheck it. A property with a working front door but no reliable after-hours response still has an operating gap. Keep an owner-accessible record of vendors, shutoffs, warranties and equipment details. Avoid placing sensitive access codes or guest information in publicly shared documents.']),
('Measure the first month against the acquisition model',[
'Compare actual opening costs, available nights, earned revenue and operating expenses with the assumptions used to buy the property. Separate a partial launch month from a stabilized annual forecast. Do not annualize a strong holiday week or treat booked future stays as cash already earned. Use the first month to correct pricing, supplies and processes, while preserving the original model for an honest comparison.'])],
'links':[('/blog/the-first-30-days-checklist/','Plan the first 30 days'),('/management/','Review management responsibilities'),('/blog/vrbo-listing-handoff-buying-str/','Review the Vrbo handoff')]
}
]

def render(title, desc, path, lead, sections, related, hub=False):
    trail = [('Home','/'),('Buy a Short-Term Rental',BASE)]
    if not hub: trail.append((title,path))
    links = ''.join(f'<li><a href="{u}">{t}</a></li>' for u,t in related)
    body = f'''<section class="hero hero-page"><div class="wrap">{tpl.breadcrumb_html(trail)}<div class="hero-inner"><span class="eyebrow">STR buyer workbook</span><h1>{title}</h1><div class="article-meta">Published September 26, 2026</div></div></div></section>
<section><div class="wrap"><article class="article"><p class="lead">{lead}</p>
<div class="callout"><p>Have a property or purchase budget in mind? <a href="/apply/">Book a call</a> to discuss your acquisition plan.</p></div>
{sections_html(sections)}
<h2>Continue your purchase research</h2><ul>{links}</ul>
<p>Prepared by BNB Accelerator. These worksheets support a purchase discussion and do not replace property-specific legal, lending, insurance, tax or inspection advice. Examples are hypothetical and do not promise investment results.</p>
</article></div></section>
{tpl.cta_band('Build a clearer plan before you buy','Discuss your budget, target property, open questions and next acquisition steps.',('/apply/','Book a Call'),(BASE,'Explore the Buyer Workbook'))}'''
    schema = tpl.graph(tpl.breadcrumb_schema(trail)) + '\n<script type="application/ld+json">'+ORG+'</script>\n'+tpl.article_schema(title,desc,tpl.SITE+path,DATE,section='Short-Term Rental Buying')
    return tpl.page(title=title+' | BNB Accelerator',description=desc,path=path,body=body,extra_schema=schema,active='/blog/')

def main():
    for p in PAGES:
        write(BASE+p['slug']+'/',render(p['title'],p['desc'],BASE+p['slug']+'/',p['lead'],p['sections'],[(BASE,'Return to the buyer workbook')]+p['links']))
    sections = [
    ('How to buy a short-term rental: the decision sequence',[
    'Start with what you can fund and operate, narrow the search to suitable properties, verify the assumptions, negotiate with a clear ceiling, and prepare the operating handoff before closing. Buying an Airbnb, vacation rental or other short-term rental requires both a real-estate purchase decision and a business operating plan. A listing’s projected revenue is only one input.',
    ('table',['Stage','Decision to make','What should be in hand'],[
    ['Prepare','Can this purchase fit your capital and responsibilities?','Readiness assessment and all-in cash budget'],
    ['Search','Which properties deserve investigation?','Buy box, market shortlist and listing screen'],
    ['Verify','Are the important claims supportable?','Property records, financial evidence and quotes'],
    ['Offer','At what price and under what conditions?','Investment memo and reviewed contract terms'],
    ['Close','Does the delivered property match the agreement?','Final documents, inventory and walkthrough'],
    ['Launch','Is the new operation ready for guests?','Completed approvals and operating handoff']])]),
    ('1. Set the budget before the search',[
    'Start with cash available after other commitments, not the largest loan amount a lender might approve. Your project budget includes the purchase contribution, transaction costs, setup, repairs, carrying costs and a reserve. Ask the lender about the intended investment use and property type early. A financing path that works for one property may not work for another.',
    f'<a href="{BASE}investment-readiness/">Complete the readiness worksheet</a>, then build your <a href="{BASE}acquisition-budget-worksheet/">acquisition cash ledger</a>. Use the <a href="/financing/">financing library</a> for deeper questions.']),
    ('2. Find and screen properties for sale',[
    'Match each listing to a written buy box. Compare the exact address, property type, guest capacity, operating demands and all-in cash range. Avoid deciding from a city ranking alone. Within the same market, association rules, jurisdiction, access, condition and guest appeal can change the purchase case.',
    f'Use the <a href="{BASE}listing-screening-scorecard/">listing scorecard</a> to move properties into reject, investigate or detailed-review categories. Explore <a href="/markets/">market guides</a> and the <a href="/compare/markets/">market comparison library</a>, then verify facts for the actual parcel.']),
    ('3. Validate revenue and the complete cost stack',[
    'Request evidence for the seller’s history and build your own operating case. Distinguish room charges from cleaning fees, taxes, refunds and platform deductions. Match comparable properties by meaningful guest characteristics and seasonality. Keep base and downside cases rather than a single optimistic annual figure.',
    'Subtract property-specific operating costs and debt service. Show replacement-reserve contributions separately and use a consistent definition when comparing returns. Include the cash needed during a delayed opening. Read the <a href="/underwriting/seller-financials/">seller financial review</a>, <a href="/underwriting/expense-ratio/">expense guide</a> and <a href="/underwriting/downside-scenario/">downside analysis</a>.']),
    ('4. Turn diligence into a purchase decision',[
    'Check intended legal use, insurability, financing, condition and operational feasibility while the transaction still provides an appropriate decision window. A seller’s permit, listing or past income does not by itself establish your right or ability to operate. Have qualified local professionals resolve the property-specific questions.',
    f'Bring the <a href="{BASE}property-tour-checklist/">property tour checklist</a>, maintain the <a href="{BASE}due-diligence-document-tracker/">evidence tracker</a> and summarize the result in an <a href="{BASE}investment-memo-template/">investment memo</a>. The memo should state your offer ceiling, open conditions and what would change your decision.']),
    ('5. Price setup and verify what you are buying',[
    'For a furnished property, agree on an itemized inventory and confirm what is owned, excluded or subject to another agreement. For an unfurnished property, normalize vendor quotes so delivery, installation and other missing work are included. “Turnkey” describes a claim you still need to test.',
    f'Use the <a href="{BASE}furnished-property-inventory/">furnished-property inventory</a> and <a href="{BASE}vendor-quote-comparison/">vendor quote comparison</a>. Review the <a href="{BASE}final-walkthrough-checklist/">final walkthrough checklist</a> with the transaction team before closing.']),
    ('6. Separate ownership from opening',[
    'The closing date and first guest arrival do not have to be the same day. Coordinate new-owner approvals, insurance, utilities, access, cleaning, listing setup and a compliant reservation transition. Confirm who makes the final opening decision and what evidence they require.',
    f'Use the <a href="{BASE}launch-handoff-checklist/">launch handoff checklist</a> and the <a href="/blog/str-purchase-to-launch-timeline/">purchase-to-launch timeline</a>. Preserve enough liquidity for delays instead of assuming immediate full occupancy.']),
    ('Choose the guide for the purchase in front of you',[
    ('ul',[
    '<a href="/blog/how-to-buy-first-airbnb/">Buying your first Airbnb</a>: understand the sequence and responsibilities.',
    '<a href="/blog/buying-airbnb-out-of-state/">Buying out of state</a>: organize local verification and operations.',
    '<a href="/blog/buy-existing-airbnb-vs-start-from-scratch/">Existing Airbnb or a new setup</a>: compare evidence and launch work.',
    '<a href="/blog/compare-two-str-properties-before-offer/">Comparing two candidate properties</a>: put the cash and downside on the same basis.',
    '<a href="/case-studies/">Reviewing client examples</a>: distinguish documented property outcomes from your own forecast.',
    '<a href="/how-it-works/">Working with BNB Accelerator</a>: review the acquisition process and <a href="/pricing/">pricing</a> before booking.'])]),
    ('Common buyer questions',[
    ('h3','How much cash do I need to buy a short-term rental?'),
    'The answer depends on purchase price, financing, condition, furnishing needs and the reserve required for that operation. Add every cash use through opening rather than using only a down-payment percentage. The acquisition-budget worksheet gives you a structure for obtaining property-specific numbers.',
    ('h3','Does a profitable seller history prove my purchase will work?'),
    'No. Your purchase price, financing, manager, insurance, availability and approval requirements may differ. Reconcile the seller’s evidence, then model your own terms and costs.',
    ('h3','Can BNB Accelerator help me buy a property?'),
    'Review our process, pricing and specific client examples, then book a call to discuss fit. Bring your available capital range, financing status, preferred property type and any listings you are considering. The conversation should identify the next decision and the evidence needed to make it.'])]
    write(BASE,render('Buy a Short-Term Rental: A Practical Buyer Workbook','Buying an Airbnb or vacation rental? Work through budget, listing selection, due diligence, offers, closing and launch with ten practical buyer worksheets.',BASE,'Make a better-informed short-term rental purchase with a clear sequence, property-specific evidence and a plan for the work after closing. This workbook brings the key decisions together and links to detailed research across the BNB Accelerator site. Start at your current stage, complete the relevant worksheet and bring your open questions to a call.',sections,[(BASE+p['slug']+'/',p['title']) for p in PAGES]+[('/airbnb-investment-property/','Evaluate an Airbnb investment property'),('/short-term-rental-investment/','Review STR investment risks and returns')],True))
    print('Generated 11 buyer workbook pages')

if __name__=='__main__': main()
