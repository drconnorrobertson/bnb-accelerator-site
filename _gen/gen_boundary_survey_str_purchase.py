#!/usr/bin/env python3
"""Generate the boundary-survey acquisition guide for STR buyers."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import blog

DATE = "2026-09-24"
SCORE = {
    "distinct_search_intent": 30,
    "buyer_relevance": 24,
    "real_question": 15,
    "service_fit": 13,
    "original_decision_support": 14,
}
assert sum(SCORE.values()) == 96

ALTA_STANDARDS = "https://www.alta.org/policies-and-standards/policy-forms/download?formID=721&type=pdf"
ALTA_TOPIC = "https://www.alta.org/topics/topic-land-survey-standards"
NSPS_2026 = "https://nsps.us.com/page/2026ALTA"
NJ_PARCELS = "https://nj.gov/njgin/edata/parcels/"

POST = {
    "slug": "boundary-survey-before-buying-str",
    "title": "Boundary surveys before buying a short-term rental",
    "title_tag": "Boundary Survey Before Buying an STR | Buyer Guide",
    "h1": "Should you get a boundary survey before buying an STR?",
    "description": "Buying an Airbnb with acreage or outdoor amenities? Use this boundary-survey framework for access, easements, encroachments, setbacks, and closing remedies.",
    "date": DATE,
    "category": "Acquisition Diligence",
    "lead": "Order an appropriate land survey before closing when the deal depends on boundaries, legal access, parking, outdoor amenities, an off-parcel utility, acreage, expansion, or removal of a title-policy survey exception. A tax parcel map, listing outline, fence, seller sketch, old plat, appraisal, and phone GPS do not establish today’s boundary. The buyer needs a licensed surveyor’s scope coordinated with the title commitment, lender, planned STR use, and local requirements early enough to resolve discrepancies before the contingency expires.",
    "sections": [
        ("The direct answer for an STR buyer", [
            "A new boundary survey is not automatically required in every U.S. home purchase. Requirements and customary products vary by state, lender, title insurer, property, and transaction. But the survey becomes high-value diligence when a revenue assumption depends on land the buyer may not own, a right the buyer may not have, or an improvement the buyer may not legally keep or build.",
            f"The current <a href=\"{ALTA_STANDARDS}\" rel=\"noopener\">2026 ALTA/NSPS Land Title Survey standards</a> explain the title problem clearly: some matters discoverable through survey and inspection are not shown in public records. The standards coordinate fieldwork, the survey plat, title evidence, optional Table A items, and certification for transactions that require that product. A typical residential buyer may need a different state-specific boundary or location survey, so the buyer should not order an ALTA/NSPS survey by name without confirming the required deliverable.",
            ("callout", "Evaluating a cabin, waterfront home, acreage parcel, shared drive, steep site, or property with outdoor amenities? <a href=\"/apply/\">Apply for a BNB Accelerator strategy call</a> to pressure-test the acquisition, site plan, improvement budget, and closing timeline. Licensed surveyors, title professionals, lenders, local authorities, and counsel must make their respective technical and legal determinations."),
        ]),
        ("Start with the buyer decision, not a survey label", [
            "Ask what the transaction must prove. A boundary survey establishes or retraces property boundaries under applicable law and professional standards. A location or mortgage product may have a narrower purpose. A topographic survey addresses terrain and elevations. An improvement or as-built survey documents specified constructed features. An ALTA/NSPS Land Title Survey aligns a defined land-title scope among the client, title insurer, lender, and surveyor.",
            ("table", ["Buyer question", "Why it matters to an STR", "Scope discussion"], [
                ["What land is being conveyed?", "Lot size, waterfront, views, privacy, and expansion can drive the purchase thesis.", "Boundary retracement, monuments, record description, adjoining evidence."],
                ["How do guests and vendors reach it?", "A driveway or path may cross another parcel or private road.", "Rights of way, observed access, recorded and offsite easements."],
                ["Where are the amenities?", "Parking, decks, docks, fire pits, hot tubs, wells, septic components, and trails may sit near or over a line.", "Improvements and their relationship to boundaries, easements, and setback information."],
                ["Can the buyer execute the design?", "A proposed pool, bedroom addition, parking pad, ADU, or event area may need usable site area.", "Planned use communicated in writing; zoning and design information coordinated separately."],
                ["What will title insure?", "A broad survey exception can leave physical matters outside coverage.", "Title commitment review, insurer requirements, survey certification, requested endorsement or exception treatment."],
            ]),
            "Tell the surveyor the planned STR use in writing. The 2026 ALTA/NSPS standards direct field features to be located to an appropriate degree of precision based on the planned use when that use is reported by the client, lender, or insurer. A silent buyer can receive a technically correct product that does not answer the investment decision.",
        ]),
        ("Do not use an online parcel line as the boundary", [
            f"Online GIS is useful for early research, not for staking a fence or proving ownership. New Jersey's official <a href=\"{NJ_PARCELS}\" rel=\"noopener\">state parcel-data page</a>, for example, says its parcel polygons do not represent legal boundaries, are not survey data, and should not be used for land-ownership determinations. County viewers around the country publish similar limitations.",
            ("ul", [
                "Aerial imagery can be offset from the parcel layer, and both can differ from the legally retraced boundary.",
                "A fence, hedge, driveway, utility line, or mowing pattern is evidence of occupation or use—not automatic proof of title.",
                "An assessor map is built for assessment and reference; it does not replace the surveyor's records research, field evidence, and boundary analysis.",
                "A listing's acreage or waterfront outline may be a marketing representation rather than a surveyed quantity or legal conclusion.",
                "Consumer GPS and phone pins do not establish legal corners or a buildable area.",
            ]),
            "Use GIS to form questions: Does the driveway appear to leave the parcel? Is the hot tub near a line? Does the dock connect to the conveyed tract? Then ask the licensed surveyor and title team to resolve those questions with the governing evidence.",
        ]),
        ("Coordinate the survey with the title commitment", [
            f"The <a href=\"{ALTA_TOPIC}\" rel=\"noopener\">American Land Title Association's survey standards page</a> describes the 2026 standards as a framework for survey-related title matters including boundary lines, easements, encroachments, access, and legal descriptions. The survey and title commitment are complementary: the commitment supplies recorded documents and proposed exceptions; the survey relates relevant documents and observed conditions to the land.",
            ("ol", [
                "Obtain the current title commitment and complete copies of every plotted easement, covenant, right of way, and other relevant exception—not only Schedule B labels.",
                "Give the surveyor the current record description, recorded plats, prior surveys, unrecorded agreements the buyer wants considered, and the complete planned-use memo.",
                "Ask the title insurer and lender, in writing, which survey product, certification parties, timing, and optional items they require.",
                "Have the surveyor identify conflicts, gaps, overlaps, access evidence, occupation lines, encroachments, and documents that cannot be plotted or do not affect the property as expected.",
                "Send the completed survey back to the title insurer, lender, and counsel for written treatment of exceptions, endorsements, requirements, and objections.",
                "Do not assume a clean drawing automatically changes the policy; confirm the issued policy and final exceptions after closing.",
            ]),
            "Surveyors locate and report under their professional scope. They do not decide every legal consequence of an encroachment, create an easement by drawing it, guarantee zoning approval, or rewrite title coverage. Keep the professionals in one evidence loop instead of asking any one of them to answer outside their role.",
        ]),
        ("Choose the right product and optional detail", [
            f"The 2026 ALTA/NSPS standards took effect February 23, 2026 and superseded earlier versions for new work under that standard. NSPS's <a href=\"{NSPS_2026}\" rel=\"noopener\">current standards resource</a> emphasizes that a request must specify the 2026 ALTA/NSPS Land Title Survey and identify selected Table A items. It also warns that unusual interests such as marinas, campgrounds, easements, leases, and mineral interests need a written scope discussion.",
            "Do not check every optional item reflexively, and do not assume the base scope includes every design datum. The buyer, surveyor, lender, and title insurer should choose information that answers the actual transaction. State and local rules may also add or override requirements.",
            ("ul", [
                "Boundary monuments may need to be set or restored if the buyer needs corners marked and the applicable scope allows it.",
                "Zoning classification and setback data require a reliable zoning report or letter and do not turn the surveyor into the zoning authority.",
                "Parking counts and types may matter when the operating plan assumes a specific guest capacity.",
                "Utility information can require owner records, observed evidence, markings, private locating, and sometimes excavation; a survey is not a guarantee of every underground line.",
                "Plottable offsite easements can matter when the property depends on access, utilities, waterfront, parking, or amenities beyond its fee boundary.",
                "A design-grade topographic or engineering survey should be scoped as design work, not presumed from a land-title survey.",
            ]),
        ]),
        ("Apply an STR-specific site dependency map", [
            "Walk every revenue-driving or safety-critical feature through four questions: Is it on the conveyed land? If not, what recorded right permits use? Does an easement, setback, covenant, or boundary constrain it? Can guests, cleaners, emergency services, and repair vendors reach it as planned?",
            ("table", ["Feature", "Survey or title risk", "Operating consequence"], [
                ["Guest parking and turnaround", "Spaces or maneuvering area cross a line, right of way, or setback.", "Lower legal capacity, neighbor conflict, towing, or redesign."],
                ["Shared or private drive", "No plotted access right, unclear width, gate issue, or maintenance allocation.", "Unreliable arrival, winter service disputes, or lender/title objection."],
                ["Deck, hot tub, pool, fire pit", "Improvement sits near a boundary, easement, waterfront line, or setback.", "Removal, relocation, permit problem, or lost listing feature."],
                ["Well, septic, sewer, propane, utilities", "Component or service route is off-parcel or conflicts with an easement.", "Access and repair uncertainty, health or service interruption."],
                ["Dock, trail, beach, view corridor", "Marketing suggests ownership or access that the deed and survey do not support.", "Material loss of guest promise and pricing thesis."],
                ["Future addition or ADU", "Buildable envelope is smaller after setbacks, easements, terrain, or encroachments.", "Projected bedroom count or amenity plan becomes infeasible."],
            ]),
            "The survey does not approve STR use or an improvement. It gives the team a reliable spatial foundation for the separate zoning, building, fire, environmental, utility, HOA, and title decisions.",
        ]),
        ("Worked example: the cabin whose driveway is not the deal", [
            "Assume an illustrative buyer is evaluating a mountain cabin marketed with three acres, a circular guest driveway, a fire-pit terrace, and room for a future two-car parking pad. The county GIS appears to place the driveway inside the parcel. The seller provides a 17-year-old survey, but the terrace and part of the current drive were built later.",
            "The buyer gives a licensed surveyor the current title commitment, recorded road easement, old survey, site plan, and planned parking expansion. Fieldwork shows the traveled driveway leaves the parcel and uses the neighbor's land outside the plotted access easement. The fire-pit terrace is inside the boundary but partly within a utility easement. The proposed parking pad would conflict with the setback information supplied in a current zoning letter.",
            "Those are three different decisions. Counsel and the title team evaluate whether access can be documented, expanded, insured, or rerouted. The utility holder and local professionals determine whether the terrace may remain and what work is allowed. The designer moves the parking plan and rechecks guest capacity. The buyer does not call the survey a failed inspection; the buyer uses it to replace unsupported assumptions with executable rights and plans.",
            "The property, dates, acreage, and findings are illustrative—not a BNB Accelerator client result, boundary opinion, or prediction. Actual conclusions require the property records, field evidence, jurisdictional standards, and qualified professionals.",
        ]),
        ("Treat an old survey as evidence, not automatic clearance", [
            "A prior survey may reduce research or fieldwork, but its usefulness depends on the product, date, certification, parties entitled to rely, standards, title evidence, field changes, and current transaction requirements. New fences, additions, decks, driveways, utilities, subdivisions, easements, occupation, and neighboring work can make an old drawing incomplete for today's decision.",
            ("ul", [
                "Ask the original surveyor whether an update is possible and what current work is required; do not alter or recertify the drawing yourself.",
                "Compare the old survey with the current deed, legal description, title commitment, recorded documents, visible occupation, and proposed improvements.",
                "Confirm that the survey covers every parcel and appurtenant right in the purchase, not only the house lot.",
                "Ask the title insurer and lender whether they will accept an update and whom the new certification must name.",
                "Do not rely on a seller affidavit as a technical substitute unless the professionals responsible for the transaction expressly accept the resulting scope and risk.",
            ]),
        ]),
        ("Convert findings into matched closing remedies", [
            "A boundary or access issue is not solved by a generic credit. First define the condition, the legal and physical remedy, the responsible parties, the documents, approvals, construction, title treatment, and timing. Some solutions require a boundary-line agreement, easement, release, corrective deed, permit, relocation, removal, redesign, title endorsement, or a combination.",
            ("table", ["Finding", "Possible path to investigate", "Evidence before closing"], [
                ["Improvement encroaches off-parcel", "License, easement, conveyance, relocation, removal, or insurer-approved treatment.", "Executed and recordable documents, revised survey, approvals, title response."],
                ["Neighbor occupies part of parcel", "Boundary analysis, agreement, objection, exception treatment, or counsel-directed resolution.", "Survey evidence, written legal strategy, final policy position."],
                ["Access is unrecorded or narrower than used", "Confirm public access, record easement, reroute, or reject the deal.", "Legal access document plotted on survey and accepted by lender/title."],
                ["Amenity conflicts with easement", "Obtain holder response, modify, relocate, or remove under applicable rules.", "Written authority, permit path, cost, schedule, revised operating plan."],
                ["Buildable envelope is smaller", "Redesign the improvement or re-underwrite without it.", "Feasible concept reviewed by relevant design and permitting professionals."],
                ["Description or parcel mismatch", "Surveyor, title, seller, and counsel reconcile the land actually conveyed.", "Corrected instruments, updated commitment, revised survey and closing documents."],
            ]),
            "When a seller will complete work, define survey update, permit, inspection, title, and buyer-review conditions. When the buyer accepts a credit, the buyer takes execution and overrun risk. Escrow and document remedies require local counsel, lender approval, and precise release terms.",
        ]),
        ("Price the finding through the STR model", [
            "The survey fee is only the cost of information. A finding can change purchase price, usable acreage, guest capacity, improvement scope, legal fees, civil work, utility access, insurance, lender approval, and launch timing. Update both the base case and downside case before removing the survey or title objection deadline.",
            ("ol", [
                "Remove revenue from any bedroom, parking space, amenity, access right, or view claim that is not yet supportable.",
                "Add professional, recording, design, permit, construction, restoration, title, and carrying costs for the proposed remedy.",
                "Stress schedule risk when a neighbor, utility holder, association, agency, lender, or insurer must consent.",
                "Keep a reserve for unresolved field or document conditions; label the assumption rather than hiding it in contingency.",
                "Recheck exit liquidity: a defect the buyer tolerates may create the same lender, title, or buyer objection on resale.",
            ]),
            "Connect the spatial result to the <a href=\"/underwriting/\">acquisition underwriting</a>. A beautiful property can still be the wrong deal when the features supporting its revenue sit outside the buyer's enforceable rights.",
        ]),
        ("Failure modes that turn a map into a closing problem", [
            ("ul", [
                "Treating the county GIS, listing aerial, fence, or seller sketch as the legal boundary.",
                "Ordering a cheap product by name without telling the surveyor the title issue and planned STR use.",
                "Waiting until the final loan week to order work that requires records, field access, title review, and possible revision.",
                "Giving the surveyor a commitment but not the underlying easement and covenant documents.",
                "Assuming an old survey covers improvements and rights created or changed after its field date.",
                "Reading an encroachment as self-executing legal permission—or assuming a drawn easement is valid without title review.",
                "Using the survey as proof of zoning approval, utility location, environmental clearance, or STR legality.",
                "Closing with a promised future easement or corrective deed that is not executed, recordable, plotted, and accepted by the necessary parties.",
            ]),
            ("warn", "Legal and professional boundary: this guide summarizes ALTA, NSPS, and New Jersey public materials reviewed September 24, 2026. It is educational, not surveying, title, legal, zoning, engineering, insurance, appraisal, or investment advice. Survey products and requirements vary by jurisdiction and transaction. Use a licensed local surveyor, title professionals, lender, authorities, and counsel."),
        ]),
        ("Turn the survey into a go, renegotiate, or walk decision", [
            "Proceed when the surveyed land, access, improvements, and material easements support the STR plan; the lender and title insurer accept the deliverable; exceptions are understood; and any remaining risk is priced. Renegotiate when a defined issue has a documentable, executable remedy but the original price or schedule ignored it. Walk away when access, ownership, or a core amenity cannot be established on acceptable terms, or when the correction destroys the investment case.",
            "Pair the survey with the <a href=\"/blog/inspection-contingency-length-str/\">inspection-contingency timeline</a>, the <a href=\"/blog/certificate-of-occupancy-str-remodel/\">remodel approval guide</a>, the <a href=\"/blog/sewer-scope-before-buying-str/\">sewer-lateral guide</a>, and the <a href=\"/design/\">STR design process</a>. Each answers a different question; none substitutes for the others.",
            "The practical next step is to send the title commitment, legal description, relevant recorded documents, prior survey, planned STR site uses, and deadline to a licensed surveyor, title professional, lender, and counsel. Get a written scope that states what the survey will—and will not—answer before authorizing the work.",
            ("callout", "Need boundary and access findings integrated with the acquisition price, amenity plan, reserves, and launch schedule? <a href=\"/apply/\">Apply for a BNB Accelerator strategy call</a>. We can coordinate the investment decision while licensed survey, title, legal, lending, and design professionals handle their conclusions."),
        ]),
    ],
    "faqs": [
        ("Do you need a boundary survey before buying an Airbnb?", "Not every transaction requires a new survey, but it is prudent when the deal depends on boundaries, access, parking, acreage, outdoor amenities, expansion, or title treatment that existing evidence does not resolve."),
        ("Is a county GIS parcel map the same as a survey?", "No. Government GIS programs commonly state that parcel layers are for reference or assessment and do not establish legal boundaries. A licensed surveyor applies records, field evidence, and governing standards."),
        ("What is the difference between a boundary survey and an ALTA/NSPS survey?", "A boundary survey establishes or retraces boundaries under applicable standards. An ALTA/NSPS Land Title Survey adds a nationally defined land-title scope coordinated with title evidence, the insurer, lender, client, optional Table A items, and certification."),
        ("Can a buyer rely on the seller's old survey?", "Only after the surveyor, title insurer, lender, and counsel assess its scope, date, certification, current title evidence, property changes, and transaction requirements. An update may be possible."),
        ("Does a land survey prove an STR is legal?", "No. A survey can locate boundaries and specified features, but STR permission requires separate zoning, licensing, building, fire, HOA, title, and other diligence."),
        ("What should an STR buyer give the surveyor?", "Provide the title commitment, full exception documents, deed and legal description, recorded plats, prior surveys, planned-use memo, relevant unrecorded agreements, lender and insurer requirements, and transaction deadline."),
    ],
    "related": [
        '<a href="/blog/inspection-contingency-length-str/">Set a workable diligence deadline</a>',
        '<a href="/blog/certificate-of-occupancy-str-remodel/">Verify remodel approvals</a>',
        '<a href="/blog/sewer-scope-before-buying-str/">Trace the sewer lateral</a>',
        '<a href="/underwriting/">Re-underwrite the site constraints</a>',
        '<a href="/design/">Coordinate the improvement plan</a>',
    ],
    "cta_h": "Buying an STR with acreage, shared access, or outdoor amenities?",
    "cta_p": "BNB Accelerator can help source and underwrite the property, coordinate the site diligence, and translate survey findings into a purchase decision while qualified local professionals handle survey, title, lender, legal, and permitting requirements.",
}


if __name__ == "__main__":
    blog.build([POST])
    print(f"candidate score: {sum(SCORE.values())}/100 — {SCORE}")
