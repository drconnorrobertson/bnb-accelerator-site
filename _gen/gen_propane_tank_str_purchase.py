#!/usr/bin/env python3
"""Generate the propane-system diligence guide for STR buyers."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import blog

DATE = "2026-09-24"
SCORE = {
    "distinct_search_intent": 30,
    "buyer_relevance": 23,
    "real_question": 15,
    "service_fit": 14,
    "original_decision_support": 15,
}
assert sum(SCORE.values()) == 97

NC_LPG = "https://www.ncagr.gov/divisions/standards/lp-gas/lp-gas-faq-and-interests-consumers/standards-lp-gas-faq-consumers"
DE_CODE = "https://delcode.delaware.gov/title16/c072/"
DE_GUIDE = "https://dnrec.delaware.gov/waste-hazardous/tanks/propane/"
PHMSA = "https://www.phmsa.dot.gov/training/pipeline/small-lp-gas-operator-guide-april-2017"
UTAH = "https://firemarshal.utah.gov/licensing-and-certification/liquified-petroleum-gas/"

POST = {
    "slug": "propane-tank-before-buying-str",
    "title": "Propane-tank diligence before buying an STR",
    "title_tag": "Propane Tank Diligence Before Buying an STR",
    "h1": "What should an STR buyer verify about a propane tank?",
    "description": "Buying an Airbnb with propane? Verify tank ownership, lease transfer, fuel balance, inspection, supplier access, permits, insurance, and opening reserves.",
    "date": DATE,
    "category": "Acquisition Diligence",
    "lead": "Before closing on a propane-served short-term rental, establish who owns every tank and component, whether a lease or supplier agreement transfers, what fuel is included, whether the complete system is lawful and acceptable to the lender and insurer, and whether deliveries can support peak-season guest use. Then obtain a qualified inspection, price repairs and replacement separately from fuel, confirm supplier access and outage response, and preserve a contractual remedy. A tank beside the house, a delivery ticket, or a seller statement does not answer the ownership, condition, compliance, supply, or operating questions by itself.",
    "sections": [
        ("The direct answer for an STR buyer", [
            "Treat propane as five linked files: ownership and contracts, physical equipment, code and permit history, fuel supply and delivery, and guest operations. A failure in any one can delay closing or launch. A leased tank may remain the supplier's property after the land is sold. An owned tank may still need repair, documentation, or a new supplier inspection. A compliant residential installation may need a different review when occupancy, appliances, outdoor amenities, backup generation, or delivery traffic changes.",
            f"North Carolina's official <a href=\"{NC_LPG}\" rel=\"noopener\">LP-gas consumer FAQ</a> gives a concrete example of why buyers must ask: it says supplier ownership may be documented through a UCC filing, supplier-owned tanks should carry company identification, and the state's residential disclosure form asks whether a fuel tank is above or below ground and leased or seller-owned. Those are North Carolina examples—not universal rules—but the diligence problem exists wherever ownership and service obligations are unclear.",
            ("callout", "Evaluating a cabin, rural home, lake property, or backup-generator site served by propane? <a href=\"/apply/\">Apply for a BNB Accelerator strategy call</a> to connect the fuel system with the offer, utilities, insurance, reserves, renovations, and opening plan. Qualified local propane, HVAC, plumbing, electrical, fire, legal, title, environmental, insurance, lending, and permitting professionals must make their respective conclusions."),
        ]),
        ("Prove who owns the tank and fuel", [
            "Do not infer ownership from location, age, burial, seller payment history, or a lack of labels. Request the tank purchase invoice, bill of sale, lease, rental or service agreement, supplier account history, UCC search where relevant, title and fixture treatment, seller disclosure, and written supplier confirmation. Identify ownership of the tank, regulators, telemetry, lines, meters, vaporizers, pads, protective barriers, and any community distribution equipment separately.",
            f"State law can make the distinction decisive. <a href=\"{DE_CODE}\" rel=\"noopener\">Delaware Code section 7208</a>, for example, says qualifying leased or bailed LP-gas containers remain movable property and supplier ownership is not changed by a sale of the land. Do not generalize that rule to another jurisdiction. Use local counsel and current statutes, contracts, filings, title evidence, and supplier records for the actual property.",
            ("table", ["Question", "Evidence to obtain", "Closing risk"], [
                ["Who owns the tank?", "Invoice, bill of sale, lease, supplier letter, label, serial and data plate, filings, contract and title review.", "Buyer may pay for equipment that does not convey or may inherit removal obligations."],
                ["Who owns the fuel?", "Contract, delivery records, gauge reading method, settlement clause, supplier valuation.", "Seller and buyer may dispute remaining gallons or prepaid fuel."],
                ["Does the agreement transfer?", "Assignment terms, consent, credit approval, minimum-use rules, pricing and fees.", "Service may stop or economics may change at closing."],
                ["Can another supplier fill it?", "Ownership terms, state rules, supplier policies, equipment compatibility and release.", "A leased tank can limit supplier choice; unauthorized filling may be prohibited."],
                ["Who removes or restores?", "Lease termination, pickup, pump-out, excavation, hole filling, line capping and surface restoration terms.", "Changing suppliers or systems can create material site cost and downtime."],
            ]),
        ]),
        ("Create a complete equipment inventory", [
            "Map every tank, cylinder, regulator, valve, line, meter, appliance connection, generator feed, shutoff, protective barrier, vent or relief area, and abandoned component. Record aboveground or underground location, manufacturer, serial, capacity, data plate, apparent age, ownership label, visible condition, fill point, delivery approach, and connected loads. Do not clean, uncover, operate, disconnect, excavate, or test equipment yourself.",
            ("ol", [
                "List all propane loads: heating, water heating, cooking, fireplaces, pool or spa heating, grills, fire features, dryers, generators, and accessory buildings.",
                "Collect installation and alteration permits, inspection finals, pressure or leak tests, appliance records, service calls, regulator replacement, tank coating or cathodic-protection records, and repair invoices.",
                "Match each component to the supplier or qualified contractor responsible for it; leased equipment and owner equipment can coexist.",
                "Identify buried line routes before planning driveways, parking, decks, pools, septic work, landscaping, fencing, utilities, or excavation.",
                "Photograph labels and plates from a safe position and preserve the supplier's emergency and account contacts in the diligence file.",
                "Ask the qualified propane professional which system portions are included, inaccessible, untested, or outside their license and inspection scope.",
            ]),
            "A home inspector may flag visible concerns without testing the complete gas system or determining lease rights, sizing, code compliance, fuel quality, appliance combustion, buried-line condition, or insurer acceptance. Read the inspection agreement and commission the right licensed disciplines.",
        ]),
        ("Define a qualified inspection instead of asking for clearance", [
            "Request a written inspection scope tied to the intended property use. It may need tank and cylinder condition, supports and anchorage, corrosion controls, regulators, valves, relief components, lines, burial and protection, leak or pressure testing, appliance connections, ventilation and combustion, shutoffs, protective barriers, separation and ignition sources, delivery access, permits, and documentation. Applicable requirements depend on jurisdiction, equipment, capacity, installation date, occupancy, and planned changes.",
            f"PHMSA publishes a <a href=\"{PHMSA}\" rel=\"noopener\">Small LP Gas Operator Guide</a> for systems that fall under federal pipeline jurisdiction. It emphasizes that some multi-user or public-place systems can be regulated differently from a typical individual residential installation. Most single-property residential tanks will not automatically become a PHMSA-regulated distribution system, but a shared community system, multiple buildings, metering, or public access should prompt the buyer to identify the operator and the governing framework rather than guess.",
            ("table", ["Inspection layer", "Decision question", "Output"], [
                ["Ownership and identity", "Is the inspected equipment the same equipment described in the contract and supplier records?", "Mapped IDs, labels, serials, owner and account status."],
                ["Tank and regulators", "Are condition, placement, protection and service history acceptable for continued use?", "Observed conditions, tests, exclusions, repair or replacement priority."],
                ["Lines and shutoffs", "Are routes known, protected and tested under the applicable procedure?", "Route evidence, test result, limitations and completion criteria."],
                ["Appliances and combustion", "Are connected loads installed and operating within each professional's scope?", "Appliance-specific findings, ventilation or combustion results, service needs."],
                ["Capacity and demand", "Can storage, vaporization, regulation and delivery cadence support concurrent peak loads?", "Load inventory and property-specific sizing or supply conclusion."],
                ["Emergency controls", "Can occupants and responders identify shutoffs and supplier contacts without unsafe intervention?", "Labeled plan, manager procedure and professional instructions."],
            ]),
            "Avoid asking anyone to declare a propane system universally safe. Require dated observations, methods, results, limitations, code or standard references where appropriate, repairs, reinspection requirements, and who is qualified to perform the next action.",
        ]),
        ("Verify siting, delivery access, and planned improvements", [
            "Tank location must work as both a regulated installation and a recurring delivery route. Map the tank and fill point relative to buildings, openings, ignition sources, property lines, roads, parking, traffic, overhead and underground utilities, septic, drainage, slopes, vegetation, snow storage, gates, fences, decks, pools, fire features, generators, and future construction. Local professionals and authorities must apply the current rules.",
            "Delivery feasibility is operational, not merely legal. Ask the supplier to confirm truck approach, hose route, turning and backing, bridge or private-road limits, gate width, surface and grade, winter service, snow and ice control, vegetation clearance, pets, guest vehicles, locked access, minimum delivery, remote monitoring, will-call procedures, and emergency or after-hours response.",
            ("ul", [
                "Do not add parking, a deck, hot tub, pool, fire pit, generator, shed, fence, retaining wall, or landscaping until the propane professional reviews separation, line routes, fill access, and relief clearances.",
                "Protect tanks and components from guest vehicles, delivery trucks, snow equipment, mowers, falling ice, flooding, erosion, tree failure, wildfire exposure, and stored materials under professional direction.",
                "Confirm that screens or landscaping do not block labels, ventilation, relief discharge, inspection, emergency shutoff, or delivery access.",
                "Coordinate buried tank and line work with utility locating, excavation law, corrosion protection, environmental response, drainage, and lawful restoration.",
                "Document whether a change in use, appliance load, aggregate capacity, accessory unit, or shared system triggers plan review or inspection.",
            ]),
            f"State rules and licenses vary. Utah's State Fire Marshal, for example, publishes <a href=\"{UTAH}\" rel=\"noopener\">separate LP-gas license classes</a> for dealers, cylinder businesses, equipment installers, and other activities. Verify the exact license and authority required where the property is located; a general contractor or appliance seller is not automatically authorized for every propane scope.",
        ]),
        ("Reconcile permits, disclosures, supplier records, and insurance", [
            "Build one record set containing the seller disclosure, lease, equipment invoice, supplier confirmation, permits and finals, service and delivery history, qualified inspection, repair proof, lender conditions, insurer response, and settlement terms. Disagreement among those records is a diligence finding, not paperwork noise.",
            f"Delaware's state guidance illustrates a transaction-specific process: its <a href=\"{DE_GUIDE}\" rel=\"noopener\">propane-tank page</a> describes seller notice and supplier service-agreement delivery requirements for a residence sale. Other states may use different or no comparable procedure. Ask local counsel and the supplier what notice, assignment, disclosure, removal, refund, deposit, and consumer-protection rules apply to the actual closing.",
            ("table", ["Participant", "Written question", "What its answer does not prove"], [
                ["Supplier", "Ownership, agreement, account transfer, equipment responsibility, delivery and emergency service.", "Title treatment, code approval, insurer coverage, or every downstream appliance condition."],
                ["Local authority", "Permit, inspection and current approval requirements for the installation or change.", "Future performance, fuel availability, contract transfer, or insurance coverage."],
                ["Insurer", "Acceptance, required inspection or mitigation, propane and STR business-use treatment, loss and interruption coverage.", "Physical safety, legal ownership, or lender approval."],
                ["Lender and appraiser", "Collateral eligibility, repairs, utilities, property use and closing conditions.", "Operational capacity or permission to short-term rent."],
                ["Title and counsel", "Fixture, lien, UCC, lease, conveyance, fuel and settlement treatment.", "Equipment condition or technical compliance."],
            ]),
        ]),
        ("Worked example: a cabin with a buried tank and generator", [
            "Assume an illustrative buyer is evaluating a four-bedroom cabin with propane heat, water heating, range, fireplaces, and a standby generator. The listing says the buried tank is included. The seller provides delivery tickets but no purchase invoice, lease, tank map, permit, or generator load documentation. A faded supplier marker is visible near the fill point.",
            "The supplier confirms it owns the buried tank and requires a new customer agreement, credit approval, minimum annual purchase, and inspection before service continues. The seller's delivery record shows winter usage but not the underground line route or simultaneous generator demand. A qualified propane professional identifies documentation and protection issues and requests a separate appliance and generator review. The driveway must remain clear for delivery during guest stays.",
            "The buyer does not value the tank as conveyed equipment. Counsel and title professionals address the contract and settlement; the supplier provides transfer and removal terms; qualified trades define repairs and load questions; the lender and insurer review final evidence. The model includes account setup, inspection, repairs, fuel at opening, delivery access controls, and a cold-weather reserve. All property facts, contract terms, and findings are illustrative—not a client result, legal opinion, inspection, code conclusion, or forecast.",
        ]),
        ("Underwrite fuel, equipment, and interruption separately", [
            "Separate the economics into fuel consumption, tank or agreement charges, inspections and maintenance, repairs, replacement, delivery constraints, and interruption. Historical gallons can be a starting point only after reconciling weather, occupancy, owner use, thermostat settings, appliance changes, tank fills, beginning and ending inventory, leaks or outages, and whether the seller's period resembles the STR plan.",
            ("ol", [
                "Create a load schedule by appliance, season, operating pattern, and concurrent peak rather than dividing annual fuel evenly by month.",
                "Normalize delivery records for gauge or inventory changes so purchased gallons are not confused with gallons consumed.",
                "Add tank rent, minimum-use or early-termination charges, monitoring, delivery fees, account deposits, fuel prebuy or contract terms, inspection, and emergency delivery where applicable.",
                "Price immediate repairs, future tank and regulator replacement, buried-line uncertainty, excavation and restoration, appliance service, permits, and professional reinspection as separate lines.",
                "Stress-test a missed delivery, supplier transition, severe-weather demand, road closure, power outage, generator run, empty tank, equipment lockout, and affected booking nights.",
            ]),
            "Use the <a href=\"/underwriting/\">STR underwriting framework</a> to model fuel and downtime without inventing efficiency or consumption. Obtain property-specific input from the supplier and qualified trades, then preserve a downside case for weather and occupancy outside the seller's history.",
        ]),
        ("Structure the closing around executable evidence", [
            "The purchase contract and settlement need to resolve the tank, fuel, lease, supplier account, inspection, repairs, and transfer timing. Local counsel should determine the legal language. A generic fixtures clause may not address supplier-owned equipment, deposits, prepaid fuel, removal, buried restoration, service interruption, or obligations that cannot be assigned.",
            ("table", ["Open item", "Possible response to investigate", "Completion evidence"], [
                ["Ownership unclear", "Seller obtains supplier and documentary confirmation; conduct appropriate filing and title review.", "Written ownership and closing treatment tied to identified equipment."],
                ["Lease does not transfer", "New agreement, seller termination, supplier removal, buyer purchase, replacement system, price or closing change.", "Executed agreement or completed lawful removal and replacement path."],
                ["Inspection finds repair", "Seller-completed work, buyer-controlled credit, escrow where viable, closing condition, or termination.", "Licensed invoice, permit/final where required, test or reinspection record."],
                ["Fuel balance disputed", "Define measurement time, method, price, taxes or fees, settlement credit, and ownership.", "Closing statement plus supplier or professional gauge documentation."],
                ["Delivery cannot support use", "Redesign access, tank or monitoring plan, alternate supplier if lawful, reduce loads, or terminate.", "Supplier acceptance and operating procedure—not a broker assurance."],
            ]),
            "Do not close on a promise that the next supplier will sort it out. Some providers will require an inspection, ownership proof, contract release, repairs, or equipment change before filling or service. Resolve the service path while contract remedies remain available.",
        ]),
        ("Build propane controls into STR operations", [
            "Transfer the system map, supplier agreement, delivery calendar, account contacts, gauge or telemetry instructions, shutoff information, inspection records, appliance list, and emergency procedure to the manager. Guests and cleaners should never be assigned diagnosis, repair, leak testing, relighting, tank handling, or fuel transfer outside approved written instructions from qualified professionals.",
            ("ul", [
                "Set reorder thresholds and named responsibility using the supplier's guidance; do not wait for a guest to report no heat or hot water.",
                "Keep delivery access clear of parked cars, snow, gates, furniture, bins, landscaping, and events on scheduled and emergency days.",
                "Create a no-flame, evacuation, and emergency-contact response for suspected gas odor or leak using supplier and authority instructions; do not improvise or switch equipment back on.",
                "Document outages, empty-tank events, regulator or appliance lockouts, fuel deliveries, repairs, guest relocations, and reopening authorization.",
                "Coordinate fireplaces, grills, fire features, pool or spa heat, and generators with the specific system capacity and professional operating instructions.",
                "Review the plan after appliance additions, renovations, supplier changes, tank work, excavation, vehicle impact, flood, wildfire, or other material events.",
            ]),
            "The operating plan should say who can close the property, contact emergency services, authorize a qualified responder, relocate guests, issue credits, and approve reopening. Fuel availability is a habitability and revenue dependency, not only a utility bill.",
        ]),
        ("Failure modes and the practical next step", [
            ("ul", [
                "Assuming a tank conveys because it is attached, buried, unlabeled, or listed as part of the property.",
                "Reading delivery tickets without obtaining the lease, ownership proof, supplier confirmation, permits, and full equipment inventory.",
                "Treating a general home inspection or appliance flame test as a complete propane-system evaluation.",
                "Changing suppliers or authorizing a fill without resolving tank ownership, contract rights, state rules, and provider requirements.",
                "Adding a generator, hot tub, pool heater, fire feature, kitchen load, or accessory unit without reviewing capacity and system changes.",
                "Blocking tank access or relief clearances with parking, decks, screening, snow, landscaping, fencing, storage, or guest amenities.",
                "Underwriting purchased gallons as consumption without beginning and ending inventory, weather, occupancy, and appliance normalization.",
                "Launching without delivery thresholds, cold-weather response, leak or odor procedures, and qualified reopening authority.",
            ]),
            ("warn", "This guide summarizes selected federal and state materials reviewed September 24, 2026. It is educational, not propane, plumbing, HVAC, electrical, fire, pipeline, environmental, legal, title, insurance, lending, contracting, tax, or investment advice. Ownership, licenses, codes, permits, contracts, equipment, suppliers, coverage, and emergency instructions vary. Propane is flammable; never inspect, operate, repair, disconnect, refill, excavate, relight, or test equipment without the qualified authority and training required."),
            "The practical next step is to photograph the equipment identifiers from a safe location, request ownership and contract documents, obtain written supplier confirmation, map every connected load and delivery constraint, and commission the qualified inspection early enough to repair, transfer, replace, reprice, or terminate before the deadline.",
            ("callout", "Need propane findings translated into a purchase decision, reserve, utility plan, and launch schedule? <a href=\"/apply/\">Apply for a BNB Accelerator strategy call</a>. We can coordinate the acquisition framework while qualified local propane, trade, legal, title, insurance, lending, environmental, and permitting professionals handle their conclusions."),
        ]),
    ],
    "faqs": [
        ("Does a propane tank automatically transfer with the house?", "No universal rule applies. A supplier may own a leased tank even when it is attached or buried. Review the contract, supplier records, disclosures, filings, title treatment, and local law with qualified professionals."),
        ("How can a buyer tell whether a propane tank is owned or leased?", "Request the purchase invoice or lease, supplier confirmation, service records, equipment label and serial, disclosures, and any relevant filing or title evidence. Do not rely on the seller's memory alone."),
        ("Can a different propane company fill a leased tank?", "Do not assume so. Ownership, contract terms, state rules, provider policy, equipment condition, and authorization may restrict filling. Resolve the question directly with the owner and qualified local professionals."),
        ("Should a buyer inspect an underground propane tank?", "Yes when it is material to the purchase, using the qualified professionals and scope appropriate to tank condition, corrosion protection, lines, ownership, permits, system operation, and planned use."),
        ("How should remaining propane be handled at closing?", "The contract should define whether fuel conveys, how and when quantity is measured, which price and fees apply, and how the settlement credit is documented. Local counsel and the supplier should guide the actual transaction."),
        ("Does propane delivery history prove the system can support an STR?", "No. Reconcile weather, occupancy, appliances, beginning and ending inventory, generator use, delivery access, peak demand, and supplier capacity before using history in the forecast."),
    ],
    "related": [
        '<a href="/blog/clue-report-before-buying-str/">Review property claim history</a>',
        '<a href="/blog/electrical-panel-inspection-before-buying-str/">Coordinate generator and electrical loads</a>',
        '<a href="/blog/private-road-maintenance-agreement-before-buying-str/">Protect fuel-delivery access</a>',
        '<a href="/underwriting/">Model fuel and interruption</a>',
        '<a href="/apply/">Discuss the acquisition strategy</a>',
    ],
    "cta_h": "Buying an STR with leased or owned propane equipment?",
    "cta_p": "BNB Accelerator can help source and underwrite the property, coordinate diligence, and translate propane findings into an acquisition and launch plan while qualified local professionals handle their conclusions.",
}


if __name__ == "__main__":
    blog.build([POST])
    print(f"candidate score: {sum(SCORE.values())}/100 — {SCORE}")
