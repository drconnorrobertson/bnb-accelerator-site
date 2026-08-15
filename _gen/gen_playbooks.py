#!/usr/bin/env python3
"""Financing, design, management, revenue projection and tax strategy pillars."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tpl
from pillars import guide, hub, write

TAX_WARN = ("This page explains how the rules work. It is not tax advice. "
            "My BnB Accelerator, LLC is a real estate acquisition firm, not a CPA firm. "
            "Work with a qualified professional. Our independent partner firm is "
            '<a href="https://aetaxadvisors.com/short-term-rentals/" target="_blank" rel="noopener">AE Tax Advisors</a>.')

# ---------------------------------------------------------------- financing

FINANCING = [
    dict(
        slug="dscr-loans",
        name="DSCR Loans",
        eyebrow="Financing",
        h1="DSCR Loans for Short-Term Rentals: How They Actually Underwrite",
        title="DSCR Loans for Short-Term Rentals (2026 Guide)",
        description="How DSCR lenders underwrite short-term rentals, what ratio you need, what rate premium to expect, and when a DSCR loan beats a conventional investment mortgage.",
        blurb="Qualify on the property's income rather than your debt-to-income ratio.",
        lead="A debt service coverage ratio loan qualifies the property rather than the borrower. The lender is asking whether the rental income covers the mortgage payment, not what your personal debt-to-income ratio looks like. For a high earner who already carries a primary mortgage and wants to buy a third or fourth property, that difference is frequently what makes the purchase possible at all.",
        sections=[
            ("How the ratio is calculated", [
                "DSCR is gross rental income divided by the total monthly obligation, usually principal, interest, taxes, insurance and any association dues. A property producing $8,000 a month against a $6,400 total payment has a DSCR of 1.25.",
                "Most lenders want 1.0 or better, and pricing improves as the ratio rises. Below 1.0 some lenders will still write the loan, at a higher rate and often with a larger down payment, on the theory that the borrower is subsidizing the property from other income.",
                ("table", ["DSCR", "Meaning", "Typical treatment"], [
                    ["Below 1.0", "Income does not cover the payment", "Higher rate, larger down payment, some lenders decline"],
                    ["1.0 to 1.15", "Breakeven to thin", "Approvable, priced up"],
                    ["1.20 to 1.35", "Comfortable", "Standard pricing tier"],
                    ["Above 1.40", "Strong", "Best available pricing"],
                ]),
            ]),
            ("The short-term rental complication", [
                "For a long-term rental, income is a signed lease. For a short-term rental there is no lease, so lenders have to decide what income to credit, and they do it in one of three ways.",
                ("ol", [
                    "<strong>Market data.</strong> The lender accepts a third-party estimate, typically AirDNA or a comparable service, for a property of that size and type in that submarket. Most common for a property with no operating history.",
                    "<strong>Trailing twelve months.</strong> If the property is already an operating short-term rental, the lender uses actual statements from the platform. This is the most favorable treatment when the property performs well.",
                    "<strong>Long-term rent schedule.</strong> Some lenders ignore short-term income entirely and use the 1007 long-term rent estimate. This is the most conservative and frequently kills otherwise viable deals.",
                ]),
                "Which method a lender uses is the single largest variable in whether a specific short-term rental deal is financeable, and it varies enormously between lenders. Confirming the method before you are under contract, not after, is the difference between a smooth close and a scramble.",
            ]),
            ("What DSCR costs relative to conventional", [
                "DSCR loans are non-qualified mortgages, so they price above conventional investment property financing. Expect a rate premium, typically in the range of one to two percentage points over a comparable conventional investment loan, though the spread moves with the market.",
                "Down payments generally run 20 to 25%, occasionally more for a thin ratio or a market the lender considers volatile. Most DSCR products carry a prepayment penalty, commonly a stepdown over three to five years, which matters if you plan to refinance or sell early.",
                "Closing costs are typically higher too, and many DSCR lenders require an interest reserve or several months of payments in reserve at closing.",
                ("ul", [
                    "Rate premium over conventional investment financing.",
                    "20 to 25% down as a general baseline.",
                    "Prepayment penalty, commonly stepping down across three to five years.",
                    "Reserve requirements at closing.",
                    "No personal income documentation, which is the entire point.",
                ]),
            ]),
            ("When DSCR is the right tool", [
                "DSCR makes sense when your debt-to-income ratio is the binding constraint, when you are self-employed or have complex income that conventional underwriting handles badly, when you are buying through an LLC, or when you already hold the conventional financing limit on other properties.",
                "It makes less sense when you would qualify conventionally and the property is strong. The rate premium is real money over a thirty-year term, and conventional financing on an investment property is meaningfully cheaper.",
                "The most common pattern we see with clients buying multiple properties is conventional financing for the first one or two, then DSCR once the personal debt-to-income ratio stops cooperating. Peter Eck, an Associate Partner at IBM who has closed six properties with us, is a case where the financing structure had to evolve as the portfolio grew.",
                ("warn", "A DSCR approval based on an aggressive third-party revenue estimate is not a validation of the deal. The lender is protecting a loan at 75% of value. You are buying at 100%. Underwrite the property yourself against actual comparable booking data regardless of what the lender credits."),
            ]),
        ],
        faqs=[
            ("What DSCR do I need for a short-term rental loan?",
             "Most lenders want 1.0 or better, meaning rental income at least covers principal, interest, taxes, insurance and dues. Pricing improves above 1.20. Some lenders will write below 1.0 at a higher rate and larger down payment."),
            ("Do DSCR lenders count Airbnb income?",
             "It varies by lender and it is the most important question to ask up front. Some use third-party market estimates, some use the property's trailing twelve months of platform statements, and some ignore short-term income entirely and use a long-term rent schedule."),
            ("How much more does a DSCR loan cost?",
             "Typically one to two percentage points over comparable conventional investment financing, plus higher closing costs, a prepayment penalty over three to five years, and reserve requirements. The premium buys you qualification without personal income documentation."),
            ("Can I buy a short-term rental in an LLC with a DSCR loan?",
             "Usually yes. DSCR products are generally written to accommodate entity ownership, which is one of the practical reasons investors choose them over conventional financing."),
        ],
        related=[
            '<a href="/financing/conventional-vs-dscr/">Conventional versus DSCR financing</a>',
            '<a href="/financing/down-payment-strategies/">Down payment strategies for STR purchases</a>',
            '<a href="/revenue-projections/">Building a revenue projection a lender will accept</a>',
            '<a href="/case-studies/peter-eck-ibm-partner-six-properties/">Case study: financing a six-property portfolio</a>',
        ],
    ),
    dict(
        slug="conventional-vs-dscr",
        name="Conventional vs DSCR",
        eyebrow="Financing",
        h1="Conventional vs DSCR Financing for a Short-Term Rental",
        title="Conventional vs DSCR Loans for STRs (2026 Comparison)",
        description="A direct comparison of conventional investment financing and DSCR loans for short-term rentals: cost, qualification, property limits, entity ownership and speed.",
        blurb="Cheaper money with harder qualification, versus easier qualification at a price.",
        lead="Conventional investment financing is cheaper. DSCR financing is easier to qualify for. That is the entire trade, and which side of it you want depends on whether your constraint is cost or qualification.",
        sections=[
            ("The comparison in full", [
                ("table", ["", "Conventional investment", "DSCR"], [
                    ["Qualifies on", "Your personal income and DTI", "The property's income"],
                    ["Rate", "Lower", "Typically 1 to 2 points higher"],
                    ["Down payment", "15 to 25%", "20 to 25%, sometimes more"],
                    ["Income documentation", "Full: tax returns, W-2s, paystubs", "None"],
                    ["Property count limit", "Commonly capped around ten financed properties", "Generally no cap"],
                    ["Entity ownership", "Usually not permitted", "Generally permitted"],
                    ["Prepayment penalty", "None", "Common, stepping down over 3 to 5 years"],
                    ["Speed to close", "Slower, heavier documentation", "Often faster"],
                ]),
            ]),
            ("When conventional wins", [
                "If you qualify conventionally and intend to hold the property long term, take the conventional loan. Over a thirty-year term the rate difference is a large amount of money, and there is no prepayment penalty constraining a future refinance or sale.",
                "Conventional is also the better choice for a first or second investment property for most W-2 earners, because the debt-to-income ratio has not yet been consumed and the documentation burden, while annoying, is manageable.",
                "The practical ceiling is the financed property count. Conventional guidelines commonly cap a borrower somewhere around ten financed properties, and the underwriting gets progressively less friendly well before that.",
            ]),
            ("When DSCR wins", [
                ("ul", [
                    "Your debt-to-income ratio is the binding constraint, usually because you carry a primary mortgage and one or more investment properties already.",
                    "Your income is self-employment, K-1, or otherwise complex enough that conventional underwriting handles it badly.",
                    "You want to hold title in an LLC, which conventional financing generally does not permit.",
                    "You need to close quickly and the documentation burden of a conventional file would jeopardize the timeline.",
                    "You are past the conventional financed property limit.",
                ]),
                "There is also a timing argument. In a competitive market, a DSCR file with no income documentation can move faster than a conventional file waiting on tax transcripts, and a seller choosing between two similar offers will take the one that closes cleanly.",
            ]),
            ("The hybrid pattern most multi-property clients follow", [
                "The sequence we see most often is conventional financing for the first one or two properties, then a shift to DSCR as the personal debt-to-income ratio stops cooperating.",
                "Some investors then refinance early DSCR loans into conventional or portfolio products once the properties have an operating history and the personal balance sheet has changed. This is where the prepayment penalty on the original DSCR loan matters, and it is why the stepdown schedule is worth negotiating at origination rather than accepting as boilerplate.",
                "A third option worth knowing about is portfolio and commercial financing, where a lender writes one loan against several properties. That becomes relevant somewhere past the third or fourth acquisition, and it changes the analysis again, since cross-collateralization ties the properties together in ways that constrain selling one individually.",
                ("warn", "Whichever route you take, do not let the loan approval substitute for your own underwriting. A lender is protecting itself at roughly 75% of value with a foreclosure remedy. You are buying the whole thing."),
            ]),
        ],
        faqs=[
            ("Is a DSCR loan better than a conventional loan for an Airbnb?",
             "Not inherently. Conventional financing is cheaper and has no prepayment penalty. DSCR is easier to qualify for, permits entity ownership, and has no financed property cap. Take conventional if you qualify and plan to hold long term."),
            ("How many investment properties can I finance conventionally?",
             "Conventional guidelines commonly cap a borrower around ten financed properties, and underwriting tightens well before that. DSCR products generally have no equivalent cap, which is a common reason investors switch."),
            ("Can I refinance a DSCR loan into a conventional loan later?",
             "Often yes, once the property has an operating history and your personal balance sheet allows it. The constraint is the prepayment penalty on the original DSCR loan, which is why the stepdown schedule is worth negotiating at origination."),
        ],
        related=[
            '<a href="/financing/dscr-loans/">How DSCR lenders underwrite short-term rentals</a>',
            '<a href="/financing/down-payment-strategies/">Down payment strategies</a>',
            '<a href="/financing/">All STR financing guides</a>',
        ],
    ),
    dict(
        slug="down-payment-strategies",
        name="Down Payment Strategies",
        eyebrow="Financing",
        h1="Down Payment Strategies for a Short-Term Rental Purchase",
        title="STR Down Payment Strategies: HELOC, 1031, Partners (2026)",
        description="Where the down payment on a short-term rental actually comes from: HELOC on a primary residence, cash-out refinance, 1031 exchange, partnerships, and the tax refund loop.",
        blurb="HELOC, cash-out refi, 1031 exchange, partnership structures, and the refund loop.",
        lead="The down payment is the constraint that stops most qualified buyers, not the mortgage. A $700,000 property at 25% down needs $175,000 plus closing costs plus a furnishing budget, and that money has to come from somewhere that does not wreck the rest of your balance sheet.",
        sections=[
            ("Home equity on a primary residence", [
                "A HELOC or home equity loan on a primary residence is the most common source of a first short-term rental down payment, because most high earners have substantial equity sitting idle in a house they already own.",
                "A HELOC is a revolving line, usually at a variable rate, drawn only as needed. That flexibility is genuinely useful during an acquisition, since you can draw for the down payment and the furnishing budget separately and repay as cash flow arrives. The variable rate is the corresponding risk.",
                "A fixed-rate home equity loan trades that flexibility for rate certainty. If you are drawing the full amount at once and have no intention of repaying it quickly, the fixed structure is usually the better fit.",
                ("warn", "Both structures secure the debt against your primary residence. That is a real risk transfer: a short-term rental that underperforms now threatens the house you live in. Size the draw so that a bad first year is survivable from income alone."),
            ]),
            ("Cash-out refinance", [
                "If your existing mortgage rate is above current market, a cash-out refinance can pull equity out and improve the rate at the same time. If your existing rate is well below market, which is true for anyone who financed or refinanced during the low-rate window, a cash-out refinance means giving up that rate on the entire balance to access a fraction of it.",
                "That arithmetic is why HELOCs have been the dominant choice for the last several years. A HELOC leaves a favorable first mortgage untouched and prices only the new money.",
                "The calculation is worth running rather than assuming. The break-even depends on the spread between your current rate and market, the size of the cash-out relative to the balance, and how long you intend to hold.",
            ]),
            ("1031 exchange from an existing property", [
                "If the down payment is coming from selling another investment property, a 1031 exchange defers the capital gain rather than realizing it, which leaves substantially more capital available for the next purchase.",
                "The mechanics are unforgiving on timing. You have 45 days from the sale to identify replacement property in writing and 180 days to close. A qualified intermediary must hold the proceeds; touching the money personally disqualifies the exchange.",
                "That 45-day identification window is the practical difficulty, and it is where a done-for-you acquisition process has real value. Finding, underwriting and getting under contract on a genuinely good short-term rental inside 45 days is difficult if you are starting from scratch when the clock begins.",
                ("ul", [
                    "45 days to identify replacement property in writing.",
                    "180 days from sale to close.",
                    "A qualified intermediary must hold proceeds throughout.",
                    "Replacement property must be like-kind investment real estate.",
                    "Debt and equity generally need to be replaced to fully defer.",
                ]),
            ]),
            ("Partnerships and the refund loop", [
                "Partnering splits the down payment and splits the return. It works when the roles are genuinely complementary, typically one partner supplying capital and the other supplying the operating attention. It fails when both partners expected the other to handle the work.",
                "For short-term rental partnerships specifically, the material participation question needs to be settled in advance. The tax benefit that makes these purchases attractive to high earners depends on meeting a participation test, and a passive capital partner may not meet it, which changes the after-tax return for that partner substantially.",
                "The refund loop is the pattern that funds the second property for many of our clients. A cost segregation study on the first property, paired with a short-term rental that meets the seven-day average stay and material participation tests, can generate a first-year deduction large enough to produce a substantial tax refund. That refund becomes the down payment on the next property.",
                "It is not automatic and it is not universal. It depends on your marginal rate, your ability to meet the participation tests, and the specifics of the property. But when it works, it compresses the timeline between the first purchase and the second dramatically.",
                ("warn", TAX_WARN),
            ]),
        ],
        faqs=[
            ("Can I use a HELOC for a short-term rental down payment?",
             "Yes, and it is the most common source for a first purchase. The tradeoff is that the debt is secured against your primary residence, so size the draw such that a poor first year for the rental is survivable from income alone."),
            ("Should I do a cash-out refinance or a HELOC?",
             "It depends on your existing rate. If your current mortgage is well below market, a cash-out refinance means repricing the whole balance to access part of it, which is usually worse than a HELOC that leaves the first mortgage untouched."),
            ("How does a 1031 exchange work for buying a short-term rental?",
             "You have 45 days from selling the relinquished property to identify replacement property in writing and 180 days to close, with a qualified intermediary holding the proceeds. The 45-day window is the practical difficulty, since finding and contracting a good property that fast is hard from a standing start."),
            ("Can a tax refund fund the next property?",
             "For some clients, yes. A cost segregation study on a property meeting the seven-day average stay and material participation tests can produce a large first-year deduction and a substantial refund. Whether that happens depends on your marginal rate and your specific facts, so confirm it with your CPA before relying on it."),
        ],
        related=[
            '<a href="/tax-strategy/cost-segregation/">How cost segregation works</a>',
            '<a href="/tax-strategy/material-participation/">Material participation requirements</a>',
            '<a href="/financing/dscr-loans/">DSCR loans for short-term rentals</a>',
            '<a href="/financing/">All financing guides</a>',
        ],
    ),
    dict(
        slug="closing-costs-and-reserves",
        name="Closing Costs & Reserves",
        eyebrow="Financing",
        h1="What a Short-Term Rental Purchase Actually Costs to Close and Launch",
        title="STR Closing Costs, Furnishing Budget and Reserves (2026)",
        description="The full cost of getting a short-term rental open: closing costs, furnishing budget by bedroom count, launch expenses and the reserve most buyers skip.",
        blurb="The full number: closing, furnishing, launch and the reserve most buyers skip.",
        lead="The purchase price is roughly 70% of what it actually takes to open a short-term rental. Closing costs, furnishing, photography, supplies, permits and a genuine operating reserve make up the rest, and a buyer who budgets only for the down payment arrives at closing underfunded.",
        sections=[
            ("The full entry cost", [
                "Our published deal sheets show total entry cost alongside purchase price for exactly this reason. A $570,000 property in Panama City Beach carried a total entry of $320,457. A $540,000 property in Denver carried $185,619. The spread between those two ratios is furnishing scope, financing structure and reserve size.",
                ("table", ["Line item", "Typical range", "Notes"], [
                    ["Down payment", "20 to 25% of price", "Higher for DSCR or thin ratio"],
                    ["Closing costs", "2 to 4% of price", "Title, origination, escrow, recording"],
                    ["Prepaid escrows", "Varies", "Insurance and property tax funded at close"],
                    ["Furnishing and design", "$25K to $90K+", "Scales with bedroom count and tier"],
                    ["Photography and listing setup", "$1K to $3K", "Do not economize here"],
                    ["Initial supplies and consumables", "$2K to $5K", "Linens, kitchen, cleaning stock"],
                    ["Permits, licenses, registration", "$100 to $2K+", "Highly market dependent"],
                    ["Operating reserve", "6 months of carry", "The line buyers most often skip"],
                ]),
            ]),
            ("Furnishing budget by bedroom count", [
                "Furnishing is the largest variable cost and the one most consistently underestimated. It scales with bedroom count, but not linearly, because the shared spaces, kitchen and outdoor areas cost roughly the same in a four-bedroom as in a six.",
                ("table", ["Bedrooms", "Standard tier", "Premium tier"], [
                    ["3 to 4", "$25,000 to $40,000", "$45,000 to $65,000"],
                    ["5 to 6", "$35,000 to $55,000", "$60,000 to $90,000"],
                    ["7 to 9", "$50,000 to $80,000", "$90,000 and up"],
                ]),
                "Which tier is correct is decided by the comparable set, not by taste. In a market where every competing listing has a game room and designer photography, a standard-tier furnishing puts the property at the bottom of the pricing pack permanently. In a market where the competition is dated, a mid-tier furnishing wins outright.",
            ]),
            ("The reserve nobody budgets", [
                "Six months of full carry, meaning mortgage, insurance, property tax, utilities and association dues, held in cash and untouched. This is the line that gets cut when the furnishing budget runs over, and cutting it is the single most common reason a fundamentally sound property becomes a distressed sale.",
                "The reserve exists for specific, predictable events: a slow first quarter while reviews accumulate, a shoulder season that underperforms, a major appliance or HVAC failure, a storm that closes the market for three weeks, or an insurance renewal that reprices sharply.",
                "None of those are unusual. All of them are survivable with a reserve and painful without one.",
                ("warn", "If the deal only works because you skipped the reserve, the deal does not work. That is a hard rule, and it is the one we apply most often when telling a client that a property they like is not the right purchase."),
            ]),
            ("Where the money is well spent and badly spent", [
                ("ul", [
                    "<strong>Well spent: photography.</strong> It is the entire first impression on every platform and it costs a fraction of a percent of the purchase.",
                    "<strong>Well spent: mattresses and linens.</strong> The most frequently mentioned items in negative reviews, and reviews compound.",
                    "<strong>Well spent: the market-specific hero amenity.</strong> Hot tub in the mountains, heated pool in the desert, dock gear at the lake. It is what the comparable set has.",
                    "<strong>Badly spent: oversized televisions.</strong> Guests do not book a vacation rental for the screen.",
                    "<strong>Badly spent: fragile or high-maintenance decor.</strong> It will break, and replacing it is a recurring cost.",
                    "<strong>Badly spent: personal taste that does not photograph.</strong> The listing photos are the product, not the room.",
                ]),
            ]),
        ],
        faqs=[
            ("How much does it cost to furnish a short-term rental?",
             "Roughly $25,000 to $40,000 for a standard-tier three to four bedroom, and $60,000 to $90,000 or more for a premium five to six bedroom. Which tier is right is decided by what the comparable listings in that submarket already have."),
            ("What are typical closing costs on an investment property?",
             "Generally 2 to 4% of purchase price for title, origination, escrow and recording, plus prepaid escrows for insurance and property tax. DSCR loans usually carry higher closing costs than conventional financing."),
            ("How much reserve should I hold on a short-term rental?",
             "Six months of full carry including mortgage, insurance, property tax, utilities and dues, held in cash. If the deal only works because the reserve was skipped, the deal does not work."),
            ("What is total entry cost?",
             "Down payment plus closing costs, prepaid escrows, furnishing, photography, initial supplies, permits and the operating reserve. It is typically well above the down payment alone, which is why our deal sheets publish it separately from purchase price."),
        ],
        related=[
            '<a href="/design/">Design and furnishing playbook</a>',
            '<a href="/financing/down-payment-strategies/">Down payment strategies</a>',
            '<a href="/revenue-projections/">Building a revenue projection</a>',
            '<a href="/how-it-works/">How the acquisition process works</a>',
        ],
    ),
]


def gen_financing():
    for f in FINANCING:
        write(f"/financing/{f['slug']}/", guide(
            slug=f["slug"], parent="/financing/", parent_name="Financing",
            title=f["title"], h1=f["h1"], eyebrow=f["eyebrow"],
            description=f["description"], lead=f["lead"],
            sections=f["sections"], faqs=f["faqs"], related=f["related"],
            section_name="STR Financing",
        ))
    write("/financing/", hub(
        path="/financing/",
        title="Short-Term Rental Financing Guides (2026)",
        h1="How short-term rental purchases actually get financed",
        eyebrow="Financing",
        description="DSCR loans, conventional investment financing, down payment sources and the full entry cost of opening a short-term rental, explained for buyers who already have a mortgage.",
        sub="Most qualified buyers are stopped by the down payment and the debt-to-income ratio, not by the mortgage rate. These guides cover both, plus what the purchase actually costs beyond the price.",
        cards=[(f"/financing/{f['slug']}/", f["name"], f["blurb"]) for f in FINANCING],
        faqs=[
            ("What is the easiest way to finance a short-term rental?",
             "For a first or second property, conventional investment financing is usually cheapest if you qualify. Past that, a DSCR loan qualifying on the property's income rather than your debt-to-income ratio is the standard route, at a rate premium of roughly one to two points."),
            ("How much do I need to buy a short-term rental?",
             "Beyond the 20 to 25% down payment, budget 2 to 4% for closing costs, $25,000 to $90,000 for furnishing depending on size and tier, a few thousand for photography and supplies, and six months of carry as a reserve."),
            ("Can I use my primary residence equity?",
             "Yes, and a HELOC is the most common source for a first purchase. Because the debt is secured against your home, size the draw so a poor first year for the rental is survivable from income alone."),
        ],
        related=[
            '<a href="/tax-strategy/">The tax strategy behind these purchases</a>',
            '<a href="/revenue-projections/">Building a revenue projection a lender will accept</a>',
            '<a href="/case-studies/">Client case studies</a>',
        ],
        list_name="Short-Term Rental Financing Guides",
    ))
    print(f"financing: {len(FINANCING)} pages + hub")


# ------------------------------------------------------------------- design

def gen_design():
    write("/design/", guide(
        slug="", parent="/design/", parent_name="Design",
        title="STR Design and Furnishing Playbook (2026)",
        h1="Designing and Furnishing a Short-Term Rental That Books",
        eyebrow="Design & Furnishing",
        description="How to furnish a short-term rental for bookings rather than taste: budget by bedroom count, the amenities that price the property, photography, and what breaks first.",
        lead="Furnishing a short-term rental is a pricing decision disguised as a decorating decision. The comparable set in your submarket has already established what a property at your bedroom count and price tier looks like, and your job is to meet or beat it, not to express a preference.",
        sections=[
            ("Start from the comparable set, not from a mood board", [
                "Before choosing anything, pull the twenty listings that will genuinely compete with yours: same submarket, same bedroom count, same broad price tier. Look at what they have, what their photography emphasizes, and what their reviews praise and complain about.",
                "That set defines the floor. In the Smokies it means hot tub, mountain view and game room. In Orlando it means a heated private pool and a converted garage game room. In Scottsdale it means a heated pool and shaded outdoor living. A property missing the category-defining amenity competes on price against properties that have it, permanently.",
                "It also defines where you can differentiate cheaply. If every competing listing has beige walls and generic art, a single well-executed design point of view will separate your listing in a thumbnail grid, which is where the booking decision actually starts.",
            ]),
            ("Budget allocation that actually works", [
                ("table", ["Category", "Share of budget", "Why"], [
                    ["Beds, mattresses, linens", "20 to 25%", "The most-mentioned category in negative reviews"],
                    ["Living and dining", "15 to 20%", "Group gathering space drives length of stay"],
                    ["Hero amenity", "15 to 25%", "Hot tub, pool heat, game room; prices the listing"],
                    ["Outdoor living", "10 to 15%", "Photographs well and gets used constantly"],
                    ["Kitchen", "10%", "Group cooking is a primary use case"],
                    ["Decor and art", "5 to 10%", "Cheapest differentiation per dollar"],
                    ["Photography", "2 to 4%", "The single highest return line item"],
                ]),
                "Two allocation errors dominate. The first is spending on televisions and electronics, which guests do not book a vacation rental for. The second is under-spending on mattresses, which is the item most likely to generate a bad review that then suppresses bookings for months.",
            ]),
            ("Sleeping capacity versus bedroom count", [
                "Nightly rate is largely set by bedroom count, but guest satisfaction is set by whether everyone slept well. Adding capacity through bunk rooms, quality sleeper sofas or a converted bonus room raises the number of guests the property serves without raising the bedroom count on the listing.",
                "Whether that helps depends on the market. At the lake, in the Smokies and in Orlando, sleeping capacity above bedroom count is a genuine advantage, because group trips split cost per person. At a premium beach house or a design-forward ski property, cramming in bunks can undercut the positioning that justifies the rate.",
                "The rule of thumb: markets where guests are optimizing cost per person reward capacity. Markets where guests are optimizing experience reward space.",
            ]),
            ("Durability, because everything is a recurring cost", [
                ("ul", [
                    "<strong>Performance fabrics on all upholstery.</strong> Not optional in a rental.",
                    "<strong>Hard-surface flooring in traffic areas.</strong> Carpet in a short-term rental is a two-year consumable.",
                    "<strong>Commercial-grade mattress protectors.</strong> The cheapest insurance in the building.",
                    "<strong>Solid wood or metal bed frames.</strong> Particleboard frames fail within two seasons of turnover.",
                    "<strong>Simple, repairable fixtures.</strong> Anything requiring a specialist to service will sit broken.",
                    "<strong>Duplicate linen sets.</strong> Three sets per bed keeps same-day turnovers possible.",
                ]),
                "Assume a replacement cycle of three to five years on soft goods and seven to ten on case goods, and budget a recurring refresh line rather than treating furnishing as a one-time capital event. Properties that skip the refresh drift down the pricing pack invisibly, one review at a time.",
            ]),
            ("Photography is the product", [
                "Guests do not book the house, they book the photographs. Professional photography with proper lighting, wide-angle composition and a deliberate shot order is the highest-return line item in the entire furnishing budget, and it costs a fraction of a percent of the purchase price.",
                "The first image decides whether anyone sees the second. It should be the property's single strongest asset: the view, the pool, the hot tub deck, the great room. Not the exterior street view, which is what most amateur listings lead with.",
                "Reshoot after any meaningful refresh. A listing showing four-year-old photography of furniture that has since been replaced is underselling the property it actually is.",
            ]),
        ],
        faqs=[
            ("How much should I budget to furnish a short-term rental?",
             "Roughly $25,000 to $40,000 for a standard three to four bedroom and $60,000 to $90,000 or more for a premium five to six bedroom. The right tier is set by what competing listings in your submarket already have, not by personal preference."),
            ("What furniture holds up best in a short-term rental?",
             "Performance fabrics on all upholstery, hard-surface flooring in traffic areas, solid wood or metal bed frames, and simple repairable fixtures. Assume three to five years on soft goods and seven to ten on case goods."),
            ("Is professional photography worth it for an Airbnb?",
             "It is the highest-return item in the furnishing budget. Guests book the photographs, not the house, and professional photography costs a fraction of a percent of the purchase price. Reshoot after any meaningful refresh."),
            ("Should I add bunk beds to increase sleeping capacity?",
             "In markets where guests optimize cost per person, such as lake, Smokies and Orlando group travel, yes. In premium beach or design-forward ski properties, added capacity can undercut the positioning that justifies the nightly rate."),
        ],
        related=[
            '<a href="/guides/str-furnishing-design-guide/">Download the furnishing and design guide</a>',
            '<a href="/financing/closing-costs-and-reserves/">What a purchase actually costs to close and launch</a>',
            '<a href="/management/">Property management playbook</a>',
            '<a href="/property-types/">Property type guides</a>',
        ],
        section_name="Design & Furnishing",
    ))
    print("design: 1 page")


# --------------------------------------------------------------- management

def gen_management():
    write("/management/", guide(
        slug="", parent="/management/", parent_name="Management",
        title="Short-Term Rental Property Management Guide (2026)",
        h1="Property Management for Short-Term Rentals: Self, Co-Host or Full Service",
        eyebrow="Property Management",
        description="How to choose between self-management, a co-host and full-service management, what each really costs, and how to evaluate a local manager on performance rather than pitch.",
        lead="Management is the decision that determines whether owning a short-term rental is an investment or a second job, and it interacts directly with the tax strategy, because the participation tests that make these purchases attractive to high earners depend on who is doing the work.",
        sections=[
            ("The three models and what they cost", [
                ("table", ["Model", "Typical cost", "Owner time", "Best for"], [
                    ["Self-management", "Software and tools only", "8 to 15 hrs/week", "Local owners, hands-on, tax participation"],
                    ["Co-host / hybrid", "10 to 15% of revenue", "2 to 5 hrs/week", "Remote owners wanting some control"],
                    ["Full service", "20 to 35% of revenue", "Under 1 hr/week", "Passive owners, multiple properties"],
                ]),
                "The percentage is not the whole cost. Full-service managers frequently mark up cleaning, charge separately for maintenance coordination, and in some cases retain a portion of the cleaning fee charged to guests. Ask for the all-in number, including every fee that touches the property, not the headline percentage.",
                "The percentage also is not the whole comparison. A manager at 20% who runs occupancy ten points higher and prices better than a manager at 30% is not cheaper, they are better, and the gap is far larger than the fee difference.",
            ]),
            ("The tax interaction most owners miss", [
                "For a high earner using a short-term rental to offset W-2 income, the property must clear a seven-day average stay test and the owner must materially participate. Handing everything to a full-service manager can make the material participation test substantially harder to meet, because one of the common tests compares your participation to everyone else's, including paid management.",
                "This does not mean full-service management is incompatible with the strategy. It means the participation question has to be planned before the management agreement is signed, not discovered at tax time.",
                "The hybrid model exists largely for this reason. An owner who handles pricing, guest communication and vendor decisions while a local co-host handles turnover logistics is doing real, documentable work on the property.",
                ("warn", TAX_WARN),
            ]),
            ("Evaluating a local manager", [
                "The single most useful question is: show me the trailing twelve months of occupancy and average daily rate for three properties you manage that are comparable to mine, in this submarket. A manager who cannot or will not produce that is selling a pitch rather than a track record.",
                ("ul", [
                    "Actual performance data on comparable properties in the same submarket.",
                    "Which pricing tool they use and who sets the strategy.",
                    "Average response time to guest messages, and who covers nights and weekends.",
                    "Their cleaner bench depth, and what happens on a same-day turnover when someone calls out.",
                    "Maintenance response process and whether they mark up vendor invoices.",
                    "Contract term, termination notice, and whether they hold the listing account or you do.",
                ]),
                "That last item matters more than it sounds. If the manager owns the Airbnb listing, the reviews and the ranking history belong to them, and leaving means starting over. Insist that the listing lives in your account with the manager granted access.",
            ]),
            ("Systems that separate good operations from bad", [
                "Dynamic pricing that actually watches the market and the event calendar, rather than a static weekend uplift. This is the largest single performance gap between well-run and poorly-run listings, and it is wider in city markets than in vacation markets.",
                "A cleaning system with photographic checklists, depth on the bench, and same-day turnover capacity. In peak season a missed turnover is not a late check-in, it is a cancellation, a refund and a review.",
                "Preventive maintenance on a calendar rather than a reaction. HVAC service before summer, hot tub chemistry weekly, gutters before autumn, freeze protection before winter. Almost every expensive emergency in a short-term rental was a cheap scheduled task six months earlier.",
                "Guest screening and house rules that are actually enforced, particularly in city markets where a single party incident can trigger an enforcement action against the permit.",
                ("ol", [
                    "Dynamic pricing tied to real demand signals and the local event calendar.",
                    "Photographic cleaning checklists with a deep cleaner bench.",
                    "Scheduled preventive maintenance, not reactive repair.",
                    "Noise monitoring in shared living areas, disclosed to guests.",
                    "A local contact who can be at the property within thirty minutes.",
                    "Review response on every review, positive and negative.",
                ]),
            ]),
        ],
        faqs=[
            ("How much does short-term rental management cost?",
             "Full-service management typically runs 20 to 35% of revenue, and a co-host or hybrid arrangement 10 to 15%. Ask for the all-in figure including cleaning markups and maintenance coordination fees rather than the headline percentage."),
            ("Does hiring a property manager affect the STR tax strategy?",
             "It can. The material participation tests that let short-term rental losses offset W-2 income compare your participation to others, including paid management. Plan the participation question before signing a management agreement, and confirm the specifics with your CPA."),
            ("How do I evaluate a short-term rental manager?",
             "Ask for trailing twelve month occupancy and average daily rate on three comparable properties they manage in your submarket. A manager who cannot produce that is selling a pitch. Also confirm the listing account stays in your name."),
            ("Should the manager own the Airbnb listing?",
             "No. If the manager holds the account, the reviews and ranking history belong to them and changing managers means starting over. The listing should live in your account with the manager granted access."),
        ],
        related=[
            '<a href="/guides/str-property-management-sop/">Download the property management SOP</a>',
            '<a href="/tax-strategy/material-participation/">Material participation requirements</a>',
            '<a href="/design/">Design and furnishing playbook</a>',
            '<a href="/property-types/city/">City short-term rentals and enforcement risk</a>',
        ],
        section_name="Property Management",
    ))
    print("management: 1 page")


# ------------------------------------------------------- revenue projections

def gen_revenue():
    write("/revenue-projections/", guide(
        slug="", parent="/revenue-projections/", parent_name="Revenue Projections",
        title="How to Build an STR Revenue Projection You Can Trust (2026)",
        h1="Building a Short-Term Rental Revenue Projection That Survives Contact With Reality",
        eyebrow="Revenue Projections",
        description="How to project short-term rental revenue honestly: comparable selection, the seasonality trap, what belongs in the expense stack, and the stress tests that matter.",
        lead="Almost every failed short-term rental purchase can be traced to a revenue projection that was wrong in a specific, predictable way. Usually the buyer annualized a peak month, trusted the seller's proforma, or built an expense stack missing three or four real lines.",
        sections=[
            ("Start with comparables, not with an estimate tool", [
                "Third-party estimate tools are useful for screening and unreliable for underwriting. They work from broad submarket averages and cannot see the specific factors that decide whether a property performs: the amenity gap against its true competitive set, drive time to the demand anchor, whether the view is real, and whether the road is passable in February.",
                "Build the projection from a comparable set you assemble yourself. Twelve to twenty listings, same submarket, same bedroom count, same amenity tier. Pull their actual booked nights and rates across a full twelve months, not a peak quarter.",
                "The most common error in comparable selection is including properties that are not actually competitive. A nine-bedroom lodge with a mountain view and a game room is not a comparable for a four-bedroom cabin without a hot tub, even if they are two miles apart and both described as Smoky Mountain cabins.",
                ("warn", "Treat any proforma supplied by a seller or listing agent as a marketing document. They are routinely built by extrapolating peak-season rates across twelve months, which produces a revenue figure the property will never reach."),
            ]),
            ("Seasonality is the whole model", [
                "Revenue is not a monthly average. It is a shape, and the shape differs completely by market. Model twelve individual months and never divide an annual figure by twelve.",
                ("table", ["Market type", "Peak", "Trough", "Trap"], [
                    ["Smokies cabin", "June to October, holidays", "January to March", "Annualizing a June figure"],
                    ["Gulf beach", "March to August", "November to January", "Ignoring hurricane disruption"],
                    ["Southwest Florida", "January to March", "July to September", "Assuming a summer season exists"],
                    ["Desert", "October to April", "June to August", "Same as above, inverted"],
                    ["Ski", "December to March, plus summer", "Shoulder months", "Modeling an average snow year"],
                    ["Lake, no second driver", "Memorial Day to Labor Day", "The other 38 weeks", "Pricing on a July rate"],
                    ["Permitted city", "Flat with event spikes", "Mild", "Missing compression nights"],
                ]),
                "Victoria's nine-bedroom Sevierville cabin produced roughly $20,000 of cash flow in June. That is a real number and it is not one twelfth of an annual figure. Antonio's Fort Myers six-bedroom produced roughly $17,000 in February for the same reason in the opposite direction. Both models were built on the shape of their market, not on a monthly average.",
            ]),
            ("The complete expense stack", [
                "Most amateur projections include mortgage, cleaning and management, and stop. The lines below are the ones that turn a projected 12% cash-on-cash return into an actual 4%.",
                ("ul", [
                    "<strong>Debt service.</strong> Principal and interest at the actual rate you will get, not today's advertised rate.",
                    "<strong>Property tax.</strong> Reassessed at your purchase price, not the seller's assessed value. This catches many buyers.",
                    "<strong>Insurance.</strong> Quoted for the specific address, with wind and flood where applicable. Coastal insurance has repriced sharply.",
                    "<strong>Management.</strong> All-in, including cleaning markups and coordination fees.",
                    "<strong>Cleaning.</strong> Net of what guests pay, since the guest-facing cleaning fee rarely covers the true cost.",
                    "<strong>Utilities.</strong> At rental-use levels, not owner-use levels. Guests do not conserve.",
                    "<strong>Internet, streaming, monitoring, software.</strong> Small individually, meaningful together.",
                    "<strong>Supplies and consumables.</strong> Ongoing, not just the initial stock.",
                    "<strong>Association dues.</strong> Including the assessment risk in coastal and resort communities.",
                    "<strong>Maintenance reserve.</strong> 1 to 2% of property value annually.",
                    "<strong>Capital expenditure reserve.</strong> Roof, HVAC, appliances, and the furnishing refresh cycle.",
                    "<strong>Permits, licenses, lodging tax compliance.</strong> Market dependent and sometimes substantial.",
                    "<strong>Vacancy and platform fees.</strong> Built into the revenue side, but verify they actually are.",
                ]),
            ]),
            ("Stress tests that matter", [
                "A projection that only works in the base case is not a projection, it is a hope. Run the property against each of these and confirm it still services its debt.",
                ("ol", [
                    "<strong>Revenue at 75% of projection.</strong> The single most useful test. New listings routinely underperform in year one while reviews accumulate.",
                    "<strong>A disrupted peak season.</strong> A named storm, a wildfire, a bad snow year, or a road closure. Three lost peak weeks is not an exotic scenario.",
                    "<strong>Insurance repricing.</strong> Model a renewal 40% higher, which is not hypothetical on the Gulf Coast.",
                    "<strong>A regulatory tightening.</strong> For city and California desert properties, model the long-term rental floor.",
                    "<strong>A rate environment where you cannot refinance.</strong> If the plan depends on refinancing in two years, the plan has a dependency, not a strategy.",
                ]),
                "We screen roughly a thousand deals a week and eliminate about 98% of them, and the majority of eliminations happen at exactly this stage. The property looks fine in the base case and fails the stress test.",
            ]),
            ("What good looks like", [
                "A defensible projection has twelve distinct monthly revenue figures derived from a comparable set you assembled, a complete expense stack including reserves, and a stress-tested downside that still covers debt service. It should be a spreadsheet you can defend line by line, not a summary number.",
                "It should also be honest about the difference between cash flow and total return. A property producing modest cash flow while amortizing debt, appreciating, and generating a large first-year depreciation deduction against W-2 income can be an excellent investment even if the cash-on-cash number alone looks unremarkable. Judging a short-term rental on cash flow alone misses most of what makes the strategy work for high earners.",
            ]),
        ],
        faqs=[
            ("How accurate are AirDNA and similar revenue estimates?",
             "Useful for screening, unreliable for underwriting. They work from broad submarket averages and cannot see the amenity gap against a property's true competitive set, drive time to the demand anchor, or whether a claimed view is real. Build the projection from comparables you select yourself."),
            ("Should I trust a seller's proforma?",
             "No. Treat it as a marketing document. Seller proformas are routinely built by extrapolating peak-season rates across twelve months, producing a revenue figure the property will never reach."),
            ("What expenses do most Airbnb projections leave out?",
             "Property tax reassessed at the purchase price, insurance quoted for the actual address, utilities at rental-use levels, association assessment risk, a maintenance reserve of 1 to 2% of value, a capital expenditure reserve, and the furnishing refresh cycle."),
            ("What is a reasonable stress test for a short-term rental?",
             "Revenue at 75% of projection, a disrupted peak season of about three weeks, an insurance renewal 40% higher, and for city properties the long-term rental floor. If the property still services its debt under those, the projection is defensible."),
        ],
        related=[
            '<a href="/tools/str-revenue-calculator/">Run the numbers in the revenue calculator</a>',
            '<a href="/data/average-str-revenue-by-market/">Average STR revenue by market</a>',
            '<a href="/data/str-occupancy-rates-2026/">STR occupancy rates for 2026</a>',
            '<a href="/case-studies/victoria-sevierville-tn-9br-cabin/">Case study: what a real peak month looks like</a>',
        ],
        section_name="Revenue Projections",
    ))
    print("revenue projections: 1 page")


# ------------------------------------------------------------- tax strategy

TAX = [
    dict(
        slug="7-day-rule",
        name="The 7-Day Rule",
        eyebrow="Tax Strategy",
        h1="The 7-Day Rule: Why Short-Term Rentals Are Not Rental Activities",
        title="The STR 7-Day Rule Explained (2026)",
        description="How the seven-day average stay test under the Section 469 regulations removes a short-term rental from automatic passive classification, and what breaks it.",
        blurb="The regulation that takes a short-term rental outside automatic passive treatment.",
        lead="The seven-day rule is the provision that makes short-term rentals interesting to high W-2 earners rather than just another real estate investment. Under the Section 469 regulations, an activity where the average period of customer use is seven days or less is not treated as a rental activity, which is what opens the door to non-passive treatment.",
        sections=[
            ("What the rule actually says", [
                "Section 469 of the Internal Revenue Code generally treats rental activities as passive per se, meaning losses cannot offset non-passive income such as wages regardless of how much work the owner does. That default is why conventional long-term rental losses rarely help a high W-2 earner.",
                "The regulations under Section 469 carve out several exceptions to the definition of a rental activity. The most relevant one applies where the average period of customer use of the property is seven days or less. An activity meeting that description is not a rental activity for these purposes.",
                "That is the entire mechanism. It does not make losses deductible by itself. It removes the automatic passive classification, which is a necessary step, not a sufficient one.",
                ("warn", TAX_WARN),
            ]),
            ("How the average is calculated", [
                "Total rented days divided by the total number of rental periods across the tax year. A property rented 200 days across 50 separate bookings has an average period of customer use of 4 days, which clears the test comfortably.",
                "It is an average across the year, not a maximum per booking. A single long stay does not automatically break it. The risk is accumulation.",
                "Documentation matters here. The calculation depends on booking-level data, so keep the platform records that support it. A reconstructed estimate is a weak position if the return is examined.",
            ]),
            ("What breaks it", [
                "The most common cause is accepting extended bookings for occupancy without tracking the annual average. Snowbird stays, corporate housing placements, insurance relocation tenants and off-season monthly rentals all push the average up.",
                "The arithmetic moves faster than owners expect. A property with 40 short bookings averaging 3 nights has 120 rented days across 40 periods, an average of 3.0. Add three 30-day bookings and it becomes 210 days across 43 periods, an average of 4.9. Add three more and it crosses 7.",
                ("ul", [
                    "Monthly and multi-month off-season bookings.",
                    "Corporate housing or traveling professional placements.",
                    "Insurance displacement tenants after a local disaster.",
                    "Snowbird stays in winter markets.",
                    "Any strategy that fills a slow season with long stays without running the annual math.",
                ]),
                "The practical control is to compute the running average monthly rather than discovering the answer in April. If the average is drifting toward the threshold, the remaining bookings for the year have to be managed accordingly.",
            ]),
            ("What has to happen next", [
                "Clearing the seven-day test is step one of two. Because the activity is no longer automatically a rental activity, the general material participation rules apply, and you must materially participate under one of the seven tests for the loss to be non-passive.",
                "Both conditions must hold in the same tax year. A property that clears the seven-day test but where the owner does not materially participate produces a passive loss, which is the same outcome as a conventional rental.",
                "When both hold, the loss is non-passive and can offset W-2 and other ordinary income. Pair that with a cost segregation study and the first-year deduction can be large enough to change the household's entire tax position for the year.",
            ]),
        ],
        faqs=[
            ("How is the 7-day average calculated for a short-term rental?",
             "Total rented days divided by the total number of rental periods across the tax year. A property rented 200 days across 50 bookings has an average period of customer use of 4 days, which clears the test. It is an annual average, not a per-booking maximum."),
            ("Does the 7-day rule alone make my losses non-passive?",
             "No. Clearing the seven-day test removes the activity from automatic rental classification under Section 469, but you must also materially participate under one of the seven IRS tests for the loss to be treated as non-passive. Both have to hold."),
            ("What breaks the 7-day rule?",
             "Accumulating long bookings without tracking the annual average. Snowbird stays, corporate housing, insurance placements and off-season monthly rentals are the usual causes, and the average moves faster than owners expect."),
            ("Should I track the average during the year?",
             "Yes. Compute the running average monthly rather than discovering it at tax time, because once the year closes there is nothing to be done about it."),
        ],
        related=[
            '<a href="/tax-strategy/material-participation/">Material participation: the second test</a>',
            '<a href="/tax-strategy/cost-segregation/">Cost segregation and first-year deductions</a>',
            '<a href="/blog/7-day-rule-explained/">Longer walkthrough of the seven day rule</a>',
            '<a href="/answers/what-is-the-str-loophole/">What is the STR loophole?</a>',
        ],
    ),
    dict(
        slug="material-participation",
        name="Material Participation",
        eyebrow="Tax Strategy",
        h1="Material Participation for Short-Term Rentals: The Seven Tests",
        title="STR Material Participation Tests Explained (2026)",
        description="The seven material participation tests, which ones short-term rental owners realistically meet, what counts as participation, and how to document it.",
        blurb="The seven tests, which ones actually apply, and how to document participation.",
        lead="Material participation is the second half of the short-term rental tax strategy and the half that gets people in trouble. Clearing the seven-day average stay test removes the automatic passive classification. Material participation is what actually makes the loss non-passive, and it has to be earned every year and documented contemporaneously.",
        sections=[
            ("The seven tests", [
                "The regulations provide seven tests. Satisfying any one of them establishes material participation for the activity in that tax year.",
                ("ol", [
                    "More than 500 hours of participation in the activity during the year.",
                    "Participation constitutes substantially all of the participation in the activity by all individuals, including non-owners.",
                    "More than 100 hours, and no other individual participates more.",
                    "The activity is a significant participation activity of more than 100 hours, and total significant participation across all such activities exceeds 500 hours.",
                    "Material participation in the activity for any five of the preceding ten tax years.",
                    "The activity is a personal service activity in which the taxpayer materially participated for any three preceding years.",
                    "Based on all facts and circumstances, participation is regular, continuous and substantial.",
                ]),
                ("warn", TAX_WARN),
            ]),
            ("Which tests short-term rental owners realistically meet", [
                "For a W-2 earner with one or two properties, the practical routes are test three, more than 100 hours with nobody participating more, and test two, substantially all of the participation.",
                "Test one, the 500-hour test, is achievable for an owner running the property directly but demanding for someone with a full-time career. It is the cleanest test to defend if you can meet it.",
                "Test seven, the facts and circumstances test, is the weakest position to rely on. It has significant limitations in the regulations and it invites exactly the kind of judgment call you do not want in an examination.",
                "Test three is where the management structure becomes decisive. If a full-service manager participates more hours than you do, test three fails. This is the single most common way the strategy breaks, and it is entirely a planning problem rather than an unavoidable one.",
            ]),
            ("What counts and what does not", [
                ("table", ["Generally counts", "Generally does not count"], [
                    ["Guest communication and booking management", "Time spent as an investor reviewing financials"],
                    ["Setting and adjusting pricing", "Studying and researching the market before purchase"],
                    ["Coordinating cleaning and maintenance", "Travel time in many circumstances"],
                    ["Vendor selection and management", "Work done in a capacity not customary for an owner"],
                    ["Shopping for and stocking supplies", "Time where the primary purpose is avoiding the passive rules"],
                    ["Handling repairs personally", "Personal use time at the property"],
                    ["Listing optimization and photography direction", ""],
                    ["Bookkeeping specific to the property", ""],
                ]),
                "Two categories deserve particular caution. Investor-type activities, reviewing statements and analyzing performance in a non-managerial capacity, are specifically excluded. And personal use of the property is not participation regardless of what maintenance you happen to do while you are there.",
            ]),
            ("Documentation is the whole defense", [
                "The regulations permit participation to be established by any reasonable means, but in practice a contemporaneous log is the difference between a defensible position and an expensive one. Reconstructing hours after the fact from memory and calendar entries is a weak position.",
                ("ul", [
                    "Log the date, the duration, a specific description of the task, and who performed it.",
                    "Keep it contemporaneously. Weekly at the outside, daily is better.",
                    "Track hours for every other person who works on the property, including managers and cleaners, because tests two and three depend on the comparison.",
                    "Retain corroborating evidence: message threads, vendor invoices, pricing change records, receipts.",
                    "Keep a separate log per property unless you have made a valid grouping election.",
                ]),
                "The grouping question is worth raising with your CPA early if you own more than one property. Whether the activities are grouped changes how the hours are counted, and the election has consequences beyond the current year.",
            ]),
            ("How management structure interacts", [
                "This is the practical crux. Full-service management typically means the manager participates more hours than the owner, which defeats test three, and it makes test two nearly impossible.",
                "The hybrid arrangement exists largely to solve this. An owner who personally handles pricing strategy, guest communication, vendor selection and purchasing while a local co-host handles turnover logistics is doing substantial, documentable work.",
                "None of this means self-management is required. It means the participation structure has to be designed before the management agreement is signed. Deciding to pursue the strategy in March for the prior tax year is too late, because the hours either happened or they did not.",
            ]),
        ],
        faqs=[
            ("What are the material participation tests for a short-term rental?",
             "There are seven tests and meeting any one establishes material participation. The practical routes for most owners are more than 500 hours, more than 100 hours with nobody participating more, or participation constituting substantially all participation in the activity."),
            ("Does using a property manager disqualify material participation?",
             "Not automatically, but it makes the tests harder. If a full-service manager participates more hours than you, the 100-hour test fails. This is a planning problem to solve before signing a management agreement, not after."),
            ("What activities count toward material participation?",
             "Guest communication, pricing, coordinating cleaning and maintenance, vendor management, supply purchasing, repairs, listing optimization and property-specific bookkeeping. Investor-type activities such as reviewing financials in a non-managerial capacity generally do not count."),
            ("How should I document participation hours?",
             "A contemporaneous log with date, duration, specific task description and who performed it, kept weekly at the outside, plus corroborating messages, invoices and receipts. Also track hours worked by managers and cleaners, since two of the tests depend on that comparison."),
        ],
        related=[
            '<a href="/tax-strategy/7-day-rule/">The seven day rule: the first test</a>',
            '<a href="/tax-strategy/cost-segregation/">Cost segregation and first-year deductions</a>',
            '<a href="/management/">How management structure affects participation</a>',
            '<a href="/blog/material-participation-str/">Longer walkthrough of material participation</a>',
        ],
    ),
    dict(
        slug="cost-segregation",
        name="Cost Segregation",
        eyebrow="Tax Strategy",
        h1="Cost Segregation for Short-Term Rentals: How the First-Year Deduction Works",
        title="Cost Segregation for Short-Term Rentals (2026 Guide)",
        description="How a cost segregation study reclassifies building components into shorter recovery periods, what a study costs, when it is worth doing, and how depreciation recapture works.",
        blurb="Reclassifying components into 5, 7 and 15-year property to accelerate depreciation.",
        lead="A cost segregation study is an engineering-based analysis that reclassifies components of a building from the long default recovery period into shorter ones. It is the amplifier on the short-term rental tax strategy: the seven-day rule and material participation make a loss usable, and cost segregation makes the loss large.",
        sections=[
            ("What a study actually does", [
                "Without a study, a building is depreciated over a single long recovery period, 39 years for nonresidential property, which is how a short-term rental with an average stay of seven days or less is generally classified, or 27.5 years for residential rental property.",
                "A cost segregation study separates the purchase into components and assigns each to its correct recovery period. Carpeting, cabinetry, specialty electrical, appliances and decorative fixtures may fall into 5 or 7-year property. Land improvements such as driveways, landscaping, fencing and site lighting typically fall into 15-year property.",
                ("table", ["Class", "Typical components"], [
                    ["5-year", "Carpet, appliances, decorative lighting, specialty electrical, furnishings"],
                    ["7-year", "Certain fixtures and equipment"],
                    ["15-year", "Driveways, walkways, landscaping, fencing, site utilities, pools"],
                    ["27.5 or 39-year", "The remaining structural building components"],
                ]),
                "The shorter-life components then become eligible for accelerated and bonus depreciation treatment, which is what concentrates a large deduction into the first year rather than spreading it across decades.",
                ("warn", TAX_WARN),
            ]),
            ("Why the timing matters so much", [
                "The deduction is not created by the study. It was always going to be taken; the study changes when. Moving deductions forward is valuable because a dollar of deduction against a high marginal rate today is worth more than the same dollar spread across thirty years, and because the cash it frees can be redeployed immediately.",
                "For a high earner, the effect can be dramatic. A study on a property in the low seven figures can produce a first-year deduction in the hundreds of thousands of dollars. Against a top combined federal and state marginal rate, that translates into a very large reduction in tax for the year.",
                "That reduction is what funds the next acquisition for many of our clients. The refund becomes the down payment, which is why several of them have moved from one property to three or six faster than their cash flow alone would have permitted.",
            ]),
            ("When a study is worth commissioning", [
                ("ul", [
                    "The property is a short-term rental that clears the seven-day average stay test, and you materially participate. Without both, the accelerated loss is passive and mostly stranded.",
                    "Your marginal rate is high enough that the deduction has real value. This strategy is built for people losing substantial sums to taxes.",
                    "The purchase price is large enough to justify the study cost. Studies generally run from a few thousand dollars upward, often priced per square foot.",
                    "You intend to hold the property for a meaningful period, because a fast sale accelerates recapture.",
                ]),
                "A study can also be applied to a property purchased in a prior year without amending returns, by filing a change in accounting method and claiming the cumulative catch-up adjustment in the current year. That is a genuinely useful option for someone who bought before understanding the strategy, and it is worth raising with your CPA.",
            ]),
            ("Recapture, which nobody mentions in the sales pitch", [
                "Accelerated depreciation is deferral, not forgiveness. When the property sells, depreciation taken is recaptured. Section 1245 recapture on the personal property components is taxed as ordinary income, and Section 1250 unrecaptured gain on the real property portion is taxed at a separate rate.",
                "That means the strategy works best for a long hold, or for an exit structured as a 1031 exchange that defers the recapture into the replacement property.",
                "It also means the after-tax return has to be evaluated across the whole hold period, not just the first year. A large first-year deduction followed by a sale in year three is a much less attractive outcome than the same deduction followed by a fifteen-year hold, and anyone presenting the strategy without mentioning recapture is not giving you the full picture.",
            ]),
            ("How it fits with the rest", [
                "The three pieces work in sequence, and all three have to hold. The seven-day average stay test takes the activity outside automatic passive classification. Material participation makes the loss non-passive. Cost segregation makes the loss large.",
                "Miss the first, and the loss is passive. Miss the second, and the loss is passive. Skip the third, and the loss exists but is small enough that it does not change your tax position meaningfully.",
                "This sequence is what we call the Reverse Offset Method: an appreciating, cash-producing asset funded in significant part by dollars that were otherwise going to the Treasury. It is also why we work alongside an independent partner firm on the tax side rather than pretending to be a CPA firm ourselves.",
            ]),
        ],
        faqs=[
            ("What is a cost segregation study?",
             "An engineering-based analysis that reclassifies components of a building purchase into shorter depreciation recovery periods, typically 5, 7 and 15-year property, so that a much larger share of the deduction falls in the early years rather than being spread across 27.5 or 39 years."),
            ("Is cost segregation worth it for a short-term rental?",
             "It depends on whether the property clears the seven-day average stay test, whether you materially participate, your marginal tax rate, the purchase price, and your intended hold period. Without the first two, the accelerated loss is passive and largely stranded."),
            ("What is depreciation recapture?",
             "When the property sells, depreciation previously taken is recaptured. Personal property components are recaptured as ordinary income under Section 1245, and the real property portion is subject to unrecaptured Section 1250 gain treatment. Accelerated depreciation is deferral, not forgiveness."),
            ("Can I do a cost segregation study on a property I already own?",
             "Generally yes, without amending prior returns, by filing a change in accounting method and taking the cumulative catch-up adjustment in the current year. Discuss the mechanics with your CPA before proceeding."),
        ],
        related=[
            '<a href="/tax-strategy/7-day-rule/">The seven day rule</a>',
            '<a href="/tax-strategy/material-participation/">Material participation tests</a>',
            '<a href="/answers/what-is-cost-segregation/">Short answer: what is cost segregation?</a>',
            '<a href="/financing/down-payment-strategies/">Using a refund to fund the next purchase</a>',
        ],
    ),
]


def gen_tax():
    for t in TAX:
        write(f"/tax-strategy/{t['slug']}/", guide(
            slug=t["slug"], parent="/tax-strategy/", parent_name="Tax Strategy",
            title=t["title"], h1=t["h1"], eyebrow=t["eyebrow"],
            description=t["description"], lead=t["lead"],
            sections=t["sections"], faqs=t["faqs"], related=t["related"],
            section_name="STR Tax Strategy",
            cta=("Find out if this applies to your situation",
                 "Thirty minutes with a specialist CPA tells you whether the strategy is worth pursuing before you look at a single property."),
        ))
    print(f"tax strategy: {len(TAX)} sub-pages")


if __name__ == "__main__":
    gen_financing()
    gen_design()
    gen_management()
    gen_revenue()
    gen_tax()
