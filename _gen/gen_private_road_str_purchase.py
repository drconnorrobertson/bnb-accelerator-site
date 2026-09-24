#!/usr/bin/env python3
"""Generate the private-road diligence guide for STR buyers."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import blog

DATE = "2026-09-24"
SCORE = {
    "distinct_search_intent": 29,
    "buyer_relevance": 24,
    "real_question": 15,
    "service_fit": 14,
    "original_decision_support": 15,
}
assert sum(SCORE.values()) == 97

FANNIE = "https://selling-guide.fanniemae.com/sel/b4-1.3-04/site-section-appraisal-report"
VA = "https://www.benefits.va.gov/HOMELOANS/documents/circulars/26-22-17.pdf"
USDA = "https://www.rd.usda.gov/sites/default/files/3550-1chapter05_0.pdf"

POST = {
    "slug": "private-road-maintenance-agreement-before-buying-str",
    "title": "Private-road agreements before buying a short-term rental",
    "title_tag": "Private-Road Agreement Before Buying an STR",
    "h1": "How should you review a private road before buying an STR?",
    "description": "Buying an Airbnb on a private road? Verify legal access, maintenance duties, lender rules, guest operations, repair exposure, and remedies before committing.",
    "date": DATE,
    "category": "Acquisition Diligence",
    "lead": "Treat a private road or shared driveway as four separate acquisition questions: does the property have recorded legal access, who controls and maintains the route, will the lender and insurer accept the arrangement, and can guests and vendors use it reliably in every expected season? A deed reference or visible driveway answers none of those questions by itself. Obtain the recorded easement and maintenance documents, compare them with the route on a current survey, verify the financing standard with the actual lender, inspect physical condition and service access, then price recurring costs and a major-repair downside before the contract deadline.",
    "sections": [
        ("The direct answer for an STR buyer", [
            "Do not close on a private-road property until qualified local professionals have established the legal route, benefited and burdened parcels, permitted users, maintenance allocation, enforcement path, and lender treatment. Then test whether the physical road supports the intended guest count, cleaner turns, deliveries, emergency access, trash collection, snow or storm response, and planned amenities. Legal access, loan eligibility, and good operations overlap, but they are not the same conclusion.",
            f"Current agency rules illustrate why the loan program matters. <a href=\"{FANNIE}\" rel=\"noopener\">Fannie Mae's Selling Guide</a> generally requires a legally enforceable, recorded maintenance agreement or covenant for a community-owned or privately maintained street, subject to stated alternatives. <a href=\"{VA}\" rel=\"noopener\">VA Circular 26-22-17</a> removed its general ongoing-maintenance-agreement requirement for private roads and shared driveways but retained the recorded permanent easement or right-of-way requirement. Those are different frameworks, not permission to assume every lender will approve the file.",
            ("callout", "Considering a cabin, lake house, mountain home, or rural STR reached by a shared road? <a href=\"/apply/\">Apply for a BNB Accelerator strategy call</a> to connect access diligence with financing, reserves, property operations, and the purchase decision. Local counsel, title, survey, lending, insurance, engineering, and public-safety professionals must make their own conclusions."),
        ]),
        ("Build the private-road file before interpreting it", [
            "Start with documents, not the seller's description that everyone has always used the road. Ask the title company and local counsel for the current deed, title commitment, complete recorded easement or right-of-way, maintenance agreement, subdivision declaration, plats, amendments, releases, road-association documents, assessments, pending-work notices, and any recorded judgments or liens related to the arrangement. Include every exhibit and legal description.",
            ("ol", [
                "Identify every parcel the driveway or road crosses from the public street to the subject property, including gates, turnouts, bridges, culverts, parking approaches, and alternate routes.",
                "Match the benefited property, burdened property, route, width, purpose, permitted users, and term in the recorded documents to the survey and what exists on the ground.",
                "List every owner, association, committee, manager, or public body with maintenance, approval, collection, gate, or construction authority.",
                "Obtain the current budget, reserves, owner ledger, invoices, meeting records, insurance information, disputes, bids, engineering reports, and planned assessments when an association or shared account exists.",
                "Give the complete file and the intended STR use—not a generic residential description—to the buyer's counsel, lender, title professional, surveyor, and insurer as relevant.",
            ]),
            "An unrecorded neighbor handshake may describe present cooperation without binding a future owner or satisfying a lender. A recorded easement can establish passage while saying little about maintenance. A maintenance agreement can allocate grading costs while failing to cover a collapsed culvert, bridge, drainage damage, snow service, or enforcement. Read the instruments together.",
        ]),
        ("Separate access rights from maintenance duties", [
            ("table", ["Question", "Evidence to examine", "STR consequence"], [
                ["Is access legally appurtenant to the property?", "Recorded easement, deed, plat, title treatment, legal descriptions.", "Without durable access, guest arrival and resale may depend on permission that can change."],
                ["Does the recorded route match the traveled route?", "Boundary or easement survey, field observations, gates and turnouts.", "Guests may be driving outside the insured or granted corridor."],
                ["Who may use it and for what purpose?", "Grant language, definitions, amendments, covenants, local legal analysis.", "Residential access may raise questions about guests, vendors, events, or commercial activity."],
                ["Who performs routine work?", "Agreement, association rules, vendor contracts, owner history.", "Grading, dust control, mowing, snow, ice, drainage, and trees affect reviews and turns."],
                ["Who pays for capital failures?", "Allocation formula, assessment authority, insurance, reserve records.", "A washout, bridge, retaining wall, or culvert can create a large unmodeled obligation."],
                ["What happens when an owner refuses?", "Notice, voting, collection, lien, self-help, arbitration, and court provisions.", "A theoretical cost share is weak if work cannot start or payment cannot be collected."],
            ]),
            "Ask counsel whether the right runs with the land, binds successors, permits the actual route and users, survives transfer, and can be enforced by the buyer. Ask the title professional what is insured, excepted, or dependent on survey evidence. Neither professional should be asked to certify road condition or operating capacity; those require different expertise.",
        ]),
        ("Read the maintenance agreement like an operating contract", [
            f"Fannie Mae says the agreement or covenant should address each party's representative share of repair payments, remedies for default, and a term that in most cases is perpetual and binds future owners. Its guide also notes that a separate agreement may not be required where state statutes define owners' private-street maintenance responsibilities, and describes a lender-indemnification path in certain other cases. That is lender guidance—not a buyer's substitute for understanding future costs and control.",
            ("ul", [
                "Scope: surface, shoulders, drainage, ditches, culverts, bridges, retaining structures, gates, signs, lighting, vegetation, dust, snow, ice, storm debris, and emergency work.",
                "Standard: who decides when work is necessary, what quality or width is required, and whether improvements exceed basic maintenance.",
                "Allocation: equal shares, frontage, distance, usage, vehicle count, benefit, or another formula; treatment of vacant lots and later subdivision.",
                "Authority: who obtains bids, chooses vendors, enters property, closes the road, calls emergency work, and approves capital projects.",
                "Money: budget, reserve, special-assessment power, payment deadline, interest, collection cost, lien rights, default remedies, and audit or reporting duties.",
                "Risk: contractor insurance, road or association coverage, indemnity, casualty proceeds, liability claims, and owner responsibilities.",
                "Change: voting thresholds, amendment power, transfer duties, dispute resolution, term, termination, and obligations binding future owners.",
            ]),
            "Do not turn a legal review into a checklist of preferred clauses. State law, the recorded chain, lender rules, and the actual document control. The checklist is designed to reveal questions for qualified review and underwriting.",
        ]),
        ("Verify the loan path before waiving financing", [
            "Send the complete access and maintenance package to the actual loan officer and underwriter early. Ask for a written list of remaining conditions and whether the appraisal must address road marketability or condition. A preapproval, automated finding, or broker assurance is not final property approval.",
            f"The VA circular shows a crucial distinction: VA no longer generally requires an ongoing HOA or joint maintenance agreement for these properties, while it still requires a recorded permanent easement or recorded right-of-way from the property to a public road in the loan file. By contrast, USDA's <a href=\"{USDA}\" rel=\"noopener\">Single Family Housing Direct handbook</a> says the site must be accessible from an all-weather road maintained by a public body or homeowners association, and when an association maintains the road, a legally enforceable ongoing-maintenance arrangement is required. Confirm which current program, lender overlay, occupancy rule, and property facts apply.",
            ("table", ["Financing checkpoint", "Ask before the deadline", "Do not substitute"], [
                ["Recorded access", "What instrument, route, permanence, and title evidence are acceptable?", "A visible driveway or seller affidavit alone."],
                ["Maintenance framework", "Does this program and lender require an agreement, statute, association, or other evidence?", "A generic form from another state or loan program."],
                ["Road condition", "Will appraisal, engineering, safety, or repair conditions apply?", "Legal access as proof of all-weather physical access."],
                ["Property use", "Is the intended occupancy and STR plan compatible with the selected loan?", "Approval of the road as approval of short-term renting."],
                ["Closing evidence", "Which signed, recorded, updated, and underwriter-approved items must be in file?", "A promise to fix documentation after closing."],
            ]),
        ]),
        ("Inspect the road as a revenue dependency", [
            "Walk and drive the full route in appropriate conditions with the relevant qualified professionals. Record surface, grade, width, sight distance, turnouts, turning radius, clearance, drainage, erosion, washouts, soft shoulders, culverts, bridges, retaining walls, gates, address markers, utility conflicts, and the interface with public pavement. Seasonal photos, service invoices, repair records, and interviews can reveal conditions absent on inspection day.",
            ("ul", [
                "Can ordinary guest vehicles safely reach, turn around, park, and leave without trespass or blocking neighbors?",
                "Can cleaners, maintenance vendors, linen delivery, refuse, septic, propane, furniture, and construction vehicles reach the property under vendor policies?",
                "What happens after snow, ice, heavy rain, wildfire response, a fallen tree, a washout, or a gate failure?",
                "Do emergency responders have the width, clearance, grade, load capacity, addressing, water-supply access, and turnaround required by the authority having jurisdiction?",
                "Who carries keys, codes, remotes, maps, and after-hours vendor contacts, and how is access restored when equipment fails?",
                "Will guests lose cellular navigation, mistake another driveway, meet opposing traffic without a turnout, or arrive after service has stopped?",
            ]),
            "Do not promise emergency access or road capacity based on a passenger-car test. Obtain current requirements and property-specific conclusions from the local fire, building, road, engineering, and other authorities or professionals whose approval matters.",
        ]),
        ("Worked example: a mountain cabin with a shared gravel road", [
            "Assume an illustrative buyer is evaluating a four-bedroom mountain cabin reached by three-quarters of a mile of shared gravel road. The listing says road maintenance is $600 per year. The title commitment lists an access easement and road agreement, while the current drive appears to cross five parcels and includes a steep culvert crossing. The buyer's model includes winter weekends and same-day turns.",
            "The document review shows that the easement benefits the cabin parcel and binds successors, but one traveled curve leaves the recorded corridor. The maintenance agreement divides ordinary grading equally among six owners; it does not clearly classify culvert replacement, authorize a reserve, or specify winter response. Association records show the $600 figure was last year's routine contribution, not a cap. A snow contractor will service only after the public approach is open and will not guarantee a completion time.",
            "The buyer does not invent a failure probability. Counsel and the surveyor address the route mismatch; the lender reviews the final documents; a qualified road professional scopes drainage and culvert condition; the insurer reviews private-road and business-use facts. The model adds documented routine expense, a buyer-selected capital reserve, and blocked-night scenarios. The buyer then renegotiates, cures, redesigns operations, or terminates under the contract. Every property, dollar, distance, and finding in this example is illustrative—not a client result or forecast.",
        ]),
        ("Put road exposure into the underwriting model", [
            "Underwrite from records and scoped work, not last year's voluntary contribution. Include regular dues, grading, gravel, dust control, snow and ice, mowing, drainage cleaning, gate service, insurance, administration, reserve funding, known assessments, and the property's allocated share of identified repairs. Keep uncertain capital work visible rather than hiding it inside a general maintenance percentage.",
            ("table", ["Scenario", "Model treatment", "Decision trigger"], [
                ["Normal operations", "Documented recurring contribution plus routine access procedures.", "Agreement, budget, history, and vendor plan align."],
                ["Deferred maintenance", "Scoped corrective work, buyer share, timing, and opening dependency.", "Qualified inspection or records identify work."],
                ["Capital failure", "Separate downside for culvert, bridge, retaining, drainage, or washout exposure.", "Scope and allocation are incomplete or reserves are thin."],
                ["Temporary closure", "Lost nights, refunds, relocations, vendor delays, and response cost.", "Only route is vulnerable and no reliable alternate exists."],
                ["Dispute or nonpayment", "Legal and collection cost are not forecastable revenue expenses; treat as decision risk.", "Default remedies, authority, or owner history are weak."],
            ]),
            "Use the <a href=\"/underwriting/\">STR underwriting framework</a> to run the acquisition with and without the expected guest capacity, peak-season access, and planned amenities. A road that works physically today can still be an unacceptable investment if the buyer lacks a financeable right, repair authority, cost visibility, or operational fallback.",
        ]),
        ("Structure closing around evidence, not reassurance", [
            "Coordinate contract rights and deadlines with local counsel. The buyer may need document delivery, survey access, association and neighbor records, lender approval, physical inspection, authority contacts, repair bids, and enough time for a recorded cure. The appropriate remedy could be seller cure, amendment, easement correction, association action, escrow, credit, price change, delayed closing, redesign, or termination. Some problems cannot be cured with money alone.",
            ("ol", [
                "Calendar title, survey, inspection, association, financing, appraisal, and objection deadlines in one control sheet.",
                "Define the unresolved question and which professional or authority can answer it.",
                "Request the exact evidence needed: recorded instrument, updated survey, underwriter approval, inspection, bid, vote, payment record, or completed work.",
                "Reconcile the final title commitment, deed, survey, loan conditions, settlement statement, road ledger, and any cure document before funding.",
                "After recording, collect the issued title policy, recorded instruments, association contacts, gate controls, maintenance calendar, vendor plan, and manager escalation protocol.",
            ]),
            "A seller credit does not relocate a driveway into the easement, create a missing legal right, bind a non-signing neighbor, make a lender accept the property, or ensure a washed-out road reopens. Match each remedy to the actual failure mode.",
        ]),
        ("Failure modes and the practical next step", [
            ("ul", [
                "Treating long-standing use as proof of recorded, transferable, and insurable access.",
                "Reviewing an easement without comparing its legal route to a current survey and the traveled road.",
                "Assuming a maintenance agreement covers bridges, culverts, drainage, snow, gates, emergencies, and capital upgrades.",
                "Using last year's dues as a maximum future cost or ignoring unpaid owners and deferred work.",
                "Assuming one agency's rule applies to every loan program, lender overlay, occupancy structure, or state.",
                "Confusing lender collateral approval with STR permission, guest safety, emergency access, or reliable operations.",
                "Launching without a road-closure response, vendor access plan, accurate directions, and gate redundancy.",
                "Accepting a post-closing promise where a recorded cure or underwriter approval is needed before funding.",
            ]),
            ("warn", "Legal, lending, and safety boundary: this guide summarizes federal agency materials reviewed September 24, 2026. It is educational, not legal, title, survey, engineering, fire, road-design, insurance, lending, tax, zoning, accessibility, or investment advice. State law, recorded instruments, lender overlays, road conditions, authority requirements, and remedies vary. Use current documents and qualified local professionals."),
            "The practical next step is to request the recorded access and maintenance package, place the route on a current survey, send the complete file to counsel and the lender, inspect the entire road, and build both recurring and capital exposure into the acquisition model before any deadline expires.",
            ("callout", "Need private-road findings translated into a purchase price, reserve, contract decision, and launch plan? <a href=\"/apply/\">Apply for a BNB Accelerator strategy call</a>. We can coordinate the investment workflow while qualified local professionals make the legal, lending, survey, insurance, engineering, and safety determinations."),
        ]),
    ],
    "faqs": [
        ("Does a private road always need a maintenance agreement for financing?", "No universal rule applies. Requirements depend on the loan program, lender overlays, state law, property facts, and current guidance. Fannie Mae and VA, for example, use different frameworks."),
        ("Is a road easement the same as a maintenance agreement?", "No. An easement may establish a right of access, while a maintenance agreement addresses work, payment, authority, and enforcement. A transaction may need both questions resolved."),
        ("What should be in a private-road maintenance agreement?", "Review the actual agreement with local counsel. Key diligence topics include covered assets and work, cost allocation, decision authority, emergencies, default remedies, insurance, amendments, duration, and successor obligations."),
        ("Can a seller credit solve a private-road problem?", "A credit can reallocate a bounded cost, but it cannot create missing legal access, correct the recorded route, bind neighbors, satisfy every lender, or guarantee future cooperation."),
        ("Should an STR buyer inspect the road separately from the house?", "Yes when access is material. The road can involve drainage, culverts, bridges, slopes, gates, seasonal service, vendor access, emergency response, and capital costs outside a standard home inspection."),
        ("Does a recorded access easement mean guests can use the road?", "Do not assume so. The grant language, definitions, property use, related covenants, state law, and facts require local legal review."),
    ],
    "related": [
        '<a href="/blog/title-commitment-before-buying-str/">Review the title commitment</a>',
        '<a href="/blog/boundary-survey-before-buying-str/">Map access on the survey</a>',
        '<a href="/blog/inspection-contingency-length-str/">Protect the diligence timeline</a>',
        '<a href="/underwriting/">Model road costs and closures</a>',
        '<a href="/apply/">Discuss the acquisition strategy</a>',
    ],
    "cta_h": "Buying an STR on a private road or shared driveway?",
    "cta_p": "BNB Accelerator can help source and underwrite the property, coordinate diligence, and translate access risk into a purchase and launch plan while qualified local professionals handle their conclusions.",
}


if __name__ == "__main__":
    blog.build([POST])
    print(f"candidate score: {sum(SCORE.values())}/100 — {SCORE}")
