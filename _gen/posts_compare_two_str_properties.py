#!/usr/bin/env python3
"""A buyer's side-by-side decision model for two STR candidates."""

import blog


POSTS = [{
    "slug": "compare-two-str-properties-before-offer",
    "title": "How to Compare Two STR Properties Before an Offer",
    "title_tag": "Compare Two STR Properties Before an Offer | BNB Accelerator",
    "h1": "How do you compare two STR properties before making an offer?",
    "description": "Comparing two STRs for sale? Normalize legal use, revenue evidence, total cash, lender terms, downside return, and deal-killer risk before choosing an offer.",
    "date": "2026-09-24",
    "category": "Buying Strategy",
    "lead": "To compare two short-term-rental properties before making an offer, put them on the same all-in cash and downside basis—not just the same purchase-price or projected-gross-revenue basis. First remove any candidate without a credible path to legal STR use. Then give each property its own evidence-backed revenue range, full operating cost stack, actual financing terms, launch timeline, and cash required through opening. A higher projected return is not a better buy when it depends on a permit, price, or occupancy assumption you cannot verify. The correct answer may be A, B, or neither. Your comparison should show the exact fact that would change the decision before a contract deadline.",
    "sections": [
        ("Apply pass-or-fail gates before ranking returns", [
            "Write the intended rental use for each address: whole-home nightly stays, owner-occupied room rental, or another plan. Get local permission for that parcel and verify association restrictions, required license, capacity, and whether approval is available to a new owner. A seller's prior Airbnb listing is evidence of history, not permission for your future operation. If one property's legal path is unresolved, mark it 'conditional' rather than giving it a full revenue score. The <a href=\"/regulations/\">regulation library</a> is a starting point, but local written confirmation and counsel control the specific transaction.",
            ("callout", "Deciding between two live STR listings? <a href=\"/apply/\">Book a BNB Accelerator acquisition call</a> to pressure-test both deals' legal use, normalized returns, and maximum offer prices before you commit."),
            "Apply the same gate to financing and insurability. Send both addresses, intended investment use, project or HOA details, and property condition to your lender and insurer. Ask for property-specific quotes, not only a borrower preapproval. The <a href=\"https://www.consumerfinance.gov/owning-a-home/loan-estimate/\" rel=\"noopener\">Consumer Financial Protection Bureau's Loan Estimate guidance</a> helps buyers compare loan charges and payments; the actual loan terms may differ by property type and condition. If either candidate requires an unapproved specialty loan or cannot obtain the needed coverage, keep it out of the 'ready to offer' column.",
            ("table", ["Comparison line", "Candidate A", "Candidate B"], [
                ["Legal STR use", "Written status, conditions, renewal path", "Written status, conditions, renewal path"],
                ["Revenue support", "Matched comps, seasonality, seller records if any", "Matched comps, seasonality, seller records if any"],
                ["Total cash through launch", "Closing, repairs, furnishing, license, reserve", "Closing, repairs, furnishing, license, reserve"],
                ["Base and downside cash flow", "After all expenses and debt service", "After all expenses and debt service"],
                ["Open decision gate", "What must be verified before offer hardens?", "What must be verified before offer hardens?"],
            ]),
        ]),
        ("Normalize revenue and expenses rather than trusting headline yield", [
            "Use a comparable set appropriate to each property's location, bedroom count, sleeping capacity, condition, and guest proposition. Separate source observations from assumptions about your own opening price and occupancy. A seller's trailing gross can be useful, but reconcile it with payout records, blocked nights, owner stays, management fees, cleaning charges, taxes, and changes in listing quality. A market-level estimate is not a property-level promise. Use the <a href=\"/underwriting/\">underwriting guides</a> to build base and conservative cases before calculating a return.",
            "Apply a consistent expense taxonomy to both candidates: platform and payment fees, cleaning, supplies, management, utilities, insurance, taxes, HOA, maintenance, capital reserve, and debt service. Do not assume the same expense ratio for a small condo and a large pool home. The number to compare is owner cash flow after realistic costs, not occupancy or gross revenue alone. If the properties have different seasonality, compare monthly cash needs as well as full-year totals so a peak-season estimate does not hide a winter funding gap.",
            "A comparison should also account for the launch lag. One property may be furnished but require a new permit; another may be legally ready but need a roof and six weeks of installation. Put expected opening dates next to carrying costs and the cash needed during zero-revenue months. Do not count booked revenue before the property is legal, insured, furnished, and available to guests. The <a href=\"/underwriting/cash-needed-to-buy/\">cash-needed-to-buy ledger</a> includes costs that a simple down-payment comparison misses.",
        ]),
        ("Run the same worked decision on both properties", [
            "Illustrative only: Candidate A needs $160,000 of total cash through launch and shows $22,000 of modeled annual owner cash flow after debt service. Candidate B needs $140,000 and shows $24,000. On those assumptions, simple cash-on-cash return is 13.8% for A and 17.1% for B. Now lower each revenue case and update costs: A falls to $10,000, or 6.3%; B falls to $8,000, or 5.7%. B's stronger base case does not make it an automatic offer when its downside is weaker or its STR permit is unconfirmed. All figures are hypothetical arithmetic, not market data, forecasts, or client outcomes.",
            "The key is not to assign subjective points after seeing which home you like. Set your hurdle first: minimum downside cash flow, maximum total cash, acceptable permit risk, and latest launch date. Then calculate both properties using the same definitions. If B fails the permit gate, its cash-on-cash result is provisional. If A needs a repair that raises total cash to $185,000, recalculate it before ranking. A good side-by-side model makes that reversal visible rather than burying it in a score.",
            "Finally set a price ceiling for each deal. Work backward from supportable net revenue and the buyer's hurdle, not the seller's asking price. The <a href=\"/blog/str-maximum-offer-price-from-revenue/\">maximum-offer-price guide</a> gives the mechanics. A candidate that is attractive only at a lower price may deserve a disciplined offer; one that fails even at a realistic discount should leave the shortlist.",
        ]),
        ("Choose A, B, or neither with an offer memo", [
            "Proceed on the candidate whose legal use, financing, insurance, cash budget, and conservative return are all supportable at your proposed price. Renegotiate when a repair, permit delay, or actual loan quote moves a still-viable property below your hurdle. Delay if the decisive document can arrive within a protected contingency; do not waive that protection just because the other listing may sell. Reject both when neither survives the downside case or when the only attractive numbers depend on unsupported guest revenue.",
            "Your one-page offer memo should name the preferred address, maximum price, cash through opening, base and downside cash flow, evidence sources and dates, unresolved gates, contingency deadlines, and the runner-up. If the favorite fails, the runner-up should be re-underwritten on its own current facts—not assumed to inherit the first property's financing or revenue. <a href=\"/apply/\">Book a call to compare your STR candidates with an acquisition team</a>. BNB Accelerator cannot guarantee permits, financing, bookings, or returns. This guide is educational, not legal, lending, tax, or investment advice; confirm the deal with qualified professionals.",
        ]),
    ],
    "faqs": [
        ("What is the first thing to compare between two STR properties?", "Confirm that each address can support your intended legal STR use and a viable financing path. A high projected return is irrelevant if the property cannot operate as planned."),
        ("Should I choose the STR with the higher projected gross revenue?", "No. Compare owner cash flow after property-specific expenses and debt service, total cash through launch, downside performance, and legal and execution risk."),
        ("How do I compare a turnkey STR with an unfurnished house?", "Add the unfurnished property's setup, launch delay and carrying costs; verify the turnkey property's transferable rights and revenue evidence. Put both on an all-in cash and downside basis."),
        ("What if neither STR meets my hurdle?", "Do not force a purchase. Keep the buy box and offer ceiling, document why each failed, and source another candidate or revise the strategy only after reassessing your capital and goals."),
    ],
    "related": [
        '<a href="/underwriting/">Review the underwriting library</a>',
        '<a href="/underwriting/cash-needed-to-buy/">Calculate total cash through launch</a>',
        '<a href="/blog/str-maximum-offer-price-from-revenue/">Set a maximum offer price</a>',
        '<a href="/blog/short-term-rental-buy-box/">Define your STR buy box</a>',
    ],
    "cta_h": "Compare real deals on the same decision basis",
    "cta_p": "We can test two addresses against legal use, revenue evidence, all-in cash, downside, and a defensible offer ceiling.",
}]


if __name__ == "__main__":
    blog.build(POSTS)
