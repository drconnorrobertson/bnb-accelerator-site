#!/usr/bin/env python3
"""Buyer-side seller-financing decision for an imminent STR purchase."""

import blog


POSTS = [{
    "slug": "buy-str-with-seller-financing",
    "title": "Should You Buy an STR With Seller Financing?",
    "title_tag": "Buy an STR With Seller Financing? | BNB Accelerator",
    "h1": "Should you buy an STR with seller financing?",
    "description": "Seller financing for an STR purchase can change cash to close but add balloon and title risk. Compare terms, downside cash flow and an exit before offering.",
    "date": "2026-09-25",
    "category": "Financing",
    "lead": "Seller financing can help a purchase-ready short-term-rental buyer when a conventional or DSCR loan will not fund the property on workable terms. It does not make a weak STR a good investment. The seller becomes your lender for some or all of the price, so the note's down payment, interest, amortization, balloon, lien position and default terms can matter as much as the real-estate price. Before offering, compare the seller's proposed structure with a lender quote and a cash purchase, then underwrite the STR on conservative buyer revenue. If the only exit is a hoped-for refinance at a higher value, do not treat the lower cash to close as free buying power.",
    "sections": [
        ("Find out what the seller is actually offering", [
            "Ask whether the seller will deliver a deed at closing secured by a recorded note and mortgage or deed of trust, finance only a subordinate portion behind a new first loan, or propose an installment contract in which title transfers later. These are different legal and financing structures. The <a href=\"https://www.consumerfinance.gov/ask-cfpb/what-is-a-contract-for-deed-en-2149/\" rel=\"noopener\">Consumer Financial Protection Bureau's contract-for-deed explainer</a> describes the title-retention risk in that form; its consumer guidance may not apply identically to an investment-property transaction. Use local real-estate and lending counsel to identify the actual documents, applicable protections, title status, servicing and recording requirements. Do not sign a vague 'owner financing available' addendum.",
            ("callout", "Evaluating a seller-financed STR offer? <a href=\"/apply/\">Book a BNB Accelerator acquisition call</a> to compare the property's conservative cash flow and the actual note terms before committing your deposit."),
            "Have the title or closing professional identify every existing mortgage or lien, who will be paid off at closing, and the priority of any seller note. If a seller proposes leaving prior debt in place, have counsel and the existing lender assess consent, due-on-sale and default exposure before treating it as executable. Confirm that the buyer can insure the property for the intended STR use, obtain any required permit, and operate under HOA rules. Private financing cannot cure an illegal nightly-rental use. The <a href=\"/underwriting/permit-transfer/\">permit-transfer guide</a> covers that separate closing gate.",
        ]),
        ("Compare total purchase cash and debt, not just the rate", [
            "Request a written term sheet showing price, cash down, financed balance, stated and effective rate, payment schedule, amortization, maturity, balloon, prepayment, late fees, escrow treatment, insurance covenants, inspection or reporting rights, default and cure terms, and who pays legal and servicing costs. Have a qualified professional review it. Then compare it with at least one real lender path using the same price and a <a href=\"/underwriting/cash-needed-to-buy/\">cash-through-launch budget</a>. A lower down payment may preserve furniture and operating reserves, but a higher price or expensive note can erase that advantage.",
            ("table", ["Question", "Evidence needed", "Buyer decision affected"], [
                ["How much cash is truly needed?", "Down payment, closing statement, setup quotes, reserves", "Whether you can close and open without exhausting liquidity"],
                ["Can the STR service the note?", "Verified revenue, conservative expense and debt schedule", "Maximum offer and downside survival"],
                ["What is due at maturity?", "Amortization table, balloon date, extension terms", "Refinance or sale contingency plan"],
                ["Is title and lien position safe?", "Title commitment, payoff statements, recorded documents", "Whether the proposed structure is executable"],
            ]),
            "Illustrative only: a $500,000 STR with $100,000 down and a $400,000 seller note at 8% interest-only costs about $2,667 monthly in interest, or $32,000 annually, before taxes, insurance and principal repayment. If the note requires a $400,000 balloon in five years, that amount remains due even after five years of timely interest payments. Suppose hypothetical annual room and fee revenue is $90,000 and operating costs excluding debt are $30,000: the $28,000 remainder after interest must still cover capital repairs, taxes on income and reserves. At $70,000 revenue with the same costs, that remainder falls to $8,000. These numbers are invented to show the calculation, not a market benchmark, lender quote or client outcome.",
        ]),
        ("Stress the STR and the seller-note exit together", [
            "Model a weak first year, slower launch, higher insurance, a repair, and a soft booking season before deciding the payment is comfortable. If the note has a balloon, test whether a future refinance would work at lower property value, higher rates and more conservative lender income treatment. Ask a potential refinance lender now what evidence and seasoning it would need; that conversation does not guarantee future approval. The <a href=\"/blog/seller-financing-balloon-str/\">balloon stress-test guide</a> goes deeper on maturity risk. Keep enough cash to survive an operating shock without missing the private note payment.",
            "Seller financing may be attractive when the seller accepts a price and payment schedule that work on the verified STR case and the buyer has a credible maturity plan. It is not attractive merely because the monthly payment looks lower than a bank quote while principal is pushed into a balloon. Calculate your <a href=\"/blog/str-maximum-offer-price-from-revenue/\">maximum offer from supported revenue</a> first, then negotiate the note inside that price ceiling. Do not pay a large price premium for financing access without quantifying its cost against a bank loan or a different property.",
        ]),
        ("Set proceed, renegotiate, delay and rejection rules", [
            "Proceed only when title and lien review, legally permitted STR use, insurance, counsel-reviewed documents, downside debt coverage and the maturity plan all work at the negotiated price. Renegotiate price, down payment, amortization, maturity or security when the structure strains cash or creates a refinance cliff. Delay releasing contingencies while decisive payoff, title, legal or servicing information is missing under valid contract protection. Reject the deal if the seller will not document existing liens, the note gives no realistic exit, the property cannot be legally operated as an STR, or the downside case leaves inadequate reserves.",
            "Put the seller note and alternative lender quote on one acquisition sheet, including all cash through launch and the amount due at maturity. Have local counsel, the title company, your lender and tax adviser review their respective parts before signing. <a href=\"/apply/\">Book a call to evaluate a seller-financed STR acquisition with BNB Accelerator</a> if you want help sourcing, underwriting and negotiating the property. We cannot guarantee financing, legal use, bookings, refinancing or returns. This is educational information, not legal, tax, lending or investment advice.",
        ]),
    ],
    "faqs": [
        ("Is seller financing a good way to buy an Airbnb property?", "It can be when the price, down payment, note payment and maturity work on verified STR cash flow and qualified professionals approve the transaction structure. It is not a substitute for purchase due diligence."),
        ("Does seller financing let me skip STR permit or insurance checks?", "No. Verify address-specific legal use, HOA restrictions, insurance and title before removing purchase protection. A private note does not authorize rentals."),
        ("What if the seller-financed STR note has a balloon?", "Calculate the exact maturity balance and stress a refinance or sale under weaker value, rates and income. Do not assume refinancing will be available when the balloon comes due."),
        ("What documents should I request before offering?", "Request the written term sheet, draft note and security documents, title commitment, current mortgage payoffs, servicing proposal, seller financials and address-specific STR permission evidence for professional review."),
    ],
    "related": [
        '<a href="/underwriting/cash-needed-to-buy/">Budget cash through launch</a>',
        '<a href="/blog/seller-financing-balloon-str/">Stress-test a balloon</a>',
        '<a href="/blog/str-maximum-offer-price-from-revenue/">Calculate a maximum offer</a>',
        '<a href="/underwriting/permit-transfer/">Verify STR permission</a>',
    ],
    "cta_h": "Make the note fit the property—not the other way around",
    "cta_p": "We can compare seller financing with lender alternatives and test the STR's cash flow before you set the offer price.",
}]


if __name__ == "__main__":
    blog.build(POSTS)
