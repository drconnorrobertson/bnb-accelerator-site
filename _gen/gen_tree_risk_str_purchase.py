#!/usr/bin/env python3
"""Generate the tree-risk assessment guide for STR buyers."""
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
    "original_decision_support": 14,
}
assert sum(SCORE.values()) == 95

USFS_GUIDE = "https://www.fs.usda.gov/sites/nfs/files/legacy-media/r04/Hazard%20Tree%20Guide--Regions%201%20and%204.pdf"
USFS_MANAGEMENT = "https://www.fs.usda.gov/Internet/FSE_DOCUMENTS/fseprd933384.pdf"
NPS = "https://www.nps.gov/yose/learn/nature/treehazards.htm"
ISA_RISK = "https://www.treesaregood.org/Tree-Owner-Resources/Managing-Hazards-and-Risk"
ISA_FIND = "https://www.treesaregood.org/Find-an-Arborist/arboristsearch"

POST = {
    "slug": "tree-risk-assessment-before-buying-str",
    "title": "Tree-risk assessments before buying a short-term rental",
    "title_tag": "Tree-Risk Assessment Before Buying an STR",
    "h1": "Should you get a tree-risk assessment before buying an STR?",
    "description": "Buying an Airbnb with mature trees? Learn when to hire an arborist, define the scope, price mitigation, protect guest areas, and structure closing.",
    "date": DATE,
    "category": "Acquisition Diligence",
    "lead": "Order a qualified tree-risk assessment when large trees or limbs can reach the house, parking, driveway, decks, hot tub, fire pit, play area, paths, utilities, septic field, neighboring property, or another place people and assets remain. A general home inspection, landscaping walk-through, seller pruning invoice, or healthy-looking canopy is not a substitute. The acquisition decision needs a defined tree population and target area, an appropriate assessment level, documented limitations, mitigation options, access and permit checks, written bids, and a post-storm monitoring plan.",
    "sections": [
        ("The direct answer for an STR buyer", [
            "Yes when a tree or tree part could strike an occupied or operational target and the consequence matters to the purchase. Prioritize wooded cabins, mature urban lots, storm-exposed properties, recently cleared sites, steep slopes, fire-affected land, construction-damaged root zones, trees near structures or utilities, and properties marketed around outdoor amenities. The goal is not to certify that trees are safe. It is to identify observable conditions, understand the limits of the inspection, reduce unacceptable risk, and carry the remaining risk deliberately.",
            f"The U.S. Forest Service's <a href=\"{USFS_GUIDE}\" rel=\"noopener\">hazard-tree guide</a> frames assessment around failure potential, damage potential, and target value. Its examples include dead or declining trees, broken branches, wounds, damaged roots, lean, weak anchoring, decay, disease, insects, wind exposure, soil conditions, and root disease. That framework is useful for acquisition questions, but a Forest Service rating system is not automatically the standard for a private residential report. Ask the arborist which current method, scope, and terminology will govern the engagement.",
            ("callout", "Evaluating a wooded cabin, lake house, mountain property, or mature urban lot? <a href=\"/apply/\">Apply for a BNB Accelerator strategy call</a> to connect tree findings with the offer, renovation plan, insurance, reserves, outdoor amenities, and opening date. Qualified arborists and local legal, insurance, utility, environmental, engineering, and permitting professionals must make their respective conclusions."),
        ]),
        ("Risk depends on the tree and the target", [
            "A defect without a meaningful target may create a different priority than the same defect over a bedroom, parked car, hot tub, or gathering area. Likewise, a valuable target does not prove the tree is likely to fail. A useful assessment connects the likelihood of whole-tree or branch failure, the likelihood of impact, and the consequence during a stated time period and occupancy pattern.",
            f"The Forest Service's <a href=\"{USFS_MANAGEMENT}\" rel=\"noopener\">Hazard Tree Management</a> guidance describes a target as something that may be struck and distinguishes moving targets from places where people or vehicles congregate or remain. For an STR, occupancy changes the target map: sleeping rooms, guest parking, decks, hammocks, fire pits, pools, hot tubs, play equipment, wedding setups, and cleaner staging can keep people in potential impact zones much longer than a quick residential walk-through suggests.",
            ("table", ["Target", "Acquisition question", "Operating consequence"], [
                ["House or guest unit", "Can whole-tree or branch failure reach occupied rooms, egress, roof, chimney, or service equipment?", "Injury, displacement, roof opening, water intrusion, booking loss."],
                ["Driveway and parking", "Can failure block the only route or strike stationary vehicles and arriving guests?", "No access, towing conflict, refunds, emergency-response delay."],
                ["Deck, hot tub, fire pit, play area", "How long are guests stationary beneath or beside the tree?", "Higher exposure in an amenity marketed as central to the stay."],
                ["Utilities and fuel", "Could limbs or roots affect overhead service, panels, propane, water, sewer, or communications?", "Outage, ignition, leak, service delay, unsafe guest conditions."],
                ["Neighboring land", "Could a subject tree or neighboring tree affect either property, and who controls mitigation?", "Access, consent, boundary, liability, and dispute risk."],
                ["Septic, drainage, retaining, or slope", "Would removal, roots, equipment, or failure interact with site systems?", "Repair complexity, erosion, access damage, redesign."],
            ]),
        ]),
        ("Define the scope before the arborist arrives", [
            "Do not order a vague tree inspection and expect every tree, root, branch, disease, boundary, and concealed condition to be covered. Give the arborist the parcel map, survey when available, planned guest-use map, renovation concept, known storm or fire history, seller records, and the decision deadline. Ask for a written proposal that identifies the trees or zones, assessment method and level, time horizon, targets, access, equipment, exclusions, deliverables, and whether recommendations and cost ranges are included.",
            ("ol", [
                "Map the main structure, accessory units, driveway, parking, paths, utilities, septic, drainage, retaining structures, decks, pool, hot tub, fire pit, play area, and planned construction.",
                "Mark every tree or stand whose whole-tree or branch-failure zone may reach those targets, including trees near property lines and offsite trees that can be observed lawfully.",
                "List recent storms, wildfire or prescribed fire, lightning, grading, trenching, paving, additions, tree removals, drainage change, soil placement, compaction, and utility work.",
                "Collect prior arborist reports, pruning and removal invoices, plant-health treatments, permits, association approvals, claims, photographs, and seller disclosures.",
                "Ask whether the assignment is a limited visual screen, basic assessment, advanced assessment, inventory, plant-health evaluation, construction-impact review, or another defined service.",
                "Require tree identifiers and a map so each observation, recommendation, bid, and completion record refers to the same tree.",
            ]),
            "A drive-by screen can identify an obvious dead tree without evaluating concealed roots or decay. A visual assessment can document observable conditions without instrument testing or climbing. Advanced work may use aerial inspection, sounding, probing, resistance or sonic tools, root investigation, laboratory analysis, or other methods when justified. More testing is not automatically better; the arborist should explain which uncertainty it is designed to reduce.",
        ]),
        ("Read the report without turning it into a guarantee", [
            f"The National Park Service explains in its <a href=\"{NPS}\" rel=\"noopener\">tree-hazard management overview</a> that disease, insects, soil moisture, wind, fire, snow, and human activity interact—and that trees without apparent defects can still fail. That is the correct boundary for a buyer: assessment can improve a decision, but it cannot eliminate all tree risk or predict every storm-driven failure.",
            ("table", ["Report element", "What to require", "Why it matters"], [
                ["Tree identity", "Number, species when supportable, location, photographs, ownership uncertainty.", "Prevents the wrong tree from being bid, pruned, removed, or monitored."],
                ["Targets and occupancy", "Named structures and use areas, expected occupancy, movement, and consequences.", "Connects findings to the actual STR plan rather than a generic residence."],
                ["Observed conditions", "Defects, health indicators, site conditions, roots, lean, canopy, attachments, and relevant history.", "Separates evidence from assumptions and seller narratives."],
                ["Risk statement", "Method, components, time frame, weather assumptions, and rating language.", "Makes ratings comparable and prevents a color label from becoming a warranty."],
                ["Limitations", "Visibility, season, foliage, access, soil, concealed roots or decay, excluded trees, weather, and tools used.", "Shows where uncertainty remains and whether more work changes the decision."],
                ["Mitigation and priority", "Options, timing, residual risk, reinspection trigger, and who is qualified to perform the work.", "Turns the report into closing and operating controls."],
            ]),
            "Ask the arborist to distinguish tree health from structural risk. A vigorous tree can have a weak attachment or compromised root system. A declining tree does not automatically require immediate removal if the target, failure mode, and mitigation support a different professional recommendation. Do not translate one attribute into the whole decision.",
        ]),
        ("Construction and amenity plans can change the answer", [
            "The assessment should address the property as purchased and the property as planned. A new driveway, parking pad, pool, deck, utility trench, septic work, retaining wall, grade change, drainage swale, patio, or addition can cut roots, compact soil, alter water, expose previously sheltered trees to wind, or move people into a target zone. Removing one tree can change wind exposure and loading on trees that remain.",
            f"The International Society of Arboriculture's <a href=\"{ISA_RISK}\" rel=\"noopener\">tree-risk guidance</a> notes that construction can injure trunks and crowns, compact soil, sever or smother roots, and change wind, sunlight, grade, and drainage. It also describes mitigation categories such as moving a target, pruning, support systems, routine care, or removal, while warning that support systems are not guarantees against failure.",
            ("ul", [
                "Overlay the root-protection and canopy concerns on the survey and site plan before finalizing amenity placement.",
                "Ask which access routes, staging zones, equipment, excavation, fill, drainage, and material storage need tree-protection controls.",
                "Coordinate tree work with utility locating, septic protection, erosion control, wildlife or habitat rules, fire requirements, historic or scenic restrictions, and local permits.",
                "Price restoration for lawn, drive, fence, irrigation, drainage, walls, roofs, utilities, and neighboring areas—not only the cut or pruning price.",
                "Reassess retained trees after design changes, major removals, root exposure, grade changes, storm damage, or construction impacts identified by the arborist.",
            ]),
        ]),
        ("Keep assessment independent from the removal sale", [
            "A company can be qualified to assess and perform work, but the buyer should understand incentives and scope. Ask who wrote the opinion, which credentials and experience apply, whether compensation depends on selling pruning or removal, and whether the buyer wants an independent consulting assessment before authorizing expensive or irreversible work.",
            f"ISA's <a href=\"{ISA_FIND}\" rel=\"noopener\">credential directory</a> lets the public locate and verify participating credential holders. A credential is one screen, not a complete vendor decision. Verify the individual, report scope, local license where required, insurance, workers' compensation, references, equipment, utility procedures, subcontractors, traffic control, debris handling, and who will obtain permits and approvals.",
            ("table", ["Role", "Primary output", "Conflict to control"], [
                ["Assessing arborist", "Mapped findings, risk analysis, options, priority, limitations, reinspection plan.", "Recommendation may lead to work the same company sells."],
                ["Tree-work contractor", "Method, crew, equipment, access, protection, debris, schedule, completion proof.", "Low bid may omit restoration, permits, difficult rigging, or excluded wood."],
                ["Engineer or other specialist", "Property-specific conclusion for structures, slopes, retaining, roots, or utilities when needed.", "Arborist findings do not replace another profession's scope."],
                ["Insurer", "Coverage, exclusions, conditions, vacancy or renovation treatment, documentation request.", "A binding decision is not a tree-risk assessment; an assessment is not coverage."],
                ["Local authority or association", "Permit, protected-tree, right-of-way, utility, fire, or design approval.", "A contractor's willingness to cut does not prove legal authority."],
            ]),
        ]),
        ("Worked example: a cabin built around outdoor gathering", [
            "Assume an illustrative buyer is evaluating a cabin whose listing emphasizes a deck, hot tub, fire pit, hammock grove, and wooded driveway. A general inspection notes dead limbs but excludes tree-risk assessment. The seller provides a pruning invoice from two years earlier. The buyer plans to add parking and widen the fire-pit area before launch.",
            "A qualified arborist maps the trees and targets. The report identifies one dead branch over guest parking, a multi-stem tree beside the hot tub requiring further evaluation, construction damage near roots along the proposed parking edge, and several trees outside the occupied zones that need routine monitoring rather than immediate work. The arborist records access and seasonal limitations and explains that the rating applies to a stated period, not every future storm.",
            "The buyer obtains matched scopes for priority pruning, advanced evaluation, root-zone protection, debris removal, and post-construction reassessment. The designer moves the parking edge and hammock targets. Counsel and a surveyor address a boundary-tree question; the insurer reviews the property and business use; the local authority confirms permit rules. The base model excludes affected amenities until work and documentation are complete. All trees, findings, responses, and costs in this example are illustrative—not a client result, arboricultural opinion, or forecast.",
        ]),
        ("Translate mitigation into the offer and underwriting", [
            "Put each recommendation into one of five lanes: remove the target, reduce exposure, prune or treat, install a professionally designed support or protection measure, remove the tree, or monitor under a defined interval and trigger. A report may recommend more than one option. The buyer then needs access, legal authority, a complete bid, completion evidence, and a residual-risk decision.",
            ("table", ["Finding", "Transaction response to investigate", "Completion evidence"], [
                ["Priority work with bounded scope", "Seller-completed work, buyer-controlled credit, escrow where viable, price change, or closing condition.", "Named-tree invoice, permit and approval, before/after records, assessor or authority follow-up when required."],
                ["Advanced assessment needed", "Extend diligence and authorize the specific method before waiving the condition.", "Written supplemental report tied to the mapped tree and target."],
                ["Neighbor or boundary tree", "Survey and local legal review; obtain consent or define lawful options.", "Written agreement, verified boundary, documented professional and legal path."],
                ["Construction interaction", "Redesign, protection plan, arborist monitoring, contractor controls, reassessment.", "Approved plan, site controls, inspection records, post-work report."],
                ["Unacceptable residual risk", "Move the target, change use, remove if lawful, renegotiate, or terminate.", "Do not substitute a waiver or guest warning for unresolved professional conclusions."],
            ]),
            "Model assessment and testing, pruning, removal, difficult access, crane or rigging, traffic control, utility coordination, permits, stump and wood handling, erosion and drainage controls, landscape restoration, structure repair, follow-up care, recurring inspection, storm response, amenity downtime, lost nights, and a property-specific reserve in the <a href=\"/underwriting/\">STR underwriting framework</a>. A round tree allowance without named work is not a bid.",
        ]),
        ("Create an operating tree-risk program before launch", [
            "Tree diligence does not end at closing because weather, disease, construction, soil, targets, and occupancy change. Transfer the mapped tree inventory and report to the manager. Define routine observations, professional reassessment intervals, event-driven inspections, stop-use zones, emergency contacts, guest communication, documentation, and authority to block an amenity or listing.",
            ("ol", [
                "Inspect the property after high wind, heavy snow or ice, lightning, flooding, fire, soil movement, vehicle impact, excavation, or a reported crack, hang-up, heave, or new lean.",
                "Train staff to photograph and escalate dead or hanging limbs, fresh cracks, root-plate movement, fungal growth, cavities, broken tops, sudden canopy change, soil disturbance, or contact with structures and utilities—without diagnosing or climbing.",
                "Keep guests and staff away from a suspected impact zone until the responsible qualified professional determines the next step.",
                "Never let cleaners, managers, or guests cut storm-loaded limbs, touch trees or branches contacting utilities, or work aloft outside their role.",
                "Record the tree ID, date, observation, weather or event, photographs, restriction, professional response, completed work, and next review date.",
                "Update the target map whenever furniture, hammocks, tents, fire pits, play equipment, parking, paths, or other guest-use areas move.",
            ]),
            "The manager also needs a booking response: who decides to close an outdoor area, relocate a vehicle, cancel a stay, call utilities or emergency services, approve a refund, and document reopening. The safest temporary action may be distance and closure, not improvised cutting.",
        ]),
        ("Failure modes and the practical next step", [
            ("ul", [
                "Calling a landscaping review or general home inspection a tree-risk assessment.",
                "Assessing only trees that look unhealthy while ignoring targets, roots, lean, attachments, site change, and neighboring trees.",
                "Ordering a vague visual opinion without mapped tree IDs, scope, method, time horizon, limitations, or priorities.",
                "Treating a low rating, healthy canopy, prior pruning, cable, or support system as a guarantee against failure.",
                "Pricing removal without access, rigging, utilities, traffic control, permits, debris, stump work, restoration, and neighboring-property constraints.",
                "Letting a renovation cut roots, compact soil, change drainage, or expose retained trees without arborist coordination.",
                "Placing a hot tub, hammock, fire pit, parking space, or play area beneath trees without updating the target assessment.",
                "Opening after a major storm or site disturbance without a defined event-driven inspection and stop-use rule.",
            ]),
            ("warn", "This guide summarizes USDA Forest Service, National Park Service, and ISA materials reviewed September 24, 2026. It is educational, not arboricultural, forestry, engineering, environmental, utility, fire, legal, insurance, contracting, medical, tax, or investment advice. Tree conditions, assessment methods, credentials, permits, protected species, boundary law, weather, coverage, and remedies vary. Trees and branches can fail without visible warning. Use qualified local professionals and current source documents."),
            "The practical next step is to map every occupied and operational target, mark the trees that can reach them, collect tree and site-change history, and request a written assessment proposal from a qualified arborist early enough to investigate, price, permit, negotiate, or redesign before the contract deadline.",
            ("callout", "Need tree findings translated into a purchase decision, reserve, amenity plan, and opening schedule? <a href=\"/apply/\">Apply for a BNB Accelerator strategy call</a>. We can coordinate the acquisition framework while qualified local arboricultural, legal, insurance, utility, engineering, environmental, and permitting professionals handle their conclusions."),
        ]),
    ],
    "faqs": [
        ("When should an STR buyer hire an arborist?", "Hire one when trees or limbs can reach occupied structures, parking, access, amenities, utilities, neighboring property, or planned construction—and whenever storm, fire, grading, root damage, lean, decay, or deadwood creates a material question."),
        ("Does a home inspection include a tree-risk assessment?", "Usually not unless the agreement explicitly says so and the inspector is qualified for that scope. Read the exclusions and order the right specialist when the purchase depends on tree condition or risk."),
        ("Can an arborist guarantee that a tree will not fall?", "No. Assessment addresses observable conditions, targets, assumptions, limitations, and a stated time frame. Trees without apparent defects can still fail, especially under unusual weather or changed site conditions."),
        ("Should the seller remove a risky tree before closing?", "That is a transaction decision. Compare seller-controlled work with a buyer-controlled credit, escrow, price change, closing condition, redesign, or termination, considering permits, access, scope, lender, insurer, and completion evidence."),
        ("Do tree cables or braces make a tree safe?", "Do not treat a support system as a guarantee. It needs professional design, installation, inspection, maintenance, and residual-risk review under the arborist's property-specific recommendation."),
        ("How often should an STR recheck its trees?", "Use the arborist's written interval and event triggers. Reassessment may be needed sooner after severe weather, fire, flooding, construction, root disturbance, nearby removals, impact, or a material change in targets or observed condition."),
    ],
    "related": [
        '<a href="/blog/landscaping-inspection-short-term-rental/">Review the broader landscape system</a>',
        '<a href="/blog/private-road-maintenance-agreement-before-buying-str/">Protect private-road access</a>',
        '<a href="/blog/wildfire-insurability-str/">Check wildfire insurability</a>',
        '<a href="/underwriting/">Model mitigation and downtime</a>',
        '<a href="/apply/">Discuss the acquisition strategy</a>',
    ],
    "cta_h": "Buying an STR with mature trees or wooded amenities?",
    "cta_p": "BNB Accelerator can help source and underwrite the property, coordinate diligence, and translate tree-risk findings into an acquisition and launch plan while qualified local professionals handle their conclusions.",
}


if __name__ == "__main__":
    blog.build([POST])
    print(f"candidate score: {sum(SCORE.values())}/100 — {SCORE}")
