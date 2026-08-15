#!/usr/bin/env python3
"""Generate one page per documented client outcome, plus the hub index.

Every client, market, bedroom count, purchase price and cash flow figure here
was taken from the live mybnbaccelerator.com case study page. Nothing is
invented. Where the live page published only property facts and no revenue
number, the page says so rather than filling the gap with a projection.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tpl

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
PUBLISHED = "2026-08-15"

# slug, name, initial, market, state, market_page, beds, price, prop_type,
# headline, narrative paragraphs, spec extras, result banner, faqs
CASES = [
    dict(
        slug="victoria-sevierville-tn-9br-cabin",
        name="Victoria",
        initial="V",
        market="Sevierville, Tennessee",
        market_link="/markets/smoky-mountains/",
        beds=9,
        price="$1,375,000",
        prop_type="9BR luxury cabin",
        category="Mountain cabin",
        headline="A nine-bedroom Smokies cabin that cleared roughly $20,000 in a single month",
        summary="Victoria bought a nine-bedroom luxury cabin in Sevierville for $1,375,000. In June, the property produced about $38,000 in bookings against roughly $18,000 in expenses, leaving approximately $20,000 in cash flow for the month.",
        result="Roughly $20,000 in cash flow in a single month during June peak season, from about $38,000 in bookings against $18,000 in expenses. At the six-month mark the property was tracking ahead of the underwriting.",
        metrics=[("Peak month bookings", "~$38,000", True),
                 ("Peak month expenses", "~$18,000", False),
                 ("Peak month cash flow", "~$20,000", True)],
        body=[
            "Victoria came to us wanting scale rather than a starter property. That instinct is right in the Smokies and dangerous everywhere else. Large-group cabins in the Sevierville and Gatlinburg corridor are the highest gross-revenue asset class we underwrite anywhere in the country, because a nine-bedroom cabin is not competing with other rentals, it is competing with hotels that cannot put twenty-six people from the same family under one roof.",
            "They are also the easiest properties in America to overpay for. Sellers of large cabins know exactly what a nine-bedroom with a mountain view books on a good July weekend, and their listing packets are built around that number. The proforma you get handed is almost always assembled from peak-season rates extrapolated across twelve months, which produces a revenue figure the property will never actually hit.",
            "We underwrote this one against actual booked-night data for nine-bedroom inventory in the same corridor, not the seller's spreadsheet. That produced a materially lower revenue expectation than the listing implied, which in turn produced a materially lower number we were willing to pay. The purchase closed at $1,375,000.",
            "The first summer confirmed the model. June produced roughly $38,000 in gross bookings. After management, cleaning, supplies, utilities, insurance, property tax and debt service, about $18,000 went back out, leaving approximately $20,000 in cash flow for the month.",
            "The important caveat, and we say this to every client looking at seasonal mountain inventory, is that a $20,000 June is not a $240,000 year. Smokies cabins earn a disproportionate share of annual revenue between June and October and again over the winter holidays. The underwriting has to be built on the annual shape of the market, not on the best month, or the shoulder season becomes a nasty surprise in year one.",
        ],
        faqs=[
            ("How much did Victoria's Sevierville cabin cost?",
             "The purchase price was $1,375,000 for a nine-bedroom luxury cabin in Sevierville, Tennessee."),
            ("How much cash flow did the property produce?",
             "Approximately $20,000 in a single month during June peak season, from roughly $38,000 in bookings against about $18,000 in expenses. That is one month on a seasonal property, not one twelfth of an annual figure."),
            ("Why buy a nine-bedroom rather than a smaller cabin?",
             "Large-bedroom-count cabins in the Smokies capture family reunions, multi-family trips and corporate retreats that four-bedroom properties cannot bid for. The tradeoff is a much higher purchase price, higher turnover cost, and a market where overpaying is easy because sellers price on peak-season performance."),
        ],
    ),
    dict(
        slug="peter-eck-ibm-partner-six-properties",
        name="Peter E.",
        initial="P",
        market="Shady Shores TX and Santa Rosa Beach FL",
        market_link="/markets/destin/",
        beds=13,
        price="$3,199,000 across three properties",
        prop_type="Three-property portfolio",
        category="Portfolio",
        headline="An IBM Associate Partner on his sixth property with us",
        summary="Peter E. is an Associate Partner at IBM who has closed six properties with BNB Accelerator across four years, including a 5BR in Shady Shores TX at $949,000 and two 4BR properties in Santa Rosa Beach FL at $1,100,000 and $1,150,000.",
        result="Three properties closed in 2023 and 2024, with three more planned for 2025 and 2026. Six total transactions across four years, which makes him the clearest single data point behind our 80% repeat buyer rate.",
        metrics=[("Properties closed", "6", True),
                 ("2023-2024 acquisitions", "3", False),
                 ("Combined price, latest 3", "$3,199,000", False)],
        properties=[
            ("Shady Shores, Texas", "5BR", "$949,000"),
            ("Santa Rosa Beach, Florida", "4BR", "$1,100,000"),
            ("Santa Rosa Beach, Florida", "4BR", "$1,150,000"),
        ],
        body=[
            "Peter is an Associate Partner at IBM. He is the client this business is actually built for: a high earner with a demanding career, a tax bill that grows every year, and no interest whatsoever in becoming a full-time real estate operator on nights and weekends.",
            "He has now closed six properties with us across four years. Three of those closed in 2023 and 2024, and three more are planned across 2025 and 2026. The three most recent are a five-bedroom in Shady Shores, Texas at $949,000, and two four-bedroom properties in Santa Rosa Beach, Florida at $1,100,000 and $1,150,000.",
            "A repeat buyer is the only unfakeable metric in this industry. Anyone can produce a testimonial from a first purchase, because at closing the client has nothing but optimism and a set of projections. Nobody buys a second property from a firm that got the first one wrong, and nobody buys a sixth unless the first five performed close enough to the model that the process itself has become boring.",
            "The portfolio also shows the diversification logic we push on multi-property clients. Shady Shores is a Dallas-Fort Worth lake market with a metro-driven weekend guest base. Santa Rosa Beach is a Gulf Coast beach market with a very different seasonal curve and a very different guest. When a hurricane season or a regional economic wobble hits one, the other is generally unaffected. Buying three properties in the same submarket is not a portfolio, it is one bet written three times.",
            "For a client at Peter's income level, the tax structure is doing as much work as the cash flow. Each acquisition paired with a cost segregation study produces a first-year deduction large enough to matter against W-2 income, provided the seven-day average stay and material participation tests are met for that year. That is the mechanism that lets a portfolio compound this fast without the client leaving IBM.",
        ],
        faqs=[
            ("How many properties has Peter E. bought with BNB Accelerator?",
             "Six across four years, with three closed in 2023 and 2024 and three more planned for 2025 and 2026."),
            ("Why does a repeat buyer rate matter more than a testimonial?",
             "A first-purchase testimonial is collected at closing, before the property has performed. A repeat purchase is collected after the client has lived with the outcome for a year or more. About 80% of our clients buy again."),
            ("Should a multi-property investor buy in the same market?",
             "Generally no. Concentrating in one submarket means one regulatory change, one hurricane season, or one supply glut hits the whole portfolio. Peter's properties span a Texas lake market and a Florida Gulf beach market, which have different seasons and different guest bases."),
        ],
    ),
    dict(
        slug="ashley-billy-fort-walton-beach-fl",
        name="Ashley & Billy",
        initial="A",
        market="Fort Walton Beach, Florida",
        market_link="/markets/destin/",
        beds=4,
        price="$630,000",
        prop_type="4BR beach house",
        category="Beach",
        headline="Almost 80 nights booked within 21 days of going live",
        summary="Ashley and Billy bought a four-bedroom in Fort Walton Beach, Florida for $630,000 and had close to 80 nights on the calendar within 21 days of the listing going live.",
        result="Close to 80 nights booked within 21 days of launch. The gap between closing and first booking is where most new short-term rentals lose their first year, and this launch closed that gap almost entirely.",
        metrics=[("Nights booked in first 21 days", "~80", True),
                 ("Purchase price", "$630,000", False),
                 ("Bedrooms", "4", False)],
        body=[
            "The most expensive month in a short-term rental's life is the one between closing and the first booking. Mortgage, insurance, utilities and property tax all start immediately. Revenue does not. Owners who close in April and do not go live until July have paid three months of carry for nothing, and they have also missed the window to accumulate the early reviews that Airbnb's ranking algorithm weighs most heavily.",
            "Ashley and Billy closed on a four-bedroom in Fort Walton Beach at $630,000 and had close to 80 nights on the calendar within 21 days of the listing going live. That is not luck. Furnishing, photography, listing copy, pricing setup and channel distribution were sequenced to run in parallel during the escrow period rather than starting after the keys changed hands.",
            "Fort Walton Beach rewards that speed more than most markets. It sits on the Emerald Coast next to Destin but prices materially below it, which means a four-bedroom here competes for the same Gulf-beach guest at a purchase price that supports much better cash-on-cash returns. The Eglin Air Force Base presence also adds a shoulder-season demand floor that pure vacation markets do not have.",
            "The launch pattern matters beyond the first month. Airbnb's search ranking heavily favors listings with recent booking velocity and a review count above the low single digits. A property that stacks 80 nights and the reviews that follow in its first three weeks enters its first full season ranked like an established listing rather than a new one, and that advantage compounds through the entire first year.",
        ],
        faqs=[
            ("How fast can a new short-term rental start booking?",
             "Ashley and Billy had close to 80 nights booked within 21 days of their Fort Walton Beach listing going live. That requires furnishing, photography, listing copy and pricing to be prepared during escrow rather than after closing."),
            ("Why is Fort Walton Beach cheaper than Destin?",
             "Fort Walton Beach sits on the same Emerald Coast stretch but carries lower purchase prices, which improves cash-on-cash return for a comparable guest profile. Eglin Air Force Base also supplies non-vacation demand that softens the shoulder season."),
            ("Does launch speed affect long-term performance?",
             "Yes. Airbnb ranking weights recent booking velocity and review count, so a listing that fills its first weeks enters peak season ranked like an established property instead of a new one."),
        ],
    ),
    dict(
        slug="antonio-fort-myers-fl-6br",
        name="Antonio",
        initial="A",
        market="Fort Myers, Florida",
        market_link="/markets/cape-coral/",
        beds=6,
        price="$1,725,000",
        prop_type="6BR waterfront",
        category="Beach",
        headline="$17,000 of February cash flow on a Southwest Florida six-bedroom",
        summary="Antonio bought a six-bedroom in Fort Myers, Florida for $1,725,000. February produced over $36,000 in bookings against about $19,000 in expenses, leaving roughly $17,000 in cash flow for the month.",
        result="Roughly $17,000 in cash flow in February, from over $36,000 in bookings against about $19,000 in expenses. February is peak snowbird season in Southwest Florida, which is exactly why the property was underwritten around that curve.",
        metrics=[("February bookings", "$36,000+", True),
                 ("February expenses", "~$19,000", False),
                 ("February cash flow", "~$17,000", True)],
        body=[
            "Southwest Florida runs on an inverted calendar compared with most of the country. While the Smokies and the Poconos are earning their money in July, Fort Myers is earning it in February, when the entire northern half of the continent is looking for somewhere warm with a pool.",
            "Antonio bought a six-bedroom in Fort Myers at $1,725,000. In February the property produced over $36,000 in gross bookings. After management, cleaning, supplies, utilities, insurance, property tax and debt service, about $19,000 went back out, leaving roughly $17,000 in cash flow for that month.",
            "The size is doing specific work here. A six-bedroom in Southwest Florida captures multi-generational snowbird stays, where three or four related households book one house for two to four weeks rather than separate hotel rooms. Those bookings have long durations, low turnover cost per night, and guests who plan a year ahead, which is a very different revenue profile from the weekend-driven pattern of a two-bedroom condo.",
            "Underwriting an inverted-season market takes discipline in the other direction from the mountains. August in Fort Myers is hot, humid, and in the middle of hurricane season. Revenue in the late-summer trough is a fraction of February, and insurance in coastal Florida has repriced sharply in recent years. Both belong in the model at purchase, not as a discovery in year one.",
        ],
        faqs=[
            ("What did Antonio's Fort Myers property cost?",
             "It was a six-bedroom purchased for $1,725,000 in Fort Myers, Florida."),
            ("How much cash flow did it produce?",
             "About $17,000 in February, from over $36,000 in bookings against roughly $19,000 in expenses. February is the peak of the Southwest Florida snowbird season, so it is a high month rather than a typical one."),
            ("Why does Southwest Florida peak in winter?",
             "Demand is driven by snowbirds escaping northern winters, so January through March are the strongest months and late summer is the weakest. Hurricane season and coastal insurance costs both need to be modeled before purchase."),
        ],
    ),
    dict(
        slug="shardul-mayanka-panama-city-beach-fl",
        name="Shardul & Mayanka",
        initial="S",
        market="Panama City Beach, Florida",
        market_link="/markets/panama-city-beach/",
        beds=4,
        price="$530,000",
        prop_type="4BR beach house",
        category="Beach",
        headline="A four-bedroom Panama City Beach entry at $530,000",
        summary="Shardul and Mayanka purchased a four-bedroom in Panama City Beach, Florida for $530,000, one of the lower entry points in our Gulf Coast inventory.",
        result="A $530,000 entry into a Gulf Coast beach market, well below the Destin and 30A price band for a comparable bedroom count and a comparable guest.",
        metrics=[("Purchase price", "$530,000", False),
                 ("Bedrooms", "4", False),
                 ("Market", "Panama City Beach", False)],
        body=[
            "Panama City Beach is the value entry into Gulf Coast beach ownership. A four-bedroom here costs a fraction of the equivalent property forty miles east on 30A, and while the nightly rate is lower, the ratio between what you pay and what the property earns is frequently better.",
            "Shardul and Mayanka bought a four-bedroom at $530,000. For a dual-income household making a first move into short-term rentals, that entry point does something important: it keeps the down payment and the furnishing budget inside a range where a slow first quarter is an annoyance rather than a crisis.",
            "The four-bedroom configuration is deliberate. In Gulf beach markets, the jump from three bedrooms to four moves a property from the couples-and-small-family bracket into the two-families-splitting-a-house bracket, where nightly rates rise faster than the purchase price does. It is the single highest-leverage bedroom count in most beach markets.",
            "Panama City Beach also carries a longer season than markets further north. Spring break, summer, and a substantial autumn shoulder driven by warm Gulf water into October give the calendar more billable weeks than a comparable Atlantic property, which is what makes the lower nightly rate work.",
        ],
        faqs=[
            ("How much did the Panama City Beach property cost?",
             "Shardul and Mayanka bought a four-bedroom in Panama City Beach, Florida for $530,000."),
            ("Is Panama City Beach a good short-term rental market?",
             "It is the value entry into the Gulf Coast. Purchase prices sit well below Destin and 30A for a similar guest, and the season runs from spring break through an autumn shoulder driven by warm Gulf water."),
            ("Why is four bedrooms a common target in beach markets?",
             "Four bedrooms moves a property out of the couples and small family bracket and into the two-families-sharing-a-house bracket, where nightly rate rises faster than purchase price."),
        ],
    ),
    dict(
        slug="julie-pocono-lake-pa-5br",
        name="Julie",
        initial="J",
        market="Pocono Lake, Pennsylvania",
        market_link="/markets/poconos/",
        beds=5,
        price="$880,000",
        prop_type="5BR lake house",
        category="Lake",
        headline="A five-bedroom Pocono Lake house inside the New York drive market",
        summary="Julie purchased a five-bedroom in Pocono Lake, Pennsylvania for $880,000, inside the two-hour drive radius that feeds the Poconos from New York and Philadelphia.",
        result="A five-bedroom in a four-season drive-to market, positioned for the New York and Philadelphia weekend demand that gives the Poconos an unusually flat annual revenue curve.",
        metrics=[("Purchase price", "$880,000", False),
                 ("Bedrooms", "5", False),
                 ("Drive market", "NYC and Philadelphia", False)],
        body=[
            "The Poconos are the clearest example of drive-market economics in the country. Roughly thirty million people live within a two-hour drive, and drive-to demand behaves very differently from fly-to demand: it books later, it books shorter, and critically, it holds up when airfare rises or discretionary travel budgets tighten.",
            "Julie bought a five-bedroom in Pocono Lake at $880,000. The bedroom count targets the group that drives Poconos revenue, which is not couples but multi-family and friend-group weekends out of New York and Philadelphia, typically two or three nights, typically booked inside of three weeks.",
            "The genuine advantage of the region is that it has four real seasons of demand. Summer lake and water sports, autumn foliage, winter ski traffic to Camelback and Blue Mountain, and spring shoulder. Compared with a single-season beach or mountain market, that produces a flatter annual revenue curve and a much less alarming set of winter statements.",
            "It is also a market with real regulatory texture. Township and homeowner association rules across Monroe and Carbon counties vary considerably property to property, and a house that cannot legally operate is worth nothing as a short-term rental regardless of how well it shows. Verifying the specific permit position before an offer goes out is not optional here.",
        ],
        faqs=[
            ("How much did Julie's Pocono Lake property cost?",
             "A five-bedroom in Pocono Lake, Pennsylvania purchased for $880,000."),
            ("Why are the Poconos considered a strong drive market?",
             "Roughly thirty million people live within a two-hour drive, largely from New York and Philadelphia. Drive-to demand books later and shorter than fly-to demand, and it holds up better when travel budgets tighten."),
            ("What is the main risk in the Poconos?",
             "Regulation. Township and homeowner association rules in Monroe and Carbon counties vary property by property, so the specific permit position has to be verified before an offer is written."),
        ],
    ),
    dict(
        slug="vishal-sevierville-tn-5br",
        name="Vishal",
        initial="V",
        market="Sevierville, Tennessee",
        market_link="/markets/smoky-mountains/",
        beds=5,
        price="$1,250,000",
        prop_type="5BR cabin",
        category="Mountain cabin",
        headline="A $1.25M five-bedroom in the highest-volume STR market in America",
        summary="Vishal purchased a five-bedroom cabin in Sevierville, Tennessee for $1,250,000, in the Smoky Mountains corridor that draws more annual visitors than any national park region in the country.",
        result="A five-bedroom in the Sevierville and Gatlinburg corridor, the single highest-volume short-term rental market in the United States by booked nights.",
        metrics=[("Purchase price", "$1,250,000", False),
                 ("Bedrooms", "5", False),
                 ("Market", "Smoky Mountains", False)],
        body=[
            "Great Smoky Mountains National Park receives more annual visitors than any other national park in the United States, roughly double the second-place park. That single fact is why the Sevierville, Pigeon Forge and Gatlinburg corridor supports more short-term rental inventory than any comparable region in the country, and why it can absorb new supply that would flood a smaller market.",
            "Vishal bought a five-bedroom cabin at $1,250,000. Five bedrooms is the practical sweet spot in the Smokies for an investor who wants group-booking economics without the acquisition cost and turnover complexity of a nine-bedroom lodge.",
            "What separates cabins that perform from cabins that do not in this market is amenity fit rather than square footage. A hot tub, a mountain view, a game room, and proximity to the Parkway drive booking rates far more than an extra 400 square feet. Underwriting has to price the amenity gap between the subject property and its actual comparable set, because that gap is what closes or does not close after purchase.",
            "Tennessee has no state income tax on wages, which is a secondary but real consideration for a high earner buying here. It does not change the federal treatment of the property, but it does remove a layer of state-level complexity that a comparable purchase in California or New York would carry.",
        ],
        faqs=[
            ("What did Vishal's Sevierville cabin cost?",
             "A five-bedroom cabin purchased for $1,250,000 in Sevierville, Tennessee."),
            ("Why is the Smokies corridor so large as a rental market?",
             "Great Smoky Mountains National Park draws more annual visitors than any other US national park, roughly double the second place park, which supports far more rental inventory than a typical mountain market."),
            ("What drives revenue differences between Smokies cabins?",
             "Amenity fit more than size. Hot tub, view, game room and Parkway proximity move nightly rates more than additional square footage does."),
        ],
    ),
    dict(
        slug="mahmoud-nashville-tn-4br",
        name="Mahmoud",
        initial="M",
        market="Nashville, Tennessee",
        market_link="/markets/nashville/",
        beds=4,
        price="Not published",
        prop_type="4BR urban STR",
        category="City",
        headline="A four-bedroom in Nashville's permitted short-term rental market",
        summary="Mahmoud purchased a four-bedroom short-term rental in Nashville, Tennessee, a city market where the permit itself is a substantial part of the asset value.",
        result="A four-bedroom in a major urban STR market where non-owner-occupied permits are restricted by zoning, which limits new supply and protects existing operators.",
        metrics=[("Bedrooms", "4", False),
                 ("Market", "Nashville, Tennessee", False),
                 ("Property type", "Urban STR", False)],
        body=[
            "Nashville is one of the few large American cities where short-term rentals are both genuinely lucrative and genuinely constrained. The city distinguishes between owner-occupied and non-owner-occupied permits, and non-owner-occupied permits are limited by zoning district. That constraint is the entire investment thesis.",
            "In an unregulated market, a strong year invites new supply, new supply compresses rates, and the returns that attracted capital disappear within two seasons. In Nashville the permit acts as a supply ceiling. A property that legally holds a non-owner-occupied permit in a permitted zone is protected from exactly the dynamic that erodes returns everywhere else.",
            "Mahmoud's four-bedroom targets the demand that makes Nashville distinctive: bachelorette parties, group trips, and Broadway weekends where six to ten people want one house within reach of downtown rather than separate hotel rooms. That guest pays well and books far ahead, and four bedrooms is the entry point into that bracket.",
            "The corresponding risk is that permit rules are political and can change. Anyone buying an urban short-term rental should underwrite what the property is worth as a long-term rental if the permit regime tightens, and be comfortable with that floor. In Nashville the long-term rental market is strong enough that the floor is a real one, which is not true of every city market.",
        ],
        faqs=[
            ("How does Nashville regulate short-term rentals?",
             "The city separates owner-occupied from non-owner-occupied permits and limits non-owner-occupied permits by zoning district. That restriction caps new supply, which protects operators who hold a valid permit."),
            ("What drives Nashville short-term rental demand?",
             "Group travel. Bachelorette parties, corporate groups and Broadway weekends favor a whole house within reach of downtown over separate hotel rooms, and that guest books early and pays well."),
            ("What is the risk in a permitted city market?",
             "Permit rules are political and can tighten. The property should be underwritten against what it would be worth as a long-term rental if the short-term permit regime changes."),
        ],
    ),
    dict(
        slug="krystin-michael-nashville-tn-4br",
        name="Krystin & Michael",
        initial="K",
        market="Nashville, Tennessee",
        market_link="/markets/nashville/",
        beds=4,
        price="Not published",
        prop_type="4BR urban STR",
        category="City",
        headline="A second Nashville four-bedroom in the group-travel bracket",
        summary="Krystin and Michael purchased a four-bedroom short-term rental in Nashville, Tennessee, targeting the same permitted group-travel segment that makes the market work.",
        result="A four-bedroom in Nashville's permitted short-term rental inventory, positioned for the group travel demand that supports the market's nightly rates.",
        metrics=[("Bedrooms", "4", False),
                 ("Market", "Nashville, Tennessee", False),
                 ("Property type", "Urban STR", False)],
        body=[
            "Krystin and Michael bought a four-bedroom in Nashville, the second property in our client base targeting the same thesis: a legally permitted whole-house rental serving group travel in a city that restricts how many of those permits exist.",
            "Urban short-term rentals behave differently from vacation-market properties in ways that matter for underwriting. Occupancy is higher and more evenly distributed across the year, because a city has business travel, event traffic, medical visitors and family stays alongside pure leisure. Nightly rates are lower than a peak-season beach house, but the annual curve is dramatically flatter, and a flat curve makes debt service far easier to carry.",
            "Nashville specifically runs a very heavy event calendar. CMA Fest, the football season, the NHL season, conventions at Music City Center and a continuous stream of Broadway weekends produce compression nights where rates run several times the baseline. Capturing those requires dynamic pricing that is actually watching the event calendar rather than a static weekend uplift.",
            "The operational demand is higher too. City guests turn over more frequently, expect faster response times, and are more likely to raise a complaint about noise or parking. Cleaning and management systems that would be adequate for a weekly beach turnover are not adequate for a market where a house can turn three times in one week.",
        ],
        faqs=[
            ("How do urban STRs differ from vacation-market properties?",
             "Occupancy is higher and spread more evenly across the year because a city has business, event, medical and family travel alongside leisure. Nightly rates are lower but the flatter annual curve makes debt service easier to carry."),
            ("What drives Nashville compression nights?",
             "The event calendar. CMA Fest, football and hockey seasons, and Music City Center conventions produce nights where rates run several times baseline, which requires dynamic pricing tied to the actual event calendar."),
            ("Are city short-term rentals harder to operate?",
             "Yes. Turnover is more frequent, response time expectations are tighter, and noise and parking complaints are more common than in a vacation market."),
        ],
    ),
    dict(
        slug="jason-marissa-champions-gate-fl-8br",
        name="Jason & Marissa",
        initial="J",
        market="Champions Gate, Florida",
        market_link="/markets/kissimmee/",
        beds=8,
        price="$650,000",
        prop_type="8BR resort home",
        category="Theme park",
        headline="Eight bedrooms near Disney for $650,000",
        summary="Jason and Marissa purchased an eight-bedroom resort home in Champions Gate, Florida for $650,000, in the Orlando theme park corridor where per-bedroom cost is the lowest in the country.",
        result="Eight bedrooms at $650,000, roughly $81,000 per bedroom, which is among the lowest per-bedroom acquisition costs available in any major short-term rental market.",
        metrics=[("Purchase price", "$650,000", False),
                 ("Bedrooms", "8", True),
                 ("Cost per bedroom", "~$81,000", True)],
        body=[
            "The Orlando theme park corridor produces a number that looks like a typo to anyone used to beach or mountain pricing: roughly $81,000 per bedroom. Jason and Marissa bought eight bedrooms in Champions Gate for $650,000. An eight-bedroom in the Smokies costs two or three times that.",
            "The reason is that Champions Gate, Reunion, Windsor Hills and the surrounding resort communities were purpose-built as vacation-home inventory at scale. These are production-built houses in master-planned communities with shared amenity complexes, not one-off custom properties. Building efficiency at that volume drives per-bedroom cost down dramatically.",
            "The guest is the multi-generational Disney trip. Grandparents, two sets of parents, and six children want one house with a private pool, a game room and a ten-minute drive to the parks, and they will pay for it, and they will book six to nine months ahead. That advance booking window is genuinely valuable, because it gives an operator visibility into the coming year that a late-booking drive market never provides.",
            "The competitive reality has to be respected. This is the most supplied short-term rental submarket in America, with thousands of nearly identical houses competing on the same platforms. Differentiation comes from themed bedrooms, pool heating, game room quality and review score, not from the house itself. An operator who furnishes to a generic standard here will lose on price to a neighbor who did not.",
        ],
        faqs=[
            ("How much does an eight-bedroom near Disney cost?",
             "Jason and Marissa bought an eight-bedroom in Champions Gate, Florida for $650,000, which works out to roughly $81,000 per bedroom."),
            ("Why is the Orlando corridor so inexpensive per bedroom?",
             "Champions Gate, Reunion and similar communities were purpose-built as vacation home inventory at production scale, which drives per-bedroom construction cost far below custom-built mountain or beach properties."),
            ("What is the main risk in the Disney corridor?",
             "Supply. It is the most heavily supplied short-term rental submarket in the country, so differentiation through themed rooms, pool heating, game room quality and review score matters more than the house itself."),
        ],
    ),
    dict(
        slug="naveen-davenport-fl-8br",
        name="Naveen",
        initial="N",
        market="Davenport, Florida",
        market_link="/markets/kissimmee/",
        beds=8,
        price="$700,000",
        prop_type="8BR resort home",
        category="Theme park",
        headline="An eight-bedroom Davenport resort home at $700,000",
        summary="Naveen purchased an eight-bedroom resort home in Davenport, Florida for $700,000, on the western edge of the Orlando theme park corridor.",
        result="Eight bedrooms at $700,000 in the Orlando corridor, roughly $87,500 per bedroom, targeting the multi-generational theme park stay.",
        metrics=[("Purchase price", "$700,000", False),
                 ("Bedrooms", "8", True),
                 ("Cost per bedroom", "~$87,500", False)],
        body=[
            "Davenport sits on the western edge of the Orlando vacation home belt, along the US-27 corridor that runs south from I-4. It is close enough to Disney to sell the proximity, and priced below the communities that sit directly against the park boundary.",
            "Naveen bought an eight-bedroom at $700,000. As with the rest of this corridor, the economics are driven by bedroom count rather than square footage or finish level, because the guest is booking on how many people the house sleeps and whether it has a private pool.",
            "Two amenities decide the pricing tier in this market. A private pool with heating is effectively mandatory, since Central Florida evenings in January and February are cool enough that an unheated pool is unusable exactly when snowbird demand peaks. A game room converted from the garage is the second, and it is the single most common upgrade that moves a Davenport property from the bottom of the pricing pack into the middle.",
            "Underwriting the Orlando corridor means underwriting the fee structure honestly. Most of these communities carry homeowner association dues that cover the shared amenity complex, and those dues are not small. A proforma that models revenue accurately but treats HOA fees as a rounding error will overstate cash flow by a meaningful margin.",
        ],
        faqs=[
            ("What did Naveen's Davenport property cost?",
             "An eight-bedroom resort home purchased for $700,000 in Davenport, Florida."),
            ("Which amenities matter most in the Orlando corridor?",
             "A heated private pool and a converted game room. Central Florida winter evenings are cool enough that an unheated pool goes unused during peak snowbird season, and a game room is the most common upgrade that lifts a property out of the bottom pricing tier."),
            ("Do HOA fees matter in Orlando resort communities?",
             "Substantially. Most of these communities charge dues covering the shared amenity complex, and a proforma that understates them will overstate cash flow."),
        ],
    ),
    dict(
        slug="laxman-sabitri-johnson-city-tx-6br",
        name="Laxman & Sabitri",
        initial="L",
        market="Johnson City, Texas",
        market_link="/markets/austin/",
        beds=6,
        price="$680,000",
        prop_type="6BR Hill Country property",
        category="Rural",
        headline="A six-bedroom Texas Hill Country property at $680,000",
        summary="Laxman and Sabitri purchased a six-bedroom in Johnson City, Texas for $680,000, in the Hill Country wine corridor between Austin and Fredericksburg.",
        result="Six bedrooms at $680,000 in the Hill Country wine corridor, positioned for the Austin and San Antonio weekend group market.",
        metrics=[("Purchase price", "$680,000", False),
                 ("Bedrooms", "6", False),
                 ("Drive market", "Austin and San Antonio", False)],
        body=[
            "Johnson City sits in the middle of the Texas Hill Country wine corridor, between Austin and Fredericksburg on US-290. The market runs on a specific guest: groups from Austin, San Antonio and Houston coming out for a wine weekend, a wedding, or a bachelorette, who want one large house within driving distance of two dozen tasting rooms.",
            "Laxman and Sabitri bought a six-bedroom at $680,000. Six bedrooms is the right target for that guest, because the wine weekend group is typically eight to twelve people and the properties competing for them are almost all four-bedroom ranch houses.",
            "The Hill Country has a genuinely favorable regulatory position. Much of the inventory is on unincorporated county land, outside city short-term rental ordinances entirely. That is a real advantage compared with Austin proper, where the licensing regime has been contested and restrictive for years. It is also a reason to verify the exact parcel status rather than assuming, because a property inside Johnson City limits and a property two miles outside them are governed differently.",
            "Seasonality here is spring and autumn, not summer. Texas summers are hot enough to suppress outdoor-driven demand in July and August, which is the opposite of the pattern in most of the country. Wildflower season in March and April and the autumn harvest window carry the year, and the model has to reflect that.",
        ],
        faqs=[
            ("What did the Johnson City property cost?",
             "Laxman and Sabitri purchased a six-bedroom in Johnson City, Texas for $680,000."),
            ("Why is the Texas Hill Country attractive for short-term rentals?",
             "Much of the inventory sits on unincorporated county land outside city short-term rental ordinances, and the market draws wine weekend and wedding groups from Austin, San Antonio and Houston."),
            ("When is the Hill Country season?",
             "Spring and autumn. Wildflower season in March and April and the autumn harvest window carry the year, while July and August heat suppresses demand, which is the reverse of most US markets."),
        ],
    ),
    dict(
        slug="dustin-branson-west-mo-8br",
        name="Dustin W.",
        initial="D",
        market="Branson West, Missouri",
        market_link="/markets/branson/",
        beds=8,
        price="$930,900",
        prop_type="8BR lake house",
        category="Lake",
        headline="An eight-bedroom on Table Rock Lake at $930,900",
        summary="Dustin purchased an eight-bedroom in Branson West, Missouri for $930,900, on the Table Rock Lake side of the Branson entertainment market.",
        result="Eight bedrooms at $930,900 combining Table Rock Lake demand with Branson's year-round entertainment traffic, which gives the property two distinct booking seasons.",
        metrics=[("Purchase price", "$930,900", False),
                 ("Bedrooms", "8", True),
                 ("Demand drivers", "Lake and entertainment", False)],
        body=[
            "Branson West is the useful part of the Branson market for an investor, because it sits on Table Rock Lake while still being inside the catchment of Branson's entertainment corridor. That combination gives a property two independent demand drivers instead of one.",
            "Dustin bought an eight-bedroom at $930,900. Table Rock is a large, clean, boating-oriented lake, and lakefront or lake-access properties with eight bedrooms serve exactly the multi-family summer trip that the market is built around.",
            "The second driver is the entertainment corridor. Branson runs a heavy theater and show schedule, and it draws substantial motorcoach and church group traffic, particularly in the autumn. That produces a genuine second season in September and October when the lake demand has faded, which most pure lake markets in the Midwest do not have.",
            "The Ozarks also carry a lower cost basis than comparable lake markets in Michigan, Wisconsin or the Northeast. Missouri property taxes are moderate, construction costs are low, and eight bedrooms for under a million dollars on a major recreational lake is not a price point available in most of the country.",
        ],
        faqs=[
            ("What did Dustin's Branson West property cost?",
             "An eight-bedroom purchased for $930,900 in Branson West, Missouri."),
            ("Why Branson West rather than Branson proper?",
             "Branson West sits on Table Rock Lake while remaining inside the entertainment corridor catchment, which gives a property both summer lake demand and autumn show and group traffic."),
            ("How does the Ozarks cost basis compare with other lake markets?",
             "Substantially lower. Eight bedrooms under a million dollars on a major recreational lake is not available in most Northeast or Great Lakes markets."),
        ],
    ),
    dict(
        slug="alfredo-millie-sevierville-tn-4br",
        name="Alfredo & Millie N.",
        initial="A",
        market="Sevierville, Tennessee",
        market_link="/markets/smoky-mountains/",
        beds=4,
        price="$865,000",
        prop_type="4BR cabin",
        category="Mountain cabin",
        headline="A four-bedroom Smokies cabin at $865,000",
        summary="Alfredo and Millie purchased a four-bedroom cabin in Sevierville, Tennessee for $865,000, targeting the highest-velocity bedroom count in the Smokies market.",
        result="A four-bedroom in the Smokies corridor, the bedroom count with the deepest and most consistent booking demand in the market.",
        metrics=[("Purchase price", "$865,000", False),
                 ("Bedrooms", "4", False),
                 ("Market", "Smoky Mountains", False)],
        body=[
            "Four bedrooms is the workhorse configuration in the Smokies. Nine-bedroom lodges produce the eye-catching monthly numbers, but they book a narrower calendar, because there are only so many twenty-six-person reunions in a given month. A four-bedroom cabin serves two families, a small friend group, a couple with in-laws, or an extended family, and that demand exists every week of the season.",
            "Alfredo and Millie bought at $865,000. The result of the narrower revenue ceiling is a much steadier occupancy pattern, and for a first purchase that steadiness is usually worth more than a higher peak.",
            "Amenities in this bracket are close to standardized, which is exactly why they matter. A hot tub, a mountain view, and a game room are what the comparable set has, and a cabin missing any one of them is priced against properties that have all three. Underwriting has to fund the gap at purchase rather than treating it as an optional later upgrade.",
            "Location within the corridor drives the rest. Sevierville, Pigeon Forge and Gatlinburg are commonly discussed as one market and they are not. Drive time to the Parkway, to Dollywood, and to the national park entrance moves nightly rates materially, and two cabins with identical specs ten minutes apart can sit in different pricing tiers.",
        ],
        faqs=[
            ("What did the Sevierville four-bedroom cost?",
             "Alfredo and Millie purchased a four-bedroom cabin in Sevierville, Tennessee for $865,000."),
            ("Why choose four bedrooms over a larger cabin?",
             "Four bedrooms serves two families or a small group, which is demand that exists every week of the season. Large lodges have a higher peak but book a narrower calendar because very large groups are less frequent."),
            ("Are Sevierville, Pigeon Forge and Gatlinburg the same market?",
             "No. Drive time to the Parkway, Dollywood and the national park entrance moves nightly rates materially, so cabins with identical specs ten minutes apart can sit in different pricing tiers."),
        ],
    ),
    dict(
        slug="joe-s-broken-bow-ok-and-destin-fl",
        name="Joe S.",
        initial="J",
        market="Broken Bow OK and Destin FL",
        market_link="/markets/broken-bow/",
        beds=8,
        price="$2,324,900 across two properties",
        prop_type="Two-property portfolio",
        category="Portfolio",
        headline="Two properties, two markets, two different seasons",
        summary="Joe S closed two properties with BNB Accelerator: a four-bedroom in Broken Bow, Oklahoma at $1,400,000 and a four-bedroom in Destin, Florida at $924,900.",
        result="A two-property, two-market portfolio pairing a Dallas-fed Oklahoma cabin market with a Gulf Coast beach market, deliberately diversified across different seasons and different guest bases.",
        metrics=[("Properties", "2", True),
                 ("Combined price", "$2,324,900", False),
                 ("Markets", "Broken Bow and Destin", False)],
        properties=[
            ("Broken Bow, Oklahoma", "4BR", "$1,400,000"),
            ("Destin, Florida", "4BR", "$924,900"),
        ],
        body=[
            "Joe's two properties are a textbook illustration of why the second purchase should rarely be in the same market as the first. A four-bedroom in Broken Bow, Oklahoma at $1,400,000 and a four-bedroom in Destin, Florida at $924,900 share a bedroom count and almost nothing else.",
            "Broken Bow is the Dallas-Fort Worth escape market. Roughly three hours from the metroplex, it has become one of the highest-performing cabin markets in the country, driven by luxury A-frames and modern cabins serving couples and small groups from Texas. The demand is drive-to, weekend-weighted and remarkably resilient.",
            "Destin is a fly-and-drive Gulf Coast beach market with a completely different curve. It peaks hard in summer, draws from a much wider geographic catchment, and carries coastal insurance costs that Oklahoma does not.",
            "The diversification is the point. If a Texas economic slowdown suppresses Dallas weekend travel, Destin's national catchment is unaffected. If a hurricane season disrupts the Gulf Coast, the Oklahoma cabin does not care. Investors who buy their second and third properties within a few miles of the first have not built a portfolio, they have increased the size of a single bet.",
            "The Broken Bow price point is worth flagging. At $1,400,000 for four bedrooms, this is a market where finish level and design carry the nightly rate rather than bedroom count. The luxury A-frame segment there competes on architecture and photography in a way that a standard cabin market does not.",
        ],
        faqs=[
            ("What properties did Joe S buy?",
             "A four-bedroom in Broken Bow, Oklahoma at $1,400,000 and a four-bedroom in Destin, Florida at $924,900."),
            ("Why buy in two different markets?",
             "Different seasons and different guest catchments. A Texas economic slowdown affects the Dallas-fed Broken Bow market but not Destin's national catchment, and a Gulf hurricane season affects Destin but not Oklahoma."),
            ("Why does Broken Bow command such high prices for four bedrooms?",
             "The market's top tier is luxury A-frames and architectural cabins competing on design and photography rather than bedroom count, serving Dallas-Fort Worth couples and small groups three hours away."),
        ],
    ),
    dict(
        slug="mark-farrah-destin-fl-4br",
        name="Mark & Farrah",
        initial="M",
        market="Destin, Florida",
        market_link="/markets/destin/",
        beds=4,
        price="$950,000",
        prop_type="4BR beach house",
        category="Beach",
        headline="A four-bedroom Destin beach house at $950,000",
        summary="Mark and Farrah purchased a four-bedroom in Destin, Florida for $950,000, on the Emerald Coast stretch that commands the highest nightly rates on the Gulf.",
        result="A four-bedroom on the Emerald Coast, in the price tier where proximity to the beach access point is the single largest driver of nightly rate.",
        metrics=[("Purchase price", "$950,000", False),
                 ("Bedrooms", "4", False),
                 ("Market", "Destin, Florida", False)],
        body=[
            "Destin sells on water color. The Emerald Coast has the clearest water and the whitest sand on the Gulf, and it commands nightly rates that a functionally identical house on a browner stretch of coast cannot approach.",
            "Mark and Farrah bought a four-bedroom at $950,000. In this market the variable that moves revenue most is walking distance to a beach access point. A house four blocks back from the beach and a house one block back can differ by 30% or more in nightly rate for the same square footage, and that gap is permanent because you cannot move the house.",
            "Destin's season is long by beach market standards. Spring break traffic starts in March, summer runs hard through August, and a substantial autumn shoulder continues into October while the Gulf is still warm. That gives the calendar more billable weeks than an Atlantic beach market at the same latitude.",
            "Two costs need honest treatment in any Gulf Coast model. Coastal insurance, including wind and flood coverage, has repriced sharply across Florida in recent years and is now a material line item rather than a footnote. And condominium or homeowner association assessments, where they apply, can arrive as large one-time items after a storm season. Both belong in the proforma at purchase.",
        ],
        faqs=[
            ("What did the Destin property cost?",
             "Mark and Farrah purchased a four-bedroom in Destin, Florida for $950,000."),
            ("What drives nightly rate differences in Destin?",
             "Walking distance to a beach access point. Houses one block from the beach can command 30% or more over otherwise identical houses four blocks back, and that gap cannot be closed by renovation."),
            ("What costs are commonly understated on the Gulf Coast?",
             "Coastal insurance, including wind and flood coverage, which has repriced sharply across Florida, and association assessments that can arrive as large one-time items after a storm season."),
        ],
    ),
    dict(
        slug="tiffany-destin-fl-5br",
        name="Tiffany",
        initial="T",
        market="Destin, Florida",
        market_link="/markets/destin/",
        beds=5,
        price="$1,100,000",
        prop_type="5BR beach house",
        category="Beach",
        headline="A five-bedroom Destin beach house at $1,100,000",
        summary="Tiffany purchased a five-bedroom in Destin, Florida for $1,100,000, moving above the four-bedroom band into the larger-group segment of the Emerald Coast market.",
        result="A five-bedroom on the Emerald Coast, in the segment where two families sharing a beach house become the primary guest rather than a single family.",
        metrics=[("Purchase price", "$1,100,000", False),
                 ("Bedrooms", "5", False),
                 ("Market", "Destin, Florida", False)],
        body=[
            "Moving from four bedrooms to five in Destin changes which guest the property competes for. Four bedrooms is a family. Five is two families splitting a beach week, and that guest has roughly double the willingness to pay because the cost is divided across two households.",
            "Tiffany bought at $1,100,000. The premium over a four-bedroom in the same area is meaningful, but the nightly rate uplift in peak summer weeks generally exceeds the proportional increase in purchase price, which is what makes the step up work.",
            "Five-bedroom inventory is also thinner. Most of the Destin housing stock is two, three and four bedrooms, so the properties genuinely competing for a five-bedroom booking are fewer in number. That thinner competitive set supports pricing in exactly the peak weeks when demand is highest.",
            "The operational cost does scale. More bedrooms means more beds to turn, more linen, more consumables, and a longer clean between guests. A five-bedroom's turnover cost is not proportionally larger than a four-bedroom's, but it is larger, and a model that scales revenue with bedroom count while holding cleaning cost flat will overstate the return.",
        ],
        faqs=[
            ("What did Tiffany's Destin property cost?",
             "A five-bedroom purchased for $1,100,000 in Destin, Florida."),
            ("Why step up from four bedrooms to five?",
             "Five bedrooms serves two families splitting a beach week, a guest with roughly double the willingness to pay because the cost is divided. Five-bedroom inventory is also thinner, so the competitive set in peak weeks is smaller."),
            ("Does turnover cost scale with bedroom count?",
             "It rises, though not proportionally. More beds, linen and consumables mean a longer and more expensive clean, and a model that scales revenue with bedrooms while holding cleaning flat overstates return."),
        ],
    ),
    dict(
        slug="adam-sevierville-tn-4br",
        name="Adam S.",
        initial="A",
        market="Sevierville, Tennessee",
        market_link="/markets/smoky-mountains/",
        beds=4,
        price="$775,000",
        prop_type="4BR cabin",
        category="Mountain cabin",
        headline="A four-bedroom Smokies cabin at $775,000",
        summary="Adam purchased a four-bedroom cabin in Sevierville, Tennessee for $775,000, an entry point below the market's four-bedroom average.",
        result="A four-bedroom in the Smokies at $775,000, entering the highest-demand bedroom count in the country's highest-volume STR market at a below-average basis.",
        metrics=[("Purchase price", "$775,000", False),
                 ("Bedrooms", "4", False),
                 ("Market", "Smoky Mountains", False)],
        body=[
            "Adam's purchase is the clearest illustration of what the acquisition side of this business actually does. A four-bedroom cabin in Sevierville at $775,000 is below where comparable four-bedroom inventory in the corridor typically transacts, and every dollar below the market basis is a permanent improvement to the return.",
            "That matters more than most first-time buyers expect. Revenue optimization is real but bounded: better photography, better pricing and better amenities might move gross revenue 10 to 20% against a poorly run comparable. Buying $50,000 or $80,000 under market is locked in at closing, it never has to be re-earned, and it improves both the cash-on-cash return and the equity position simultaneously.",
            "We screen roughly a thousand deals a week and eliminate about 98% of them. That ratio exists because the properties worth buying are a small fraction of the properties for sale, and because the difference between the two is almost never visible from the listing photos. It is visible in the comparable booking data, the amenity gap, the deferred maintenance, and what the seller will actually accept.",
            "Sevierville remains our most-transacted market for a reason. The demand base is the largest in the country, the inventory is deep enough that there is always something mispriced, and Tennessee's lack of a wage income tax removes a layer of state-level complexity for high-earning buyers.",
        ],
        faqs=[
            ("What did Adam's Sevierville cabin cost?",
             "A four-bedroom cabin purchased for $775,000 in Sevierville, Tennessee."),
            ("Why does purchase price matter more than revenue optimization?",
             "Optimization is bounded, perhaps 10 to 20% of gross revenue against a poorly run comparable. Buying under market is locked in at closing, never has to be re-earned, and improves both cash-on-cash return and equity position at once."),
            ("How many deals does BNB Accelerator review?",
             "Roughly a thousand a week, with about 98% eliminated. The properties worth buying are a small fraction of those for sale, and the difference is rarely visible in listing photos."),
        ],
    ),
]



# ------------------------------------------------------------- Landings --
#
# Every documented client outcome gets its own landing page at
# /case-studies/<first-name><-last-initial>-<city>/. Two sources feed them:
# the case studies above, and the client deal tracker in deals.json. A tracker
# deal is folded into a case study when the client and the purchase price match,
# because the tracker holds the financials the case study never published
# (down payment, closing, design budget, cash flow, cash-on-cash). Where a
# tracker deal has no matching case study it gets a landing page of its own.
#
# Two rules hold everywhere on these pages:
#   1. Clients appear as a first name plus a last initial, never a full surname.
#   2. Street addresses are never published. A market and a property type is the
#      level of detail the tracker permits without identifying the property.

DEALS = {d["id"]: d for d in json.load(
    open(os.path.join(HERE, "deals.json")))["deals"]}
MARKET_DATA = json.load(open(os.path.join(HERE, "market_data.json")))

# Historic case study slug -> (landing slug, city, [tracker deal ids])
LANDING = {
    "victoria-sevierville-tn-9br-cabin": ("victoria-sevierville", "Sevierville", ["deal-21"]),
    "peter-eck-ibm-partner-six-properties": ("peter-e-santa-rosa-beach", "Santa Rosa Beach", ["deal-18", "deal-11"]),
    "ashley-billy-fort-walton-beach-fl": ("ashley-billy-fort-walton-beach", "Fort Walton Beach", ["deal-15"]),
    "antonio-fort-myers-fl-6br": ("antonio-fort-myers", "Fort Myers", []),
    "shardul-mayanka-panama-city-beach-fl": ("shardul-mayanka-panama-city-beach", "Panama City Beach", ["deal-12"]),
    "julie-pocono-lake-pa-5br": ("julie-pocono-lake", "Pocono Lake", ["deal-20"]),
    "vishal-sevierville-tn-5br": ("vishal-sevierville", "Sevierville", []),
    "mahmoud-nashville-tn-4br": ("mahmoud-nashville", "Nashville", []),
    "krystin-michael-nashville-tn-4br": ("krystin-michael-nashville", "Nashville", []),
    "jason-marissa-champions-gate-fl-8br": ("jason-marissa-champions-gate", "Champions Gate", []),
    "naveen-davenport-fl-8br": ("naveen-davenport", "Davenport", ["deal-14"]),
    "laxman-sabitri-johnson-city-tx-6br": ("laxman-sabitri-johnson-city", "Johnson City", []),
    "dustin-branson-west-mo-8br": ("dustin-w-branson-west", "Branson West", ["deal-02"]),
    "alfredo-millie-sevierville-tn-4br": ("alfredo-millie-n-sevierville", "Sevierville", []),
    "joe-s-broken-bow-ok-and-destin-fl": ("joe-s-broken-bow", "Broken Bow", []),
    "mark-farrah-destin-fl-4br": ("mark-farrah-destin", "Destin", ["deal-07"]),
    "tiffany-destin-fl-5br": ("tiffany-destin", "Destin", ["deal-13"]),
    "adam-sevierville-tn-4br": ("adam-s-sevierville", "Sevierville", ["deal-25"]),
}

# Tracker deals with no case study. deal id -> (slug, name, city, category,
# property type, what the market is bought for)
DEAL_PAGES = {
    "deal-01": ("dan-m-austin", "Dan M. & Kimberly", "Austin", "City",
                "City short-term rental",
                "an event-driven city market where March, football weekends and festival dates carry a disproportionate share of the year"),
    "deal-03": ("valerie-m-broken-bow", "Valerie M.", "Broken Bow", "Mountain cabin",
                "Mountain cabin",
                "a drive-to cabin market fed by Dallas and Oklahoma City, where couples' cabins turn over fast and design is the differentiator"),
    "deal-04": ("raymond-x-broken-bow", "Raymond X.", "Broken Bow", "Mountain cabin",
                "Mountain cabin",
                "a drive-to cabin market fed by Dallas and Oklahoma City, where the Hochatown corridor carries the highest rates"),
    "deal-05": ("meena-denver", "Meena", "Denver metro", "City",
                "City short-term rental",
                "a metro where the city itself restricts non-primary-residence rentals, so the deals sit in the surrounding jurisdictions"),
    "deal-06": ("kevin-denver", "Kevin", "Denver metro", "City",
                "City short-term rental",
                "a metro where the city itself restricts non-primary-residence rentals, so the deals sit in the surrounding jurisdictions"),
    "deal-08": ("harshavardhan-meghna-orlando", "Harshavardhan & Meghna", "Orlando corridor", "Theme park",
                "Resort home",
                "a resort-home market where bedroom count drives revenue and the per-bedroom purchase price is the number that matters"),
    "deal-09": ("amber-gulf-shores", "Amber", "Gulf Shores", "Beach",
                "Beach property",
                "Alabama's family Gulf market, where summer carries the year and the shoulder season is the underwriting risk"),
    "deal-10": ("david-hollister", "David", "Hollister", "Lake",
                "Lake property",
                "the Table Rock Lake corridor south of Branson, where lake access and entertainment demand run on different calendars"),
    "deal-16": ("erwin-lilyana-florida-panhandle", "Erwin & Lilyana", "Florida Panhandle", "Beach",
                "Beach property",
                "the 30A corridor, one of the highest average daily rate coastal markets in the country"),
    "deal-17": ("adam-florida-panhandle", "Adam", "Florida Panhandle", "Beach",
                "Beach property",
                "the 30A corridor, where proximity to the beach and the quality of the furnishing package set the rate"),
    "deal-19": ("pruthvi-poconos", "Pruthvi", "Poconos", "Lake",
                "Lake property",
                "a drive-to market inside three hours of New York and Philadelphia, where township rules differ road by road"),
    "deal-22": ("krystin-smoky-mountains", "Krystin", "Smoky Mountains", "Mountain cabin",
                "Mountain cabin",
                "the highest gross-revenue cabin corridor in the country, where large-group inventory competes with hotels rather than with other rentals"),
    "deal-23": ("mahmoud-smoky-mountains", "Mahmoud", "Smoky Mountains", "Mountain cabin",
                "Mountain cabin",
                "a seasonal cabin market that earns a disproportionate share of the year between June and October and again over the winter holidays"),
    "deal-24": ("hema-smoky-mountains", "Hema", "Smoky Mountains", "Mountain cabin",
                "Mountain cabin",
                "a seasonal cabin market where the underwriting has to be built on the annual shape of demand, not on the best month"),
}

# Market slug -> the market page path used on landing pages.
MARKET_PATH = {
    "austin": "/markets/austin/",
    "branson": "/markets/branson/",
    "broken-bow": "/markets/broken-bow/",
    "denver": "/markets/denver/",
    "destin": "/markets/destin/",
    "gulf-shores": "/markets/gulf-shores/",
    "kissimmee": "/markets/kissimmee/",
    "poconos": "/markets/poconos/",
    "smoky-mountains": "/markets/smoky-mountains/",
    "nashville": "/markets/nashville/",
    "panama-city-beach": "/markets/panama-city-beach/",
    "cape-coral": "/markets/cape-coral/",
    "gatlinburg": "/markets/gatlinburg/",
}

# Optional per-landing assets. Fill these in as they become available and the
# section renders itself; leave a slug out and the page simply omits it.
#   PHOTOS[slug] = ("/assets/case-studies/<file>.jpg", "alt text", width, height)
#   AIRBNB[slug] = "https://www.airbnb.com/rooms/..."
#
# There is no proforma link and there should not be one. Deal data lives on the
# page as a table, not behind a link to a spreadsheet somebody has to open.
PHOTOS = {}
AIRBNB = {}

# Site-standard illustration, matching /tools/str-revenue-calculator/ defaults:
# a cost segregation study reclassifies roughly a quarter of purchase price into
# shorter lives, and a high earner's combined marginal rate is around 40%.
COST_SEG_PCT = 0.25
MARGINAL_RATE = 0.40


def label(r):
    """How a landing page is named in a link: client, property, place."""
    if r["city"].lower() in r["prop_type"].lower():
        return f'{r["name"]}, {r["prop_type"]}'
    return f'{r["name"]}, {r["prop_type"]} in {r["city"]}'


def usd(n):
    return f"${n:,.0f}"


def deals_for(slug, ids):
    return [DEALS[i] for i in ids if i in DEALS]


def records():
    """Every landing page as one uniform record, case studies first."""
    out = []
    for c in CASES:
        slug, city, deal_ids = LANDING[c["slug"]]
        ds = deals_for(slug, deal_ids)
        # The case study's own market is the specific one; the tracker buckets
        # several cities into one regional label, so it never wins here.
        market_slug = c["market_link"].strip("/").split("/")[-1]
        out.append(dict(
            slug=slug, legacy=c["slug"], name=c["name"], initial=c["initial"],
            city=city, market=c["market"], market_slug=market_slug,
            market_link=c["market_link"], category=c["category"],
            prop_type=c["prop_type"], beds=c["beds"], price=c["price"],
            headline=c["headline"], summary=c["summary"], result=c["result"],
            metrics=c["metrics"], body=c["body"], faqs=c["faqs"],
            properties=c.get("properties"), deals=ds, kind="case"))
    for did, (slug, name, city, category, prop_type, thesis) in DEAL_PAGES.items():
        d = DEALS[did]
        out.append(deal_record(slug, name, city, category, prop_type, thesis, d))
    return out


def deal_record(slug, name, city, category, prop_type, thesis, d):
    md = MARKET_DATA.get(d["market_slug"], {})
    plain = name.replace("&", "and")
    yr = f" in {d['year']}" if d["year"] else ""
    summary = (f"{plain} bought a {prop_type.lower()} in {d['market']} for {usd(d['price'])}"
               f"{yr}, entering the deal for {usd(d['entry'])} all in. The property produces "
               f"{usd(d['cash_flow'])} a year in cash flow, a {d['coc']:.2f}% cash-on-cash return "
               f"on the cash invested.")
    headline = (f"{usd(d['cash_flow'])} a year on {usd(d['entry'])} in, "
                f"a {d['coc']:.1f}% cash-on-cash return")
    body = [
        f"{plain} bought in {d['market']}, {thesis}. The purchase closed at {usd(d['price'])}.",
        (f"Getting in cost {usd(d['entry'])}. That is {usd(d['down'])} of down payment, "
         f"{usd(d['closing'])} in closing costs and {usd(d['design'])} of furniture, "
         f"linens, photography and everything else that has to be in the house before the "
         f"first guest arrives." if d["design"] else
         f"Getting in cost {usd(d['entry'])}: {usd(d['down'])} of down payment plus "
         f"{usd(d['closing'])} in closing costs."),
        (f"The design budget is the line most buyers underestimate. It is not decoration, it "
         f"is the difference between a property that books at the market rate and one that "
         f"sits below it, and it has to be funded at closing rather than out of the first "
         f"season's revenue." if d["design"] else
         "Furnishing was handled outside the figures shown here, so the entry cost above "
         "reflects the down payment and closing costs only."),
        (f"Against that entry cost the property returns {usd(d['cash_flow'])} a year after "
         f"management, cleaning, supplies, utilities, insurance, property tax and debt "
         f"service, which is a {d['coc']:.2f}% cash-on-cash return."),
    ]
    if md:
        body.append(
            f"For context on the market rather than this property: {md['name']} entry prices "
            f"run {md['entry']}, average daily rates {md['adr']}, occupancy {md['occ']}, and "
            f"gross revenue {md['gross']}. {md['peak']}. Those are estimates assembled from "
            f"closings and active comparables, not a projection for any specific house.")
    body.append(
        "The tax position is where a purchase like this earns its keep for a high earner. A "
        "cost segregation study reclassifies part of the purchase price into five, seven and "
        "fifteen year property, which under current bonus depreciation rules produces a large "
        "first-year deduction. Whether that deduction offsets W-2 income depends on the seven "
        "day average stay test and material participation, both of which are facts about how "
        "the property is run.")
    faqs = [
        (f"What did {plain} pay for the property?",
         f"{usd(d['price'])} in {d['market']}{yr}. We publish the market and the numbers, not "
         f"the street address."),
        ("What did it cost to get into the deal?",
         f"{usd(d['entry'])} all in: {usd(d['down'])} down, {usd(d['closing'])} in closing "
         f"costs" + (f", and {usd(d['design'])} for design and furnishing." if d["design"] else ".")),
        ("What does the property return?",
         f"{usd(d['cash_flow'])} a year in cash flow after all operating costs and debt "
         f"service, which is a {d['coc']:.2f}% cash-on-cash return on {usd(d['entry'])} invested."),
        ("Is this a typical result?",
         "No. It is one documented outcome for one property. Across the deals we publish with "
         "full financials the average cash-on-cash return is 13.3%, and individual deals in "
         "that set range from under 2% to over 24%. Real estate involves risk, including loss "
         "of principal."),
    ]
    return dict(
        slug=slug, legacy=None, name=name, initial=plain[0], city=city,
        market=d["market"], market_slug=d["market_slug"],
        market_link=MARKET_PATH.get(d["market_slug"], "/markets/"),
        category=category, prop_type=prop_type, beds=None, price=usd(d["price"]),
        headline=headline, summary=summary,
        result=(f"{usd(d['cash_flow'])} a year in cash flow on {usd(d['entry'])} of cash "
                f"invested, a {d['coc']:.2f}% cash-on-cash return."),
        metrics=[("Purchase price", usd(d["price"]), False),
                 ("Total entry cost", usd(d["entry"]), False),
                 ("Annual cash flow", usd(d["cash_flow"]), True),
                 ("Cash-on-cash return", f"{d['coc']:.2f}%", True)],
        body=body, faqs=faqs, properties=None, deals=[d], kind="deal")


# ------------------------------------------------------------ Page parts --

def price_num(text):
    """The first dollar figure in a published price string, or None."""
    m = re.search(r"\$([\d,]+)", text or "")
    return int(m.group(1).replace(",", "")) if m else None


def deal_panel(r):
    """Entry cost and return, straight from the tracker."""
    ds = r["deals"]
    if not ds:
        return ""
    # A tracker record can sit materially above the price in the case study,
    # which means it is a different purchase by the same client in the same
    # market. Say so rather than letting two prices contradict each other.
    note = ""
    case_price = price_num(r["price"])
    tracker = sum(d["price"] for d in ds)
    if (r["kind"] == "case" and not r.get("properties") and case_price
            and abs(tracker - case_price) > 0.05 * case_price):
        note = (f"        <p>The tracker records a {usd(tracker)} purchase for this client in "
                f"this market. Those are the figures below. The property described above closed "
                f"at {usd(case_price)}.</p>\n")
    blocks = []
    for d in ds:
        design = (f'          <li><span class="k">Design and furnishing</span>'
                  f'<span class="v">{usd(d["design"])}</span></li>\n' if d["design"] else "")
        label = (f'        <h3 class="deal-block-head">{tpl.esc(d["market"])}'
                 f'{" &middot; " + str(d["year"]) if d["year"] else ""}</h3>\n'
                 if len(ds) > 1 else "")
        blocks.append(f"""{label}        <ul class="spec-list">
          <li><span class="k">Purchase price</span><span class="v">{usd(d['price'])}</span></li>
          <li><span class="k">Down payment</span><span class="v">{usd(d['down'])}</span></li>
          <li><span class="k">Closing costs</span><span class="v">{usd(d['closing'])}</span></li>
{design}          <li><span class="k">Total entry cost</span><span class="v">{usd(d['entry'])}</span></li>
          <li><span class="k">Annual cash flow</span><span class="v green">{usd(d['cash_flow'])}</span></li>
          <li><span class="k">Cash-on-cash return</span><span class="v green">{d['coc']:.2f}%</span></li>
        </ul>""")
    return ('        <h2 id="deal-numbers">The deal numbers</h2>\n'
            '        <p>Straight from the client deal tracker: what it cost to get in, and what '
            'it returns.</p>\n' + note + "\n".join(blocks) + "\n")


def tax_panel(r):
    """Illustrative cost segregation position on the purchase price."""
    if not r["deals"]:
        return ""
    # Illustrate against the price this page leads with, not the tracker's,
    # so the figure a reader checks against is the one they just read.
    price = price_num(r["price"]) or sum(d["price"] for d in r["deals"])
    ded = price * COST_SEG_PCT
    saving = ded * MARGINAL_RATE
    return f"""        <h2 id="tax">The tax position</h2>
        <ul class="spec-list">
          <li><span class="k">Purchase price</span><span class="v">{usd(price)}</span></li>
          <li><span class="k">Typical cost seg reclassification</span><span class="v">25% of price</span></li>
          <li><span class="k">Illustrative year-one deduction</span><span class="v green">{usd(ded)}</span></li>
          <li><span class="k">Illustrative tax reduction at 40%</span><span class="v green">{usd(saving)}</span></li>
        </ul>
        <p class="small text-muted">An illustration, not this client's return: 25% of price
        reclassified at a 40% marginal rate, the same assumptions as our
        <a href="/tools/str-revenue-calculator/">calculator</a>. Your number depends on your study,
        your rate, and meeting the <a href="/tax-strategy/7-day-rule/">seven day</a> and
        <a href="/tax-strategy/material-participation/">material participation</a> tests. We are
        not a CPA firm.</p>
"""


def big_numbers(r):
    """The five figures a buyer actually reads, in the order they read them.

    A portfolio page keeps its own headline metrics rather than aggregating the
    tracker: summing entry cost across two tracked properties while showing a
    purchase price that covers three would read as one deal and be wrong.
    """
    price = price_num(r["price"])
    ds = r["deals"]
    out, seen = [], set()

    def add(k, v, green=False):
        v = str(v)
        if v in seen:
            return
        seen.add(v)
        out.append((k, v, green))

    if ds and not r.get("properties"):
        # The tracker's own cash-on-cash figure, never a recomputed one: its
        # denominator is the cash the client actually had at risk.
        coc = (f'{ds[0]["coc"]:.2f}%' if len(ds) == 1 else
               f'{sum(d["coc"] for d in ds) / len(ds):.2f}% avg')
        add("Purchase price", usd(price or sum(d["price"] for d in ds)))
        add("Total entry", usd(sum(d["entry"] for d in ds)))
        add("Annual cash flow", usd(sum(d["cash_flow"] for d in ds)), True)
        add("Cash-on-cash", coc, True)
    else:
        # "$2,324,900 across two properties" is a sentence, not a stat.
        if price:
            add("Combined price" if r.get("properties") else "Purchase price", usd(price))
        for k, v, g in r["metrics"]:
            # A market name is not a number and does not belong in this band.
            if any(c.isdigit() for c in str(v)):
                add(k, v, g)
        if len(out) < 3:
            # Nothing numeric was published for this one. Say what is known
            # rather than leading the page with "Not published".
            for k, v, g in r["metrics"]:
                add(k, v, g)
    if price:
        add("Year-one tax reduction", usd(price * COST_SEG_PCT * MARGINAL_RATE), True)

    cells = "".join(
        f'<div class="big-stat"><span class="big-stat-val{" green" if g else ""}">'
        f'{tpl.esc(v)}</span><span class="big-stat-key">{tpl.esc(k)}</span></div>'
        for k, v, g in out[:5])
    return f'      <div class="big-stats">{cells}</div>'


def hero_visual(r):
    """The property photo where we have one, a plate of the numbers where we do not."""
    photo = PHOTOS.get(r["slug"])
    if photo:
        src, alt, w, h = photo
        return f"""      <figure class="case-photo">
        <img src="{src}" alt="{tpl.esc(alt)}" width="{w}" height="{h}" loading="eager" decoding="async">
        <figcaption>{tpl.esc(r['prop_type'])}, {tpl.esc(r['market'])}</figcaption>
      </figure>"""
    chips = "".join(
        f'<div class="case-plate-stat"><span class="k">{tpl.esc(k)}</span>'
        f'<span class="v{" green" if g else ""}">{tpl.esc(v)}</span></div>'
        for k, v, g in r["metrics"][:3])
    return f"""      <div class="case-plate" aria-hidden="false">
        <span class="case-plate-type">{tpl.esc(r['prop_type'])}</span>
        <span class="case-plate-market">{tpl.esc(r['market'])}</span>
        <div class="case-plate-stats">{chips}</div>
      </div>"""


def links_panel(r, all_recs):
    """Market, blog, sibling case studies, services. Every landing page links out."""
    import crosslink_markets as xl
    items = []
    items.append(f'<li><a href="{r["market_link"]}">Short-term rental market analysis for '
                 f'{tpl.esc(r["city"])}</a></li>')
    entry = xl.MAP.get(r["market_slug"])
    if entry:
        state_slug, state_name, pt_slug, pt_label, _cases, posts = entry
        for bp, text in posts:
            items.append(f'<li><a href="/blog/{bp}/">{text}</a></li>')
        items.append(f'<li><a href="/regulations/{state_slug}/">{state_name} short-term '
                     f'rental regulations</a></li>')
        items.append(f'<li><a href="/property-types/{pt_slug}/">{pt_label} investing guide</a></li>')
    siblings = [x for x in all_recs
                if x["market_slug"] == r["market_slug"] and x["slug"] != r["slug"]][:4]
    for s in siblings:
        items.append(f'<li><a href="/case-studies/{s["slug"]}/">{label(s)}</a></li>')
    items += [
        '<li><a href="/case-studies/">All client case studies</a></li>',
        '<li><a href="/deals/">The full deal tracker</a></li>',
        '<li><a href="/how-it-works/">How the acquisition process works</a></li>',
        '<li><a href="/financing/">Financing a purchase like this</a></li>',
        '<li><a href="/design/">The design and furnishing playbook</a></li>',
        '<li><a href="/tax-strategy/">The tax strategy behind these purchases</a></li>',
    ]
    inner = "\n".join(f"            {i}" for i in items)
    return f"""        <div class="callout">
          <h3>Related</h3>
          <ul>
{inner}
          </ul>
        </div>"""


def render_landing(r, all_recs):
    """One deal, read top to bottom in about eight seconds.

    Numbers first, one sentence of context, a call to action, then the deal
    table. The narrative and the FAQ sit behind disclosures: they are worth
    having on the page for the reader who wants them and for search, and they
    are not worth putting between a visitor and the booking button.
    """
    url = f"{tpl.SITE}/case-studies/{r['slug']}/"
    trail = [("Home", "/"), ("Case Studies", "/case-studies/"),
             (f"{r['name']}, {r['city']}", f"/case-studies/{r['slug']}/")]

    props = ""
    if r.get("properties"):
        rows = "\n".join(
            f"              <tr><td>{m}</td><td>{b}</td><td>{p}</td></tr>"
            for m, b, p in r["properties"])
        props = f"""        <h2>The properties</h2>
        <div class="table-scroll">
          <table>
            <thead><tr><th>Market</th><th>Bedrooms</th><th>Purchase price</th></tr></thead>
            <tbody>
{rows}
            </tbody>
          </table>
        </div>
"""

    airbnb = ""
    if AIRBNB.get(r["slug"]):
        airbnb = (f'        <p><a class="btn btn-outline btn-sm" href="{AIRBNB[r["slug"]]}" '
                  f'target="_blank" rel="noopener nofollow">View the Airbnb listing</a></p>\n')

    beds = f", {r['beds']} bedrooms" if r["beds"] else ""
    story = "\n".join(f"          <p>{p}</p>" for p in r["body"])

    schema = tpl.graph(
        tpl.breadcrumb_schema([(n, p) for n, p in trail]),
        tpl.ORG_SCHEMA,
    ) + "\n" + tpl.article_schema(
        r["headline"], r["summary"], url, PUBLISHED, section="Client Case Study"
    ) + "\n" + tpl.faq_schema(r["faqs"])

    faq_items = "\n".join(
        f"""            <div class="faq-group">
              <h3>{q}</h3>
              <div class="faq-answer"><p>{a}</p></div>
            </div>""" for q, a in r["faqs"])

    body = f"""
  <section class="hero hero-page">
    <div class="wrap">
      {tpl.breadcrumb_html(trail)}
      <div class="hero-inner">
        <span class="eyebrow">Case Study &middot; {r["category"]}</span>
        <h1>{r["headline"]}</h1>
        <div class="article-meta">
          <span>{r["name"]}</span><span>&middot;</span><span>{r["market"]}</span><span>&middot;</span><span>{r["prop_type"]}{beds}</span>
        </div>
      </div>
    </div>
  </section>

  <section class="section-sm">
    <div class="wrap">
{big_numbers(r)}
      <p class="case-line">{r["result"]}</p>
      <div class="btn-row">
        <a class="btn btn-accent btn-lg" href="/apply/">Book a Call</a>
        <a class="btn btn-outline btn-lg" href="/case-studies/">See more deals</a>
      </div>
{hero_visual(r)}
    </div>
  </section>

  <section class="bg-alt">
    <div class="wrap">
      <article class="article">
{props}{deal_panel(r)}
{airbnb}{tax_panel(r)}
        <details class="disclose">
          <summary>The full story</summary>
{story}
        </details>

        <details class="disclose">
          <summary>Questions about this deal</summary>
{faq_items}
        </details>

{links_panel(r, all_recs)}

      </article>
    </div>
  </section>
{tpl.cta_band(
    "Want numbers like these on your own deal?",
    "One call. We will tell you what your income, timeline and tax position can actually buy.",
    ("/apply/", "Book a Call"),
    ("/case-studies/", "See all deals"))}"""

    return tpl.page(
        title=f"{r['name']}: {r['prop_type']}, {r['market']} | Case Study",
        description=r["summary"][:158],
        path=f"/case-studies/{r['slug']}/",
        body=body,
        extra_schema=schema,
        body_class="blog",
        active="/case-studies/",
    )


def render_index(recs):
    trail = [("Home", "/"), ("Case Studies", "/case-studies/")]

    groups = {}
    for r in recs:
        groups.setdefault(r["market_slug"], []).append(r)
    order = sorted(groups, key=lambda k: (-len(groups[k]), k))

    def market_label(ms):
        md = MARKET_DATA.get(ms)
        return md["name"] if md else groups[ms][0]["market"].split(",")[0]

    sections = []
    for ms in order:
        rs = groups[ms]
        heading = market_label(ms)
        cards = []
        for r in rs:
            head = r["metrics"][0]
            second = r["metrics"][2] if len(r["metrics"]) > 2 else r["metrics"][-1]
            cards.append(f"""        <article class="case-card" data-reveal>
          <div class="case-top">
            <span class="avatar">{r["initial"]}</span>
            <div>
              <h3><a href="/case-studies/{r["slug"]}/">{r["name"]}</a></h3>
              <span class="role">{r["prop_type"]}, {r["city"]}</span>
            </div>
          </div>
          <ul class="spec-list">
            <li><span class="k">{head[0]}</span><span class="v{" green" if head[2] else ""}">{head[1]}</span></li>
            <li><span class="k">{second[0]}</span><span class="v{" green" if second[2] else ""}">{second[1]}</span></li>
          </ul>
          <p><a class="btn btn-outline btn-sm" href="/case-studies/{r["slug"]}/">See the deal</a></p>
        </article>""")
        sections.append(f"""      <h2 class="market-group-head" id="{ms}">{tpl.esc(heading)}
        <span class="market-group-count">{len(rs)} {"deal" if len(rs) == 1 else "deals"}</span></h2>
      <div class="grid grid-3">
{chr(10).join(cards)}
      </div>""")

    jump = " ".join(f'<a class="chip" href="#{ms}">{tpl.esc(market_label(ms))}</a>'
                    for ms in order)

    faqs = [
        ("Are these results typical?",
         "No. Each page is one documented outcome for one property. Across the deals published "
         "with full financials the average cash-on-cash return is 13.3% and the range runs from "
         "under 2% to over 24%. Real estate involves risk, including loss of principal."),
        ("Why do clients appear as a first name and an initial?",
         "Because a full name plus a market plus a purchase price identifies a house. Clients "
         "authorized us to publish the numbers, not their identity, so no page on this site "
         "carries a client surname or a street address."),
        ("How is cash flow calculated?",
         "Gross booking revenue minus management, cleaning, supplies, utilities, insurance, "
         "property tax and debt service. Where a figure covers a single month rather than a "
         "year, the page says so, because peak-month cash flow on a seasonal property is not "
         "one twelfth of annual cash flow."),
        ("What is included in the entry cost?",
         "Down payment, closing costs and the design and furnishing budget. Furnishing is the "
         "line most buyers leave out, and it has to be funded at closing rather than out of the "
         "first season's revenue."),
        ("Can I speak to past clients?",
         "Yes. Ask for references on your first call and we will connect you with clients who "
         "bought in situations comparable to yours."),
    ]

    schema = tpl.graph(
        tpl.breadcrumb_schema(trail),
        """    {
      "@type": "CollectionPage",
      "name": "BNB Accelerator Case Studies",
      "description": "Documented client outcomes from done-for-you short-term rental acquisitions.",
      "url": "https://mybnbaccelerator.com/case-studies/",
      "isPartOf": { "@id": "https://mybnbaccelerator.com/#website" }
    }""",
        tpl.ORG_SCHEMA,
    ) + "\n" + tpl.faq_schema(faqs) + "\n" + tpl.graph(
        '    {\n      "@type": "ItemList",\n      "itemListElement": [\n' +
        ",\n".join(
            f'        {{ "@type": "ListItem", "position": {i}, '
            f'"url": "{tpl.SITE}/case-studies/{r["slug"]}/", '
            f'"name": "{tpl.esc(r["name"] + ", " + r["city"])}" }}'
            for i, r in enumerate(recs, 1)) +
        "\n      ]\n    }")

    n = len(recs)
    body = f"""
  <section class="hero hero-page">
    <div class="wrap">
      {tpl.breadcrumb_html(trail)}
      <div class="hero-inner">
        <span class="eyebrow">Client Results</span>
        <h1>Actual properties. Actual numbers.</h1>
        <p class="hero-sub">{n} client deals, each with its own page: what they paid, what it
        cost to get in, and what it returns.</p>
        <div class="btn-row">
          <a class="btn btn-accent btn-lg" href="/apply/">Book a Call</a>
          <a class="btn btn-ghost-light btn-lg" href="/deals/">Deal tracker</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section-sm">
    <div class="wrap">
      <div class="stats-bar">
        <div class="stat"><span class="stat-num">500+</span><span class="stat-label">Homes closed</span></div>
        <div class="stat"><span class="stat-num">260+</span><span class="stat-label">Clients served</span></div>
        <div class="stat"><span class="stat-num">80%</span><span class="stat-label">Repeat buyer rate</span></div>
        <div class="stat"><span class="stat-num">{n}</span><span class="stat-label">Deals published here</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="section-head" data-reveal data-hub-heading>
        <span class="eyebrow">Client results</span>
        <h2>Every deal, by market</h2>
        <p>Clients appear as a first name and an initial. We publish the numbers, not the address.</p>
      </div>
      <div class="chip-row">{jump}</div>

{chr(10).join(sections)}
    </div>
  </section>

  <section class="bg-alt">
    <div class="wrap wrap-narrow">
      <article class="article">
{tpl.faq_html(faqs)}
      </article>
    </div>
  </section>
{tpl.cta_band(
    "Book a call and run your own numbers",
    "We screen roughly a thousand deals a week and eliminate about 98%. Tell us your situation and we will tell you whether the strategy fits.",
    ("/apply/", "Book a Call"),
    ("/deals/", "See the deal tracker"))}"""

    return tpl.page(
        title=f"Case Studies (2026): {n} Real BNB Accelerator Client Deals",
        description=(f"{n} documented BNB Accelerator client deals, each with its own page: "
                     f"purchase price, entry cost, annual cash flow and cash-on-cash return, "
                     f"by market."),
        path="/case-studies/",
        body=body,
        extra_schema=schema,
        active="/case-studies/",
    )


def write(path, html):
    full = os.path.join(ROOT, path.strip("/"), "index.html")
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)


def main():
    recs = records()
    slugs = [r["slug"] for r in recs]
    assert len(slugs) == len(set(slugs)), "duplicate landing slug"
    for r in recs:
        write(f"/case-studies/{r['slug']}/", render_landing(r, recs))
    write("/case-studies/", render_index(recs))
    print(f"case studies: {len(recs)} landing pages + index")


if __name__ == "__main__":
    main()
