#!/usr/bin/env python3
"""Generate the FIRPTA closing guide for short-term-rental buyers."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import blog

DATE = "2026-09-24"
SCORE = {
    "distinct_search_intent": 30,
    "buyer_relevance": 24,
    "real_question": 15,
    "service_fit": 13,
    "original_decision_support": 14,
}
assert sum(SCORE.values()) == 96

FIRPTA = "https://www.irs.gov/individuals/international-taxpayers/firpta-withholding"
EXCEPTIONS = "https://www.irs.gov/individuals/international-taxpayers/exceptions-from-firpta-withholding"
FORM_8288 = "https://www.irs.gov/instructions/i8288"
PUB_515 = "https://www.irs.gov/publications/p515"

POST = {
    "slug": "firpta-foreign-seller-str-buyer",
    "title": "FIRPTA for STR buyers purchasing from a foreign seller",
    "title_tag": "FIRPTA for STR Buyers: Foreign-Seller Closing Guide",
    "h1": "What should an STR buyer do when the seller is a foreign person?",
    "description": "Buying an STR from a foreign seller? Use this FIRPTA closing guide to verify status, calculate withholding, handle Form 8288, and protect the timeline.",
    "date": DATE,
    "category": "Acquisition Diligence",
    "lead": "Treat FIRPTA as a buyer-side closing obligation, not merely the foreign seller's tax problem. When a foreign person disposes of U.S. real property, the buyer is generally the withholding agent and may be held liable if the required amount is not withheld and remitted. For an investment property that will operate primarily as a short-term rental, the general starting rate is 15% of the foreign seller's amount realized—not 15% of estimated gain. The right workflow is to establish seller status, identify any valid exception or IRS withholding certificate, calculate the correct base, and assign the filing mechanics before money moves.",
    "sections": [
        ("The direct answer for an STR buyer", [
            f"The IRS <a href=\"{FIRPTA}\" rel=\"noopener\">FIRPTA withholding guidance</a> says the buyer is the withholding agent in most direct real-estate purchases from a foreign person. The buyer must determine whether the seller is foreign. If withholding applies and the buyer fails to do it, the IRS may collect the tax from the buyer. A title or closing company can administer the process, but delegating the paperwork does not justify leaving the issue undocumented.",
            "Do not wait for closing week. Ask for the seller's nonforeign-status certification or disclosure early enough for the closing professional and tax counsel to evaluate it. If the seller is foreign, add FIRPTA to the contract-to-close schedule alongside title, financing, insurance, inspection, STR legality, and entity documents. A reduced-withholding request can affect when funds may be released and when the transaction team can finish its federal filings.",
            ("callout", "Reviewing an operating STR or vacation home with an unusual seller or closing structure? <a href=\"/apply/\">Apply for a BNB Accelerator strategy call</a> to pressure-test the acquisition and closing calendar. A qualified FIRPTA tax professional and closing attorney should determine and execute the withholding treatment."),
        ]),
        ("Use this five-gate FIRPTA decision tree", [
            ("table", ["Gate", "Question", "Buyer evidence"], [
                ["1. Asset", "Is the buyer acquiring a U.S. real property interest?", "Deed, legal description, allocated personal property, and transaction structure."],
                ["2. Seller", "Is each transferor a foreign person for FIRPTA purposes?", "Valid certification of nonforeign status or documented foreign status for every seller."],
                ["3. Exception", "Does a withholding exception actually apply?", "The specific certification, IRS certificate, or other required notice—not an oral assurance."],
                ["4. Amount", "What amount is realized and what rate applies?", "Cash, property transferred, assumed liabilities, joint-owner allocation, and applicable rate support."],
                ["5. Execution", "Who withholds, files, remits, and retains proof?", "Written closing instructions, Forms 8288 and 8288-A, deadlines, payment evidence, and file retention."],
            ]),
            "Stop at the first unresolved gate. Seller nationality, mailing address, visa status, and the LLC name on the deed are clues, not substitutes for the federal definitions and required documents. A resident alien is not a foreign person for this rule, while a foreign corporation, foreign partnership, foreign trust, foreign estate, or nonresident alien can be. A disregarded entity generally cannot certify itself as the transferor; its owner is treated as the transferor for this purpose.",
            "The transaction form matters too. A direct property purchase is not necessarily analyzed the same way as buying equity in an entity that owns the STR. If the proposal involves an entity-interest purchase, assignment, exchange, trust, or seller-financing structure, have counsel identify the applicable withholding regime before reusing a standard property-closing checklist.",
        ]),
        ("Why the withholding base can surprise buyers", [
            "FIRPTA generally starts with 15% of the foreign person's amount realized. The IRS defines amount realized as the cash paid or to be paid, the fair market value of other property transferred, and liabilities assumed by the buyer or to which the property remains subject. That is materially different from multiplying the rate by the seller's expected taxable gain, net proceeds, or equity check.",
            ("ul", [
                "Include assumed or property-level liabilities when the federal definition requires them; do not use only the buyer's cash at closing.",
                "When U.S. and foreign owners sell jointly, allocate amount realized among transferors using the applicable capital-contribution method before calculating the foreign portion.",
                "Treat furniture or other associated personal property carefully. A sale allocation does not automatically remove it from the U.S. real-property-interest analysis.",
                "Do not reduce withholding because commissions, debt payoff, or other closing charges leave the seller with less cash unless authoritative guidance or an IRS certificate supports the reduction.",
            ]),
            f"The current <a href=\"{FORM_8288}\" rel=\"noopener\">Form 8288 instructions</a> require the buyer or other transferee to complete the applicable section, attach a Form 8288-A for each person subject to withholding, and generally file and transmit the tax by the 20th day after the transfer. Penalties can apply, and the tax plus interest may be collected from a buyer that failed to withhold.",
        ]),
        ("The residence exception usually does not fit a pure STR acquisition", [
            f"The IRS <a href=\"{EXCEPTIONS}\" rel=\"noopener\">exceptions page</a> describes a no-withholding rule for an individual who buys for use as a residence when the amount realized is $300,000 or less. The individual or qualifying family member must have definite plans to reside there for at least 50% of the days anyone uses the property during each of the first two 12-month periods; vacant days are ignored. The Form 8288 instructions also describe a 10% rate for a qualifying residence purchase of $1 million or less.",
            "Those are residence rules, not discounts available simply because the asset is a house. An LLC buyer does not qualify for the $300,000 residence exception, even if an individual owns the LLC. An individual planning predominantly guest use may fail the 50%-of-used-days test. A buyer should never promise personal-use days on paper while the underwriting, management agreement, and listing calendar show a full-time rental plan.",
            ("warn", "Do not assume a sub-$300,000 STR is exempt or a sub-$1 million STR gets 10% withholding. The residence-use and buyer-status conditions must be satisfied. Have the closing tax professional document the conclusion from the actual vesting and intended use."),
        ]),
        ("Certifications and withholding certificates solve different problems", [
            "A valid certification of nonforeign status supports a conclusion that FIRPTA withholding is not required because the seller is not foreign. It generally includes the transferor's name, U.S. taxpayer identification number, address, and a statement signed under penalties of perjury. The seller may provide it to the buyer or to a qualified substitute, such as a qualifying closing attorney or title company, which then gives the buyer the required statement.",
            "A withholding certificate is different. If the seller is foreign but the standard withholding would exceed the seller's maximum tax liability, the buyer or seller may ask the IRS to reduce or eliminate withholding. Form 8288-B is used in many such cases. The IRS says it will normally act by the 90th day after receiving a complete application, which makes early preparation a real closing-timeline issue.",
            f"Filing an application does not mean the buyer can release all proceeds. The IRS <a href=\"{PUB_515}\" rel=\"noopener\">Publication 515</a> and Form 8288 instructions explain the timing mechanics. When a proper application is submitted on or before transfer, the buyer still withholds, but the filing and remittance deadline can be deferred until the 20th day after the IRS mails its certificate or denial. Counsel and escrow should document where the withheld funds remain and the release conditions.",
        ]),
        ("Worked example: a $720,000 investment cabin", [
            "Assume an illustrative buyer LLC contracts to acquire a U.S. cabin and furnishings for $720,000 from one foreign individual. The buyer plans to operate it as a full-time short-term rental. No exception or IRS withholding certificate has been established by closing, and assume the full $720,000 is the amount realized for this simplified example.",
            "The residence exceptions do not fit the stated facts: the buyer is an LLC and the intended use is investment lodging. At the general 15% rate, the illustrative withholding is $108,000. That figure is based on amount realized, not the seller's projected gain or cash after paying a mortgage. The settlement statement should show the withholding treatment, but the buyer's file also needs the underlying status documentation, completed forms, remittance responsibility, deadline, and proof of delivery.",
            "Now add one fact: before closing, the seller submits a complete Form 8288-B showing that the statutory withholding materially exceeds maximum tax liability. That application does not let the team improvise a lower number. Escrow holds the otherwise required amount, and the team follows the federal timing and the eventual IRS determination. If the contract cannot tolerate that hold, the issue belongs in negotiation before contingencies expire.",
            "The purchase price, allocation, $108,000 result, and facts are illustrative—not a report of a BNB Accelerator transaction or a universal calculation. Liabilities, multiple sellers, transaction structure, certifications, and an IRS certificate can change the result.",
        ]),
        ("Put FIRPTA into the contract-to-close schedule", [
            ("ol", [
                "Identify every legal transferor and the federal tax owner of any disregarded seller entity; do not review only the signature block on the listing agreement.",
                "Require the appropriate foreign-status disclosure or certification by a dated contract milestone, with a process for the qualified substitute to hold protected tax information.",
                "Name the FIRPTA tax professional and the closing party performing the calculation, forms, remittance, and post-closing evidence package.",
                "Calculate amount realized from the contract, assumed liabilities, ownership allocation, and included property; reconcile it to the settlement statement.",
                "If reduced withholding is requested, establish the Form 8288-B filing date, escrowed amount, IRS correspondence recipient, release standard, and outside timing plan.",
                "Confirm Forms 8288 and 8288-A, payment method, federal deadline, and proof-retention owner before authorizing disbursement.",
                "Check for separate state nonresident-seller withholding rules. Federal FIRPTA compliance does not establish state compliance.",
            ]),
            "The cleanest handoff is a one-page responsibility matrix signed off by the buyer's attorney or tax adviser and the closing professional. It should answer who verifies status, who calculates, who controls the funds, who signs each form, who remits, who receives IRS mail, and who gives the buyer the final evidence package. 'Title is handling it' is not a control unless the title company confirms exactly what that means.",
        ]),
        ("Failure modes that put the buyer at risk", [
            ("ul", [
                "Treating the seller's foreign status as confidential information the buyer has no need to resolve, even though the buyer is generally the withholding agent.",
                "Calculating 15% of gain, net proceeds, or seller equity instead of testing the federal amount-realized definition.",
                "Applying the $300,000 exemption or 10% rate to an LLC-owned or predominantly rental STR without satisfying residence conditions.",
                "Accepting a certification that does not come from the tax owner, lacks required information, or conflicts with known facts.",
                "Assuming a pending Form 8288-B permits release of the withheld funds before the IRS determination.",
                "Closing without assigning the 20-day filing and remittance work or retaining objective proof that it happened.",
                "Solving federal withholding while overlooking a separate state foreign- or nonresident-seller withholding rule.",
            ]),
            ("warn", "Tax and legal boundary: this guide summarizes federal IRS materials reviewed September 24, 2026. It is educational, not tax, legal, escrow, title, accounting, or investment advice. FIRPTA is fact-specific, state rules are separate, and forms and guidance can change. Use a qualified cross-border tax professional and closing attorney."),
        ]),
        ("Keep the tax workflow connected to the investment decision", [
            "FIRPTA usually changes closing execution, not the property's operating potential. Still, an unresolved seller-status issue, cash holdback, delayed certificate, or weak contract can create timing and liquidity risk. Add those effects to the deal calendar and reserve plan rather than pretending they sit outside underwriting.",
            "Continue the property work in parallel: verify address-level STR use, review the permit transfer, test seller revenue, inspect life-safety systems, bind insurance, and model debt and reserves. Use the <a href=\"/underwriting/\">BNB Accelerator underwriting framework</a>, review <a href=\"/blog/buy-str-entity-or-assets/\">whether you are buying the property or entity assets</a>, and avoid <a href=\"/blog/closing-before-peak-season-str/\">rushing a closing merely to catch peak season</a>.",
            "Before releasing funds, ask for one closing memo that states the seller-status evidence, applicable exception or rate, amount-realized calculation, withheld amount, forms, remittance deadline, responsible party, and evidence location. That memo gives the buyer, adviser, and future file reviewer the same answer—and exposes any missing decision while it can still be fixed.",
        ]),
    ],
    "faqs": [
        ("Is the STR buyer responsible for FIRPTA withholding?", "In most direct purchases from a foreign seller, the buyer is the withholding agent. A closing company may administer the process, but the IRS can hold the buyer liable when required withholding is missed."),
        ("Is FIRPTA 15% of the foreign seller's profit?", "Generally no. The starting calculation is 15% of amount realized, which can include cash, transferred property, and assumed liabilities. It is not simply the seller's gain or net equity."),
        ("Does the $300,000 residence exception apply to an investment Airbnb?", "Usually not on pure-investment facts. It requires an individual buyer and definite plans for the buyer or qualifying family to reside there for at least 50% of the days anyone uses it during each of the first two 12-month periods."),
        ("What are Forms 8288 and 8288-A used for?", "The buyer or other transferee uses Form 8288 to report and transmit FIRPTA withholding, with Form 8288-A prepared for each foreign person subject to withholding. The general deadline is the 20th day after transfer, subject to specific certificate timing rules."),
        ("Can a pending Form 8288-B reduce the amount released at closing?", "A pending application does not itself authorize an improvised reduction. When timely filed, the otherwise required amount is withheld while remittance can be deferred until the IRS acts. Escrow and counsel should document control and release of the funds."),
    ],
    "related": [
        '<a href="/blog/buy-str-entity-or-assets/">Choose between a property and entity-asset purchase</a>',
        '<a href="/blog/closing-before-peak-season-str/">Avoid rushing the closing for peak season</a>',
        '<a href="/blog/the-first-30-days-checklist/">Sequence the first 30 days after closing</a>',
        '<a href="/underwriting/">Use the acquisition underwriting framework</a>',
        '<a href="/partners/">Coordinate with qualified advisers</a>',
    ],
    "cta_h": "Buying an STR with a complex seller or closing structure?",
    "cta_p": "BNB Accelerator can help source and underwrite the property, pressure-test the acquisition calendar, and coordinate diligence while qualified tax, legal, title, and escrow professionals execute FIRPTA compliance.",
}


if __name__ == "__main__":
    blog.build([POST])
    print(f"candidate score: {sum(SCORE.values())}/100 — {SCORE}")
