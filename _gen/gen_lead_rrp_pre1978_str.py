#!/usr/bin/env python3
"""Generate the EPA lead RRP decision guide for pre-1978 STR renovations."""
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

RRP = "https://www.epa.gov/lead/lead-renovation-repair-and-painting-program"
CONTRACTORS = "https://www.epa.gov/lead/renovation-repair-and-painting-program-contractors"
WORK = "https://www.epa.gov/lead/renovation-repair-and-painting-program-work-practices"
DISCLOSURE = "https://www.epa.gov/lead/lead-based-paint-disclosure-rule-section-1018-title-x"
INVESTOR_FAQ = "https://www.epa.gov/lead/i-have-profit-business-where-i-purchase-residential-properties-and-renovate-them-type"

POST = {
    "slug": "lead-rrp-pre-1978-str-renovation",
    "title": "EPA lead RRP rules for a pre-1978 STR renovation",
    "title_tag": "Does EPA Lead RRP Apply to a Pre-1978 Airbnb?",
    "h1": "Does the EPA lead RRP rule apply when renovating a pre-1978 STR?",
    "description": "Renovating a pre-1978 Airbnb? Use this EPA lead RRP checklist to scope testing, certified contractors, work practices, records, and closing diligence.",
    "date": DATE,
    "category": "Acquisition Diligence",
    "lead": "Usually, assume the federal Renovation, Repair and Painting rule applies when a paid contractor disturbs painted surfaces in a pre-1978 short-term rental, unless a documented exclusion covers the housing, components, or work. An investor who performs covered work personally—or through employees—can also trigger certification duties because the work supports a rental business. The practical mistake is treating the short-stay exception in the separate lead disclosure rule as an exemption from renovation requirements. It is not. Screen the property, painted components, work scope, contractor credentials, and state program before pricing or starting the renovation.",
    "sections": [
        ("The direct answer for an STR buyer", [
            f"EPA's <a href=\"{RRP}\" rel=\"noopener\">Lead Renovation, Repair and Painting Program</a> says that anyone paid to disturb painted surfaces in pre-1978 housing generally must be certified and use trained workers and lead-safe practices. The agency also says the rule can apply when an owner rents all or part of the home, and when an investor buys, renovates, and sells homes for profit. Calling the property a vacation rental, cabin, or Airbnb does not decide the question.",
            "For acquisition purposes, the year built is only the first gate. The buyer must identify whether the building is covered target housing, which surfaces the scope will disturb, whether qualified testing has removed any components from the rule, who will perform the work, and whether EPA or an authorized state or Tribal program administers the job. Put those answers in the renovation estimate before the inspection period expires.",
            ("callout", "Considering an older home that needs a launch renovation? <a href=\"/apply/\">Apply for a BNB Accelerator strategy call</a> to pressure-test the property, improvement scope, opening timeline, and reserves. Qualified lead professionals, contractors, and counsel must determine and perform the required compliance work."),
        ]),
        ("Use this five-gate RRP decision tree", [
            ("table", ["Gate", "Question", "Evidence to collect"], [
                ["1. Building", "Was the house or covered child-occupied facility built before 1978?", "Assessor record, permit history, certificate of occupancy, and addition dates."],
                ["2. Housing", "Is it covered target housing rather than an excluded housing type?", "Unit configuration, occupancy facts, and any certified lead-free determination."],
                ["3. Scope", "Will work disturb painted surfaces beyond an applicable exclusion?", "Room-by-room surface map, quantities, demolition, and window work."],
                ["4. Performer", "Who will perform, offer, or direct the work?", "Owner, employee, property manager, general contractor, and every affected trade."],
                ["5. Program", "Does EPA or an authorized state or Tribal program govern?", "Job address, current program authority, firm certificate, and renovator assignment."],
            ]),
            "If a gate is unresolved, budget and schedule as though covered until the qualified team documents otherwise. That does not mean every old home contains lead-based paint or every maintenance task is regulated. It means the buyer should not use appearance, a seller statement, or a contractor's ordinary license as proof of an RRP exclusion.",
            "The rule is broader than painting. EPA lists remodeling, maintenance, electrical work, plumbing, carpentry, paint preparation, and window replacement among potentially covered activities because these trades can disturb painted surfaces. The renovation plan—not the line item name—determines what needs review.",
        ]),
        ("Do not confuse purchase disclosure, guest leases, and renovation", [
            f"The federal <a href=\"{DISCLOSURE}\" rel=\"noopener\">Lead-Based Paint Disclosure Rule</a> generally requires sellers of most pre-1978 housing to disclose known lead-based paint information and available records before a buyer signs the contract, provide the federal pamphlet, include contract language, and give the buyer a 10-day opportunity to conduct an inspection or risk assessment unless the parties change that period in writing.",
            "That disclosure framework contains an exception for leases of 100 days or less, such as short-term vacation rentals when renewal or extension cannot occur. The exception concerns that particular rental disclosure rule. It does not turn a pre-1978 investment property into post-1977 housing, certify painted components as lead-free, or exempt the owner's renovation from RRP.",
            ("ul", [
                "At purchase: obtain the seller's disclosure, reports, notices, paint tests, risk assessments, and renovation records before waiving the inspection opportunity.",
                "Before work: determine RRP coverage from the building, scope, testing, performer, and jurisdiction—not from the intended average guest stay.",
                "During operations: separately confirm federal, state, local, licensing, and platform duties for guest disclosures and known hazards.",
            ]),
        ]),
        ("Scope thresholds are not a permission slip to divide a project", [
            f"EPA's <a href=\"{CONTRACTORS}\" rel=\"noopener\">contractor guidance</a> describes a minor repair and maintenance exclusion for work disturbing six square feet or less of paint per room inside or 20 square feet or less on the exterior. Window replacement and demolition of painted surfaces are covered regardless of square footage, and prohibited practices remain prohibited regardless of area.",
            "Measure disturbed paint, not the room's floor area or the new material's size. A bathroom vanity replacement may disturb wall paint, trim, fastener points, and adjoining surfaces. Replacing several windows is not minor work merely because each opening is small. Electrical and plumbing penetrations can accumulate into a covered scope.",
            "Do not split one planned project into artificial micro-jobs to stay under a threshold. Give the certified renovator the complete contemporaneous scope and let the qualified firm document its applicability analysis. If the design changes, re-screen the work before crews expand into new rooms or components.",
        ]),
        ("Testing can narrow the scope, but the tester matters", [
            "RRP paint testing is not mandatory, but EPA says the rule applies unless there is qualifying documentation that affected paint is not lead-based. A certified renovator can use an EPA-recognized test kit or collect paint-chip samples for an EPA-recognized laboratory. Certified lead inspectors or risk assessors can use additional approved methods and can evaluate components more broadly.",
            "A hardware-store test performed by the buyer, seller, cleaner, or uncertified contractor is not the same as a rule-compliant determination. Nor does a renovated-looking room prove the underlying trim, doors, windows, siding, or earlier paint layers are free of regulated lead. Test the components the final scope will actually disturb and retain the written determination.",
            ("ol", [
                "Freeze a preliminary room-by-room scope before requesting testing.",
                "Identify every painted or coated component the work may cut, sand, drill, demolish, remove, or replace.",
                "Choose the qualified tester and method based on the decision needed: component-specific RRP screening, inspection, or risk assessment.",
                "Map results back to the estimate; do not describe the whole property as lead-free from limited component tests.",
                "Preserve reports and revise the map when demolition exposes another layer or the design changes.",
            ]),
        ]),
        ("Owner labor, employees, managers, and outside firms", [
            f"EPA's <a href=\"{INVESTOR_FAQ}\" rel=\"noopener\">investor renovation FAQ</a> says an individual who buys residential property for profit and personally performs covered pre-1978 work is performing for compensation and must be a certified renovator and Lead-Safe Certified Firm. The same concept applies when a business uses its own employees. A landlord or property manager should not assume that calling paid work 'in-house maintenance' removes it from the rule.",
            "If the owner hires an outside firm to perform all the covered work, EPA says the owner does not need firm or renovator certification solely on that basis, but the hired firm must be Lead-Safe Certified and use a trained, certified renovator. Verify the firm certificate against the legal entity on the contract, confirm the assigned certified renovator, and address subcontractors rather than accepting a logo or verbal statement.",
            "A general contractor's ordinary license, insurance certificate, or lead-abatement credential does not automatically prove the specific RRP firm and renovator requirements are satisfied. Ask the lead professional which credentials apply to this work and jurisdiction, and make compliance a written contract deliverable.",
        ]),
        ("Worked example: a 1965 cabin launch renovation", [
            "Assume an investor is buying an illustrative 1965 three-bedroom cabin to operate as a short-term rental. The launch scope includes interior repainting, removal of two painted walls, replacement of eight windows, new electrical openings, and replacement of painted exterior trim. The investor's handyman proposes to start demolition immediately after closing.",
            "The project has strong RRP signals: pre-1978 housing, paid work, demolition, window replacement, and substantial painted-surface disturbance. The minor-repair exclusion does not rescue the windows or wall demolition. Before closing, the buyer should obtain purchase disclosures and historical reports, have the final components reviewed or tested by qualified professionals, verify the governing program, and bid the covered scope through a certified firm with an assigned certified renovator.",
            "Now suppose qualified testing documents that certain 1985 replacement windows and one later addition are free of regulated lead paint for the affected components. That evidence may narrow the covered scope, but it does not automatically clear original trim, siding, doors, or the 1965 rooms. The buyer updates the component map and estimate rather than announcing that the cabin passed a lead test.",
            "All dates, quantities, and scope details are illustrative, not a report of a BNB Accelerator property. Actual coverage, testing, containment, cleaning, clearance, scheduling, and cost depend on the property, work, program, and qualified professionals.",
        ]),
        ("Build the compliance package into bids and the budget", [
            f"EPA's <a href=\"{WORK}\" rel=\"noopener\">RRP work-practice guidance</a> covers pre-renovation education, dust containment, cleaning, and job records. It says required records are kept for three years, including certification and training documentation, certified-renovator designation, qualifying test results, inspection reports, proof of pre-renovation education, and required project reports.",
            ("ul", [
                "Bid assumptions: identified components, test basis, occupied or vacant status, furniture protection, access, utilities, and sequencing.",
                "Credentials: exact certified firm, certificate expiration, assigned certified renovator, worker training, and subcontractor responsibilities.",
                "Execution: containment plan, prohibited-practice controls, daily cleanup, waste movement, verification, and stop-work process for hidden conditions.",
                "Handoff: records, photographs, test reports, receipts, cleaning verification, change orders, and a component-level summary for the property file.",
                "Economics: compliance labor, testing, temporary vacancy, slower sequencing, contingency, and possible redesign—not an invented universal cost per square foot.",
            ]),
            "Avoid budgeting one generic 'lead allowance.' The useful model separates known certified work, testing decisions, scope uncertainty, schedule impact, and a contingency for newly exposed components. That makes bids comparable and shows whether the property still clears the <a href=\"/underwriting/\">acquisition underwriting</a> after a compliant launch scope.",
        ]),
        ("Check the governing program and the local layers", [
            "EPA administers RRP in most jurisdictions, while authorized states and one Tribe operate their own programs in lieu of the federal program. That list can change, and firms working across jurisdictions may need different certifications. Use the current EPA firm-certification page and the job address rather than a contractor's home office to identify the governing program.",
            "RRP is not the only layer. State and local lead laws, housing codes, worker-safety rules, building permits, waste requirements, lender conditions, insurance provisions, and child-occupied-facility rules can add duties. A lead abatement project also has a different purpose and credential framework from ordinary renovation that disturbs paint. Ask the qualified lead professional to identify which category the scope falls into.",
            ("warn", "Health and legal boundary: this guide summarizes federal EPA materials reviewed September 24, 2026. It is educational, not legal, environmental, health, construction, occupational-safety, insurance, or investment advice. Programs and project facts differ. Use the applicable regulator, a certified lead professional, qualified contractors, and counsel."),
        ]),
        ("Failure modes and the practical next step", [
            ("ul", [
                "Assuming the short-term guest-lease disclosure exception also exempts the owner's renovation work.",
                "Letting demolition start during a tight launch schedule before coverage, testing, and credentials are documented.",
                "Accepting a consumer test kit or a seller's fresh paint as proof that affected components are lead-free.",
                "Treating window replacement, wall demolition, or prohibited practices as minor maintenance because the visible area looks small.",
                "Verifying only the general contractor while ignoring the legal firm, certified renovator, property manager, handyman, and subcontractors who disturb paint.",
                "Keeping no project file after the listing launches, leaving the owner unable to reproduce the testing, education, work-practice, or cleaning record.",
            ]),
            "Before the inspection period ends, require four outputs: a dated lead-disclosure file, a component-and-scope map, written identification of the governing program, and at least one bid from a properly certified firm that states its compliance deliverables. Put the cost and schedule into the downside case alongside permits, insurance, financing, and revenue ramp.",
            "If the property still works, sequence the certified work before furniture and photography, protect the launch date with contingency, and preserve the complete record. Pair this diligence with the <a href=\"/blog/vacant-renovation-str-coverage/\">renovation insurance guide</a>, the <a href=\"/blog/certificate-of-occupancy-str-remodel/\">certificate-of-occupancy remodel guide</a>, and the <a href=\"/design/\">BNB Accelerator design process</a>. If the scope no longer works, renegotiate or walk away based on evidence rather than hiding the risk under a cosmetic renovation budget.",
        ]),
    ],
    "faqs": [
        ("Does the EPA RRP rule apply to an Airbnb built before 1978?", "It often applies when paid work disturbs painted surfaces in covered pre-1978 housing. Short-term-rental branding does not create an RRP exemption. The housing, scope, testing, performer, and governing program must be checked."),
        ("Does the 100-day vacation-rental exception remove RRP duties?", "No. That exception belongs to the federal lead disclosure rule for certain short leases. It does not by itself exempt renovation, repair, or painting work from RRP."),
        ("Can an STR owner perform the work personally without certification?", "Not automatically. EPA says an investor or landlord performing covered work for a rental or profit can be performing for compensation and may need firm and renovator certification."),
        ("Is every small paint repair covered?", "EPA describes a minor repair exclusion at six square feet or less per interior room or 20 square feet or less outside, but window replacement, painted-surface demolition, and prohibited practices are not rescued by those limits."),
        ("Can a home test kit prove the STR is lead-free?", "Not for an RRP exclusion when used by an unqualified person. EPA requires qualifying determinations by specified certified professionals using recognized methods, with the affected components and records clearly documented."),
    ],
    "related": [
        '<a href="/blog/vacant-renovation-str-coverage/">Insure the property during renovation</a>',
        '<a href="/blog/certificate-of-occupancy-str-remodel/">Check certificate-of-occupancy impacts</a>',
        '<a href="/design/">Plan the design and improvement scope</a>',
        '<a href="/underwriting/">Model the complete acquisition budget</a>',
        '<a href="/partners/">Coordinate with qualified specialists</a>',
    ],
    "cta_h": "Buying a pre-1978 STR that needs renovation?",
    "cta_p": "BNB Accelerator can help source and underwrite the property, define the launch scope, and coordinate acquisition diligence while certified lead, construction, legal, and insurance professionals handle their technical requirements.",
}


if __name__ == "__main__":
    blog.build([POST])
    print(f"candidate score: {sum(SCORE.values())}/100 — {SCORE}")
