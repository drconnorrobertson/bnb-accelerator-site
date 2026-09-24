#!/usr/bin/env python3
"""Generate the ADA coverage decision guide for short-term-rental buyers."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import blog

DATE = "2026-09-24"
SCORE = {
    "distinct_search_intent": 30,
    "buyer_relevance": 22,
    "real_question": 14,
    "service_fit": 13,
    "original_decision_support": 15,
}
assert sum(SCORE.values()) == 94

TITLE_III = "https://www.ada.gov/law-and-regs/regulations/title-iii-regulations/"
LODGING_GUIDE = "https://www.ada.gov/resources/lodging-guide/"
STANDARDS = "https://www.ada.gov/law-and-regs/design-standards/2010-stds/"
SERVICE_FAQ = "https://www.ada.gov/resources/service-animals-faqs/"

POST = {
    "slug": "does-ada-apply-short-term-rental",
    "title": "Does the ADA apply to a short-term rental?",
    "title_tag": "Does the ADA Apply to a Short-Term Rental? | BNB",
    "h1": "Does the ADA apply to a short-term rental?",
    "description": "Does the ADA apply to an Airbnb or vacation rental? Use this fact-specific checklist for lodging status, design, reservations, and service animals.",
    "date": DATE,
    "category": "Acquisition Diligence",
    "lead": "Sometimes. A short-term rental is not automatically covered by—or exempt from—Title III of the Americans with Disabilities Act just because it is a house, an Airbnb listing, or residentially zoned. The federal analysis turns on how the property and lodging business actually operate. A single private home may present a different case from a cabin resort, condo-hotel, rental pool, or centrally managed portfolio. Before buying or renovating, separate three questions: whether the operation is a covered place of lodging, which duties follow if it is, and what other state, local, building-code, fair-housing, or platform requirements apply independently.",
    "sections": [
        ("The short answer for a buyer", [
            f"Title III covers specified places of public accommodation, including many places of lodging. The Department of Justice's <a href=\"{TITLE_III}\" rel=\"noopener\">Title III regulations</a> define a place of lodging through operating facts, not the label on the listing. The definition includes an inn, hotel, motel, or another facility that offers short stays and operates with hotel-like conditions and amenities. It also contains a narrow exception for certain small, owner-occupied establishments.",
            "That means an investor should not use a one-line rule such as 'houses are exempt' or 'every vacation rental is a hotel.' Establish the facts first. The property type, number of rentable rooms, owner's residence, guest's right to a particular unit, reservations process, management structure, and services can all matter. Coverage is a legal conclusion for qualified counsel, but these facts belong in acquisition diligence.",
            ("callout", "Evaluating a property with an unusual operating model or renovation plan? <a href=\"/apply/\">Apply for a BNB Accelerator strategy call</a> to pressure-test the acquisition, operating plan, and improvement budget. Accessibility counsel and design professionals should make the legal and technical determinations."),
        ]),
        ("Start with four gates, in order", [
            ("table", ["Gate", "Question", "What to document"], [
                ["1. Operation", "How will guests actually book and use the property?", "Stay length, unit selection, return rights, services, and who manages reservations."],
                ["2. Lodging status", "Do the facts resemble a regulated place of lodging?", "Short stays plus the hotel-like conditions described in the federal definition."],
                ["3. Small-property exception", "Is the facility both small enough and actually owner-occupied?", "Rentable-room count and evidence that the proprietor uses the facility as a residence."],
                ["4. Duties", "If covered, which operational and physical-access obligations apply?", "Existing conditions, planned construction or alterations, reservation flow, policies, and communications."],
            ]),
            "Do not collapse these gates. A property can be a covered lodging operation without every guest room needing the same physical features. Conversely, a buyer should not conclude that no accessibility work is relevant merely because a particular construction standard does not apply to one planned repair. Coverage, policy modifications, communication, reservations, new construction, alterations, and existing-barrier removal are related but distinct analyses.",
            "Also keep federal Title III separate from other requirements. State civil-rights laws, local building codes, fair-housing rules, licensing conditions, contracts, and booking-platform policies may define different scopes and duties. A federal conclusion does not erase those layers. Put each authority in its own diligence row, with an owner and a source, instead of treating 'ADA review' as a universal yes-or-no checkbox.",
        ]),
        ("What makes an STR look like a place of lodging", [
            "Under the federal definition, a covered place of lodging includes an inn, hotel, or motel, as well as another facility that provides guest rooms for short-term stays—generally 30 days or less—when guests do not have a right to return to a specific room or unit and the operation supplies hotel-like conditions or amenities. The regulation gives examples of those conditions: on- or off-site management and reservations, walk-up or call-in availability, housekeeping or linen services, and reservations for a room type without guaranteeing a specific unit.",
            "Those are legal facts, not a mechanical point score. Centralized reservations plus linen service does not, by itself, produce a definitive answer. But a common-site eight-cabin operation with one brand, one manager, shared guest services, and interchangeable unit assignments presents a materially different fact pattern from an owner renting one identified detached house under one contract.",
            ("ul", [
                "Save the guest-facing booking path, terms, confirmation email, unit-assignment language, cancellation policy, and any security-deposit terms.",
                "Identify whether the guest books a specific legal unit or merely a unit type that the operator can change.",
                "List management, front-desk, housekeeping, linen, food, transport, and shared-amenity services, including services performed by contractors.",
                "Map ownership and control when units are individually owned but reservations, marketing, or operations are pooled.",
                "Compare the written model with actual practice. A contract label does not cure a contradictory guest experience.",
            ]),
        ]),
        ("The five-room exception is narrower than it sounds", [
            f"The regulation excludes an establishment located within a facility containing no more than five rooms for rent or hire only when the proprietor actually occupies that facility as the proprietor's residence. The DOJ's <a href=\"{LODGING_GUIDE}\" rel=\"noopener\">guide for places of lodging</a> describes the same owner-occupied, five-or-fewer-room boundary. Both conditions matter.",
            "A buyer should therefore avoid three common shortcuts. First, count rooms offered for rent under the relevant facts rather than assuming that one listing equals one room. Second, verify actual proprietor occupancy; a mailing address, occasional stay, or local manager is not necessarily residence. Third, do not extend a potential exception for one facility to an entire multi-building or pooled operation without advice on how the facilities are treated.",
            "For a house-hack or bed-and-breakfast acquisition, collect floor plans, the proposed rentable-room plan, the owner's intended living space, licensing documents, and the actual operating calendar. If the model depends on the exception, have counsel test it before the purchase contract, renovation scope, and revenue case become hard to change.",
        ]),
        ("If Title III applies, separate the duty buckets", [
            f"The DOJ lodging guide explains that covered lodging businesses may have duties involving reasonable policy modifications, effective communication, service animals, existing barriers, and accessible design for new construction and alterations. The <a href=\"{STANDARDS}\" rel=\"noopener\">2010 ADA Standards</a> include transient-lodging requirements, including Sections 224 and 806. Do not take a guest-room table out of context and apply it before establishing the facility, construction history, scope of work, and applicable standard.",
            ("ol", [
                "Operating policies: review check-in, deposits, occupancy, companion assistance, mobility devices, and emergency procedures for unnecessary access barriers.",
                "Reservations: determine whether the booking process describes accessible features with enough detail for a guest to assess suitability and whether applicable hold, block, and guarantee rules are met.",
                "Communication: identify how guests with hearing, vision, speech, or other disabilities can obtain information and communicate during booking and a stay.",
                "Service animals: train the person answering inquiries on the limited questions and fee rules that apply to covered entities; do not simply relabel a pet policy.",
                "Physical access: distinguish new construction, alterations, and existing-facility barrier removal. Commission a qualified survey instead of relying on listing photographs or an owner's estimate.",
            ]),
            f"For covered businesses, the DOJ's <a href=\"{SERVICE_FAQ}\" rel=\"noopener\">service-animal FAQ</a> says staff may ask only two questions when the need is not obvious: whether the dog is required because of a disability and what work or task it has been trained to perform. A hotel may not confine a service-animal user to a pet-friendly room or impose a cleaning charge merely for hair or dander, though the same damage charge imposed on other guests may apply when actual damage occurs.",
        ]),
        ("Worked example: an eight-cabin acquisition", [
            "Assume a buyer is considering an illustrative eight-cabin property on one parcel. Guests generally stay three nights, reserve one of three cabin types, and may be reassigned among cabins in that type. One off-site team controls the website, phone reservations, check-in messages, housekeeping, and linens. The seller calls each cabin a private vacation home.",
            "The label does not end the inquiry. Short stays, non-guaranteed unit assignment, centralized management and reservations, and housekeeping or linen service are meaningful place-of-lodging signals. The small owner-occupied exception appears unlikely on these facts because there are more than five rentable rooms and the proprietor does not live at the facility. Before pricing improvements, the buyer should obtain the plans and permit history, document the reservation system, commission an accessibility assessment, and ask counsel which Title III duties and design provisions apply.",
            "Now contrast an illustrative owner renting one specifically identified detached house. The guest signs for that house, has no chance of reassignment, and receives no hotel-like services. That is a different federal fact pattern, not an automatic exemption. The buyer still checks state and local accessibility law, building code, fair-housing issues, and platform terms. Neither example predicts a legal outcome or a project cost; both show why operating facts belong beside the <a href=\"/underwriting/\">financial underwriting</a>.",
        ]),
        ("Acquisition and renovation diligence checklist", [
            ("ol", [
                "Write a one-page operating model: property and room count, average and maximum stay, named unit versus unit type, management, reservations, housekeeping, linens, and shared amenities.",
                "Diagram the ownership and control chain, including any rental pool, condo-hotel agreement, association, master operator, or third-party manager.",
                "Collect certificates of occupancy, permits, plans, prior accessibility reviews, violation notices, guest complaints, and written accommodation procedures.",
                "Walk the full guest journey: discovery, booking, feature disclosure, arrival, parking, entrance, route, sleeping area, bathroom, amenities, emergency communication, and checkout.",
                "Define the renovation scope before closing and have an accessibility professional flag work that could be an alteration or affect an accessible route.",
                "Price only evidence-backed corrections. Keep a separate contingency for unresolved design, permit, and policy work; do not bury it in furniture or cosmetic budgets.",
                "Have qualified counsel analyze Title III and other applicable law, then assign implementation to the designer, contractor, manager, and reservations owner with written acceptance criteria.",
            ]),
            "Accessibility diligence can change the acquisition decision in several legitimate ways: a manageable policy and booking update, a redesign before construction, a larger improvement reserve, a different management workflow, or a decision not to pursue a property whose physical or operating constraints cannot support the intended model. The goal is not to declare a property 'ADA certified.' It is to expose obligations, decisions, and costs before they become guest problems or closing surprises.",
        ]),
        ("Failure modes that create avoidable risk", [
            ("ul", [
                "Assuming residential zoning or a residential mortgage decides whether the lodging operation is a public accommodation.",
                "Treating five bedrooms as an automatic exemption without verifying the number of rooms for rent and the proprietor's actual residence.",
                "Advertising a unit as accessible without measurements, route details, photographs, or a feature inventory that supports the claim.",
                "Copying a no-pets rule into service-animal responses or charging an automatic pet or cleaning fee where Title III rules apply.",
                "Relying on the booking platform to satisfy the operator's legal duties or to describe property-specific features accurately.",
                "Beginning a bathroom, entrance, parking, or common-area renovation before a qualified accessibility review establishes the relevant scope.",
            ]),
            ("warn", "Legal boundary: this guide summarizes federal DOJ materials reviewed September 24, 2026. It is educational, not legal, architectural, engineering, fair-housing, building-code, investment, or accessibility advice. Application is fact-specific, other laws may be broader, and requirements can change. Use qualified counsel and accessibility professionals for the property and work scope."),
        ]),
        ("Turn the answer into a closing decision", [
            "Before the inspection period ends, require three outputs: counsel's scoped coverage analysis, an accessibility professional's prioritized property findings, and an operator's written plan for reservations, communications, service-animal handling, and feature descriptions. Translate each open item into a responsible party, due date, cost range, and closing condition. That creates a decision record instead of a vague compliance promise.",
            "Then test those costs and constraints with the rest of the deal: address-level STR legality, insurance, financing, demand, revenue evidence, reserves, management, and the <a href=\"/design/\">design scope</a>. Review the <a href=\"/blog/security-camera-privacy-str/\">guest privacy diligence guide</a> for another policy-to-property handoff and the <a href=\"/property-types/\">property-type library</a> when comparing operating formats.",
            "If the opportunity still fits, preserve the evidence and decisions in the acquisition file and train the operating team before the first listing goes live. If it does not fit, walk away because of a documented constraint—not because someone relied on a slogan about houses, bedrooms, or Airbnb.",
        ]),
    ],
    "faqs": [
        ("Does the ADA apply to every Airbnb or vacation rental?", "No blanket rule makes every listing covered or exempt. Federal Title III analysis depends on the facility and how the lodging operation works. State, local, building-code, fair-housing, and platform requirements may apply separately."),
        ("Is a property with five or fewer rentable rooms automatically exempt?", "No. The federal exception also requires the proprietor to actually occupy the facility as a residence. Both the room limit and owner-occupancy condition matter."),
        ("Must an existing covered STR be completely rebuilt?", "Not necessarily. Existing-facility barrier removal, new construction, and alterations are different duty categories. A qualified professional should identify the applicable standard and scope rather than assuming full reconstruction or no work."),
        ("Can a covered lodging business charge a pet fee for a service animal?", "The DOJ says hotels may not charge a cleaning fee merely because a service animal stayed, though they may charge for actual damage on the same basis as other guests. Apply current law to the specific operation with counsel."),
        ("Do Airbnb or Vrbo policies replace the ADA analysis?", "No. Platform rules are a separate layer. The owner and operator still need to determine which federal, state, local, code, licensing, and contractual requirements apply."),
    ],
    "related": [
        '<a href="/underwriting/">Build the acquisition underwriting case</a>',
        '<a href="/design/">Plan the STR design and improvement scope</a>',
        '<a href="/management/">Define the operating model</a>',
        '<a href="/blog/security-camera-privacy-str/">Audit security-camera privacy before closing</a>',
        '<a href="/partners/">Coordinate with qualified specialists</a>',
    ],
    "cta_h": "Buying an STR with a complex operating or renovation plan?",
    "cta_p": "BNB Accelerator can help source and underwrite the property, pressure-test the operating model, and coordinate acquisition diligence while qualified legal and accessibility professionals make the compliance determinations.",
}


if __name__ == "__main__":
    blog.build([POST])
    print(f"candidate score: {sum(SCORE.values())}/100 — {SCORE}")
