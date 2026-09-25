#!/usr/bin/env python3
"""Buyer-specific criteria for sourcing a short-term rental acquisition."""

import blog


POSTS = [{
    "slug": "short-term-rental-buy-box",
    "title": "Build a Short-Term Rental Buy Box",
    "title_tag": "How to Build a Short-Term Rental Buy Box | BNB Accelerator",
    "h1": "What should be in your short-term rental buy box?",
    "description": "Set STR purchase criteria for capital, markets, legal use, property features, return thresholds, operations, and fallback before reviewing listings.",
    "date": "2026-09-24",
    "category": "Acquisition Diligence",
    "lead": "A useful STR buy box is a short set of pass/fail rules that tells an acquisition team which properties deserve a full underwrite. Start with available cash after reserves, financing and closing constraints, legal ability to host, target guest and market, launch workload, and a downside return threshold. Make amenities and design preferences secondary. If a property cannot pass permission, capital, and downside tests, a beautiful listing or optimistic revenue forecast should not put it back in the search.",
    "sections": [
        ("Write the investor constraints before the property wishlist", [
            "A generic real-estate buy box starts with price, bedrooms, and geography. An STR buy box needs more because the home must function as a hospitality business after purchase. Write down who will manage it, how far you can travel, what personal use you want, when you need it operating, and the amount of liquidity you will keep after closing and launch. A cash limit is not simply the down payment; it includes lender-required reserves, closing costs, setup and a separate operating cushion. Use the <a href=\"/underwriting/cash-needed-to-buy/\">cash-needed framework</a> to calculate the property-specific amount.",
            ("callout", "Have capital ready but too many STR markets and listings to screen? <a href=\"/apply/\">Book a BNB Accelerator acquisition call</a> to turn your budget, return hurdle, and operating preferences into a search that can reject weak deals early."),
            "Ask the lender which loan product fits your intended occupancy and use. Do not describe an investment property as a second home to obtain different terms. Compare written Loan Estimates on the same loan amount and timeline; the <a href=\"https://www.consumerfinance.gov/owning-a-home/compare/compare-loan-estimates/\" rel=\"noopener\">Consumer Financial Protection Bureau</a> recommends comparing payment, upfront lender costs, credits, and cash to close—not just the advertised rate. Lender policies may change and the applicable loan must be confirmed for your transaction."
        ]),
        ("Use hard gates, flexible ranges, and preferences", [
            "Hard gates eliminate an address without a revenue model. Flexible ranges define what is worth deeper work, not automatic acceptance. Preferences guide tie-breakers only. This separation prevents the search from becoming either impossibly narrow or so loose that every attractive property qualifies.",
            ("table", ["Decision layer", "Example criterion", "Evidence before an offer"], [
                ["Hard gate", "Whole-home STR use is permitted for this address and buyer", "Jurisdiction guidance, permit path, HOA and recorded restrictions"],
                ["Hard gate", "All-in cash and post-launch reserves fit available capital", "Lender terms, closing estimate, setup bids, reserve calculation"],
                ["Hard gate", "Property can be launched within your realistic capacity", "Work scope, vendors, manager availability and calendar"],
                ["Flexible range", "Price and sleeping capacity support the target guest", "Actual available listings and truly comparable STRs"],
                ["Flexible range", "Conservative net return clears your own hurdle", "Independent revenue, full expenses and downside model"],
                ["Preference", "Pool, view, game room, or architectural style", "Guest demand and incremental cost; never a substitute for the gates"],
            ]),
            "Local short-stay rules are not interchangeable across a metro area. <a href=\"https://www.airbnb.com/help/article/376\" rel=\"noopener\">Airbnb's hosting guidance</a> identifies zoning, registration and permits as possible restrictions; obtain the actual jurisdiction's current written requirements for a target address. The <a href=\"/underwriting/hoa-restrictions/\">HOA guide</a> and <a href=\"/underwriting/permit-transfer/\">permit-transfer guide</a> cover two separate failure points. A market can be attractive while a particular parcel or ownership structure is not eligible."
        ]),
        ("Choose a market by fit, then select a property by evidence", [
            "A market belongs in the buy box only if it has a plausible guest demand pattern, an address-level legal path, purchasable inventory within your capital, a reachable operator or vendor network, and a downside you can tolerate. Compare a few markets with the same assumptions instead of screening the entire country by a single average revenue figure. Start with the <a href=\"/markets/\">market library</a>, <a href=\"/scenarios/\">illustrative scenario library</a>, and <a href=\"/blog/how-to-choose-str-market/\">market-selection guide</a>, then verify current local rules and comparable listings for the actual submarket.",
            "Within a market, describe the guest you intend to serve before writing 'three bedrooms' or 'must have hot tub.' A family group, couples weekend, or drive-to-lake trip may imply different beds, parking, access, seasonal risk, and amenity costs. Translate that into a small number of functional requirements. Screen nearby operating listings for comparable capacity, location, amenities, availability and price. A property is not a comparable merely because it is in the same city or has the same bedroom count.",
            "Do not hard-code a revenue target from a data tool alone. The <a href=\"/revenue-projections/\">revenue-projection framework</a> and <a href=\"/blog/how-to-analyze-airbnb-deal/\">deal-analysis guide</a> separate observed comp evidence from assumptions about occupancy, nightly rate and expenses. If seller statements are available, reconcile them to platform payouts, calendars and taxes. If the property has never rented, use a wider uncertainty range and a more conservative opening ramp."
        ]),
        ("Run the buy box on one sample deal", [
            "Illustrative only: a buyer has $180,000 available for an STR acquisition and decides to retain $35,000 after launch. Their maximum transaction-and-launch cash requirement is therefore $145,000, subject to lender approval and the actual reserve requirement. A listing priced within the search range needs $105,000 at closing, an estimated $28,000 to furnish and prepare, and $16,000 of immediate repairs. Its $149,000 total fails the capital gate before operating reserves, even if projected revenue is attractive. The buyer can negotiate price or scope, increase documented available capital, or reject it; the $145,000 limit should not silently move to save the deal.",
            "On a second listing, the cash requirement fits, but the seller says an STR permit can transfer and cannot provide written confirmation. That fails the permission gate pending proof. A third listing clears both gates but only meets the buyer's return hurdle if peak-season occupancy persists year-round. That fails the downside test. The buy box has done its job by saving full underwriting time for properties where the important assumptions can actually be supported.",
            "Set a review date for the buy box. If every property fails, determine whether the market, budget, timing, return hurdle or feature requirement is the constraint. Change one assumption deliberately and record why; do not relax legal permission or underwrite unverified revenue to create inventory. Conversely, if every listing passes, your gates are too vague to protect acquisition time."
        ]),
        ("Hand the same brief to everyone sourcing the deal", [
            "Give the buyer's agent, lender, property manager and acquisition team one written brief with hard gates, ranges, preferences, acceptable fallback use, sources of capital, and who signs off on exceptions. Ask for a rejection log: which gate failed, what evidence is missing, and whether the property can be reconsidered after a specific document or price change. This makes the search auditable and prevents attractive photos from resetting the criteria at every showing.",
            "Proceed to full diligence when the hard gates have evidence and a conservative model clears your own return hurdle. Renegotiate when price or documented work scope can repair a failed capital or return test. Reject when hosting rights cannot be established, the launch requires unavailable capital or operators, or the deal works only under optimistic assumptions. <a href=\"/apply/\">Book a call to build and test your STR acquisition buy box</a>. BNB Accelerator can help source and analyze options; it cannot guarantee permits, financing, bookings, tax outcomes or investment returns. This page is educational and not legal, tax, lending, insurance or investment advice."
        ]),
    ],
    "faqs": [
        ("How narrow should an STR buy box be?", "Narrow enough to reject properties that fail permission, capital, launch capacity, or a conservative return test; flexible on cosmetic features and reasonable price or layout ranges."),
        ("Should a target cash-on-cash return be a hard gate?", "Your own hurdle can be a gate after a complete, conservative property-level model. A headline return from a seller or data tool is not enough evidence to apply it."),
        ("Can I use one buy box for several STR markets?", "Keep investor-level constraints the same, but use market-specific demand, rules, insurance, taxes, operating costs and comparables before deciding whether an address passes."),
        ("What if no property fits?", "Identify the binding constraint and intentionally revise one flexible requirement, market or timeline. Do not waive legal eligibility or invent revenue to force a purchase."),
    ],
    "related": [
        '<a href="/blog/how-to-choose-str-market/">Choose an STR market</a>',
        '<a href="/underwriting/cash-needed-to-buy/">Cash needed to buy</a>',
        '<a href="/blog/how-to-analyze-airbnb-deal/">Analyze an Airbnb deal</a>',
        '<a href="/underwriting/permit-transfer/">Permit-transfer diligence</a>',
    ],
    "cta_h": "Turn your criteria into a real STR search",
    "cta_p": "We can translate your capital, market and return requirements into a defensible acquisition brief and compare actual properties against it.",
}]


if __name__ == "__main__":
    blog.build(POSTS)
