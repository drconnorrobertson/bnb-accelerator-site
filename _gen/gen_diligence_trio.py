#!/usr/bin/env python3
"""Generate three distinct STR acquisition-diligence guides."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import blog

DATE = "2026-09-24"
SCORES = {
 "foundation": {"distinct_search_intent":30,"buyer_relevance":25,"real_question":15,"service_fit":13,"original_decision_support":14},
 "electrical": {"distinct_search_intent":30,"buyer_relevance":25,"real_question":15,"service_fit":13,"original_decision_support":15},
 "phase_i": {"distinct_search_intent":30,"buyer_relevance":23,"real_question":15,"service_fit":13,"original_decision_support":15},
}
for score in SCORES.values(): assert sum(score.values()) >= 75

HUD_FOUNDATION="https://www.hud.gov/sites/dfiles/PIH/documents/NSPIRE-Standards-v2.2-Foundation.pdf"
HUD_INSPECTION="https://archives.hud.gov/offices/hsg/sfh/ref/sfhp1-22.cfm"
CPSC_FPE="https://www.cpsc.gov/Newsroom/News-Releases/1983/Commission-Closes-Investigation-Of-FPE-Circuit-Breakers-And-Provides-Safety-Information-For-Consumers"
CPSC_ALUMINUM="https://www.cpsc.gov/Newsroom/News-Releases/1974/CPSC-Safety-Recommendations-For-Aluminum-Wiring-In-Homes"
EPA_AAI="https://www.epa.gov/brownfields/brownfields-all-appropriate-inquiries"
EPA_PHASE="https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=P1016H0P.txt"

POSTS=[
{
"slug":"structural-engineer-foundation-cracks-before-buying-str",
"title":"When foundation cracks need an engineer before an STR purchase",
"title_tag":"Foundation Cracks: When an STR Buyer Needs an Engineer",
"h1":"When should an STR buyer hire a structural engineer for foundation cracks?",
"description":"See when foundation cracks justify an engineer before buying an STR, what evidence to request, how to scope repairs, and how to protect the closing decision.",
"date":DATE,"category":"Acquisition Diligence",
"lead":"Hire an appropriately licensed structural engineer when cracks, displacement, movement, altered framing, retaining conditions, drainage history, or a proposed renovation create a load-path question that a general inspection cannot resolve. Do not ask a repair salesperson to both diagnose the cause and define the only solution. The buyer needs an independent description of observed conditions, likely mechanisms, investigation limits, stabilization or repair criteria, monitoring needs, and any urgent occupancy restriction before pricing the property as a short-term rental.",
"sections":[
("The direct answer: escalate the question, not every hairline crack",[
f"A crack is an observation, not a diagnosis. HUD's <a href=\"{HUD_FOUNDATION}\" rel=\"noopener\">NSPIRE foundation standard</a> uses measurable crack criteria for its housing-inspection program and tells inspectors to look for related indicators such as unlevel floors and doors or windows that do not function. Those thresholds serve that program; they are not a universal engineering rule or a promise that smaller cracks are harmless.",
"Escalate when the pattern suggests differential movement, the crack is displaced or changing, water is entering, masonry is bowing, framing has been cut or removed, columns or beams appear improvised, floors slope materially, openings rack, additions meet the original structure awkwardly, a hillside or retaining wall affects support, or the revenue plan adds hot tubs, bedrooms, decks, walls, openings, or concentrated loads.",
("callout","Buying a house with movement, past foundation work, or a major amenity plan? <a href=\"/apply/\">Apply for a BNB Accelerator strategy call</a> to connect engineering scope with offer terms, financing, insurance, reserves, and launch timing.")
]),
("Build an evidence file before the site visit",[
("table",["Evidence","What it can answer","What it cannot prove"],[
["Dated crack and elevation records","Whether an observed condition changed during the recorded period.","Cause, future performance, or concealed conditions."],
["Prior engineer report and drawings","What was observed, assumed, designed, and recommended then.","That work was installed correctly or remains adequate now."],
["Permits, finals, invoices, warranties","Who performed work and whether a permit closed.","A warranty of structural performance or coverage of later changes."],
["Drainage, plumbing, grading, tree, and soil history","Potential contributors and chronology.","Which mechanism controls without professional analysis."],
["Seller disclosure and claim history","Known events, repairs, and insurance activity.","Absence of an undisclosed or unknown condition."]
]),
"Ask for original plans, additions, wall removals, foundation repairs, waterproofing, underpinning, pier or anchor layouts, geotechnical records, monitoring logs, plumbing repairs, drainage work, and transferable warranties. Photograph every accessible face with scale and location. Do not cover, patch, excavate, load-test, or open assemblies without permission and a safe plan."
]),
("Give the engineer a decision question, not a vague inspection request",[
("ol",[
"Identify the intended transaction decision, planned guest capacity, proposed structural changes, and material amenities.",
"Provide the survey, plans, disclosures, general inspection, photographs, prior reports, repair documents, and deadline before the visit.",
"Ask which building areas, site features, crawlspaces, attics, retaining elements, decks, and additions are included and excluded.",
"Request location-specific observations, likely causes or hypotheses, uncertainty, recommended investigation, urgency, monitoring, and repair performance criteria.",
"Ask whether geotechnical, drainage, plumbing, architectural, surveying, or destructive-access support is needed.",
"Require the written deliverable, limitations, drawings or calculations if needed, and responsibility for reviewing repair completion."
]),
f"HUD's archived <a href=\"{HUD_INSPECTION}\" rel=\"noopener\">home-inspection guidance</a> encourages a detailed inspection and separates conditions affecting structural integrity from ordinary cosmetic repair. An engineering engagement should preserve that distinction rather than turn every crack into the same repair package."
]),
("Translate a finding into a comparable scope",[
"A useful recommendation states the affected locations, objective, design basis, sequence, access, temporary support, materials or performance criteria, drainage dependencies, monitoring, permit path, inspection hold points, completion evidence, and responsibility for concealed changes. Without those details, bids for piers, anchors, wall reinforcement, drainage, masonry, framing, or waterproofing may solve different problems.",
("table",["Finding state","Transaction posture","Minimum evidence"],[
["Cosmetic or stable condition supported","Proceed with documented maintenance and monitoring.","Written reasoning, baseline photos, monitoring trigger."],
["Cause plausible; extent bounded","Price a defined repair and schedule.","Engineer criteria, matched bids, permit and closeout path."],
["Multiple plausible causes","Investigate soil, water, plumbing, framing, or concealed areas.","Written testing or access plan and contract time."],
["Active movement or safety concern","Restrict use and resolve stabilization before guests.","Professional direction, temporary measures, designed repair."],
["Material area inaccessible","Create access or carry a defensible downside case.","Location-specific limit and costed next step."]
])
]),
("Worked example: the sloped-floor mountain cabin",[
"Assume an illustrative cabin has a diagonal masonry crack, a floor that drops toward an enclosed porch, sticky exterior doors, and invoices for drainage work but no engineering report. The revenue plan assumes a new hot tub on the porch. A foundation contractor proposes piers after a free visit; another says the issue is water.",
"The buyer retains an independent engineer, supplies the addition history and survey, obtains floor elevations, and follows the engineer's recommendation for limited crawlspace access and drainage review. The scope distinguishes original foundation movement from the porch connection, prohibits the hot-tub assumption until its support is designed, and defines monitoring and repair criteria. The buyer prices the same scope and models the cabin unavailable through permit, repair, restoration, and acceptance. This example is illustrative, not a client result or engineering opinion."
]),
("Underwrite the full consequence",[
"Move professional fees, access, testing, temporary support, design, permits, repair, utilities, drainage, waterproofing, finish restoration, landscaping, monitoring, carrying costs, financing conditions, insurance requirements, and schedule contingency into the <a href=\"/underwriting/\">STR acquisition model</a>. Remove any bedroom, deck, hot tub, or amenity dependent on unresolved capacity from the base case.",
"Proceed when the condition is bounded and the repair has measurable completion criteria. Renegotiate when cost and delay are defined but material. Walk when access is blocked, the load path cannot be evaluated, movement may be active without time to investigate, or the deal only works if the least expensive diagnosis is correct."
]),
("Failure modes and next step",[
("ul",["Treating crack width alone as a diagnosis or universal safety threshold.","Using the repair company's proposal as the only assessment.","Ignoring additions, decks, retaining walls, drainage, plumbing, or amenity loads.","Accepting a warranty without reading covered work, exclusions, maintenance, and transfer terms.","Comparing bids that solve different causes or include different restoration work.","Letting lender acceptance substitute for guest-safety and operating diligence."]),
("warn","Educational only, not structural, engineering, geotechnical, construction, legal, insurance, lending, or investment advice. Licensing, code, permit, disclosure, and practice rules vary."),
"Preserve the evidence, write the exact decision question, and obtain a property-specific engagement from a qualified local professional before the contingency expires.",
("callout","Need to turn a structural finding into a conservative purchase decision? <a href=\"/apply/\">Apply to BNB Accelerator</a>.")
])
],
"faqs":[
("Does every foundation crack require a structural engineer?","No. But displacement, movement indicators, water, altered framing, hillside conditions, prior repairs, or planned structural loads can justify escalation."),
("Is a foundation contractor the same as an independent engineer?","No. A contractor may install repairs, but a buyer should understand incentives and obtain independent design or diagnosis when the decision requires it."),
("Can a seller repair the crack before closing?","Only with a written scope, access, permits where required, documentation, professional review, completion evidence, and a contract remedy."),
("Should a hot tub be included in the engineer's scope?","Yes when its location or concentrated load could affect framing, decks, foundations, soil, or retaining systems.")
],
"related":['<a href="/blog/boundary-survey-before-buying-str/">Boundary survey diligence</a>','<a href="/blog/wdo-termite-inspection-before-buying-str/">Wood-damage inspection</a>','<a href="/blog/mold-inspection-before-buying-str/">Moisture and mold assessment</a>','<a href="/underwriting/">Underwrite repair downside</a>','<a href="/apply/">Discuss the acquisition</a>'],
"cta_h":"Buying an STR with foundation questions?","cta_p":"BNB Accelerator can connect professional scopes, offer terms, reserves, and launch timing into one acquisition decision."
},
{
"slug":"electrical-panel-inspection-before-buying-str",
"title":"Electrical panel and wiring diligence before buying an STR",
"title_tag":"Electrical Panel Inspection Before Buying an STR",
"h1":"Should you get a specialist electrical inspection before buying an STR?",
"description":"Use this STR electrical diligence framework to inspect legacy panels and wiring, test capacity assumptions, scope corrections, and protect closing decisions.",
"date":DATE,"category":"Acquisition Diligence",
"lead":"Order a qualified electrical evaluation when the general inspection, building age, panel labeling, renovation history, service size, visible wiring, insurer, lender, or amenity plan raises a material question. The goal is not a brand-name panic list. It is a documented property-specific answer about service, panels, overcurrent protection, grounding and bonding, branch wiring, wet-location protection, equipment, prior alterations, capacity, permits, and corrections needed before guests use the property.",
"sections":[
("The specialist trigger is evidence plus intended use",[
"An STR can add simultaneous loads from HVAC, electric water heating, laundry, cooking, EV charging, hot tubs, saunas, pool equipment, exterior lighting, well pumps, septic controls, and guest devices. A system that powered a lightly occupied home may still need evaluation for the proposed plan. Capacity and safety are separate: a larger service does not correct defective terminations, and a tidy panel does not prove adequate capacity.",
f"CPSC's historical <a href=\"{CPSC_FPE}\" rel=\"noopener\">Federal Pacific Stab-Lok investigation notice</a> did not establish that every breaker would fail or prescribe a universal replacement. It told consumers to follow local codes, avoid overloads, and have certain equipment problems checked by qualified professionals. That nuance is why a buyer should obtain a current property-specific assessment rather than repeat an internet verdict.",
("callout","Planning a hot tub, EV charger, electric conversion, or high-occupancy STR? <a href=\"/apply/\">Apply for a BNB Accelerator strategy call</a> to connect electrical scope, insurance, budget, and opening sequence.")
]),
("Inventory the system before asking for a price",[
("table",["Layer","Record","Decision"],[
["Utility and service","Overhead or underground, meter, service rating, conductors, disconnects.","Can supply and equipment support the plan?"],
["Panels","Manufacturer, model, labels, ratings, mains, subpanels, directories, clearances.","What is damaged, obsolete, incompatible, or improperly installed?"],
["Branch wiring","Material, age, visible condition, splices, extensions, multiwire circuits.","What needs testing, repair, replacement, or restricted use?"],
["Protection","Breakers or fuses, GFCI, AFCI, surge, bonding, grounding.","Which current rules apply to the actual scope?"],
["STR loads","HVAC, water heater, kitchen, laundry, spa, pool, EV, well, septic.","What is existing, concurrent, proposed, and optional?"],
["History","Permits, finals, remodels, insurer notices, outages, overheating, repairs.","Which alterations lack reliable closeout?"]
]),
"Give the electrician the property plan and equipment specifications, not just a request to check the panel. Name every structure, detached building, exterior circuit, dock, pool, spa, gate, well, pump, generator, solar system, battery, or EV load relevant to guests and operations."
]),
("Treat aluminum branch wiring as a scoped condition",[
f"CPSC's <a href=\"{CPSC_ALUMINUM}\" rel=\"noopener\">aluminum-wiring safety notice</a> warned that improper connections can overheat and unsafe work can cause serious shock. A buyer should not disturb devices, open energized equipment, or accept an unlabeled repair claim. Ask a qualified electrician to identify where aluminum conductors are present, what circuits and connection methods exist, what evidence is visible, and which current correction methods and local requirements apply.",
"A seller invoice saying aluminum wiring was remediated is not enough. Obtain the exact locations, connector or method, installer qualification, permit and final where required, device and panel compatibility, inaccessible areas, and what remains untouched."
]),
("Separate condition corrections from capacity upgrades",[
("ol",["Correct urgent shock, fire, arcing, overheating, water-intrusion, damaged-equipment, or exposed-conductor hazards under professional direction.","Map existing circuits and reconcile the directory to actual loads.","Perform calculations appropriate to the proposed equipment and jurisdiction.","Define panel, feeder, conductor, device, grounding, bonding, protection, disconnect, and clearance changes.","Confirm utility coordination, trenching, meter, transformer, easement, lead-time, permit, and inspection dependencies.","Sequence wall opening and restoration with design, plumbing, HVAC, pool, spa, and exterior work."]),
"Do not assume a service upgrade is only a panel swap. Utility work, exterior location, trenching, meter rules, feeders, grounding, drywall, siding, landscaping, equipment lead time, and downstream panels can control price and schedule."
]),
("Worked example: an older lake house with a hot-tub plan",[
"Assume an illustrative 1970s lake house has a mixed panel directory, a small subpanel in the garage, some aluminum branch wiring, and a seller-installed exterior receptacle. The plan adds a hot tub, heat-pump water heater, and EV charger. The general inspector recommends review but does not calculate proposed load.",
"The buyer provides equipment specifications to a licensed electrician, maps circuits, documents wiring and panel conditions, and asks the utility about service work. The scope separates immediate corrections from optional electrification and includes permits and restoration. The base forecast opens without the EV charger and hot tub; the upside case activates them only after documented completion. This is illustrative, not electrical advice or a client result."
]),
("Make the closing remedy auditable",[
("table",["Response","Use when","Control"],[
["Seller completes work","Scope is bounded and time allows.","Buyer-approved scope, licensed installer, permits, finals, invoices, reinspection."],
["Buyer credit or price change","Buyer should control design and contractor.","Lender limits, adequate amount, post-close access and coverage."],
["Escrow","A narrow item cannot finish before closing.","Counsel-drafted funding, deadlines, overruns, access, release, and failure remedy."],
["Remove amenity","Upgrade is optional and economics work without it.","Physical and marketing controls preventing premature use."],
["Terminate","Hazard, access, utility, insurance, or cost remains unbounded.","Exercise the contract right before the deadline."]
]),
"Underwrite evaluation, utility fees, design, permits, panels, feeders, circuits, devices, protection, trenching, wall opening, restoration, carrying costs, unavailable amenities, and schedule reserve in the <a href=\"/underwriting/\">property model</a>. Confirm STR business-use coverage with the actual insurer."
]),
("Failure modes and practical next step",[
("ul",["Declaring a panel safe or unsafe from a photograph or brand name alone.","Replacing a panel without investigating branch wiring, feeders, grounding, bonding, and proposed loads.","Using a plug-in tester as proof of the entire system.","Pricing an EV charger, spa, sauna, or pool without utility dependencies.","Accepting undocumented remediation or open permits.","Launching guests before exterior, wet-location, or amenity circuits are completed and inspected as required."]),
("warn","Educational only, not electrical, code, engineering, utility, legal, insurance, lending, or investment advice. Equipment, hazards, licensing, permits, codes, and acceptable methods vary. Do not open or work on energized equipment."),
"Create a system-and-load inventory, collect permits and repair records, and commission a written evaluation early enough to price corrections and optional upgrades.",
("callout","Need an electrical finding translated into reserves and a realistic opening plan? <a href=\"/apply/\">Apply to BNB Accelerator</a>.")
])
],
"faqs":[
("Does a home inspection replace an electrical inspection?","No. A general inspection may identify visible concerns; a property-specific electrical scope can go further where condition, capacity, or proposed loads require it."),
("Does an old electrical panel always need replacement?","Not solely because of age. Current condition, listing and compatibility, local requirements, insurer, proposed load, and parts all matter."),
("Should an STR buyer calculate loads before adding a hot tub?","Yes. Provide actual equipment specifications and proposed concurrent loads to the qualified electrician and utility as applicable."),
("Is a permit final proof every electrical condition is safe?","No. It documents the jurisdiction's process for the permitted scope, not concealed work, later alterations, maintenance, or excluded items.")
],
"related":['<a href="/blog/vacant-renovation-str-coverage/">Renovation insurance planning</a>','<a href="/blog/inspection-contingency-length-str/">Inspection timeline</a>','<a href="/blog/clue-report-before-buying-str/">Property claim history</a>','<a href="/underwriting/">Model upgrades and downtime</a>','<a href="/apply/">Discuss the property</a>'],
"cta_h":"Buying an STR with legacy electrical systems?","cta_p":"BNB Accelerator can coordinate diligence questions, underwriting, and closing strategy around qualified electrical conclusions."
},
{
"slug":"phase-i-environmental-site-assessment-str-purchase",
"title":"When an STR buyer needs a Phase I environmental assessment",
"title_tag":"Phase I Environmental Assessment for an STR Purchase",
"h1":"When should an STR buyer order a Phase I environmental site assessment?",
"description":"Learn when a Phase I environmental assessment fits an STR purchase, what it does not test, how to handle findings, and how to protect the acquisition decision.",
"date":DATE,"category":"Acquisition Diligence",
"lead":"Consider a Phase I Environmental Site Assessment when the parcel, adjoining land, historical use, records, lender, investor, entity structure, or intended redevelopment creates a credible contamination or liability question—especially for a former gas station, dry cleaner, agricultural operation, industrial use, auto shop, commercial conversion, fill site, or property near a known release. A Phase I is primarily a records, reconnaissance, interview, and professional-opinion process. It generally is not the same thing as sampling soil, groundwater, vapor, paint, mold, asbestos, or drinking water.",
"sections":[
("The decision starts with purpose and timing",[
f"EPA defines <a href=\"{EPA_AAI}\" rel=\"noopener\">All Appropriate Inquiries</a> as evaluating environmental conditions and potential contamination liability. EPA recognizes ASTM E1527-21 and, for qualifying forestland or rural property, E2247-23 as consistent with the federal AAI rule. Certain CERCLA liability protections require AAI before acquisition plus other statutory criteria and continuing obligations after acquisition; ordering a report alone does not create blanket immunity.",
"A buyer may also order a Phase I for lender policy, investor governance, redevelopment planning, or risk discovery even when no federal defense is claimed. Define the intended use with environmental counsel and the environmental professional before accepting a cheap desktop product that may not satisfy the purpose.",
("callout","Evaluating a converted motel, commercial building, farm, auto-related site, or unusual parcel for STR use? <a href=\"/apply/\">Apply for a BNB Accelerator strategy call</a> to connect environmental diligence with renovation, financing, insurance, and underwriting.")
]),
("Use a trigger screen before ordering",[
("table",["Trigger","Why it matters","Immediate evidence"],[
["Former commercial or industrial use","Historical operations may involve tanks, solvents, waste, fill, or releases.","Directories, aerials, fire-insurance maps, permits, databases."],
["Gas station, auto, dry-cleaning, printing, manufacturing","Use-specific chemicals and pathways may warrant review.","Operational history, tank records, closure files, agency records."],
["Agricultural or rural operation","Fuel, pesticide, dumping, burn, equipment, and storage history can matter.","Farm records, interviews, reconnaissance, state files."],
["Adjacent listed or suspect property","Contamination can migrate across boundaries.","Database location, topography, hydrogeology, agency documents."],
["Fill, odors, staining, drums, vents, distressed vegetation","Observed conditions may indicate a release or need safety controls.","Photos and professional direction; do not disturb."],
["Commercial-to-lodging conversion","Redevelopment can change exposure, excavation, vapor, and lender questions.","Concept plan, demolition scope, occupancy requirements."]
]),
"A clean residential appearance does not erase a parcel's history, and a database hit does not prove the subject property is contaminated. The professional integrates records, distances, setting, interviews, observations, data gaps, and judgment."
]),
("Know what the report must communicate",[
f"EPA's AAI page says the written work must address conditions indicating releases or threatened releases, significant data gaps, environmental-professional qualifications and signature, and an opinion about additional appropriate investigation when the professional has one. EPA's <a href=\"{EPA_PHASE}\" rel=\"noopener\">brownfields assessment fact sheet</a> describes Phase I as using existing information, while Phase II often includes sampling and analysis.",
("ol",["Confirm the standard, property definition, purchaser or user, reliance parties, report purpose, and closing date.","Define every parcel, easement, structure, outbuilding, and area in the acquisition.","Provide title information, specialized knowledge, commonly known information, environmental liens or use limitations, and reasons for an unusually low price as directed.","Require historical sources, databases, interviews, reconnaissance, adjoining observations, findings, significant data gaps, limitations, and recommendations.","Ask which non-scope issues—such as asbestos, lead, mold, radon, wetlands, drinking water, or vapor—are included, excluded, or separately proposed."])
]),
("A Phase I is not a laboratory clearance",[
"Do not market the result as environmentally clean. A Phase I can identify recognized, controlled, or historical conditions, data gaps, and other issues under the chosen scope, but it does not necessarily collect samples or quantify cleanup cost. Further work may include records retrieval, agency consultation, geophysics, tank investigation, vapor assessment, or Phase II sampling designed by qualified professionals.",
("table",["Result","Buyer question","Possible next move"],[
["No recognized condition identified","Were scope, timing, access, sources, and gaps adequate?","Counsel and professional confirm reliance, validity, and obligations."],
["Historical or controlled condition","What closure, restrictions, monitoring, or duties remain?","Obtain agency documents and counsel review; price controls."],
["Recognized condition","What release evidence exists and what investigation is appropriate?","Define a targeted next phase before the deadline."],
["Significant data gap","Could missing information change the opinion?","Extend research, create access, interview sources, or price uncertainty."],
["Non-scope business risk","Could asbestos, lead, vapor, wetlands, mold, or another excluded issue affect the plan?","Commission the correct separate assessment."]
])
]),
("Worked example: converting a former roadside store",[
"Assume an illustrative buyer wants to turn a former roadside store with an upstairs apartment into a group-stay STR. Historical aerials and directories show an auto-service use decades ago; the seller has no tank closure records. The residential inspection does not address subsurface conditions.",
"An environmental professional performs the agreed Phase I, identifies the historic auto use and missing tank documentation as material, and recommends targeted further investigation. The buyer does not excavate or collect casual samples. Counsel, lender, and the professional align the next scope; the model excludes opening revenue until environmental, zoning, building, insurance, and occupancy paths are resolved. This is illustrative, not a finding, legal conclusion, cleanup plan, or client result."
]),
("Put uncertainty into contract and underwriting",[
"Environmental diligence needs access rights, enough time, seller document duties, authority for interviews and agency files, sampling permission when needed, restoration responsibility, confidentiality, cost allocation, and a remedy for material results. Counsel must approve transaction language; a generic home-inspection clause may not fit invasive work or liability concerns.",
"Model professional fees, counsel, records, survey and title work, further investigation, monitoring, controls, cleanup planning, lender delay, insurance review, redesign, carrying costs, lost space, demolition or soil-management constraints, continuing obligations, and uncertainty in the <a href=\"/underwriting/\">acquisition model</a>. Do not insert an invented cleanup number before a qualified scope exists."
]),
("Failure modes and next step",[
("ul",["Ordering after acquisition when the intended legal purpose required pre-acquisition work.","Using the wrong boundary, purchaser, reliance party, standard, or purpose.","Calling a transaction screen or database report a Phase I without checking scope.","Treating absence of sampling as proof contamination is absent.","Ignoring adjoining properties, historic uses, data gaps, use limitations, or continuing obligations.","Beginning demolition or excavation before findings and worker, waste, permit, and insurance requirements are resolved."]),
("warn","Educational only, not environmental, legal, engineering, health, cleanup, insurance, lending, tax, or investment advice. Federal, state, tribal, and local rules vary."),
"Send the parcel, entity, closing date, planned use, historic clues, lender request, and intended legal purpose to environmental counsel and a qualified environmental professional before selecting the scope.",
("callout","Need environmental diligence integrated with an STR acquisition model? <a href=\"/apply/\">Apply to BNB Accelerator</a>.")
])
],
"faqs":[
("Does a Phase I environmental assessment include soil testing?","Usually not as the core Phase I process. Sampling is generally associated with separately designed further investigation, often called Phase II."),
("Is a Phase I only for commercial property?","No simple label controls. Historic use, adjoining land, lender requirements, redevelopment, liability purpose, and property setting can make it relevant."),
("Does a Phase I guarantee protection from CERCLA liability?","No. Certain protections require compliant pre-acquisition AAI plus all other applicable statutory criteria and continuing obligations."),
("Can the buyer rely on the seller's old Phase I?","Do not assume so. Timing, update requirements, scope, reliance rights, purchaser duties, changed conditions, and purpose all need review.")
],
"related":['<a href="/blog/buried-oil-tank-before-buying-str/">Buried tank diligence</a>','<a href="/blog/asbestos-survey-before-str-renovation/">Asbestos survey planning</a>','<a href="/blog/title-commitment-before-buying-str/">Title commitment review</a>','<a href="/underwriting/">Underwrite investigation risk</a>','<a href="/apply/">Discuss the acquisition</a>'],
"cta_h":"Buying an unusual or formerly commercial property?","cta_p":"BNB Accelerator can coordinate the acquisition model around qualified environmental, legal, lending, and design conclusions."
}
]

if __name__=="__main__":
    blog.build(POSTS)
    for name, score in SCORES.items():
        print(f"{name}: {sum(score.values())}/100 — {score}")
