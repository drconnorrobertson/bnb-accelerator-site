#!/usr/bin/env python3
"""Generate the buried heating-oil tank diligence guide for STR buyers."""
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

EPA_UST = "https://www.epa.gov/ust/underground-storage-tank-technical-compendium-about-2015-ust-regulation"
EPA_BROWNFIELDS = "https://www.epa.gov/ust/petroleum-brownfields"
OREGON_DEQ = "https://www.oregon.gov/deq/tanks/Pages/HOT-Buying-or-Selling.aspx"
NJDEP_HOME = "https://dep.nj.gov/srp/community/homeowner/"
NJDEP_FAQ = "https://dep.nj.gov/srp/unregulated/unregulated-faqs/"
NJ_INSURANCE = "https://www.nj.gov/dobi/division_consumers/insurance/oiltanks.htm"
MASSDEP = "https://www.mass.gov/guides/site-cleanup-for-homeowners"

POST = {
    "slug": "buried-oil-tank-before-buying-str",
    "title": "Buried oil tank checks before buying a short-term rental",
    "title_tag": "Buried Oil Tank Before Buying an STR | Buyer Guide",
    "h1": "Should you check for a buried oil tank before buying an STR?",
    "description": "Buying an older Airbnb? Use this buried-oil-tank framework to find records, confirm tank status, assess releases, price cleanup, and structure closing.",
    "date": DATE,
    "category": "Acquisition Diligence",
    "lead": "Investigate a possible buried heating-oil tank when the property, records, equipment, site features, or neighborhood history point to current or former oil heat. A standard home inspection, an empty tank, or a seller's statement that a tank was removed does not by itself establish location, closure, release status, or regulatory completion. The buyer's job is to separate tank status from environmental status, use qualified local professionals, document the search limits, and resolve the acquisition decision before the contingency expires.",
    "sections": [
        ("The direct answer for an STR buyer", [
            "Do not order a tank search for every property by reflex, but do not ignore evidence of former oil heat. Older construction, a furnace conversion, fill or vent piping, cut supply lines, an oil-fired appliance, unexplained patches, fuel records, or local tank files can justify a property-specific investigation. Obtain the owner's written permission before any intrusive work. Do not probe, excavate, open, pump, sample, or alter a suspected tank yourself.",
            f"Federal status is not a clearance. EPA's <a href=\"{EPA_UST}\" rel=\"noopener\">underground-storage-tank technical compendium</a> explains that a tank storing heating oil for consumptive use on the premises is excluded from the federal UST definition. EPA also notes that states may regulate tanks excluded under federal rules or impose more stringent requirements. State and local fire, building, environmental, disclosure, cleanup, contractor, and property-transfer rules still need to be checked for the actual address.",
            ("callout", "Evaluating an older cabin, coastal house, rural property, or converted heating system? <a href=\"/apply/\">Apply for a BNB Accelerator strategy call</a> to integrate tank uncertainty with the offer, diligence calendar, reserve, financing, insurance, and opening plan. Qualified environmental, tank, legal, insurance, engineering, and regulatory professionals must make their respective determinations."),
        ]),
        ("Separate tank status from release status", [
            "Buyers often ask whether the property has a tank as if that produces a yes-or-no environmental answer. It does not. A tank can be active, abandoned, closed in place, or removed. Separately, the property can have no release identified, an investigation still open, a confirmed release under assessment, active cleanup, or documented regulatory closure. Keep both tracks visible.",
            ("table", ["Tank condition", "What it does not prove", "Buyer evidence to seek"], [
                ["No tank found in a defined search", "That no tank ever existed or that every inaccessible area was cleared.", "Search method, areas covered, obstructions, records reviewed, limits, photos, and qualified firm's conclusion."],
                ["Active heating-oil tank", "That the tank, lines, fill system, soil, insurance, and future removal are acceptable.", "System evaluation, age/material if known, leak evidence, operating records, local compliance, coverage, and end-of-life plan."],
                ["Abandoned or reportedly empty", "That it was legally decommissioned, cleaned, filled, removed, sampled, or free of releases.", "Closure method, permits, contractor record, contents disposition, sampling basis, agency record, and present site evidence."],
                ["Closed in place", "That all jurisdictions allow the method or that surrounding soil was assessed adequately.", "Approved scope, cleaning/fill documentation, sampling and laboratory records, permits, inspections, and regulator status."],
                ["Removed", "That contaminated soil was absent, removed, documented, reported, or given closure.", "Removal report, photos, disposal records, sampling locations/results, chain of custody, cleanup file, and final agency correspondence."],
            ]),
            f"Oregon DEQ's <a href=\"{OREGON_DEQ}\" rel=\"noopener\">buyer-and-seller guidance</a> offers a useful jurisdiction-specific warning: an emptied tank is not necessarily decommissioned. Treat that as an Oregon example, not a universal rule; the definitions and required evidence depend on the property jurisdiction.",
        ]),
        ("Start with a records-and-history screen", [
            "A useful investigation begins before anyone arrives with field equipment. Build a timeline of the building's heat sources, conversions, additions, owners, permits, deliveries, claims, and earthwork. Ask for original documents rather than relying on a checkbox or verbal recollection.",
            ("ol", [
                "Review seller disclosures, purchase records, fuel-delivery bills, furnace and boiler invoices, heating-conversion records, utility history, insurance claims, environmental reports, and prior inspection files.",
                "Search the available fire-marshal, building, health, environmental, tax, and municipal records for tank installation, closure, removal, spills, permits, inspections, cleanup cases, liens, or restrictions.",
                "Compare dates and addresses across every record. A receipt for a different tank, parcel, owner, or partial scope is not the property's closure file.",
                "Read the actual closure and laboratory documents. Identify who performed the work, what tank was addressed, what areas were accessible, where samples were taken, which methods were used, and what limitations remain.",
                "Map renovations, driveways, decks, additions, retaining walls, septic work, wells, drainage, and utility routes that may conceal or constrain a tank location and future excavation.",
                "Give the qualified professional the timeline before the site visit so field work tests the unresolved questions instead of repeating a generic scan.",
            ]),
            "Records can narrow uncertainty but seldom replace a site-specific conclusion. An old fuel bill proves delivery, not tank location. A furnace permit proves equipment work, not soil condition. A cleanup invoice without sample and agency records may not show what was completed or accepted.",
        ]),
        ("Read the site without turning clues into conclusions", [
            "Document observable indicators and let a qualified tank or environmental professional interpret them. Potential clues can include exterior fill and vent pipes, capped or cut piping, copper lines through a foundation, an oil-fired appliance, staining, petroleum odor, patched slabs, unusual depressions, disturbed landscaping, or a location consistent with delivery access. Absence of a visible pipe does not prove absence of a buried tank.",
            f"New Jersey DEP's <a href=\"{NJDEP_HOME}\" rel=\"noopener\">homeowner guidance</a> lists warning signs such as unexplained fuel consumption, water in a tank, burner problems, staining, oil sheen, and petroleum odor. These are indicators that merit professional attention, not a buyer's diagnostic test. If odor, sheen, stained soil, or an active leak is encountered, stop disturbing the area and follow local emergency and reporting direction.",
            ("ul", [
                "Do not drive a rod into the ground; it can damage a tank, utility, septic component, drainage line, or other buried feature.",
                "Do not open a fill, pump liquid, move soil, or collect casual samples. These actions can create safety, disposal, reporting, evidence, and liability problems.",
                "Do not describe a visual walk-through as a tank sweep. Require the provider to state methods, coverage, obstructions, assumptions, and limitations.",
                "Do not assume one instrument distinguishes every tank from utilities, reinforced concrete, debris, or other buried metal. The professional should select and correlate appropriate methods.",
            ]),
        ]),
        ("Use an investigation ladder with decision gates", [
            "The diligence scope should become more specific as evidence increases. Not every property needs excavation or environmental sampling. The purpose of each step is to answer a question that changes the transaction, not merely accumulate reports.",
            ("table", ["Gate", "Question", "Typical output"], [
                ["1. Historical screen", "Was oil heat used, and is tank installation, removal, closure, or release documented?", "Timeline, agency-file results, unresolved records, likely tank areas."],
                ["2. Qualified site search", "Is there evidence of a tank or associated piping in the defined accessible areas?", "Methods, coverage map, findings, photographs, limitations, recommended next step."],
                ["3. Tank identification", "What was found, is it active, and what is its physical and regulatory status?", "Qualified evaluation, local records, safe access plan, service or closure options."],
                ["4. Release assessment", "Is there evidence of petroleum impact, and what media or receptors could be affected?", "Professional sampling or assessment plan, validated results, conceptual site understanding, agency coordination when required."],
                ["5. Cleanup and closure", "What work, documentation, monitoring, reporting, and approval are necessary?", "Regulator-aligned work plan, qualified bids, schedule, completion evidence, remaining obligations."],
            ]),
            "Sampling design belongs to an environmental professional who understands the tank, geology, building, groundwater, utilities, private wells, drainage, vapor pathways, local program, and proposed transaction. The buyer should understand the question and acceptance criteria, not prescribe sample counts or locations from a generic checklist.",
        ]),
        ("Why a federal exemption does not eliminate buyer risk", [
            f"EPA's <a href=\"{EPA_BROWNFIELDS}\" rel=\"noopener\">petroleum-brownfields guidance</a> says prospective purchasers should conduct due diligence to understand contamination and potential liabilities. EPA also warns that purchasers of petroleum-contaminated property may become legally responsible for cleanup and that petroleum sites do not always fit the same federal landowner protections available under CERCLA. A residential heating-oil tank's exclusion from federal UST technical standards does not erase petroleum contamination, state cleanup law, common-law claims, lender conditions, insurance exclusions, or neighboring-property impacts.",
            f"State programs demonstrate why address-specific review matters. New Jersey DEP describes residential heating-oil systems as <a href=\"{NJDEP_FAQ}\" rel=\"noopener\">unregulated heating-oil tanks under its tank framework</a>, while still overseeing remediation after a discharge and requiring appropriately certified firms for regulated cleanup work. The label 'unregulated' therefore must not be read as 'no obligations.' Other states and localities use different thresholds, terms, agencies, and procedures.",
            "Ask local environmental counsel or the qualified consultant which current laws and programs apply, who is considered responsible, whether a release must be reported, what approvals are needed, whether recorded notices or use restrictions exist, and what evidence constitutes completion. Do this before structuring a seller repair, escrow, assignment, or post-closing cleanup.",
        ]),
        ("Worked example: an older cabin converted to a heat pump", [
            "Assume an illustrative buyer is evaluating a 1950s cabin that now uses a ductless heat pump. The seller says the prior oil furnace was removed years ago. A capped pipe sits near the foundation, but the disclosure says 'unknown' for underground tanks. The local permit search shows the heat-pump installation and no tank-removal record. The cabin also uses a private well downhill from the suspected area.",
            "The buyer obtains written access and hires a qualified local firm. Its records review and site search define the accessible areas, equipment, obstructions, and limitations, then identify a probable tank near the foundation. The buyer does not ask the general inspector to open it or commission arbitrary soil samples. An environmental professional reviews the tank, building, slope, well, regulatory program, and planned excavation access, then writes the investigation scope.",
            "If the professional finds no evidence of a release under the accepted scope, the buyer still needs a lawful tank closure or continued-use plan, supporting records, future-removal budget, and insurance approval. If petroleum impact is identified, the buyer needs reporting advice, a defined assessment and cleanup path, regulator coordination where applicable, qualified bids, schedule, completion criteria, and a contract remedy. The two branches are not equivalent simply because both started with the same tank.",
            "This cabin and sequence are illustrative—not a BNB Accelerator client result, environmental conclusion, or statement that any search or sample clears a property. Actual methods and obligations depend on site conditions, professional judgment, and current jurisdictional rules.",
        ]),
        ("Build a complete tank or cleanup work scope", [
            "A tank-removal quote is not automatically an environmental completion budget. Ask qualified firms to bid a common, regulator-informed scope and make unknown-condition pricing visible. The work plan may need to address permits, utility location, safe product removal, cleaning, inerting, tank access, building protection, excavation, lifting, transport, disposal, soil management, sampling, laboratory work, backfill, compaction, paving or landscape restoration, reporting, and agency fees.",
            ("ul", [
                "Identify which contractor or professional controls each phase and which licenses, certifications, insurance, and permits are required.",
                "Separate base tank work from unit prices or allowances for impacted soil, groundwater, utilities, structural support, access changes, shoring, disposal, and extended professional oversight.",
                "Define who makes field decisions when the tank is opened or removed and unexpected staining, odor, holes, water, or impacted material appears.",
                "State where excavated material and residual product may be stored, characterized, transported, and disposed, with manifests or receipts retained.",
                "Define sampling, laboratory, documentation, regulator submission, response, and final-closure responsibilities before work starts.",
                "Include restoration only after environmental and inspection hold points are satisfied, so backfill does not conceal unresolved evidence.",
            ]),
            f"Massachusetts DEP's <a href=\"{MASSDEP}\" rel=\"noopener\">homeowner cleanup guidance</a> illustrates the possible pathways: oil can affect soil, groundwater, indoor air, drinking-water wells, or neighboring property, and qualified environmental help may be needed. The buyer should model the property-specific receptors and uncertainty rather than assume every project ends with pulling a tank and filling a hole.",
        ]),
        ("Choose a closing remedy that controls evidence and liability", [
            "A seller-completed project can keep the buyer from inheriting open work, but only if the buyer can review the scope, professionals, findings, submissions, change orders, and completion evidence before contingency release or closing. A credit gives the buyer control after closing but may be too small, restricted by the lender, unavailable for environmental work, or irrelevant to liability. A price reduction does not make a release finite.",
            ("table", ["Finding", "Possible transaction response", "Minimum decision evidence"], [
                ["No tank located; search materially limited", "Expand access or methods, preserve a specific contingency, price the uncertainty, or terminate.", "Written search limits, historical evidence, obstruction plan, counsel and lender input."],
                ["Active tank with no release evidence identified", "Continue service with a documented operating/end-of-life plan or arrange lawful replacement/closure.", "System condition, coverage, compliance, professional recommendation, future cost and timing."],
                ["Abandoned tank; closure file missing", "Seller completes qualified investigation and closure, or buyer uses a carefully structured remedy with counsel.", "Tank identity, jurisdiction requirements, assessment scope, bids, access, reporting path."],
                ["Removal documented; environmental file incomplete", "Obtain original reports and agency records; have a professional identify the missing decision evidence.", "Sampling basis, laboratory and chain-of-custody records, disposal, agency status, remaining limits."],
                ["Release confirmed or suspected", "Pause deadline, notify appropriate parties as advised, define assessment/cleanup, and decide whether to renegotiate or walk.", "Professional findings, legal/reporting advice, regulator path, estimates, schedule, insurance and finance response."],
            ]),
            "Escrow is not a magic fix. Counsel, lender, title company, insurer, environmental professional, seller, and regulator may need to align on funding, access, control, reporting, overruns, completion standards, deadlines, defaults, survival, and release. If the worst credible branch breaks the acquisition case, use the contract remedy before the deadline.",
        ]),
        ("Clear financing, insurance, title, and disclosure dependencies", [
            "Send the actual tank and environmental facts—not a sanitized summary—to the professionals whose decisions control closing and operation. Ask the lender whether an active, abandoned, removed, or leaking tank changes appraisal, collateral, repair escrow, holdback, eligibility, or closing conditions. Ask the title professional and counsel about recorded cleanup notices, environmental liens, easements, access, restrictions, or exceptions.",
            f"Coverage must be confirmed in writing against the actual policy and carrier underwriting. New Jersey's insurance department, for example, warns in its <a href=\"{NJ_INSURANCE}\" rel=\"noopener\">oil-tank consumer guidance</a> that some homeowners policies exclude oil-tank pollution and that carriers can have tank-related underwriting rules. That is a New Jersey consumer example, not a statement about a particular policy. Property, pollution, liability, business-use, vacancy, renovation, tank, and lost-income coverage may differ, and pre-existing conditions can be excluded.",
            "Do not underwrite grants, reimbursement funds, seller insurance, or state assistance until eligibility, registration timing, coverage trigger, deductibles, exclusions, limits, assignability, documentation, and available funding have been confirmed by the program or carrier. Assistance is a possible recovery source, not proof that the buyer's downside is capped.",
            "Preserve disclosure and environmental records for future refinancing and resale. Counsel should advise what must be disclosed, recorded, delivered to guests or occupants, reported to agencies, or maintained with the property file.",
        ]),
        ("Underwrite the STR impact beyond tank removal", [
            "Move the full schedule and downside into the <a href=\"/underwriting/\">STR acquisition model</a>. Include the investigation period, professional fees, access work, permits, tank work, assessment, cleanup, restoration, carrying costs, financing extensions, lost launch time, alternate heat, safety controls, management time, and a reserve for defined unknowns. Do not count revenue during a period when the building, yard, access, utilities, or insurance will prevent lawful guest operation.",
            "If the property will retain oil heat, the operating plan needs delivery access, fill and vent protection, gauge and line monitoring, service, emergency contacts, spill response, guest separation, freeze protection, and a replacement decision. Exterior amenities, parking, snow removal, septic, wells, landscaping, and future additions must not block tank service or emergency access.",
            "Pair the environmental finding with the <a href=\"/blog/title-commitment-before-buying-str/\">title commitment review</a>, <a href=\"/blog/boundary-survey-before-buying-str/\">boundary survey decision</a>, <a href=\"/blog/inspection-contingency-length-str/\">inspection contingency schedule</a>, and <a href=\"/blog/vacant-renovation-str-coverage/\">renovation coverage plan</a>. Each answers a separate closing dependency.",
        ]),
        ("Failure modes that create expensive ambiguity", [
            ("ul", [
                "Treating the federal heating-oil exclusion as permission to skip state and local review.",
                "Accepting 'empty,' 'abandoned,' 'filled,' or 'removed' without the underlying scope and records.",
                "Calling a visual inspection or undefined instrument pass a complete tank clearance.",
                "Letting an unqualified person probe, open, pump, excavate, sample, transport, or dispose of material.",
                "Sampling without a site model, decision question, professional protocol, or regulator context.",
                "Negotiating only the tank-removal price while ignoring investigation, cleanup, disposal, restoration, delay, and professional oversight.",
                "Assuming a credit, insurance policy, reimbursement program, or escrow transfers environmental responsibility.",
                "Closing before lender, title, insurer, counsel, qualified consultant, and applicable agency requirements are aligned.",
                "Launching the STR without preserving the file or handing active-tank controls to the operator.",
            ]),
            ("warn", "This guide summarizes federal and selected state sources reviewed September 24, 2026. It is educational, not environmental, engineering, legal, insurance, lending, title, tax, health, contractor, regulatory, or investment advice. Tank terminology, professional requirements, reporting duties, cleanup standards, transfer rules, and liability differ by jurisdiction and facts. Use qualified local professionals and current agency guidance for the property."),
        ]),
        ("Turn the evidence into a go, renegotiate, or walk decision", [
            "Proceed when the tank history and current status are understood to the level the professionals, agencies, lender, title company, insurer, and buyer require; the investigation or cleanup scope is executable; the completion evidence is defined; and the conservative downside still fits the deal. Renegotiate when a bounded condition can be corrected but the original price or timeline ignored it. Walk when access is refused, the site remains open-ended, financing or coverage will not clear, responsibility cannot be structured acceptably, or the credible downside breaks the investment case.",
            "The practical next step is to assemble the heating timeline, government and contractor records, site clues, search limitations, and transaction deadline, then ask a qualified local environmental professional what question the next investigation step must answer. Keep that decision log beside the purchase contract and underwriting—not buried in an inspection attachment.",
            ("callout", "Need a possible tank or petroleum issue translated into an offer, diligence plan, reserve, and closing decision? <a href=\"/apply/\">Apply for a BNB Accelerator strategy call</a>. We can coordinate the acquisition framework while qualified local environmental, legal, insurance, lending, title, and tank professionals handle their conclusions."),
        ]),
    ],
    "faqs": [
        ("Does a home inspection find underground oil tanks?", "Not necessarily. General inspections have scope limits and may only note visible clues. If records or site evidence suggest a tank, use a qualified local provider with a defined search method, coverage area, and written limitations."),
        ("Does an empty oil tank mean it was decommissioned?", "No universal conclusion follows from 'empty.' Closure definitions and requirements vary. Obtain the work scope, permits, cleaning or fill records, environmental assessment, laboratory documents when used, and agency status for the property jurisdiction."),
        ("Are home heating-oil tanks exempt from regulation?", "EPA excludes on-premises consumptive-use heating-oil tanks from the federal UST definition, but states and localities may regulate them or impose cleanup, fire, building, reporting, contractor, and transfer requirements. Petroleum releases can still create liability."),
        ("What if a tank was removed but there is no soil report?", "Collect the removal, disposal, photograph, permit, sample, laboratory, and agency files that exist. A qualified environmental professional should identify what the missing evidence means and whether further investigation is warranted."),
        ("Can a seller credit solve a leaking oil tank?", "A credit changes purchase economics but does not by itself define cleanup, secure access, satisfy regulators, bind insurance, clear a lender, cap overruns, or transfer liability. Structure any remedy with qualified legal and environmental advice."),
        ("What should an STR buyer keep after tank work?", "Keep search reports, permits, contractor qualifications, tank and disposal records, photographs, sampling plans, chain-of-custody and laboratory reports, cleanup submissions, regulator correspondence, invoices, insurance decisions, and operating instructions."),
    ],
    "related": [
        '<a href="/blog/title-commitment-before-buying-str/">Review the title commitment</a>',
        '<a href="/blog/boundary-survey-before-buying-str/">Decide whether a boundary survey is needed</a>',
        '<a href="/blog/inspection-contingency-length-str/">Build the diligence timeline</a>',
        '<a href="/underwriting/">Model the complete acquisition downside</a>',
        '<a href="/apply/">Discuss the acquisition strategy</a>',
    ],
    "cta_h": "Buying an STR with current or former oil heat?",
    "cta_p": "BNB Accelerator can help source and underwrite the property, coordinate the diligence decision, and translate tank uncertainty into an acquisition plan while qualified local professionals handle environmental, legal, insurance, and regulatory work.",
}


if __name__ == "__main__":
    blog.build([POST])
    print(f"candidate score: {sum(SCORE.values())}/100 — {SCORE}")
