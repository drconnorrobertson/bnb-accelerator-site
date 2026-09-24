#!/usr/bin/env python3
"""Two distinct STR acquisition checks: ice-dam exposure and water delivery."""

import blog


POSTS = [
    {
        "slug": "ice-dam-risk-before-buying-str",
        "title": "Ice-Dam Risk Before Buying a Short-Term Rental",
        "title_tag": "How to Check Ice-Dam Risk Before Buying an STR | BNB Accelerator",
        "h1": "How do you check ice-dam risk before buying a short-term rental?",
        "description": "Check roof-edge staining, attic heat loss, prior winter leaks, and safe snow management before buying an STR in a freezing climate.",
        "date": "2026-09-24",
        "category": "Acquisition Diligence",
        "lead": "Ask how the roof and attic behave during a freeze-thaw cycle, not just whether the shingles look sound on a clear day. Ice dams can send meltwater beneath roofing and into the building; overhangs and entry routes can also become hazardous for guests. Review winter photos and repair records, inspect accessible attic and roof-edge evidence with qualified professionals, and price both the building remedy and a safe winter operating plan before the diligence deadline.",
        "sections": [
            ("A roof inspection is not a winter-performance history", [
                "An ice dam forms when roof snow melts and refreezes at a colder edge. The <a href=\"https://www.weather.gov/grr/roofIceDams\" rel=\"noopener\">National Weather Service explains</a> that backed-up water can work beneath shingles and damage the attic, ceiling, walls, and contents. A roof can appear dry on a summer showing while a repeated winter leak has been patched indoors. This question is distinct from <a href=\"/blog/roof-age-str-policy-binding/\">roof age and insurance binding</a>: the issue is the roof-and-attic system's behavior in freezing weather and its impact on guest access.",
                ("callout", "Is a winter-market acquisition relying on a roof with unknown freeze-thaw history? <a href=\"/apply/\">Book a BNB Accelerator acquisition call</a> to model the repair scope, winter access plan, and downside case before committing."),
                "Do not treat icicles alone as proof of structural damage, or an absence of icicles on one visit as proof of safety. Ask what happened during prior winters and whether repairs addressed a cause or only a stain."
            ]),
            ("Build a winter evidence file", [
                "Request dated photos of eaves and roof valleys after snow, past leak and insurance records available to the buyer, invoices for roof or attic work, and any recurring roof-raking or heat-cable service records. Ask the seller whether water ever appeared at exterior walls, window heads, ceilings, or light fixtures after thaw. Map the location and date of each reported event rather than accepting 'the roof was repaired' as a complete answer.",
                ("table", ["Check", "Evidence", "Decision it informs"], [
                    ["Exterior", "Eave and valley condition, gutter discharge, ice or staining in winter photos", "Whether a roofer needs to investigate a particular roof edge"],
                    ["Attic", "Accessible insulation, air leaks, ventilation path, damp or stained sheathing", "Whether an envelope specialist should scope air sealing and insulation"],
                    ["Interior", "Prior ceiling or wall staining, repair invoices, moisture findings", "Whether hidden damage needs further inspection"],
                    ["Guest routes", "Entry, parking, steps, and areas below overhangs", "Whether winter operations can keep people away from falling ice"],
                ]),
                "The <a href=\"https://www.energy.gov/sites/default/files/2023-03/insulation_guide_0.pdf\" rel=\"noopener\">U.S. Department of Energy's Building America guidance</a> describes air sealing, insulation, and appropriate roof ventilation as parts of ice-dam prevention for vented attics. It also notes possible water intrusion and falling-icicle hazards. Existing assemblies differ, so do not specify a one-size-fits-all retrofit from an online checklist. Have a roofer and, where needed, an insulation or building-envelope professional inspect the actual assembly."
            ]),
            ("Price the complete cure and operating plan", [
                "Ask the roofer to distinguish current roof damage from conditions that cause repeated melting and refreezing. A quote to replace shingles may not address heat loss below the roof. Conversely, an attic air-sealing proposal may not repair damaged sheathing or interior finishes. Get written scopes, exclusions, permits where relevant, timing, and whether work can be completed before the next season. Ask the insurer how any known prior water damage or planned repair affects the proposed policy; do not assume a particular claim outcome.",
                "Create a separate winter operating plan for snow and ice observations, vendor response, gutters and downspouts, and guest entry. The <a href=\"https://www.weather.gov/grr/roofIceDams\" rel=\"noopener\">National Weather Service advises</a> keeping heavy snow and blocked drainage in view, but roof work can be dangerous. Use trained vendors and avoid asking guests or untrained staff to climb, chip ice, or stand below a suspect overhang. Link this plan to the <a href=\"/blog/snow-removal-cost-str/\">snow-removal cost model</a>, rather than assuming the driveway contract covers the roof.",
                "Illustrative only: a buyer obtains a $12,000 envelope proposal, a $6,000 roofing and finish-repair estimate, and a $4,000 uncertainty reserve. The $22,000 total is a planning case, not a market quote. Add any unavailable nights and ongoing winter service expense separately. If the home is marketed for peak winter stays, a temporary closure can matter more than it would in a slow season; test that with property-specific booking assumptions in the <a href=\"/underwriting/downside-scenario/\">downside model</a>."
            ]),
            ("Proceed, renegotiate, or stop", [
                "Proceed if the problem is scoped, damage is understood, safe guest access is feasible, qualified vendors can complete the work, and the revised acquisition economics still clear the buyer's threshold. Keep all findings and vendor responsibilities in the handoff file.",
                "Renegotiate if documented roof, attic, or finish work changes the capital requirement. Extend diligence or stop if recurring leaks cannot be explained, the roof/attic assembly cannot be assessed within the contingency, or winter access remains unsafe. <a href=\"/apply/\">Book a call to compare a repaired candidate with alternatives</a>. This is educational guidance, not engineering, insurance, legal, tax, or investment advice."
            ]),
        ],
        "faqs": [
            ("Do icicles mean an ice dam has already damaged the house?", "Not necessarily. They justify a closer look at roof-edge, attic, and interior evidence, especially when there is a leak history."),
            ("Will a new roof alone prevent ice dams?", "Not always. The roof covering, attic air leakage, insulation, and ventilation need property-specific assessment."),
            ("Can a regular snow-removal vendor manage roof ice?", "Do not assume so. Confirm the vendor's scope, training, insurance, and safe method; keep guests and untrained staff away from roof work."),
            ("How does ice-dam risk enter underwriting?", "Separate repair capital, uncertainty reserve, recurring winter service, and a plausible lost-night scenario. Do not treat all four as one roofing quote."),
        ],
        "related": [
            '<a href="/blog/roof-age-str-policy-binding/">Roof-age and insurance diligence</a>',
            '<a href="/blog/snow-removal-cost-str/">Snow-removal cost</a>',
            '<a href="/underwriting/downside-scenario/">Downside underwriting</a>',
        ],
        "cta_h": "Underwrite the winter roof, not the sunny showing",
        "cta_p": "We can compare the qualified repair scope and winter guest-access plan with the acquisition's expected return.",
    },
    {
        "slug": "water-pressure-capacity-before-buying-str",
        "title": "Water Pressure and Capacity Before Buying an STR",
        "title_tag": "How to Test STR Water Pressure Before Buying | BNB Accelerator",
        "h1": "Can the water system handle a full STR house?",
        "description": "A single strong shower does not prove full-house capacity. Test simultaneous demand, identify supply limits, and price a property-specific fix before buying.",
        "date": "2026-09-24",
        "category": "Acquisition Diligence",
        "lead": "A quick tap test is not enough for a property marketed to a full group. Ask a qualified plumber to check static and flowing pressure, fixture flow, hot-water delivery, and simultaneous-use performance at the proposed guest capacity. If the property uses a private well, evaluate well yield and recovery separately. Trace any poor result to the supply, pressure equipment, distribution piping, heater, or fixture before budgeting a cure. This is a buyer's capacity decision, not a promise of a universal pressure number.",
        "sections": [
            ("Define the guest-use test before testing", [
                "Write down the occupancy the listing will actually promise and the number of showers, sinks, laundry appliances, dishwashers, and outdoor water features likely to run together. A property with six bedrooms and four bathrooms can pass a one-shower tour yet fail the morning turnover pattern. The <a href=\"/blog/airbnb-guest-experience/\">guest-experience guide</a> notes that water pressure matters to guests; this article is about proving that the property's system can deliver under the intended use before the buyer commits.",
                ("callout", "Does a large-group acquisition depend on showers and laundry running together? <a href=\"/apply/\">Book a BNB Accelerator acquisition call</a> to put water-system capacity into the property screening and repair budget."),
                "Distinguish three questions: is the source supplying enough water, is the plumbing distributing it adequately, and is enough hot water available for the use case? Fixing one does not necessarily fix the others. A pressure gauge reading at one hose bib is useful evidence, not a whole-house performance test."
            ]),
            ("Run a documented, simultaneous-use inspection", [
                "Have the plumber record static pressure with fixtures off and flowing pressure at representative points while agreed combinations of showers, sinks, and appliances run. Record which fixtures were open, for how long, and whether pressure or temperature changed. Check for leaks, restrictive or old piping, partially closed valves, pressure regulators, treatment equipment, and water-heater recovery. Have the inspector explain which parts of the system were inaccessible or outside the inspection scope.",
                ("table", ["Question", "What to document", "Potential next specialist"], [
                    ["Supply and pressure", "Static and flowing readings, location, test conditions, utility or well source", "Plumber; utility or well professional"],
                    ["Distribution", "Which floors or fixtures weaken during simultaneous use, piping and valve observations", "Plumber"],
                    ["Hot water", "Heater type, age, recovery, temperature behavior, proposed simultaneous demand", "Plumber or water-heater specialist"],
                    ["Private well", "Well log, pump and pressure-tank records, sustained yield and recovery test", "Qualified well contractor"],
                ]),
                "The <a href=\"https://www.epa.gov/watersense/home-maintenance\" rel=\"noopener\">EPA describes a basic household pressure-gauge check</a> with other water uses off. That establishes a starting measurement, not the dynamic performance of a full STR. For private wells, the <a href=\"https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=9101D55B.TXT\" rel=\"noopener\">EPA's guidance for real-estate professionals</a> identifies well records, pump and pressure-tank information, and a yield test as relevant purchase diligence."
            ]),
            ("Do not confuse a weak shower with a weak source", [
                "If one fixture is poor while others are fine, investigate its valve, aerator, showerhead, or branch pipe. If several fixtures weaken together, investigate upstream supply and distribution. If cold water remains acceptable while hot water turns lukewarm, investigate heater capacity and recovery. These are diagnostic patterns, not diagnoses; the professional should confirm the cause and written remedy.",
                "A private well introduces a different failure mode: short tests may draw from stored water while sustained demand exceeds well yield or pump capacity. The <a href=\"https://pubs.usgs.gov/gip/gw_ruralhomeowner/gw_ruralhomeowner_new.html\" rel=\"noopener\">U.S. Geological Survey explains</a> that pumping faster than a well's inflow can temporarily exhaust available water until the well recovers. Use a qualified well contractor's sustained test for that question, alongside the <a href=\"/blog/private-well-buying-short-term-rental/\">existing private-well acquisition guide</a>. For municipal supply, ask the utility and plumber about service size, meter, and any known supply limitation instead of assuming the utility side is unlimited."
            ]),
            ("Convert the finding into an acquisition decision", [
                "Obtain a written scope identifying the cause, equipment or pipe work, permit responsibility, wall or floor restoration, and what performance the contractor expects after the repair. Check whether construction would delay the opening date or remove a bathroom from service. Avoid treating a booster pump, larger heater, or new well as a generic line item until a professional confirms suitability and approvals.",
                "Illustrative only: suppose a buyer models $8,000 for plumbing work, $3,000 for opened-wall restoration, and $2,000 as a contingency. That is $13,000 of incremental capital, not an estimated price for a particular system. If a bathroom remains out of service for a launch period, model a realistic lower occupancy or fewer bookable nights separately. Run that case through <a href=\"/underwriting/downside-scenario/\">downside underwriting</a> rather than assuming the full-house revenue forecast is intact.",
                "Proceed if the source and system can support the intended use with a feasible, priced remedy and the revised economics still work. Renegotiate around documented capital and downtime. Extend diligence or stop if a crucial well-yield or utility limitation cannot be resolved before the contingency or if the listing would have to promise a capacity the system cannot deliver. <a href=\"/apply/\">Book a call to compare this property with less constrained options</a>. This guide is educational, not plumbing, water-quality, legal, insurance, tax, or investment advice."
            ]),
        ],
        "faqs": [
            ("Is one strong shower enough to validate a large STR?", "No. Test representative simultaneous demand and hot-water recovery against the occupancy the property will actually advertise."),
            ("Does a pressure-gauge reading prove the whole system is adequate?", "No. Static pressure is one starting measurement. Flowing pressure, distribution, heater performance, and test duration also matter."),
            ("Does a private well need a different test?", "Yes. Ask a qualified well contractor about sustained yield and recovery, and review pump and pressure-tank records; a brief fixture test may not expose a source limit."),
            ("Should I just budget for a booster pump?", "Not before the cause is diagnosed and the professional confirms that the proposed equipment is suitable and allowed."),
        ],
        "related": [
            '<a href="/blog/private-well-buying-short-term-rental/">Private-well acquisition</a>',
            '<a href="/blog/airbnb-guest-experience/">Guest-experience priorities</a>',
            '<a href="/underwriting/downside-scenario/">Downside underwriting</a>',
        ],
        "cta_h": "Test the whole-house water experience",
        "cta_p": "We can compare verified water capacity, repair scope, and launch economics with alternative acquisition candidates.",
    },
]


if __name__ == "__main__":
    blog.build(POSTS)
