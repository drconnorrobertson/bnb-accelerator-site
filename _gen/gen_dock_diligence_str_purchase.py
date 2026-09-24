#!/usr/bin/env python3
"""Generate the dock-permit and inspection guide for STR buyers."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import blog

DATE = "2026-09-24"
SCORE = {
    "distinct_search_intent": 29,
    "buyer_relevance": 23,
    "real_question": 15,
    "service_fit": 14,
    "original_decision_support": 15,
}
assert sum(SCORE.values()) == 96

USACE_PERMITS = "https://www.poa.usace.army.mil/Missions/Regulatory/Do-I-Need-A-Permit/"
USACE_APPLY = "https://www.nwp.usace.army.mil/Missions/Regulatory/Apply/"
TVA_FAQ = "https://www.tva.com/environment/shoreline-construction-permits/shoreline-construction-faq"
FERC_FAQ = "https://www.ferc.gov/about/what-ferc/frequently-asked-questions-faqs/hydropower-frequently-asked-questions-faqs"
CPSC_SHOCK = "https://www.cpsc.gov/s3fs-public/WaysToProtectYourselfAndOthersFromShockOrElectrocutionuUpdated07312019.pdf"

POST = {
    "slug": "dock-permit-inspection-before-buying-waterfront-str",
    "title": "Dock permits and inspections before buying a waterfront STR",
    "title_tag": "Dock Permit and Inspection Before Buying an STR",
    "h1": "How should you verify a dock before buying a waterfront STR?",
    "description": "Buying a waterfront Airbnb? Verify dock rights, permits, transfer rules, compliance, structure, electrical safety, water access, insurance, and repairs.",
    "date": DATE,
    "category": "Acquisition Diligence",
    "lead": "Verify a waterfront dock as three separate assets before closing: the legal right to reach and occupy the shoreline, the permits or licenses authorizing the built facility, and the physical dock system guests will use. Reconcile the deed, survey, shoreline authority file, association documents, permit drawings, and current construction; commission qualified structural and electrical inspections; confirm water depth and level variability, access, shared-use rules, insurance, and repair authority; then price every correction and operating limitation. A dock in listing photographs is not proof that it conveys, transfers, complies, remains usable, or is safe for STR guests.",
    "sections": [
        ("The direct answer for a waterfront STR buyer", [
            "Do not assign revenue or amenity value to a dock until the buyer has evidence of the relevant land or access rights, permit status, transfer or reissuance path, as-built match, physical condition, electrical status, water access, and lawful intended use. The controlling entity may be a city, county, state agency, federal agency, tribal authority, lake association, homeowners association, utility, hydropower licensee, landowner, or several of them. Approval by one does not replace the others.",
            f"The U.S. Army Corps of Engineers explains that docks, piers, ramps, and shoreline stabilization are examples of work that can require authorization under federal <a href=\"{USACE_PERMITS}\" rel=\"noopener\">Section 10 or Section 404 permitting</a>, depending on the water and activity. Federal jurisdiction is only one layer. State water-quality, submerged-land, coastal, environmental, local building, floodplain, electrical, septic, association, and project-specific shoreline rules may also apply.",
            ("callout", "Evaluating a lake house, river property, coastal home, shared dock, or private marina slip? <a href=\"/apply/\">Apply for a BNB Accelerator strategy call</a> to connect waterfront diligence with the offer, insurance, reserves, guest capacity, and launch plan. Qualified local legal, title, survey, marine, structural, electrical, environmental, insurance, lending, and permitting professionals must make their respective conclusions."),
        ]),
        ("Start with rights before inspecting boards and pilings", [
            "A buyer can own the upland home without owning the submerged land, dock footprint, access strip, or exclusive water right implied by the listing. Request the deed, title commitment, survey, plat, easements, riparian or littoral-right analysis, submerged-land lease, shoreline license, association declaration, slip assignment, marina agreement, and every permit or approval. Local counsel and title professionals must determine what conveys and what can be insured.",
            ("table", ["Right or interest", "Evidence to examine", "Failure mode"], [
                ["Shoreline access", "Deed, survey, recorded easement, project boundary, access path and gate rights.", "House conveys but lawful route to the dock does not."],
                ["Dock footprint", "Submerged-land right, lease, license, permit, approved plan, coordinates or survey.", "Structure occupies public, utility, association, or neighboring area without current authority."],
                ["Exclusive or shared use", "Declaration, allocation, slip number, bylaws, rules, reservation or rental restrictions.", "Buyer receives shared access or a different slip than marketed."],
                ["Boat and water access", "Navigation rights, channel, dredging authority, depth records, level policy, launch access.", "Dock exists but intended boat cannot reliably reach it."],
                ["Repair and replacement", "Permit conditions, association approval, access rights, contractor staging and neighboring consent.", "Buyer can use the dock but cannot lawfully rebuild or reach it with equipment."],
                ["Commercial or rental use", "Permit terms, shoreline plan, association rules, marina contract, local STR and business rules.", "Private residential authorization does not support paid guest, event, watercraft, or commercial activity."],
            ]),
            "Treat marketing language such as deeded dock, dock rights, community marina, transferable permit, private cove, deep water, or grandfathered structure as a claim to verify. Each phrase can mean something different under the controlling documents.",
        ]),
        ("Identify every permitting authority and current file", [
            f"Federal, state, local, association, and reservoir authorities can overlap. The Corps' <a href=\"{USACE_APPLY}\" rel=\"noopener\">regulatory permit guidance</a> distinguishes Section 10 work affecting navigable waters from Section 404 discharges of dredged or fill material and notes that maintenance or replacement of piers, floats, and mooring structures can require authorization. The buyer should contact the correct district and local agencies rather than assuming an old structure is exempt.",
            f"Hydropower reservoirs add another layer. FERC explains that a project licensee may implement a <a href=\"{FERC_FAQ}\" rel=\"noopener\">shoreline management plan</a> controlling structures such as private docks, marinas, erosion-control works, utilities, roads, and dredging within the project boundary. FERC also notes that a project boundary does not itself change private property rights. The permit file and the title file answer related but different questions.",
            ("ol", [
                "Identify the waterbody, shoreline owner, submerged-land owner, project or reservoir operator, federal district, state agencies, local jurisdiction, association, and marina or dock manager.",
                "Request the complete permit or license, approved drawings, amendments, conditions, inspection records, correspondence, violations, fees, renewal dates, and transfer procedure.",
                "Compare the permit holder, upland parcel, dock ID, location, dimensions, slips, roof, lifts, utilities, shore connection, stabilization, dredging, and vegetation work with current conditions.",
                "Ask each relevant authority in writing whether the file is current, transferable or reissued on sale, compliant, and sufficient for the buyer's intended use and planned work.",
                "Calendar application, notice, inspection, correction, transfer, renewal, seasonal-work, environmental, and closing deadlines separately.",
            ]),
        ]),
        ("A permit may not transfer automatically", [
            f"TVA's current <a href=\"{TVA_FAQ}\" rel=\"noopener\">shoreline-permit FAQ</a> provides a useful example: Section 26a permits do not automatically transfer when the permit holder sells the property; a new owner must apply for the existing facilities, and transfer treatment depends on prior approval and the facility matching that approval. TVA says ownership changes require notice within its stated period. That rule is specific to TVA—not a national rule—but it shows why buyers must obtain the exact authority's current process before closing.",
            ("table", ["Permit status", "Buyer question", "Decision response"], [
                ["Current and as-built compliant", "What transfer, reissue, fee, inspection, insurance, and timing remain?", "Make completion evidence and post-close deadlines explicit."],
                ["Permit exists; dock differs", "Can the deviation be corrected, approved, reduced, or removed?", "Obtain authority direction and complete technical scope before pricing."],
                ["Permit expired or holder wrong", "Is renewal or new application available, and can buyer rely before ownership?", "Preserve contingency; do not assign dock value to an uncertain path."],
                ["No permit located", "Was authorization required, and what records or enforcement apply?", "Use authority and counsel; a seller affidavit is not agency approval."],
                ["Grandfathered claim", "Which written provision protects which exact structure and use?", "Require the governing document and as-built match."],
                ["Use condition conflicts with STR plan", "Are guests, rentals, events, boats, lifts, lighting, roofs, or commercial use restricted?", "Redesign operations, obtain approval, reprice, or terminate."],
            ]),
            "Do not make closing contingent only on the seller submitting an application. Define the required authority response, compliant configuration, final inspection, transfer or issuance, acceptable conditions, timing, cost responsibility, and remedy if the result differs.",
        ]),
        ("Commission separate structural, marine, and electrical scopes", [
            "A general home inspection rarely evaluates every dock component, underwater support, anchorage, shore connection, lift, electrical system, or wave and water-level exposure. Define the property-specific team. It may include a marine contractor or engineer, structural engineer, licensed electrician with waterfront experience, surveyor, diver, shoreline specialist, and environmental professional.",
            ("table", ["System", "Inspection questions", "Typical evidence"], [
                ["Pilings, crib, anchors and underwater support", "Movement, damage, embedment or attachment, corrosion, decay, scour, impact, load path.", "Above- and below-water observations, measurements, photographs, professional conclusions and limitations."],
                ["Framing, decking, roof and rails", "Decay, corrosion, connections, uplift, lateral loading, guard conditions, trip and fall hazards, rated loads.", "Component map, repair priority, design or permit need, completion standard."],
                ["Gangway, hinges, floats and shore connection", "Range of motion, slope, flotation, freeboard, wear, pinch points, seasonal level and accessibility.", "Operational test under observed level plus stated unobserved conditions."],
                ["Lifts and mechanical equipment", "Ownership, capacity, structure, cables, controls, guarding, service history, parts and permits.", "Equipment IDs, qualified service report, load and operating limits."],
                ["Electrical", "Feed, disconnects, grounding and bonding, protective devices, wiring methods, lights, receptacles, pumps and lifts.", "Licensed waterfront-electrical inspection, test results, panel and circuit mapping, corrections."],
                ["Shoreline and stabilization", "Erosion, scour, wall, bulkhead, riprap, drainage, vegetation, access and environmental approvals.", "Survey and professional scope coordinated with authorities."],
            ]),
            "Ask every inspector to state what was visible, accessed, tested, submerged, loaded, operated, or excluded; the water level and weather; assumptions; required further work; and whether the opinion supports continued use, repair, alteration, or replacement. A calm-water visual visit is not a storm, ice, flood, drawdown, freeze, wake, or high-occupancy test.",
        ]),
        ("Treat dock electricity as a stop-use issue until verified", [
            "Electricity near water can create electrocution risk without an obvious warning. Do not let guests swim from, touch, or use powered dock equipment when electrical condition is unknown or a qualified professional identifies a concern. Never ask a manager, cleaner, guest, seller, or marine contractor to improvise electrical testing outside their license and safe procedure.",
            f"CPSC's <a href=\"{CPSC_SHOCK}\" rel=\"noopener\">shock and electrocution guidance</a> stresses protective devices, labeled power controls, and avoiding electrical products or wires while wet or in contact with wet surfaces. A dock inspection must apply the current locally adopted requirements and actual installation; a household receptacle check or visual presence of a protective device does not establish the complete waterfront system's condition.",
            ("ul", [
                "Identify every source feeding the dock, including house, subpanel, generator, solar, battery, marina, neighboring or shared service, temporary cords, and abandoned wiring.",
                "Map disconnects and circuits for receptacles, lights, pumps, lifts, deicers, chargers, appliances, sound, cameras, gates, and shore-power equipment.",
                "Require qualified testing and documentation of the applicable protective, grounding, bonding, wiring, enclosure, corrosion, and disconnect requirements.",
                "Create a lockout and reopening process after flooding, submersion, impact, lightning, storm damage, tripped protection, tingling reports, wiring alterations, or equipment replacement.",
                "Keep swimming, floating, paddling, fishing, and boat activity outside any restricted zone defined by authorities and qualified professionals.",
            ]),
        ]),
        ("Verify water access across seasons and operating conditions", [
            "A dock can be permitted and structurally sound yet fail the guest promise because of shallow water, drawdowns, sediment, vegetation, tides, currents, wakes, ice, flood debris, drought, navigation restrictions, or inaccessible launch points. Obtain current authority data and property-specific observations rather than relying on one water-level reading or seller photograph.",
            ("ol", [
                "Identify the governing elevation or datum and record observed water depth at a known date, location, and reference—not an unlabeled number.",
                "Review available historical operating ranges, seasonal drawdown, tides, drought, flood, storm, sediment, dredging, ice, wake, and navigation information from responsible authorities.",
                "Match the intended boats and activities to lawful depth, clearance, channel, launch, bridge, current, speed, no-wake, and seasonal restrictions using qualified sources.",
                "Confirm who may dredge, remove vegetation, stabilize the bank, repair access, or alter the bottom—and which permits, disposal, testing, and environmental reviews apply.",
                "Write the listing promise conservatively: dock access does not automatically mean year-round swimming, deep water, boat launching, every watercraft, or unrestricted guest use.",
            ]),
            "Do not underwrite dredging or stabilization from a per-foot contractor quote before authority, environmental, access, material-disposal, design, testing, timing, and maintenance requirements are defined. A technically possible project may still be unavailable to the buyer.",
        ]),
        ("Worked example: a lake house marketed with a two-slip dock", [
            "Assume an illustrative buyer is evaluating a lake house marketed with a private two-slip covered dock and lift. The title includes the upland parcel, but the dock sits within a utility-managed reservoir boundary. The seller provides an old permit card and says the dock is grandfathered. The buyer plans to include kayaks, allow guest swimming, and add lighting and a second lift.",
            "The authority file shows one uncovered slip and a smaller platform approved to a prior owner. The current roof, storage area, wiring, and second slip do not match the drawing. A marine inspection identifies repairable connections but excludes underwater supports; the electrician requires the dock to remain unpowered until corrections and testing are complete. Seasonal records show water at the platform varies enough to affect the buyer's intended boat.",
            "The buyer pauses all dock revenue assumptions. Counsel and the title professional clarify shoreline and access rights; the authority explains the transfer and correction path; qualified professionals define underwater, structural, and electrical scopes; the insurer and lender review the final configuration. The model separates permit uncertainty, removal or correction, repairs, electrical work, water-use limits, and lost amenity time. Every fact and finding is illustrative—not a client result, permit interpretation, inspection, or forecast.",
        ]),
        ("Put the complete dock exposure into underwriting", [
            "Price professional review, surveys, underwater work, transfer and permit fees, design, structural repairs, pilings or anchors, decking, rails, roof, floats, gangway, lifts, electrical corrections, shoreline stabilization, dredging, environmental compliance, access, cranes or barges, debris and disposal, winterization, inspections, insurance, association charges, routine maintenance, storm removal, replacement, and amenity downtime.",
            ("table", ["Scenario", "Model treatment", "Decision trigger"], [
                ["Permitted and usable", "Documented transfer, immediate work, recurring service, insurance and replacement reserve.", "Authority, inspection, title and operating conclusions align."],
                ["Dock usable with restrictions", "Lower guest promise or capacity; exclude prohibited boats, swimming, seasons, or equipment.", "Rules and physical conditions are supportable but narrower than marketing."],
                ["Correction path defined", "Design, permit, removal or rebuild, construction, carrying cost, and blocked amenity nights.", "Written authority direction and complete professional scopes exist."],
                ["Transfer or compliance uncertain", "Value property without the dock and preserve contract remedy.", "No reliable approval, timing, as-built match, or lawful use conclusion."],
                ["Major event downside", "Storm, flood, ice, debris, electrical outage, access loss, guest relocation, deductible and uninsured exposure.", "Carrier terms, site history and physical scope justify scenario."],
            ]),
            "Use the <a href=\"/underwriting/\">STR underwriting framework</a> to compare the property with and without the dock amenity. Do not convert a seller's revenue story into dock value unless bookings, rates, legal use, water access, insurance, maintenance, and replacement are supported independently.",
        ]),
        ("Structure the contract and closing around evidence", [
            "Coordinate title, survey, association, permit, inspection, financing, appraisal, insurance, environmental, and access deadlines. The purchase agreement may need document delivery, authority contact, field access, underwater inspection, invasive or electrical testing, seller correction, transfer cooperation, post-close application duties, removal, restoration, escrow, credit, price adjustment, or termination. Local counsel must determine the language and remedies.",
            ("ul", [
                "Require the exact approved facility and parcel to be identified, not a generic dock reference.",
                "Define whether boats, lifts, personal watercraft, furniture, storage, safety equipment, and fuel transfer separately from the real property.",
                "Reconcile the final survey, deed, title exceptions, shoreline documents, permit drawing, authority response, inspection reports, repairs, and settlement statement before funding.",
                "Do not accept a credit for a missing right, nontransferable authorization, unlawful structure, blocked access, or unknown removal duty unless the buyer knowingly accepts the unresolved outcome and all stakeholders allow it.",
                "After closing, complete transfer or reissuance steps, record deadlines, store the permanent file, and give only the necessary operating controls to the manager.",
            ]),
        ]),
        ("Build guest and manager controls before listing the dock", [
            "A waterfront amenity needs written operating boundaries. Define whether swimming, diving, fishing, overnight mooring, lifts, watercraft, grills, alcohol, events, children, pets, nighttime use, ice, high water, storms, and third-party rentals are allowed under the permit, association, insurer, and property-specific safety plan. Do not copy generic rules from another lake or dock.",
            ("ol", [
                "Post occupancy, use, equipment, water-condition, footwear, lighting, life-jacket, supervision, weather, and emergency rules approved for the property.",
                "Inspect at the professional cadence and after storms, flood, ice, impact, unusual movement, electrical events, high water, drawdown, erosion, or repairs.",
                "Train staff to report loose boards, movement, corrosion, damaged rails, exposed wiring, tripped protection, submerged equipment, debris, fuel, sharp objects, wildlife, and missing safety equipment without attempting specialist repairs.",
                "Create stop-use thresholds, physical barriers, booking disclosures, guest relocation or credit authority, and named professional reopening approval.",
                "Record inspections, photographs, water level, closures, incidents, maintenance, permits, authority correspondence, and changes to listing claims.",
            ]),
            "Waterfront risk cannot be eliminated with a waiver or house-rule paragraph. The physical facility, legal authorization, insurance, operating supervision, and emergency plan must support the actual guest activity.",
        ]),
        ("Failure modes and the practical next step", [
            ("ul", [
                "Treating waterfront ownership as proof that a dock footprint, access route, slip, or submerged-land right conveys.",
                "Accepting an old permit card without the approved drawings, current holder, conditions, transfer process, and as-built comparison.",
                "Calling a dock grandfathered without written authority and an exact match between protected structure and current construction.",
                "Using a home inspection as the structural, underwater, lift, shoreline, and waterfront-electrical review.",
                "Assuming one sunny-season depth measurement proves year-round water access for the intended boat and guests.",
                "Pricing repair, dredging, stabilization, or replacement before confirming authority, design, environmental, access, disposal, and neighboring constraints.",
                "Adding roofs, lifts, lights, outlets, watercraft, storage, or guest activity without permit and insurer review.",
                "Opening the dock without electrical stop-use controls, event inspections, water rules, closures, and professional reopening authority.",
            ]),
            ("warn", "This guide summarizes USACE, FERC, TVA, and CPSC materials reviewed September 24, 2026. It is educational, not legal, title, riparian-rights, survey, marine, structural, electrical, environmental, navigation, insurance, lending, emergency, tax, or investment advice. Rights, waters, permits, project boundaries, ownership, transfer, construction, conditions, coverage, and remedies vary. Drowning, electrical, structural, weather, current, and water-level hazards can be fatal. Use current authority records and qualified local professionals."),
            "The practical next step is to identify every authority and ownership layer, request the complete permit and approved drawing, compare it with the current dock and survey, map the intended guest use, and commission the necessary structural, underwater, electrical, shoreline, title, and insurance reviews before the contract deadline.",
            ("callout", "Need dock findings translated into a purchase decision, reserve, guest promise, and opening plan? <a href=\"/apply/\">Apply for a BNB Accelerator strategy call</a>. We can coordinate the acquisition framework while qualified local legal, title, survey, marine, structural, electrical, environmental, insurance, lending, and permitting professionals handle their conclusions."),
        ]),
    ],
    "faqs": [
        ("Does a dock permit automatically transfer when waterfront property sells?", "Not necessarily. Transfer, reissuance, notice, inspection, compliance, and application rules depend on the authority and permit. TVA, for example, says its Section 26a shoreline permits do not transfer automatically."),
        ("Does owning waterfront property mean the buyer owns the dock?", "No. Upland land, submerged land, dock equipment, shoreline access, permits, leases, easements, and shared slip rights can have different owners or controls. Verify each with qualified professionals."),
        ("Should a buyer get a separate dock inspection?", "Yes when the dock is material. The scope may need structural, underwater, marine, lift, electrical, shoreline, survey, and permit expertise beyond a general home inspection."),
        ("Can an unpermitted dock be grandfathered?", "Do not assume so. Require the controlling authority's written rule and file, then confirm the exact current structure and use qualify. Seller or broker statements are not authority approval."),
        ("How should a buyer verify water depth at a dock?", "Record the depth, location, date, method, and water-level datum, then compare authority records for seasonal, operational, tidal, drought, flood, sediment, and navigation conditions with the intended boat and use."),
        ("Does dock insurance automatically cover STR guests?", "No. Disclose the dock, lifts, swimming, watercraft, paid guests, events, and other activities to the actual carrier and obtain the property-specific coverage decision and conditions in writing."),
    ],
    "related": [
        '<a href="/blog/title-commitment-before-buying-str/">Verify waterfront and access rights</a>',
        '<a href="/blog/electrical-panel-inspection-before-buying-str/">Coordinate electrical diligence</a>',
        '<a href="/blog/dock-watercraft-str-liability/">Review dock and watercraft liability</a>',
        '<a href="/underwriting/">Model repairs and amenity downtime</a>',
        '<a href="/apply/">Discuss the acquisition strategy</a>',
    ],
    "cta_h": "Buying a waterfront STR with a dock, slip, or shoreline permit?",
    "cta_p": "BNB Accelerator can help source and underwrite the property, coordinate diligence, and translate waterfront findings into an acquisition and launch plan while qualified local professionals handle their conclusions.",
}


if __name__ == "__main__":
    blog.build([POST])
    print(f"candidate score: {sum(SCORE.values())}/100 — {SCORE}")
