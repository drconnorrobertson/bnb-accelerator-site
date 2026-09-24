#!/usr/bin/env python3
"""Generate the sewer-scope acquisition guide for STR buyers."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import blog

DATE = "2026-09-24"
SCORE = {
    "distinct_search_intent": 30,
    "buyer_relevance": 24,
    "real_question": 14,
    "service_fit": 13,
    "original_decision_support": 14,
}
assert sum(SCORE.values()) == 95

EPA_CONDITION = "https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=P1008C45.TXT"
EPA_CMOM = "https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=30006OW9.TXT"
PORTLAND_VIDEO = "https://www.portland.gov/bes/connecting-sewer/sewer-photo-video-map"
PORTLAND_REPAIR = "https://www.portland.gov/ppd/publicworks/ur-uc-permit-guide"
PORTLAND_CODE = "https://www.portland.gov/code/17/32/070"

POST = {
    "slug": "sewer-scope-before-buying-str",
    "title": "Sewer scopes before buying a short-term rental",
    "title_tag": "Sewer Scope Before Buying an STR | Buyer Guide",
    "h1": "Should you get a sewer scope before buying an STR?",
    "description": "Buying an Airbnb on public sewer? Use this sewer-scope framework to verify the full lateral, repair responsibility, permits, bids, and closing remedies.",
    "date": DATE,
    "category": "Acquisition Diligence",
    "lead": "Usually, yes—order a camera inspection when the property has a private sewer lateral and the condition or route is not already documented by a recent, complete, transferable report. A general home inspection, a freely draining toilet, and a public-sewer connection do not show the buried pipe's full condition. The decision-ready package is the video, written findings, route and depth information, ownership boundary, local compliance status, repair alternatives, and property-specific bids obtained before the inspection contingency expires.",
    "sections": [
        ("The direct answer for an STR buyer", [
            "A sewer scope is not automatically required by one nationwide home-sale rule. It is a risk and diligence decision, and some local programs separately require testing, certification, or repair when property transfers or other triggers occur. The buyer should ask the local sewer utility and permitting authority what applies to the address rather than assuming the closing agent or home inspector will catch it.",
            f"EPA's <a href=\"{EPA_CONDITION}\" rel=\"noopener\">wastewater collection-system condition guide</a> identifies lateral closed-circuit television inspection as a method that can show leaks, water stains, changes in pipe material or diameter, sags, and bends. It also notes that recordkeeping for laterals is often incomplete. That is why a clean utility account or a line on a municipal map is not a condition report.",
            ("callout", "Evaluating an older home, tree-covered lot, steep cabin, long lateral, or prior backup? <a href=\"/apply/\">Apply for a BNB Accelerator strategy call</a> to pressure-test the acquisition, repair reserve, closing structure, and launch plan. Licensed plumbers, sewer contractors, utilities, engineers, inspectors, and local authorities must perform and interpret their respective work."),
        ]),
        ("Define the asset before ordering the inspection", [
            "First confirm that the building actually discharges to a public sanitary sewer. A listing marked 'public sewer' can still leave questions about a shared or party line, private collection system, ejector pump, force main, converted septic system, or route across another parcel. Ask for utility records, connection permits, repair history, diagrams, easements, and any active notices.",
            ("table", ["Question", "Why it changes the decision", "Evidence to collect"], [
                ["What does the property use?", "A septic inspection and a sewer-lateral scope answer different questions.", "Utility confirmation, bills, septic abandonment record, connection permit."],
                ["Which pipe is private?", "The buyer may own only part of the route—or much more than expected.", "Utility responsibility map, code, parcel map, written agency response."],
                ["Is the line shared?", "Repairs, access, capacity, and cost allocation may involve neighbors or an association.", "Recorded easement, maintenance agreement, HOA documents, connection diagram."],
                ["How does sewage reach the main?", "Gravity, pumps, long runs, steep drops, and multiple buildings create different failure modes.", "As-built plans, cleanout locations, pump records, route and depth locating."],
                ["Does a local trigger apply?", "Sale, renovation, added plumbing, utility work, or a prior defect can create an inspection or correction obligation.", "Current ordinance, utility program rules, permits, compliance certificate."],
            ]),
            "Do not let the inspection vendor guess the legal ownership boundary. The camera operator can document what the equipment reaches; the utility, code, deeds, easements, and qualified advisers establish who owns, may access, and must repair each segment.",
        ]),
        ("A complete sewer scope is more than a video file", [
            f"The City of Portland's <a href=\"{PORTLAND_VIDEO}\" rel=\"noopener\">official sewer video guidance</a> is a useful example of a documented submittal: it calls for a video, written report, surface photographs of the located sewer, and a map or diagram. Its local rules do not govern other cities, but the package illustrates why an unlabeled phone clip is weak acquisition evidence.",
            ("ol", [
                "Identify the address, inspection date, operator, access point, direction of travel, and equipment used.",
                "Run and record the accessible length toward the public connection, not merely the easiest interior segment.",
                "Keep continuous distance references and identify material, diameter, connections, transitions, bends, sags, roots, deposits, offsets, cracks, deformation, infiltration, and standing water.",
                "Locate the route and important defects at the surface when practical; record approximate depth and uncertainty.",
                "State where the camera stopped and why—blockage, trap, bend, collapse, inaccessible cleanout, or equipment limit.",
                "Deliver the unedited video, still images, written findings, sketch, recommended next steps, and any limitations.",
            ]),
            "A 'pass' with no grading standard is not enough. Ask the qualified inspector to distinguish routine maintenance from defects that need further evaluation, repair, replacement, or agency review. The buyer's job is then to translate those findings into ownership, access, cost, schedule, and operating consequences.",
        ]),
        ("The full-length rule prevents false reassurance", [
            "A camera that travels 18 feet in a 90-foot lateral has inspected only 18 feet. If a trap, root mass, offset, or missing cleanout stops the camera, record the limitation and decide whether cleaning, another access point, or a new cleanout is needed during the contingency period. Do not call an incomplete run 'clear.'",
            f"EPA's collection-system guide lists lateral CCTV as one of several assessment methods and notes that mainline CCTV may see only the first few feet of a lateral. A municipal main inspection therefore does not substitute for a property-side scope. In one local example, Portland's <a href=\"{PORTLAND_REPAIR}\" rel=\"noopener\">lateral repair and connection guide</a> separates private-property and right-of-way permits and responsibilities.",
            ("ul", [
                "Confirm whether the camera reached the municipal main, a city branch, a shared line, or only a visible transition.",
                "Ask who owns every uninspected segment and whether the buyer can legally reach it for inspection and repair.",
                "Check whether cleaning before scoping could remove evidence or is necessary to obtain usable footage; let the qualified vendor set the protocol.",
                "When a line is inaccessible, carry the unresolved segment as a named risk with a contract remedy and downside reserve.",
            ]),
        ]),
        ("Separate condition from ownership and compliance", [
            "Three conclusions are required. Condition asks what the pipe looks like and how it functions. Ownership asks who maintains and pays for each segment. Compliance asks whether the connection, material, route, shared arrangement, and proposed repair satisfy current local rules. One conclusion cannot prove the other two.",
            f"EPA's <a href=\"{EPA_CMOM}\" rel=\"noopener\">CMOM program guide</a> explains that local sewer-use ordinances may address private-lateral inspection and that some communities use an inspection before property sale. That is program guidance, not a nationwide transfer requirement. Check the current local ordinance and obtain an address-specific answer.",
            f"Responsibility can turn at a curb, property line, cleanout, easement, branch, or main. Portland's current <a href=\"{PORTLAND_CODE}\" rel=\"noopener\">maintenance code</a>, for example, assigns obligations by system ownership and street or easement configuration. Cite local examples only as examples—the target property's governing documents control.",
        ]),
        ("Read the findings as an acquisition decision tree", [
            ("table", ["Finding", "Next diligence step", "Do not assume"], [
                ["Roots or deposits", "Ask whether cleaning allows a second full inspection and whether entry points indicate a structural defect.", "That routine snaking permanently fixes the cause."],
                ["Standing water or a sag", "Have the qualified contractor assess severity, length, slope, flow, and repair options.", "That water in one frame proves either failure or acceptability."],
                ["Crack, offset, deformation, or collapse", "Locate it, verify access and ownership, and obtain comparable repair scopes.", "That a spot price covers excavation, restoration, permits, and the remaining line."],
                ["Material transition", "Document each material and joint; assess age, condition, and compatibility in context.", "That one visible modern section means the full line was replaced."],
                ["Shared or off-parcel route", "Review recorded rights, maintenance allocation, capacity, and neighbor or HOA obligations.", "That historic use creates a clean, transferable access right."],
                ["Camera cannot pass", "Create access or investigate under the vendor's protocol before waiving the contingency.", "That the unseen downstream segment is sound."],
                ["No observed defect", "Preserve the complete report and still verify ownership, compliance, and operating history.", "That a scope guarantees future performance."],
            ]),
            "The scope is evidence at one point in time. It does not certify future flow, rule out intermittent backups, determine structural engineering questions, or replace plumbing, title, code, utility, and insurance diligence.",
        ]),
        ("Worked example: an older four-bedroom cabin", [
            "Assume an illustrative buyer is evaluating a 1968 four-bedroom cabin connected to public sewer. The listing says the sewer line was 'updated,' the seller provides a receipt for 25 feet of replacement, and toilets drain normally. Mature trees cover the front yard, the main is across the road, and no cleanout is visible near the property line.",
            "A licensed vendor scopes from a basement cleanout. The video shows newer plastic near the building, then a transition to older pipe, root intrusion, and standing water before the camera stops at 54 feet. Surface locating places the stoppage near the roadside, but the team does not yet know whether the unseen segment lies on private property, in the right-of-way, or in an easement.",
            "The receipt did not prove a full replacement; it documented only the first section. The buyer obtains the utility responsibility map and permit history, has a qualified contractor clear the obstruction under an agreed protocol, orders a second full run, locates the route, and gets two matched-scope bids. The bids separately state access, traffic control, excavation or lining assumptions, permits, inspection, surface restoration, and warranty.",
            "The buyer then compares three remedies before the contingency expires: seller completes an approved repair with transferable records; seller credits a negotiated amount and the buyer controls the work after closing; or the buyer terminates if access, timing, or total cost remains unacceptable. The dates, layout, findings, and remedies are illustrative, not a client result or prediction.",
        ]),
        ("Price the whole repair, not the pipe alone", [
            "A verbal per-foot number is not a renovation budget. The path to the pipe may cross a slab, finished room, deck, retaining wall, steep slope, landscaped yard, driveway, sidewalk, public street, or another parcel. A technically feasible liner may still require access work, cleaning, spot repair, permits, inspection, or connection corrections.",
            ("ul", [
                "Diagnosis: cleaning, repeat video, locating, engineering or utility review, and access creation.",
                "Construction: spot repair, full replacement, lining or bursting where allowed, cleanouts, pump work, and code corrections.",
                "Public interface: utility coordination, permits, inspections, traffic control, right-of-way work, bonds, and approved contractors.",
                "Restoration: slab, flooring, walls, driveway, sidewalk, landscaping, drainage, retaining features, and neighbor property.",
                "STR impact: vacancy, contractor lead time, furnishing sequence, guest cancellation exposure, and reopening verification.",
                "Uncertainty: concealed conditions, unscoped length, depth, rock, groundwater, utilities, easement access, and change orders.",
            ]),
            "Move the complete matched-scope number into the <a href=\"/underwriting/\">property underwriting</a> and preserve a separate uncertainty reserve. Do not finance the purchase to the edge and assume the first month's revenue will fund a buried-line emergency.",
        ]),
        ("Choose a closing remedy that preserves control", [
            "The best remedy depends on defect certainty, contractor availability, permits, lender and insurer requirements, and the buyer's tolerance for post-closing construction. A seller repair can preserve buyer cash but creates scope-control and documentation risk. A credit gives the buyer control but may not equal the eventual cost and can be limited by the loan structure. Escrow arrangements require counsel, lender approval, precise release conditions, and enough money.",
            ("ol", [
                "Attach the video, report, route sketch, utility answer, and bid scope to the decision file.",
                "Define the defect and the exact acceptable remedy; avoid 'repair sewer as needed.'",
                "Name required permits, licensed parties, inspections, testing, restoration, warranties, paid receipts, and record transfer.",
                "Give the buyer review and reinspection rights before funds release or contingency removal.",
                "Address what happens if the camera cannot verify the repaired segment or new defects appear.",
                "Confirm the remedy works with the purchase contract, title, lender, insurer, utility, and closing schedule.",
            ]),
            "Contract language and escrow mechanics are legal work. Use local counsel and the closing professionals rather than copying a clause from another market.",
        ]),
        ("Translate the scope into STR operations", [
            "A sewer line that is acceptable for acquisition still needs an operating plan. Record cleanout locations, shutoff and utility contacts, plumber escalation details, known restrictions, pump alarms if present, and the boundary between a guest clog and a lateral failure. Train the manager to take slow drains, gurgling, sewage odors, and repeated fixture backups seriously.",
            "High guest turnover does not automatically prove the pipe needs replacement, but it changes the cost of failure. A backup can take bedrooms or the whole property offline, trigger specialized cleanup, damage finishes, and disrupt future reservations. Confirm insurance treatment and emergency vendors before launch rather than after sewage reaches a guest area.",
            "Keep the acquisition video, final repair footage, permits, inspections, warranties, invoices, easements, utility correspondence, and route map in the permanent property file. Give the manager the operating information without exposing unrelated sensitive closing records.",
        ]),
        ("Failure modes that turn a pipe issue into a bad deal", [
            ("ul", [
                "Skipping the scope because the property is connected to a municipal sewer rather than septic.",
                "Treating normal fixture drainage on inspection day as proof of buried-pipe condition.",
                "Accepting footage that stops early without measuring and explaining the uninspected length.",
                "Assuming the city owns everything outside the parcel or the owner owns only to the property line.",
                "Calling a partial replacement receipt proof that the full lateral is modern and permitted.",
                "Obtaining one repair number that excludes locating, access, right-of-way work, permits, restoration, and STR downtime.",
                "Letting the seller close a defect without buyer reinspection, final video, approvals, warranty, and paid records.",
                "Ignoring shared lines, off-parcel routes, and missing easements because the connection has worked historically.",
            ]),
            ("warn", "Legal and technical boundary: this guide summarizes EPA and Portland public materials reviewed September 24, 2026. Portland is an example, not a rule for other jurisdictions. This is educational, not plumbing, engineering, environmental, legal, title, insurance, construction, or investment advice. Use qualified local professionals and the responsible utility and authorities."),
        ]),
        ("Turn the sewer scope into a go, renegotiate, or walk decision", [
            "Proceed when the full accessible route is documented, important limitations are resolved or priced, ownership and access are clear, local compliance is confirmed, and the complete repair downside fits the deal. Renegotiate when a defined defect has an executable scope but the original price or timeline ignored it. Walk away when the seller blocks appropriate investigation, the line cannot be legally accessed or repaired on acceptable terms, or open-ended cost and launch delay break the investment case.",
            "Pair this workflow with the <a href=\"/blog/inspection-contingency-length-str/\">inspection-contingency guide</a>, the <a href=\"/blog/str-cash-reserves-seasonality/\">cash-reserve framework</a>, and the <a href=\"/blog/normalize-str-utility-bills/\">utility normalization guide</a>. If the property uses onsite wastewater instead, start with the <a href=\"/blog/septic-system-inspection-short-term-rental/\">septic inspection guide</a> rather than treating a sewer camera as a substitute.",
            "The practical next step is simple: identify the wastewater system, ask the utility for the address-specific responsibility and compliance record, then order the right inspection early enough to obtain follow-up access and repair bids before the contingency deadline.",
            ("callout", "Need the sewer finding integrated with the purchase price, reserves, contractor timeline, and STR opening plan? <a href=\"/apply/\">Apply for a BNB Accelerator strategy call</a>. We can coordinate the acquisition decision while licensed local professionals handle the pipe, permits, title, and legal conclusions."),
        ]),
    ],
    "faqs": [
        ("Should every STR buyer get a sewer scope?", "A scope is usually prudent when a property has a private sewer lateral and no recent complete report proves its condition. Local transfer or compliance rules may separately require testing or certification."),
        ("Does a home inspection include a sewer camera inspection?", "Do not assume it does. Confirm the exact home-inspection scope and separately order a qualified sewer-lateral camera inspection when needed."),
        ("What should a sewer-scope report include?", "Keep the complete video, written findings, distance references, materials, defects, route and important surface locations, endpoint, limitations, still images, and recommended next steps."),
        ("Who pays for a damaged sewer lateral?", "Responsibility varies by jurisdiction, ownership, location, easement, shared-line agreement, and contract. Obtain the applicable utility or code map and address-specific professional advice."),
        ("What if the camera cannot reach the sewer main?", "Treat the uninspected segment as unresolved. Ask a qualified vendor whether cleaning, another access point, a cleanout, locating, or another method is appropriate before the contingency expires."),
        ("Can an STR buyer accept a seller credit instead of repair?", "Possibly, after confirming the full scope, financing limits, access, permits, timing, and downside. A credit transfers execution and overrun risk to the buyer."),
    ],
    "related": [
        '<a href="/blog/inspection-contingency-length-str/">Set a workable inspection period</a>',
        '<a href="/blog/septic-system-inspection-short-term-rental/">Inspect an onsite septic system</a>',
        '<a href="/blog/str-cash-reserves-seasonality/">Build the acquisition reserve</a>',
        '<a href="/blog/normalize-str-utility-bills/">Normalize utility evidence</a>',
        '<a href="/underwriting/">Model the complete downside case</a>',
    ],
    "cta_h": "Buying an STR with an undocumented sewer lateral?",
    "cta_p": "BNB Accelerator can help source and underwrite the property, coordinate acquisition diligence, and translate the inspection into a purchase decision while qualified local professionals handle the sewer, utility, title, permit, and legal work.",
}


if __name__ == "__main__":
    blog.build([POST])
    print(f"candidate score: {sum(SCORE.values())}/100 — {SCORE}")
