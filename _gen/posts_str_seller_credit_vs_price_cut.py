#!/usr/bin/env python3
"""Offer-stage cash-versus-basis choice for a financed STR buyer."""

import blog


POSTS = [{
    "slug": "str-seller-credit-vs-price-reduction",
    "title": "STR Purchase: Seller Credit or Lower Price?",
    "title_tag": "STR Seller Credit vs Price Reduction | BNB Accelerator",
    "h1": "Should an STR buyer ask for a seller credit or a lower price?",
    "description": "Buying an STR? Compare a seller credit with a price reduction using cash to close, lender limits, launch reserves and long-term debt before you negotiate.",
    "date": "2026-09-25",
    "category": "Buying Strategy",
    "lead": "For a short-term-rental buyer, a seller credit and an equal price reduction are not interchangeable. A usable credit can reduce the cash due at closing and leave more money for the launch, but it usually does not lower the purchase price or loan balance. A price cut lowers the amount financed and may improve long-term economics, yet it can free less cash immediately. The better request depends on your loan program, the lender's allowed uses and cap, the actual closing charges, appraisal, down payment, and the capital you still need for furnishings, permits and reserves. Compare both offers on the same written lender worksheet before you negotiate—not on the headline concession alone.",
    "sections": [
        ("Get the lender's usable-credit number first", [
            "Ask the lender to run two transaction scenarios for the specific STR purchase: the proposed price with a seller-paid closing-cost credit, and the lower price without one. Request projected cash to close, loan amount, payment, appraisal treatment, eligible charges and any credit that cannot be used. <a href=\"https://selling-guide.fanniemae.com/sel/b3-4.1-02/interested-party-contributions-ipcs\" rel=\"noopener\">Fannie Mae's interested-party-contribution guide</a> sets limits and classifications for loans sold under its rules; other loan programs and lenders can differ. Do not assume a credit can be paid to you in cash or applied to furniture just because the contract calls it an STR setup allowance.",
            ("callout", "Negotiating an offer on a specific STR? <a href=\"/apply/\">Book a BNB Accelerator acquisition call</a> to compare the lender-approved credit, lower-price alternative and cash needed to launch before sending terms."),
            "Compare the draft contract language with the lender's written answer and ask the settlement team how the concession will appear on the final closing statement. The <a href=\"https://www.consumerfinance.gov/owning-a-home/closing-disclosure/\" rel=\"noopener\">Consumer Financial Protection Bureau's Closing Disclosure explainer</a> shows seller credits and the cash-to-close calculation as separate items. A credit larger than eligible costs may be reduced or treated differently under program rules. Have the actual lender and closing professionals confirm, rather than using a generic percentage from another loan type.",
        ]),
        ("Model both offers through the first guest", [
            "Make a two-column comparison with price, down payment, loan amount, eligible closing costs, usable seller credit, cash to close, post-close setup cash, minimum reserve and first-year payment. Keep the STR's opening budget separate: furniture, safety work, photography, permits, supplies and a ramp reserve usually come due after closing. A credit that saves closing cash may protect this launch budget; it does not erase the expense. Use the <a href=\"/underwriting/cash-needed-to-buy/\">cash-through-launch worksheet</a> and ask whether either option leaves the buyer below the required reserve floor.",
            ("table", ["Decision line", "Seller credit at higher price", "Lower price without credit"], [
                ["Cash at closing", "Can be lower if lender permits full use", "Often higher despite a smaller down payment"],
                ["Loan principal", "Usually based on the higher contract price", "Usually lower if loan-to-value structure is unchanged"],
                ["STR launch liquidity", "May preserve cash for a timed opening", "May require more cash before setup begins"],
                ["Unusable concession", "Possible if credit exceeds eligible costs or program cap", "No seller credit to expire, but appraisal still matters"],
            ]),
            "Illustrative arithmetic only: assume a $500,000 STR purchase, 25% down, $12,000 of lender-approved closing charges and an available $10,000 seller credit. The credit scenario is $125,000 down plus $12,000 charges minus $10,000 credit, or $127,000 cash to close, with a $375,000 starting loan before other adjustments. A $10,000 price cut instead produces a $490,000 price, $122,500 down and $12,000 charges, or $134,500 cash to close, with a $367,500 starting loan. The credit preserves $7,500 more cash initially; the price cut starts with $7,500 less debt. Taxes, escrow, lender fees, appraisal and program treatment could change both outputs. This is not a quote, market statistic or client result.",
        ]),
        ("Decide whether liquidity or basis is the constraint", [
            "A usable credit may be stronger when the buyer has a sound deal but a tight, dated launch budget: the extra closing liquidity keeps the furnishing and reserve plan intact without borrowing elsewhere. It may be weaker when projected closing charges are too small to absorb it, the lender disallows it, the higher price cannot appraise, or the deal only meets the return hurdle at a lower basis. A price reduction usually helps when the conservative STR revenue cannot support the original debt or when reserves are already ample. Recalculate the <a href=\"/blog/str-maximum-offer-price-from-revenue/\">maximum offer from supported revenue</a>; neither structure should make you pay more than the property is worth to your plan.",
            "Ask the lender for a third scenario if a smaller credit plus a modest price cut could satisfy both constraints. Do not silently inflate the price to create a nominal credit: financing concessions and appraisal review may defeat that structure. Likewise, do not mistake seller-paid repairs, a furniture purchase, a rate buydown and a general closing-cost credit for the same thing. Each has different timing, evidence and lender treatment. The narrower <a href=\"/blog/seller-credit-str-furnishings/\">furnishing-credit guide</a> covers why a closing credit is not itself a post-close furniture payment.",
        ]),
        ("Proceed, renegotiate, delay or walk away", [
            "Proceed when the lender confirms the credit is usable, the appraisal and final cash-to-close plan work, and the STR still meets your return and reserve hurdles. Renegotiate toward a lower price when financing or long-term economics are binding; toward a permitted credit when opening liquidity is the binding constraint; or split the difference when both matter. Delay removing financing or appraisal protection while a revised Loan Estimate, closing-cost detail or lender approval is pending. Reject the purchase if the seller's price only works by assuming an impermissible credit, spending the emergency reserve, or projecting unverified STR revenue.",
            "Before countering, write down both scenarios' cash to close, loan balance, first-year debt service, launch cash and downside reserves. Send the actual proposed language to your lender and local real-estate counsel. <a href=\"/apply/\">Book a call to compare STR offer terms with BNB Accelerator</a> if you want help sourcing, underwriting and negotiating the acquisition. We cannot guarantee financing, appraisal, permits, bookings or returns. This guide is educational, not legal, tax, lending or investment advice; confirm your own transaction terms with qualified professionals.",
        ]),
    ],
    "faqs": [
        ("Is a seller credit the same as a lower STR purchase price?", "No. A usable credit can reduce eligible closing cash, while a lower price generally reduces the amount financed. Compare written lender scenarios and the remaining cash for launch."),
        ("Can a seller credit pay for Airbnb furniture after closing?", "Do not assume it can. The lender must confirm allowed uses and the settlement team must show how the credit applies. Budget post-close furniture separately."),
        ("What if the STR does not appraise at the higher price?", "A large credit does not remove appraisal risk. Ask the lender to model the appraisal shortfall and use a valid appraisal contingency or renegotiate the price before assuming the credit survives."),
        ("When should an STR buyer favor a price cut?", "Favor a price cut when lower debt and a defensible purchase basis matter more than immediate closing liquidity, or when the proposed credit cannot be fully used under the loan terms."),
    ],
    "related": [
        '<a href="/underwriting/cash-needed-to-buy/">Budget cash through STR launch</a>',
        '<a href="/blog/str-maximum-offer-price-from-revenue/">Calculate a maximum offer</a>',
        '<a href="/blog/seller-credit-str-furnishings/">Check furnishing-credit limits</a>',
        '<a href="/blog/compare-two-str-properties-before-offer/">Compare purchase alternatives</a>',
    ],
    "cta_h": "Negotiate the concession your STR plan can use",
    "cta_p": "We can compare cash-to-close and long-term economics on the property you are considering before your offer terms become binding.",
}]


if __name__ == "__main__":
    blog.build(POSTS)
