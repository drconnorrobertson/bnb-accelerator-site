#!/usr/bin/env python3
"""Generate the Level 2 chimney-inspection guide for STR buyers."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import blog

DATE = "2026-09-24"
SCORE = {
    "distinct_search_intent": 30,
    "buyer_relevance": 24,
    "real_question": 15,
    "service_fit": 13,
    "original_decision_support": 14,
}
assert sum(SCORE.values()) == 96

CSIA_LEVEL2 = "https://web.csia.org/external/wcpages/wcmedia/documents/CSIA_Level2_MasonryChimney%20Revision%20Final.pdf"
CSIA_CERT = "https://www.csia.org/certification"
USFA_HEATING = "https://www.usfa.fema.gov/prevention/home-fires/prevent-fires/heating/"
CPSC_CO = "https://www.cpsc.gov/safety-education/safety-education-centers/carbon-monoxide-information-center/protect-your-family-from-carbon-monoxide-poisoning--"
CPSC_HEATING = "https://www.cpsc.gov/Safety-Education/Safety-Education-Centers/Carbon-Monoxide-Information-Center/Home-Heating-Equipment"
EPA_INSTALL = "https://www.epa.gov/burnwise/wood-burning-installation-and-maintenance"
EPA_FAQ = "https://www.epa.gov/burnwise/frequent-questions-about-wood-burning-appliances"
EPA_DATABASE = "https://cfpub.epa.gov/oarweb/woodstove/index.cfm"

POST = {
    "slug": "level-2-chimney-inspection-before-buying-str",
    "title": "Level 2 chimney inspections before buying an STR",
    "title_tag": "Level 2 Chimney Inspection Before Buying an STR",
    "h1": "Should you get a Level 2 chimney inspection before buying an STR?",
    "description": "Buying a cabin with a fireplace? Use this Level 2 chimney-inspection framework to define scope, interpret findings, price repairs, and plan guest use.",
    "date": DATE,
    "category": "Acquisition Diligence",
    "lead": "Order a qualified Level 2 chimney inspection during the purchase of an STR when the property has a chimney, fireplace, insert, wood or pellet stove, or another appliance vented through a chimney you may own or use. A general home inspection, a recent cleaning receipt, or a seller's statement that the fireplace works does not replace a defined chimney-system evaluation. The buyer needs a written scope covering every relevant flue and connected appliance, a video scan where the standard calls for one, documented access limits, repair priorities, and a clear decision about guest use before contingencies expire.",
    "sections": [
        ("The direct answer for an STR buyer", [
            f"Yes, if a chimney or connected hearth system is part of the property decision. The Chimney Safety Institute of America's <a href=\"{CSIA_LEVEL2}\" rel=\"noopener\">Level 2 masonry-chimney procedure</a> says this level is recommended when property is being sold and when use conditions change, an appliance is added or replaced with a dissimilar one, a flue will be relined, or an event may have damaged the chimney. It says a Level 2 includes the Level 1 elements plus accessible areas and a video scan of the chimney interior, with limitations documented when access or geometry prevents complete scanning.",
            "Do not translate that industry standard into a claim that every jurisdiction legally mandates the same inspection. NFPA standards, building and fire codes, manufacturer instructions, local ordinances, insurance requirements, and professional licensing rules interact differently by location. Ask the qualified chimney professional and local authority which current requirements apply to the address and proposed work.",
            ("callout", "Buying a cabin, historic house, ski property, or lake home with a fireplace or stove? <a href=\"/apply/\">Apply for a BNB Accelerator strategy call</a> to connect the chimney findings with the offer, repair reserve, insurance, renovation sequence, guest policy, and opening date. Qualified chimney, hearth, fire, structural, masonry, HVAC, legal, insurance, and code professionals must make their respective determinations."),
        ]),
        ("Do not collapse five different services into one", [
            "The word 'inspection' is used loosely in real-estate files. Ask exactly what was performed, under which standard, by whom, on which flues and appliances, and with what access. A receipt that says 'chimney service' cannot answer those questions.",
            ("table", ["Service or record", "Primary purpose", "Critical limitation"], [
                ["General home inspection", "Observe accessible home systems and flag concerns under the inspector's scope.", "Usually does not include a full interior flue video scan or specialist serviceability conclusion."],
                ["Chimney sweeping", "Remove specified deposits or obstructions from a defined flue or appliance path.", "Cleaning is not proof that the liner, clearances, masonry, appliance, or every flue is acceptable."],
                ["Level 1 inspection", "Evaluate readily accessible portions under continued-use conditions as defined by the applicable standard.", "Does not provide the expanded accessible-area and interior video scope associated with Level 2."],
                ["Level 2 inspection", "Evaluate the system for a sale, change, or event using expanded access and interior scanning within stated limits.", "Still cannot see every concealed condition and is not a guarantee against future failure."],
                ["Engineering, invasive, or repair investigation", "Resolve structural, concealed, design, code, or repair questions beyond the inspection scope.", "Needs a separately authorized scope, safety plan, and appropriately qualified professional."],
            ]),
            "Cleaning and inspection can occur during the same visit, but the report should distinguish them. If deposits prevent a meaningful scan, the professional may recommend cleaning and then completing or repeating the inspection. The buyer should not accept 'it was swept' as the final serviceability conclusion.",
        ]),
        ("Inventory every flue, appliance, and ownership boundary", [
            "Start with a system map. One masonry chimney can contain several flues serving different fireplaces or appliances. A factory-built fireplace has listed components and clearances that differ from a site-built masonry fireplace. A freestanding stove, insert, gas log set, furnace, boiler, or water heater may have its own venting system. An apparently abandoned opening can still matter if the flue, thimble, or combustible clearance remains part of the building.",
            ("ol", [
                "List every fireplace, stove, insert, gas log set, firebox, cleanout, thimble, vent connector, appliance, chimney stack, flue, cap, and termination the property appears to contain.",
                "Match each appliance to its vent path without guessing. Record fuel, manufacturer, model, listing label, installation date, manual, installer, permit, and alteration history when available.",
                "Identify shared walls, chases, attics, crawlspaces, mechanical rooms, roof areas, additions, and finished surfaces that control access or conceal system components.",
                "Confirm whether any chimney or flashing crosses a parcel, party wall, common element, condominium responsibility line, easement, or neighbor-controlled area with counsel and the relevant documents.",
                "Mark systems the seller says are decorative, disconnected, abandoned, unsafe, or never used; those labels need physical and documentary confirmation.",
                "Tell the inspector which appliances the STR plan will retain, replace, convert, relight, or decommission so the report addresses the intended condition of use.",
            ]),
            "Do not light an unknown fireplace or appliance as a buyer test. The qualified professional decides whether and how the system can be operated during evaluation. A cold visual condition may be the only safe starting point when history or serviceability is unknown.",
        ]),
        ("Build the pre-inspection record", [
            "Collect the history before the site visit so the inspector can target unresolved events and changes. The absence of records is not proof of a defect, but it changes confidence and may change the necessary scope.",
            ("ul", [
                "Prior chimney inspection and sweeping reports, including photographs, video files, measurement sheets, limitations, and technician identity.",
                "Appliance manuals, listing plates, installation instructions, permits, final inspections, invoices, warranties, liner records, and hearth or surround alterations.",
                "Insurance claims, fire-department responses, chimney-fire history, smoke or carbon-monoxide incidents, lightning, wind, tree impact, earthquake, roof leak, freeze, or masonry-repair records.",
                "Roof replacement, flashing, cricket, cap, crown, waterproofing, tuckpointing, rebuild, reline, damper, smoke-chamber, chase-cover, or connector work.",
                "Seller reports about odors, smoke spillage, poor draft, staining, fallen tile, water entry, animal nesting, unusual appliance shutdowns, or rooms that become smoky.",
                "Rental rules, insurance requirements, local fire inspection checklists, prior operating instructions, cleaning logs, and any decision to restrict guest use.",
            ]),
            "Cross-reference this file with the <a href=\"/blog/clue-report-before-buying-str/\">property claim-history report</a>. A reported fire, smoke, roof, wind, water, or lightning loss can justify focused questions even when the chimney was not named in the claim summary. The underlying adjuster and repair records matter more than a category label.",
        ]),
        ("Define the Level 2 scope in writing", [
            f"CSIA's procedure says Level 2 access can include the roof and accessible attics, basements, and crawlspaces, and it calls for video scanning or a similar inspection of the chimney interior. It also says exceptions should be reported when an area cannot be accessed or the flue cannot be scanned because of size or offsets. Those limitations are acquisition facts, not fine print to ignore.",
            ("table", ["Scope element", "What the buyer should request", "Why it changes the decision"], [
                ["Systems covered", "Every named flue, fireplace, chimney, connector, and connected appliance—or an explicit excluded list.", "A report on the living-room fireplace may say nothing about a second flue or mechanical appliance."],
                ["Access", "Accessible exterior, roof, attic, crawlspace, basement, chase, cleanouts, appliance areas, and concealed-area limits.", "Finished construction, roof conditions, snow, height, or safety constraints can leave material uncertainty."],
                ["Interior scan", "Recorded or captured images tied to location, direction, flue, and finding, with scan limitations.", "A buyer needs traceable evidence rather than a verbal statement that a camera was used."],
                ["Condition findings", "Deposits, obstruction, liner, joints, offsets, moisture, masonry, metal, clearances, connector, firebox, smoke chamber, damper, cap, crown, flashing, support, and appliance concerns within scope.", "Different findings require different professionals, urgency, and repair paths."],
                ["Use conclusion", "Written recommendation for continued use, cleaning, repair, further evaluation, decommissioning, or no operation pending work.", "The STR team needs a defensible operating status, not a vague list of defects."],
                ["Standards and limits", "Standard and edition used, local-code assumptions, inaccessible components, destructive work excluded, and conditions that could change the result.", "A report is only as broad as its declared basis and access."],
            ]),
            f"Check individual credentials, experience, insurance, report quality, and independence. The <a href=\"{CSIA_CERT}\" rel=\"noopener\">CSIA certification page</a> describes its certified chimney-sweep credential as testing knowledge of chimney and venting evaluation and maintenance. A credential supports qualification; it does not erase the need to review scope, conflicts, local licenses, references, or fuel-specific expertise.",
        ]),
        ("Translate findings into decision categories", [
            "Do not reduce the report to pass or fail unless the professional and governing framework actually use those terms. Classify each finding by system, consequence, required professional, permission to operate, next evidence, cost path, and deadline.",
            ("table", ["Finding category", "Acquisition response", "Operating status"], [
                ["Routine service or deposits", "Complete specified cleaning or maintenance, document reinspection if needed, and set recurring service interval.", "Use only after the qualified professional states service conditions are satisfied."],
                ["Localized repair with defined scope", "Obtain matched bids, permits if required, compatible materials, inspection criteria, and warranty.", "Keep offline until the professional's stated repair and acceptance steps are complete."],
                ["Liner, clearance, support, or concealed concern", "Bring in the appropriate chimney specialist, mason, engineer, hearth professional, or code official; define any invasive access.", "No guest use while serviceability remains unresolved."],
                ["Appliance or vent mismatch", "Verify listing and manufacturer instructions; price replacement, reconfiguration, dedicated venting, or decommissioning.", "Do not assume a new appliance can connect to the old path."],
                ["Water entry or exterior deterioration", "Coordinate chimney masonry, cap/crown, flashing, roof, drainage, and interior moisture assessment as one causal scope.", "Treat active leakage and damaged material separately from combustion use."],
                ["System will not be offered to guests", "Permanently and safely decommission, block access, remove misleading listing claims, and preserve documentation as professionals require.", "A sign saying 'do not use' is not a physical or insurance control by itself."],
            ]),
        ]),
        ("Worked example: a two-flue mountain cabin", [
            "Assume an illustrative buyer is evaluating a mountain cabin with a living-room masonry fireplace and an upstairs opening where a wood stove was removed. The seller supplies a two-year-old sweeping invoice for 'main fireplace.' The general inspection photographs the firebox and roofline but excludes internal flue condition. The STR plan highlights the fireplace as a winter amenity.",
            "The buyer commissions a qualified Level 2 scope for both flues, the fireplace, the former stove connection, accessible masonry, roof, attic, and crawlspace. The report documents its video route and access limits. Suppose the professional identifies a displaced liner joint in the active flue, an incompletely closed former thimble upstairs, and moisture staining near the roof penetration. The report directs no operation pending defined follow-up.",
            "The buyer obtains a liner or repair evaluation from the appropriate chimney specialist, a masonry and flashing scope coordinated with the roofer, and confirmation of the lawful method for the abandoned opening. Matched bids separate known work from change-order triggers. The insurer receives the report, intended guest use, planned repair, and final documentation requirements. The revenue model assumes no fireplace until every dependency is cleared.",
            "If the completed scope, schedule, insurance terms, and conservative reserve fit the acquisition, the buyer can negotiate from evidence. If hidden extent remains open-ended or the fireplace is central to the revenue thesis and cannot be offered, the buyer reruns the deal without the amenity or uses the contract remedy. This cabin and findings are illustrative—not a client result or inspection conclusion.",
        ]),
        ("Price the repair as a system, not a line item", [
            "A quote to install a liner or repair masonry may exclude access, scaffolding, roof protection, demolition, combustible-clearance correction, appliance work, electrical or gas work, permits, design, engineering, interior finish removal, water-damage repair, painting, disposal, final inspection, or restoration. Require comparable scopes and make concealed-condition triggers explicit.",
            ("ol", [
                "Tie every bid item to a report finding, exact chimney/flue/appliance, drawing or photograph, and responsible trade.",
                "State listed system, material, dimensions, compatibility, manufacturer instructions, code basis, permit path, and inspection responsibility where applicable.",
                "Separate safety or serviceability work from optional efficiency, cosmetic, or amenity upgrades so the decision does not hide the minimum viable scope.",
                "Define access, fall protection, staging, weather limits, occupant protection, dust and debris controls, adjacent finishes, utilities, and property restoration.",
                "List assumptions and unit prices or decision gates for concealed deterioration, liner removal, masonry rebuild, chase access, structural support, roof work, and unavailable components.",
                "Define completion evidence: permits, final inspections, photographs, product records, warranties, test or commissioning results, and qualified post-repair inspection as applicable.",
            ]),
            "Move cost, downtime, guest-use restrictions, financing delay, carrying expense, and reserve into the <a href=\"/underwriting/\">acquisition model</a>. If the listing strategy depends on fireplace photography and winter guest use, also model the downside case with the amenity permanently removed or unavailable for the first season.",
        ]),
        ("Clear code, insurance, and contract dependencies", [
            "Ask the local building and fire authorities which permits, adopted codes, inspections, disclosure rules, solid-fuel restrictions, air-quality rules, and STR fire-safety requirements apply. Existing construction, historic status, appliance replacement, fuel conversion, relining, structural repair, and decommissioning can follow different paths. The inspection report does not issue a permit or approve a design.",
            "Send the actual system description, report, intended STR use, guest access, planned repairs, renovation period, and completion documents to the insurance professional. Ask whether wood burning, fireplaces, stoves, pellet appliances, gas logs, age, type, claims history, protective devices, vacancy, or contractor work affects eligibility, premium, deductible, inspection, exclusions, warranties, or required endorsements. Only the actual carrier and policy answer the coverage question.",
            "Use counsel to align the chimney decision with inspection, insurance, financing, title, and repair provisions. Seller-completed work can reduce the buyer's post-closing project but gives the seller schedule and contractor control. A credit gives the buyer control but does not make a hidden defect finite or guarantee insurance. Escrow needs a defined scope, adequate funding, access, completion criteria, overrun allocation, lender and title approval, and a remedy if work cannot close.",
        ]),
        ("Turn a cleared fireplace into an STR operating system", [
            f"Annual service is the floor, not the complete guest plan. The <a href=\"{USFA_HEATING}\" rel=\"noopener\">U.S. Fire Administration</a> advises having chimneys cleaned and inspected by a professional each year and keeping items that can burn at least three feet from heat sources. The <a href=\"{CPSC_CO}\" rel=\"noopener\">Consumer Product Safety Commission</a> recommends annual service of chimneys and vents and carbon-monoxide alarms on every level and outside sleeping areas.",
            f"EPA's historic <a href=\"{EPA_INSTALL}\" rel=\"noopener\">wood-burning installation and maintenance guidance</a> highlights clearances, floor protection, assembly, vent sizing, height, location, and configuration. Its <a href=\"{EPA_FAQ}\" rel=\"noopener\">wood-burning FAQ</a> explains that creosote is combustible and can build when smoke condenses in a cooler chimney. EPA certification applies to specified manufactured wood heaters, not to a whole chimney or every fireplace; buyers can check qualifying models in the <a href=\"{EPA_DATABASE}\" rel=\"noopener\">EPA-certified wood-heater database</a> when relevant.",
            ("ul", [
                "Decide whether guests may use the appliance at all; confirm the choice with the carrier, local rules, manager, cleaner, and maintenance provider.",
                "If use is allowed, provide fuel- and appliance-specific instructions, permitted fuel, damper and screen controls, occupancy supervision, shutdown, ash handling, and emergency steps approved by qualified professionals.",
                "Control the fuel supply and remove prohibited materials, accelerants, loose paper, decorative combustibles, and ambiguous tools from the guest-use area.",
                "Maintain required smoke and carbon-monoxide alarms, extinguishers, hearth protection, clearances, screens or doors, address visibility, and emergency contacts under local rules and manufacturer direction.",
                "Schedule professional inspection, cleaning, and service based on use, findings, manufacturer instructions, insurer conditions, and local requirements—not merely the calendar year.",
                "Create an immediate lockout trigger for smoke spillage, alarm activation, unusual odor, visible damage, water entry, debris, animal activity, guest misuse, or any chimney-fire suspicion.",
            ]),
            "A decorative disclaimer in the listing does not control physical access. If the system is not approved for guest use, use a professional decommissioning or access-control solution and remove amenity claims and staged fire images that imply availability.",
        ]),
        ("Failure modes that create false confidence", [
            ("ul", [
                "Treating the home inspector's firebox photo as an interior chimney evaluation.",
                "Treating a sweeping receipt as proof of liner condition, clearances, structural integrity, appliance compatibility, or every flue.",
                "Ordering a Level 2 inspection for one fireplace while ignoring other flues or connected appliances in the chimney.",
                "Accepting a verbal camera result without traceable images, system identification, limitations, or a written use recommendation.",
                "Saying a system 'passes NFPA' without naming the standard edition, adopted local code, exact scope, or professional conclusion.",
                "Letting a repair bidder redefine the inspection problem without comparing scope or addressing conflicts and qualifications.",
                "Pricing only the liner or masonry item while omitting access, roof, structural, permit, interior, appliance, and restoration dependencies.",
                "Assuming insurance accepts guest fireplace use because the seller had a homeowners policy.",
                "Advertising or unlocking the fireplace before repairs, documentation, coverage, operating controls, and recurring service are complete.",
            ]),
            ("warn", "This guide summarizes fire-safety, consumer-product, environmental, and chimney-industry sources reviewed September 24, 2026. It is educational, not fire-safety, chimney, engineering, masonry, HVAC, environmental, legal, insurance, code, medical, contracting, or investment advice. Standards, adopted codes, inspection levels, professional licensing, permits, appliance instructions, and STR rules vary. Use qualified local professionals and current source documents."),
        ]),
        ("Turn the report into a go, renegotiate, or walk decision", [
            "Proceed when every relevant system has a defined scope and access record, findings and limitations are understood, necessary specialists agree on an executable repair or decommissioning path, insurance and local requirements are addressed, completion evidence is defined, and the conservative cost and schedule fit. Renegotiate when a bounded repair or loss of amenity changes price or launch timing. Walk when access is refused, material systems remain uninspected, concealed downside cannot be controlled, or the investment only works if an uncleared fireplace is offered to guests.",
            "Pair this workflow with the <a href=\"/blog/str-fire-inspection-closing/\">STR fire-inspection guide</a>, the <a href=\"/blog/roof-inspection-short-term-rental/\">roof inspection guide</a>, the <a href=\"/blog/mold-inspection-before-buying-str/\">moisture assessment guide</a>, and the <a href=\"/blog/inspection-contingency-length-str/\">inspection-contingency timeline</a>. A chimney report does not replace those separate decisions.",
            "The practical next step is to inventory all flues and appliances, collect the history, identify the intended post-closing use, and obtain a written Level 2 scope from a qualified local professional before the inspection window becomes too short to investigate findings.",
            ("callout", "Need fireplace or chimney risk translated into an offer, repair reserve, insurance plan, and guest-use decision? <a href=\"/apply/\">Apply for a BNB Accelerator strategy call</a>. We can coordinate the acquisition framework while qualified chimney, fire, structural, masonry, HVAC, insurance, legal, and code professionals handle their conclusions."),
        ]),
    ],
    "faqs": [
        ("What is a Level 2 chimney inspection?", "It is an expanded chimney-system evaluation used for circumstances such as a property sale or change in use. CSIA's procedure includes Level 1 elements, accessible areas such as roof and attic where safe, and an interior video scan or similar method, with limitations documented."),
        ("Does every home sale legally require a Level 2 chimney inspection?", "Do not assume so. NFPA standards, adopted codes, local laws, contract terms, insurer requirements, and professional recommendations vary. Confirm what applies to the property with qualified local professionals and officials."),
        ("Is chimney sweeping the same as a Level 2 inspection?", "No. Sweeping removes specified deposits or obstructions. A Level 2 inspection evaluates defined accessible components and includes an interior scan within its scope. Cleaning may be needed before a useful scan, but one service does not substitute for the other."),
        ("Does a general home inspection include a chimney camera scan?", "Often it does not, but scope varies. Read the agreement and report. If the purchase decision includes a chimney or hearth appliance, commission the appropriate specialist inspection rather than assuming a general inspection covered it."),
        ("Should an STR let guests use a fireplace after it passes inspection?", "Inspection is only one dependency. Guest use also depends on local rules, insurer approval, appliance and manufacturer requirements, alarms and fire controls, operating procedures, manager capacity, maintenance, and the owner's risk decision."),
        ("What if the chimney cannot be fully scanned?", "Require the report to state which areas or flues were not scanned, why, and what further access or evaluation is recommended. Treat the unresolved area as uncertainty in the contract and underwriting rather than assuming it is acceptable."),
    ],
    "related": [
        '<a href="/blog/str-fire-inspection-closing/">Build the complete STR fire-safety file</a>',
        '<a href="/blog/roof-inspection-short-term-rental/">Coordinate chimney and roof findings</a>',
        '<a href="/blog/clue-report-before-buying-str/">Reconcile prior insurance claims</a>',
        '<a href="/underwriting/">Model repairs and downtime</a>',
        '<a href="/apply/">Discuss the acquisition strategy</a>',
    ],
    "cta_h": "Buying an STR with a fireplace, stove, or chimney?",
    "cta_p": "BNB Accelerator can help source and underwrite the property, coordinate the diligence file, and translate chimney findings into an acquisition and guest-use plan while qualified local professionals handle fire, structural, code, insurance, and repair conclusions.",
}


if __name__ == "__main__":
    blog.build([POST])
    print(f"candidate score: {sum(SCORE.values())}/100 — {SCORE}")
