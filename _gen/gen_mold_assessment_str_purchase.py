#!/usr/bin/env python3
"""Generate the moisture and mold assessment guide for STR buyers."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import blog

DATE = "2026-09-24"
SCORE = {
    "distinct_search_intent": 30,
    "buyer_relevance": 24,
    "real_question": 15,
    "service_fit": 12,
    "original_decision_support": 14,
}
assert sum(SCORE.values()) == 95

EPA_TESTING = "https://www.epa.gov/mold/samplingtesting-mold-necessary"
EPA_PROS = "https://www.epa.gov/mold/who-can-test-my-home-or-clean-fix-and-remediate-my-home-mold"
EPA_HOME = "https://www.epa.gov/mold/brief-guide-mold-moisture-and-your-home"
EPA_REMEDIATION = "https://www.epa.gov/mold/mold-remediation-schools-and-commercial-buildings-guide-chapter-3"
EPA_TABLE = "https://www.epa.gov/mold/mold-remediation-schools-and-commercial-buildings-guide-chapter-5"

POST = {
    "slug": "mold-inspection-before-buying-str",
    "title": "Mold inspections before buying a short-term rental",
    "title_tag": "Mold Inspection Before Buying an STR | Buyer Guide",
    "h1": "Should you get a mold inspection before buying an STR?",
    "description": "Buying an Airbnb with leaks, odors, or water damage? Use this mold-inspection framework for moisture sources, qualified assessment, remediation, and closing.",
    "date": DATE,
    "category": "Acquisition Diligence",
    "lead": "Order a qualified moisture and mold assessment when the property has visible growth, musty odors, prior water damage, active leaks, chronic humidity, suspicious staining, concealed-risk areas, or an incomplete remediation history. Do not substitute a generic air-sample package for a building investigation. EPA says routine sampling is often unnecessary when mold is visible and no federal mold or spore limits exist. The acquisition decision should identify the moisture source, affected materials and extent, safe investigation and remediation scope, repair sequence, verification criteria, cost, and STR reopening plan.",
    "sections": [
        ("The direct answer for an STR buyer", [
            f"A buyer does not need automatic whole-house mold sampling simply because the building will become an STR. EPA's <a href=\"{EPA_TESTING}\" rel=\"noopener\">mold sampling guidance</a> says that in most cases visible mold makes sampling unnecessary and that sampling cannot show compliance with a federal mold standard because no EPA or other federal limits have been set for mold or mold spores.",
            "The better question is whether the property needs a professional moisture and mold investigation. If evidence points to a problem—or if the planned renovation will open a high-risk concealed area—define that investigation during the inspection period. A report that names a mold type but never finds the leak, wet assembly, or affected extent does not create a dependable repair budget.",
            ("callout", "Evaluating a humid cabin, coastal home, basement-heavy property, or building with leak and remediation history? <a href=\"/apply/\">Apply for a BNB Accelerator strategy call</a> to pressure-test the acquisition, repair reserve, opening sequence, and operating controls. Qualified indoor-environmental, building-envelope, HVAC, plumbing, remediation, medical, insurance, and legal professionals must make their respective determinations."),
        ]),
        ("Separate four decisions that buyers often collapse", [
            ("table", ["Decision", "Question", "Evidence"], [
                ["Moisture investigation", "Where is water entering, accumulating, or condensing, and is the source active?", "History, visual evidence, measurements, envelope and system evaluation."],
                ["Mold assessment", "What materials and areas are affected or plausibly concealed, and how large is the problem?", "Qualified inspection, documented extent, limitations, targeted access."],
                ["Sampling", "Would a professionally designed sample answer a specific question that changes the plan?", "Written objective, protocol, locations, methods, laboratory and interpretation."],
                ["Remediation and repair", "How will contamination and damaged materials be handled while the moisture source and building defect are corrected?", "Work plan, containment, worker protection, removal or cleaning, repairs and verification."],
            ]),
            "A moisture inspection can be warranted when sampling is not. Remediation can be warranted without knowing the species of visible mold. Conversely, a sample result does not determine whether flashing, plumbing, grading, HVAC, insulation, drainage, or a vapor-control assembly is functioning.",
            f"EPA's <a href=\"{EPA_HOME}\" rel=\"noopener\">home moisture guide</a> states the central fact: mold does not grow without water or moisture. The buyer should therefore trace the building and operating conditions that support growth, not chase a single laboratory number.",
        ]),
        ("Use trigger-based diligence instead of routine testing", [
            ("table", ["Trigger", "Next step", "Why it matters"], [
                ["Visible growth", "Document it without disturbing it and obtain a qualified extent and moisture evaluation.", "EPA says sampling is generally unnecessary when mold is already visible."],
                ["Musty odor with no visible source", "Investigate likely concealed cavities, HVAC, crawlspace, attic, flooring and furnishings under a controlled plan.", "Hidden growth or trapped moisture may sit outside the normal inspection view."],
                ["Active leak or elevated moisture", "Identify the source, path, duration, materials and dry-out status; bring in the appropriate trade.", "Cleanup without source correction invites recurrence."],
                ["Old stain or seller-reported repair", "Obtain incident, drying, remediation, repair and verification records; assess present condition.", "A painted surface or new flooring is not a moisture history."],
                ["Finished basement, below-grade room or enclosed crawlspace", "Review drainage, waterproofing, vapor control, ventilation, HVAC and concealed finishes.", "The future STR layout may use spaces the seller rarely occupied."],
                ["Planned demolition", "Coordinate concealed-material access with asbestos, lead, electrical and structural safety before opening assemblies.", "Exploratory demolition can spread contaminants or create other regulated hazards."],
                ["No evidence or history", "Complete ordinary building diligence and keep monitoring; do not manufacture a sampling result without a decision objective.", "Mold is ubiquitous and an isolated number can be misleading without context."],
            ]),
            "The trigger list is not exhaustive. Climate, construction, property condition, insurance history, prior vacancy, disaster exposure, guest layout, and local rules can justify additional work. Let the qualified assessor set the scope after reviewing the actual building and decision deadline.",
        ]),
        ("Design a property-specific moisture investigation", [
            "Start outside and follow plausible water paths inward. A useful assessment connects site drainage, roof and wall assemblies, penetrations, windows and doors, plumbing, appliances, bathrooms, HVAC, attic, crawlspace or basement, insulation, finishes, and occupancy patterns. It distinguishes present readings from historical evidence and records inaccessible areas.",
            ("ol", [
                "Collect seller disclosures, leak and claim history, roof and plumbing invoices, mitigation or drying logs, remediation reports, laboratory results, photographs, permits and warranties.",
                "Map visible staining, deterioration, odors, condensation, corrosion, efflorescence, warped material, peeling coatings and prior patching by room and assembly.",
                "Measure conditions with appropriate tools and document instrument, location, comparison point, surface or material, date, weather and operating conditions.",
                "Evaluate likely sources: bulk water, plumbing, groundwater, capillary movement, indoor humidity, air leakage, cold surfaces, HVAC or condensate, and guest-generated moisture.",
                "Identify inaccessible cavities and decide whether seller-authorized access, a specialist, or a named post-closing contingency is required.",
                "Create a causal map that ties each observed condition to confirmed or potential sources, affected materials, uncertainty and next action.",
            ]),
            "Infrared images, moisture meters, humidity readings and borescopes can support an investigation, but each has limits. A thermal pattern is not a mold identification, a dry surface today does not erase prior damage, and a high reading needs appropriate confirmation and interpretation.",
        ]),
        ("Use sampling only when it answers a defined question", [
            f"EPA says mold sampling should be performed by professionals experienced in sampling protocols, methods, and interpretation. Its <a href=\"{EPA_PROS}\" rel=\"noopener\">professional-selection guidance</a> also notes that EPA has no certification program for mold inspectors or remediation firms, though some states may impose their own requirements.",
            "Before authorizing samples, write the decision they will support. Examples may include investigating a hidden source when other evidence is inconclusive, distinguishing materials under a professional protocol, addressing a specific health or legal question with the appropriate specialists, or verifying a remediated area when the project plan calls for sampling. Do not order samples merely to get a pass/fail score.",
            ("ul", [
                "Who designed the protocol, and are assessment and remediation roles independent where required or prudent?",
                "What hypothesis or question does each location answer?",
                "What field conditions, control or comparison samples, laboratory method, and chain of custody apply?",
                "How will results be interpreted without a federal safe-level threshold?",
                "What result would change the scope, purchase remedy, remediation, verification, or medical consultation?",
                "What are the limitations, including spatial and temporal variability and inaccessible areas?",
            ]),
            "A low or non-detect result in one air sample does not clear every wall, floor, HVAC component, crawlspace, or attic. A high result does not by itself identify the source or complete repair. Sampling belongs inside the building investigation, not above it.",
        ]),
        ("Select qualified, conflict-aware professionals", [
            "Check the property's state and locality for assessor, remediator, contractor, laboratory, disclosure, worker-safety and disposal requirements. Ask about the assessor's education, field experience, professional credentials, insurance, methods, report format, references, and experience with the building type and transaction timeline.",
            ("table", ["Role", "Primary question", "Conflict control"], [
                ["Independent assessor or consultant", "What is the moisture/mold condition, extent, cause hypothesis, and investigation or verification plan?", "Ask whether the firm sells remediation and how scope decisions are separated."],
                ["Building-envelope, roof, plumbing or HVAC specialist", "Which system defect causes or contributes to moisture?", "Require evidence and a defined repair scope rather than a sales diagnosis."],
                ["Remediation contractor", "How will affected material be contained, handled, cleaned or removed under the approved plan?", "Bid the same scope and acceptance criteria across qualified firms."],
                ["Structural engineer", "Has long-term moisture damaged load-bearing or safety-critical components?", "Use when condition suggests integrity concerns, not as a substitute for environmental assessment."],
                ["Medical professional", "What does an individual need medically?", "Keep health decisions outside the real-estate team's competence."],
            ]),
            "EPA recommends checking qualifications, training, experience and references. The cheapest inspection can be expensive if it produces an uninterpretable sample sheet, no moisture-source analysis, and no scope a contractor can price.",
        ]),
        ("Worked example: a finished lower level with a musty odor", [
            "Assume an illustrative buyer is evaluating a mountain cabin with a finished lower-level game room and bunk area. The space has a musty odor, a freshly painted exterior wall, and a dehumidifier draining continuously. The seller reports that a gutter overflow was repaired two years earlier but provides no drying or remediation file. A basic home inspection records normal fixture function and one dry surface reading.",
            "The buyer commissions a qualified moisture and mold assessment rather than buying a three-sample air package. The assessor maps the odor and finishes, reviews drainage and roof discharge, documents staining behind removable trim with permission, compares material readings, and identifies a concealed-risk zone at the base of the wall. A building-envelope specialist evaluates the exterior water path.",
            "Suppose controlled access confirms wet sheathing and visible growth behind part of the wall. The team does not need a species name to know that moisture source correction, extent assessment, safe remediation and reconstruction must be scoped. Sampling is used only if the qualified plan identifies a decision it will answer. The buyer obtains matched repair and remediation bids plus schedule, containment and verification criteria.",
            "The cabin, conditions and sequence are illustrative—not a BNB Accelerator client result, environmental conclusion, or medical recommendation. The actual response depends on the building, material, extent, occupants, rules and qualified professionals.",
        ]),
        ("Build one integrated remediation and repair scope", [
            f"EPA's <a href=\"{EPA_REMEDIATION}\" rel=\"noopener\">commercial-building remediation guidance</a> says to identify the source or cause of the moisture problem, plan the work, fix the water problem, clean and dry affected material, discard material that cannot be cleaned, and check for recurrence. It also says to consult a structural engineer or qualified professional when mold may have damaged building integrity.",
            "For an acquisition, do not compare a mold-cleaning bid with a complete building-repair bid as though they are the same. Use a common scope that separates investigation, source repair, remediation, damaged-material removal, system cleaning where justified, reconstruction, contents, verification, and recurrence prevention.",
            ("ul", [
                "Exact rooms, assemblies, materials, approximate extent, access and stated uncertainty.",
                "Water-source repair by the appropriate licensed trade, including tests or inspections that prove the repair.",
                "Containment, worker protection, pressure or airflow controls, material handling, cleaning methods and waste path as applicable.",
                "HVAC isolation or evaluation, contents handling, adjacent-area protection and daily site controls.",
                "Criteria for change orders if concealed damage is larger than the initial scope.",
                "Reconstruction materials and details that address the original moisture mechanism.",
                "Independent or otherwise qualified post-remediation verification under a written acceptance plan.",
            ]),
            f"EPA's <a href=\"{EPA_TABLE}\" rel=\"noopener\">material-specific remediation table</a> emphasizes that methods depend on affected material and area and that professional judgment matters. A universal spray-and-paint scope is not a property decision framework.",
        ]),
        ("Define completion before work begins", [
            "Completion is not the day the remediation crew leaves. The acceptance plan should address source correction, absence of visible growth and moldy odor, completed cleaning, dry materials, removal or treatment of affected materials under the scope, containment teardown conditions, documentation, and any project-specific sampling or verification criteria set by the qualified professional.",
            ("ol", [
                "Name the assessor or party who writes the remediation protocol and the party authorized to verify completion.",
                "Document pre-work conditions, containment and source repair, work performed, hidden conditions, material disposition, cleaning and final observations.",
                "Complete verification before reconstructing assemblies that would conceal failed work, when the plan requires it.",
                "Reinspect the corrected water pathway during suitable conditions when practical; a dry-weather snapshot may not test a rain leak.",
                "Preserve reports, photos, invoices, warranties, permits, laboratory records when used, and operating instructions in the property file.",
                "Set post-closing monitoring for humidity, leaks, condensate, crawlspace or basement conditions and recurrence indicators.",
            ]),
        ]),
        ("Translate the finding into a closing remedy", [
            "The purchase remedy should match uncertainty and control. A seller-completed project may preserve buyer cash but gives the seller schedule and contractor control. A credit or price reduction gives the buyer control but may underestimate concealed damage and may be limited by the loan. Escrow needs counsel, lender and title approval, adequate funding, a complete scope and clear release conditions.",
            ("table", ["Condition", "Acquisition response", "Evidence before contingency removal"], [
                ["Small, visible, source clearly corrected", "Qualified scope, remediation or buyer-controlled reserve, verification plan.", "Source evidence, extent assessment, priced scope and contract remedy."],
                ["Hidden extent unresolved", "Authorized access, broader assessment, substantial named contingency or termination.", "Documented limitations and a downside the buyer can actually fund."],
                ["Active roof, plumbing, drainage or HVAC source", "Repair source and affected materials as one sequenced project.", "Trade diagnosis, matched bids, schedule, insurance and verification."],
                ["Structural deterioration suspected", "Engineer and relevant specialists before pricing cosmetic restoration.", "Safety and repair conclusions incorporated into the scope."],
                ["Seller blocks appropriate investigation", "Do not replace missing evidence with a generic sample or verbal warranty.", "Use the contract remedy with counsel before the deadline."],
            ]),
            "Move the complete cost and launch delay into the <a href=\"/underwriting/\">acquisition model</a>. Include carrying costs, lost opening weeks, alternate lodging or vacancy controls, replacement finishes, contents, project management, insurance conditions and a concealed-damage reserve.",
        ]),
        ("Hand the moisture plan to STR operations", [
            "High turnover adds moisture loads and makes small failures harder to observe. Guests shower, cook, use hot tubs, open windows during humid weather, block returns, alter thermostats and may not report slow leaks. Cleaners see the property often, but they need a simple escalation protocol rather than responsibility for diagnosing mold.",
            ("ul", [
                "Define acceptable thermostat, ventilation and dehumidification settings for occupied and vacant periods.",
                "Place leak detection and shutoff controls where property-specific risk and qualified design support them.",
                "Give cleaners a photo-based escalation list: musty odor, staining, condensation, swelling, peeling, wet textiles and recurring bathroom growth.",
                "Inspect roof drainage, plumbing connections, condensate systems, crawlspace or basement, caulking and known repair areas on an appropriate schedule.",
                "Create an incident response for leaks, sewage, storms, HVAC failure and guest complaints, including who can take rooms offline.",
                "Keep remediation records secure but make the moisture-control instructions accessible to the manager and maintenance team.",
            ]),
            "Confirm property and liability insurance treatment before closing and before remediation. Mold, water, vacancy, construction and business-use coverage can have different exclusions, sublimits, conditions and reporting duties. Only the actual policy and carrier response answer the property-specific question.",
        ]),
        ("Failure modes that turn moisture into a reopening problem", [
            ("ul", [
                "Buying a generic air-test package and skipping the moisture-source investigation.",
                "Treating a low sample result as clearance for inaccessible walls, floors, attic, crawlspace or HVAC.",
                "Painting stains or applying a coating before correcting the leak and assessing damaged material.",
                "Letting exploratory demolition disturb concealed growth, asbestos or lead without a coordinated safety plan.",
                "Comparing remediation bids with different areas, materials, containment, source repairs and verification criteria.",
                "Allowing the same sales process to define the problem, expand the scope and certify completion without examining conflicts and local requirements.",
                "Reconstructing too early and concealing wet material or incomplete work.",
                "Launching guests without operating controls, records, insurance review and a recurrence response.",
            ]),
            ("warn", "Health and professional boundary: this guide summarizes EPA materials reviewed September 24, 2026. It is educational, not medical, indoor-environmental, occupational-safety, legal, insurance, engineering, inspection, remediation, construction, or investment advice. Requirements vary by state and locality. People with health concerns should consult a qualified healthcare professional."),
        ]),
        ("Turn the assessment into a go, renegotiate, or walk decision", [
            "Proceed when the moisture source and affected extent are understood, the repair and remediation sequence is executable, completion criteria are clear, the downside is funded, and the operating plan reduces recurrence risk. Renegotiate when a defined condition has a qualified scope but the original price and timeline ignored it. Walk away when appropriate access is refused, concealed extent remains open-ended, safety or structural questions cannot be resolved, or the total project breaks the investment case.",
            "Pair this workflow with the <a href=\"/blog/roof-inspection-short-term-rental/\">roof inspection guide</a>, the <a href=\"/blog/vacant-renovation-str-coverage/\">renovation-coverage guide</a>, the <a href=\"/blog/asbestos-survey-before-str-renovation/\">asbestos survey guide</a>, and the <a href=\"/blog/inspection-contingency-length-str/\">inspection-timeline guide</a>. Each addresses a separate dependency.",
            "The practical next step is to gather the complete water-damage history, map every moisture signal and inaccessible area, and ask a qualified local professional for a written assessment scope before ordering samples or letting anyone open the building.",
            ("callout", "Need moisture findings integrated with the offer, repair reserve, renovation plan, and STR opening date? <a href=\"/apply/\">Apply for a BNB Accelerator strategy call</a>. We can coordinate the acquisition decision while qualified environmental, building, medical, legal, insurance, and remediation professionals handle their conclusions."),
        ]),
    ],
    "faqs": [
        ("Should every STR buyer order mold testing?", "No. EPA says routine sampling is often unnecessary, especially when mold is visible. Buyers should use trigger-based moisture and mold assessment and sample only when a qualified protocol answers a defined decision question."),
        ("Can an air sample prove an Airbnb has no mold problem?", "No. A sample is limited by location, timing, method and interpretation. It does not clear inaccessible assemblies or identify and repair the moisture source."),
        ("What should a mold inspection focus on?", "Focus on moisture history and sources, visible and hidden-risk areas, affected materials and extent, building-system defects, inaccessible areas, remediation scope, repair sequence and verification criteria."),
        ("Does EPA certify mold inspectors?", "EPA says it has no certification program for mold inspectors or remediation firms, although some states may impose requirements. Check qualifications, training, experience, references and local rules."),
        ("Should visible mold be sampled before remediation?", "EPA says sampling is generally unnecessary when visible mold is present. A qualified professional may recommend targeted sampling when it will answer a specific question and change the plan."),
        ("What records should the STR owner keep after remediation?", "Keep assessment and work plans, source-repair evidence, photographs, invoices, permits, laboratory records when used, verification documents, warranties and ongoing moisture-control instructions."),
    ],
    "related": [
        '<a href="/blog/roof-inspection-short-term-rental/">Inspect the roof and water pathways</a>',
        '<a href="/blog/vacant-renovation-str-coverage/">Arrange renovation-period coverage</a>',
        '<a href="/blog/asbestos-survey-before-str-renovation/">Plan safe concealed-material access</a>',
        '<a href="/underwriting/">Model the complete repair downside</a>',
        '<a href="/apply/">Discuss the acquisition strategy</a>',
    ],
    "cta_h": "Buying an STR with odors, leaks, or water-damage history?",
    "cta_p": "BNB Accelerator can help source and underwrite the property, coordinate the diligence file, and translate moisture findings into a purchase decision while qualified local professionals handle environmental, building, medical, insurance, and remediation work.",
}


if __name__ == "__main__":
    blog.build([POST])
    print(f"candidate score: {sum(SCORE.values())}/100 — {SCORE}")
