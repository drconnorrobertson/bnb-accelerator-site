#!/usr/bin/env python3
"""Airport-noise decision support for prospective STR buyers."""

import blog


POSTS = [{
    "slug": "airport-noise-before-buying-short-term-rental",
    "title": "Airport Noise Before Buying a Short-Term Rental",
    "title_tag": "Airport Noise Before Buying an STR | BNB Accelerator",
    "h1": "How do you check flight noise before buying a short-term rental?",
    "description": "Use airport noise maps, timed site visits, comparable reviews, and a guest-use test to price aircraft noise before buying a short-term rental.",
    "date": "2026-09-24",
    "category": "Market & Property Selection",
    "lead": "A home near an airport can offer convenient access and still be a poor fit for a quiet-cabin or outdoor-entertaining rental. Before buying, locate the property against the airport's current noise and land-use material, then visit during the hours guests will use bedrooms, patios, and pools. Review comparable guest feedback and test the revenue case at a conservative rate. Distance from the terminal and a seller's claim that flights are 'rarely noticed' are weak substitutes for address-level evidence.",
    "sections": [
        ("The direct answer", [
            "Use three lenses: the airport's published planning data, the sound and frequency experienced at the property, and how that exposure affects the guest promise. The <a href=\"https://www.faa.gov/airports/environmental/airport_noise/noise_exposure_maps\" rel=\"noopener\">Federal Aviation Administration lists airport noise exposure maps</a> prepared under Part 150, but these are voluntary and not every airport has one. A map is a screening tool, not a guarantee that guests will find the yard quiet on a particular evening. Record its date and whether it depicts existing or forecast operations.",
            ("callout", "Considering an STR near an airport, training field, or flight corridor? <a href=\"/apply/\">Ask BNB Accelerator to test the property's guest fit and downside revenue case</a> during the acquisition review. The buyer and local specialists should verify current airport activity, property conditions, and any applicable land-use restrictions."),
            "This is a different question from <a href=\"/blog/airbnb-neighbors-and-noise/\">guest-generated noise and neighbors</a>. Here the exposure comes from outside the operator's control. A noise monitor and house rules cannot change aircraft operations."
        ]),
        ("Read the map correctly", [
            "Find the airport sponsor's current Part 150 noise exposure map, airport master plan or environmental review, and any local airport land-use compatibility map. Ask the airport's noise or planning office which document is current and what changes are planned. The <a href=\"https://www.faa.gov/airports/environmental/land_use\" rel=\"noopener\">FAA's land-use guidance</a> emphasizes that compatibility is a planning issue shared by airports and local governments; zoning or disclosures may therefore be local.",
            "The FAA's primary planning measure is a day-night average sound level over a long period, with nighttime weighting. It can describe cumulative exposure and land-use compatibility, but it is not a count of audible flyovers in a guest's two-hour patio dinner. The <a href=\"https://www.faa.gov/regulations_policies/policy_guidance/noise/basics\" rel=\"noopener\">FAA's explanation of the DNL metric</a> is useful for interpreting the map. Being outside a 65-DNL contour does not mean a guest will never hear aircraft; being inside one does not quantify a specific property's nightly rate loss.",
            ("ol", [
                "Place the address, not just the neighborhood name, on the latest available map and note the map's issue and forecast dates.",
                "Ask whether runway use, cargo operations, training flights, or proposed changes make current and future patterns materially different.",
                "Check whether the local government records an airport influence area, disclosure, easement, or land-use restriction affecting the parcel.",
                "Do not draw a flight path from a single day's tracking app and treat it as a permanent schedule."
            ])
        ]),
        ("Visit like a guest, not an appraiser", [
            "Visit at breakfast, evening outdoor-use hours, and overnight if practical. Repeat on a weekday and a weekend, and ask the airport whether season or runway configuration changes the pattern. Record the exact time, weather, windows open or closed, where you stood, audible events, and whether ordinary conversation or sleep would be affected. A single visit can miss a runway rotation or busy departure bank. A phone sound-meter app can help compare rooms, but without calibration and a defined measurement protocol it is not a legal or scientific noise study.",
            ("table", ["Guest use", "Field question", "Possible deal effect"], [
                ["Bedroom", "Can a light sleeper rest with windows in their normal position?", "Window, insulation, cooling, and disclosure decisions"],
                ["Patio or pool", "Can guests converse during the hours featured in the listing?", "Amenity appeal and rate support"],
                ["Remote work", "Will calls be interrupted in the advertised workspace?", "Loss of a target guest segment"],
                ["Arrival", "Does airport convenience meaningfully help the same guests?", "A location benefit that may offset, but not erase, noise risk"],
            ]),
            "Read recent reviews from genuinely comparable nearby listings for repeated mentions of planes, sleep, outdoor noise, or surprisingly quiet interiors. A review is anecdotal; look for patterns across properties and dates. If all comparable operators mention soundproofing or close outdoor spaces early, treat that as a clue for inspection, not as proof of a particular discount."
        ]),
        ("Price the guest promise honestly", [
            "An airport-adjacent property may work for quick weekend stays, business travelers, or groups that value transport access. The same exposure can undermine a premium retreat positioned around silence, nature, or uninterrupted outdoor meals. Separate the location benefit from the noise penalty in the comparable set. Do not use a lake cabin's rate for a property whose main outdoor amenity is under a departure path without direct evidence that guests accept it.",
            "Illustrative only: the seller projects 180 booked nights at $350, or $63,000 gross. A conservative buyer case tests 165 nights at $325, or $53,625 gross. The $9,375 difference is not an estimate of an airport's impact; it is a sensitivity to ask whether the investment still works if the guest promise must be priced more modestly. Replace both rates and occupancy assumptions with date-level comparable evidence and a property-specific projection. The <a href=\"/revenue-projections/\">projection guide</a> shows how to build that case.",
            "Consider what mitigation costs: qualified window and insulation work, HVAC allowing windows to stay closed, outdoor screening, and honest listing copy. Some measures may make the interior usable without changing patio exposure. Have a contractor price them before treating a lower purchase price as sufficient. Never promise 'no airport noise' if the field test contradicts it."
        ]),
        ("Proceed, renegotiate, or reject", [
            "Proceed when the map and airport plans are understood, site visits cover the relevant guest periods, comparable reviews support the proposed positioning, and the downside return still clears the buyer's threshold. Keep the dated map, visit log, photos, comparable notes, and revised underwriting with the deal file.",
            "Renegotiate when a specific mitigation scope or rate adjustment has a defensible cost. If the seller describes the property as quiet, write the buyer's observed condition into the negotiation rather than debating a subjective adjective. Review any recorded airport easement or disclosure with local counsel.",
            "Decline when the property's central guest promise depends on quiet the location cannot deliver, future airport plans create an exposure outside the buyer's tolerance, or the conservative rate and occupancy fail the required return. Use the <a href=\"/underwriting/downside-scenario/\">downside model</a> and <a href=\"/apply/\">book an acquisition call</a> if you want to compare this address with quieter alternatives. This is an educational framework, not acoustical, legal, lending, insurance, tax, or investment advice."
        ]),
    ],
    "faqs": [
        ("Does being outside an FAA 65-DNL contour mean an STR is quiet?", "No. A planning contour is an average exposure measure, not a guarantee about individual flyovers or guest experience at a particular hour."),
        ("Do all airports have a Part 150 noise exposure map?", "No. Airports prepare these maps voluntarily. Ask the airport sponsor for its most current noise, master-plan, or environmental material."),
        ("Is a single property visit enough?", "Usually not if noise is material to the guest promise. Visit at the likely guest-use times and ask about runway, seasonal, or operational variation."),
        ("How should a buyer price airport noise?", "Use comparable booking and review evidence, a conservative property-specific revenue case, and written mitigation bids. There is no universal percentage discount."),
    ],
    "related": [
        '<a href="/revenue-projections/">Build a revenue projection</a>',
        '<a href="/blog/airbnb-neighbors-and-noise/">Manage guest noise</a>',
        '<a href="/underwriting/downside-scenario/">Stress the downside case</a>',
        '<a href="/apply/">Discuss a property</a>',
    ],
    "cta_h": "Test the sound before buying the location",
    "cta_p": "We can connect the airport exposure, guest positioning, and revenue sensitivity in the acquisition review.",
}]


if __name__ == "__main__":
    blog.build(POSTS)
