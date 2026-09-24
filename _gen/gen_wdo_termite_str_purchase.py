#!/usr/bin/env python3
"""Generate the WDO and termite-inspection guide for STR buyers."""
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

EPA_TERMITES = "https://www.epa.gov/safepestcontrol/termites-how-identify-and-control-them"
EPA_SELECT = "https://www.epa.gov/safepestcontrol/tips-selecting-pest-control-service"
USFS_TERMITES = "https://research.fs.usda.gov/treesearch/23127"
NC_GUIDE = "https://www.ncagr.gov/divisions/structural-pest-control-and-pesticides/structural/consumer-information/homeowners-guide-wood-destroying-insect-report"
FL_TERMITES = "https://www.fdacs.gov/Consumer-Resources/Health-and-Safety/Protect-Your-Home-from-Pests/Termites"
FL_GUIDE = "https://ccmedia.fdacs.gov/content/download/21782/file/Understanding_Wood_Destroying_Organisms_Report.pdf"
HUD_FORM = "https://www.hud.gov/sites/documents/NPMA33.PDF"
HUD_HANDBOOK = "https://www.glb.hud.gov/hud-partners/single-family-handbook-4000-1"

POST = {
    "slug": "wdo-termite-inspection-before-buying-str",
    "title": "WDO and termite inspections before buying an STR",
    "title_tag": "WDO Termite Inspection Before Buying an STR",
    "h1": "Should you get a WDO or termite inspection before buying an STR?",
    "description": "Buying an Airbnb? Use this WDO-inspection framework to define scope, interpret termite findings, separate treatment from repairs, and structure closing.",
    "date": DATE,
    "category": "Acquisition Diligence",
    "lead": "Order a qualified wood-destroying insect or organism inspection when local practice, the lender, the contract, the building type, climate, property history, or visible conditions justify it. Do not treat a general home inspection, pest-control invoice, termite bond, seller statement, or visually clear report as proof that every structural member is sound. The acquisition decision must define which organisms and structures were covered, record inaccessible areas, separate active infestation from old evidence and damage, price treatment separately from repairs, and preserve a closing remedy for unresolved extent.",
    "sections": [
        ("The direct answer for an STR buyer", [
            f"Yes, in termite-prone areas and whenever evidence or transaction requirements make wood-destroying pests a material risk. The U.S. Forest Service says <a href=\"{USFS_TERMITES}\" rel=\"noopener\">subterranean termites occur throughout the contiguous United States</a> and may consume a board's interior while leaving an outer shell, making damage easy to overlook. Early detection and treatment can reduce the threat, but a transaction report remains a limited visual snapshot rather than a structural warranty.",
            "Use the exact report required in the property state and by the lender. Depending on jurisdiction, the service may be called a WDI, WDO, wood-infestation, termite, or structural-pest inspection. Those labels do not guarantee identical organisms, forms, access, reporting rules, professional licenses, time periods, or treatment standards.",
            ("callout", "Buying a cabin, beach house, historic home, raised foundation, or property with decks and crawlspaces? <a href=\"/apply/\">Apply for a BNB Accelerator strategy call</a> to connect WDO findings with the offer, repair reserve, insurance, financing, renovation sequence, and opening date. Qualified pest, structural, building, moisture, legal, insurance, and lending professionals must make their respective determinations."),
        ]),
        ("Start by defining what the report covers", [
            f"Coverage varies materially. The federal <a href=\"{HUD_FORM}\" rel=\"noopener\">NPMA-33 Wood Destroying Insect Inspection Report</a> describes termites, carpenter ants, carpenter bees, and reinfesting wood-boring beetles, and expressly excludes mold, mildew, and noninsect wood-destroying organisms. By contrast, Florida's official guidance addresses a state WDO form that can report live organisms, evidence, damage, and wood-decay fungi. Never infer the Florida scope from an NPMA-33—or the reverse.",
            ("table", ["Question", "Why it matters", "Evidence"], [
                ["Which form and rule apply?", "State forms, lender forms, local customs, and private reports can use different definitions and deadlines.", "Current state regulator guidance, lender instruction, inspection agreement, blank form."],
                ["Which organisms are covered?", "Termites are not the only wood-destroying insects, and some WDO forms include decay fungi while others exclude them.", "Named organisms and exclusions on the signed report."],
                ["Which structures are covered?", "Detached garages, sheds, fences, docks, decks, retaining structures, and guest units may be excluded unless requested.", "Structure list, diagram, address, photographs, explicit exclusions."],
                ["Which areas were accessible?", "Finished walls, insulation, stored items, low crawlspaces, slab edges, floor coverings, and unsafe areas can conceal activity or damage.", "Access map and limitations by location, not a generic disclaimer."],
                ["What date and purpose apply?", "A lender or closing form can have a limited acceptance period that is not a warranty period.", "Inspection date, transaction use, lender acceptance, contract deadline."],
            ]),
            f"North Carolina's regulator explains in its <a href=\"{NC_GUIDE}\" rel=\"noopener\">homebuyer's WDI-report guide</a> that the state report is a careful visual examination of accessible areas and is not a warranty that wood-destroying insects are absent. It also warns that calling the document a 'clearance letter' or 'termite letter' can misstate its scope. Use that as a North Carolina example of why buyers must read the actual governing form.",
        ]),
        ("Separate infestation, evidence, damage, conducive conditions, and access", [
            "Five columns keep the report from becoming a misleading pass/fail label. A live organism means something different from wings, pellets, tubes, frass, galleries, exit holes, old treatment marks, or repaired wood. Visible damage does not establish remaining structural capacity. Conducive conditions increase risk but do not by themselves identify an active colony. Inaccessible areas preserve uncertainty even when nothing is found elsewhere.",
            ("table", ["Report category", "Decision question", "Professional follow-up"], [
                ["Live organism or active infestation", "Which organism, where, how far may activity extend, and what treatment applies?", "Licensed pest professional under current label and state rules; structural review if damage is present."],
                ["Evidence without live organism", "Is evidence current or old, what organism likely caused it, and was prior treatment complete?", "Pest expert, treatment history, monitoring or expanded access as recommended."],
                ["Visible damage", "What members are affected, and does damage alter strength, serviceability, egress, deck safety, or repair design?", "Appropriate contractor, engineer, building professional, or specialist—not the pesticide bid alone."],
                ["Conducive condition", "What moisture, drainage, wood-to-soil contact, cellulose debris, vegetation, leak, or ventilation condition supports recurrence?", "Relevant drainage, plumbing, envelope, crawlspace, landscape, or construction professional."],
                ["Inaccessible or obstructed area", "Can access be created safely before the deadline, or must the buyer price the unknown?", "Seller-authorized access plan, pest professional, and any trade needed to avoid damage or hazard."],
                ["No visible evidence", "Was the scope complete enough for the decision, and what ongoing prevention remains?", "Documented limits, lender acceptance, periodic inspection and property controls."],
            ]),
            f"Florida's <a href=\"{FL_GUIDE}\" rel=\"noopener\">official WDO-report completion guide</a> distinguishes live organisms, other evidence, and damage, and notes that the inspector need not state the degree of damage. That is a critical acquisition boundary: the pest report can locate visible damage without quantifying the structural repair.",
        ]),
        ("Prepare the property so the inspection can answer the question", [
            "Obstructions convert a seemingly favorable report into a list of unknowns. Negotiate access before the visit and ask the inspector what must be exposed. The buyer should not personally tear out finishes, probe structural wood, disturb suspected pesticide residues, or enter unsafe crawlspaces without permission and qualified direction.",
            ("ol", [
                "List every structure and wood-intensive feature to include: main building, guest unit, garage, porches, decks, stairs, docks, sheds, fences, retaining elements, crawlspaces, attics, and additions as relevant.",
                "Collect prior inspection, treatment, renewal, bond, warranty, repair, permit, moisture, plumbing, drainage, roof, flood, and insurance-claim records.",
                "Have the seller move stored items, unlock hatches, provide crawlspace and attic access, identify concealed access panels, and disclose unsafe areas under the inspector's written preparation instructions.",
                "Map spray foam, batt insulation, encapsulation liners, finished ceilings, paneling, carpet, cabinets, appliances, low clearance, standing water, debris, and vegetation that block viewing.",
                "Document wood-to-soil contact, firewood, stumps, form boards, mulch, planters, leaking hose bibs, roof runoff, grading, plumbing leaks, HVAC condensate, and chronic dampness for professional evaluation.",
                "Ask what selective access or additional inspection will be recommended if evidence terminates at an obstruction or damage extent cannot be seen.",
            ]),
            "The access plan should respect asbestos, lead, electrical, structural, animal, confined-space, and moisture hazards. Opening an assembly can create a larger safety and remediation problem when the building history is unknown. Coordinate the appropriate specialists before destructive access.",
        ]),
        ("Use a licensed, conflict-aware inspection process", [
            f"Licensing and authorized forms are state-specific. Florida's Department of Agriculture and Consumer Services provides <a href=\"{FL_TERMITES}\" rel=\"noopener\">termite program resources, its official WDO form, and licensing contacts</a>. North Carolina says its transaction report must be issued by a licensed person or someone working for a licensed structural-pest firm. Check the actual state regulator rather than relying on a national credential alone.",
            ("ul", [
                "Verify the individual and firm's current license for inspection and any treatment category the work requires.",
                "Ask who hired and pays the inspector, whether the company sells treatment or repairs, and how findings are kept independent from the sales proposal.",
                "Require the governing form, complete agreement, covered structures and organisms, photographs or diagram, inaccessible-area list, findings by location, signatures, and recommendations.",
                "Ask whether the inspector reviewed company treatment records, seller records, posted treatment notices, monitoring stations, warranties, and prior diagrams where applicable.",
                "If treatment is proposed, obtain the pest identification, product label, method, treated area, preparation, reentry, monitoring, warranty, renewal, transfer, retreatment, and damage-repair terms in writing.",
            ]),
            f"EPA's <a href=\"{EPA_SELECT}\" rel=\"noopener\">pest-control-service selection guidance</a> warns against pressure for immediate package treatment and says buyers should understand guarantee coverage, annual inspection charges, and whether structural damage is covered if treatment fails. A warranty is only as useful as its written scope, exclusions, provider, transfer rules, and ongoing obligations.",
        ]),
        ("Do not let lender clearance replace buyer diligence", [
            f"Mortgage programs and lenders can require particular reports or repairs, but financing acceptance does not establish that every structure is sound or every operating risk is resolved. HUD's current <a href=\"{HUD_HANDBOOK}\" rel=\"noopener\">Single Family Housing Handbook 4000.1 portal</a> is the source for current FHA policy and updates. The NPMA-33 form itself warns that its transaction-use period is not a warranty and that inaccessible areas can conceal infestation or damage.",
            "Ask the lender which current form, inspector qualification, covered structures, report age, signatures, treatment, repair evidence, reinspection, and clearance documents are required for this loan. Then separately decide what the buyer needs for a short-term-rental acquisition. A lender may focus on collateral eligibility; the owner must also address guest safety, decks and exterior amenities, repair downtime, operating access, insurance, and long-term prevention.",
            "Do not describe a report as 'clean' merely because it satisfies a lender checkbox. Preserve the signed report, all pages and attachments, inaccessible areas, treatment recommendation, repair evidence, reinspection, invoice, warranty, and lender response in one dated file.",
        ]),
        ("Worked example: an insulated crawlspace under a cabin", [
            "Assume an illustrative buyer is evaluating a wooded cabin with a wraparound deck and a low crawlspace. The seller provides a transferable termite-service agreement and says the property is inspected annually. The general home inspection notes elevated moisture near one corner and damaged trim at the deck ledger. Spray foam and an encapsulation liner conceal much of the floor framing and foundation edge.",
            "The buyer orders the state-appropriate WDI/WDO inspection and names the cabin, attached deck, stairs, and crawlspace in scope. The inspector records termite evidence near a plumbing penetration, visible damage at one rim area, and substantial inaccessible framing behind foam and liner. The service agreement shows monitoring but does not promise structural repairs. The report does not quantify the damage.",
            "With seller authorization, the pest professional, moisture specialist, and appropriate contractor design limited access that does not casually damage the encapsulation or spread contaminants. A structural engineer is added if the revealed framing or deck connection raises capacity questions. The licensed pest firm identifies the organism and treatment path; the repair professional prices removal and replacement; the drainage and plumbing teams address the moisture sources.",
            "The buyer compares seller-completed work with a buyer-controlled repair, credit, escrow, or termination. The base STR model assumes the deck and affected rooms remain unavailable until treatment, structural work, moisture correction, permits, reinspection, and insurance conditions are complete. This example is illustrative—not a client result, pest identification, structural opinion, or treatment recommendation.",
        ]),
        ("Build separate treatment, repair, and prevention scopes", [
            "Termite control and building repair are different contracts. Treatment can address the target organism without replacing damaged framing. Repair can replace wood without eliminating the colony, entry path, or moisture condition. Prevention can reduce future risk without proving current structural capacity. The purchase plan needs all three when the evidence calls for them.",
            ("table", ["Scope", "Questions to resolve", "Completion evidence"], [
                ["Pest treatment", "Correct organism, product or system, label, coverage, preparation, reentry, retreatment, monitoring, license, and reporting.", "Signed treatment record, product and area documentation, required notices, reinspection, warranty or service agreement."],
                ["Damage assessment", "Members affected, concealed extent, structural consequence, temporary support, selective demolition, and design responsibility.", "Qualified report, drawings or repair scope, photographs, calculations when required, permit path."],
                ["Building repair", "Exact materials, access, shoring, replacement versus sistering, connectors, finishes, utilities, code upgrades, restoration, and change-order triggers.", "Permits and finals where required, invoices, photos, warranties, professional acceptance."],
                ["Conducive-condition correction", "Leaks, grading, drainage, wood-to-soil contact, debris, ventilation, roof runoff, landscaping, firewood, and crawlspace moisture.", "Trade completion, moisture or drainage checks, inspection, maintenance instructions."],
                ["Ongoing prevention", "Inspection frequency, station monitoring, renewal fee, transfer, exclusions, owner duties, reporting, and response time.", "Service calendar, agreement, diagram, owner and manager handoff."],
            ]),
            f"EPA's <a href=\"{EPA_TERMITES}\" rel=\"noopener\">termite identification and control guidance</a> says termite-service firms must be state licensed and pesticide labels control how products are used. It notes that reentry time varies by product and is stated on the label. Never invent a universal treatment method, exposure rule, or guest-return time; use the licensed applicator and actual registered-product instructions.",
        ]),
        ("Price the acquisition downside and closing remedy", [
            "Move the complete work into the <a href=\"/underwriting/\">acquisition model</a>: additional access, treatment, monitoring, structural evaluation, temporary support, demolition, damaged-wood repair, moisture correction, permits, finish restoration, carrying costs, financing delays, unavailable amenities, lost launch weeks, and an uncertainty reserve tied to inaccessible areas.",
            ("table", ["Finding", "Possible transaction response", "Decision evidence"], [
                ["No evidence; meaningful access", "Proceed with documented limits and ongoing prevention.", "Complete signed report, included structures, maintenance plan, lender and insurer acceptance."],
                ["No evidence; material areas inaccessible", "Create access, expand inspection, price the unknown, preserve contingency, or walk.", "Location-specific limits and a professional plan for reducing uncertainty."],
                ["Active infestation; damage not established", "Define licensed treatment, inspection or monitoring, reentry, warranty, and recurrence controls.", "Organism identification, treatment scope, product label, access, schedule, reinspection."],
                ["Visible damage; extent bounded", "Combine treatment and qualified repair with seller work or a buyer-controlled remedy.", "Structural or building scope, matched bids, permits, completion criteria, reserve."],
                ["Damage disappears behind finishes or critical structure", "Authorize targeted access and specialist review before committing—or underwrite a truly conservative worst case.", "Defined invasive scope, safety controls, stop points, responsibility, contract remedy."],
                ["Seller refuses access or appropriate inspection", "Do not replace evidence with a warranty promise or cosmetic patch.", "Use counsel and the contract before the deadline."],
            ]),
            "A seller-paid treatment may help but does not give the buyer control over repair extent or provider selection. A credit preserves control but can be constrained by the loan and may not cover hidden damage. Escrow needs counsel, lender, title, adequate funding, access rights, defined release conditions, overruns, deadlines, and a remedy if the work expands or fails inspection.",
        ]),
        ("Hand the WDO plan to STR operations", [
            "Short-term-rental turnover changes the monitoring system. Cleaners, maintenance vendors, landscapers, and managers can notice wings, pellets, frass, mud tubes, damp wood, leaks, deck movement, or recurring debris—but they should report and photograph, not diagnose species or apply pesticides outside their role.",
            ("ul", [
                "Keep firewood and cellulose debris away from the structure under the pest professional's property-specific guidance.",
                "Maintain roof runoff, grading, drainage, plumbing, HVAC condensate, crawlspace conditions, exterior coatings, vegetation clearance, and wood-to-soil separation.",
                "Add decks, porch posts, railings, stairs, docks, sheds, and exterior amenities to the inspection and maintenance schedule where relevant.",
                "Record monitoring-station locations so cleaners, landscapers, snow crews, and guests do not move or bury them.",
                "Schedule treatment around vacancy, preparation, ventilation, reentry, housekeeping, food and pet controls exactly as the product label and licensed applicator require.",
                "Create a stop-use and escalation rule when damage may affect floors, stairs, decks, railings, furniture support, or another guest-access area.",
                "Preserve inspection, treatment, repair, product, warranty, renewal, and transfer records for insurance, refinancing, future repairs, and resale.",
            ]),
            "Confirm insurance treatment of insect damage, rot, collapse, maintenance, pesticide application, vacancy, repair work, and business use with the actual carrier and policy. Never assume a termite bond or pest warranty fills a property-policy exclusion or structural-repair gap.",
        ]),
        ("Failure modes that turn a report into false clearance", [
            ("ul", [
                "Calling every transaction document a termite letter without reading its organisms, form, structures, access, or exclusions.",
                "Treating 'no visible evidence' as a guarantee about walls, insulated framing, slab edges, low crawlspaces, or other inaccessible areas.",
                "Ordering only the main-house inspection while excluding decks, garages, guest units, sheds, docks, or other material structures.",
                "Letting the treatment seller determine structural sufficiency or repair scope outside their qualification.",
                "Replacing visibly damaged wood before the pest evidence, extent, treatment, and required reporting are documented.",
                "Buying a treatment package without identifying the organism, label, treated area, reentry, monitoring, warranty, renewal, and owner duties.",
                "Assuming an annual service sticker or transferable bond covers pre-existing damage, every species, repair, retreatment, or STR use.",
                "Closing before lender form requirements, repairs, reinspection, insurance, and inaccessible-area decisions are aligned.",
                "Launching guests while structural or pesticide reentry restrictions remain unresolved.",
            ]),
            ("warn", "This guide summarizes federal and selected state sources reviewed September 24, 2026. It is educational, not pest-control, pesticide, structural, engineering, environmental, legal, insurance, lending, medical, contracting, tax, or investment advice. Organisms, forms, access standards, licensing, treatment, product labels, warranties, lender rules, and transaction remedies vary. Use qualified local professionals and current source documents."),
        ]),
        ("Turn the WDO report into a go, renegotiate, or walk decision", [
            "Proceed when the correct report covers the material structures and organisms, access is adequate for the decision, findings and conducive conditions are understood, treatment and repair are separated, the completion evidence is defined, lender and insurance requirements are clear, and the downside fits the model. Renegotiate when a bounded treatment or repair changes price and opening timing. Walk when access is blocked, structural extent remains open-ended, qualified scopes conflict without resolution, or the investment only works by assuming concealed damage does not exist.",
            "Pair this workflow with the <a href=\"/blog/mold-inspection-before-buying-str/\">moisture and mold assessment guide</a>, the <a href=\"/blog/clue-report-before-buying-str/\">claim-history guide</a>, the <a href=\"/blog/inspection-contingency-length-str/\">inspection-contingency timeline</a>, and the <a href=\"/blog/vacant-renovation-str-coverage/\">renovation coverage guide</a>. Each answers a different acquisition dependency.",
            "The practical next step is to obtain the governing form, list every structure and organism to cover, map blocked areas, collect treatment and repair history, and ask a licensed local professional for a written inspection scope early enough to investigate any finding before the contract deadline.",
            ("callout", "Need WDO findings translated into access decisions, repair reserves, closing terms, and an STR opening plan? <a href=\"/apply/\">Apply for a BNB Accelerator strategy call</a>. We can coordinate the acquisition framework while qualified pest, structural, legal, insurance, lending, and repair professionals handle their conclusions."),
        ]),
    ],
    "faqs": [
        ("Is a WDO inspection the same as a termite inspection?", "Not always. A WDI or WDO report may cover termites plus other insects or decay organisms, depending on the state, form, and agreement. Read the named organisms and exclusions rather than relying on the label."),
        ("Does a clear WDO report guarantee there are no termites?", "No. Transaction reports generally address visible evidence in accessible areas at a point in time and contain stated limitations. Concealed or inaccessible activity and damage can remain."),
        ("Does a termite treatment repair structural damage?", "No. Pest treatment and building repair are separate scopes. A qualified building professional or engineer may need to assess damaged members while the licensed pest professional handles identification and treatment."),
        ("Should detached structures and decks be inspected?", "Include every structure and feature material to the purchase and STR use. State practice may not automatically include detached buildings, fences, docks, or sheds, so name them in the inspection agreement."),
        ("Can an STR reopen immediately after termite treatment?", "Do not use a universal timeline. Preparation and reentry depend on the registered product label, treatment method, licensed applicator, ventilation or other instructions, and any local or insurance requirements."),
        ("Does a termite bond transfer to the buyer?", "Some agreements may transfer, while others require a fee, inspection, renewal, or may exclude damage and certain organisms. Read the full written agreement and confirm transfer directly with the provider before closing."),
    ],
    "related": [
        '<a href="/blog/mold-inspection-before-buying-str/">Investigate moisture and concealed damage</a>',
        '<a href="/blog/clue-report-before-buying-str/">Reconcile prior property claims</a>',
        '<a href="/blog/inspection-contingency-length-str/">Build enough diligence time</a>',
        '<a href="/underwriting/">Model treatment, repairs, and downtime</a>',
        '<a href="/apply/">Discuss the acquisition strategy</a>',
    ],
    "cta_h": "Buying an STR with termite or wood-damage risk?",
    "cta_p": "BNB Accelerator can help source and underwrite the property, coordinate the diligence file, and translate WDO findings into an acquisition plan while qualified pest, structural, legal, insurance, and repair professionals handle their conclusions.",
}


if __name__ == "__main__":
    blog.build([POST])
    print(f"candidate score: {sum(SCORE.values())}/100 — {SCORE}")
