#!/usr/bin/env python3
"""Purchase loan structure decision; sources checked 2026-10-01.

Query: Should I use an interest-only or amortizing loan to buy an STR?
Gate: distinct intent 24/25, imminent buyer relevance 30/30, evidence 14/15,
acquisition-service fit 19/20, original decision support 9/10 = 96/100.
Search evidence: lender pages from AHL, Pillar, and Lendmire answering IO vs
amortizing rental/STR financing questions. No search volume or lead claims.
Distinct from reading-a-dscr-term-sheet: purchase viability across initial
payments and the contractual transition, no-refinance downside, remaining
balance and cash needed under two actual quotes. Primary sources below.
Rejected adjacent prepayment-penalty topic as already covered by term-sheet
and refinance pages; rejected lender-name swaps without a new buyer decision.
"""

import blog


POSTS = [{
    "slug": "interest-only-vs-amortizing-str-purchase",
    "title": "Interest-Only vs Amortizing Loans for an STR Purchase",
    "title_tag": "Interest-Only Loan for an STR Purchase | BNB Accelerator",
    "h1": "Should you buy an STR with an interest-only loan?",
    "description": "Compare interest-only and amortizing loans before buying an STR. Model the payment reset, cash reserves and a hold without refinancing before you offer.",
    "date": "2026-10-01",
    "category": "Financing",
    "lead": "An interest-only loan can reduce the opening payment on an STR purchase, but it should not be the reason an otherwise unaffordable property looks buyable. Compare the actual interest-only and amortizing quotes before making an offer. Model the first year, the contractual payment transition and a hold in which you cannot refinance or sell on your preferred date. Proceed only if your cash, conservative property income and documented loan terms support that plan. If the property works solely because you omit principal payments and assume a future refinance, lower the offer, change the financing or choose another property. This guide shows how to turn the payment difference into a purchase decision.",
    "sections": [
        ("Get the payment schedule that will govern your purchase", [
            ("callout", 'Comparing loan options for an STR you want to buy? <a href="/apply/">Book a call</a> with BNB Accelerator to test the property price, cash through launch and loan payment schedule before committing to an offer.'),
            "An interest-only payment covers interest during a specified period without scheduled principal reduction. What happens next depends on the contract. <a href=\"https://ahlend.com/docs/how-do-interest-only-dscr-loans-work/\" rel=\"noopener\">American Heritage Lending's explanation</a> describes a rental loan that begins with interest-only payments and then amortizes over the remaining term. The <a href=\"https://www.consumerfinance.gov/ask-cfpb/what-is-an-interest-only-loan-en-101/\" rel=\"noopener\">CFPB's general explanation</a> also identifies loans that require payoff or refinancing at the end of the period. Ask which structure you are actually offered. An amortization transition and a balloon due date create different cash requirements.",
            "Request both quotes for the same property, intended STR use, buyer or entity, closing date and documented income method. Obtain the loan balance, rate, whether it is fixed or adjustable, interest-only duration, total term, transition payment, fees, required down payment, reserves, prepayment terms and any maturity payoff. For an adjustable loan, obtain the index, margin, adjustment dates and caps. Ask the lender to supply the payment schedule; a headline rate is insufficient.",
            "The <a href=\"https://www.pillarprivatelending.com/resources/dscr/interest-only-vs-pi-rental\" rel=\"noopener\">Pillar Private Lending comparison</a> notes that the payment used for qualification can differ by lender or program. Have your lender identify its qualifying payment and accepted rental income in writing. Keep that ratio separate from your own after-expense cash model. Loan approval does not establish that the acquisition meets your investment hurdle. Sources were checked October 1, 2026; current eligibility and terms require lender confirmation.",
        ]),
        ("Compare opening cash flow with the later payment", [
            "Illustrative only: assume a $500,000 STR purchase with a $375,000 loan, a fixed 7.5% annual rate and a 30-year total term. Compare a loan amortizing from month one with a loan requiring interest-only payments for ten years and then amortizing the unchanged balance over twenty years. Assume no voluntary principal payments, identical rates and no fees for this payment illustration. These are hypothetical inputs, not current quotes, market returns or a recommendation.",
            ("table", ["Payment or balance", "Amortizing from purchase", "Ten years interest-only, then amortizing"], [
                ["Initial monthly principal and interest, or interest only", "$2,622.05", "$2,343.75"],
                ["Loan balance after 120 scheduled payments", "$325,481.20", "$375,000.00"],
                ["Monthly payment when year eleven begins, rate unchanged", "$2,622.05", "$3,020.97"],
            ]),
            "Monthly interest in this model is loan balance multiplied by 7.5% and divided by twelve. The amortizing payment repays the balance at that monthly rate over either 360 or 240 payments. The interest-only option initially preserves $278.30 per month, but the payment rises by $677.22 when amortization starts. The balance has also remained $49,518.80 higher after ten years than under scheduled amortization. Treat principal reduction as equity building rather than an operating expense; a smaller payment does not automatically mean a higher total investment return.",
            "Now apply the debt payments to the same property. Suppose collected monthly revenue is $6,000 and all operating costs plus a replacement-reserve allowance total $2,500, leaving $3,500 before loan payments. Include management, platform charges, utilities, repairs, taxes, insurance and any HOA dues in those costs; this simplified model holds the total constant only to isolate the loan effect. Cash remaining is $877.95 with amortization from the purchase, $1,156.25 during interest-only and $479.03 after its transition. These figures are owner cash planning, not the lender's DSCR calculation.",
            "Reduce modeled revenue by 10% to $5,400 while keeping costs at $2,500. The initial interest-only loan still shows $556.25 per month, but its later payment creates a $120.97 monthly deficit. The amortizing option retains $277.95. That finding does not forecast year eleven; it shows that the proposed purchase needs a credible way to absorb the later obligation under modestly weaker revenue. Run higher operating costs and a lower-demand season too. The <a href=\"/underwriting/downside-scenario/\">STR downside framework</a> covers those property assumptions.",
        ]),
        ("Test the purchase without a timely refinance or sale", [
            "Make one version of the purchase model in which you retain the loan through its contractual transition. Use today's supportable property revenue, the transition payment and explicit cost stress, rather than assuming nightly rates will grow enough to fill the gap. For an adjustable loan, model the rate adjustments using the actual contract limits and lender schedule. If maturity instead requires a balloon payoff, identify a funded repayment plan and test the failure of the planned refinance. Do not substitute the amortization example above for balloon analysis.",
            "The CFPB cautions against relying on a sale or refinance to solve a higher payment because property value or the borrower's finances can change. For an STR buyer, there are additional property questions: will legal rental use remain available, will documented revenue meet the future lender's method, and what balance must be refinanced? Those are underwriting dependencies, not promises about a future loan. Read <a href=\"/blog/refinance-after-str-stabilization/\">the refinance-readiness guide</a> before treating stabilized bookings as an exit.",
            "Identify where the opening payment difference will go. A written plan to retain it as liquidity is different from spending it or immediately buying another property. In the illustration, the initial difference is only $278.30 per month; it must compete with repair surprises and weak booking months. Decide what cash you will keep outside the property and how much you could contribute without compromising other obligations. The <a href=\"/blog/str-lender-reserve-requirements/\">lender reserve requirement</a> and your own buffer serve different purposes.",
            "Compare actual cash required as well as payments. An interest-only quote may carry different leverage, points or reserve conditions from an amortizing quote. As a separate hypothetical, a change from 75% to 70% financing on a $500,000 purchase requires $25,000 more toward the price. That extra cash is unavailable for furnishing and opening unless you fund it elsewhere. Replace these assumed percentages with the approved quotes and use <a href=\"/underwriting/cash-needed-to-buy/\">cash needed through launch</a> to avoid spending the same reserves twice.",
        ]),
        ("Set the offer around the loan you can carry", [
            "Create a two-column purchase memo with the actual initial payment, transition or maturity obligation, cash to close, launch budget, retained reserves, conservative annual cash flow and expected balance at your planned exit. Put the no-refinance case beside the base case. Compare the same candidate property first, then use <a href=\"/blog/compare-two-str-properties-before-offer/\">the two-property comparison</a> to test an alternative purchase if the loan choice is masking a weak price.",
            ("table", ["Finding before your offer", "Decision"], [
                ["Both schedules clear your cash and downside hurdles; you have a defined use for opening liquidity", "Proceed with the structure that fits your hold and risk tolerance"],
                ["Interest-only passes initially but the later obligation fails your stress model", "Reduce the price or loan balance, compare amortizing financing, or reject"],
                ["Eligibility, transition terms or payment schedule are still unclear", "Delay commitment under valid contract protection until the lender answers"],
                ["Closing and setup consume the reserves needed for a slow launch", "Renegotiate or choose a less capital-intensive property"],
                ["The deal requires future appreciation, rate cuts or an unapproved refinance to remain affordable", "Reject that acquisition thesis or redesign it before buying"],
            ]),
            "Ask the lender to price any changes instead of assuming a lower offer reduces every cost proportionally. Recheck loan eligibility, source of down payment, financing deadlines and the property-specific STR permission. <a href=\"/apply/\">Book a call</a> to compare loan structures and purchase candidates with BNB Accelerator. We help buyers find, underwrite, negotiate, close and launch STR properties; your lender determines financing terms and approval. This is educational information, not lending, legal, tax or investment advice. Financing, permits, rental income, refinancing, resale values and returns are not guaranteed.",
        ]),
    ],
    "faqs": [
        ("Is an interest-only loan better for buying an STR?", "It depends on the actual quotes, cash needs and hold plan. Compare initial and later payments, remaining principal, fees, leverage and a downside case without refinancing before choosing the loan or property."),
        ("Can interest-only make an STR qualify for a DSCR loan?", "It may improve the ratio if that product qualifies on the interest-only payment. Other programs use a different payment. Obtain the lender's written income and payment methodology; qualification is separate from owner cash flow."),
        ("What happens when an STR interest-only period ends?", "Read the contract. Some loans begin amortizing the balance over the remaining term; others can require payoff. Fixed or adjustable rate provisions also matter. Get the exact transition schedule from the lender before buying."),
        ("Should I rely on refinancing before interest-only payments end?", "Do not make affordability depend solely on a future refinance. Model carrying the contractual obligation without one and test the future balance, property value, revenue documentation, legal use and reserve needs."),
    ],
    "related": [
        '<a href="/blog/reading-a-dscr-term-sheet/">Review the complete DSCR term sheet</a>',
        '<a href="/blog/str-mortgage-preapproval-before-property/">Prepare financing before the property search</a>',
        '<a href="/underwriting/">Use the STR acquisition underwriting framework</a>',
        '<a href="/tools/str-revenue-calculator/">Model property revenue and expenses</a>',
    ],
    "cta_h": "Choose financing that supports the STR purchase",
    "cta_p": "Compare the opening payment, later obligation and cash through launch before deciding what to offer.",
}]


if __name__ == "__main__":
    blog.build(POSTS)
