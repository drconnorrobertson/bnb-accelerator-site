#!/usr/bin/env python3
"""Generate the radon-testing acquisition guide for STR buyers."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import blog

DATE = "2026-09-24"
SCORE = {
    "distinct_search_intent": 30,
    "buyer_relevance": 23,
    "real_question": 15,
    "service_fit": 12,
    "original_decision_support": 14,
}
assert sum(SCORE.values()) == 94

BUYER_GUIDE = "https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=P1019REH.TXT"
RETEST = "https://www.epa.gov/radon/how-often-should-i-testretest-my-home-radon"
MAP = "https://www.epa.gov/radon/epa-map-radon-zones-and-supplemental-information"
PROS = "https://www.epa.gov/radon/find-radon-test-kit-or-measurement-and-mitigation-professional"
NEW_HOME = "https://www.epa.gov/radon/how-protect-your-family-radon-when-buying-newly-built-home"
REDUCTION = "https://www.epa.gov/sites/default/files/2016-12/documents/2016_consumers_guide_to_radon_reduction.pdf"

POST = {
    "slug": "radon-test-before-buying-str",
    "title": "Radon testing before buying a short-term rental",
    "title_tag": "Should You Test an STR for Radon Before Buying?",
    "h1": "Should you test a short-term rental for radon before buying it?",
    "description": "Buying an Airbnb or vacation rental? Use this radon-testing framework for test location, closed-house conditions, mitigation bids, and STR operations.",
    "date": DATE,
    "category": "Acquisition Diligence",
    "lead": "Yes. Test the property for radon during acquisition diligence, even when the county is mapped as lower potential, the seller has an older result, or the home is newly built. For a short-term rental, the test must reflect the lowest level guests or staff could use regularly—not only the seller's current living pattern. A valid result then becomes a property decision: accept it, retest under a defensible protocol, price mitigation, redesign the guest layout, or walk away. It should not be reduced to a generic home-inspection checkbox.",
    "sections": [
        ("The direct answer for an STR buyer", [
            f"EPA's revised <a href=\"{BUYER_GUIDE}\" rel=\"noopener\">Home Buyer's and Seller's Guide to Radon</a> recommends testing when buying or selling a home and fixing the home when the radon level is 4 picocuries per liter (pCi/L) or higher. EPA also says levels below 4 pCi/L still pose some risk and may be reduced. The only way to know the level in a specific property is to test it.",
            "The STR operating plan changes how the buyer uses that guidance. A basement that the seller treats as storage may become a game room, bunk room, gym, office, or staff workspace. The test location, renovation scope, HVAC plan, booking calendar, mitigation-system handoff, and retest schedule should follow that future use. If the team tests only the seller's main floor, it may answer the wrong property question.",
            ("callout", "Evaluating a basement-heavy cabin, older home, or conversion opportunity? <a href=\"/apply/\">Apply for a BNB Accelerator strategy call</a> to pressure-test the acquisition, layout, opening plan, and reserves. Qualified radon professionals and local authorities should set the testing and mitigation requirements."),
        ]),
        ("Use this six-step acquisition decision tree", [
            ("table", ["Step", "Question", "Evidence"], [
                ["1. Future use", "What is the lowest level that could be used regularly?", "Proposed floor plan, sleeping areas, amenities, office, laundry, and staff tasks."],
                ["2. Prior result", "Is an existing test recent, correctly located, and protocol-compliant?", "Full report, device, dates, conditions, tester, interference controls, and renovations since."],
                ["3. New test", "Which real-estate testing option fits the deadline?", "Qualified tester, device, location, minimum duration, and closed-house instructions."],
                ["4. Interpretation", "What decision follows from the result and uncertainty?", "EPA guidance, state rules, proximity to 4 pCi/L, and seasonal limitations."],
                ["5. Mitigation", "Can the property be reduced reliably without harming the STR plan?", "Qualified bids, routing, discharge, electrical work, permits, noise, aesthetics, and retest."],
                ["6. Operations", "Who keeps the system working after launch?", "Gauge or alarm check, outage response, maintenance, records, and recurring retest owner."],
            ]),
            "Do not jump from a single number to a purchase decision. First verify that the number answers the intended-use question and came from a valid test. Then translate it into a scoped mitigation and operating plan. A property with an elevated result can remain viable when the system, cost, schedule, and ongoing controls are documented; a low-looking but invalid test should not receive more weight than the evidence supports.",
        ]),
        ("Test the future guest footprint, not the seller's habits", [
            "EPA tells buyers to test the lowest level that could be used regularly. That may be the lowest level currently occupied, or a lower level a buyer might use as a family room or play area. For an STR, write the intended use beside every lower-level room before selecting the location.",
            ("ul", [
                "A finished basement marketed as a game room or theater is a regular-use area even if no bed is shown.",
                "A lower-level bunk room or bedroom conversion raises both the testing and legal-occupancy questions; radon testing does not validate the room as sleeping space.",
                "A laundry, maintenance shop, or housekeeping room may create recurring worker exposure even if guests rarely enter.",
                "A walkout level with its own HVAC zone can behave differently from the seller's main-floor test location.",
                "A crawlspace is not automatically the measurement location, but its construction and condition can affect mitigation design; let the qualified tester evaluate the building.",
            ]),
            "Keep the radon location decision connected to the <a href=\"/design/\">design plan</a>. If the use changes after closing, retest at the relevant level instead of assuming the acquisition result covers a new layout.",
        ]),
        ("When can you rely on the seller's radon report?", [
            f"EPA's <a href=\"{RETEST}\" rel=\"noopener\">retesting guidance</a> says a buyer may want a new test when the prior checklist was not followed, the result is not recent—for example, within two years—the home has been renovated or altered, or the buyer plans to use a lower level than the one tested. Those are especially common in an STR acquisition.",
            ("ol", [
                "Obtain the complete laboratory or monitor report rather than a number copied into a disclosure form.",
                "Confirm the test location and height, device type, start and stop time, and whether the device met its minimum exposure period.",
                "Check closed-house conditions, HVAC operation, weather notes, occupancy, and evidence of interference prevention or detection.",
                "Verify whether a mitigation system was operating during the test and obtain its installation and maintenance records.",
                "Compare the date with later foundation work, additions, window or HVAC changes, weatherization, basement finishing, or altered use.",
                "Ask the qualified tester whether state or transaction rules require a different protocol or credential.",
            ]),
            "A seller's valid report can be useful evidence, but the buyer's plan still controls relevance. If the seller tested an upstairs living room and the STR thesis depends on a finished walkout basement, commission a new test in the proper location.",
        ]),
        ("How to run a short-term test during a transaction", [
            "EPA describes short-term devices that remain in the home from two to 90 days, depending on the device, and long-term tests that run more than 90 days. Long-term testing better represents the year-round average, but a transaction often requires a shorter decision window. All radon tests should run for at least 48 hours, and some devices require longer.",
            "For a real-estate decision, EPA lists three short-term options: two passive tests run simultaneously for at least 48 hours; two identical passive tests run sequentially in the same location; or one continuous monitor for at least 48 hours. The guide recommends fixing when the applicable average or monitor result is 4 pCi/L or more. The closer a short-term result is to 4, the more uncertainty exists about the year-round average.",
            "For a test shorter than four days, windows and exterior doors should be closed at least 12 hours before testing and remain closed except for normal entry and exit. Heating and cooling should operate normally; device placement, high winds or storms, humidity, drafts, and interference can affect validity. A vacant property is not a shortcut if contractors, cleaners, agents, or seller activity break the protocol.",
            ("warn", "Use a qualified measurement professional for transaction decisions, particularly when the property is occupied, access is uncontrolled, the deadline is short, or state rules apply. Write access and closed-house instructions into the inspection schedule before placing the device."),
        ]),
        ("The county radon map cannot clear an address", [
            f"EPA's <a href=\"{MAP}\" rel=\"noopener\">Map of Radon Zones</a> is a planning tool based on broad factors such as measurements, geology, radioactivity, soils, and foundation types. EPA explicitly says the map should not determine whether an individual home needs testing and that homes with elevated levels exist in all three zones.",
            "Market selection and property testing answer different questions. A zone map may help a team anticipate common building practices or available providers, but it cannot replace a measurement at the actual property. Likewise, a neighboring home's result does not establish this home's level; foundations, pathways, pressure, construction, ventilation, and operation differ.",
            "New construction is not exempt from the decision. EPA recommends asking whether radon-resistant construction features were used and whether the finished home was tested. Passive features are not proof of a low indoor measurement, and some systems may need an in-line fan if testing shows an elevated result.",
        ]),
        ("Worked example: a lower-level game room", [
            "Assume an illustrative buyer is evaluating a mountain cabin with a main floor and finished walkout basement. The seller provides a three-year-old 2.1 pCi/L result from an upstairs bedroom. The buyer's STR plan puts a game room, television area, and laundry in the basement and does not add a legal bedroom. The inspection deadline is ten days away.",
            "The prior result is not enough for this decision: it is older, comes from the wrong level, and predates the buyer's regular-use plan. The buyer hires a qualified tester, secures access and closed-house conditions, and runs an appropriate real-estate test in the lowest level that could be used regularly. Assume the illustrative continuous monitor reports 5.2 pCi/L under valid conditions.",
            "Because the result is at or above EPA's 4 pCi/L action level, the buyer gets qualified mitigation bids before the deadline. The bids must show system type and routing, fan and electrical work, discharge location, permits, installation timing, post-mitigation testing, warranty, noise and appearance effects, and operating instructions. The buyer adds the selected scope and a schedule contingency to underwriting instead of applying an invented national allowance.",
            "The 2.1 and 5.2 pCi/L results, dates, layout, and deadline are illustrative, not a report of a BNB Accelerator property. A qualified professional should select the protocol and interpret the actual conditions under applicable state and local requirements.",
        ]),
        ("Turn an elevated result into a bid you can underwrite", [
            f"Use EPA's <a href=\"{PROS}\" rel=\"noopener\">radon professional locator guidance</a> and the state radon program to identify credential and licensing requirements. Ask more than one qualified mitigator for a property-specific scope. The cheapest pipe-and-fan number is not necessarily the complete launch cost.",
            ("ul", [
                "System design: foundation type, suction points, sealing, fan, electrical feed, vent route, discharge clearances, labels, and warning device.",
                "STR fit: exterior appearance, fan location and noise, guest-access protection, owner closets, deck or window conflicts, and listing-photo implications.",
                "Project dependencies: permits, electrician, roofer or siding work, crawlspace membrane, moisture issues, and access before furniture installation.",
                "Proof: installation record, warranty, operating instructions, labeled system, post-mitigation test, and independent measurement where appropriate.",
                "Operations: continuous power, periodic warning-device check, contact for service, fan replacement reserve, and retest calendar.",
            ]),
            "Model the bid as property infrastructure, not a one-time concession. Include the initial system, related trades, test and retest, schedule impact, ongoing electricity and maintenance, and eventual fan replacement. Do not invent a universal mitigation price; foundation design and project constraints drive the property-specific quote.",
        ]),
        ("Post-mitigation testing and STR operations", [
            f"EPA's <a href=\"{REDUCTION}\" rel=\"noopener\">Consumer's Guide to Radon Reduction</a> recommends a post-mitigation test within 30 days after installation, but no sooner than 24 hours after an active system begins operating. It also recommends considering an independent follow-up measurement, checking the warning device regularly, never turning off an active system fan, and retesting at least every two years.",
            "Translate that into the management system. Add the gauge or alarm to the property inspection checklist, photograph the normal reading at handoff, label the breaker, keep the fan powered during guest stays and turnovers, and define what cleaners or managers do if the warning device changes. A working system should not depend on the owner remembering it from another state.",
            "Retest when the lower-level use changes or the home is renovated or altered in a way that could affect radon conditions. Preserve acquisition, post-mitigation, recurring, and post-renovation reports in one property file. If local law or professional guidance calls for a different interval or response, follow the applicable standard.",
        ]),
        ("Failure modes and the go/no-go decision", [
            ("ul", [
                "Skipping testing because the property sits in an EPA Zone 2 or Zone 3 county, is new, or a nearby house tested low.",
                "Accepting a seller's isolated number without the report, location, protocol, conditions, test date, or renovation history.",
                "Testing the seller's occupied floor while the STR plan puts guests or workers on a lower level.",
                "Allowing cleaners, contractors, open windows, storms, or device movement to invalidate a rushed transaction test.",
                "Treating a result near 4 pCi/L as perfectly precise or treating 3.9 as risk-free and 4.0 as a fundamentally different building.",
                "Negotiating a credit without obtaining a buildable mitigation design, related-trade scope, post-mitigation test, and operating handoff.",
                "Installing a system, turning it off between bookings, and never checking the warning device or retesting after renovation.",
            ]),
            ("warn", "Health and legal boundary: this guide summarizes EPA materials reviewed September 24, 2026. It is educational, not medical, environmental, engineering, inspection, legal, insurance, or investment advice. State and local requirements vary. Use qualified radon measurement and mitigation professionals and the applicable authorities."),
            "Before the inspection contingency ends, require a valid result for the future guest footprint, a written interpretation under the applicable protocol, and a mitigation bid when the result or uncertainty warrants one. Put the complete response into the <a href=\"/underwriting/\">underwriting</a>, renovation schedule, and management handoff. Pair it with the <a href=\"/blog/inspection-contingency-length-str/\">inspection-contingency guide</a> and the <a href=\"/blog/certificate-of-occupancy-str-remodel/\">remodel occupancy guide</a>. Proceed, renegotiate, redesign, or walk away from a documented property decision—not a county color or an unsupported seller claim.",
        ]),
    ],
    "faqs": [
        ("Should every STR buyer test for radon?", "EPA recommends testing when buying or selling a home, and its zone map should not be used to clear an individual address. The test should reflect the property's future regular-use areas."),
        ("Where should a radon test be placed in a vacation rental?", "EPA says to test the lowest level that could be used regularly. For an STR, that can include a proposed basement game room, bunk area, office, or recurring staff workspace even if the seller does not use it that way."),
        ("What radon level should trigger mitigation?", "EPA recommends fixing a home at 4 pCi/L or higher and says lower levels still carry risk and may be reduced. Results close to 4 require careful interpretation because short-term tests have uncertainty."),
        ("Can a buyer rely on the seller's old radon test?", "Only after verifying the full report, protocol, location, conditions, age, tester, mitigation status, and changes since testing. EPA notes buyers may want a new test after alterations, when results are not recent, or when a lower level will be used."),
        ("Does a radon mitigation system need ongoing attention?", "Yes. EPA recommends checking the warning device, keeping an active fan running continuously, completing post-mitigation testing, maintaining the system, and retesting at least every two years."),
    ],
    "related": [
        '<a href="/blog/inspection-contingency-length-str/">Set the inspection-contingency timeline</a>',
        '<a href="/blog/certificate-of-occupancy-str-remodel/">Verify remodel and occupancy impacts</a>',
        '<a href="/design/">Plan lower-level guest spaces</a>',
        '<a href="/underwriting/">Model the acquisition and mitigation scope</a>',
        '<a href="/partners/">Coordinate with qualified specialists</a>',
    ],
    "cta_h": "Buying an STR with a basement or uncertain test history?",
    "cta_p": "BNB Accelerator can help source and underwrite the property, align the guest plan with diligence, and coordinate the acquisition file while qualified radon professionals handle testing and mitigation.",
}


if __name__ == "__main__":
    blog.build([POST])
    print(f"candidate score: {sum(SCORE.values())}/100 — {SCORE}")
