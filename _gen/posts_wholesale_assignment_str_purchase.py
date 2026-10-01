#!/usr/bin/env python3
"""Wholesale-assigned STR purchase financing, checked 2026-10-01.

Primary query: Can I finance a wholesale-assigned STR property purchase?
Gate: distinct intent 24/25; imminent buyer 30/30; search evidence 12/15;
acquisition service fit 19/20; original decision support 9/10 = 94/100.
Search evidence: BNBCalc's wholesale rental-investor guide and NightYield's
wholesale-assignment STR financing question. These establish intent only;
changing factual claims below use primary sources.
Distinct from the existing off-market sourcing page: this addresses a buyer
already evaluating an assigned contract, its loan basis and cash-to-close,
fee/deposit exposure, and the remaining time to establish lawful STR use.
Rejected this run: backup-offer topic (general-homebuyer intent); partnership
topic (existing STR partnership page); management-business purchase (service
fit below gate). No claimed query volumes, rankings, or performance.
"""

import blog


POSTS = [{
    "slug": "finance-wholesale-assigned-str-purchase",
    "title": "Financing a Wholesale-Assigned STR Property Purchase",
    "title_tag": "Finance a Wholesale STR Purchase | BNB Accelerator",
    "h1": "Can you finance a wholesale-assigned STR property purchase?",
    "description": "Buying an STR through a wholesale assignment? Check lender acceptance, assignment-fee cash, contract deadlines and legal rental use before committing.",
    "date": "2026-10-01",
    "category": "Financing",
    "lead": "A wholesale-assigned STR purchase may be financeable, but an attractive Airbnb projection does not establish that your lender will fund the transaction. Before paying an assignment fee or accepting a hard deposit deadline, send the lender and closing agent the original purchase contract, every amendment and assignment, the proposed settlement figures, and your intended short-term rental use. Get written answers on eligibility, the price used to size the loan, income documentation and required buyer cash. The immediate purchase decision is whether you can close with enough money left to make the property legally guest-ready and carry it through a slow opening. If the contract or loan terms leave that answer unresolved, preserve your diligence time or decline the assignment.",
    "sections": [
        ("Establish what you are buying before accepting the assignment", [
            ("callout", 'Have a wholesale STR deal in hand? <a href="/apply/">Book a call</a> with BNB Accelerator to compare the total acquisition cost, financing conditions and launch requirements before committing buyer funds.'),
            "In a simple assignment, the seller has agreed to sell to a contract holder, and you are offered that holder's purchase rights for a fee. A double closing has a different sequence: the intermediary buys and then resells. Ask which structure is actually proposed and which person or entity signs each document. A fee request or marketing sheet is not a complete transaction file. The <a href=\"/blog/find-off-market-str-properties-for-sale/\">off-market STR sourcing guide</a> explains how to find candidates; this guide starts after someone offers you a specific contract to acquire.",
            "Request the executed seller contract, amendments, assignment document, all additional fees, seller consent where required, title or escrow contact, access arrangements and deadlines. Have local counsel check assignability, seller authority, who is obligated to close, which buyer protections survive, and whether you can obtain documents and inspections before funds become exposed. Identify who holds each deposit, when it is refundable, when the assignment fee is earned and what happens if the seller, lender or title process prevents closing. Do not assume the assignment gives you a fresh inspection or financing period.",
            "Rules depend on the state. As one specific example, the <a href=\"https://www.oregon.gov/rea/Pages/Residential-Property-Wholesaling.aspx\" rel=\"noopener\">Oregon Real Estate Agency's wholesaling guidance</a> describes registration or licensing requirements and written disclosures to potential buyers before contracting. That example is a reason to check the applicable state agency and your documents, not a nationwide statement about licensing, cancellation rights or fee enforceability. Sources were checked October 1, 2026.",
        ]),
        ("Get a lender answer on both the contract chain and STR income", [
            "Ask the actual lender to review the proposed structure, rather than relying on the wholesaler's assurance that 'DSCR works.' A borrower preapproval does not necessarily approve this property, assignment, fee arrangement or closing date. Send the complete file and ask for a written eligibility decision, remaining conditions and the date by which those conditions can realistically clear. The lender and closing agent should see the same prices, fees, parties and documents.",
            ("table", ["Question to send before committing", "What the answer changes"], [
                ["Will this product accept this assignment or double closing, including the full chain of parties?", "Whether the proposed transaction can close with that lender"],
                ["What original price, resale price or appraised value sets the lending basis?", "Loan proceeds and the buyer's cash gap"],
                ["Can any assignment fee be financed, and how must it appear in the settlement documents?", "Cash needed beyond the ordinary down payment"],
                ["Does this purchase qualify using STR history, projections or long-term market rent?", "Whether the revenue evidence supports loan approval"],
                ["Are the property's condition, buyer entity and closing deadline eligible?", "Whether repair work or documentation requires another structure or delay"],
            ]),
            "One published product illustrates why these questions matter. <a href=\"https://www.epmwholesale.com/documents/EPM-DSCR-Prime-Guidelines.pdf\" rel=\"noopener\">EPM's DSCR Prime guidelines, version 11</a>, section 8.1, use the lower of the original contract purchase price or appraisal for an assignment and exclude the assignment fee from that price. Section 10.4 does not allow STR income on purchase transactions. These are terms of that published product, not universal DSCR rules or an offer of financing. Ask your lender for its current product terms and borrower-specific approval; a different lender may assess the deal differently.",
            "Keep qualification and investment underwriting separate. A loan sized on long-term market rent may still finance a property you plan to operate legally as an STR, but the lender must confirm the intended use and eligibility. Conversely, an accepted Airbnb projection does not prove that conservative net rental income will cover your expenses, debt and reserves. Use the <a href=\"/blog/reading-a-dscr-term-sheet/\">DSCR term-sheet checklist</a> and <a href=\"/blog/what-lenders-do-with-airdna/\">projection-documentation guide</a> to identify exactly which income figure the lender is using.",
        ]),
        ("Calculate the assignment cash gap before calling it a discount", [
            "An assignment fee is part of what you spend to acquire the deal even if the lender excludes it from the lending basis. Compare total cash through launch with the cash you can actually commit. Do not treat borrowing capacity, an estimated appraisal or a future refinance as available closing money. Budget fees separately until the lender confirms their treatment in writing.",
            "Illustrative model only, not a lender quote, market estimate or client result: assume a $400,000 original seller contract, a $20,000 assignment fee and a hypothetical 75% loan-to-value limit. Assume the appraisal is at least $420,000, but the selected lender sizes the loan on the original $400,000 price. The loan would be $300,000, leaving $100,000 toward the seller price plus the $20,000 fee. Applying 75% to the $420,000 total instead would incorrectly suggest $315,000 of loan proceeds and understate cash needed by $15,000.",
            ("table", ["Illustrative cash item", "Amount"], [
                ["Original seller price less modeled loan proceeds", "$100,000"],
                ["Assignment fee paid from buyer cash", "$20,000"],
                ["Other closing costs and prepaid items", "$12,000"],
                ["Repairs needed before hosting", "$25,000"],
                ["Furnishings and launch setup", "$20,000"],
                ["Cash retained as reserves", "$18,000"],
                ["Total modeled cash through launch", "$195,000"],
            ]),
            "Replace every number with property bids, settlement estimates, lender conditions and your launch plan. In this example, acquisition, closing, repairs and setup total $477,000 before retained reserves; a public-listing alternative should be compared on that same basis. Check whether the closing estimate includes lender fees, insurance and tax prepayments. Check separately how the lender verifies its required reserves. Avoid counting the same dollar as an assignment payment, renovation funding and a post-closing reserve.",
            "The fee is economically affordable only if the resulting total cost still supports your required outcome. For example, a cheaper seller contract can lose its advantage when the fee, urgent repairs and missed peak-season launch are included. Use <a href=\"/underwriting/cash-needed-to-buy/\">the acquisition cash framework</a>, compare a candidate in the same <a href=\"/markets/\">market</a>, and stress-test lower bookings and a delayed first guest with <a href=\"/underwriting/downside-scenario/\">the downside worksheet</a>. Paying a fee for access does not establish a property discount.",
        ]),
        ("Make lawful STR use and launch timing part of the commitment", [
            "The contract clock is especially important when the original buyer has already used much of the diligence period. Before accepting the assignment, map the remaining dates against the evidence you still need: parcel-level STR permission, HOA rules, permit availability or transfer treatment, insurable use, property condition, repair bids and the loan decision. Ask the municipality and association about your intended buyer and stay length. Have the responsible agent or attorney arrange a valid extension or condition where needed; verbal permission to 'take a few more days' is not your decision plan.",
            "If the home is advertised as an operating Airbnb, verify seller payouts and expenses through <a href=\"/underwriting/seller-financials/\">source records</a>. Also establish what happens to the listings, guest obligations and operating assets. <a href=\"https://www.airbnb.com/help/article/1431\" rel=\"noopener\">Airbnb's account-transfer guidance</a> says account ownership and reservations cannot be transferred between hosts or accounts. An assignment of a real estate contract does not resolve that platform issue. Price any required new listing and revenue ramp into the purchase, and use the <a href=\"/blog/buying-an-operating-str/\">operating STR diligence guide</a> for the broader handoff.",
            ("table", ["Finding", "Purchase response"], [
                ["Lender and closing agent accept the structure; buyer cash, lawful use and downside all clear", "Proceed within the reviewed contract terms"],
                ["A larger cash gap or verified repair/launch cost makes the current price fail", "Renegotiate the fee, price or permitted terms, then recheck financing"],
                ["A specific permit, title or lender answer is pending with a realistic resolution date", "Seek a documented extension or protection before committing funds"],
                ["Contract access is withheld, material fees are undisclosed, STR use is prohibited or cash runs out before launch", "Reject the proposed STR purchase"],
            ]),
            "Your next step is a short decision memo: total seller price and fees, lender-approved basis and proceeds, verified cash through launch, remaining diligence dates, earliest lawful guest date and the reason to proceed or stop. Bring the original contract and lender response to that review. <a href=\"/apply/\">Book a call</a> with BNB Accelerator to evaluate this STR acquisition and compare available alternatives. BNB Accelerator helps buyers find, underwrite, negotiate, close and launch properties; lender, legal and title determinations belong with the responsible professionals. This is educational information, not legal, tax, lending or investment advice. Financing, closing, permits, bookings and returns are not guaranteed.",
        ]),
    ],
    "faqs": [
        ("Can a DSCR loan finance a wholesale-assigned STR purchase?", "Possibly, depending on the lender, product, contract chain, property, intended use and borrower. Obtain written approval of the actual assignment and income documentation before committing funds; a generic DSCR preapproval is insufficient."),
        ("Can I include the assignment fee in my STR mortgage?", "Do not assume so. Some published products exclude it from the lending basis. Ask your lender to state its treatment, approved proceeds and required settlement disclosure, then budget any unfinanced fee as buyer cash."),
        ("Does a wholesale assignment restart the STR inspection period?", "Do not assume a new period. Review the original contract, amendments and assignment with local counsel or your responsible agent, including remaining deadlines, access, contingencies and deposit treatment."),
        ("When should I reject a wholesale Airbnb deal?", "Reject the proposed STR purchase when you cannot review the contract and fees, cannot verify lawful hosting, cannot fund closing and launch with adequate reserves, or cannot secure the necessary lender and title acceptance before commitment."),
    ],
    "related": [
        '<a href="/blog/find-off-market-str-properties-for-sale/">Find off-market STR candidates</a>',
        '<a href="/blog/str-property-wont-qualify-for-loan/">Check property-specific loan obstacles</a>',
        '<a href="/underwriting/permit-transfer/">Verify buyer permit rights</a>',
        '<a href="/blog/compare-two-str-properties-before-offer/">Compare the assignment with another property</a>',
    ],
    "cta_h": "Know what this wholesale STR purchase will require",
    "cta_p": "Review the contract structure, fee, cash through launch and legal rental use before deciding whether to buy.",
}]


if __name__ == "__main__":
    blog.build(POSTS)
