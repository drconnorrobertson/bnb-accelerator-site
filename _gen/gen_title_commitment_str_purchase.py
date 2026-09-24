#!/usr/bin/env python3
"""Generate the title-commitment review guide for STR buyers."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import blog

DATE = "2026-09-24"
SCORE = {
    "distinct_search_intent": 30,
    "buyer_relevance": 25,
    "real_question": 15,
    "service_fit": 12,
    "original_decision_support": 14,
}
assert sum(SCORE.values()) == 96

CFPB_COMMITMENT = "https://www.consumerfinance.gov/rules-policy/regulations/1026/o/"
CFPB_LENDER = "https://www.consumerfinance.gov/ask-cfpb/what-is-lenders-title-insurance-en-163/"
CFPB_SHOP = "https://www.consumerfinance.gov/owning-a-home/close/shop-for-title-insurance-and-other-closing-services/"
ALTA_FORMS = "https://www.alta.org/policies-and-standards/policy-forms/"
ALTA_SURVEY = "https://www.alta.org/topics/topic-land-survey-standards"

POST = {
    "slug": "title-commitment-before-buying-str",
    "title": "Title commitment review before buying a short-term rental",
    "title_tag": "Title Commitment Review for an STR | Buyer Guide",
    "h1": "How should you review a title commitment before buying an STR?",
    "description": "Buying an Airbnb? Use this title-commitment framework to check ownership, legal description, requirements, exceptions, access, restrictions, and final coverage.",
    "date": DATE,
    "category": "Acquisition Diligence",
    "lead": "Review the title commitment as a decision document, not a closing formality. Confirm the proposed insured, estate, policy amount, and legal description; track every requirement to completion; read each exception with its underlying document; test access, parking, amenities, restrictions, and planned STR use; then compare the final issued owner’s policy with the negotiated commitment. A commitment is an offer to issue title insurance on stated terms—not a guarantee that every listed matter is harmless or that the property may operate as a short-term rental.",
    "sections": [
        ("The direct answer for an STR buyer", [
            f"The Consumer Financial Protection Bureau describes a <a href=\"{CFPB_COMMITMENT}\" rel=\"noopener\">title commitment report</a> as a title-company document describing the property interest and status of title, parties with interests and their claims, issues to resolve before closing, premiums, and policy endorsements. That makes it central to the purchase decision, but the buyer still needs the full documents and qualified legal and title review.",
            "Read the commitment during the contract's title-review window, not at the signing table. The operative deadline, objection method, seller cure rights, permitted exceptions, and termination remedies come from the purchase contract and local law. Calendar them separately from the inspection and financing dates.",
            ("callout", "Evaluating an STR with shared access, HOA restrictions, waterfront rights, multiple parcels, acreage, or a recent renovation? <a href=\"/apply/\">Apply for a BNB Accelerator strategy call</a> to pressure-test the acquisition, site dependencies, reserves, and opening plan. Local counsel, title professionals, surveyors, lenders, and authorities must determine the legal and insurance conclusions."),
        ]),
        ("A commitment is not the final title policy", [
            f"ALTA's <a href=\"{ALTA_FORMS}\" rel=\"noopener\">current policy-forms collection</a> lists separate commitment, owner's-policy, homeowner's-policy, loan-policy, short-form, and endorsement forms. Forms and state variations differ, so use the actual commitment and proposed policy for the transaction rather than a generic online summary.",
            ("table", ["Document", "What it does", "Buyer control"], [
                ["Title search or evidence", "Supports the title company's underwriting analysis.", "Ask what records and date the examination covers."],
                ["Title commitment or preliminary report", "States the terms on which a policy is proposed, subject to requirements, exceptions, exclusions, conditions, and changes.", "Object on time, request documents, negotiate treatment, and confirm updates."],
                ["Pro forma policy", "Shows how the requested policy may look if approved; it is not the issued policy.", "Use it to verify proposed insured, land, exceptions, endorsements, and coverage structure."],
                ["Closing documents and marked commitment", "Record how listed requirements and exceptions are expected to be handled at closing.", "Require evidence of payoff, release, corrective documents, recording instructions, and accepted changes."],
                ["Issued owner's policy", "Provides the buyer's actual title-insurance contract after closing, subject to its terms.", "Compare it promptly with the final agreed commitment and store it permanently."],
            ]),
            "A clean closing table does not prove that the policy later issued exactly as expected. Assign one person to obtain the recorded deed, final settlement documents, issued policy, endorsements, and referenced exceptions, then complete a post-closing comparison.",
        ]),
        ("Build the review package before reading exceptions", [
            "A commitment line that cites a book, page, instrument number, plat, declaration, or deed is only an index. Request a legible copy of the complete underlying document and every exhibit, amendment, assignment, release, and referenced map needed to understand it. A one-line title-company summary is not the governing text.",
            ("ol", [
                "Collect the executed purchase contract and all amendments, especially the legal description, title deadline, objection process, cure rights, and permitted exceptions.",
                "Collect the full commitment, jacket or conditions, schedules, proposed endorsements, tax and lien information, and any search notes the title professional will share.",
                "Request complete copies of every recorded document listed as an exception or requirement, plus relevant plats and prior policies.",
                "Add the current deed, survey, parcel records, HOA or association package, lease or management documents, and seller disclosures.",
                "Write a one-page STR use memo: access, parking, guest count, outdoor amenities, waterfront or common-area use, signs, events, pets, improvements, and manager operations.",
                "Give the complete package to the buyer's local counsel, title professional, lender, and surveyor as their roles require.",
            ]),
            "The use memo matters because an exception can be acceptable for one buyer and fatal for another. A utility easement may be routine until the proposed hot tub, pool, parking expansion, or addition occupies the same area. A private-road agreement may support residential access but allocate costs or control in ways the STR model did not price.",
        ]),
        ("Review Schedule A or its local equivalent", [
            "Start with identity and land before debating exceptions. Verify the proposed insured name and vesting match the buyer's approved ownership structure. Confirm the seller or current vested owner, estate or interest to be insured, policy type, amount, commitment date, property address, and complete legal description.",
            ("ul", [
                "Names: resolve spelling, entity, trust, marital, estate, authority, and signature-capacity questions before closing.",
                "Land: confirm every parcel, lot, tract, appurtenant easement, parking interest, storage area, dock right, or common interest that the deal depends on.",
                "Legal description: compare the commitment, deed, contract, survey, appraisal, lender documents, tax parcels, and listing package; street address is not a substitute.",
                "Policy amount: ask the title professional and counsel what amount and product are appropriate for the buyer; do not assume the lender's amount protects the buyer's equity.",
                "Effective date: identify the gap between the commitment date and recording, and ask how the title company will update the search and handle the gap.",
            ]),
            "A purchase can close on the correct street address while omitting a second parcel, parking tract, access strip, or amenity right that supported the price. Reconcile the land list before underwriting revenue or approving final loan documents.",
        ]),
        ("Treat requirements as a closing control list", [
            "Requirements are conditions the title insurer says must be satisfied before it will issue the proposed policy. Many are ordinary—executing the deed, paying the seller's loan, releasing liens, recording documents, paying taxes or charges—but ordinary does not mean self-proving.",
            ("table", ["Requirement type", "Evidence to request", "STR buyer concern"], [
                ["Seller authority and conveyance", "Entity documents, probate or trust authority, resolutions, deed and execution requirements.", "A rushed remote or estate sale needs identity and authority controls."],
                ["Mortgage or lien payoff", "Current payoff, authorized disbursement, release or satisfaction process, update after recording.", "Unreleased liens can impair the buyer's insured ownership and refinancing."],
                ["Taxes and assessments", "Current status, proration, delinquency payoff, special assessment details.", "Recurring or pending obligations change operating expense and cash at closing."],
                ["Corrective instruments", "Recordable deed, affidavit, release, easement, boundary agreement, or other counsel-approved document.", "A promise to correct after closing may leave access or the amenity plan unresolved."],
                ["Survey or inspection evidence", "Accepted survey, affidavits, title-company approval, revised exceptions or endorsements.", "Physical use and title coverage must align with the site plan."],
                ["Gap and recording controls", "Updated search, signed closing documents, funding conditions, recording confirmation.", "Last-minute instruments or failed recording can change the expected insured position."],
            ]),
            "Create a tracker with the exact requirement, responsible party, due date, evidence, title-company acceptance, lender acceptance, and final status. Do not mark an item complete because the seller says it is handled or funds appear on a settlement statement; confirm the insurer's required evidence and final treatment.",
        ]),
        ("Read each exception as a coverage and use question", [
            "An exception generally identifies a matter the proposed policy will not insure against, subject to the exact form and wording. It is not automatically a title defect, and deleting an exception is not always available. The buyer needs to understand what the matter does, whether it affects the land, how it intersects with the STR plan, and what the final policy will say.",
            ("ol", [
                "Copy the exception text and citation into a review table; attach the full underlying document.",
                "Determine which parcel, area, right, person, or obligation it affects and plot spatial matters on the survey when appropriate.",
                "Translate it into the buyer's planned use: access, parking, occupancy, leasing, signs, events, pets, amenities, utilities, construction, common areas, and management.",
                "Ask counsel and the title professional whether the matter should be satisfied, released, modified, subordinated, insured over, narrowed, endorsed, accepted, or treated another way.",
                "Record the title company's written response and any conditions; a broker's verbal reassurance does not amend policy language.",
                "Verify the final issued policy, endorsements, and exception wording after recording.",
            ]),
            "Some matters fall outside title insurance even if they never appear as a property-specific exception, because policies contain exclusions, conditions, definitions, and limits. Review the whole proposed product, not only Schedule B.",
        ]),
        ("Use an STR-specific exception matrix", [
            ("table", ["Recorded or observed matter", "Decision question", "Possible operational effect"], [
                ["Access or private-road easement", "Does the conveyed right cover the actual route, guests, vendors, gates, width, parking, maintenance, and all parcels used?", "Arrival failure, snow-service cost, gate disputes, or lender concern."],
                ["Declaration, covenant, or HOA regime", "What restrictions, amendment rights, enforcement powers, dues, approval rules, and rental provisions apply?", "STR prohibition or limits, amenity restrictions, fines, design delay, or cash obligations."],
                ["Utility, drainage, conservation, or slope easement", "Does the planned improvement conflict with the burdened area or access rights?", "Relocation or loss of a pool, hot tub, parking pad, deck, or addition."],
                ["Survey or possession exception", "What boundary, encroachment, occupation, or unrecorded-use risk remains outside proposed coverage?", "Uncertain acreage, parking, amenity ownership, or neighbor conflict."],
                ["Mineral, timber, water, shoreline, or development reservation", "What rights were severed or reserved, who may exercise them, and what coverage or consent exists?", "Site disturbance, limits on marketed rights, financing or resale complexity."],
                ["Lease, option, right of first refusal, or occupancy claim", "Who may possess or acquire the property, and what must terminate or remain?", "Delayed launch, conflicting possession, transfer restriction, or future sale issue."],
                ["Tax, assessment, lien, or improvement district", "Which amount is due, recurring, pending, or superior, and who pays?", "Higher closing cash, recurring expense, or priority risk."],
                ["Plat note, setback, or development restriction", "Does it affect existing improvements or the planned guest-capacity and amenity plan?", "Redesign, permit problem, reduced usable site, or exit risk."],
            ]),
            "This matrix is a question generator, not a legal interpretation. A recorded document may have definitions, exhibits, amendment history, enforcement limits, or jurisdiction-specific effects that change the initial reading.",
        ]),
        ("Owner's coverage and lender's coverage are not interchangeable", [
            f"The CFPB explains that <a href=\"{CFPB_LENDER}\" rel=\"noopener\">lender's title insurance protects the lender</a> against covered title problems affecting its loan and does not protect the buyer's equity. The CFPB's <a href=\"{CFPB_SHOP}\" rel=\"noopener\">closing-services guidance</a> likewise distinguishes the lender's policy from an owner's policy that protects the buyer's financial investment.",
            "Do not assume that paying a title charge means the buyer receives the desired owner's product. Ask what owner's policy form is proposed, who is insured, the amount, covered risks, exclusions, conditions, exceptions, endorsements, continuation or transfer rules, and premium. State regulation, filed forms, property type, and underwriter approval affect what is available.",
            "Entity vesting matters. If the buyer changes from an individual to an LLC, trust, partnership, or another owner before or after closing, have counsel and the insurer confirm the effect on vesting, loan approval, policy insured, and coverage. Do not rely on an informal plan to deed the property later.",
        ]),
        ("Worked example: lake access that is not one simple line", [
            "Assume an illustrative buyer is evaluating a cabin marketed with lake access, a shared private road, and parking for six vehicles. The title commitment covers the house parcel but the listing also references a separate access parcel. Schedule B cites a road agreement, subdivision declaration, utility easement, and plat. The buyer initially sees common documents and no obvious lien problem.",
            "The document package changes the decision. The legal description does not include the separate parcel; the road easement follows a route narrower than the area guests currently drive; the agreement allocates maintenance by a formula the underwriting omitted; and the utility easement crosses the only proposed overflow-parking area. None of those facts alone tells the buyer to proceed or walk.",
            "The buyer's counsel, title professional, surveyor, lender, and designer coordinate the response. The seller documents the actual lake-access interest, the survey plots the recorded access and utility areas, the title insurer states what land and rights it will insure, and the operating plan reduces parking until a compliant design is confirmed. The buyer re-underwrites maintenance cost and guest capacity before the objection deadline.",
            "The property, rights, parking count, and findings are illustrative—not a BNB Accelerator client result or a legal opinion. Actual commitments, exceptions, documents, remedies, and policy coverage are property- and jurisdiction-specific.",
        ]),
        ("Build objections around evidence and remedies", [
            "A useful title objection identifies the commitment item, governing document, contract right, buyer concern, requested cure or treatment, deadline, and required proof. Counsel should draft or approve it. Vague requests such as 'provide clear title' may not preserve a specific objection or require the remedy the buyer needs.",
            ("table", ["Issue", "Remedy to investigate", "Completion evidence"], [
                ["Missing release or payoff", "Satisfaction, release, payoff and recording process acceptable to insurer.", "Updated commitment or written insurer acceptance plus recorded release when required."],
                ["Missing parcel or appurtenant right", "Correct contract and conveyance documents; add land or insured right if available.", "Revised legal description, survey, commitment, lender approval, deed and policy."],
                ["Problematic covenant or easement", "Amendment, release, consent, subordination, endorsement, redesign, price change, or termination.", "Executed recordable document or written coverage/treatment accepted by buyer and lender."],
                ["Survey discrepancy", "Correction, boundary or access document, removal, relocation, or specific policy treatment.", "Revised survey, recorded instruments, permits where needed, updated exceptions."],
                ["Unclear STR restriction", "Local legal interpretation, association confirmation where appropriate, contract remedy, or withdrawal.", "Written legal and operational conclusion; never title insurance as a substitute for STR permission."],
            ]),
            "A credit does not cure an access right or erase a restrictive covenant. It only reallocates money. Use a credit when the buyer knowingly accepts the legal and execution risk and the unresolved issue is compatible with the lender, insurer, contract, and operating plan.",
        ]),
        ("Perform a pre-close and post-close reconciliation", [
            "Before authorizing funding, compare the final commitment or marked version with the contract, deed, survey, settlement statement, loan documents, entity documents, and negotiated cure evidence. Confirm no new exception or unresolved requirement has appeared and that requested endorsements are approved—not merely discussed.",
            ("ul", [
                "Correct insured and vesting name, estate, policy amount, land, legal description, and parcel list.",
                "Every requirement has named evidence and title-company acceptance; pending recordings have an accountable follow-up.",
                "Every exception has been read with its document and final disposition is recorded in the decision file.",
                "The lender's conditions and the buyer's owner's-coverage requirements are tracked separately.",
                "The deed, corrective instruments, releases, easements, and other closing documents are recordable and match the approved structure.",
                "After closing, retrieve recording confirmations, the issued owner's policy and endorsements, then compare them with the negotiated commitment.",
            ]),
            "Title work also needs an operating handoff. Give the manager the road, parking, common-area, association, amenity, and access rules needed for daily operations while keeping sensitive ownership and policy records secure.",
        ]),
        ("Failure modes that turn title review into a launch problem", [
            ("ul", [
                "Opening the commitment after the objection deadline or only at the closing table.",
                "Reading exception summaries without obtaining the complete recorded documents and exhibits.",
                "Checking the street address but not reconciling the full legal description and every parcel or appurtenant right.",
                "Assuming a requirement will disappear automatically because payoff funds are shown on the settlement statement.",
                "Treating every exception as a defect—or treating a routine-looking exception as harmless without testing the STR plan.",
                "Assuming lender's title insurance protects the buyer's equity or that title insurance proves STR legality.",
                "Accepting verbal promises that an easement, release, amendment, or endorsement will be handled after closing.",
                "Failing to compare the issued policy, endorsements, and final exceptions with the negotiated commitment.",
            ]),
            ("warn", "Legal and insurance boundary: this guide summarizes CFPB and ALTA materials reviewed September 24, 2026. It is educational, not legal, title, insurance, lending, survey, tax, zoning, or investment advice. Commitments, contracts, policy forms, regulation, and remedies vary by state and transaction. Use local counsel and qualified title, survey, lending, and closing professionals."),
        ]),
        ("Turn the commitment into a go, renegotiate, or walk decision", [
            "Proceed when the insured land and ownership structure are correct, requirements have executable closing controls, material exceptions are understood, legal access and planned use are supportable, the owner's coverage is acceptable, and the deal still works after recurring obligations and site constraints. Renegotiate when a defined issue has a reliable cure, coverage path, redesign, or price adjustment. Walk away when a core right or operating assumption cannot be established on acceptable terms before the contractual deadline.",
            "Pair this review with the <a href=\"/blog/boundary-survey-before-buying-str/\">boundary-survey guide</a>, the <a href=\"/blog/inspection-contingency-length-str/\">diligence-timeline guide</a>, the <a href=\"/blog/reading-an-hoa-declaration/\">HOA declaration review</a>, and the <a href=\"/underwriting/\">acquisition model</a>. Title insurance does not replace any of them.",
            "The practical next step is to calendar the objection deadline, obtain the full commitment and every cited document, write the STR use memo, and schedule a coordinated review with local counsel and the title professional while there is still time to cure, redesign, reprice, or terminate.",
            ("callout", "Need title findings translated into an acquisition price, site plan, reserve, and launch decision? <a href=\"/apply/\">Apply for a BNB Accelerator strategy call</a>. We can coordinate the investment workflow while local legal, title, survey, lending, insurance, and regulatory professionals handle their conclusions."),
        ]),
    ],
    "faqs": [
        ("What is a title commitment in an STR purchase?", "It is the title insurer's commitment to issue a policy on stated terms if its requirements are satisfied, subject to exceptions, exclusions, conditions, and later changes. It is not the final policy or proof of STR legality."),
        ("What should a buyer check in Schedule A?", "Verify the proposed insured and vesting, current owner, estate or interest, policy type and amount, effective date, and complete legal description including every parcel and appurtenant right."),
        ("What is the difference between title requirements and exceptions?", "Requirements are conditions the insurer says must be satisfied before issuing the proposed policy. Exceptions identify matters the proposed policy will not cover, subject to the exact form and wording."),
        ("Does lender's title insurance protect the STR buyer?", "The CFPB says lender's title insurance protects the lender and does not protect the buyer's equity. Ask about the appropriate owner's policy and read its actual terms."),
        ("Does title insurance confirm that short-term renting is allowed?", "No. STR permission requires separate review of zoning, permits, licensing, HOA documents, covenants, building and fire rules, and other applicable requirements."),
        ("What happens after closing?", "Obtain the recorded deed and corrective documents, recording confirmations, issued owner's policy and endorsements, then compare the insured, land, amount, exceptions, and coverage with the negotiated commitment."),
    ],
    "related": [
        '<a href="/blog/boundary-survey-before-buying-str/">Coordinate the boundary survey</a>',
        '<a href="/blog/reading-an-hoa-declaration/">Review HOA rental restrictions</a>',
        '<a href="/blog/inspection-contingency-length-str/">Protect the review deadline</a>',
        '<a href="/underwriting/">Re-underwrite title obligations</a>',
        '<a href="/apply/">Discuss the acquisition strategy</a>',
    ],
    "cta_h": "Buying an STR with complicated access, rights, or restrictions?",
    "cta_p": "BNB Accelerator can help source and underwrite the property, coordinate the acquisition file, and translate title findings into a purchase decision while qualified local professionals handle title, legal, survey, lending, and regulatory work.",
}


if __name__ == "__main__":
    blog.build([POST])
    print(f"candidate score: {sum(SCORE.values())}/100 — {SCORE}")
