#!/usr/bin/env python3
"""Closing section per operations post."""

EXTRA = {
    "occupancy-versus-rate-which-to-optimize": ("A worked comparison", [
        "Two four-bedroom cabins in the same corridor. Property A runs 78% occupancy at $310 a night across 60 bookings. Property B runs 58% occupancy at $415 a night across 32 bookings. Annual gross is close: roughly $88,000 against roughly $87,700.",
        "Property A has 60 turnovers at $200 each, or $12,000. Property B has 32, or $6,400. That is a $5,600 difference in cleaning alone before consumables, and Property A is also absorbing roughly twice the wear on linens, furniture and finishes.",
        "Property A's owner reports a busy, successful cabin. Property B's owner reports a quieter one. Property B is roughly $6,000 to $9,000 a year more profitable and will need its furnishing refresh later. The occupancy number is the one that feels like performance and the one that is least connected to it.",
    ]),
    "pricing-the-booking-window": ("Testing your own window", [
        "You can establish your market's booking window from your own data in one season. Export your reservations with the booking date and the check-in date, subtract, and plot the distribution.",
        "Most operators are surprised by the result. Properties owners believe book two months ahead frequently show a median lead time under three weeks, and the handful of long-lead bookings that shaped the impression turn out to be peak weeks and holidays only.",
        "Once you know the actual distribution, the pricing rules follow. If the median lead time is eighteen days, a calendar that looks empty at thirty days out is normal and discounting it is giving away revenue. If the median is ninety days, an empty thirty-day window is a genuine signal.",
    ]),
    "the-cleaning-fee-problem": ("The competitive check", [
        "Before setting a fee, look at what your ten closest comparables charge and, more importantly, what their minimum stays are. Those two numbers move together, and a property with a high fee and a one-night minimum is the one guests complain about.",
        "If your comparables all run a $250 fee with a three-night minimum and you run $250 with a one-night minimum, you are the expensive option in every search where a guest is looking at short stays, and the cheapest option for nobody.",
        "Also check whether the market's fees are trending. In several markets, platforms surfacing total price more prominently has pushed operators toward absorbing more of the fee into the rate. Whether that is right for you depends on your stay length mix, but being significantly out of step with the comparable set on displayed total is a booking problem regardless of the underlying economics.",
    ]),
    "reviews-compound-like-interest": ("The volume defense", [
        "The most reliable protection against a bad review is a large denominator. A single three star review among twelve reviews visibly moves the average. The same review among two hundred does not.",
        "That argues for asking every guest, once, and for prioritizing review volume in the first year even where it means accepting bookings at rates you would otherwise hold out on.",
        "It also argues against long gaps in operation. A property that goes dark for a season stops accumulating reviews while competitors continue, and re-entering the market with a stale review profile is measurably harder than staying visible.",
        "The practical target for a new listing is to get past ten reviews as fast as safely possible, and past fifty within the first full year. Beyond that, individual reviews stop being existential and start being feedback, which is a much more comfortable place to operate from.",
    ]),
    "preventive-maintenance-calendar": ("Building the vendor bench before you need it", [
        "The most common reason preventive maintenance does not happen is that the owner has no one to call. Finding an HVAC technician in a resort market in July is difficult and expensive; finding one in April is neither.",
        "Build the list in the first month of ownership: HVAC, plumber, electrician, handyman, pool or hot tub service, landscaper, and a general contractor for anything larger. Meet them, use them for something small, and confirm they will take a call from your property.",
        "Ask each about their seasonal availability, because vendors in resort markets are frequently booked out during exactly the periods you are most likely to need them. A relationship established in the shoulder season gets a call answered in peak.",
        "For remote owners, one scheduled seasonal inspection by a trusted local, paid for as a line item, catches most of what a walk-through would catch and costs a fraction of a single emergency.",
    ]),
    "the-first-30-days-checklist": ("Why compressing the gap is worth real money", [
        "The carrying cost of an idle month is easy to underestimate. On a $700,000 property, mortgage, insurance, property tax and utilities can run several thousand dollars, and that is before considering the revenue the month would have produced.",
        "In a peak-season month the combined figure can exceed $15,000 of opportunity cost. That is not an abstraction; it is a real reduction in first-year return that never gets recovered.",
        "There is also a compounding effect through ranking. A property that launches into peak season with reviews accumulating enters the following shoulder season with an established profile. One that launches in the shoulder starts from zero when demand is thin, which is a harder place to build velocity.",
        "The work required to compress the gap is scheduling rather than spending. Ordering furnishing during escrow costs the same as ordering it after closing. The difference is entirely in when the calendar opens.",
    ]),
    "listing-photos-shot-order": ("Testing the hero image", [
        "Most platforms allow reordering photographs at any time, which makes the hero image a testable variable rather than a fixed decision.",
        "Run one image for a defined period, note the listing's view and booking performance, then swap and compare. The effect can be substantial, particularly in crowded markets where the thumbnail is doing most of the work.",
        "What frequently wins is not the most beautiful image but the most legible one at thumbnail size. A wide interior shot that reads as a generic room at 200 pixels loses to a hot tub deck at sunset that is instantly recognizable.",
        "Seasonal swapping is worth testing too. A ski property leading with a snow image in October and a summer image in May is selling the season the guest is currently shopping for, which is a small change with a measurable effect.",
    ]),
    "guest-communication-templates": ("Automation without sounding automated", [
        "All five messages can be automated on most management platforms, triggered by booking, days before arrival, hours after check-in and days before checkout.",
        "The risk is that automated messages read as automated, which undercuts the trust they are meant to build. Two things fix that: writing them in a natural voice rather than a corporate one, and including specifics that could only apply to your property and market.",
        "A message that says 'the grocery store closest to the cabin is the Food City on the Parkway, about eight minutes down the hill' reads as a person. One that says 'local amenities are available nearby' reads as a template, because it is.",
        "Leave the post-check-in message slightly less polished than the rest. It is the one where guests are most likely to reply with a problem, and a message that reads as a genuine person asking is more likely to get an honest answer than a formatted one.",
    ]),
    "amenity-roi-ranking": ("Amenities that create liability", [
        "Some high-return amenities carry risk that belongs in the decision. Hot tubs, pools and trampolines are the common ones, and all three raise both insurance and injury exposure.",
        "That is not an argument against them. A hot tub is close to mandatory in mountain markets and a heated pool is close to mandatory in desert ones, and a property without them competes at a permanent discount.",
        "It is an argument for handling them properly: confirming coverage with your insurer specifically for the amenity, meeting any local safety requirements such as pool fencing and alarms, posting rules clearly, and maintaining them on a schedule rather than reactively.",
        "Trampolines and similar recreational equipment are a different calculation, because they add meaningful injury exposure without a corresponding booking benefit in most markets. Several insurers exclude them outright. In most cases the sensible answer is not to have one.",
    ]),
    "handling-a-damage-claim": ("Budgeting for damage as a cost", [
        "Owners who treat every incident as an anomaly to be recovered spend more time and goodwill than the recovery is worth. Owners who budget a damage allowance treat the same incidents as a line item and move on.",
        "A reasonable planning figure is a small percentage of gross revenue set aside annually for damage, breakage and loss that will not be recovered. That covers the stained towels, the broken glassware, the missing hair dryer and the scuffed wall that are simply part of operating.",
        "With that allowance in place, the claim decision becomes cleaner. Below the allowance threshold, absorb it. Above it, document and claim. That removes the emotional component from a decision that should be arithmetic.",
        "It also produces a more accurate proforma. A model with no damage line is understating cost, and a model with an accurate one is a better basis for judging whether a property actually performs.",
    ]),
    "direct-bookings-worth-the-effort": ("What the numbers have to clear", [
        "Before building a direct channel, calculate what it would actually save. Take last year's platform commission, estimate what share of bookings you could realistically convert, and multiply.",
        "For a single property producing $90,000 gross with 3% host commission, that is $2,700 a year in total. Converting a third of bookings saves $900. Against the cost of a booking-capable website, payment processing, damage protection, tax collection setup and the time to run it, the trade is frequently unfavorable.",
        "For an owner with four properties in one market producing $400,000 combined, the same arithmetic supports a much stronger case, and the marketing effort amortizes across the portfolio.",
        "The exception at any scale is repeat guests, where the conversion cost is close to zero because the relationship already exists. That channel is worth building even for a single property, and it does not require a marketing operation, only a way to take a booking and collect the tax.",
    ]),
    "what-to-do-in-a-slow-season": ("Deciding which strategy fits", [
        "The choice comes down to three questions. How severe is the trough? Is there a genuinely different guest available? And does your tax position constrain long stays?",
        "A mild trough with a strong primary season generally favors using the window for work, because the forgone revenue is small and the property benefits from arriving at peak refreshed.",
        "A severe trough in a market with real alternative demand, such as a desert property with remote work appeal or a college town with academic-year stays, favors targeting a different guest, subject to the seven-day average caution.",
        "A severe trough with no alternative demand favors pricing to cover carry, accepting that the months will be roughly break-even and protecting review velocity through them. What matters most is choosing deliberately rather than defaulting into whatever happens, which is what produces the panicked discounting that costs the most.",
    ]),
    "switching-managers-without-losing-a-season": ("The self-management alternative", [
        "Before hiring a replacement, it is worth asking whether the property needs full-service management at all. Many owners hire it by default and discover afterward that the cost is 20 to 35% of revenue for work they could largely direct themselves.",
        "The hybrid model, where the owner handles pricing, guest communication and vendor decisions while a local co-host handles turnover logistics, typically costs 10 to 15% and gives the owner far more control over the two things that drive performance: pricing and guest experience.",
        "It also aligns better with the material participation tests, which is a substantial financial consideration for owners relying on the tax treatment.",
        "The requirement is that the owner actually does the work. A hybrid arrangement where the owner intends to manage pricing and then does not is worse than full service, because nobody is doing it. Be honest about the hours available before choosing the structure.",
    ]),
    "noise-monitoring-and-neighbors": ("Documenting your compliance", [
        "In markets with active enforcement, keeping a record of your own controls is worth the small effort it takes. If a complaint pattern does develop, the difference between an owner who can demonstrate systematic controls and one who cannot is substantial.",
        "Keep the disclosed noise monitoring policy, the house rules as presented to guests, the occupancy limits, the parking instructions, and a log of any incidents with what was done in response.",
        "Also keep evidence of the neighbor relationship: the introduction, the direct contact number provided, and any calls received and resolved. An owner who can show a neighbor called and the issue was resolved in twenty minutes is in a different position from one with no record.",
        "None of this is difficult and none of it matters until it does. In a capped-permit market where the permit is a large share of the property's value, it is inexpensive insurance on the most valuable thing you own there.",
    ]),
    "what-a-good-month-actually-looks-like": ("Reading someone else's numbers", [
        "When you are shown a short-term rental's performance, whether by a seller, an agent or an online post, the questions that separate a real number from a marketed one are consistent.",
        "Is this gross bookings or net? Which months does it cover? What is the annual figure and how is it distributed across twelve months? What is the full expense stack, including insurance quoted for this address and property tax at the purchase price rather than the seller's assessment? What is in the maintenance and capital reserve? How many bookings does the revenue represent, and what is the turnover cost?",
        "A seller who can answer all of those is a professional operator and the numbers are probably real. One who cannot is quoting gross bookings from a good quarter.",
        "This is exactly why we treat seller proformas as marketing documents and underwrite against actual booked-night data for genuinely comparable inventory instead. It is also why roughly 98% of what we screen does not survive the process.",
    ]),
}
