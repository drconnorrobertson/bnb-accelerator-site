#!/usr/bin/env python3
"""Quarterly market update posts, 2021 to 2026.

These are the "what changed this quarter" posts: platform policy, travel
patterns, the seasonal shape of demand, and what an owner should have done
about it. Four a year across six years.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import era

QUARTERS = {
    1: dict(
        name="Q1", months="January through March",
        season=("Q1 is the widest spread of the year between markets. Southwest Florida, the "
                "Arizona desert and the Gulf snowbird markets are at peak, while the Smokies, the "
                "Poconos and most lake markets are in their thinnest stretch. A portfolio that "
                "peaks together has one revenue season; a portfolio built across both shapes has "
                "two."),
        focus=("Q1 is also when last year's tax position becomes final and this year's becomes "
               "changeable. The participation log either exists or it does not, and the running "
               "average period of customer use for the new year starts accumulating from January."),
        actions=[
            "Compute last year's average period of customer use from booking-level data before "
            "filing, rather than estimating it.",
            "Total participation hours by person and by property, including managers and cleaners, "
            "because two of the seven tests depend on that comparison.",
            "Start this year's log in January rather than reconstructing it in December.",
            "Book preventive maintenance for the spring: HVAC service before summer, and pool or "
            "hot tub servicing before the season turns.",
            "Review pricing for the coming peak against the comparable set as it stands now, not "
            "as it stood when you bought.",
        ],
    ),
    2: dict(
        name="Q2", months="April through June",
        season=("Q2 is when the summer-peaking markets wake up and the winter-peaking ones go "
                "quiet. Spring break carries the Gulf into April, the Smokies and the Poconos "
                "ramp through May and June, and the desert markets begin their descent toward a "
                "trough that will last until October."),
        focus=("Q2 is the last window to fix anything before peak season. Furnishing refreshes, "
               "photography, amenity gaps and maintenance all cost far less in May than in July, "
               "because in May they cost money and in July they cost bookings."),
        actions=[
            "Reshoot photography if anything changed, and reshoot regardless if the images are "
            "more than about two years old.",
            "Audit the amenity gap against the current comparable set rather than the one that "
            "existed at purchase.",
            "Set minimum stays and premium floor rates across the peak weeks before demand "
            "arrives, not after.",
            "Confirm the cleaner bench has depth for same-day turnovers in peak season.",
            "Check the reserve. Peak season is when a failure is most expensive and most likely.",
        ],
    ),
    3: dict(
        name="Q3", months="July through September",
        season=("Q3 is peak for the mountain, lake and beach markets and the trough for the "
                "desert. It is also hurricane season on the Gulf and the Atlantic, which is the "
                "single largest source of disrupted peak weeks in the whole calendar."),
        focus=("Q3 is an operating quarter rather than a strategic one. The decisions that "
               "determine how it goes were made in Q2, and what is left is execution: turnovers, "
               "guest response, pricing against real-time demand, and handling whatever breaks."),
        actions=[
            "Watch net revenue per available night rather than occupancy, because occupancy at "
            "peak flatters everything.",
            "Respond to guest problems within minutes even when resolution takes hours, because "
            "response speed is the largest factor in whether a problem becomes a bad review.",
            "Ask every departing guest for a review, once, without pressure.",
            "For coastal properties, confirm the storm plan and the insurance position before the "
            "peak of the season rather than during it.",
            "Log participation hours weekly. Q3 is when the hours actually happen and when they "
            "are least likely to be recorded.",
        ],
    ),
    4: dict(
        name="Q4", months="October through December",
        season=("Q4 splits. October is a genuine peak in the mountain markets on leaf season and "
                "in the Hill Country on the harvest window. November is thin nearly everywhere. "
                "The winter holidays are a compression period in cabin and ski markets, and the "
                "desert and snowbird markets begin their climb."),
        focus=("Q4 is the planning quarter. The tax year is closing, next year's calendar is "
               "opening, and the decisions made in December determine which tax year a purchase "
               "lands in and whether the property is placed in service in time."),
        actions=[
            "Confirm the running average period of customer use for the year and manage the "
            "remaining bookings accordingly.",
            "If a purchase is intended for this tax year, confirm it will be placed in service, "
            "meaning furnished, permitted and available for booking, before 31 December.",
            "Do not rush a December purchase to capture a deduction. A bad property bought for a "
            "tax reason is a bad property for far longer than a tax year.",
            "Schedule the trough for maintenance, deep cleaning and furnishing refresh, because "
            "that work has to happen somewhere and January is cheaper than July.",
            "Rebuild the reserve if the year drew it down.",
        ],
    ),
}


def build(q, year):
    y = era.YEARS[year]
    qd = QUARTERS[q]
    sections = [
        (f"What was happening across the market", [
            y["summary"],
            y["market_mood"],
            y["rates"],
        ]),
        (f"The seasonal shape of {qd['name']}", [
            qd["season"],
            ("Reading a quarter in isolation is how owners talk themselves into bad decisions. A "
             "thin quarter in a seasonal market is not underperformance, it is the shape of the "
             "asset, and it should have been in the model at purchase."),
        ]),
        (f"What {qd['name']} is actually for", [
            qd["focus"],
            y["tax_angle"],
            ("warn", "This is an explanation rather than tax advice. My BnB Accelerator, LLC is a "
                     "real estate acquisition firm, not a CPA firm. Our independent partner firm is "
                     '<a href="https://aetaxadvisors.com/short-term-rentals/" target="_blank" '
                     'rel="noopener">AE Tax Advisors</a>.'),
        ]),
        (f"The {qd['name']} checklist", [
            ("ol", qd["actions"]),
        ]),
        (f"The risk carried into {qd['name']} {year}", [
            y["risk"],
            y["advice"],
            ("The consistent thread across every quarter on this site is that the environment "
             "changes and the discipline does not. Twelve individual monthly revenue figures, a "
             "complete expense stack including reserves, and a stress test at 75% of projection "
             "that still covers debt service."),
        ]),
        ("What to carry into the next quarter", [
            (f"{qd['months']} is one quarter of a business that is measured annually. The number "
             f"that matters is not what this quarter produced but whether the year is tracking to "
             f"the model, and whether the reserve is intact."),
            ("If the year is behind the model, the useful question is which input was wrong: "
             "revenue, cost, or the assumption about the market. Each has a different fix, and "
             "discounting is the right answer to only one of them."),
            ("If the year is ahead, the useful question is whether that is the property or the "
             "market. A property outperforming a flat market is a property to buy more of. A "
             "property matching a rising market has told you nothing yet."),
        ]),
    ]
    return dict(
        slug=f"str-market-update-{qd['name'].lower()}-{year}",
        cluster="market-updates",
        category="Market Update",
        year=year,
        title=f"STR Market Update: {qd['name']} {year}",
        h1=f"Short-Term Rental Market Update: {qd['name']} {year}",
        title_tag=f"STR Market Update {qd['name']} {year}: What Changed",
        description=(f"The short-term rental market in {qd['name']} {year}: what changed, the "
                     f"seasonal shape of {qd['months'].lower()}, the tax position, and the "
                     f"quarter's checklist."),
        lead=(f"{qd['name']} {year} in short-term rentals. {year} was {y['headline']}, and "
              f"{qd['months'].lower()} has its own shape on top of that. Here is what moved, what "
              f"it meant for an owner, and what the quarter was actually for."),
        sections=sections,
        faqs=[
            (f"What happened in the STR market in {qd['name']} {year}?", y["summary"]),
            (f"Which markets peak in {qd['months'].lower()}?", qd["season"]),
            (f"What was bonus depreciation in {year}?", y["bonus_note"]),
        ],
        related=[
            '<a href="/topics/market-updates/">All market updates</a>',
            '<a href="/topics/market-analysis/">Market analysis by city and year</a>',
            '<a href="/revenue-projections/">Building a revenue projection</a>',
            '<a href="/blog/what-to-do-in-a-slow-season/">Managing the trough</a>',
        ],
    )


def all_posts():
    return [build(q, y) for y in sorted(era.YEARS) for q in (1, 2, 3, 4)]


if __name__ == "__main__":
    import blog
    p = all_posts()
    wc = [blog.word_count(x) for x in p]
    print(f"{len(p)} market-update posts, {min(wc)}-{max(wc)} words, avg {sum(wc)//len(wc)}")
