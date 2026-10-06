"""Reviewed content owners for eight existing STR buyer-intent URLs.

tpl.page consults these exact routes, so ordinary legacy regeneration retains
the reviewed copy. No routes, market averages or real client outcomes are added.
"""
from decimal import Decimal
from datetime import date
import json
from buyer_intent_inputs import (BEACH_ENTRY, FURNISHING, FOURPLEX, CHANDLER_ENTRY,
                                 OCCUPANCY_QUARTERS, fourplex_threshold)

REVIEWED = '2026-10-06'
COST = '/guides/str-investment/beach-house/investment-cost/'
FURNISH = '/guides/str-investment/beach-house/furnishing-budget/'
BREAK_EVEN = '/guides/str-investment/fourplex/break-even-occupancy/'
CHANDLER = '/markets/chandler/'
ARIZONA = '/blog/arizona-str-investing/'
REVPAR = '/answers/what-is-revpar/'
OCCUPANCY = '/blog/airbnb-occupancy-rates-explained/'
PRICING = '/pricing/'
SOURCES = {
    'closing': 'https://www.consumerfinance.gov/owning-a-home/closing-disclosure/',
    'flood': 'https://www.floodsmart.gov/',
    'chandler': 'https://www.chandleraz.gov/business/tax-and-license/short-term-rental',
    'arizona': 'https://www.azleg.gov/ars/9/00500-39.htm',
    'revpar': 'https://www.amadeus-hospitality.com/insight/what-is-revpar-formula-calculate/',
    'sedona': 'https://www.bnbacceleratorreviews.co/case-studies/sedona-az-2025-46',
    'library': 'https://www.bnbacceleratorreviews.co/case-studies',
}


def link(path, label):
    return f'<a href="{path}">{label}</a>'


def money(value):
    return f'${Decimal(str(value)):,.0f}'


def percent(value):
    return f'{Decimal(str(value)):.1f}%'


PAGES = {
    COST: dict(
        title='Beach House Investment Cost: Full Buyer Budget | BNB Accelerator',
        h1='How much does a beach house cost to buy and launch as an STR?',
        description='Build a beach-house STR cash budget with down payment, closing, repairs, furnishings, launch and reserves. See an example that credits earnest money once.',
        eyebrow='Beach-house acquisition cash',
        lead='The price of a beach house is only the first input. A financed STR purchase also needs closing cash, immediate work, guest-ready furnishings and money left after opening. Build one dated cash ledger before choosing an offer; the hypothetical $800,000 purchase below requires $335,000 of committed cash before any separately quoted acquisition-service fee.',
        sections=[
            ('Worked hypothetical: $800,000 purchase, $335,000 cash plan', [
                'These invented amounts describe one planning case, not a coastal price range, lender quote or BNB Accelerator client result. Assume 25% down, no financed setup costs and no seller credits. The closing allowance includes all prepaids and escrow deposits in this example; do not add those same amounts again.',
                ('table', ['Cash category', 'Assumption', 'Evidence to replace it'], [
                    ['Down payment', '$200,000', 'Written loan terms: $800,000 × 25%'],
                    ['Closing charges and prepaids', money(BEACH_ENTRY['closing_costs_and_prepaids']), 'Lender and settlement estimate, insurance and escrow details'],
                    ['Immediate repairs', money(BEACH_ENTRY['immediate_repairs']), 'Inspection findings and priced trade scope'],
                    ['Furnishing allowance', money(BEACH_ENTRY['furnishing_allowance']), 'Itemized delivered-and-installed quote'],
                    ['Launch expenses', money(BEACH_ENTRY['launch']), 'Photography, supplies, permits and setup invoices'],
                    ['Operating reserve held after opening', money(BEACH_ENTRY['operating_reserve']), 'Monthly downside and delayed-opening cash model'],
                    ['Additional deductible liquidity', money(BEACH_ENTRY['deductible_liquidity']), 'Actual wind/flood/STR policy terms'],
                    ['Total committed purchase and launch cash', '$335,000', 'Sum of these distinct categories'],
                ]),
                f'The $42,000 setup line is an allowance. Replace it with an {link(FURNISH, "itemized coastal furnishing budget")}; a quote below the allowance leaves cash available, rather than proving savings already earned. Keep routine cleaning and utilities in the operating model, rather than hiding them in furniture.',
            ]),
            ('Earnest money reduces the remaining wire, not the investment total', [
                'Assume $20,000 earnest money is paid earlier and fully credited on the final settlement statement. Down payment plus closing/prepaids is $228,000. The remaining closing wire is $228,000 − $20,000 = $208,000. Post-closing setup and retained reserve allocations are $107,000. The cash plan still totals $20,000 + $208,000 + $107,000 = $335,000.',
                f'{link(SOURCES["closing"], "The CFPB Closing Disclosure explainer")} distinguishes cash to close from closing charges and money already paid. Match the actual statement and loan product with your closing professional. If an inspection or insurance invoice was paid outside closing, mark it paid in the same category; do not add it twice.',
            ]),
            ('Price the coastal exposures before releasing the deposit', [
                f'{link(SOURCES["flood"], "FloodSmart explains that most homeowners policies exclude flood damage")}. Obtain quotes for the actual rental use and location, with wind/flood coverage, contents, deductibles, exclusions and interruption terms shown separately. A deductible is cash exposure; an insurance premium is an expense. Neither guarantees reimbursement for a closed calendar.',
                ('ul', ['Confirm parcel rental use, permitted capacity and HOA terms for the buyer.',
                        'Price roof, HVAC, moisture, exterior corrosion and drainage defects with appropriate specialists.',
                        'Ask whether utilities, storage, beach access or parking add recurring or one-time costs.',
                        'Keep operating and deductible reserves distinct in this example; if your own reserve covers both, reconcile the overlap instead of funding it twice.']),
                f'Use the existing {link("/financing/closing-costs-and-reserves/", "all-in buyer budget")} and {link("/blog/str-purchase-to-launch-timeline/", "launch-delay cash plan")} for the broader method. The maximum simultaneous cash shortfall matters more than a generic percentage reserve.',
            ]),
            ('Turn the ledger into a purchase decision', [
                f'{link(PRICING, "Request the actual service fee and scope")} before treating the cash plan as complete. Add that fee and all unquoted third-party costs to the property ledger. Record each amount, payment date, source, owner and whether it remains an estimate.',
                'Proceed to a shortlist only when financing, legal use and quotes fit the cash you can commit while preserving the agreed reserve. If the plan spends every dollar at closing, lower the purchase scope or pause the search. A seller’s projected revenue does not fund your opening invoices.',
            ]),
        ],
        faqs=[('Is the down payment the full cost of buying a beach-house STR?', 'No. Include closing/prepaid cash, repairs, furnishings, launch and reserves, plus separately quoted service or vendor fees. The example uses invented assumptions.'),
              ('Do I add earnest money to cash to close?', 'Count credited earnest money once. It is part of total invested cash and reduces the remaining settlement wire when the final statement applies the credit.'),
              ('Is $335,000 a minimum BNB Accelerator buyer budget?', 'No. It is the total of one hypothetical purchase ledger, not a company eligibility threshold or a quote.')],
    ),
    FURNISH: dict(
        title='Beach House Furnishing Budget: Itemized STR Setup | BNB Accelerator',
        h1='What belongs in a beach-house STR furnishing budget?',
        description='Itemize a beach-house rental setup by room, freight, installation and contingency. Verify included furnishings, legal guest capacity and opening readiness.',
        eyebrow='Delivered and installed setup',
        lead='A furnishing budget should buy a complete, installed guest setup for the legal capacity of the house. It needs room inventory, freight, assembly, spare essentials and an acceptance date. A retail cart does not show whether a coastal rental can open, or whether the seller’s furniture is actually included in the sale.',
        sections=[
            ('Worked hypothetical: a $39,600 installed setup', [
                'Assume a four-bedroom property whose authorized occupancy supports the proposed bed plan. All amounts below are invented allowances for this one scope. They are not current vendor prices, BNB design fees or evidence of a nightly-rate premium.',
                ('table', ['Scope', 'Allowance'], [
                    ['Four bedroom packages at $4,000 each', money(FURNISHING['four_bedrooms_at_4000_each'])],
                    ['Living and dining', money(FURNISHING['living_and_dining'])],
                    ['Outdoor furniture', money(FURNISHING['outdoor_furniture'])],
                    ['Kitchen equipment and linen stock', money(FURNISHING['kitchen_and_linen_stock'])],
                    ['Technology and safety items', money(FURNISHING['technology_and_safety'])],
                    ['Freight, assembly and installation', money(FURNISHING['freight_and_installation'])],
                    ['Subtotal', money(sum(FURNISHING.values()))],
                    ['10% contingency on this subtotal', '$3,600'],
                    ['Setup cash allowance with contingency', '$39,600'],
                ]),
                'Require each quote to identify tax, freight, disposal, installation and substitutions. The example treats those costs as included in the stated categories. A contingency is held cash until spent; a lead-time problem may still need a separate carrying-cost allowance.',
                f'This is a detail worksheet. Put its accepted total into the {link(COST, "beach-house acquisition cash example")} rather than adding two different furnishing allowances. The purchase-price ledger and this independent setup example use different invented scopes.',
            ]),
            ('Buying furnished: verify the actual inventory', [
                ('ul', ['Attach a room-by-room included-item schedule to the purchase file; distinguish owned, leased and excluded items.',
                        'Photograph condition and record age for mattresses, sofas, outdoor pieces and major appliances.',
                        'Check missing linens, kitchen stock, locks, smoke/CO equipment and owner storage before pricing replacements.',
                        'Have the lender, settlement professional and counsel confirm how furniture is documented and valued.']),
                '“Sold furnished” is a scope claim. It does not certify guest readiness or the condition at possession. Price damaged or missing essentials as immediate work, with the responsible payer and completion date recorded.',
            ]),
            ('A delivery date is not an opening acceptance', [
                ('table', ['Acceptance check', 'Record to keep'], [
                    ['Bed plan matches approved capacity', 'Current capacity record and room layout'],
                    ['Critical furniture installed and safe', 'Inspection checklist, photos and punch list'],
                    ['Coastal cleaning/replacement plan', 'Washable materials, spare-stock list and local replacement source'],
                    ['Locks, internet and equipment work', 'Test results and vendor support details'],
                    ['Manager accepts the inventory', 'Signed handoff list and remaining work register'],
                ]),
                f'Use the {link("/management/", "management handoff checklist")} to assign inventory ownership, replenishment and repairs. Use the {link("/blog/str-purchase-to-launch-timeline/", "launch timeline")} to fund a delayed installation. Furniture spending alone proves neither a faster launch nor rental income.',
            ]),
        ],
        faqs=[('Is furnishing spend part of the property appraisal?', 'Do not assume it is. Ask the lender and settlement professional how the real estate and included personal property are treated.'),
              ('Does this example set a price per bedroom?', 'No. Four invented $4,000 packages are only one line in a hypothetical complete setup, with common rooms, stock, delivery and contingency separately counted.'),
              ('When is the setup finished?', 'When the legal capacity, installed inventory, safety/operating tests and agreed handoff are accepted, with remaining work assigned and funded.')],
    ),
    BREAK_EVEN: dict(
        title='Fourplex Break-Even Occupancy: Unit-Night Math | BNB Accelerator',
        h1='How do you calculate break-even occupancy for a fourplex STR?',
        description='Calculate fourplex STR break-even from paid unit-night contribution and fixed cash costs. Stress lower ADR, unavailable units and a mixed long-term lease.',
        eyebrow='Multifamily cash threshold',
        lead='Count available nights for each rentable unit, then divide the building’s fixed cash obligations by contribution per paid unit-night. A fourplex does not have only 365 available nights. Break-even is a cash threshold to compare with a conservative forecast; it is not expected occupancy or lender approval.',
        sections=[
            ('Worked hypothetical: 1,089 paid unit-nights', [
                'Assume four legally rentable units, each unavailable for 10 of 365 calendar nights. Available inventory is 4 × 355 = 1,420 unit-nights. This simplified case gives each unit the same realized lodging ADR and variable cost; different units need separate contributions in a real model.',
                'At a hypothetical $150 ADR, 20% revenue-linked distribution/management fees and $30 of variable cost per paid unit-night, contribution is $150 × 80% − $30 = $90. The variable line is after any retained guest cleaning fee; exclude pass-through taxes and avoid counting a fee in both lines.',
                ('table', ['Annual fixed cash obligation', 'Assumption'], [
                    ['Principal and interest debt service', money(FOURPLEX['debt_service'])],
                    ['Taxes and insurance', money(FOURPLEX['tax_and_insurance'])],
                    ['Fixed utilities and common service', money(FOURPLEX['fixed_utilities_and_common_service'])],
                    ['Replacement-reserve funding', money(FOURPLEX['replacement_reserve'])],
                    ['Total annual obligations', '$98,000'],
                ]),
                'Required paid unit-nights = $98,000 ÷ $90 = 1,088.89, rounded up to 1,089 whole unit-nights. Break-even occupancy = 1,089 ÷ 1,420 = 76.7%. This owner cash threshold includes debt and reserve funding. It is not accounting NOI or a DSCR numerator.',
            ]),
            ('Stress the rate and the usable inventory separately', [
                ('table', ['Case', 'Contribution per night', 'Required / available unit-nights', 'Threshold'], [
                    ['Base: $150 ADR', '$90', '1,089 / 1,420', percent(fourplex_threshold()['occupancy_percent'])],
                    ['ADR falls 10% to $135', '$78', '1,257 / 1,420', percent(fourplex_threshold(adr=135)['occupancy_percent'])],
                    ['Base ADR; one unit loses another 90 nights', '$90', '1,089 / 1,330', percent(fourplex_threshold(unavailable_extra=90)['occupancy_percent'])],
                ]),
                'A result above 100% cannot be covered within that inventory at that contribution. Higher minimum stays, owner use, repair closures or permit delays can change the denominator. Do not “solve” an infeasible case by deleting reserve funding or assuming every blocked date was booked.',
                f'Reconcile the {link(OCCUPANCY, "paid, available and calendar nights")} and compare monthly demand with the threshold. Use {link("/financing/dscr-loans/", "the separate lender DSCR and investor cash-flow checks")} for the loan question.',
            ]),
            ('One long-term unit does not guarantee an easier threshold', [
                'Assume one unit becomes a lawful long-term rental at an invented $1,800 monthly rent. Deduct 20% for incremental leased-unit expenses that are not already in the fixed building stack: $21,600 × 80% = $17,280 annual contribution. Keep the $98,000 building obligations unchanged for this comparison.',
                'The three STR units have 3 × 355 = 1,065 available unit-nights. They must cover $98,000 − $17,280 = $80,720, requiring 897 paid unit-nights at $90 contribution: 84.2% occupancy. The lease offsets obligations but also removes STR inventory. Verify leases, unit permissions and financing rather than assuming mixed use is allowed.',
            ]),
            ('Take these records to the offer decision', [
                ('ul', ['Unit-by-unit calendar, lease and permit/use file, including existing residents and possession dates.',
                        'Realized rate and revenue evidence for the same reporting period; seasonal comparables for each unit type.',
                        'Utility/meter allocation, turnover cost, shared repairs and fixed building costs.',
                        'Written debt terms, buyer tax/insurance estimates and a component replacement schedule.']),
                f'{link("/blog/reconcile-airbnb-payout-export/", "Verify seller income")} before relying on its ADR. Proceed only if the conservative unit-level forecast can cover the cash threshold and the monthly deficits fit your retained reserves. Equal unit rates are a disclosed simplification, not a market fact.',
            ]),
        ],
        faqs=[('Do I divide fourplex paid nights by 365?', 'Only if measuring one unit for one full year. For a building, aggregate each unit’s available nights; four fully available units have 1,460 unit-nights before closures or other exclusions.'),
              ('Does 76.7% mean the property will achieve that occupancy?', 'No. It is the calculated cash threshold under invented costs and rates. A forecast requires independent unit-level and seasonal evidence.'),
              ('Can I combine long-term and short-term units?', 'Verify use, leases and lender terms first. Then subtract the leased unit’s contribution from obligations without double-counting expenses, and remove its nights from STR inventory.')],
    ),
    CHANDLER: dict(
        title='Chandler STR Investment: Buyer Due Diligence | BNB Accelerator',
        h1='How should a buyer screen a short-term rental investment in Chandler?',
        description='Screen a Chandler STR address for city licensing, HOA use, matched comparables, full purchase cash and weak-month carrying costs before an offer.',
        eyebrow='Chandler address-level research',
        lead='Start a Chandler STR purchase with the address, the buyer’s permitted use and the actual guest trip you intend to serve. Then price the full entry budget and a weak operating month. This educational guide does not establish current BNB Accelerator service availability, a citywide return or permission for a particular parcel.',
        sections=[
            ('Make a Chandler use file before a revenue forecast', [
                f'{link(SOURCES["chandler"], "Chandler’s current short-term rental license guidance")} lists a city license for each location, a state TPT license, county rental registration, neighbor notification, posted emergency/use information and license numbers in advertisements. Verify the buyer’s current application and ownership-change requirements; a seller’s operating listing is not the buyer’s authorization.',
                ('table', ['Question', 'Document or written confirmation'], [
                    ['Which jurisdiction controls the address?', 'Parcel map and city/county confirmation'],
                    ['Can this buyer operate the proposed use?', 'Current city instructions and completed license/use file'],
                    ['Does the HOA permit the stay pattern?', 'Declaration, amendments, rules and relevant minutes'],
                    ['Who responds locally?', 'Named emergency/operating contact and accepted coverage'],
                    ['Is the operation insured and tax-ready?', 'Actual rental-use quotes and applicable tax registrations'],
                ]),
                f'Use the existing {link("/blog/permits-that-do-not-transfer/", "permit and HOA transfer checklist")} to identify what must be obtained anew or updated. The city workflow is evidence of requirements, not a guarantee of approval or opening date.',
            ]),
            ('Choose comparables for the trip, not the metro label', [
                'Treat corporate, family, event or winter-visitor demand as hypotheses to test. For each candidate, document the trip destination, travel time at relevant hours, authorized capacity, parking, pool and cooling costs, workspace and minimum-stay pattern. A similar-looking home elsewhere in Phoenix may serve a different trip.',
                'Request a full year of property-specific earned revenue and available/paid nights. Compare legal, similar-capacity listings near the same trip drivers for ordinary weekdays and weak months as well as event dates. Advertised rates and unavailable calendars do not establish realized ADR or occupancy.',
                f'{link("/blog/reconcile-airbnb-payout-export/", "Reconcile the seller’s income packet")} before using it in an offer. For broader state research, use the {link(ARIZONA, "Arizona buyer evidence guide")}; Chandler’s local question stays on this canonical.',
            ]),
            ('Worked hypothetical: $265,000 entry cash and a weak month', [
                'Assume an invented $650,000 purchase with 25% down. These inputs are not Chandler averages or lender terms. Add $162,500 down, $22,500 closing/prepaids, $12,500 immediate repairs, $35,000 furnishing, $4,500 launch and $28,000 retained reserve: $265,000. Add any separately quoted service fee or other excluded costs before treating the ledger as complete.',
                'For one invented 30-night operating month, assume 12 paid nights at $160 lodging ADR: $1,920 lodging revenue. Revenue-linked charges total 18%; night-variable cost is $22 and fixed cash obligations are $4,400. Monthly cash = $1,920 × 82% − 12 × $22 − $4,400 = −$3,089.60, before any additional replacement-reserve funding.',
                'The fixed line must include the actual debt, tax/insurance and ongoing utility/pool costs once quoted. One weak month does not set the full reserve: model the sequence of monthly deficits, a slower launch and a repair interruption, with overlapping reserve purposes reconciled.',
            ]),
            ('Define the next decision and the service boundary', [
                'Bring the address, cash ceiling, loan conditions, legal-use packet, matched comparables and unresolved expenses to a purchase review. Ask which diligence facts could lower the offer or require walking away. Request current service coverage and written deliverables separately; this page’s educational coverage supplies neither.',
                f'The {link("/financing/closing-costs-and-reserves/", "all-in reserve and closing guide")} and {link("/management/", "management handoff checklist")} cover the next files. A purchase process or historical Arizona closing does not establish your rental returns.',
            ]),
        ],
        faqs=[('Does a Chandler Airbnb listing prove I can operate after purchase?', 'No. Verify the buyer’s licensing, parcel/HOA use, tax setup, insurance and operating responsibilities. Seller listing activity is not buyer approval.'),
              ('Are the $650,000 price and $265,000 budget Chandler market averages?', 'No. Both belong to one invented planning example and must be replaced with property-specific terms and quotes.'),
              ('Does this page confirm BNB Accelerator currently buys in Chandler?', 'No. It provides educational purchase checks. Obtain current service availability and scope directly in writing.')],
    ),
    ARIZONA: dict(
        title='Arizona STR Investing: Address-Level Buyer Checks | BNB Accelerator',
        h1='How do you compare Arizona STR investments before choosing an address?',
        description='Build an Arizona STR purchase file by jurisdiction, guest trip, seasonal cash and operating scope. Separate educational coverage from current service and returns.',
        eyebrow='Arizona purchase evidence', published='2026-08-11',
        lead='An Arizona label does not supply a permit, a comparable nightly rate or a viable cash budget. Compare the exact jurisdiction, guest trip, stay pattern and monthly costs for each address. This guide covers research; current acquisition-service availability and historical company transactions are separate evidence.',
        sections=[
            ('State law is a starting point for the local file', [
                f'{link(SOURCES["arizona"], "Arizona’s municipal STR statute")} limits municipal prohibitions and authorizes specified local requirements. It also contains qualifications and an accessory-dwelling provision. It does not clear an address, an HOA, the proposed occupancy or a buyer’s license application. Read the current rule and obtain the applicable local instructions.',
                f'If the candidate is in Chandler, use {link(CHANDLER, "Chandler address-specific purchase checks")} for its city workflow, matched comparables and buyer cash file. Do not transfer that answer to Scottsdale, Mesa, Sedona or an unincorporated parcel. A city name in marketing copy can differ from the actual jurisdiction.',
            ]),
            ('Compare addresses using the same evidence columns', [
                ('table', ['Purchase question', 'Evidence for each candidate', 'Reason to pause'], [
                    ['Proposed guest trip and stay pattern', 'Trip destination, travel time, capacity and monthly matched comps', 'A metro average substitutes for the property’s guests'],
                    ['Legal and association use', 'Parcel jurisdiction, buyer application requirements and HOA documents', 'Permission depends only on the seller’s listing'],
                    ['Price and cash committed', 'Loan terms, settlement estimate, repairs, setup and separate service quote', 'An opening invoice would consume the retained reserve'],
                    ['Summer/winter operating exposure', 'Monthly paid/available nights, realized rates and utility/pool bills', 'A peak month is annualized without a weak-month case'],
                    ['Possession and operating transition', 'Leases, existing reservations, included items and manager scope', 'The purchase assumes an unconfirmed transfer'],
                ]),
                f'Begin with {link("/blog/reconcile-airbnb-payout-export/", "seller-income verification")}, then run {link("/financing/dscr-loans/", "lender underwriting separately from owner cash flow")}. Keep source, period and confidence beside every number. No table of statewide “average ROI” can replace this file.',
            ]),
            ('Historical acquisition evidence has a narrower meaning', [
                f'The {link(SOURCES["sedona"], "public Sedona closing-balance story")} records a $993,000 tracker purchase-price field, a November 21, 2025 closing-date field and a $25,000 seller-concession field. Its notes discuss insurance/lender conditions, title balancing and a final cash-to-close difference. The tracker status is not independent deed verification, and the credit field does not prove its final application.',
                f'This is useful evidence about closing coordination. It supplies no annual rental income or return. The {link(SOURCES["library"], "company-operated acquisition/process library")} preserves other historical records with their limits. Use a current settlement statement, license/use file and operating evidence for your own purchase.',
            ]),
            ('Stay length and seasonal reserves are purchase inputs', [
                'Price a proposed longer-stay lease and a nightly operation as separate legal, lending and operating cases. Collect lease terms, cleaning frequency, unpaid/blocked nights and month-by-month costs. Do not assume that a stay pattern produces a particular tax treatment or deduction; have the owner’s tax adviser assess the actual facts.',
                f'Use {link(OCCUPANCY, "the paid/available-night occupancy worksheet")} to expose owner blocks and seasonal differences. Use {link("/blog/str-purchase-to-launch-timeline/", "the delayed-opening cash plan")} and {link("/management/", "the operating handoff register")} for reserves and transition dependencies. These existing files support an address decision without recreating a generic state forecast.',
            ]),
            ('Make the search brief specific enough to reject a property', [
                'Write the cash ceiling, financing conditions, acceptable monthly deficit, intended personal use, verified jurisdiction and operational responsibilities. Choose which fact could stop the offer and who will obtain it before the deposit deadline. Ask for current service scope and market availability before relying on a team’s involvement.',
            ]),
        ],
        faqs=[('Does Arizona state preemption mean every home can be an STR?', 'No. Read the statute’s qualifications and current local rules, then verify the parcel, ownership, license, capacity, HOA and actual use.'),
              ('Which Arizona market has the best rental return?', 'This guide does not establish that ranking. Compare independently supported property income, expenses, invested cash, debt and reserve assumptions for the same period.'),
              ('Does a historical Arizona acquisition prove active service coverage today?', 'No. A historical transaction, educational guide and current service agreement answer different questions.')],
    ),
    REVPAR: dict(
        title='RevPAR Definition and Formula for STR Buyers | BNB Accelerator',
        h1='What is RevPAR, and how do you calculate it for an STR?',
        description='RevPAR means revenue per available room or unit-night. Calculate it with consistent lodging revenue, ADR and occupancy, then test costs before buying.',
        eyebrow='Revenue metric definition', published='2026-08-15',
        lead='RevPAR means revenue per available room. For a whole-property STR, treat the listing as one rentable unit and calculate lodging revenue divided by its available unit-nights for the same period. Equivalently, use realized lodging ADR multiplied by paid-night occupancy with the same denominator. RevPAR measures revenue yield, not buyer profit.',
        sections=[
            ('Keep the unit, period and revenue definition consistent', [
                f'{link(SOURCES["revpar"], "Amadeus explains the hotel RevPAR formulas")} as room revenue / available rooms or ADR × occupancy. Our whole-listing STR adaptation uses unit-nights. A four-bedroom house rented as one listing is one unit; four separately rented legal units have four calendars.',
                'Use earned lodging revenue after lodging refunds for one reporting period. Exclude separately accounted pass-through taxes and cleaning from this numerator. Realized ADR = that lodging revenue / paid unit-nights. Occupancy = those paid unit-nights / available unit-nights. Future reserved stays are a separate forecast, not earned results.',
                f'If owner use or repair closures remove nights, show the policy and calendar-night utilization too. {link(OCCUPANCY, "Reconcile paid, available and calendar nights")} before comparing two listings. Changing only the availability denominator can improve the displayed metric without adding a dollar.',
            ]),
            ('Worked hypothetical: higher RevPAR can still contribute less cash', [
                'Assume two separate whole-property listings, each with 30 available nights in the same period. All inputs are invented and lodging-only.',
                ('table', ['Metric', 'Listing A', 'Listing B'], [
                    ['Paid nights / available nights', '18 / 30', '24 / 30'],
                    ['Realized lodging ADR', '$200', '$160'],
                    ['Lodging revenue', '$3,600', '$3,840'],
                    ['Paid occupancy', '60%', '80%'],
                    ['RevPAR', '$120', '$128'],
                    ['Assumed revenue-linked charges', '20%', '20%'],
                    ['Other variable cost per paid night', '$25', '$40'],
                    ['Contribution before fixed costs, debt and reserves', '$2,430', '$2,112'],
                ]),
                'A contributes $3,600 × 80% − 18 × $25 = $2,430. B contributes $3,840 × 80% − 24 × $40 = $2,112. B has $8 higher RevPAR but $318 less contribution because the expense assumptions differ. Neither result is net owner cash flow until fixed bills, debt and replacement funding are included.',
            ]),
            ('Use it as one check in the purchase file', [
                'Request the property-level lodging ledger, paid/available calendar, refunds and owner/maintenance block policy. Use the same period and unit definition for comps. A portfolio dashboard mixing bedrooms, whole houses and future bookings cannot supply a reproducible comparison.',
                f'For a purchase threshold, use the {link(BREAK_EVEN, "fourplex unit-night break-even calculation")} or your property’s full cost model. For lender qualification, use {link("/financing/dscr-loans/", "the DSCR-versus-owner-cash-flow distinction")}. A definition page supplies neither an income forecast nor a loan decision.',
            ]),
        ],
        faqs=[('What does RevPAR stand for?', 'Revenue per available room. For a whole-property STR, state the adapted rentable-unit definition and use available unit-nights for the reporting period.'),
              ('Is RevPAR the same as ADR?', 'No. ADR divides lodging revenue by paid nights. RevPAR divides it by available nights, including available nights that were not sold.'),
              ('Does a higher RevPAR establish a better investment?', 'No. It excludes acquisition cash, financing and expenses. The hypothetical comparison shows higher RevPAR alongside lower contribution before fixed costs.')],
    ),
    OCCUPANCY: dict(
        title='Airbnb Occupancy Rates: Calculate and Underwrite | BNB Accelerator',
        h1='How do you calculate Airbnb occupancy rates before buying?',
        description='Reconcile paid, available and calendar nights before buying an Airbnb. See owner-block and seasonal examples, then compare occupancy with a cash threshold.',
        eyebrow='Availability and seasonal evidence', published='2026-08-10',
        lead='Airbnb occupancy is meaningful only with a stated period and availability policy. Calculate paid guest nights divided by available nights, and also show paid nights divided by calendar nights. A blocked date may be owner use, maintenance or a reservation; an unavailable listing calendar does not prove earned revenue.',
        sections=[
            ('Worked hypothetical: 80% occupied, 53.3% calendar utilization', [
                'Assume one 30-night month, with six owner-use nights and four maintenance nights excluded from availability. That leaves 20 available nights. If 16 guest nights are paid, reported available-night occupancy is 16 ÷ 20 = 80%; calendar utilization is 16 ÷ 30 = 53.3%. Neither number should hide the 10 excluded nights.',
                ('table', ['Reconciliation line', 'Nights'], [
                    ['Calendar inventory', '30'], ['Owner-use blocks', '6'],
                    ['Maintenance blocks', '4'], ['Available inventory', '20'],
                    ['Paid guest nights', '16'], ['Available but unsold nights', '4'],
                ]),
                'Keep booked future stays, fulfilled/earned stays, cancellations and owner blocks separately identifiable. If the system reports something different from paid occupied nights, keep that original definition beside the adjusted buyer metric. Do not count one night in two statuses.',
            ]),
            ('Build a seasonal forecast, then weight the annual totals', [
                'The following independent hypothetical uses one non-leap-year listing. Availability is after disclosed closures or owner use. The quarterly groups summarize a monthly worksheet; they are not market ranges or a guarantee that peak demand will pay for weak months.',
                ('table', ['Period', 'Calendar', 'Available', 'Paid', 'ADR', 'Lodging revenue'], [
                    [f'Quarter {i + 1}', str(q[0]), str(q[0] - q[1]), str(q[2]), money(q[3]), money(q[2] * q[3])]
                    for i, q in enumerate(OCCUPANCY_QUARTERS)
                ] + [['Annual total', '365', '346', '190', '$190.24 weighted', '$36,145']]),
                'Annual available-night occupancy = 190 ÷ 346 = 54.9%. Calendar utilization = 190 ÷ 365 = 52.1%. Weighted realized ADR = $36,145 ÷ 190 = $190.24. Add the nights and revenue first; do not average quarterly percentages or ADRs without their weights.',
                f'Combine rate and paid-night occupancy in the {link(REVPAR, "RevPAR definition and worked comparison")}. Then calculate expenses and monthly cash separately. Gross lodging revenue is not money available for distribution after costs.',
            ]),
            ('A forecast and a break-even threshold answer different questions', [
                f'A forecast asks what the evidence supports selling at each rate. A cash threshold asks what paid nights must cover the stated obligations. Use the {link(BREAK_EVEN, "fourplex break-even occupancy worksheet")} for the unit-night method; its 76.7% hypothetical threshold is not an occupancy prediction.',
                'Match seasonal comparables, authorized capacity, actual trip drivers and the proposed stay pattern. Put lower rates, more unsold nights and launch downtime into the same monthly cash forecast. A high annual occupancy percentage can still conceal an unfunded sequence of weak months.',
            ]),
            ('Request an occupancy file that can be reconciled', [
                ('ul', ['One property/listing identifier, currency, exact dates and report definitions.',
                        'Daily availability with reasons for owner, maintenance and legal-use closures.',
                        'Paid/fulfilled stays, cancellations, refunds and future reservations separated.',
                        'Monthly realized lodging rates and cost invoices for the same period.']),
                f'{link("/blog/reconcile-airbnb-payout-export/", "Verify the seller’s earnings and payouts")} rather than infer income from a calendar screenshot. Use the {link("/blog/str-purchase-to-launch-timeline/", "launch-delay cash plan")} to size liquidity against the maximum overlapping shortfall, not an unsupported “good occupancy” benchmark.',
            ]),
        ],
        faqs=[('What is a good Airbnb occupancy rate?', 'There is no universal percentage in this guide. Compare the same availability policy, realized rate, legal capacity and costs, then test the buyer’s monthly cash threshold.'),
              ('Should owner-blocked nights disappear from the analysis?', 'Show them separately. Excluding them from available nights changes reported occupancy; calendar utilization keeps the full-year capacity visible.'),
              ('Can I treat an unavailable competitor calendar as bookings?', 'No. It can contain owner use, maintenance, minimum-stay effects or other closures. Request reliable records and disclose what cannot be verified.')],
    ),
    PRICING: dict(
        title='BNB Accelerator Cost: Service Quote and Buyer Fit',
        h1='What does BNB Accelerator cost, and does the scope fit your purchase?',
        description='Request the actual BNB Accelerator fee and deliverables in writing. Separate service cost, property cash and reserves before choosing acquisition support.',
        eyebrow='Service quote and purchase readiness',
        lead='Get the current BNB Accelerator service fee, payment schedule and scope in writing before committing. A property budget is not a service quote. Keep the acquisition fee, cash invested in the property and retained operating reserve distinct, then decide which work the agreement performs and which decisions remain yours.',
        sections=[
            ('Worked hypothetical: $10,000 of quote and extra-cost headroom', [
                'Assume $200,000 is available for one buyer’s purchase plan. The property commitment is $165,000, consisting of $120,000 down payment, $15,000 closing/prepaids and $30,000 repairs/setup. Preserve a separate $25,000 operating reserve. The remaining amount is $200,000 − $165,000 − $25,000 = $10,000.',
                'That $10,000 is headroom for the actual service fee and every still-unquoted extra. It is not BNB Accelerator’s published price, a recommended fee or a minimum capital requirement. If the actual quote and extras exceed it, revise the property commitment or add available capital before treating the plan as funded.',
                f'For a coastal purchase, use the {link(COST, "beach-house acquisition cash example")} to see the property ledger’s separate categories. For any property, use the existing {link("/financing/closing-costs-and-reserves/", "closing and reserve worksheet")}. A fee paid at signing cannot simultaneously remain in the operating reserve.',
            ]),
            ('Ask for a proposal with inspectable deliverables', [
                ('table', ['Before signing, ask', 'Record in the agreement or purchase file'], [
                    ['What is the complete service price?', 'Total fee, due dates, triggers and refund/termination terms'],
                    ['What will I receive before approving a property?', 'Sourcing criteria, analysis, assumptions and approval steps'],
                    ['Which work is excluded or performed by others?', 'Broker, lender, counsel, inspection, insurance, design, management and tax costs'],
                    ['Who chooses vendors and authorizes spend?', 'Selection rights, referral relationships, change approvals and payment responsibility'],
                    ['What happens if a suitable property is not found?', 'Search scope, review dates, extension and exit remedies'],
                    ['What does launch completion mean?', 'Accepted inventory, listing/operating scope, remaining work and handoff records'],
                ]),
                f'Compare the scope against {link("/management/", "the management handoff responsibilities")}. Acquisition help does not itself settle ongoing management, lender approval, legal permission or tax treatment. Require the relevant professional’s own engagement and written answer.',
            ]),
            ('Bring a purchase brief that makes a fit decision possible', [
                ('ul', ['Available cash and the amount that must remain liquid after closing.',
                        'Financing status, borrower/property conditions and purchase timing.',
                        'Preferred property type, personal-use expectations and risk boundaries.',
                        'Any listing links, seller records, jurisdiction/HOA evidence and unresolved costs.',
                        'Owner time, local operating coverage and decisions you expect to retain.']),
                'A buyer ready to search can define these limits and obtain the missing records. A buyer expecting a guaranteed rental return, a preset deduction or a fully passive purchase should resolve those expectations before signing. Compare the written tasks with the work you would otherwise perform or contract separately.',
            ]),
            ('Use process evidence with its limits', [
                f'The {link(SOURCES["library"], "company-operated acquisition/process library")} contains reported purchase and coordination records. Such stories can show which diligence or handoff tasks arose, but do not verify rental returns or certify that every task is included in your proposal. Match the current scope to your own file.',
                f'{link("/how-it-works/", "Review the existing acquisition process")} and bring the quote questions to {link("/apply/", "a buyer strategy call")}. A conversation should identify the next decision and evidence needed, rather than replace written terms.',
            ]),
        ],
        faqs=[('Is there a fixed service price in this example?', 'No. Obtain the current actual fee and scope in writing. The hypothetical $10,000 figure is remaining budget capacity, not a company quote.'),
              ('Is the service fee included in a property’s down payment?', 'Treat it as a separate obligation unless the actual signed documents specify otherwise. Reconcile all payment dates and remaining liquidity.'),
              ('What should I bring to a pricing discussion?', 'Available cash, financing conditions, property/search criteria, timing, owner involvement and any listing or diligence records, plus the scope and fee questions above.')],
    ),
}


def curated_payload(path):
    """Supply content only for the eight explicit owners; preserve other routes."""
    data = PAGES.get(path)
    if data is None:
        return None
    import tpl
    from pillars import sections_html
    trail = [('Home', '/')]
    if path.startswith('/guides/'):
        trail += [('Guides', '/guides/'), ('STR purchase guides', '/guides/str-investment/')]
    elif path.startswith('/blog/'):
        trail += [('Blog', '/blog/')]
    elif path.startswith('/markets/'):
        trail += [('Markets', '/markets/')]
    elif path.startswith('/answers/'):
        trail += [('Definitions', '/answers/')]
    trail.append((data['eyebrow'], path))
    webpage = json.dumps({'@type': 'WebPage', '@id': tpl.SITE + path + '#webpage',
                         'url': tpl.SITE + path, 'name': data['h1'],
                         'description': data['description'], 'dateModified': REVIEWED})
    schema = tpl.graph(tpl.breadcrumb_schema(trail), webpage, tpl.ORG_SCHEMA) + '\n' + tpl.faq_schema(data['faqs'])
    if data.get('published'):
        schema += '\n' + tpl.article_schema(data['h1'], data['description'], tpl.SITE + path,
                                           data['published'], REVIEWED, section=data['eyebrow'])
    published = ('<span>Published ' + date.fromisoformat(data['published']).strftime('%B %d, %Y').replace(' 0', ' ') + '</span><span>&middot;</span>') if data.get('published') else ''
    sections = '\n'.join(sections_html([(heading, blocks)]).replace(
        '<div class="table-scroll">', '<div class="table-scroll" role="region" tabindex="0" aria-label="' + tpl.esc(heading) + ' table">')
        for heading, blocks in data['sections'])
    body = f'''<!-- buyer-intent-reviewed:2026-10-06 -->
  <section class="hero hero-page"><div class="wrap">
    {tpl.breadcrumb_html(trail)}
    <div class="hero-inner"><span class="eyebrow">{data['eyebrow']}</span>
      <h1>{data['h1']}</h1>
      <p class="hero-sub">{tpl.esc(data['description'])}</p>
      <div class="article-meta">{published}<span>Updated October 6, 2026</span></div>
    </div></div></section>
  <section><div class="wrap"><article class="article">
    <p class="lead">{data['lead']}</p>
{sections}
{tpl.faq_html(data['faqs'])}
{tpl.AUTHOR_BOX}
  </article></div></section>
{tpl.cta_band('Review the purchase before committing capital',
             'Bring the property, available cash and unresolved diligence questions to a buyer strategy call.',
             ('/apply/', 'Discuss My STR Purchase'), ('/underwriting/', 'Review the Purchase File'))}'''
    return dict(title=data['title'], description=data['description'], body=body,
                extra_schema=schema, body_class='blog',
                active='/markets/' if path.startswith('/markets/') else '/blog/')
