"""Reviewed content for six existing buyer-decision routes.

The blog and pillar renderers consult this module so legacy generators cannot
restore the old repeated copy. No routes or real client outcomes are invented.
Public source links were checked on 2026-10-06. Every worked example is hypothetical.
"""

REVIEWED = "2026-10-06"
LIBRARY = "https://www.bnbacceleratorreviews.co/case-studies"
SOURCES = {
    "balance": LIBRARY + "/sedona-az-2025-46",
    "capacity": LIBRARY + "/sevierville-tn-42",
    "handoff": LIBRARY + "/broken-bow-ok-46",
    "delay": LIBRARY + "/albrightsville-pa-47",
    "airbnb": "https://www.airbnb.com/help/article/3632",
    "dscr": "https://visiolending.com/resources/what-is-a-dscr-loan-how-rental-property-investors-qualify/",
    "denver": "https://www.denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Business-Licensing/Business-licenses/Short-term-rentals",
}


def link(path, label):
    return f'<a href="{path}">{label}</a>'


EVIDENCE_NOTE = (
    f'The {link(LIBRARY, "company-operated public evidence library")} lists 86 sanitized '
    'acquisition records, including 29 process stories, as checked on October 6, 2026. '
    'A recorded purchase, credit or handoff is evidence about a transaction. It does '
    'not establish a full-year rental return, transferable permission or a typical result.'
)

RELATED = [
    link("/blog/reconcile-airbnb-payout-export/", "Verify seller income"),
    link("/financing/closing-costs-and-reserves/", "Budget cash through launch"),
    link("/financing/dscr-loans/", "Separate lender DSCR from owner cash flow"),
    link("/blog/permits-that-do-not-transfer/", "Check permit and HOA transfer"),
    link("/blog/str-purchase-to-launch-timeline/", "Fund a delayed opening"),
    link("/management/", "Plan the management handoff"),
]

POSTS = {
    "reconcile-airbnb-payout-export": dict(
        title="Reconcile an Airbnb Payout Export Before Buying an STR",
        title_tag="Verify Seller Airbnb Income: Payout Reconciliation | BNB Accelerator",
        h1="How do you verify a seller's Airbnb income before buying?",
        description="Reconcile seller Airbnb charges, fees, refunds and deposits for one property and period, then separate historic income from buyer cash flow.",
        category="Revenue Evidence",
        lead="A seller's revenue claim becomes useful only when you can follow the same property's guest charges through refunds, fees and payouts to the money received. Request a full reporting period, explain timing differences, and identify expenses outside the platform. Even a reconciled payout total is not the buyer's profit or proof that the seller's permit, listing or reservations will transfer.",
        sections=[
            ("Request a property-specific evidence packet", [
                f'{link(SOURCES["airbnb"], "Airbnb explains its downloadable earnings reports")} and listing/date filters. Ask the authorized owner or manager for a listing-specific export, monthly statements and remittance evidence for the same start and end dates. A dashboard may combine paid transactions and future bookings; mark those separately. Use redacted records that retain amounts and dates without guest identities or unrelated bank activity.',
                ("ul", [
                    "Property/listing identifier, currency, exact reporting dates and whether the report follows stay dates or payout dates.",
                    "Reservation charges split into accommodation, cleaning and taxes; cancelled stays, refunds, chargebacks and adjustments.",
                    "Platform fees, co-host splits, manager deductions and any outstanding or scheduled payouts.",
                    "Property-level bank deposits or manager remittances and invoices for costs paid outside the platform.",
                ]),
                "A screenshot of booked nights cannot answer these questions. When the seller uses several channels, reconcile each separately before combining them. Exclude owner-blocked nights from occupancy and explain major outages; a closed calendar is not evidence of paid stays.",
            ]),
            ("Worked hypothetical: charges to deposits", [
                "This example uses invented amounts for one property and one completed twelve-month period. Assume the exported total includes separately identified taxes and no other adjustments. Your actual export may define gross earnings differently; map each column before subtracting anything.",
                ("table", ["Reconciliation step", "Amount"], [
                    ["Guest charges, including the separately listed items below", "$100,000"],
                    ["Less taxes collected and remitted separately", "−$8,000"],
                    ["Less refunds", "−$4,000"],
                    ["Less host fees", "−$3,000"],
                    ["Net amount due to the host", "$85,000"],
                    ["Less unpaid amount at period end", "−$2,000"],
                    ["Expected deposits for this period's activity", "$83,000"],
                ]),
                "Suppose matching bank receipts are $84,500. A $1,500 payout from the prior period explains the difference: $83,000 + $1,500 = $84,500. Keep that timing bridge rather than increasing current-period revenue. Cleaning fees included in charges are not free profit; subtract the actual cleaner cost in the expense model. Do not subtract a platform fee again if a manager statement already reports income net of it.",
            ]),
            ("Bridge reconciled income to the buyer model", [
                "Next subtract property-level management, cleaning, utilities, insurance, taxes, maintenance and other operating costs using invoices or quotes. Keep debt service and replacement reserves visible in the owner cash-flow model. Separate realized income, future reservations and estimates. One strong month does not establish an annual pattern, and a twelve-month report still may not reflect the buyer's financing or launch delay.",
                "Use a reservation-to-payout ledger to flag unmatched deposits, partial refunds and manager transfers. If a discrepancy is unexplained, show the amount as unverified and test the purchase without it. Reconciled historical income is one demand input; use a separate forward case for the buyer's permission, pricing, new listing, costs and capital requirements.",
                f'For an example of that distinction, {link(SOURCES["capacity"], "the public Sevierville process record")} discusses capacity documentation and reservation transition. It supplies no measured rental income. ' + EVIDENCE_NOTE,
            ]),
            ("A decision before the diligence deadline", [
                "Proceed when the property, period and cash bridge reconcile sufficiently for your price and financing. Reprice when verified income is materially lower than the seller claim. Seek a written extension through local counsel if a missing channel or manager packet can be obtained in time. Decline an income premium when the deal needs numbers the seller cannot substantiate.",
                "Save a one-page memo: claimed income, verified amount, timing adjustments, missing costs, transfer assumptions and the offer ceiling. Attach the reports and name who checked them. Bring that packet to the lender and accountant; do not replace it with a newly calculated client return drawn from an incomplete public case study.",
            ]),
        ],
        faqs=[
            ("Is an Airbnb payout the same as rental profit?", "No. It is a platform or manager cash receipt after specified deductions. Operating costs, debt service and reserves may still be unpaid."),
            ("Should bank deposits equal the earnings report?", "Reconcile them with a timing bridge. Prior-period receipts, unpaid payouts and refunds can make deposit dates differ from stay or transaction dates."),
            ("Can verified seller earnings prove my first-year return?", "No. Your permission, listing, financing, costs and opening date need a separate buyer model."),
        ],
    ),
    "permits-that-do-not-transfer": dict(
        title="STR Permit and HOA Transfer Checks Before Buying",
        title_tag="Does an STR Permit Transfer? HOA and Buyer Checklist | BNB Accelerator",
        h1="Will the seller's STR permit and HOA permission survive your purchase?",
        description="Check buyer eligibility, permit transfer, HOA restrictions and guest capacity before valuing an operating short-term rental's future bookings.",
        category="Regulations",
        lead="A deed, a local STR permit and an HOA's rental permission answer different questions. Establish whether the buyer can operate at the exact parcel, under the proposed ownership and guest capacity, before counting post-closing bookings. A seller's valid permit or a neighboring Airbnb listing does not establish the buyer's right to host.",
        sections=[
            ("Three approvals to check separately", [
                ("table", ["Evidence", "Buyer question", "Who confirms"], [
                    ["Government license and zoning", "Does ownership change require a new approval, and does this buyer qualify?", "Issuing authority and local counsel"],
                    ["Recorded covenants and HOA documents", "Are short stays allowed, capped or subject to an approval tied to the seller?", "Association records and local counsel"],
                    ["Occupancy and safety documents", "What guest count, bedrooms, parking and inspections are authorized?", "Controlling authority and qualified inspector"],
                ]),
                "Collect the current permit, holder name, parcel/unit, expiry, conditions and notices. Ask for the ownership-change procedure and earliest lawful operating date in writing. For an HOA, review recorded restrictions, amendments, rental caps, waiting lists, minimum stays, dues and pending changes; an agent's summary or a seller's past use is insufficient. Ask counsel which documents and contract protections apply before the review deadline expires.",
                f'{link(SOURCES["capacity"], "The published Sevierville record")} describes capacity documentation and a reservation transition. The stated capacity in that record requires a current local check; it is not a transferable approval for a different buyer or property.',
            ]),
            ("Worked hypothetical: a buyer approval gap", [
                "Assume, solely for this example, that the issuing office requires a new buyer application and the HOA allows the proposed use. A planned eight-week gap costs $800 per week in mortgage, utilities, insurance and dues. Application and inspection expenses add $1,200. Cash needed before permission is $6,400 + $1,200 = $7,600. An extra four weeks adds $3,200, bringing that modeled gap to $10,800.",
                "These are invented inputs, not a permitting timeline or a forecast. Model zero STR revenue during the unapproved interval. If the seller has $12,000 of future reservations during that period, do not offset the $7,600 with them. Confirm who remains responsible for those bookings and any refund or cancellation exposure; add a separate allowance if your documents put costs on the buyer.",
                "When no buyer approval is available, a longer delay allowance does not solve the issue. Revalue for another lawful use or reject the STR thesis. Any alternative rental use needs its own authority, financing and cash-flow check.",
            ]),
            ("Use geography precisely", [
                f'{link(SOURCES["denver"], "Denver’s licensing guidance")} ties STR operation to a primary residence. A Denver metro label does not answer the rules for a parcel in another municipality. Historical Colorado acquisition records and educational pages do not establish a current active acquisition service area or permission for a nonresident buyer. Confirm service availability separately from legal use.',
                "Apply the same address-specific discipline in any market: city versus county boundaries, subdivision covenants, unit configuration, ownership type and allowed guest count. Preserve useful historical records with their date and limits, and get a fresh response for the buyer's actual plan.",
            ]),
            ("Make permission a dated purchase decision", [
                ("ol", [
                    "Name the authority and association that control this address; retain the actual source documents.",
                    "State what must be approved again and who submits it; identify any capacity or use change.",
                    "Put the delivery date, review rights and remedy for an adverse answer in counsel-reviewed purchase terms.",
                    "Price the no-revenue interval, added costs and a denied-permission case before approving the offer.",
                    "Keep reservations closed for unauthorized dates; arrange a platform-compliant handoff separately.",
                ]),
                "A seller promise to help after closing is not a completed permission check. If the authority cannot decide before your contract deadline, assess an enforceable extension or an alternative property with local counsel. BNB can coordinate diligence; it cannot guarantee a permit, HOA approval or opening date.",
                EVIDENCE_NOTE,
            ]),
        ],
        faqs=[
            ("Does an STR permit transfer with the deed?", "That depends on the exact authority, permit and buyer. Obtain its ownership-change requirements and check private restrictions separately."),
            ("Can an HOA restriction override a city permit?", "Local permission does not establish compliance with private covenants. Review the applicable HOA and deed documents with local counsel."),
            ("Can I count seller bookings while my permit is pending?", "Model zero STR revenue until your own lawful operation and reservation arrangements are confirmed."),
        ],
    ),
    "str-purchase-to-launch-timeline": dict(
        title="STR Purchase-to-Launch Timeline and Delay Reserves",
        title_tag="STR Launch Delay: Timeline and Reserve Example | BNB Accelerator",
        h1="How much cash should you hold when an STR launch slips?",
        description="Map permit, repair and management dependencies from closing to first guest, then calculate launch carry and a separate operating reserve.",
        category="Buying Strategy",
        lead="Closing starts ownership costs; it does not establish an opening date. Build the schedule around the slowest required approval or vendor task and fund the period with no guest revenue. Keep launch carry separate from the cash cushion you intend to retain once the property is operating.",
        sections=[
            ("Build a dependency schedule, not a promised day count", [
                ("table", ["Gate", "Completion evidence", "Depends on"], [
                    ["Funding and possession", "Title confirmation and lawful access", "Loan, settlement and contract terms"],
                    ["Repairs and safety", "Agreed work verified and inspections completed", "Access, scope and contractor availability"],
                    ["Buyer permission and insurance", "Required approvals and coverage effective", "Authority, association and insurer"],
                    ["Furnishing and photography", "Installed inventory and accepted photos", "Access and completed repair work"],
                    ["Operating handoff", "Vendor coverage, listing setup and tested guest access", "Permission, insurance and manager readiness"],
                ]),
                "Assign an owner, dated evidence and a fallback to each gate. Some tasks can run in parallel, but a photo appointment cannot cure missing permission and a furnishing delivery cannot cure unsafe repairs. First guest availability starts after every required gate passes. A seasonal deadline is a planning goal, not evidence that a launch will meet it.",
                f'{link(SOURCES["delay"], "The public Albrightsville process story")} records repair discussion and a closing extension. It does not measure the subsequent launch delay or rental income. ' + EVIDENCE_NOTE,
            ]),
            ("Worked hypothetical: two months without guests", [
                "Assume the buyer closes while an approval and repair sequence remains outstanding. Fixed carry is $3,200 a month. Two zero-revenue months require $6,400; one-time launch/setup spending adds $5,000. A separately chosen operating cushion of three months of the same fixed carry is $9,600. Total cash for these three buckets is $21,000, beyond the down payment, closing costs and furnishing already budgeted.",
                ("table", ["Cash bucket", "Planned opening", "One month later"], [
                    ["No-revenue launch carry", "$6,400", "$9,600"],
                    ["One-time setup", "$5,000", "$5,000"],
                    ["Operating cushion retained at opening", "$9,600", "$9,600"],
                    ["Total for these buckets", "$21,000", "$24,200"],
                ]),
                "The additional month requires $3,200 of additional cash. Spending the $9,600 cushion to finish the launch leaves less protection for the first low season; it does not make the delay free. These invented inputs are not a recommended universal reserve or a local approval time. Deductible repairs, a major replacement and cancellation exposure require separate amounts if they are not included here.",
            ]),
            ("Stress the first operating season", [
                "Use twelve monthly buyer revenue figures based on the intended opening date. Recalculate if the delay removes peak-season weeks; do not shift the seller's full year into the remaining months. Test both low-season shortfalls and a repair shock. A lender's required reserves may overlap money you planned to hold, so distinguish required available cash, cash actually spent and the cushion left after launch.",
                "Mark each setup item as already funded, due before opening or optional. For repairs and furnishing, obtain scope, deposit, delivery and acceptance dates. For permission, distinguish an estimate from issued approval. When a task slips, update the dependent dates, the cash draw and the earliest bookable date in one decision file.",
            ]),
            ("A weekly opening review", [
                ("ul", [
                    "What gate currently controls opening, and what dated document will close it?",
                    "Which committed bookings could be affected, and who owns the authorized resolution?",
                    "What is cash spent to date, cash still committed and the remaining operating cushion?",
                    "Does the revised first-year model still justify the purchase and operating plan?",
                    "What triggers additional owner funding, a phased launch or an alternative lawful use?",
                ]),
                "Before making an offer, price a delayed-opening case you can fund without assumed guest receipts. Before opening, confirm permission, coverage, completed safety work, cleaners and guest access. After the first stays, compare actual statements with the dated launch model. Preserve the variance so the next purchase budget reflects what happened.",
            ]),
        ],
        faqs=[
            ("How many days does an STR take to launch?", "There is no universal period. Identify the controlling approval or vendor dependency and confirm every required gate before making dates available."),
            ("Is launch carry the same as an operating reserve?", "No. Launch carry funds spending before guests arrive. The operating cushion is money intended to remain available after opening."),
            ("Can future bookings fund my delayed opening?", "Do not assume they can. Until operation and payout timing are confirmed, plan the no-revenue interval with available owner cash."),
        ],
    ),
}

GUIDES = {
    "/financing/closing-costs-and-reserves/": dict(
        title="All-In STR Buyer Budget: Closing, Launch and Reserves",
        h1="What is the all-in cash budget to buy and launch an STR?",
        description="Build an STR buyer budget from down payment through closing, furnishing, launch carry and retained reserves, with a worked cash example.",
        eyebrow="Buyer Cash Budget",
        lead="Purchase price is not cash needed, and a down payment is only one use of cash. Reconcile the lender/title estimate to the final settlement statement, then add everything paid outside closing and the cushion you intend to keep. Label quoted amounts, allowances and unresolved costs separately so the offer uses a budget the buyer can actually fund.",
        sections=[
            ("Give every dollar one job", [
                ("ul", [
                    "Down payment: confirm price, loan proceeds and any deposit already paid.",
                    "Closing and prepaids: separate fees from tax/insurance escrow and confirm credits actually allowed and applied.",
                    "Furnishing and repairs: inventory included in the sale, replacement scope, delivery, labor and acceptance.",
                    "Launch: approvals, photography, supplies, vendor setup and cash carry before guests arrive.",
                    "Retained cash: lender requirements, low-season deficits, deductible exposure and replacement risk, with overlap identified.",
                ]),
                "Avoid subtracting earnest money twice: it is part of cash already contributed, while the final wire is the balance due. Avoid adding tax/insurance prepaids twice if they are already in the settlement estimate. A seller credit is not free cash to spend on furnishing; use only the application supported by the lender and signed settlement documents.",
            ]),
            ("Worked hypothetical: a $600,000 purchase", [
                "Assume a 25% down payment and the invented cash allowances below. These are planning inputs, not quoted program terms, fees or expected returns. The buyer will replace each allowance with current property-specific documentation.",
                ("table", ["Cash use", "Amount", "Evidence to replace assumption"], [
                    ["Down payment: 25% × $600,000", "$150,000", "Loan and price terms"],
                    ["Closing fees and prepaids", "$18,000", "Lender/title breakdown"],
                    ["Furnishing and installation", "$35,000", "Inventory and supplier scope"],
                    ["Repair allowance", "$8,000", "Inspection and contractor quote"],
                    ["Launch setup", "$4,000", "Permit, photography and supply costs"],
                    ["Two months of carry at $3,000", "$6,000", "Opening schedule and fixed costs"],
                    ["Cash cushion retained at opening", "$18,000", "Buyer downside plan"],
                    ["Total cash allocated", "$239,000", "Sum of the seven uses above"],
                ]),
                "If the buyer has $225,000 available, the gap is $14,000. A proposed $10,000 seller credit would leave $229,000 needed, and a $4,000 gap, only if the lender permits it and the final statement applies it against those budgeted costs. Until confirmed, retain the $239,000 case. A lower price also changes financing; recalculate the entire sheet rather than subtracting the price reduction from cash dollar for dollar.",
            ]),
            ("Reconcile cash-to-close before the wire", [
                f'{link(SOURCES["balance"], "The public Sedona closing story")} describes a final cash-to-close difference alongside a recorded seller-concession field. The story does not prove that the entire credit was applied. Keep the signed addendum, lender treatment and final settlement statement together. Confirm wire instructions through an independently verified title-company contact.',
                "For each variance, note whether it changes cash due now, cash due later or merely shifts a prepaid amount. Confirm loan proceeds, prorations, deposit credits, closing fees and the remaining wire with title. Separately total furnishing, repairs, launch and the remaining cushion; the title wire does not fund every line in an all-in buyer budget.",
                "Ashley and Billy's public case originally listed $220,800 of entry cost, while $63,000 down, $1,950 closing and $159,750 design sum to $224,700. That $3,900 discrepancy cannot be cured by choosing one total without the supporting statement. Use the evidence gap as a reconciliation lesson, not as a corrected client outcome.",
            ]),
            ("Approve a budget that survives a slower launch", [
                "Test a later opening, a smaller allowed credit and an uncovered repair. Show cash spent through opening and cash still on hand after it. A reserve transferred between two labels is still the same cash; disclose overlap rather than counting it as two cushions. If financing requires cash to remain available, ask how the lender verifies it and when it can be used.",
                "Keep operating reserves visible when comparing two properties. A smaller down payment can leave more cash available while increasing the payment; a larger furnishing allowance may improve the product while reducing the downside cushion. Compare the complete buyer cases and their dated quotes before setting an offer ceiling.",
                EVIDENCE_NOTE,
            ]),
        ],
        faqs=[
            ("Does cash-to-close cover the whole STR purchase budget?", "No. Add costs paid outside the settlement statement and the cash cushion intended to remain after opening; identify any overlap."),
            ("Can I subtract a seller credit from my furnishing budget?", "Only count the credit where the lender and final settlement documents permit and apply it. It is not automatically cash for furnishings."),
            ("What if case-study entry costs do not add up?", "Flag the difference, retain the source fields and request supporting records. Do not invent a corrected total or client return."),
        ],
    ),
    "/financing/dscr-loans/": dict(
        title="STR DSCR Underwriting Versus Investor Cash Flow",
        h1="Can an STR pass lender DSCR and still lose money for its owner?",
        description="Compare a lender's rent-to-PITIA DSCR with owner cash flow after management, operating costs and reserves using a worked STR example.",
        eyebrow="DSCR Underwriting",
        lead="Yes. A lender's qualifying ratio can omit costs that the owner must pay. Get the lender's exact income method and payment definition in writing, then build a separate cash-flow model using the buyer's revenue, operating expenses, financing and reserve needs. Loan approval is a financing result, not verification of rental profitability.",
        sections=[
            ("Identify which ratio the lender actually uses", [
                f'{link(SOURCES["dscr"], "Visio Lending’s published explanation")} uses monthly rent divided by principal, interest, taxes, insurance and association dues, or PITIA. That is one residential rental underwriting method. Other products can define income, deductions and the denominator differently; an NOI-to-debt-service ratio is a separate calculation. Do not mix the definitions or present one lender’s method as universal.',
                ("ul", [
                    "What income is credited: trailing property reports, an appraisal rent schedule or a third-party projection?",
                    "What discount, expense adjustment or seasonality treatment applies to STR income?",
                    "Which payment components are included, and what ratio does this quoted program require?",
                    "What borrower credit, liquidity, reserve, title and property requirements remain?",
                    "What fees, amortization, interest-only period and prepayment terms affect the buyer's hold?",
                ]),
                "Ask for the current term sheet for the specific borrower and property. Do not infer an accepted loan amount or interest rate from a published case, and do not rely on an old rate premium or ratio tier as a current offer.",
            ]),
            ("Worked hypothetical: 1.25 DSCR, negative owner cash", [
                "Assume this hypothetical lender credits $6,000 per month and defines the payment as $4,800 PITIA. Its ratio is $6,000 ÷ $4,800 = 1.25. Separately assume the buyer earns that same $6,000, with the costs below. None of these figures is a quote, underwriting approval or forecast.",
                ("table", ["Buyer monthly cash bridge", "Amount"], [
                    ["Revenue assumed available to the buyer", "$6,000"],
                    ["Management, cleaning, utilities, supplies and maintenance outside PITIA", "−$1,800"],
                    ["PITIA, with tax/insurance/dues counted here once", "−$4,800"],
                    ["Replacement reserve contribution", "−$300"],
                    ["Owner cash after these costs", "−$900"],
                ]),
                "The 1.25 ratio and negative $900 answer different questions. If operating costs remain fixed at $1,800, revenue must reach $6,900 to cover those costs, $4,800 PITIA and the $300 reserve contribution. If fees vary with revenue, solve using the actual variable-cost structure instead. Do not subtract property taxes or insurance a second time outside PITIA; show repairs and cleaner costs that are genuinely additional.",
            ]),
            ("Test the income evidence and the buyer period", [
                "A seller's trailing year may support demand without describing the buyer's first year. Confirm source records, dates, channels and refunds. For a projection, identify comparable properties, actual legal capacity, amenities and seasonality. Test the buyer's earliest opening date and a weaker revenue case. A lender accepting a source does not reconcile missing expenses for the investor.",
                "Keep qualifying income, buyer forecast and realized operating income in separate columns. Model each month rather than annual rent divided by twelve when demand is seasonal. Debt service starts according to loan terms even if permission, furnishing or a manager transition delays guests. Include the no-revenue interval in the cash budget as well as the ratio review.",
            ]),
            ("Choose financing against the complete hold", [
                "Compare the actual conventional, DSCR or portfolio quotes available to you. Include origination, closing costs, rate, loan size, reserve requirements and an early-exit cost. Entity ownership and personal guarantees need written lender confirmation. Lower initial payments can be accompanied by a later payment change; model the relevant years and the proposed exit rather than only the opening month.",
                "Proceed when financing fits the borrower and the independently supported owner model fits the buyer's downside and cash limits. Reprice or reduce leverage when those limits fail. Do not rescue a weak operating case with an assumed refinance, appreciation or tax refund.",
                EVIDENCE_NOTE,
            ]),
        ],
        faqs=[
            ("Does 1.25 DSCR guarantee positive owner cash flow?", "No. A rent-to-PITIA ratio can omit management, cleaning, utilities, maintenance and reserves. Calculate owner cash separately."),
            ("Do all DSCR lenders use the same Airbnb income?", "No. Obtain the specific income source, adjustments and ratio definition for the current quoted program."),
            ("Should I deduct taxes and insurance again after PITIA?", "Do not double-count them. Identify costs already included in the payment and show genuinely additional costs separately."),
        ],
    ),
    "/management/": dict(
        title="STR Management Handoff: Reservations, Fees and Owner Controls",
        h1="How do you hand an operating STR to a new manager?",
        description="Reconcile future reservations, payouts, manager fees and guest responsibilities at an STR purchase, with a hypothetical handoff and fee comparison.",
        eyebrow="Management Handoff",
        lead="Treat management selection and the closing handoff as separate decisions. Choose a manager on the written scope and complete cost, then map who owns each reservation, payout, guest response and vendor task on either side of closing. A signed deed does not itself transfer a platform account, listing history or a manager agreement.",
        sections=[
            ("Write a reservation and responsibility register", [
                f'{link(SOURCES["handoff"], "The public Broken Bow handoff story")} records communication between incoming and outgoing managers about reservations alongside lending and closing work. It establishes a process dependency, not successful future stays or rental returns. Build your own handoff against the actual platform, contract and manager rules.',
                ("table", ["Register field", "What to resolve before closing"], [
                    ["Channel and stay dates", "Which operator can legally service each stay, especially one spanning closing?"],
                    ["Charges and cash already received", "Who holds deposits and who owes the guest service or refund?"],
                    ["Payout timing and deductions", "Who receives each payout and how are costs reconciled?"],
                    ["Guest communication", "Who is authorized to explain any change and handle urgent issues?"],
                    ["Listing and access", "Which accounts, permissions, photos and licenses can be used by the buyer?"],
                    ["Turnover and repairs", "Named cleaner, backup, access test and acceptance of outstanding work"],
                ]),
                "Use reservation references without publishing guest identities. Ask the platforms and managers how the intended arrangement is supported; do not assume accounts or reviews can be assigned with the sale. Have counsel document cancellation, refund, payout and post-close reconciliation responsibilities. Separate a future booking from cash received or an obligation satisfied.",
            ]),
            ("Worked hypothetical: booked value is not handoff cash", [
                "Assume $15,000 of gross future stays are on the seller's calendar. Of that, $6,000 has already been received and $9,000 remains scheduled. This proves neither that $15,000 transfers nor that any of it is buyer profit. If the authorized transition leaves the outgoing operator responsible for stays and refunds, the buyer cannot simply book that total as opening cash. Reconcile each obligation and the permitted settlement adjustment with counsel and the managers.",
                "For a separate hypothetical fee comparison, assume both managers would produce the same $60,000 annual rental revenue and exclude identical pass-through cleaning costs. Manager A charges 20% plus $3,000 of quoted annual extras: $12,000 + $3,000 = $15,000. Manager B charges 25% including those same services: $15,000. The headline percentages differ; this scope's modeled cost is equal. Revenue and service quality remain assumptions requiring their own evidence.",
                "Request comparable-property statements with a consistent period and cost definition, references you can evaluate through an authorized process, and a fee schedule covering setup, maintenance coordination, minimums and termination. A lower advertised percentage is not enough to choose between different scopes.",
            ]),
            ("Give the buyer controls from day one", [
                ("ul", [
                    "Written account/listing ownership and permission arrangements consistent with platform rules.",
                    "Authority to approve maintenance above a specified amount and a separate emergency process.",
                    "Owner access to property-level statements, deductions, invoices and reservation status.",
                    "Cleaner and backup coverage, photo checks, tested locks and a local emergency contact.",
                    "Clear notice, termination and data/export terms so changing managers can be planned.",
                ]),
                "Record which tasks the owner actually performs. Management structure can affect tax participation questions, but a manager's service tier or promised hours does not establish a tax result. Have the owner's tax adviser review the actual facts separately; do not add an assumed tax refund to handoff funding.",
            ]),
            ("Close the loop after the first statements", [
                "Before the first buyer-controlled guest arrives, confirm lawful operation, coverage, safe access, cleaning and an escalation owner. After the first payouts, compare each reservation against the transition register and investigate missing money or duplicated charges. Close the seller-manager reconciliation under the documented terms and retain the final packet.",
                "Keep a dated list of open repairs and vendor tasks. A process story mentioning a walkthrough or guest complaint does not certify that a problem was permanently repaired. Require acceptance evidence for your own property, and fund remaining work from the buyer budget rather than assumed future bookings.",
                EVIDENCE_NOTE,
            ]),
        ],
        faqs=[
            ("Do a seller's Airbnb reservations automatically become mine?", "No. Verify the actual platform, legal-use, manager and purchase arrangements for each stay, payout and guest obligation."),
            ("Is a 20% manager cheaper than a 25% manager?", "Compare the same services and revenue basis with all extras. The hypothetical $60,000 example has equal $15,000 costs at those two different headline rates."),
            ("What should be checked after the handoff?", "Match the first reservation and payout statements to the transition register, verify outstanding work and document any seller-manager reconciliation."),
        ],
    ),
}


def curated_post(post):
    """Preserve publication history while replacing a reviewed route's content."""
    content = POSTS.get(post["slug"])
    if content is None:
        return post
    return dict(post, **content, modified=REVIEWED,
                related=[item for item in RELATED if f'/blog/{post["slug"]}/' not in item],
                cta_h="Bring the property and the evidence to a buyer strategy call",
                cta_p="Review the income packet, cash budget and unresolved launch decisions before committing capital.")
