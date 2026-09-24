#!/usr/bin/env python3
"""Generate the asbestos survey guide for STR acquisition renovations."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import blog

DATE = "2026-09-24"
SCORE = {
    "distinct_search_intent": 30,
    "buyer_relevance": 23,
    "real_question": 15,
    "service_fit": 13,
    "original_decision_support": 14,
}
assert sum(SCORE.values()) == 95

EPA_REMODEL = "https://www.epa.gov/asbestos/im-remodeling-my-home-do-i-need-be-concerned-about-asbestos-building-materials"
OSHA = "https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.1101"
EPA_FAMILY = "https://www.epa.gov/asbestos/protect-your-family-exposures-asbestos"
EPA_DEMO = "https://www.epa.gov/large-scale-residential-demolition/asbestos-containing-materials-acm-and-demolition"
EPA_KNOW = "https://www.epa.gov/asbestos/how-do-i-know-if-i-have-asbestos-my-home-floor-tile-ceiling-tile-shingles-siding-etc"

POST = {
    "slug": "asbestos-survey-before-str-renovation",
    "title": "Asbestos surveys before renovating a short-term rental",
    "title_tag": "Asbestos Survey Before an STR Renovation | Buyer Guide",
    "h1": "Do you need an asbestos survey before renovating an STR?",
    "description": "Buying an older Airbnb to renovate? Use this asbestos survey framework for suspect materials, qualified testing, contractor bids, records, and launch timing.",
    "date": DATE,
    "category": "Acquisition Diligence",
    "lead": "If an STR renovation will disturb material that could contain asbestos, commission a scope-specific assessment by a properly trained and accredited asbestos professional before demolition or repair begins. Do not rely on the building's age alone, a visual inspection, a seller's memory, or a contractor's generic allowance. Federal environmental rules contain a limited exclusion for some small residential buildings, but that does not erase OSHA worker-protection duties or stricter state and local requirements. The buyer needs a material map, governing-rule review, qualified abatement or work plan, cost, schedule, and reopening criteria before the renovation budget is dependable.",
    "sections": [
        ("The direct answer for an STR buyer", [
            f"EPA's <a href=\"{EPA_REMODEL}\" rel=\"noopener\">home-remodeling asbestos guidance</a> says asbestos cannot be identified by sight. When suspect material is damaged or a planned renovation will disturb it, EPA recommends sampling by a properly trained and accredited asbestos inspector and analysis by a qualified laboratory. For an acquisition, that assessment should follow the actual renovation scope rather than a generic list of old-house materials.",
            "The word 'survey' can mean different scopes across jurisdictions. Ask the inspector and regulator what assessment is required for the exact property, work, occupancy, and permit. A limited sample of one flooring layer does not clear a whole building, and a broad inspection that does not address concealed layers may not answer a demolition question.",
            ("callout", "Considering an older property with demolition, flooring, ceiling, siding, or mechanical work? <a href=\"/apply/\">Apply for a BNB Accelerator strategy call</a> to pressure-test the acquisition, improvement scope, reserves, and opening timeline. Accredited asbestos professionals, contractors, regulators, and counsel must determine and perform the required technical work."),
        ]),
        ("Use three separate rule layers", [
            ("table", ["Layer", "What it governs", "Buyer question"], [
                ["Environmental", "Inspection, notification, emission controls, removal, and disposal for covered renovation or demolition activities.", "Does federal asbestos NESHAP or a state or local equivalent apply to this building and scope?"],
                ["Worker protection", "Employee exposure, presumed materials, regulated areas, work methods, training, communication, and records.", "Which owner, employer, general contractor, and trade duties apply before employees disturb material?"],
                ["Property and operations", "Permits, licensing, occupancy, contract allocation, insurance, guest separation, and reopening.", "What evidence must exist before work starts and before guests or staff return?"],
            ]),
            "Do not let one answer substitute for another. A small residential building may be outside a particular federal environmental provision yet still be subject to OSHA requirements when employees perform construction work and to state or local asbestos rules. Conversely, an environmental notification does not prove that worker training, exposure controls, waste handling, or final handoff are complete.",
            "An STR's commercial use does not justify a one-line conclusion about the residential exclusion. Property configuration, number of dwelling units, common ownership or control, the wider project, demolition versus renovation, threshold quantities, and the administering agency can matter. Get the applicability decision from qualified professionals and the responsible regulator.",
        ]),
        ("Why the federal residential exclusion is not a safe shortcut", [
            f"EPA explains that the federal asbestos NESHAP requires a thorough inspection before covered demolition or renovation, while some residential buildings with four or fewer dwelling units are excluded. Its <a href=\"{EPA_DEMO}\" rel=\"noopener\">demolition guidance</a> warns that state and local identification requirements may still apply. The federal exclusion can also fail when residential buildings are part of a larger installation or project.",
            "For a single STR purchase, that means the team should ask a precise question: which federal, state, and local provisions govern this address and complete scope? Do not ask only whether 'houses are exempt.' A detached home, a four-unit building, a condo-hotel component, a cabin complex, and multiple buildings under common control can present different analyses.",
            ("ul", [
                "Identify every building and dwelling unit included in the project, not only the rentable unit shown on the listing.",
                "Describe whether work is renovation, partial demolition, full demolition, disaster repair, or a combination.",
                "Identify common ownership or control and whether adjacent structures are part of the same project.",
                "Ask the state or local air, environmental, labor, and building agencies about additional inspection, notification, licensing, and disposal rules.",
                "Preserve the written applicability response or professional memorandum in the permanent property file.",
            ]),
        ]),
        ("OSHA changes the owner-contractor handoff", [
            f"OSHA's <a href=\"{OSHA}\" rel=\"noopener\">construction asbestos standard, 29 CFR 1926.1101</a>, covers demolition, removal, encapsulation, construction, alteration, repair, maintenance, and renovation involving asbestos or presumed asbestos-containing material. It assigns building or facility owners information, determination, notification, and record duties, while employers have their own assessment, training, exposure-control, work-practice, and communication obligations.",
            "Under OSHA's presumption framework, thermal system insulation and sprayed- or troweled-on surfacing material in buildings constructed no later than 1980 are treated as presumed asbestos-containing material unless properly rebutted. Resilient flooring and associated mastic or backing installed no later than 1980 also receive specific presumed treatment. Other materials can still contain asbestos even when they are not on that presumption list.",
            "Before covered work begins, the owner must determine the presence, location, and quantity of ACM or PACM at the work site under the standard and notify specified bidders, employers, employees, and tenants. The general contractor also retains supervisory responsibilities on covered projects. A line in the contract saying 'contractor responsible for asbestos' does not create the underlying material information or complete the handoff.",
        ]),
        ("Build a scope-specific material map", [
            "Start with the renovation scope, then trace every material that will be cut, drilled, scraped, sanded, demolished, removed, penetrated, or exposed. EPA lists examples such as floor tile, ceiling tile, and old pipe wrap, but no checklist can identify material content by appearance. Concealed layers are especially important in properties with repeated remodels.",
            ("ol", [
                "Freeze a preliminary room-by-room scope, including mechanical, electrical, plumbing, exterior, roofing, and site-connected work.",
                "Collect original plans, permits, prior surveys, abatement reports, invoices, product records, demolition photographs, and seller disclosures.",
                "Have the accredited inspector define homogeneous areas and an appropriate sampling plan under the applicable program.",
                "Map results to components and exact locations; avoid broad labels such as 'house tested negative' when only selected materials were sampled.",
                "Create a stop-work protocol for newly exposed suspect material and name the person who can authorize additional assessment.",
                "Update the map after abatement or renovation and transfer remaining-material information to the manager and future owner as required.",
            ]),
            f"EPA's <a href=\"{EPA_KNOW}\" rel=\"noopener\">consumer guidance</a> recommends testing suspect material when it is damaged or planned work will disturb it. Do not collect a sample yourself, break a corner to look inside, or let a handyman perform exploratory demolition. Sampling can release fibers and should be planned by the qualified professional.",
        ]),
        ("Worked example: a 1976 cabin launch scope", [
            "Assume an illustrative buyer is evaluating a 1976 cabin. The STR launch scope removes a textured ceiling, replaces resilient flooring and adhesive, opens walls for electrical work, and replaces insulation around old mechanical piping. The seller has no asbestos report, and the general contractor carries ordinary liability insurance but has not identified an asbestos professional.",
            "The year and work create clear diligence questions. Some materials fall within OSHA's pre-1981 presumption framework, while others are simply suspect and require professional evaluation because the work will disturb them. The buyer commissions an accredited, scope-specific assessment before authorizing demolition, asks counsel and the regulator which environmental rules apply, and gives the resulting location-and-quantity information to bidders.",
            "Suppose qualified laboratory results identify asbestos in selected flooring mastic and pipe insulation but not in the sampled ceiling material. The result does not clear untested siding, roofing, wall layers, or another flooring system. The buyer obtains compliant abatement or work-plan bids for the positive components, prices related access and restoration, sets the stop-work protocol, and defines the documentation required before other trades return.",
            "The date, materials, findings, and scope are illustrative—not a report of a BNB Accelerator property or a substitute for inspection. Actual material designations, sampling, regulatory coverage, work classifications, clearance, disposal, and cost depend on the property and jurisdiction.",
        ]),
        ("Compare complete bids, not just removal prices", [
            f"EPA's <a href=\"{EPA_FAMILY}\" rel=\"noopener\">asbestos exposure guidance</a> recommends a written contract that specifies the work plan, cleanup, and applicable federal, state, and local requirements, including notification, removal, handling, and disposal. For an STR acquisition, a bid should also identify schedule and handoff dependencies.",
            ("ul", [
                "Applicability and credentials: legal firm name, licenses or accreditations, competent person, supervisor, worker training, and jurisdiction.",
                "Scope: exact materials, quantities, locations, work classification, access, containment, adjacent areas, and exclusions.",
                "Execution: notifications, regulated areas, engineering controls, protective equipment, decontamination, air monitoring where applicable, and emergency response.",
                "Waste: packaging, labels, transport, approved disposal destination, receipts, and manifest or equivalent records where required.",
                "Reoccupation and handoff: visual inspection, monitoring or clearance criteria where required, remaining ACM map, final report, photographs, and release authority.",
                "Restoration: who repairs walls, flooring, insulation, finishes, mechanical systems, and guest areas after asbestos work is complete.",
            ]),
            "The lowest abatement number can be misleading when it excludes access demolition, replacement materials, licensed trades, extended vacancy, clearance, or disposal. Compare bids against the same material map and acceptance criteria, then move the selected cost and time into the <a href=\"/underwriting/\">acquisition model</a>.",
        ]),
        ("Sequence the STR renovation around controlled access", [
            "Do not install furniture, stock linens, schedule photography, or allow cleaners and designers into an affected area while asbestos work remains unresolved. Separate regulated work from ordinary construction and define who controls access. Workers from other trades can be exposed even when they are not touching the suspect material directly.",
            "A practical sequence is assessment, applicability review, abatement or controlled-work plan, notifications and permits, regulated work, required cleanup and verification, written release, restoration, final property cleaning, furnishing, photography, and launch. The order may differ under local rules, but guest occupancy should never be used to compress a professional safety decision.",
            "If suspect material appears after demolition starts, stop affected work, restrict access, preserve the condition, and trigger the professional assessment process. Do not sweep, vacuum with ordinary equipment, bag loose debris casually, or move it through guest areas. Follow the competent person's and regulator's instructions.",
        ]),
        ("Records become an operating asset", [
            "OSHA requires certain asbestos information and notification records to remain with the building owner for the duration of ownership and transfer to successive owners. Even where a specific federal record provision does not apply to one property, a disciplined permanent file reduces the chance that a future manager, electrician, cleaner, or contractor unknowingly disturbs remaining material.",
            ("ul", [
                "Keep the inspector's qualifications, survey scope, diagrams, sample log, laboratory chain of custody, results, and limitations.",
                "Keep regulator correspondence, notifications, permits, contractor credentials, work plans, daily logs, monitoring and clearance records, disposal evidence, photographs, and final report.",
                "Maintain a current remaining-ACM or presumed-material map and communicate it to contractors before future work.",
                "Write a manager escalation rule for damaged material, leaks, guest incidents, or maintenance that may disturb a listed component.",
                "Store sensitive contractor and property records securely while ensuring authorized operators can retrieve the safety information when needed.",
            ]),
        ]),
        ("Failure modes that turn diligence into a shutdown", [
            ("ul", [
                "Assuming a single-family home is exempt from every asbestos rule because of the federal NESHAP residential exclusion.",
                "Treating pre-1981 as a universal proof of asbestos, or post-1980 as proof that every installed material is asbestos-free.",
                "Identifying flooring, ceiling texture, pipe wrap, siding, or roofing by appearance rather than qualified assessment and laboratory analysis.",
                "Sampling material personally or allowing exploratory demolition before the material map and stop-work procedure exist.",
                "Giving bidders a generic note about asbestos instead of the known location and quantity information and full disturbance scope.",
                "Comparing removal-only bids that exclude containment, other trades, disposal, verification, restoration, and schedule effects.",
                "Launching guests after the abatement crew leaves without the documentation and release required by the applicable plan and authorities.",
            ]),
            ("warn", "Health and legal boundary: this guide summarizes EPA and OSHA materials reviewed September 24, 2026. It is educational, not environmental, occupational-safety, medical, legal, inspection, construction, insurance, or investment advice. Requirements vary by property, work, employer, state, and locality. Use accredited professionals and the responsible regulators."),
        ]),
        ("Turn the survey into a purchase decision", [
            "Before contingencies expire, require a scope-specific assessment or a written professional reason it is not needed, a rule-applicability review, a material map tied to the renovation, comparable qualified bids, a schedule, and a reopening or handoff standard. If concealed layers cannot be assessed until demolition, carry a separately labeled contingency and a contract remedy rather than pretending the risk is zero.",
            "Connect the result to the rest of the property decision: permits, renovation insurance, lender draws, contractor availability, legal STR use, revenue ramp, and reserves. Pair this workflow with the <a href=\"/blog/lead-rrp-pre-1978-str-renovation/\">lead RRP guide</a>, the <a href=\"/blog/vacant-renovation-str-coverage/\">vacant-renovation insurance guide</a>, and the <a href=\"/design/\">BNB Accelerator design process</a>.",
            "Proceed when the material risk is mapped, the work is legally and technically executable, the cost is in the downside case, and the launch sequence protects workers and guests. Renegotiate, redesign, or walk away when the seller will not permit appropriate assessment, the schedule cannot absorb required work, or the complete scope breaks the investment case.",
        ]),
    ],
    "faqs": [
        ("Do you need an asbestos survey before renovating an Airbnb?", "When planned work will disturb suspect material, EPA recommends assessment and sampling by a properly trained and accredited asbestos professional. The exact survey and legal requirements depend on the property, work, and jurisdiction."),
        ("Are single-family STRs exempt from asbestos rules?", "Not from every rule. A federal environmental provision excludes some residential buildings with four or fewer units, but exceptions, OSHA worker-protection duties, and state or local rules can still apply."),
        ("Can you tell whether flooring or a ceiling contains asbestos by looking?", "No. EPA says asbestos content cannot be determined by appearance alone. Qualified sampling and laboratory analysis are used when suspect material will be disturbed or is damaged."),
        ("Does every pre-1981 material contain asbestos?", "No. OSHA requires certain pre-1981 thermal insulation, surfacing material, and resilient flooring systems to be presumed asbestos-containing unless properly rebutted. Other materials need fact-specific evaluation."),
        ("What should an STR buyer obtain after asbestos work?", "The package depends on applicable requirements but commonly includes professional reports, credentials, notifications, work records, monitoring or clearance evidence where required, disposal records, photographs, and an updated map of remaining material."),
    ],
    "related": [
        '<a href="/blog/lead-rrp-pre-1978-str-renovation/">Review lead RRP requirements</a>',
        '<a href="/blog/vacant-renovation-str-coverage/">Arrange renovation-period insurance</a>',
        '<a href="/blog/inspection-contingency-length-str/">Set a workable diligence timeline</a>',
        '<a href="/underwriting/">Model the complete acquisition scope</a>',
        '<a href="/design/">Coordinate the STR renovation design</a>',
    ],
    "cta_h": "Buying an older STR that needs demolition or repair?",
    "cta_p": "BNB Accelerator can help source and underwrite the property, define the launch scope, and coordinate acquisition diligence while accredited asbestos, construction, legal, environmental, and insurance professionals handle their requirements.",
}


if __name__ == "__main__":
    blog.build([POST])
    print(f"candidate score: {sum(SCORE.values())}/100 — {SCORE}")
