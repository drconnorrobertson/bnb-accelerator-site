#!/usr/bin/env python3
"""Per-year context for backdated posts.

Every generated post is composed from a year block and a subject block, so a
2021 Gatlinburg post and a 2024 Gatlinburg post argue different things because
the rate environment, the supply picture and the tax law genuinely differed.

Bonus depreciation percentages follow the TCJA phase-down and then the OBBBA
restoration, which is the single most consequential tax fact for this audience
across the period:
  2017-2022  100%
  2023        80%
  2024        60%
  2025        40% for property acquired on or before 19 Jan 2025;
              100% for property acquired and placed in service after that date
  2026       100% under OBBBA for qualifying acquisitions
"""

YEARS = {
    2021: dict(
        label="2021",
        bonus="100%",
        bonus_note="Bonus depreciation was still at 100% under the TCJA schedule, and would remain there through 2022 before the phase-down began.",
        rates="Mortgage rates spent most of the year near historic lows, which made financing cheap and competition for property fierce.",
        headline="the year domestic travel came back faster than anyone had modelled",
        summary=(
            "2021 was the year short-term rental demand came back violently. Domestic leisure "
            "travel recovered far faster than international, drive-to markets absorbed the "
            "overflow, and guests who would previously have booked a hotel booked a whole house "
            "instead. Supply had not caught up, so occupancy and nightly rates rose together, "
            "which almost never happens."),
        market_mood=(
            "Demand outran supply for most of the year. Properties that would have struggled in "
            "2019 filled at rates their owners had not thought possible, which made the market "
            "look easier than it was."),
        risk=(
            "The risk nobody priced in 2021 was that the conditions were exceptional rather than "
            "normal. Buyers who underwrote on 2021 revenue and 2021 financing costs were building "
            "a model on the best year the asset class had ever had."),
        tax_angle=(
            "With bonus depreciation still at 100%, a cost segregation study on a property placed "
            "in service that year could accelerate the full eligible amount into year one, which "
            "made the strategy unusually powerful for high earners."),
        advice=(
            "The right discipline in 2021 was to underwrite on pre-pandemic revenue rather than "
            "current revenue, and to buy on a basis that would survive normalisation."),
    ),
    2022: dict(
        label="2022",
        bonus="100%",
        bonus_note="2022 was the final year of 100% bonus depreciation under the TCJA schedule before the step-down to 80% in 2023.",
        rates="Rates rose sharply through the year as the Federal Reserve tightened, and the cost of financing a purchase in December was very different from March.",
        headline="the year cheap money ended and the phase-down clock started",
        summary=(
            "2022 split into two halves. The first looked like 2021: strong demand, rising rates, "
            "aggressive competition for inventory. The second was defined by the fastest rise in "
            "borrowing costs in decades, which changed what a property had to earn to work."),
        market_mood=(
            "Revenue held up better than most expected while the cost of capital rose underneath "
            "it. Deals underwritten in the spring frequently did not pencil by the autumn on the "
            "same purchase price."),
        risk=(
            "Supply caught up in several markets during 2022. The properties that struggled were "
            "the ones bought at 2021 prices on the assumption that 2021 occupancy would persist."),
        tax_angle=(
            "2022 was the last year at 100% bonus depreciation, which pulled some purchases "
            "forward into December as buyers tried to place property in service before the "
            "step-down."),
        advice=(
            "The discipline that mattered in 2022 was stress testing against a higher rate and a "
            "normalised occupancy at the same time, rather than one or the other."),
    ),
    2023: dict(
        label="2023",
        bonus="80%",
        bonus_note="Bonus depreciation stepped down to 80% for property placed in service in 2023, the first year of the TCJA phase-down.",
        rates="Borrowing costs stayed high all year, and the gap between what sellers wanted and what the numbers supported was the defining feature of the market.",
        headline="the year the market cooled and underwriting started to matter again",
        summary=(
            "2023 was the correction. Rates stayed high, supply that had been added during the "
            "boom arrived on the market, and occupancy in several previously unstoppable markets "
            "came down. The phrase that circulated was Airbnbust, which was overstated, and the "
            "underlying shift was real: revenue per property fell in markets where supply had "
            "grown fastest."),
        market_mood=(
            "The spread between well-run and poorly-run properties widened sharply. In a market "
            "where everything fills, operational quality is invisible. In 2023 it was the whole "
            "difference."),
        risk=(
            "The properties that got into trouble in 2023 were bought at peak prices with thin "
            "reserves in markets that were absorbing new supply. None of those three alone was "
            "fatal. Together they were."),
        tax_angle=(
            "With bonus depreciation at 80%, a cost segregation study still produced a large "
            "first-year deduction, and the arithmetic changed enough that the study cost had to "
            "be weighed more carefully on smaller purchases."),
        advice=(
            "2023 rewarded buyers who could underwrite honestly and walk away. Basis mattered more "
            "than it had in years, because there was no longer a rising tide to cover an overpay."),
    ),
    2024: dict(
        label="2024",
        bonus="60%",
        bonus_note="Bonus depreciation fell to 60% for property placed in service in 2024, continuing the TCJA phase-down.",
        rates="Financing costs remained elevated relative to the 2021 window, and buyers had adjusted their expectations rather than waiting for a return to cheap money.",
        headline="the year the market stabilised and the tax benefit shrank",
        summary=(
            "2024 was the stabilisation. The panic of 2023 faded, supply growth slowed in most "
            "markets, and occupancy found a floor. What changed most was the tax side: bonus "
            "depreciation at 60% meant the same property produced a materially smaller first-year "
            "deduction than it would have three years earlier."),
        market_mood=(
            "Buyers who had waited for prices to collapse were still waiting. What actually "
            "happened was a market that stopped falling and started rewarding operators who had "
            "systems rather than luck."),
        risk=(
            "The live risk in 2024 was regulatory rather than economic. Several resort markets "
            "tightened permits, and the direction of travel in high-pressure housing markets was "
            "consistently toward restriction."),
        tax_angle=(
            "At 60% bonus depreciation, the strategy still worked and the margin was thinner. "
            "Buyers doing the arithmetic properly found that purchase basis and marginal rate "
            "mattered more than they had when the deduction was 100%."),
        advice=(
            "2024 was a year to buy on fundamentals rather than on the tax benefit, because the "
            "tax benefit alone no longer carried a marginal deal."),
    ),
    2025: dict(
        label="2025",
        bonus="40% or 100%",
        bonus_note=(
            "2025 was the split year. Property acquired on or before 19 January 2025 stayed on the "
            "phase-down at 40%. The One Big Beautiful Bill Act, signed in July, permanently "
            "restored 100% bonus depreciation for qualifying property acquired and placed in "
            "service after 19 January 2025."),
        rates="Financing costs had settled into a range buyers had learned to underwrite around rather than wait out.",
        headline="the year the acquisition date on your closing statement started to matter enormously",
        summary=(
            "2025 was the year the tax calculation split in two. Property acquired on or before "
            "19 January stayed on the old phase-down at 40%. Property acquired after that date, "
            "once OBBBA passed in July, qualified for 100% bonus depreciation again. The same "
            "property, the same buyer, a different acquisition date, and a materially different "
            "first-year deduction."),
        market_mood=(
            "Supply growth had slowed enough that well-selected markets were producing consistent "
            "results again, and the gap between markets widened as regulation diverged."),
        risk=(
            "The risk in 2025 was assuming the restored bonus depreciation applied to a property "
            "already owned or already under contract before the cut-off. Acquisition date, not "
            "placed-in-service date alone, governs which schedule applies."),
        tax_angle=(
            "For anyone buying after 19 January 2025, the restoration of 100% bonus depreciation "
            "returned the strategy to full strength for the first time since 2022."),
        advice=(
            "2025 rewarded buyers who confirmed with their CPA which schedule their specific "
            "acquisition fell under before modelling a deduction."),
    ),
    2026: dict(
        label="2026",
        bonus="100%",
        bonus_note="100% bonus depreciation applies under OBBBA to qualifying property acquired and placed in service after 19 January 2025, and it is permanent rather than scheduled to phase down.",
        rates="Buyers are underwriting to current financing costs rather than to a hoped-for future, which has made pricing more rational than it was in either the boom or the correction.",
        headline="the year the tax strategy is back at full strength and market selection decides everything",
        summary=(
            "2026 is the first full year with 100% bonus depreciation permanently restored under "
            "OBBBA. For a high earner buying a property that clears the seven-day average stay "
            "test and where they materially participate, the first-year deduction is back to where "
            "it was in 2021. What is not back to 2021 is the market: supply is deeper, regulation "
            "is tighter in the places that tightened, and buying badly is no longer covered by a "
            "rising tide."),
        market_mood=(
            "The spread between markets is wider than at any point in this period. Arizona and "
            "Tennessee are workable and stable. California and much of Colorado are not, for "
            "reasons that have nothing to do with demand."),
        risk=(
            "The risk in 2026 is the same one that has been true throughout: buying on the tax "
            "benefit rather than on the property. A permanent 100% deduction makes a good purchase "
            "excellent and does not make a bad purchase acceptable."),
        tax_angle=(
            "With 100% bonus depreciation permanent, the constraint has shifted back to the "
            "participation tests and the seven-day average, which are operational rather than "
            "legislative and therefore inside the owner's control."),
        advice=(
            "2026 rewards market selection and basis. The tax side is as favourable as it has "
            "ever been, which means the differentiator is everything else."),
    ),
}

# Named the way the audience searches for them.
CLUSTERS = {
    "market-analysis": dict(
        name="STR Market Analysis",
        slug="market-analysis",
        blurb="City-by-city market analysis and how each market moved year by year.",
        intro="Twenty markets, tracked across six years. What each one was in 2021, what happened to it through the correction, and where it stands now.",
    ),
    "tax-strategy": dict(
        name="Tax Strategy",
        slug="tax-strategy",
        blurb="Cost segregation, bonus depreciation, material participation, the seven day rule and OBBBA.",
        intro="The mechanics of the short-term rental tax strategy, and how the bonus depreciation schedule changed underneath it between 2021 and 2026.",
    ),
    "acquisition-financing": dict(
        name="Acquisition & Financing",
        slug="acquisition-financing",
        blurb="Finding deals, analysing properties, loan types, negotiation and closing.",
        intro="How to find a property worth buying, how to underwrite it honestly, and how the financing options changed as rates did.",
    ),
    "design-furnishing": dict(
        name="Design & Furnishing",
        slug="design-furnishing",
        blurb="Interior design, amenities, photography and staging that changes booking decisions.",
        intro="Furnishing is a pricing decision disguised as a decorating decision. These are the choices that move the nightly rate.",
    ),
    "revenue-optimization": dict(
        name="Revenue Optimization",
        slug="revenue-optimization",
        blurb="Pricing strategy, dynamic pricing, occupancy and average daily rate.",
        intro="Occupancy and rate are not equally valuable, and the operators who understand why consistently out-earn the ones who do not.",
    ),
    "guest-experience": dict(
        name="Guest Experience",
        slug="guest-experience",
        blurb="Reviews, communication, cleaning and check-in.",
        intro="Reviews compound like interest. Everything in this cluster is about the inputs to that loop.",
    ),
    "property-management": dict(
        name="Property Management",
        slug="property-management",
        blurb="SOPs, automation, remote management and co-hosting.",
        intro="Management is the decision that determines whether a short-term rental is an investment or a second job.",
    ),
    "regulatory": dict(
        name="Regulatory",
        slug="regulatory",
        blurb="STR laws by state and city, HOA rules, permits and insurance.",
        intro="Regulation is the risk that never appears in a revenue projection, and the one most likely to end an investment outright.",
    ),
    "case-studies": dict(
        name="Case Studies",
        slug="case-studies",
        blurb="Client results, before and after, and full ROI breakdowns.",
        intro="Documented client outcomes with the underwriting that produced them, and what generalises from each.",
    ),
    "market-updates": dict(
        name="Market Updates",
        slug="market-updates",
        blurb="Airbnb policy changes, travel trends and seasonal analysis.",
        intro="What changed in the industry each quarter, and what it meant for an owner rather than for a headline.",
    ),
}

# Existing hand-written and previously generated posts map onto clusters by
# the category shown in their eyebrow.
CATEGORY_TO_CLUSTER = {
    "Market Analysis": "market-analysis",
    "Tax Strategy": "tax-strategy",
    "Financing": "acquisition-financing",
    "Acquisition": "acquisition-financing",
    "Getting Started": "acquisition-financing",
    "Strategy": "acquisition-financing",
    "Design & Furnishing": "design-furnishing",
    "Revenue Optimization": "revenue-optimization",
    "Pricing Strategy": "revenue-optimization",
    "Operations": "property-management",
    "Property Management": "property-management",
    "Guest Experience": "guest-experience",
    "Regulatory": "regulatory",
    "Case Study Breakdown": "case-studies",
    "Case Study": "case-studies",
}


def cluster_for(category):
    return CATEGORY_TO_CLUSTER.get(category, "acquisition-financing")
