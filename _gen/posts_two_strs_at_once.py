#!/usr/bin/env python3
"""Decision-stage comparison of simultaneous and sequential STR purchases."""

import blog


POSTS = [{
    "slug": "buy-two-short-term-rentals-at-once",
    "title": "Buy Two Short-Term Rentals at Once or One First?",
    "title_tag": "Buy Two STRs at Once or One First? | BNB Accelerator",
    "h1": "Should you buy two short-term rentals at once or one first?",
    "description": "Buying two STRs soon? Compare lender treatment, all-in cash, reserves, launch overlap, downside risk, and one-at-a-time alternatives before making offers.",
    "date": "2026-09-24",
    "category": "Buying Strategy",
    "lead": "Most first-time short-term-rental buyers should close one well-supported property before committing to a second, even if they have capital for two down payments. Two simultaneous purchases can make sense when both properties independently clear the buyer's hurdle, lenders have reviewed the combined obligations, and cash remains for two launches plus a common downside. The decision is not simply whether two listings diversify revenue. It is whether the buyer can finance, permit, furnish, insure, and stabilize both before either produces dependable owner cash flow. Put a one-property path beside a two-property path before making overlapping offers, and give each property its own stop rule.",
    "sections": [
        ("Test both financing files as one purchase plan", [
            "Tell both lenders about every pending purchase, closing date, existing mortgage, and intended STR use. Do not obtain two separate preapprovals that each assume the other deal does not exist. Ask how the first closing changes debt-to-income analysis, property count, rent documentation, down payment, loan terms, and final approval on the second. A lender's quote for one property is not approval for the pair. If financing products differ, make the comparison on actual written terms rather than advertised rates.",
            ("callout", "Considering two STR purchases in the same season? <a href=\"/apply/\">Book a BNB Accelerator acquisition call</a> to compare candidate deals, financing dependencies, and the cash left after both launches."),
            "<a href=\"https://selling-guide.fanniemae.com/sel/b3-4.1-01/minimum-reserve-requirements\" rel=\"noopener\">Fannie Mae's reserve guide</a> says additional reserves can be required for multiple financed properties. It also says the same assets may satisfy reserve requirements for simultaneous second-home or investment-property applications under its rules; that does not mean the same dollars can pay two down payments, two furnishing bills, and future operating losses. Ask the actual lender for the documented reserve calculation and post-closing liquidity requirement. Use the <a href=\"/blog/str-lender-reserve-requirements/\">STR lender-reserve guide</a> to distinguish lender minimums from your own operating buffer.",
            "Fannie Mae has a specific <a href=\"https://selling-guide.fanniemae.com/sel/b3-3.8-06/rental-income-non-subject-property-investment-properties-purchased-within-45-days-subject-property\" rel=\"noopener\">rental-income topic for investment properties bought within 45 days of another application's subject property</a>. It sets documentation and treatment rules, including that lease agreements are not permitted for those recently purchased properties under that topic. Do not assume a new STR's projected nightly revenue will immediately offset its entire payment on the next loan. Have the lender explain the applicable program, timing, and qualifying-income calculation before sequencing offers.",
        ]),
        ("Count every dollar twice only in the stress test, not in the bank", [
            "Build a separate cash-to-close and launch ledger for property A and property B. Include down payment, closing costs, due diligence, repairs, furnishing, photography, license, insurance, utilities, manager setup, and required reserves for each. Then make one combined cash schedule by week. The first property's deposit, inspection, and furnishing draw can land before the second property's loan is final. If funds are invested or tied up in an appraisal gap, they may not be available for either launch when needed.",
            "Illustrative only: a buyer has $300,000 available. Candidate A requires $105,000 through launch and candidate B requires $125,000. The remaining $70,000 is not automatically free cash: it must cover lender reserves, personal obligations, delayed opening, and simultaneous downside. Suppose both produce no guest revenue for two months while monthly combined carrying and setup costs total $12,000; the illustrative buffer falls to $46,000 before maintenance surprises. These are planning numbers, not market performance data. Compare the pair with one property and cash left untouched until actual operating results arrive. The <a href=\"/underwriting/cash-needed-to-buy/\">all-in acquisition ledger</a> is the starting point.",
            ("table", ["Decision lens", "One STR first", "Two STRs together"], [
                ["Financing", "One file and one initial property count", "Two interdependent files; confirm both with lenders"],
                ["Cash", "One launch budget and reserve", "Two overlapping closing and launch schedules"],
                ["Evidence", "First property's real operations can inform the next buy", "Both are mostly projections at commitment"],
                ["Downside", "One property carries vacancy and repair risk", "Two can fail together through season, regulation, or contractor delay"],
            ]),
        ]),
        ("Check whether two launches create a shared failure mode", [
            "Separate the properties' economics first: verify address-level STR permission, comparable revenue, taxes, insurance, management, and an offer ceiling for each. Then test correlation. Two cabins in the same seasonal market may share cleaners, contractors, weather and regulatory risk. Two markets reduce some correlated exposure but require two vendor systems and two sets of local diligence. The existing <a href=\"/blog/str-portfolio-diversification/\">portfolio-diversification guide</a> addresses where to hold properties; this purchase decision is about whether both should enter escrow and launch at once.",
            "Ask whether the same person or vendor can handle two inspections, furnishing installs, permit filings, guest setups, and first-week problems without delaying either listing. A manager who promises capacity should give property-specific onboarding dates and fees. If the second launch slips, carry its mortgage, insurance and utilities without STR income in the downside case. A purchase model that only works when both open on the original date has too little margin for a two-property acquisition.",
            "There is also an information advantage to waiting. The first STR's real booking pace, guest mix, cleaning cost, insurance, and maintenance needs can reveal whether the original underwriting was sound. Waiting is not automatically better: a second genuinely exceptional deal may disappear. But the cost of waiting should be compared with the value of learning, preserved liquidity, and a simpler closing, not merely with a forecast of lost revenue.",
        ]),
        ("Choose simultaneous, sequential, or neither before signing", [
            "Proceed with two only when each passes its own legal-use and downside test, both lenders underwrite the combined plan, the two closing and launch schedules are credible, and post-closing cash exceeds lender minimums plus the buyer's stress reserve. Buy one first when candidate A is strong but B is marginal, or when the second requires the first to perform immediately. Renegotiate B if the pair works only at a lower basis or with a later closing; delay B if financing or permit evidence will not arrive within its contingency window.",
            "Reject simultaneous purchases if one deal depends on an unverified STR permit, duplicate use of closing funds, projected rent that the lender will not count, or a single vendor whose delay stops both launches. Your next step is to send the lender a written two-address plan and build a combined weekly cash schedule, then rank the candidates as if only one can close. <a href=\"/apply/\">Book a call to compare a one- versus two-STR acquisition plan</a>. BNB Accelerator cannot guarantee permits, financing, revenue, or returns. This article is educational, not legal, lending, tax, or investment advice; confirm your transaction with qualified professionals.",
        ]),
    ],
    "faqs": [
        ("Can I get two mortgages to buy two STRs at the same time?", "Possibly, but disclose both pending purchases and intended investment use to the lenders. Have them evaluate debt, qualifying income, financed-property count, reserves, and closing sequence together."),
        ("Do lender reserves double when buying two investment properties at once?", "Not necessarily under every program. Fannie Mae's simultaneous-application guidance permits the same assets to satisfy specified reserve requirements for both files, but two down payments and two launch budgets still require real cash."),
        ("Should I buy one Airbnb first and wait for actual revenue before a second?", "Often, particularly for a first-time buyer, because real operations provide evidence and preserve liquidity. Compare that learning and downside protection with the specific second deal rather than applying a universal waiting period."),
        ("What would stop a two-STR purchase plan?", "Unverified permits, a lender's rejection of the combined obligations, insufficient cash after both launches, overlapping vendor bottlenecks, or downside results below the buyer's hurdle."),
    ],
    "related": [
        '<a href="/underwriting/cash-needed-to-buy/">Build the all-in cash ledger</a>',
        '<a href="/blog/str-lender-reserve-requirements/">Review lender reserve requirements</a>',
        '<a href="/blog/str-portfolio-diversification/">Compare portfolio concentration</a>',
        '<a href="/blog/short-term-rental-buy-box/">Set a purchase buy box</a>',
    ],
    "cta_h": "Sequence STR purchases around real cash and evidence",
    "cta_p": "We can assess two candidates independently, then test lender dependencies, combined reserves, launch capacity, and downside before you commit.",
}]


if __name__ == "__main__":
    blog.build(POSTS)
