#!/usr/bin/env python3
"""Build 500 property-specific STR acquisition decision guides and their hub.

The library is deliberately about a buyer's decision, not city-keyword pages.
All numerical inputs on a live deal must come from that deal's documents.
"""

from __future__ import annotations

import html
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import tpl
from pillars import write

BASE = "/guides/str-investment/"
DATE = "2026-09-24"

# name, URL, buyer fit, revenue test, physical diligence, legal/insurance
# diligence, financing issue, operating burden, resale alternative
ASSETS = [
    ("beach house", "beach-house", "seasonal coastal demand and high maintenance exposure", "separate peak weeks from shoulder-season nights and storm-related closures", "roof, salt corrosion, drainage, HVAC and exterior fasteners", "flood and wind coverage, evacuation rules and parcel-level rental permission", "insurance cost and deductible can change the lender's debt-coverage case", "sand, humidity and rapid turnover wear", "year-round residential demand may be thinner than vacation demand"),
    ("lake house", "lake-house", "water access that guests can actually use", "price waterfront, lake-view and no-access comparables separately", "dock condition, shoreline, septic and seasonal water level", "dock rights, lake association rules and liability coverage", "dock or shoreline repairs may require extra cash outside the mortgage", "watercraft rules, dock inspections and storm cleanup", "value may depend on transferable access rights"),
    ("mountain cabin", "mountain-cabin", "drive-to leisure demand with weather-sensitive access", "test weekday occupancy and winter cancellations apart from holiday peaks", "slope drainage, roof load, foundation and access road", "private-road maintenance, wildfire exposure and local occupancy limits", "remote appraisal comparables can be sparse", "snow removal, hot tub service and remote dispatch", "a buyer may discount difficult year-round access"),
    ("ski chalet", "ski-chalet", "concentrated winter revenue and expensive peak-week mistakes", "model snow-dependent nights separately from summer use", "heating system, ice dams, insulation and parking", "resort-area rules, snow access and winter peril exclusions", "seasonality can weaken lender treatment of annual cash flow", "rapid winter turns, gear storage and emergency heat", "resale depends on both winter demand and non-ski utility"),
    ("desert vacation home", "desert-home", "warm-weather demand with heat and water constraints", "separate event demand from ordinary midweek bookings", "cooling capacity, pool equipment, roof and irrigation", "water restrictions, pool liability and local STR eligibility", "pool equipment and utility reserves increase cash needed", "pool care, cooling failures and summer vacancy", "year-round residential utility should be tested independently"),
    ("urban condo", "urban-condo", "walkable demand subject to building-level control", "compare legally permitted units in the same building or use class", "building systems, special assessments and sound isolation", "declaration, board rules, master policy and permit transferability", "project eligibility can block otherwise attractive conventional financing", "front-desk access, elevators and shared-space guest rules", "HOA policy can change the investor buyer pool"),
    ("suburban single-family home", "suburban-home", "family stays with a viable long-term-rental alternative", "compare family-size stays with nearby ordinary rentals", "bedroom legality, parking, yard and major systems", "neighborhood rules, nuisance limits and insurer occupancy terms", "appraisal may follow owner-occupant comparables rather than STR income", "yard care, trash and neighborhood response", "long-term rent is a measurable fallback"),
    ("rural farmhouse", "rural-farmhouse", "group stays where infrastructure sets the real capacity", "test travel time and event-driven demand without assuming constant groups", "well, septic, broadband, access and outbuildings", "event-use limits, fire access, farm liability and zoning", "nonstandard acreage and outbuildings may complicate appraisal", "long vendor travel times and onsite-system maintenance", "non-STR buyers may value acreage differently"),
    ("tiny home", "tiny-home", "lower entry price but limited usable capacity", "compare legal, insulated tiny-home inventory rather than full houses", "foundation, utility hookups, ventilation and storage", "dwelling classification, minimum size and permitted occupancy", "loan options may narrow if the unit is personal property", "small-space cleaning and rapid guest wear", "buyer financing and land rights drive liquidity"),
    ("duplex", "duplex", "two income streams with shared-building exposure", "underwrite each unit and the combined operating calendar separately", "separate meters, sound transfer, egress and common systems", "unit-level permit rules, tenant rights and insurance use", "lender may apply different treatment to occupied and short-term units", "shared trash, parking and guest-neighbor friction", "long-term leases can support an alternate exit"),
    ("triplex", "triplex", "small multifamily income with unit-mix decisions", "compare full-STR, mixed-lease and all-long-term cases", "unit separation, fire systems, meters and deferred common repairs", "license limits per parcel, tenant rights and building classification", "income underwriting depends on verified unit rents and legal use", "coordinating cleaners and residents in shared areas", "multifamily buyers will scrutinize normalized NOI"),
    ("fourplex", "fourplex", "four-unit cash flow and higher operational coordination", "build unit-level forecasts before aggregating revenue", "fire separation, roof, parking, meters and capital backlog", "parcel caps, lodging rules and resident access", "loan eligibility can turn on occupancy and property condition", "turnover density, noise and common-area care", "conventional multifamily demand offers a possible fallback"),
    ("townhouse", "townhouse", "lower exterior control and close neighbors", "compare similar attached homes rather than detached vacation houses", "shared walls, parking allocation and exterior responsibilities", "association documents, guest access and master-policy gaps", "association assessments affect qualifying cash flow", "noise monitoring, access rules and shared-space upkeep", "association restrictions affect investor resale"),
    ("luxury estate", "luxury-estate", "high nightly rates with concentrated capital at risk", "use truly comparable large-home bookings and test fewer reservations", "specialty systems, pool, grounds and replacement cost", "event restrictions, high-limit liability and staffing obligations", "jumbo or portfolio financing may need larger reserves", "concierge, grounds, pool and after-hours staffing", "the buyer pool can be narrower at a premium price"),
    ("historic home", "historic-home", "distinctive experience with preservation constraints", "isolate the premium attributable to the property rather than the town", "old wiring, plumbing, envelope and prior alterations", "historic review, accessibility obligations and insurance terms", "renovation draws may need more time and contingencies", "specialist repairs and guest expectations for old systems", "preservation rules constrain value-add plans"),
    ("waterfront cabin", "waterfront-cabin", "small-footprint water access and weather risk", "test actual water-use season and access quality", "shoreline erosion, dock, septic and moisture intrusion", "riparian rights, flood coverage and watercraft liability", "shoreline work may be excluded from standard renovation finance", "dock, pest and seasonal utility care", "transferable water rights matter more than a view label"),
    ("A-frame cabin", "a-frame-cabin", "design appeal with unusual usable floor area", "compare bookable sleeping capacity rather than advertised square footage", "roof intersections, insulation, loft egress and drainage", "loft sleeping approval, fire egress and specialty insurance", "appraisal may not credit design premiums at retail cost", "ladder safety, snow shedding and compact turnover", "resale depends on legal bedrooms and broad-market usability"),
    ("manufactured home", "manufactured-home", "lower purchase price with title and land questions", "compare homes with the same title, land and financing status", "tie-downs, foundation, age and utility connections", "land ownership, park rules, STR permission and insurer eligibility", "age and foundation can sharply limit loan programs", "parts availability and park-related access", "resale liquidity depends on financeable title and land"),
    ("mixed-use building", "mixed-use-building", "multiple revenue uses and complex shared systems", "separate lodging contribution from retail or office income", "fire separation, utilities, access and commercial systems", "zoning, occupancy classification and separate insurance", "commercial terms may change leverage and debt service", "distinct vendors and guest/business circulation", "exit buyers may price each use with a different cap rate"),
    ("new-construction vacation home", "new-construction-home", "modern systems with completion and launch timing risk", "forecast from operating comparables, not a seller's untested pro forma", "punch list, warranty, site drainage and utility commissioning", "certificate of occupancy, STR permit and insurance start date", "construction completion can change rate lock and cash-to-close", "new vendor setup and warranty response", "first-year actuals may lag a stabilized resale story"),
]

# slug, title phrase, question, method, documents, stress, decision boundary
DECISIONS = [
    ("investment-cost", "investment cost", "What is the real all-in cost?", "Add contract price, closing costs, inspections, repairs, furnishings, launch costs and opening reserves. Keep tax benefits out of cash-to-close.", "purchase contract, lender estimate, bids, furniture schedule and reserve policy", "Increase the largest unfinished bid and delay opening one month.", "Proceed only when the cash requirement remains fundable after that stress."),
    ("cash-on-cash-return", "cash-on-cash return", "What cash return survives a conservative case?", "Divide annual cash flow after debt service and recurring reserves by total cash invested, including furnishing and launch capital.", "revenue comps, operating quotes, debt terms and cash ledger", "Cut revenue and add an unplanned repair without changing the denominator.", "Reject a target return that exists only after excluding startup cash."),
    ("break-even-occupancy", "break-even occupancy", "How many booked nights cover the carrying cost?", "Divide fixed annual costs by contribution per booked night after platform fees, variable cleaning and consumables.", "nightly-rate evidence, fixed bills, cleaning quote and fee schedule", "Use a lower realized rate and more owner-blocked nights.", "Require break-even demand below a defensible downside booking case."),
    ("revenue-forecast", "revenue forecast", "Can a buyer defend the revenue assumption?", "Build a month-by-month forecast from permitted, comparable properties and adjust for size, access, amenities and calendar availability.", "comparable calendars, raw booking exports, permit record and launch calendar", "Remove the top demand month and model a slower first quarter.", "Do not price the deal from an unsupported annual gross number."),
    ("dscr-loan", "DSCR loan", "Would a DSCR loan fit this purchase?", "Ask the lender which rental income it accepts, what expenses it applies and whether the property type is eligible; mirror those terms in the buyer model.", "written term sheet, appraisal scope, insurance quote and lender income rules", "Recalculate at a lower qualifying rent and a higher rate.", "Treat lender eligibility and investor return as separate tests."),
    ("conventional-financing", "conventional financing", "Will conventional financing work for the intended use?", "Confirm occupancy, unit count, project eligibility, income documentation and reserve requirements with the lender before waiving contingencies.", "preapproval, property details, association documents and lender conditions", "Model a longer close and a second funding path.", "Keep a financing exit if property-specific approval is unresolved."),
    ("bridge-financing", "bridge financing", "Is short-term financing justified?", "Compare all fees, points, interest, extension rights and refinance risk with the value created by the plan.", "bridge quote, draw schedule, renovation budget and takeout lender criteria", "Delay stabilization and use the contractual extension rate.", "Do not rely on a refinance that requires perfect revenue or appraisal."),
    ("seller-financing", "seller financing", "Should the buyer request seller financing?", "Compare down payment, note rate, balloon, lien position and default terms with bank financing and the seller's ability to deliver clear title.", "draft note, title report, senior-loan consent and amortization schedule", "Model a missed refinance at the balloon date.", "Use counsel and proceed only when the exit from the note is credible."),
    ("renovation-budget", "renovation budget", "How much renovation can the deal carry?", "Price scope by trade, add contingency and downtime, then compare incremental contribution with added capital and execution risk.", "inspection report, contractor bids, permit timeline and before/after comps", "Raise the largest trade cost and delay opening by a month.", "Separate essential compliance work from optional design upgrades."),
    ("furnishing-budget", "furnishing budget", "What should furnishing cost before launch?", "Build a room-by-room inventory, delivery schedule, replacement reserve and installation labor budget; test it against guest capacity.", "room plan, vendor quotes, delivery dates and asset inventory", "Assume one delayed shipment and one replacement in the first year.", "Avoid using a generic per-bedroom allowance when the layout differs."),
    ("permit-diligence", "permit diligence", "Is legal short-term-rental use verifiable?", "Check the exact parcel and ownership structure with the local authority; record permit, cap, inspection, tax and renewal requirements.", "ordinance, parcel record, written local response and license file", "Underwrite the property under the allowed fallback use.", "Treat uncertain legal use as a purchase condition, not post-close homework."),
    ("hoa-diligence", "HOA diligence", "Can an association restrict the plan?", "Read the declaration, amendments, rules, minutes and enforcement history for minimum stays, guest access and future rule changes.", "association documents, board response, minutes and resale package", "Model a longer minimum stay or loss of STR permission.", "Do not rely on a listing claim or a neighbor's current practice."),
    ("insurance-quote", "insurance quote", "Is the operating plan insurable at the modeled cost?", "Request an address-specific quote that names short-term-rental use, peril limits, deductible, liability and business-income coverage.", "bindable quote, exclusions, loss history and lender insurance requirements", "Carry the largest deductible and a renewal premium increase.", "Make coverage terms part of the pre-close decision file."),
    ("seller-financials", "seller financials", "Can seller revenue be reconciled?", "Reconcile reservation dates, gross bookings, refunds, fees, taxes and deposits to statements and bank records.", "reservation export, platform payout report, bank deposits and P&L", "Remove nontransferable reviews, owner labor and one-off event spikes.", "Pay for independently supported earnings, not screenshots."),
    ("property-inspection", "property inspection", "What inspections belong in the contract window?", "Start with a general inspection, then order specialists for the asset's systems and revenue-critical amenities.", "inspection report, specialist scope, seller disclosures and repair bids", "Price the highest-impact defect and its guest downtime.", "Extend or protect the contingency when decisive reports arrive late."),
    ("management-cost", "management cost", "What will hands-off operation actually cost?", "Compare full-service, co-host and self-management with all fees, minimums, dispatch, cleaning oversight and owner time.", "management proposal, fee schedule, SLA and owner task list", "Add after-hours incidents and peak-season turnover volume.", "Buy the operating coverage required by the asset, not the lowest headline percentage."),
    ("cleaning-cost", "cleaning cost", "Does the turnover budget match the stay pattern?", "Estimate turns from booked nights divided by average stay; multiply by full clean, laundry, inspection and restock cost.", "cleaner bids, stay-length comps, linen plan and turnover calendar", "Shorten average stay and increase same-day turns.", "Do not compare gross nightly rate with cleaning fees excluded from costs."),
    ("utility-cost", "utility cost", "How should utilities enter the underwriting?", "Use bills and system loads to estimate fixed service plus occupancy-sensitive electricity, gas, water, internet and waste.", "twelve months of bills, rate schedules and equipment inventory", "Model a weather extreme and higher guest capacity.", "Replace a flat percentage with documented monthly costs."),
    ("maintenance-reserve", "maintenance reserve", "How much cash should be reserved for repairs?", "List major components, expected replacement cost and remaining life; fund a recurring reserve separate from routine maintenance.", "age and condition of systems, bids, warranties and service history", "Bring one major replacement into year one.", "Do not count the lender's reserve requirement as the property's repair reserve."),
    ("property-tax-reset", "property-tax reset", "Could taxes rise after acquisition?", "Ask the assessor how a sale, renovation or change of use affects assessed value and exemptions; use the buyer's likely bill.", "current bill, assessment record, local rules and assessor response", "Remove seller exemptions and raise assessed value.", "Underwrite the new owner's tax exposure before setting a maximum offer."),
    ("appraisal-risk", "appraisal risk", "Will the purchase price appraise under the chosen loan?", "Separate real estate from furniture and STR business value; compare the lender's appraisal method with actual closed sales.", "appraisal scope, closed comparables, furniture inventory and lender policy", "Model a lower appraisal and required extra cash.", "Cap any appraisal gap at an amount that preserves operating reserves."),
    ("offer-contingencies", "offer contingencies", "Which contingencies protect the buyer?", "Match each unresolved investment assumption to a document deadline, inspection right, financing condition or negotiated remedy.", "purchase agreement, diligence calendar, lender timeline and vendor availability", "Assume one critical answer arrives after earnest money is at risk.", "Have local counsel align the contract clock with the actual diligence work."),
    ("cash-flow-downside", "cash-flow downside", "How does the deal perform when bookings disappoint?", "Calculate monthly cash after debt, fixed costs, variable expenses and replacement reserve under base and downside revenue.", "monthly revenue model, debt schedule, fixed bills and variable-cost quotes", "Cut occupancy, raise insurance and add one repair.", "Require a reserve that covers the worst plausible cash-burn period."),
    ("purchase-price-limit", "purchase-price limit", "What is a defensible maximum offer?", "Solve backward from required return and cash available, then cross-check appraisal comps and the long-term-use fallback.", "return target, full cash budget, revenue case and comparable sales", "Reprice with lower revenue and higher entry costs.", "Walk away when the seller's ask exceeds both the return limit and evidence-supported value."),
    ("exit-strategy", "exit strategy", "Who could buy this property later?", "Identify likely STR, second-home and long-term-rental buyers; model sale costs, loan balance and restrictions each would inherit.", "sale comps, permit-transfer rules, asset condition and debt schedule", "Use a lower exit multiple and longer sale period.", "Do not count platform reviews or a personal permit as transferable value without proof."),
]

assert len(ASSETS) == 20
assert len(DECISIONS) == 25

ASSET_NOTES = {
    "beach-house": "A coastal booking pattern can put a large share of the year in a small number of weeks. Ask for monthly rather than annual comps, then compare wind and flood policy terms with the property's elevation and claims history. Exterior metal, condensers and deck hardware face salt exposure. A buyer who prices only interior finishes can miss recurring capital work and a storm-season cash reserve.",
    "lake-house": "The premium depends on usable water access, not simply a map pin near a lake. Verify recorded access, dock ownership, lake-level variation and whether boats or swimming are allowed. A dock, seawall or septic repair can consume the same cash planned for furnishing. Look at both lake-season bookings and demand when the water experience is unavailable.",
    "mountain-cabin": "Driveway grade, road maintenance and emergency access can determine whether guests and vendors reach the home in bad weather. Check snow removal responsibility and the actual distance from the cleaner's service area. Mountain revenue often clusters around weekends and holidays, so a calendar that assumes uniform occupancy can mask the carrying cost of quiet midweeks.",
    "ski-chalet": "The strongest winter dates can make annual revenue look durable even when snow conditions vary. Separate true ski-season bookings from shoulder and summer demand. Heat, roof snow load, ice dams and vehicle access can create costly peak-week outages. A delayed repair in January may sacrifice more contribution than the same delay in May.",
    "desert-home": "Pool and cooling systems are part of the guest product and the operating budget. Check equipment age, electric load, water costs and whether local restrictions affect the planned amenity. Event-week demand should be separated from ordinary weeks. A high annual average can conceal a long hot-weather period with weaker bookings and heavier utility use.",
    "urban-condo": "Building rules can determine the entire business case. Read the governing documents and board history before treating an active listing as proof of future permission. Guest access, elevator rules, sound transfer and special assessments can alter operating costs. A lender may also reject the project even if the individual unit's numbers appear attractive.",
    "suburban-home": "Family capacity, parking and neighbor impact matter as much as bedroom count. Verify legal sleeping rooms and practical arrival space before using large-group comparables. The same home may have a conventional lease fallback, which gives a useful independent test of carrying costs and exit value if short-term permissions or bookings change.",
    "rural-farmhouse": "Rural properties often shift risk from the building to site infrastructure. A well, septic system, private road or weak internet connection can limit legal capacity and guest satisfaction. Vendor travel time raises the price of a late-night fix. Avoid assuming group-event income without confirming the property's permitted use and actual event demand.",
    "tiny-home": "The low headline price can hide land, utility and title costs. Confirm whether the unit is real property, whether it meets dwelling rules and how many guests can legally sleep there. Financing and resale can differ sharply from a standard house. Compact interiors also make storage, cleaning flow and ventilation material operating questions.",
    "duplex": "Two units offer operating choices, but each unit needs a separate legal and financial case. Shared systems, meters and sound transfer can make one guest stay affect the other unit or a long-term tenant. Review leases and tenant rights before assuming both doors are available. The combined income statement should still show unit-level performance.",
    "triplex": "A triplex can support mixed rental strategies, yet shared circulation and unit-level permit caps may constrain the plan. Verify each legal unit, fire separation and meter arrangement. Keep existing tenant obligations visible. When comparing a mixed-use operating plan with all-long-term leasing, include the extra coordination and guest turnover cost.",
    "fourplex": "Four rentable units do not automatically mean four STR permits or four independent revenue streams. Confirm parcel-level restrictions and whether the building's common areas can handle the guest pattern. Unit-level revenue and expenses are essential; a strong unit can conceal a weak one in an aggregate pro forma. Conventional multifamily economics offer a useful exit cross-check.",
    "townhouse": "Attached ownership trades some exterior maintenance control for association dependence. The declaration can govern guest stays, parking, trash and exterior work. Shared walls increase noise exposure, and a master policy may leave the interior or rental-income gap with the owner. Read the actual insurance allocation alongside the HOA rules.",
    "luxury-estate": "A premium nightly rate can come from relatively few high-value reservations. One cancellation, staffing failure or unavailable amenity can move annual results materially. Verify the market has a true comparable buyer and guest segment, then price pool, grounds and specialist systems. The exit pool may be thin even when the home's photography is compelling.",
    "historic-home": "Distinctive architecture may support demand, but older systems and preservation rules can slow the improvement plan. Inspect wiring, plumbing, envelope and previous alterations with specialists. Confirm what changes require historic approval before using renovation upside in the offer. Repair parts and contractor availability belong in the downtime estimate.",
    "waterfront-cabin": "A compact cabin's economics may depend on the exact shoreline and dock rights. Verify access, erosion, flood exposure, moisture intrusion and septic capacity. A water view is not the same as legal water use. Model the booking calendar when swimming or boating is unavailable, and price seasonal maintenance before treating the amenity as pure premium.",
    "a-frame-cabin": "Photos emphasize the roof shape, while underwriting depends on usable space. Sloped ceilings and lofts can reduce legal sleeping capacity or make cleaning harder. Check loft egress, insulation and drainage at roof intersections. Compare revenue with properties that have the same permitted capacity, not with larger cabins that merely share a distinctive look.",
    "manufactured-home": "Title, foundation and land ownership can determine whether the deal is financeable and resalable. Verify whether the home is permanently affixed, whether the land conveys and whether a park agreement limits guest stays. Older units may be difficult to insure or finance. Compare total entry cash and exit options with a standard home, not just the list price.",
    "mixed-use-building": "Residential lodging and commercial space may be valued, financed and insured under different assumptions. Separate entrances, fire systems, utility meters and tenant obligations before combining revenues. A retail or office tenant can stabilize cash flow yet complicate guest circulation. Each use needs its own legal basis and downside case.",
    "new-construction-home": "A new home has limited operating history, so the pro forma must come from independent comparables. Completion, certificate of occupancy, punch-list work and permit issuance can all delay the first booking. Confirm which warranty claims are handled promptly enough for a guest operation. A lender's rate lock or appraisal timing may expire before the property is ready.",
}

DECISION_NOTES = {
    "investment-cost": "Build the cash ledger in the order money leaves the account: earnest money, inspections, lender deposits, closing funds, final contractor draws, furniture and launch stock. This prevents a profitable-looking annual model from masking an unfunded opening. Maintain a separate reserve rather than treating unused furnishing budget as emergency liquidity.",
    "cash-on-cash-return": "Choose a consistent definition before comparing properties. Include all invested cash and subtract replacement reserves from distributable cash. A high return created by thin reserves is not comparable with a fully funded deal. Show the result before any speculative tax benefit, then let the owner's CPA evaluate tax treatment separately.",
    "break-even-occupancy": "First determine the contribution of a booked night after costs that change with occupancy. Then divide fixed annual cash obligations by that contribution. The answer is a minimum number of paid nights, not a market forecast. Compare it with a conservative month-by-month calendar and with the nights the owner intends to block.",
    "revenue-forecast": "Use actual availability and realized revenue, not a screenshot of advertised nightly rates. Remove cleaning fees or taxes if they are not retained revenue. Adjust each comp for capacity, location and amenities, and disclose where evidence is thin. A new listing should carry a launch ramp until pricing and reviews have been tested.",
    "dscr-loan": "DSCR programs vary in the income they accept and the property types they finance. Request the lender's written treatment of short-term income, appraisal rent schedule and reserve requirements. Then calculate the investor's own full cash-flow case, including management and capex, because a loan that qualifies can still be a poor investment.",
    "conventional-financing": "A borrower preapproval does not clear the address. Occupancy intent, unit count, association project review, property condition and documented reserves can change the answer. Ask the lender to identify property-specific conditions before the financing contingency ends, and retain a cash plan if an appraisal or project review causes delay.",
    "bridge-financing": "Short-term debt should finance a defined transition with a credible takeout. Put every point, draw fee, minimum interest period and extension charge on a timeline. The plan must survive a slower renovation and a lower appraisal at refinance. A cheap teaser rate is irrelevant if the exit loan will not accept the asset.",
    "seller-financing": "A seller note changes timing, not the need to repay. Have counsel examine lien position, due-on-sale exposure, servicing and default rights. Model the amortization and balloon from actual terms; compare it with the cash likely available from sale or refinance when due. Do not use an optimistic future valuation as the only exit.",
    "renovation-budget": "Split the scope into legal-use and safety work, revenue-critical repairs and optional design upgrades. Obtain trade bids and a realistic schedule for each. Downtime belongs in project cost because a delayed first booking has a cash effect. Price any improvement from incremental net contribution rather than from a hoped-for rate increase alone.",
    "furnishing-budget": "Start with the licensed guest count and the room plan. Specify beds, linens, seating, kitchen stock, outdoor items, installation and spare essentials, then compare supplier lead times with the launch date. Keep an itemized inventory for insurance and eventual sale. Retail spend is not automatically recoverable in the property's appraisal.",
    "permit-diligence": "Search rules at the jurisdiction, parcel, unit and owner level. Record caps, renewals, inspections, tax accounts and whether an existing permit survives sale. A currently operating neighbor proves little about the buyer's address. Underwrite the allowed alternative use if the permit is denied or delayed, and align the contract with that result.",
    "hoa-diligence": "Obtain the current declaration, amendments, rules and relevant meeting minutes, not a broker summary. Look for minimum stays, guest registration, parking, fines and the board's power to change policy. Confirm which insurance and maintenance costs fall on the unit owner. A favorable informal answer should be preserved in writing and checked against governing documents.",
    "insurance-quote": "The quote must name the actual occupancy and services offered. Compare wind, flood, wildfire, liability and business-income terms where relevant, along with deductibles and exclusions. Ask what changes at renewal or after a claim. Carry the deductible as available cash because coverage does not make the first dollars of a loss disappear.",
    "seller-financials": "Request raw reservation and payout exports for the same period as the P&L. Reconcile refunds, fees, taxes, owner stays and platform account changes to deposits. Normalize owner labor and one-time expenses. If the seller cannot provide a reproducible bridge from bookings to cash, lower confidence in the earnings and price accordingly.",
    "property-inspection": "A general inspection identifies systems but may not resolve the most expensive question. Order specialists for the asset's material exposures before the contract window closes. Require bids for defects that affect capacity, safety or opening date. The output should be a priced correction plan, not a stack of reports with no ownership or deadline.",
    "management-cost": "Compare proposals on the work actually delivered: messaging, pricing, cleaning supervision, local dispatch, maintenance authority and monthly reporting. List tasks that remain with the owner and value that time. Minimum fees, setup charges and add-ons can reverse a headline commission comparison, especially during a slow season.",
    "cleaning-cost": "Turnover volume follows stay length, not just occupancy. Model busy same-day turns, laundry capacity, inspection, consumables and a backup crew. A guest-paid cleaning fee may offset some cost, but it can also affect conversion and platform presentation. Compare net contribution per stay after the complete turnover expense.",
    "utility-cost": "Use a full billing year when available and separate fixed account charges from weather and guest use. Add internet, streaming, trash and amenity loads. A property that is empty can still carry substantial minimum service costs. Stress the months with the highest heating or cooling demand rather than spreading the annual bill evenly.",
    "maintenance-reserve": "Build a component schedule for roof, HVAC, water systems, appliances, exterior features and revenue-critical amenities. Record age, condition, expected replacement cost and likely timing. Routine service belongs in operating expenses; large replacements belong in a funded reserve. The first-year requirement may exceed a steady annual average.",
    "property-tax-reset": "The seller's bill can reflect an older assessment or exemption the buyer cannot keep. Check the local reassessment mechanism and recent comparable assessments with the assessor. Renovation or a changed use may add another trigger. Use the buyer's probable tax bill in debt-coverage and cash-return calculations before deciding the offer.",
    "appraisal-risk": "An STR business can have value to the buyer that an appraiser will not credit as real estate. Separate the building, furniture and nontransferable operating history. Review closed comparable sales and the lender's appraisal scope before covering a gap. Extra cash used for a gap is capital that cannot also fund launch or emergencies.",
    "offer-contingencies": "Turn each major unknown into a contract event with a clear evidence deadline. The calendar must allow enough time for permits, insurer, lender and specialist inspections. If the remedy is a credit, define how it will be priced and whether the lender allows it. Local counsel should write the protection before the buyer releases deposit leverage.",
    "cash-flow-downside": "Build monthly cash, not only an annual profit line. Debt and insurance continue during a weak booking month, while variable expenses fall with occupancy. The largest cumulative deficit determines reserve need. Stress correlated problems, such as a revenue dip during a repair, instead of changing one optimistic input at a time.",
    "purchase-price-limit": "Start with a required after-reserve return and full entry cash. Solve for a price that meets it, then compare that ceiling with closed-sale evidence and an alternate-use case. If the seller asks more, do not solve the gap by deleting reserves or assuming tax savings. A disciplined maximum makes the walk-away decision easier.",
    "exit-strategy": "List buyer groups that can legally use and finance the property, then estimate net proceeds after debt, sale costs and repairs. Treat reviews, permits and manager relationships as conditional until transfer is verified. A narrow buyer pool or slow sale means carrying costs continue longer. The exit model should be credible even if STR income falls.",
}
assert set(ASSET_NOTES) == {a[1] for a in ASSETS}
assert set(DECISION_NOTES) == {d[0] for d in DECISIONS}

WORKSHEETS = {
    "investment-cost": "Cash required = down payment + buyer closing costs + immediate repairs + furniture + launch spend + opening reserve. Keep prepaid items and refundable deposits visible as separate lines.",
    "cash-on-cash-return": "Cash-on-cash return = annual cash after debt service and replacement reserve / all cash invested. Show both the base case and a lower-revenue case.",
    "break-even-occupancy": "Break-even booked nights = annual fixed cash costs / contribution per booked night. Contribution is realized night revenue less night-level variable costs.",
    "revenue-forecast": "Annual gross revenue = sum of each month's available nights × expected occupancy × realized nightly revenue. Do not apply one annual average to every season.",
    "dscr-loan": "Lender DSCR = income allowed by the lender / debt service under the lender's definition. Investor cash flow uses the full expense and reserve stack separately.",
    "conventional-financing": "Compare cash-to-close, payment, reserve requirement and permitted occupancy for each written loan option. A preapproval is conditional on the property.",
    "bridge-financing": "Bridge carry = points + fees + interest through expected takeout + extension cost + remaining renovation cash. Compare it with the permanent-loan path.",
    "seller-financing": "Payment and balloon must be modeled from the signed note terms. Compare remaining principal at maturity with a conservative refinance amount.",
    "renovation-budget": "Project cost = signed trade bids + permits + contingency + extra carrying costs while the unit is unavailable. Incremental return uses added net income, not added gross revenue.",
    "furnishing-budget": "Launch spend = room inventory + freight + installation + replacements for damaged or delayed essentials. Keep owner-use items outside the rental budget.",
    "permit-diligence": "Record allowed use as a verified condition: parcel, owner, unit, permit class, capacity, expiration and transfer rule. Price the fallback independently.",
    "hoa-diligence": "Extract the operative stay minimum, guest-access rules, fines, assessment obligations and amendment procedure from actual governing documents.",
    "insurance-quote": "Annual insurance cost = premium + reserve for the property-specific deductible and exclusions. Align the insured use with the planned booking pattern.",
    "seller-financials": "Reconciled gross bookings - refunds - platform fees - taxes remitted = expected deposits, adjusted for timing. Explain every material variance.",
    "property-inspection": "Risk-adjusted repair budget = priced immediate defects + contingency + lost contribution during repair. Separate safety or legal-use items from cosmetic work.",
    "management-cost": "Total management cost = base commission + minimum fees + setup + inspection + dispatch + after-hours charges + owner tasks that remain.",
    "cleaning-cost": "Annual turns = forecast booked nights / average stay length. Multiply turns by cleaning, laundry, restock and inspection cost, then add deep cleans.",
    "utility-cost": "Monthly utilities = service minimums + weather load + guest-use load + internet + waste. Use actual billing periods when available.",
    "maintenance-reserve": "Annual replacement reserve = sum of major component replacement costs / realistic remaining years, adjusted for near-term work already identified.",
    "property-tax-reset": "Buyer tax estimate = likely post-sale assessed value × applicable rate, adjusted for exemptions the buyer actually qualifies for.",
    "appraisal-risk": "Appraisal gap cash = contract price - appraised real-estate value after lender adjustments. Add this to cash-to-close rather than hiding it in projected returns.",
    "offer-contingencies": "For each unresolved fact, record evidence owner, delivery date, deposit deadline and remedy. A report delivered after the deadline does not protect the buyer.",
    "cash-flow-downside": "Monthly cash = revenue - variable expenses - fixed bills - debt payment - replacement reserve. Track the maximum cumulative deficit, not only year-end profit.",
    "purchase-price-limit": "Maximum offer is the lower of a return-based price and evidence-supported value after accounting for all required startup cash and a downside reserve.",
    "exit-strategy": "Net sale proceeds = sale price - selling costs - debt payoff - required repairs or concessions. Compare under STR and non-STR buyer cases.",
}
assert set(WORKSHEETS) == {d[0] for d in DECISIONS}


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def titlecase(value: str) -> str:
    return value.title().replace("Dscr", "DSCR").replace("Hoa", "HOA")


def guide(asset, decision):
    name, asset_slug, fit, revenue, physical, legal, finance, operations, resale = asset
    slug, phrase, question, method, documents, stress, boundary = decision
    path = f"{BASE}{asset_slug}/{slug}/"
    title = f"{titlecase(name)} STR {titlecase(phrase)} Guide"
    description = f"Buying a {name}? Check {phrase}, required documents, downside cases and the decision rule before committing capital."
    trail = [("Home", "/"), ("Guides", "/guides/"), ("STR investor guides", BASE), (title, path)]
    related = [(f"{BASE}{asset_slug}/{d[0]}/", d[1]) for d in DECISIONS if d[0] != slug][:2]
    if slug in {"dscr-loan", "conventional-financing", "bridge-financing", "seller-financing"}:
        parent = "/financing/"
    elif slug in {"permit-diligence", "hoa-diligence"}:
        parent = "/regulations/"
    elif slug in {"management-cost", "cleaning-cost", "utility-cost", "maintenance-reserve"}:
        parent = "/management/"
    else:
        parent = "/underwriting/"
    schema = tpl.graph(tpl.breadcrumb_schema(trail), tpl.ORG_SCHEMA)
    body = f"""
  <section class="hero hero-page"><div class="wrap">{tpl.breadcrumb_html(trail)}
    <div class="hero-inner"><span class="eyebrow">For business owners and real estate investors</span>
      <h1>{esc(title)}</h1><p class="hero-sub">{esc(question)} A purchase-stage worksheet for {esc(('an' if name[0].lower() in 'aeiou' else 'a') + ' ' + name)}.</p>
    </div></div></section>
  <section><div class="wrap"><article class="article">
    <p class="lead">{esc(('An' if name[0].lower() in 'aeiou' else 'A') + ' ' + name)} can appeal to investors because of {esc(fit)}. Before committing capital, answer this question for the actual address: {esc(question)} The method is to {esc(method[0].lower() + method[1:])}</p>
    <h2>Make the decision before the deposit is at risk</h2>
    <p>{esc(DECISION_NOTES[slug])}</p>
    <h2>What changes for this property</h2>
    <p>{esc(ASSET_NOTES[asset_slug])}</p>
    <p>The revenue case should {esc(revenue)}. Record the source, the period covered and any owner-blocked nights beside the forecast.</p>
    <p>The physical file should address {esc(physical)}. The legal and insurance file should address {esc(legal)}. A favorable answer on one does not repair an unsupported answer on the other. Obtain written, address-specific evidence before letting the contract's protection expire.</p>
    <h2>Documents to request</h2>
    <ul>
      <li>{esc(documents.capitalize())}.</li>
      <li>Property-specific records for {esc(physical)}.</li>
      <li>Written confirmation of {esc(legal)}.</li>
      <li>Financing sensitivity: {esc(finance[0].upper() + finance[1:])}.</li>
    </ul>
    <h2>Run the downside case</h2>
    <p><strong>Worksheet:</strong> {esc(WORKSHEETS[slug])}</p>
    <p>{esc(stress)} Keep the original and stressed worksheets side by side. Recalculate cash needed at closing, the first twelve months of cash flow, and the reserve required to survive a delay or repair. If a source is missing, mark that input as unverified rather than filling it with the seller's optimistic estimate.</p>
    <p><strong>Operating exposure to price:</strong> {esc(operations[0].upper() + operations[1:])}. Identify the vendor, fee, start date and backup for each required task. Those costs affect the underwriting and the date of the first rentable night.</p>
    <h2>Decision rule for the buyer</h2>
    <p>{esc(boundary)} Also test the exit: {esc(resale)}. A business owner should decide whether the property still fits when attention is focused on the primary business; a real estate investor should compare the same capital with the next available deal on a consistent after-reserve basis.</p>
    <p>Use the <a href="{parent}">existing BNB Accelerator guide</a> for the broader method, then bring the address, documents and assumptions to a qualified lender, insurer, attorney, CPA or inspector as appropriate. These pages are decision worksheets, not a representation that any listed property type is available or approved in a given market.</p>
    <div class="callout"><h3>Continue the purchase file</h3><ul>
      <li><a href="{related[0][0]}">Review {esc(related[0][1])} for this property type</a></li>
      <li><a href="{related[1][0]}">Review {esc(related[1][1])} for this property type</a></li>
      <li><a href="{BASE}">Browse all investor decision guides</a></li>
    </ul></div>
    {tpl.AUTHOR_BOX}
  </article></div></section>
  {tpl.cta_band("Want help screening the acquisition?", "BNB Accelerator sources and underwrites short-term-rental purchases for business owners and real estate investors.", ("/apply/", "Apply for a Call"), ("/case-studies/", "See Client Results"))}
"""
    body = "\n".join(line.rstrip() for line in body.split("\n"))
    return path, tpl.page(title=f"{title} | BNB Accelerator", description=description,
                          path=path, body=body, extra_schema=schema, active="/blog/")


def hub():
    trail = [("Home", "/"), ("Guides", "/guides/"), ("STR investor guides", BASE)]
    groups = []
    for asset in ASSETS:
        name, slug = asset[:2]
        links = "\n".join(
            f'<li><a href="{BASE}{slug}/{d[0]}/">{esc(titlecase(d[1]))}</a></li>'
            for d in DECISIONS
        )
        groups.append(f'<section><h2>{esc(name.title())}</h2><ul class="sitemap-list">{links}</ul></section>')
    body = f"""
  <section class="hero hero-page"><div class="wrap">{tpl.breadcrumb_html(trail)}
    <div class="hero-inner"><span class="eyebrow">Acquisition library</span>
      <h1>STR investment purchase guides</h1>
      <p class="hero-sub">500 property-specific decisions for business owners and real estate investors. Choose the property and the purchase question, then replace every assumption with address-specific evidence.</p>
    </div></div></section>
  <section><div class="wrap"><p class="lead">Start with the capital decision, legal use and an operating downside. Each guide names the records to request and the condition that can change the offer.</p>
    <div class="sitemap-index">{''.join(groups)}</div>
  </div></section>
  {tpl.cta_band("Ready to screen an actual property?", "Bring the address and documents to a BNB Accelerator strategy call.", ("/apply/", "Apply for a Call"), ("/underwriting/", "See Underwriting"))}
"""
    schema = tpl.graph(tpl.breadcrumb_schema(trail), tpl.ORG_SCHEMA)
    body = "\n".join(line.rstrip() for line in body.split("\n"))
    return tpl.page(title="STR Investment Purchase Guides | BNB Accelerator",
                    description="500 acquisition decision guides for business owners and real estate investors buying short-term rental property.",
                    path=BASE, body=body, extra_schema=schema, active="/blog/")


def main():
    paths = set()
    for asset in ASSETS:
        for decision in DECISIONS:
            path, page = guide(asset, decision)
            if path in paths:
                raise RuntimeError(f"duplicate guide: {path}")
            paths.add(path)
            write(path, page)
    write(BASE, hub())
    print(f"investor guides: {len(paths)} decision pages plus hub")


if __name__ == "__main__":
    main()
