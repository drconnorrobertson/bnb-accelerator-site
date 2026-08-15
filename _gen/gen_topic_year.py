#!/usr/bin/env python3
"""Compose topic-by-year posts for the non-market clusters.

Each topic carries its own substance, and the year block supplies what was
actually different about that year, so a 2023 pricing post argues from a
cooling market and a 2021 pricing post argues from a market where everything
filled regardless.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import era

TAX_WARN = ("This is an explanation of how the rules worked, not tax advice. My BnB Accelerator, "
            "LLC is a real estate acquisition firm, not a CPA firm. Our independent partner firm "
            'is <a href="https://aetaxadvisors.com/short-term-rentals/" target="_blank" '
            'rel="noopener">AE Tax Advisors</a>.')

# topic key -> dict of the topic's own substance, reused across years
TOPICS = {
    # ------------------------------------------------------------ tax cluster
    "bonus-depreciation": dict(
        cluster="tax-strategy", category="Tax Strategy",
        name="Bonus Depreciation for Short-Term Rentals",
        what=("Bonus depreciation lets a taxpayer deduct a percentage of the cost of qualifying "
              "shorter-life property in the year it is placed in service, rather than spreading it "
              "across the asset's recovery period. For a short-term rental, the qualifying property "
              "is what a cost segregation study reclassifies out of the building: carpet, "
              "appliances, decorative lighting, specialty electrical, furnishings, and land "
              "improvements such as driveways, landscaping and pools."),
        mechanics=[
            "A cost segregation study separates the purchase into components and assigns each to "
            "its correct recovery period, commonly 5, 7 and 15 years for the pieces that come out "
            "of the building shell.",
            "Bonus depreciation then applies to those shorter-life components at whatever "
            "percentage the law allows for the year the property is placed in service.",
            "The remaining structure continues over its long recovery period, 39 years for a "
            "short-term rental with an average stay of seven days or less, or 27.5 for residential "
            "rental property.",
            "None of this is usable against wage income unless the activity clears the seven-day "
            "average period of customer use and the owner materially participates.",
        ],
        pitfalls=[
            "Treating the deduction as free money. It is a timing shift, and on sale the "
            "depreciation taken is recaptured, with Section 1245 recapture on personal property "
            "components taxed as ordinary income.",
            "Commissioning a study before confirming the participation position, which produces a "
            "large loss that is passive and generally suspended.",
            "Assuming the placed-in-service date is the closing date. It is when the property is "
            "ready and available for its intended use, which for a rental generally means "
            "available for booking.",
        ],
        related=[
            '<a href="/tax-strategy/cost-segregation/">Cost segregation explained</a>',
            '<a href="/tax-strategy/material-participation/">Material participation tests</a>',
            '<a href="/blog/depreciation-recapture-str/">Depreciation recapture</a>',
        ],
    ),
    "cost-segregation": dict(
        cluster="tax-strategy", category="Tax Strategy",
        name="Cost Segregation on a Short-Term Rental",
        what=("A cost segregation study is an engineering-based analysis that reclassifies parts of "
              "a building purchase into shorter recovery periods. It does not create a deduction "
              "that did not exist. It moves deductions forward, which matters because a dollar "
              "deducted against a high marginal rate today is worth more than the same dollar "
              "spread across three decades."),
        mechanics=[
            "An engineer or qualified specialist inspects the property and the closing documents "
            "and allocates the purchase price across component classes.",
            "Carpet, appliances, decorative fixtures, specialty electrical and furnishings "
            "typically fall into 5 or 7-year property.",
            "Driveways, walkways, landscaping, fencing, site utilities and pools typically fall "
            "into 15-year land improvements.",
            "The reclassified components then become eligible for bonus depreciation at the rate "
            "in force for the placed-in-service year.",
        ],
        pitfalls=[
            "Doing the study on a property that does not clear the seven-day test, which leaves "
            "the accelerated loss passive and largely stranded.",
            "Planning a short hold. Recapture on sale returns much of what the study deferred, so "
            "the strategy rewards a long hold or an exit structured as a 1031 exchange.",
            "Commissioning the study so late that the report does not exist before the filing "
            "deadline.",
        ],
        related=[
            '<a href="/tax-strategy/cost-segregation/">The full cost segregation guide</a>',
            '<a href="/blog/choosing-cost-segregation-firm/">Choosing a provider</a>',
            '<a href="/blog/look-back-cost-segregation-study/">Look-back studies on property you already own</a>',
        ],
    ),
    "material-participation": dict(
        cluster="tax-strategy", category="Tax Strategy",
        name="Material Participation on a Short-Term Rental",
        what=("Material participation is what converts a loss from passive to non-passive. Clearing "
              "the seven-day average stay test removes the automatic rental classification under "
              "Section 469. It does not by itself make the loss usable against wage income. For "
              "that, the owner has to materially participate under one of seven tests."),
        mechanics=[
            "More than 500 hours of participation in the activity during the year.",
            "Participation constituting substantially all of the participation by all individuals, "
            "including paid managers and cleaners.",
            "More than 100 hours, with no other individual participating more, which is the route "
            "most W-2 earners actually take.",
            "Four further tests covering significant participation activities, prior-year "
            "participation, personal service activities, and a facts and circumstances test.",
        ],
        pitfalls=[
            "Handing everything to a full-service manager, which frequently defeats the 100-hour "
            "test because the manager participates more than the owner.",
            "Reconstructing a participation log in April rather than keeping one contemporaneously.",
            "Counting investor-type activities such as reviewing statements in a non-managerial "
            "capacity, which are specifically excluded.",
        ],
        related=[
            '<a href="/tax-strategy/material-participation/">The seven tests in detail</a>',
            '<a href="/blog/participation-log-that-survives-audit/">Building a participation log</a>',
            '<a href="/management/">How management structure affects participation</a>',
        ],
    ),
    "seven-day-rule": dict(
        cluster="tax-strategy", category="Tax Strategy",
        name="The Seven Day Rule",
        what=("The seven-day rule is the provision that takes a short-term rental outside the "
              "automatic passive classification that applies to rental activities. Under the "
              "Section 469 regulations, an activity where the average period of customer use is "
              "seven days or less is not treated as a rental activity for these purposes."),
        mechanics=[
            "The calculation is total rented days divided by the total number of rental periods "
            "across the tax year.",
            "A property rented 200 days across 50 separate bookings has an average period of "
            "customer use of 4 days, which clears comfortably.",
            "It is an annual average, not a per-booking maximum, so a single long stay does not "
            "break it. Accumulation does.",
            "Clearing it is necessary and not sufficient. Material participation is the second "
            "condition, and both have to hold in the same tax year.",
        ],
        pitfalls=[
            "Accepting snowbird, corporate housing or insurance placement bookings without running "
            "the annual average as you go.",
            "Discovering the average at filing time, when nothing can be done about it.",
            "Assuming a property in a market with naturally long stays can hold the average.",
        ],
        related=[
            '<a href="/tax-strategy/7-day-rule/">The seven day rule in detail</a>',
            '<a href="/blog/7-day-rule-explained/">A longer walkthrough</a>',
            '<a href="/answers/what-is-the-str-loophole/">What is the STR loophole?</a>',
        ],
    ),
    # ------------------------------------------ acquisition & financing cluster
    "str-financing": dict(
        cluster="acquisition-financing", category="Financing",
        name="Financing a Short-Term Rental",
        what=("Financing decides the price range you can shop in, whether you can hold title in an "
              "entity, and how many properties you can own before the structure has to change. It "
              "is the third decision in the sequence, after the tax position and the participation "
              "structure, and before the market."),
        mechanics=[
            "Conventional investment financing is cheapest, requires personal title and a "
            "cooperating debt-to-income ratio, and is commonly capped around ten financed "
            "properties.",
            "DSCR loans qualify on the property's income rather than the borrower's ratio, permit "
            "entity ownership, and price roughly one to two points above conventional.",
            "How a DSCR lender credits short-term rental income is the single largest variable in "
            "whether a deal is financeable: a market estimate, the trailing twelve months, or a "
            "long-term rent schedule.",
            "Most DSCR products carry a prepayment penalty stepping down across three to five "
            "years, which is negotiable against rate.",
        ],
        pitfalls=[
            "Finding a property and then discovering the lender uses a long-term rent schedule.",
            "Treating a lender approval as validation of the deal. The lender is protected at "
            "roughly 75% of value with a foreclosure remedy; the buyer is not.",
            "Ignoring reserve requirements at closing, which are real capital and belong in the "
            "entry cost.",
        ],
        related=[
            '<a href="/financing/dscr-loans/">How DSCR lenders underwrite STRs</a>',
            '<a href="/financing/conventional-vs-dscr/">Conventional versus DSCR</a>',
            '<a href="/blog/reading-a-dscr-term-sheet/">Reading a DSCR term sheet</a>',
        ],
    ),
    "analyzing-deals": dict(
        cluster="acquisition-financing", category="Acquisition",
        name="Analysing a Short-Term Rental Deal",
        what=("Underwriting is the part of this business that actually determines outcomes, and it "
              "is the part most buyers do least. We screen roughly a thousand deals a week and "
              "eliminate about 98%, and almost all of that elimination happens in the analysis "
              "rather than at the viewing."),
        mechanics=[
            "Assemble twelve to twenty genuinely competitive listings: same submarket, same "
            "bedroom count, same amenity tier, and pull twelve months of booked nights and rates.",
            "Model twelve individual monthly revenue figures rather than dividing an annual number "
            "by twelve, because seasonality is the whole shape of the risk.",
            "Build the complete expense stack: debt service at the actual rate, property tax "
            "reassessed at your purchase price, insurance quoted for the address, management "
            "all-in, cleaning per turnover, utilities at rental-use levels, dues, and reserves.",
            "Stress it: revenue at 75%, three lost peak weeks, insurance 40% higher, and for city "
            "properties the long-term rental floor.",
        ],
        pitfalls=[
            "Treating a seller's proforma as data. They are routinely built by extrapolating "
            "peak-season rates across twelve months.",
            "Building a comparable set on bedroom count and distance alone, so the subject property "
            "is compared against inventory it does not actually compete with.",
            "Omitting the maintenance and capital expenditure reserves, which is the most common "
            "reason a projected return exceeds the realised one.",
        ],
        related=[
            '<a href="/revenue-projections/">Building a revenue projection</a>',
            '<a href="/blog/assembling-a-comparable-set/">Assembling a comparable set</a>',
            '<a href="/blog/the-stress-tests-that-matter/">The stress tests that matter</a>',
        ],
    ),
    # ------------------------------------------ revenue optimization cluster
    "pricing-strategy": dict(
        cluster="revenue-optimization", category="Pricing Strategy",
        name="Short-Term Rental Pricing Strategy",
        what=("Pricing is the highest-return hour an owner spends, and the one most often handed to "
              "a tool and forgotten. Revenue is occupancy multiplied by rate, and the two are not "
              "equally valuable because every additional booked night carries a turnover cost."),
        mechanics=[
            "Set a base rate by season and day of week, then apply a premium to high-demand dates "
            "known well in advance.",
            "Hold premium dates firm through the long booking window rather than discounting to "
            "fill early, because that inventory sells closer in at full price.",
            "Introduce reductions on a schedule as dates approach unsold, with a floor set by your "
            "variable cost per booking.",
            "Track net revenue per available night rather than occupancy, because occupancy is the "
            "number that feels like success and is least connected to profit.",
        ],
        pitfalls=[
            "Reactive discounting in a late-booking drive market, where the gap would have filled "
            "at full rate anyway.",
            "Selling compression weeks months out at ordinary rates, which cannot be recovered.",
            "Reading occupancy above roughly 75% outside peak as success rather than as evidence "
            "the property is underpriced.",
        ],
        related=[
            '<a href="/blog/pricing-the-booking-window/">Pricing across the booking window</a>',
            '<a href="/blog/occupancy-versus-rate-which-to-optimize/">Occupancy versus rate</a>',
            '<a href="/blog/airbnb-dynamic-pricing-tools/">Dynamic pricing tools</a>',
        ],
    ),
    # ------------------------------------------------- property management
    "management-systems": dict(
        cluster="property-management", category="Property Management",
        name="Running a Short-Term Rental Remotely",
        what=("Management determines whether a short-term rental is an investment or a second job, "
              "and it interacts directly with the tax strategy, because the participation tests "
              "compare the owner's hours against everyone else's including paid management."),
        mechanics=[
            "Self-management runs roughly 8 to 15 hours a week per property and costs only tools.",
            "A co-host or hybrid arrangement runs 2 to 5 hours a week at 10 to 15% of revenue, and "
            "is the structure most compatible with the material participation tests.",
            "Full service runs under an hour a week at 20 to 35% of revenue, and frequently defeats "
            "the 100-hour participation test.",
            "The systems that separate good operations from bad are dynamic pricing tied to real "
            "demand, photographic cleaning checklists with a deep cleaner bench, and scheduled "
            "preventive maintenance rather than reactive repair.",
        ],
        pitfalls=[
            "Choosing a hybrid structure, intending to manage pricing and guest communication, and "
            "then not doing it, which is worse than full service because nobody is doing it.",
            "Letting the manager hold the listing account, so the reviews and ranking history "
            "belong to them and leaving means starting over.",
            "Comparing managers on headline percentage rather than all-in cost including cleaning "
            "markups and coordination fees.",
        ],
        related=[
            '<a href="/management/">The property management playbook</a>',
            '<a href="/blog/preventive-maintenance-calendar/">The preventive maintenance calendar</a>',
            '<a href="/blog/switching-managers-without-losing-a-season/">Switching managers</a>',
        ],
    ),
    # ---------------------------------------------------- guest experience
    "guest-experience": dict(
        cluster="guest-experience", category="Guest Experience",
        name="Guest Experience and Reviews",
        what=("Reviews are not feedback. They are an input to a ranking algorithm that determines "
              "how many people see the listing, which determines bookings, which determines "
              "reviews. The loop runs in both directions, which is why the first ten matter "
              "disproportionately."),
        mechanics=[
            "Cleanliness is the most frequently cited factor in negative reviews across the "
            "industry, followed by listing accuracy, communication and check-in friction.",
            "None of those four are capital items, which means review performance is a function of "
            "process rather than of property quality.",
            "A structured five-message sequence covering booking, one week out, day before, shortly "
            "after check-in and day before checkout removes most routine questions.",
            "The post-check-in message is the highest-value one, because it surfaces problems while "
            "they are still fixable.",
        ],
        pitfalls=[
            "Overselling in the listing, which guarantees disappointment because guests rate "
            "against expectations rather than an absolute standard.",
            "Responding defensively to a bad review, which signals to every future guest how you "
            "would handle their problem.",
            "Long checkout task lists, which guests who paid a cleaning fee experience as a double "
            "charge.",
        ],
        related=[
            '<a href="/blog/reviews-compound-like-interest/">How reviews compound</a>',
            '<a href="/blog/guest-communication-templates/">The five messages every guest should get</a>',
            '<a href="/blog/setting-expectations-in-the-listing/">Setting expectations</a>',
        ],
    ),
    # ------------------------------------------------------ design cluster
    "design-furnishing": dict(
        cluster="design-furnishing", category="Design & Furnishing",
        name="Furnishing a Short-Term Rental",
        what=("Furnishing is a pricing decision disguised as a decorating decision. The comparable "
              "set in a submarket has already established what a property at a given bedroom count "
              "and price tier looks like, and the job is to meet or beat it rather than to express "
              "a preference."),
        mechanics=[
            "Budget roughly $25,000 to $40,000 for a standard three to four bedroom and $60,000 to "
            "$90,000 or more for a premium five to six bedroom, excluding the hero amenity.",
            "Allocate about a quarter to beds, mattresses and linens, which is the category most "
            "cited in negative reviews, and 2 to 4% to photography, which is the highest-return "
            "line in the budget.",
            "Fund the amenity gap against the actual comparable set at purchase rather than "
            "deferring it, because a property missing what its competitors have underperforms from "
            "day one.",
            "Assume a three to five year replacement cycle on soft goods and seven to ten on case "
            "goods, and budget a recurring refresh rather than a one-time capital event.",
        ],
        pitfalls=[
            "Spending on televisions and electronics, which guests do not book a vacation rental "
            "for, while under-spending on mattresses, which generate the reviews.",
            "Photographing a property before it is finished, which produces images that undersell "
            "it for an entire season.",
            "Ordering furnishing after closing rather than during escrow, where case-goods lead "
            "times of four to eight weeks cost a launch window.",
        ],
        related=[
            '<a href="/design/">The design and furnishing playbook</a>',
            '<a href="/blog/furnishing-budget-by-bedroom-count/">Budget by bedroom count</a>',
            '<a href="/blog/amenity-roi-ranking/">Ranking amenities by return</a>',
        ],
    ),
    # -------------------------------------------------- regulatory cluster
    "regulation": dict(
        cluster="regulatory", category="Regulatory",
        name="Short-Term Rental Regulation",
        what=("Regulation is the risk that never appears in a revenue projection and the one most "
              "likely to end an investment outright. Every jurisdiction sits in one of four "
              "positions, and identifying which answers most of what matters."),
        mechanics=[
            "State preemption of bans, as in Arizona and Idaho, is the strongest protection "
            "available because it removes the possibility that the property becomes unable to "
            "operate legally.",
            "Local control with light regulation is comfortable and offers no guarantee against a "
            "future tightening.",
            "Local control with permit caps cuts both ways: a barrier when buying and a moat once "
            "in, because capped supply protects against rate compression.",
            "Effectively prohibitive jurisdictions, including New York City, Denver, Atlanta and "
            "Charleston for non-owner-occupied purchases, are closed regardless of the numbers.",
        ],
        pitfalls=[
            "Assuming a state-level headline settles a parcel-level question.",
            "Skipping the homeowner association declaration, which binds independently and which "
            "state preemption does not reach.",
            "Treating prior operation as evidence of legality or of transferability.",
        ],
        related=[
            '<a href="/regulations/">Rules by state</a>',
            '<a href="/blog/the-four-regulatory-postures/">The four regulatory postures</a>',
            '<a href="/blog/permits-that-do-not-transfer/">Permits that do not transfer</a>',
        ],
    ),
}


def build(key, year):
    t = TOPICS[key]
    y = era.YEARS[year]
    is_tax = t["cluster"] == "tax-strategy"

    lead = (f"{t['what']} This is where it stood in {year}, which was "
            f"{y['headline']}.")

    sections = [
        (f"What {year} changed", [
            y["summary"],
            y["market_mood"],
            (y["bonus_note"] if is_tax else y["rates"]),
        ]),
        ("How it works", [
            t["what"],
            ("ol", t["mechanics"]),
        ]),
        (f"What that meant in {year} specifically", [
            (y["tax_angle"] if is_tax else y["market_mood"]),
            y["risk"],
            y["advice"],
        ] + ([("warn", TAX_WARN)] if is_tax else [])),
        ("Where it goes wrong", [
            "The failure modes are consistent across years, which is itself useful information: "
            "they are not caused by the market cycle, so a different year does not protect you "
            "from them.",
            ("ul", t["pitfalls"]),
        ]),
        (f"What a buyer should have done in {year}", [
            y["advice"],
            ("The underwriting discipline does not change with the year. Twelve individual monthly "
             "revenue figures from a comparable set you assembled, a complete expense stack "
             "including reserves, and a stress test at 75% of projection that still covers debt "
             "service."),
            ("We screen roughly a thousand deals a week and eliminate about 98% of them. That "
             "ratio has held across every year on this site, through the boom, the correction and "
             "the stabilisation, because it is a function of how listings are selected rather than "
             "of the market."),
        ]),
        ("What generalises, and what does not", [
            (f"Reading a year in isolation is the most common analytical error in this business. "
             f"{y['label']} had its own conditions, and someone who learned the wrong lesson from "
             f"it carried that lesson into a market that no longer rewarded it."),
            ("What generalises is the mechanics above. The definitions, the tests, the sequence and "
             "the failure modes are the same in every year on this site, which is why they are "
             "worth learning properly once rather than relearning each cycle."),
            ("What does not generalise is the environment: the cost of capital, the depth of "
             "supply, the bonus depreciation percentage, and the regulatory posture of a given "
             "jurisdiction. Those change, sometimes abruptly, and a model that treats them as "
             "fixed is a model that was only ever right about one year."),
            ("The practical consequence is to build the analysis so the environment is an input "
             "rather than an assumption. A property that only works at one interest rate, one "
             "occupancy level and one tax treatment is not an investment thesis, it is a bet that "
             "nothing moves."),
        ]),
    ]

    faqs = [
        (f"What was different about {t['name'].lower()} in {year}?",
         y["summary"]),
        (f"What was the main risk in {year}?",
         y["risk"]),
        (f"What was bonus depreciation in {year}?" if is_tax else
         f"What were financing conditions like in {year}?",
         y["bonus_note"] if is_tax else y["rates"]),
    ]

    related = list(t["related"]) + [
        f'<a href="/topics/{t["cluster"]}/">All {era.CLUSTERS[t["cluster"]]["name"].lower()} posts</a>',
    ]

    return dict(
        slug=f"{key}-{year}",
        cluster=t["cluster"],
        category=t["category"],
        year=year,
        title=f"{t['name']} in {year}",
        h1=f"{t['name']} in {year}",
        title_tag=f"{t['name']} in {year}",
        description=(f"{t['name']} in {year}: what changed that year, how the mechanics work, "
                     f"where it goes wrong, and what a buyer should have done."),
        lead=lead,
        sections=sections,
        faqs=faqs,
        related=related,
    )


def all_posts():
    return [build(k, y) for k in TOPICS for y in sorted(era.YEARS)]


if __name__ == "__main__":
    p = all_posts()
    sys.path.insert(0, HERE := os.path.dirname(os.path.abspath(__file__)))
    import blog
    wc = [blog.word_count(x) for x in p]
    print(f"{len(p)} topic-year posts, {min(wc)}-{max(wc)} words, avg {sum(wc)//len(wc)}")
