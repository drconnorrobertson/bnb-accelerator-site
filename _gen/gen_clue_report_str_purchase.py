#!/usr/bin/env python3
"""Generate the property claim-history guide for STR buyers."""
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

TEXAS_DOI = "https://www.tdi.texas.gov/tips/check-your-propertys-insurance-claim-history.html"
WASHINGTON_OIC = "https://www.insurance.wa.gov/insurance-resources/auto-insurance/credit-and-insurance/clue-comprehensive-loss-underwriting-exchange"
CFPB_CLUE = "https://www.consumerfinance.gov/consumer-tools/credit-reports-and-scores/consumer-reporting-companies/companies-list/comprehensive-loss-underwriting-exchange/"
CFPB_SHARING = "https://www.consumerfinance.gov/ask-cfpb/do-auto-and-homeowners-insurance-companies-share-my-information-about-claims-en-1821/"
LEXIS_CLUE = "https://risk.lexisnexis.com/products/clue-property"
FTC_INSURERS = "https://www.ftc.gov/business-guidance/resources/consumer-reports-what-insurers-need-know"
NAIC_POLICY = "https://content.naic.org/article/consumer-insight-understanding-your-homeowners-or-renters-policy"

POST = {
    "slug": "clue-report-before-buying-str",
    "title": "C.L.U.E. reports before buying a short-term rental",
    "title_tag": "C.L.U.E. Report Before Buying an STR | Buyer Guide",
    "h1": "Should you ask for a C.L.U.E. report before buying an STR?",
    "description": "Buying an Airbnb? Use this C.L.U.E.-report framework to reconcile past claims, repairs, inspections, insurance quotes, contingencies, and closing risk.",
    "date": DATE,
    "category": "Acquisition Diligence",
    "lead": "Ask the seller for a current property claim-history report early enough to investigate every listed loss and obtain a property-specific insurance decision before the applicable contingency expires. A C.L.U.E. report can reveal reported loss dates, categories, and payments that affect underwriting or point to repairs worth inspecting. It is not a damage survey, repair certificate, complete property history, disclosure substitute, or promise that an STR policy will bind. The buyer must reconcile the report with the building, repair file, seller disclosures, and insurer response.",
    "sections": [
        ("The direct answer for an STR buyer", [
            f"Yes—when the seller can lawfully obtain and share an appropriate report, include it in acquisition diligence. The <a href=\"{TEXAS_DOI}\" rel=\"noopener\">Texas Department of Insurance</a> says buyers can ask an owner to show the property's C.L.U.E. report, and that insurers use past claims as one factor in pricing homeowners insurance. The <a href=\"{WASHINGTON_OIC}\" rel=\"noopener\">Washington Office of the Insurance Commissioner</a> likewise says the owner must request a report for a property a prospective buyer wants to evaluate.",
            "Order the insurance quote in parallel rather than waiting to interpret the report yourself. The seller's consumer disclosure and the carrier's underwriting process are related but not interchangeable. The carrier must evaluate the actual applicant, address, proposed short-term-rental use, occupancy, renovations, amenities, protection systems, limits, deductibles, and other underwriting facts.",
            ("callout", "Buying a property with a water, fire, roof, liability, theft, or catastrophe history? <a href=\"/apply/\">Apply for a BNB Accelerator strategy call</a> to integrate the loss file with inspections, underwriting, insurance timing, repair reserves, and the offer. Qualified insurance, inspection, engineering, environmental, legal, lending, and contracting professionals must make their respective determinations."),
        ]),
        ("Understand what C.L.U.E. is—and what it is not", [
            f"C.L.U.E. stands for Comprehensive Loss Underwriting Exchange. The <a href=\"{CFPB_CLUE}\" rel=\"noopener\">Consumer Financial Protection Bureau's company listing</a> describes it as a claims-information exchange that collects and reports up to seven years of home-insurance and personal-property claims for insurance pricing and underwriting. The CFPB says a consumer can request one free report every 12 months and that requesting one's own report does not hurt credit scores.",
            f"LexisNexis describes <a href=\"{LEXIS_CLUE}\" rel=\"noopener\">C.L.U.E. Property</a> as a consumer-reporting-agency product containing property loss history such as loss date, cause, and amount paid. LexisNexis also warns that source data can contain errors and should be independently verified. That limitation belongs in the buyer's process: an entry is a lead to reconcile, while a blank report is not a whole-building clearance.",
            ("table", ["Evidence", "What it can establish", "What it cannot establish"], [
                ["C.L.U.E. or other loss-history report", "Claims attributed to the matching person or property criteria within the report's period and data sources.", "Every loss, unreported damage, repair quality, current condition, future coverage, or legal disclosure compliance."],
                ["Seller disclosure", "The seller's representations and known conditions under the applicable form and law.", "Independent verification, full insurance history, or insurer acceptance."],
                ["Claim and repair file", "Adjuster scope, payments, mitigation, contractor work, permits, photos, warranties, or completion evidence that actually exists.", "That concealed conditions are sound or every paid item was completed correctly."],
                ["Property inspection or specialist report", "Observed condition and testing within a defined scope on a specific date.", "The complete claims database or a guarantee against future loss."],
                ["Insurance quote or binder", "The carrier's current offer or bound terms for the disclosed risk, subject to its documents and conditions.", "A warranty of property condition or coverage outside the actual policy."],
            ]),
        ]),
        ("Ask the seller for the right package", [
            "A buyer generally should not attempt to order another person's consumer report. Ask the seller, through the transaction process and with counsel where appropriate, to obtain their current property report and share the property-relevant portion in a secure manner. The report can include personal identifiers and policy information, so unnecessary personal data should be handled and redacted under professional guidance rather than posted in a shared marketing folder.",
            ("ol", [
                "Request the current report for the exact property address and ask when it was generated, by whom, and which reporting company produced it.",
                "Ask for seller disclosures, a written list of all known losses and claims, and clarification of any event that did not result in a claim.",
                "For each reported loss, request claim correspondence, adjuster estimates, mitigation and remediation records, contractor invoices, permits, inspections, photographs, laboratory or engineering reports when relevant, warranties, and proof of completion.",
                "Ask about open claims, supplemental payments, recoverable depreciation, subrogation, litigation, code-upgrade work, lender-held proceeds, unfinished repairs, exclusions added after a loss, and prior nonrenewal or cancellation notices—without assuming any one item applies.",
                "Document material mismatches by date, location, loss type, claimed amount, repair scope, and present condition. Let counsel address disclosure duties and contract consequences.",
                "Transmit the actual known loss and repair facts to the prospective insurer and relevant specialists before the buyer's deadlines.",
            ]),
            f"The CFPB confirms that <a href=\"{CFPB_SHARING}\" rel=\"noopener\">specialty consumer reporting agencies collect property-and-casualty claims information</a> and that insurers may use those reports to decide what policies to offer and what premiums to charge. The buyer therefore needs both sides of the file: evidence about the property's condition and an insurer's response to the disclosed history.",
        ]),
        ("Read every claim as a question, not a verdict", [
            "Create one row for each entry and translate it into a physical-condition and insurance question. The amount paid is not the same as repair cost, current value, or damage severity. A zero-payment or denied claim can still correspond to an event worth understanding. A large payment can reflect a broad restoration that was completed well—or one that remains incomplete. The report alone cannot decide which.",
            ("table", ["Reported loss type", "Physical follow-up", "Insurance follow-up"], [
                ["Water, freezing, backup, or appliance discharge", "Locate source; review dry-out and remediation; inspect affected assemblies, plumbing, drainage, HVAC, finishes, and recurrence controls.", "Confirm how the carrier classifies the cause, whether repairs are documented, and what water, backup, mold, or freeze terms apply."],
                ["Roof, wind, hail, or catastrophe", "Match event to roof planes, exterior, windows, siding, structure, permits, invoices, and remaining service life.", "Confirm roof age/material, inspection requirements, wind/hail deductible, cosmetic exclusions, actual-cash-value terms, and mitigation credits."],
                ["Fire, smoke, or electrical", "Review origin-and-cause information when available, electrical and structural work, smoke remediation, permits, final inspections, and affected systems.", "Disclose the event and completed corrections; ask what inspections or records are required to bind."],
                ["Liability, animal, pool, trampoline, or guest injury", "Identify the physical or operating hazard and whether it remains at the property.", "Confirm business-use, premises-liability, amenity, animal, and umbrella eligibility with the actual STR program."],
                ["Theft or vandalism", "Review entry points, vacant periods, alarm/access changes, neighborhood context, and remaining damage.", "Ask about occupancy, vacancy, protective-device, theft, and short-term-rental conditions."],
                ["Unknown, duplicate, or mismatched entry", "Do not invent a cause; compare address, date, records, and seller history.", "Have the report owner use the reporting company's dispute process and keep the carrier informed of timing."],
            ]),
            "Use a specialist appropriate to the loss rather than asking one general inspector to certify everything. A water claim may need plumbing, envelope, moisture, mold, or drainage expertise. A fire may need electrical, structural, code, or environmental review. A roof claim may require roofing and wind-mitigation documentation. The necessary scope comes from the event and current evidence.",
        ]),
        ("Reconcile four files before removing contingencies", [
            "The decision is strongest when four independent views agree: the claims report, the seller's disclosure and repair records, the physical investigation, and the insurer's underwriting response. Build an exception log rather than forcing agreement where evidence is missing.",
            ("table", ["Pattern", "What it means", "Buyer response"], [
                ["All four align", "The event, repair, present condition, and insurance response tell a consistent story.", "Preserve evidence, price remaining life and deductibles, and confirm final binding conditions."],
                ["Claim exists; seller file is thin", "A loss was reported, but completed scope or cause correction is not demonstrated.", "Obtain original records and targeted inspection; carry unresolved work as a real decision risk."],
                ["Seller discloses damage; report is blank", "The event may have been uninsured, outside the report period, unreported, omitted, or associated differently.", "Investigate the event; do not treat the blank report as proof it did not happen."],
                ["Repairs look complete; insurer adds conditions", "Physical correction does not guarantee underwriting acceptance or desired terms.", "Compare qualified markets, satisfy reasonable documentation needs, and model actual terms before the deadline."],
                ["Report appears wrong or unrelated", "The owner may need to dispute source data; the buyer cannot erase it by explanation.", "Preserve contract flexibility while the owner follows the formal dispute process and carriers reassess."],
                ["Seller refuses or cannot provide it", "The buyer has less evidence; the reason may be procedural, privacy-related, or substantive.", "Use counsel and the contract, seek alternate records, obtain early carrier review, increase uncertainty, or decline."],
            ]),
        ]),
        ("Run insurance diligence in parallel", [
            f"The <a href=\"{NAIC_POLICY}\" rel=\"noopener\">National Association of Insurance Commissioners</a> notes that insurers commonly review claims history when a new policy is written or renewed and may use C.L.U.E. or similar reports. That does not mean every carrier interprets the same entry the same way. Underwriting rules, eligible uses, deductibles, exclusions, documentation, inspections, valuation, catastrophe capacity, and pricing differ.",
            "Give the broker or carrier a complete description of the proposed operation: short-term-rental use, whether the owner occupies any portion, entity and named-insured structure, maximum guests, amenities, pools or hot tubs, fireplaces, docks, watercraft, events, renovations, vacancy before opening, property management, and any commercial activity. A quote premised on owner occupancy or ordinary long-term residential use may not answer the STR question.",
            ("ul", [
                "Ask whether the quote is preliminary, conditionally approved, bindable, or bound, and list every outstanding inspection, photo, repair, form, payment, and underwriting condition.",
                "Compare coverage forms, valuation, limits, deductibles, sublimits, exclusions, endorsements, business-income assumptions, ordinance or law, equipment breakdown, water backup, service line, flood, earthquake, wind, named storm, and umbrella compatibility as applicable.",
                "Confirm replacement-cost assumptions and whether the planned renovation, vacancy, or construction requires a different policy before the permanent STR program begins.",
                "Do not rely on a seller's premium. The buyer, use, carrier, market, limits, deductibles, property data, and effective date can produce different terms.",
            ]),
            "Put the actual premium, deductibles, exclusions, required improvements, and coverage gaps into the <a href=\"/underwriting/\">acquisition model</a>. Insurance feasibility is not just a closing checkbox; it affects fixed cost, downside severity, renovation sequence, guest capacity, amenity design, and whether the investment can operate as planned.",
        ]),
        ("Handle errors and adverse decisions correctly", [
            "If the seller believes an entry is inaccurate, the seller—not the buyer—should use the consumer-reporting company's dispute process and supply supporting evidence. The buyer can track the issue, keep contract deadlines visible, ask the carrier what documentation it can consider, and decide whether unresolved timing is acceptable. A verbal explanation does not amend the database.",
            f"The <a href=\"{FTC_INSURERS}\" rel=\"noopener\">Federal Trade Commission's FCRA guidance for insurers</a> says a permissible purpose is required to obtain a consumer report, generally insurance underwriting involving the consumer or the consumer's permission. It also explains that when adverse insurance action is based partly or completely on a consumer report, the insurer must provide a notice identifying the reporting agency and the consumer's rights to a free report and to dispute inaccurate or incomplete information.",
            "A buyer should not diagnose legal compliance from an adverse-action notice. Read it, preserve it, request the identified report promptly, compare the data with the application, and speak with the carrier, reporting agency, insurance professional, and counsel as appropriate. The reporting agency supplies information; it does not make the underwriting decision.",
        ]),
        ("Worked example: repeat water claims in a future game room", [
            "Assume an illustrative buyer is under contract for a cabin whose finished lower level will become a game room and bunk area. The seller disclosure mentions one washing-machine leak repaired three years ago. The seller-provided claim report lists two water losses eighteen months apart, with different loss dates and payment amounts. The basement has new flooring and wall paneling, but the file contains only one mitigation invoice.",
            "The buyer creates two claim rows and requests the carrier correspondence, adjuster scopes, drying records, plumbing invoices, photographs, permits, and proof of both completed repairs. A qualified moisture and building investigation maps each reported source and affected assembly. The plumber evaluates the corrected supply and drainage work. The buyer sends the loss history, reports, planned STR use, and proposed sleeping layout to the insurance broker.",
            "If the second entry is a duplicate, the seller follows the formal dispute path while the buyer preserves the deadline. If it represents a separate unresolved backup or recurring drainage problem, the team expands the physical scope, prices correction and reconstruction, and reviews coverage terms. If the carrier will bind only after specified work, those conditions join the renovation schedule and closing remedy. The report triggered the questions; it did not answer them.",
            "This cabin, sequence, and outcomes are illustrative—not a client result, insurance promise, engineering opinion, environmental conclusion, or legal determination. The actual investigation and coverage response depend on the records, building, jurisdiction, applicant, use, and carrier.",
        ]),
        ("Structure the contract and closing decision", [
            "Request the report and insurance work early. The seller needs time to order the disclosure; the buyer needs time to obtain underlying claim records, schedule specialists, receive quotes, respond to carrier conditions, and resolve mismatches before inspection and insurance deadlines. Counsel should adapt the contract language to the jurisdiction rather than relying on a generic 'clean C.L.U.E.' phrase.",
            ("ol", [
                "Define which report or loss history the seller will provide, the property address, recency, delivery deadline, and permitted treatment of personal information.",
                "Preserve the buyer's right to investigate each loss, receive repair evidence, obtain insurance acceptable to the buyer and lender, and use the applicable termination or renegotiation remedy.",
                "Do not define success as 'no claims.' A documented claim with a durable repair and acceptable insurance may be manageable; a blank report with obvious damage may not be.",
                "If seller work is proposed, define scope, contractor qualifications, permits, access, documentation, inspections, warranties, completion timing, carrier acceptance, and what happens when concealed conditions expand the work.",
                "If using a credit, price change, or escrow, confirm lender, title, insurer, and counsel approval and model uncovered overruns and launch delay. Money does not cure an uninsurable condition by itself.",
                "Before closing, obtain the final policy evidence required by the lender and buyer, verify no material facts changed, and retain the complete claim-and-repair file for operations and resale.",
            ]),
        ]),
        ("Failure modes that turn claim history into a closing surprise", [
            ("ul", [
                "Waiting until the week of closing to ask the seller for the report or start STR insurance underwriting.",
                "Treating a blank report as proof that the property never suffered damage.",
                "Treating a claim payment as proof that every damaged item was repaired properly.",
                "Comparing the report only with the disclosure and skipping physical inspection and repair records.",
                "Assuming a standard homeowners quote covers the disclosed short-term-rental use, amenities, vacancy, or renovation.",
                "Sharing an unredacted consumer report broadly or attempting to order someone else's report without a lawful basis.",
                "Letting the buyer, agent, or inspector guess why an entry is wrong instead of having the report owner use the formal dispute process.",
                "Relying on the seller's old premium, carrier, or policy instead of the buyer's bindable terms.",
                "Accepting a credit without pricing the physical work, insurance effect, schedule, exclusions, and unresolved downside.",
            ]),
            ("warn", "This guide summarizes federal and selected state insurance sources reviewed September 24, 2026. It is educational, not insurance, legal, privacy, credit-reporting, inspection, engineering, environmental, lending, contracting, tax, or investment advice. Report access, disclosures, dispute rights, underwriting practices, coverage, and transaction remedies vary by person, policy, property, carrier, state, and contract. Use qualified professionals and current source documents."),
        ]),
        ("Turn the loss file into a go, renegotiate, or walk decision", [
            "Proceed when the reported losses and known damage reconcile with the seller file, targeted inspections, completed repairs, and insurance terms; remaining work and deductibles fit the model; and the planned STR use can be bound on acceptable terms. Renegotiate when a defined condition has a repair and insurance path but the original price or opening date ignored it. Walk when the seller blocks material diligence, recurring damage remains unresolved, records and conditions cannot be reconciled, or acceptable coverage cannot be secured within the contract and investment constraints.",
            "Pair this workflow with the <a href=\"/blog/mold-inspection-before-buying-str/\">moisture and mold assessment guide</a>, the <a href=\"/blog/roof-inspection-short-term-rental/\">roof inspection guide</a>, the <a href=\"/blog/vacant-renovation-str-coverage/\">renovation-period coverage guide</a>, and the <a href=\"/blog/inspection-contingency-length-str/\">inspection timeline framework</a>. Each handles a different part of the decision.",
            "The practical next step is to request the current report, place every entry in a reconciliation table, attach the corresponding disclosure and repair evidence, assign a qualified physical follow-up, and send the complete facts to the prospective STR insurer before the buyer's deadlines.",
            ("callout", "Need a property's claim history translated into inspections, insurance conditions, reserves, and a purchase decision? <a href=\"/apply/\">Apply for a BNB Accelerator strategy call</a>. We can coordinate the acquisition framework while qualified insurance, legal, inspection, engineering, and repair professionals handle their conclusions."),
        ]),
    ],
    "faqs": [
        ("Can a home buyer order the seller's C.L.U.E. report?", "A prospective buyer generally asks the current owner to request the property report. Follow the transaction process, privacy requirements, and legal guidance rather than attempting to obtain another person's consumer report directly."),
        ("How many years of claims can a C.L.U.E. report contain?", "The CFPB and state insurance regulators describe C.L.U.E. as reporting up to seven years of home or personal-property claims. The actual report and matching data control, and older or unreported damage may not appear."),
        ("Does a blank C.L.U.E. report prove the house has no damage?", "No. Damage may have been uninsured, unreported, outside the reporting period, associated differently, or absent from the contributing data. Compare the report with disclosures, records, inspections, and the building itself."),
        ("Does a paid insurance claim prove the repair was completed?", "No. A payment entry does not establish the exact damage, work performed, contractor quality, permits, final condition, or correction of the original cause. Obtain the underlying claim and repair file and inspect the relevant systems."),
        ("Can prior property claims affect an STR insurance quote?", "Insurers may consider claims history when deciding eligibility, price, coverage, deductibles, inspections, or required repairs. The effect varies by carrier and facts, so disclose the planned STR use and obtain property-specific terms early."),
        ("What if an entry on the report is wrong?", "The report owner should use the consumer-reporting company's dispute process and supporting records. Keep purchase deadlines visible and ask the insurer what it can consider while the dispute is pending."),
    ],
    "related": [
        '<a href="/blog/mold-inspection-before-buying-str/">Investigate water and mold history</a>',
        '<a href="/blog/roof-inspection-short-term-rental/">Inspect the roof after prior losses</a>',
        '<a href="/blog/vacant-renovation-str-coverage/">Arrange renovation-period coverage</a>',
        '<a href="/underwriting/">Model premiums, deductibles, and repairs</a>',
        '<a href="/apply/">Discuss the acquisition strategy</a>',
    ],
    "cta_h": "Buying an STR with a prior insurance claim?",
    "cta_p": "BNB Accelerator can help source and underwrite the property, coordinate the loss-history decision, and translate repair and coverage evidence into an acquisition plan while qualified professionals handle insurance, legal, inspection, and repair conclusions.",
}


if __name__ == "__main__":
    blog.build([POST])
    print(f"candidate score: {sum(SCORE.values())}/100 — {SCORE}")
