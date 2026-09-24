#!/usr/bin/env python3
"""Generate the FinCEN cash-STR acquisition diligence guide."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import blog

DATE = "2026-09-24"
SCORE = {
    "distinct_search_intent": 30,
    "buyer_relevance": 24,
    "real_question": 14,
    "service_fit": 14,
    "original_decision_support": 15,
}
assert sum(SCORE.values()) == 97

FAQS = "https://www.fincen.gov/rre-faqs"
QUICK_GUIDE = "https://www.fincen.gov/system/files/2025-12/General-Fact-Sheet.pdf"
REQUIREMENT_SHEET = "https://www.fincen.gov/system/files/RRE-Requirement-Fact-Sheet.pdf"

POST = {
    "slug": "fincen-cash-str-llc-reporting",
    "title": "FinCEN reporting for a cash STR purchase through an LLC",
    "title_tag": "FinCEN Cash STR Rules for LLC Buyers | BNB Accelerator",
    "h1": "Does FinCEN reporting apply when an LLC buys an STR with cash?",
    "description": "Does an LLC cash purchase of an STR require a FinCEN report? Use this 2026 decision tree to prepare ownership, signer, and payment records.",
    "date": DATE,
    "category": "Acquisition Diligence",
    "lead": "Usually, yes: a non-financed purchase of U.S. residential real estate by an LLC can fall under FinCEN's Residential Real Estate Reporting Rule when the closing occurs on or after March 1, 2026 and no exception applies. The closing or settlement professional normally files the Real Estate Report, but the buyer still has to provide complete entity, beneficial-owner, signer, and payment information. For a short-term-rental buyer, that makes reporting readiness a closing-workflow issue—not a reason to abandon an otherwise sound ownership structure.",
    "sections": [
        ("The direct answer for an STR buyer", [
            f"FinCEN's <a href=\"{QUICK_GUIDE}\" rel=\"noopener\">official quick-reference guide</a> uses a four-part test: the property is residential; the transfer is non-financed; the buyer is a covered entity or trust; and no exception applies. A one-to-four-family house, condominium, or similar residential unit does not stop being residential merely because the buyer plans to operate it as a short-term rental.",
            "An LLC buying the property with cash is the cleanest example of a potentially reportable transaction. The rule can also treat some credit-backed purchases as non-financed when the credit is not both secured by the acquired property and extended by a financial institution subject to the specified anti-money-laundering and suspicious-activity-reporting duties. Do not assume that seller financing, a private note, or other nonbank credit automatically removes the report.",
            ("callout", "Already comparing a cash, DSCR, or delayed-financing acquisition? <a href=\"/apply/\">Apply for a BNB Accelerator strategy call</a> and we can pressure-test the acquisition timeline, reserves, and operating case. Your title professional and attorney must determine the transaction's FinCEN obligations."),
        ]),
        ("Use this four-gate decision tree", [
            ("table", ["Gate", "Question", "Practical reading"], [
                ["1. Property", "Is the transferred interest U.S. residential real property?", "One-to-four-family homes, condos, co-ops, and certain residential development land can qualify."],
                ["2. Financing", "Does every transferee receive qualifying secured financing?", "An ordinary mortgage from a covered financial institution generally points away from reporting; cash and some nonbank credit point toward it."],
                ["3. Buyer", "Will an LLC, corporation, partnership, other covered entity, or trust take title?", "An individual buyer is generally outside this reporting rule; a qualifying LLC is not."],
                ["4. Exception", "Does a specific transfer or transferee exception apply?", "Use the actual exception and closing facts. Price alone is not an exception."],
            ]),
            f"If all four gates indicate coverage, treat the closing as reportable unless the reporting professional or counsel reaches a different conclusion from the specific facts. FinCEN's <a href=\"{REQUIREMENT_SHEET}\" rel=\"noopener\">buyer-facing requirement sheet</a> says the homebuyer does not file the report; a real-estate professional involved in settlement or closing does.",
            "That distinction matters operationally. The investor should not try to self-file in place of the reporting person, but should identify the reporting person early, answer the information request completely, and make sure entity documents, wiring instructions, and signing authority agree. A last-week entity change can alter the people and payment details that must be collected.",
        ]),
        ("What counts as non-financed", [
            f"The <a href=\"{FAQS}\" rel=\"noopener\">FinCEN Residential Real Estate FAQs</a> define a non-financed transfer by looking for qualifying credit extended to every transferee. The credit must be secured by the transferred property and come from a financial institution with the relevant AML-program and suspicious-activity-reporting obligations. A 50% down payment plus a qualifying mortgage to the only transferee is not treated the same as an all-cash closing.",
            "The trap is translating 'financed' in ordinary conversation into 'not reportable' under the rule. A seller note is financing in plain English, but it may not meet FinCEN's two-part lender-and-security test. The same caution applies to bridge money, private lenders, cross-collateralized credit, or financing issued to only one of several buying entities.",
            ("ul", [
                "Ask the settlement agent, in writing, whether the transaction is being treated as financed or non-financed under the FinCEN rule.",
                "Identify every transferee that will receive title; do not analyze only the lead LLC when multiple entities are buying.",
                "Give the reporting professional the lender's legal name and requested loan structure early enough to resolve classification before closing.",
                "Keep the financing analysis separate from the STR underwriting. A transaction can be reportable and still be financeable and economically sound.",
            ]),
        ]),
        ("What the LLC buyer should prepare", [
            "FinCEN places the filing duty on one reporting person selected by a reporting cascade or a written designation agreement. In a typical closing, that may be the settlement or closing agent. The buyer's job is to make the requested information accurate, consistent, and available before it becomes a scheduling problem.",
            ("ol", [
                "Confirm the exact legal name, trade name, jurisdiction, tax or other identifying number, and current principal-place-of-business address for each buying entity.",
                "Map each individual who directly or indirectly exercises substantial control or owns or controls at least 25% of the LLC. Beneficial ownership is measured as of closing.",
                "List each individual who will sign transaction documents for the entity and the capacity in which that person signs.",
                "Document total consideration and the source, amount, method, account, financial institution, and payor for relevant payments requested by the reporting person.",
                "Resolve any mismatch among the purchase contract, deed vesting, operating agreement, lender documents, wire sender, and signing resolutions.",
                "Ask who is the reporting person, whether a designation agreement is being used, and when the buyer's certification package is due.",
            ]),
            "Do not email sensitive identity or account information through an improvised thread simply because a deadline is close. Use the title, settlement, or legal professional's approved secure collection method and independently verify wire instructions. BNB Accelerator can coordinate the acquisition checklist, but it is not the FinCEN reporting person or the buyer's legal adviser.",
        ]),
        ("Worked example: an illustrative cash cabin purchase", [
            "Assume an investor signs a contract for an illustrative $625,000 cabin designed for one family and intends to operate it as a short-term rental. A newly formed LLC will take title. The LLC has two 50% members; one member signs the deed and settlement documents. The buyer plans to wire the purchase price without a mortgage.",
            "The property is residential, the transfer is non-financed, and an LLC is receiving title. Unless a specific exception applies, the transaction is likely within the reporting framework. The settlement team would identify the reporting person. Both 50% members meet the ownership threshold, and the signing member is also a signing individual. The reporting person—not the buyer—files the report, but the buyer supplies and certifies the requested information.",
            "Now change one fact: the LLC obtains a mortgage secured by the cabin from a financial institution that confirms it has the required AML and suspicious-activity-reporting obligations. That may move the transaction outside the non-financed definition. Change a different fact—replace the bank mortgage with a seller note—and the answer may move back toward reportable. The ownership vehicle alone does not decide the result.",
            "The $625,000 figure is illustrative, not a threshold or a statement about any BNB Accelerator acquisition. FinCEN says there is no sale-price threshold for this rule. Even a low-price or no-consideration transfer can require analysis.",
        ]),
        ("Exceptions and 1031 exchanges", [
            "Do not use a summary list as a substitute for the rule. FinCEN identifies transaction exceptions for certain transfers related to death, divorce, bankruptcy, court supervision, specified no-consideration transfers to trusts, transfers to a qualified intermediary for a Section 1031 exchange, and transfers with no reporting person. The transferee definitions also exclude specified regulated or publicly reporting entities.",
            "A 1031 exchange deserves special attention. FinCEN's FAQs explain that the transfer to the qualified intermediary may be excepted, while the later transfer from the qualified intermediary to the exchanger can remain potentially reportable when the exchanger is an entity or trust. 'It is a 1031' is therefore not a complete FinCEN analysis.",
            "Likewise, buying through a disregarded single-member LLC does not by itself create an exception. Federal tax classification and FinCEN's transferee-entity analysis answer different questions. Have the settlement professional or attorney apply the rule to the actual deed, buyer, financing, and transfer sequence.",
        ]),
        ("Timing, privacy, and the closing calendar", [
            "The rule applies to reportable transfers closing on or after March 1, 2026. FinCEN states that the filing deadline is the later of 30 calendar days after closing or the last day of the month following the closing month. That filing window belongs to the reporting person, but the buyer should not treat it as extra time to provide closing-critical information.",
            "The report can include identifying information about the property, transferee, beneficial owners, signing individuals, transferor, consideration, and certain payments. FinCEN says reports are stored in a secure, non-public database available only to authorized users. That does not remove the buyer's responsibility to use secure transmission practices with the closing team.",
            ("warn", "Legal boundary: this guide summarizes federal materials checked September 24, 2026. It is educational, not legal, tax, title, privacy, or compliance advice. FinCEN guidance can change, and state closing practices differ. Ask the reporting professional and qualified counsel to apply the current rule to the transaction."),
        ]),
        ("The acquisition-team handoff", [
            "Add a FinCEN line to the closing checklist as soon as the buyer, vesting, and capital stack are selected. The owner should be clear; the reporting professional should be named; the secure document channel should be known; and unresolved ownership or funding changes should have a decision deadline. That is enough to keep a reporting question from becoming a surprise without letting compliance paperwork crowd out property diligence.",
            "Continue the actual STR work in parallel: verify the address-level legal use, obtain a bindable insurance quote, reconcile seller revenue, test the downside case, confirm lender and reserve requirements, and build the opening operating plan. Review <a href=\"/blog/buy-str-entity-or-assets/\">whether the transaction is buying real estate or entity assets</a>, compare <a href=\"/blog/delayed-financing-cash-str/\">delayed financing after a cash purchase</a>, and use the <a href=\"/underwriting/\">BNB Accelerator underwriting framework</a> to keep the closing structure tied to the investment decision.",
            "If the structure remains unclear, pause the entity or funding change—not the evidence collection. Send counsel and the closing professional one concise fact pattern: property type, proposed transferee, ownership map, signing individual, financing source, lender status, transfer sequence, consideration, and closing date. A precise question gets a more useful answer than asking whether 'the new LLC rule' applies.",
        ]),
    ],
    "faqs": [
        ("Does FinCEN reporting apply when an LLC buys an STR with cash?", "Often yes. A non-financed transfer of U.S. residential real property to a qualifying LLC is reportable when no exception applies and the closing occurs on or after March 1, 2026. The settlement or closing professional should confirm the result for the actual transaction."),
        ("Does the STR buyer file the Real Estate Report?", "Usually no. FinCEN assigns filing to one reporting person in the closing and settlement cascade or through a written designation agreement. The buyer supplies complete and certified information requested by that reporting person."),
        ("Does a private or seller-financed loan avoid FinCEN reporting?", "Not automatically. Credit removes a transfer from the non-financed category only when it satisfies FinCEN's security and covered-financial-institution requirements for every transferee. Ask the reporting professional to classify the specific financing."),
        ("Is there a minimum purchase price for the rule?", "No. FinCEN states that neither property value nor sale price determines whether the transfer is reportable."),
        ("Is a 1031 exchange always exempt?", "No. The transfer to a qualified intermediary may be excepted, but the later transfer from the intermediary to an entity or trust can remain potentially reportable."),
    ],
    "related": [
        '<a href="/financing/">Compare STR financing structures</a>',
        '<a href="/blog/buy-str-entity-or-assets/">Buying the property versus the entity</a>',
        '<a href="/blog/delayed-financing-cash-str/">Delayed financing after a cash close</a>',
        '<a href="/underwriting/">Use the acquisition underwriting framework</a>',
        '<a href="/partners/">Coordinate with qualified advisers</a>',
    ],
    "cta_h": "Buying an STR through an LLC? Pressure-test the whole closing.",
    "cta_p": "BNB Accelerator can help source and underwrite the property, model the capital stack, and coordinate the acquisition checklist while your closing and legal professionals handle FinCEN compliance.",
}


if __name__ == "__main__":
    blog.build([POST])
    print(f"candidate score: {sum(SCORE.values())}/100 — {SCORE}")
