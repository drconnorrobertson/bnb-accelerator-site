#!/usr/bin/env python3
"""Generate the floodplain substantial-improvement guide for STR buyers."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import blog

DATE = "2026-09-24"
SCORE = {
    "distinct_search_intent": 30,
    "buyer_relevance": 24,
    "real_question": 15,
    "service_fit": 14,
    "original_decision_support": 13,
}
assert sum(SCORE.values()) == 96

DESK = "https://www.fema.gov/sites/default/files/documents/fema_nfip_substantial-improvement-substantial-damage-desk-reference.pdf"
FAQ = "https://www.fema.gov/node/628407"
OFFICIALS = "https://www.fema.gov/sites/default/files/documents/fema_floodplain_presenter-guide.pdf"
MSC = "https://msc.fema.gov/portal/home"

POST = {
    "slug": "floodplain-substantial-improvement-str-renovation",
    "title": "Floodplain substantial-improvement rules for STR renovations",
    "title_tag": "Floodplain 50% Rule for an STR Renovation | BNB",
    "h1": "Will the floodplain 50% rule force you to elevate an STR?",
    "description": "Renovating a flood-zone STR? Use this substantial-improvement framework to verify structure value, project cost, local rules, and elevation exposure.",
    "date": DATE,
    "category": "Acquisition Diligence",
    "lead": "It can. In an NFIP-participating community, an improvement to a building in the regulated floodplain can be deemed substantial when the project cost equals or exceeds 50% of the structure's pre-improvement market value. The local floodplain administrator—not the buyer, contractor, lender, appraiser, or insurer—makes the determination under the adopted ordinance. If the project crosses the applicable threshold, the existing building may have to meet floodplain requirements for new construction, which can turn a cosmetic STR renovation into an elevation, foundation, utility, access, and permitting project. Screen this before buying or finalizing the design.",
    "sections": [
        ("The direct answer for an STR buyer", [
            f"FEMA's <a href=\"{FAQ}\" rel=\"noopener\">substantial-improvement guidance</a> defines substantial improvement as reconstruction, rehabilitation, an addition, or another improvement whose cost equals or exceeds 50% of the structure's market value before work starts. Structures with substantial damage are included regardless of how much repair the owner actually proposes. The minimum federal framework is implemented through local floodplain regulations and permits.",
            "Do not divide the renovation budget by the purchase price. The denominator is generally the market value of the structure alone, excluding land and other non-building value. The numerator is not necessarily the cash contract price for the general contractor. The community reviews which labor, materials, overhead, donated work, and related costs must be included under its ordinance and FEMA framework.",
            ("callout", "Evaluating a coastal, river, or lake property with a large launch renovation? <a href=\"/apply/\">Apply for a BNB Accelerator strategy call</a> to pressure-test the acquisition, improvement budget, insurance, and opening timeline. The local floodplain administrator and qualified design professionals must make the regulatory and technical determinations."),
        ]),
        ("Use this six-gate decision tree before pricing the remodel", [
            ("table", ["Gate", "Question", "Required evidence"], [
                ["1. Location", "Is the building in a regulated flood hazard area?", "Effective map, panel and date, zone, floodway status, base flood elevation, and local overlay."],
                ["2. Ordinance", "What threshold, accumulation period, and elevation standard apply?", "Current local floodplain ordinance, amendments, freeboard, and administrator interpretation."],
                ["3. Building status", "Is it pre-FIRM, post-FIRM, conforming, nonconforming, or previously substantially improved?", "Original permits, elevation records, prior SI/SD determinations, and certificate history."],
                ["4. Denominator", "What market value will the community accept for the structure only?", "Accepted assessment method or appraisal that excludes land, site work, furnishings, and business value."],
                ["5. Numerator", "What project costs must be counted?", "Complete labor and material scope, owner labor, donated items, overhead, additions, related trades, and prior cumulative work."],
                ["6. Consequence", "What exact work follows if the threshold is reached?", "Written local determination, required design elevation, foundation, utilities, access, permits, and insurance input."],
            ]),
            "A buyer should resolve the gates in order. An architect cannot reliably redesign around a rule that has not been identified, and a contractor cannot price the consequence without a local determination and elevation target. If the answer at any gate remains unknown, do not treat the renovation contingency as a small percentage of finishes.",
        ]),
        ("The 50% fraction uses building value, not deal value", [
            f"FEMA's current <a href=\"{DESK}\" rel=\"noopener\">Substantial Improvement/Substantial Damage Desk Reference</a> uses the present market value of the structure only, before improvement, as the denominator. Its worksheet excludes land value and calls for a market appraisal or adjusted assessed value accepted by the community. For a damaged building, value is measured before the damage occurred.",
            "That distinction is critical in STR acquisitions. Purchase price can include valuable waterfront land, furniture, a hot tub, a dock, landscaping, bookings, brand assets, or seller goodwill. Those items can make the deal price look large while the structure-only denominator remains much smaller. An income approach based on STR revenue also does not establish the building value used by the official.",
            ("ul", [
                "Ask the floodplain administrator which valuation methods and effective date the community accepts before ordering an appraisal.",
                "Tell the appraiser that the assignment is for a substantial-improvement determination and must separate the structure from land, land improvements, accessory buildings, furnishings, and operating value.",
                "Do not assume the tax assessment's improvement line will be accepted without adjustment; local practice controls.",
                "If the ratio is close to the threshold, obtain a current, defensible structure appraisal and submit it through the official permit process rather than using a broker opinion.",
            ]),
        ]),
        ("The project-cost numerator is broader than a contractor check", [
            "The FEMA worksheet tells officials to use the actual cost of construction and to include volunteer labor and donated supplies. A low contractor bid does not necessarily reduce the official numerator if the owner separately buys materials, performs labor, receives donated finishes, or divides one connected renovation among trades.",
            "Build one master scope that includes demolition, labor, materials, additions, structural work, plumbing, electrical, HVAC, roofing, windows, built-ins, project overhead, and other items the community counts. Then let the administrator classify inclusions and exclusions. Do not omit work because it happens after opening, is paid by a seller credit, or sits in a separate design or furnishing spreadsheet.",
            "FEMA describes limited exclusions, including certain work that directly corrects officially cited health, sanitary, or safety code violations, and special treatment may exist for qualifying historic structures. Those are not broad owner-selected deductions. Obtain written confirmation before removing a line from the substantial-improvement calculation.",
        ]),
        ("Local rules can be stricter and can accumulate projects", [
            f"The minimum NFIP framework uses 50%, but communities can adopt more restrictive rules. FEMA's <a href=\"{OFFICIALS}\" rel=\"noopener\">local-official guidance</a> emphasizes that the community makes the substantial-improvement determination. A local ordinance may use a lower percentage, require freeboard above the base flood elevation, or count cumulative improvements over a stated period.",
            "Cumulative rules matter to a buyer inheriting someone else's permit history. A seller may have renovated a kitchen, added a deck, replaced windows, or repaired storm damage in prior years. Even if the buyer's next project looks safely below 50% in isolation, the community may aggregate it with earlier permitted work. Ask for the official improvement ledger or determination history rather than relying on the seller's memory.",
            ("ol", [
                "Obtain the current ordinance and all locally adopted amendments, not a generic web summary.",
                "Ask whether substantial improvement is calculated per project, per permit, over a rolling period, or over the life of the structure.",
                "Request prior building and floodplain permits, cost affidavits, substantial-damage findings, elevation certificates, variances, and code-enforcement records.",
                "Confirm whether the parcel is in a regulatory floodway or local overlay with additional limits beyond elevation.",
                "Ask which design elevation applies today, including freeboard, before commissioning a feasibility sketch.",
            ]),
        ]),
        ("What happens when the threshold is reached", [
            "Under the NFIP minimum approach, a substantially improved residential building in the Special Flood Hazard Area generally must meet the community's floodplain requirements for new construction. FEMA's worksheet states that a residential pre-FIRM building determined to be substantially improved must be elevated to or above the base flood elevation; local freeboard can require additional height. Other requirements can address foundations, flood-damage-resistant materials, enclosures, utilities, equipment, openings, anchoring, and coastal conditions.",
            "Do not translate that into 'raise the house a few feet' before a qualified designer studies the site. Elevation can affect stairs, accessible routes, decks, parking, headroom, mechanical systems, utility connections, septic or sewer, setbacks, floodway encroachment, wind design, and the guest arrival sequence. The project can also change flood-insurance rating and lender requirements, but only an address-specific quote and design can quantify that.",
            "Post-FIRM buildings also require care. Even when the building already appears elevated, improvements cannot make compliant features noncompliant, and a new determination can invoke current local standards. Verify the as-built elevations and permitted configuration instead of inferring compliance from pilings or exterior photographs.",
        ]),
        ("Worked example: the purchase price hides the trigger", [
            "Assume an illustrative buyer contracts for a coastal STR at $750,000. The price allocation includes land, furnishings, and the operating opportunity. The community accepts a qualified appraisal showing $280,000 as the pre-improvement market value of the principal structure only. The proposed launch renovation has $150,000 of countable labor, materials, and related cost under the local official's review.",
            "The substantial-improvement ratio is $150,000 divided by $280,000, or approximately 53.6%. It is not $150,000 divided by the $750,000 purchase price. At a 50% local threshold, the project would be substantial. The buyer must obtain the official determination and price the resulting compliance scope before deciding whether to close, redesign, renegotiate, or terminate.",
            "Now assume the buyer removes cosmetic work and phases the rest next year. That does not automatically solve the issue. The community may view the work as one project, count necessary related work, or apply a cumulative-improvement rule. A phasing plan should be submitted to the administrator rather than engineered privately to avoid the threshold.",
            "All amounts, allocations, the 53.6% ratio, and property facts are illustrative. They are not BNB Accelerator results or a safe-harbor calculation. The official numerator, denominator, threshold, aggregation method, and consequence come from the applicable ordinance and community determination.",
        ]),
        ("Acquisition diligence before the inspection deadline", [
            ("ol", [
                f"Use the official <a href=\"{MSC}\" rel=\"noopener\">FEMA Flood Map Service Center</a> and local records to identify the effective map, zone, panel, base flood elevation, floodway, amendments, and map-change documents.",
                "Collect the elevation certificate and compare its building diagram, floor elevations, equipment, and survey date with the actual structure and planned guest areas.",
                "Obtain building permits, renovation costs, storm-repair records, substantial-damage findings, prior SI calculations, code citations, and variance files.",
                "Send the complete preliminary scope—not only the contractor's headline price—to the floodplain administrator and ask for the community's required valuation and cost forms.",
                "Commission the accepted structure-only valuation and a code feasibility review when the ratio could approach the threshold.",
                "Price both paths: a below-threshold scope that remains legitimate and useful, and a compliance scope if the project is determined substantial.",
                "Get address-specific builder, lender, and flood-insurance input on the selected permitted configuration; do not assume a renovation credit solves regulatory cost.",
            ]),
            "Make the purchase contract support this work. The diligence period must be long enough to obtain records, meet the administrator, develop a credible scope, and receive qualified estimates. A generic home-inspection contingency may expire before the material floodplain question is answered.",
        ]),
        ("Failure modes that turn finishes into a structural problem", [
            ("ul", [
                "Dividing the renovation cost by purchase price, appraised property value, or projected STR value instead of the accepted structure-only market value.",
                "Using a contractor estimate that omits owner materials, donated work, related trades, overhead, additions, or prior cumulative improvements.",
                "Assuming several small permits avoid aggregation without reading the local ordinance or obtaining written administrator guidance.",
                "Treating an elevation certificate as proof that every existing enclosure, utility, addition, and planned alteration complies with current rules.",
                "Relying on a lender flood determination or insurance quote to replace a floodplain-development permit decision.",
                "Buying furniture and booking photography before the community determines whether the building must be elevated or redesigned.",
                "Assuming an old variance, seller's permit, or pre-FIRM status permanently exempts the structure from current substantial-improvement rules.",
            ]),
            ("warn", "Legal and technical boundary: this guide summarizes FEMA materials reviewed September 24, 2026. It is educational, not legal, engineering, surveying, appraisal, construction, insurance, lending, tax, or investment advice. Local ordinances and official determinations control. Consult the floodplain administrator and qualified professionals before buying or designing work."),
        ]),
        ("Turn the determination into a go/no-go decision", [
            "Before removing contingencies, require a written property file with the governing ordinance, map and elevation evidence, prior permit history, accepted structure value, itemized countable project cost, preliminary or final local determination, and a design-and-cost response for each outcome. If the official will not issue a final determination until a permit application, preserve that limitation and make the contract decision from a conservative, documented scenario.",
            "Connect the result to the full deal. An elevation project may change debt timing, renovation insurance, guest access, parking, design, opening season, reserve needs, and exit value. Use the <a href=\"/underwriting/\">BNB Accelerator underwriting framework</a>, compare the existing <a href=\"/blog/flood-zone-str-underwriting/\">flood-zone offer guide</a>, and coordinate the <a href=\"/blog/vacant-renovation-str-coverage/\">renovation-period insurance plan</a>.",
            "A favorable answer is not merely 'under 50%.' It is a permitted scope that preserves the guest promise, stays within the adopted rule, has an evidence-backed cost, and does not defer an unavoidable compliance problem to the next owner. A negative answer is not necessarily a bad property; it is a signal to redesign, reprice, elevate intentionally, or walk away before the budget is trapped.",
        ]),
    ],
    "faqs": [
        ("What is the floodplain 50% rule?", "Under the NFIP minimum framework, reconstruction, rehabilitation, an addition, or another improvement can be substantial when its cost equals or exceeds 50% of the structure's market value before work starts. The local community makes the determination under its ordinance."),
        ("Is the STR purchase price used in the 50% calculation?", "Generally no. FEMA's framework uses the market value of the structure only and excludes land. Purchase price may also include furnishings, site improvements, bookings, or business value that do not belong in the denominator."),
        ("Can an owner split the STR renovation into smaller permits?", "Do not assume so. Local ordinances may aggregate related work or use cumulative-improvement rules over time. Submit the complete plan to the floodplain administrator and obtain written guidance."),
        ("What happens if a residential STR is substantially improved?", "The building generally must meet the adopted floodplain requirements for new construction. For a pre-FIRM residence, that commonly includes elevation to the required flood elevation, plus local freeboard and other building requirements."),
        ("Who decides whether the renovation is a substantial improvement?", "The local community's authorized floodplain official makes the determination. Contractors, appraisers, insurers, lenders, architects, and buyers supply evidence but do not replace that official decision."),
    ],
    "related": [
        '<a href="/blog/flood-zone-str-underwriting/">Underwrite the complete flood-zone offer</a>',
        '<a href="/blog/vacant-renovation-str-coverage/">Arrange renovation-period insurance</a>',
        '<a href="/blog/inspection-contingency-length-str/">Set a workable diligence timeline</a>',
        '<a href="/underwriting/">Model the acquisition and compliance paths</a>',
        '<a href="/design/">Coordinate the property design scope</a>',
    ],
    "cta_h": "Renovating an STR in a regulated floodplain?",
    "cta_p": "BNB Accelerator can help source and underwrite the property, pressure-test the improvement plan, and coordinate acquisition diligence while the local administrator and qualified flood, design, insurance, and construction professionals make their determinations.",
}


if __name__ == "__main__":
    blog.build([POST])
    print(f"candidate score: {sum(SCORE.values())}/100 — {SCORE}")
