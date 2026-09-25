#!/usr/bin/env python3
"""Purchase decision when an operating STR's revenue is falling."""

import blog


POSTS = [{
    "slug": "buy-str-with-declining-revenue",
    "title": "Should You Buy an STR With Declining Revenue?",
    "title_tag": "Buy an STR With Declining Revenue? | BNB Accelerator",
    "h1": "Should you buy an STR with declining revenue?",
    "description": "Buying an Airbnb with falling revenue? Verify the trend, diagnose its cause, reset the offer price, and decide whether to proceed, renegotiate or walk away.",
    "date": "2026-09-25",
    "category": "Buying Strategy",
    "lead": "You can buy an operating short-term rental whose revenue is falling, but only if the price and purchase plan work on a defensible forward case—not the seller's best year. A decline might come from owner-blocked nights, a temporary management lapse, weaker pricing, new competition, or a durable change in local demand. Those explanations have different values to a buyer. Before offering, rebuild revenue month by month, compare the property with genuinely similar STRs, identify what you could change after closing, and underwrite the cost and time to make that change. If the seller cannot document the cause, treat the lower run rate as the starting point rather than paying for an unproven rebound.",
    "sections": [
        ("Confirm the decline before explaining it", [
            "Ask for at least two comparable periods of monthly booking and payout records, channel by channel, with reservation dates, cancellations, refunds, taxes, cleaning fees and platform fees separated. Obtain bank deposits and any direct-booking ledger to reconcile what was actually collected. Airbnb's <a href=\"https://www.airbnb.com/help/article/3632\" rel=\"noopener\">earnings dashboard guidance</a> describes transaction-level reports and downloadable CSV files; a screenshot of a headline earnings number is not an adequate substitute for records you can reconcile. Match booked stays to the month they occurred, rather than mistaking payout timing for demand.",
            ("callout", "Considering an offer on an STR with shrinking receipts? <a href=\"/apply/\">Book a BNB Accelerator acquisition call</a> to review the revenue evidence and the price you can safely support before you commit."),
            "Normalize each period for bookable nights. Mark seller stays, maintenance closures, minimum-stay changes, listing pauses and rooms taken offline. A calendar with fewer sellable nights can show lower gross revenue even when guest demand for available nights stayed strong. Conversely, a fully available calendar with more vacant nights is a different warning. Verify the physical property's configuration and legal STR use at the address; a seller's old income does not prove you can operate on identical terms after purchase. The <a href=\"/underwriting/seller-financials/\">seller-financials guide</a> gives a broader document-reconciliation checklist.",
        ]),
        ("Decompose the change into nights, rate and market pressure", [
            "For each comparable month, calculate available nights, paid nights, paid-night occupancy and average nightly room revenue. Room revenue is approximately paid nights multiplied by average nightly rate; compare fees and other income separately. Then build a <a href=\"/blog/assembling-a-comparable-set/\">matched STR comparable set</a> with similar location, capacity, access, quality and operating permission. If similar homes weakened while this one stayed available and maintained, do not label the decline a simple management fix. If comparable demand held but this home's conversion fell after poor reviews, neglected photos or inconsistent availability, investigate whether a buyer can remedy the issue, at what cost and on what timetable.",
            ("table", ["Possible driver", "Evidence to request", "Purchase implication"], [
                ["Fewer sellable nights", "Calendar blocks, repair records, owner-use dates", "Could normalize, but verify buyer access and repair cost"],
                ["Lower paid-night occupancy", "Booking pace and matched comparable calendars", "May signal market demand or listing-specific weakness"],
                ["Lower achieved nightly rate", "Reservation-level room rates and discount history", "Tests pricing power and margin, not just gross bookings"],
                ["Changed channel or fee mix", "Platform and direct-booking payouts, refunds, fee schedules", "Reconcile gross revenue to cash the buyer can retain"],
            ]),
            "Avoid comparing a peak-season quarter with an off-season quarter or a full year with a partial year. Do not infer that a property-specific fall is temporary solely because a broker says the seller was distracted. Obtain dates, operating records and independent comparables. Equally, a broader market decline may not make every property unbuyable; it changes the conservative forward revenue and therefore the offer ceiling.",
        ]),
        ("Underwrite the buyer's reset, not the seller's peak", [
            "Create a base case from supported current performance, a downside case using weaker occupancy or rate, and an upside case only for changes with an owner, budget and credible implementation schedule. Include management, cleaning, utilities, taxes, insurance, repairs, platform fees, furnishing or refresh work, permits, debt service and cash reserves. If the old account's review history helped conversions, do not assume that goodwill follows the property: read the <a href=\"/blog/airbnb-reviews-property-sale/\">review-transfer purchase guide</a> and allow for a <a href=\"/blog/new-listing-ramp-underwriting/\">new-listing ramp</a> where needed. Convert each scenario into a maximum offer using your actual financing and return threshold.",
            "Illustrative arithmetic only: an STR advertised with a prior-year $80,000 gross and a trailing $64,000 gross has a $16,000 gap. If records show the equivalent of 40 additional owner-blocked nights at a supported $200 room rate, that explains up to $8,000 of room revenue before expenses, not the full $16,000. The remaining gap still needs a documented explanation. If those nights instead were open but unbooked, simply restoring availability adds nothing. These figures are hypothetical, not a market benchmark, client result or earnings forecast. Re-run the deal on the verified $64,000 baseline and whatever adjustment the evidence—not the listing pitch—supports.",
            "Price any remedy explicitly. A refresh quote, better operator or new photography may improve the case, but the buyer funds it and bears execution risk. Deduct that cash and the expected ramp period from the price you can pay. If the upside case is the only one that meets your hurdle, you are buying a turnaround, not a stable income stream. Use the <a href=\"/blog/str-maximum-offer-price-from-revenue/\">maximum-offer framework</a> to keep optimism from silently raising your bid.",
        ]),
        ("Make an offer decision with clear stop conditions", [
            "Proceed when complete records reconcile, local STR permission and buyer financing are confirmed, matched comparables support the conservative demand case, and the price works after transition and reserves. Renegotiate when the decline is understood but lower current cash flow or a required fix changes your maximum offer; request a price reduction or supported seller credit rather than paying for the seller's peak year. Delay removing a diligence contingency when a decisive record, permit answer, lender condition or repair quote is still outstanding. Reject the deal when the seller will not provide verifiable records, legal use cannot be confirmed, market-wide weakness breaks your hurdle, or the price requires an unproven recovery.",
            "Put the conclusion in a one-page acquisition memo: verified trailing revenue, reason for change, comparable evidence, buyer transition costs, base/downside economics, maximum offer and unresolved conditions. Then decide whether to negotiate this property or source the next one. <a href=\"/apply/\">Book a call to review an STR purchase with BNB Accelerator</a> if you want help testing the records, setting a disciplined offer and planning the handoff. We cannot guarantee bookings, financing, permits or returns. This is educational information, not legal, tax, lending or investment advice; confirm property-specific facts with qualified professionals.",
        ]),
    ],
    "faqs": [
        ("Is falling STR revenue an automatic reason not to buy?", "No. Determine whether the decline is a reporting artifact, reduced availability, a fixable property issue or durable demand weakness. Buy only if documented current economics and a conservative transition case work at the negotiated price."),
        ("What seller records show why Airbnb income dropped?", "Request monthly reservation and payout exports, calendars with blocked nights, direct-booking records, bank deposits, refunds, fees, repair closures and owner-use dates. Reconcile them to the periods used in the listing's income claim."),
        ("Should I pay based on the STR's best revenue year?", "Not unless independent evidence supports that level as achievable for the buyer after closing. Use verified recent performance for the base case and treat a recovery as an explicitly costed upside case."),
        ("Can a new owner restore bookings just by improving the listing?", "Possibly, but do not assume it. Diagnose whether the weakness is listing-specific or market-wide, budget the changes, and model the new owner's account, reviews and launch ramp before raising the offer."),
    ],
    "related": [
        '<a href="/underwriting/seller-financials/">Verify seller financials</a>',
        '<a href="/blog/assembling-a-comparable-set/">Build matched STR comparables</a>',
        '<a href="/blog/new-listing-ramp-underwriting/">Underwrite the buyer launch ramp</a>',
        '<a href="/blog/str-maximum-offer-price-from-revenue/">Set a maximum offer</a>',
    ],
    "cta_h": "Do not pay for a rebound you cannot verify",
    "cta_p": "We can help you trace the decline, compare alternatives and decide whether this operating STR deserves an offer at all.",
}]


if __name__ == "__main__":
    blog.build(POSTS)
