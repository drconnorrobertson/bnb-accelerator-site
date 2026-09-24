#!/usr/bin/env python3
"""Generate the slope-stability diligence guide for STR buyers."""
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
    "original_decision_support": 15,
}
assert sum(SCORE.values()) == 98

USGS_SIGNS = "https://www.usgs.gov/programs/landslide-hazards/what-are-signs-landslide-development-what-do-i-do-if-landslide-occurs"
USGS_MAPS = "https://www.usgs.gov/programs/landslide-hazards/maps"
USGS_HANDBOOK = "https://pubs.usgs.gov/circ/1325/"
NRCS_WSS = "https://websoilsurvey.nrcs.usda.gov/app/"
NRCS_START = "https://www.nrcs.usda.gov/conservation-basics/soil/getting-started-with-web-soil-survey"

POST = {
    "slug": "slope-stability-geotechnical-assessment-before-buying-str",
    "title": "Slope-stability assessments before buying an STR",
    "title_tag": "Slope-Stability Assessment Before Buying an STR",
    "h1": "When should an STR buyer order a slope-stability assessment?",
    "description": "Buying an Airbnb on a slope? Learn when to escalate to geotechnical review, investigate drainage and retaining systems, price uncertainty, and protect closing.",
    "date": DATE,
    "category": "Acquisition Diligence",
    "lead": "Escalate to a qualified geotechnical engineer or engineering geologist when the property, access road, planned construction, or nearby terrain shows credible slope-movement, landslide, debris-flow, settlement, erosion, fill, retaining-wall, or drainage risk. A general home inspection, foundation review, online hazard map, soil-survey rating, seller repair invoice, or dry-day walk-through does not replace a site-specific scope. The purchase decision must define the hazard question, include terrain above and below the parcel, reconcile maps and history with field evidence, investigate water and earthwork, and price both mitigation and the uncertainty that remains.",
    "sections": [
        ("The direct answer for an STR buyer", [
            "Order specialist review when evidence could change whether the site, road, structures, utilities, septic system, retaining features, or planned amenities are supportable. Triggers include mapped susceptibility, known nearby slides, steep or modified slopes, old cut-and-fill pads, undocumented retaining walls, cracks or scarps in the ground, bulges at the slope toe, leaning or offset features, recurring erosion, unexpected springs or seepage, displaced drains, patched pavement, foundation movement connected to the site, post-fire terrain, and material grading or construction plans.",
            f"The U.S. Geological Survey's <a href=\"{USGS_SIGNS}\" rel=\"noopener\">landslide-warning guidance</a> lists possible indicators such as new cracks, bulges or deformation in soil and pavement; new water flow or ponding; leaning poles, fences or trees; sticking openings and new building cracks; broken utilities; soil separating from foundations; and abnormal well-level changes. USGS also warns that some landslides occur suddenly without warning. Visible signs justify escalation; their absence is not a guarantee of stability.",
            ("callout", "Evaluating a mountain cabin, hillside home, bluff property, steep private road, or site with retaining structures? <a href=\"/apply/\">Apply for a BNB Accelerator strategy call</a> to connect geotechnical diligence with the offer, financing, insurance, renovation plan, reserves, and launch date. Qualified local geotechnical, geological, civil, structural, drainage, legal, surveying, insurance, lending, and permitting professionals must make their respective conclusions."),
        ]),
        ("Assess the whole terrain system, not only the house", [
            "Slope hazards do not respect parcel lines or the footprint of a home inspection. Material can originate uphill, move through the subject, undermine a road, or continue into downhill property. Water can arrive from roads, roofs, neighboring grading, failed utilities, springs, drainage easements, or natural channels. Start with the terrain and drainage system that can affect the acquisition, then narrow the professional scope.",
            ("table", ["Zone", "Evidence to investigate", "STR consequence"], [
                ["Uphill source area", "Scarps, cuts, fills, channels, disturbed soil, rockfall, wildfire, roads, development, drainage outlets.", "Material or water may reach the house even when the subject slope looks intact."],
                ["Building pad and foundations", "Grading history, fill, settlement, cracks, movement monitoring, drainage, repair records.", "Repair may require site stabilization, not only cosmetic or structural work."],
                ["Slope face and toe", "Bulging, erosion, seepage, retaining, excavation, loss of support, debris, vegetation change.", "Toe disturbance or saturation can change stability and usable outdoor space."],
                ["Driveway and private road", "Pavement cracks, settlement, washouts, culverts, walls, cuts, shoulders, alternate access.", "Guests, vendors, lenders, and emergency services may lose the only route."],
                ["Utilities and wastewater", "Broken lines, leaks, trenches, tanks, drain fields, wells, poles, buried services.", "Water release can worsen conditions; movement can interrupt occupancy."],
                ["Downhill runout area", "Historic deposits, channels, neighboring structures, road or stream crossings.", "A slide may create offsite damage, access loss, liability, or regulatory response."],
            ]),
            "Give the specialist access to the current survey, topography when available, legal drainage and access documents, parcel history, aerial imagery, site plans, road records, retaining-wall information, geologic and landslide mapping, utility records, claims, repairs, permits, and the buyer's proposed use. A street address alone is not a meaningful scope boundary.",
        ]),
        ("Use maps as screening evidence, not a property verdict", [
            f"USGS maintains <a href=\"{USGS_MAPS}\" rel=\"noopener\">national landslide inventory and susceptibility mapping</a> assembled from federal, state, and local sources. Maps can identify historical landslides, regional susceptibility, post-fire debris-flow concerns, and earthquake-triggered ground-failure context. They are valuable for asking better questions, but coverage, resolution, date, triggers, and mapped phenomena vary.",
            f"The USGS <a href=\"{USGS_HANDBOOK}\" rel=\"noopener\">Landslide Handbook</a> explains that susceptibility maps show relative slope stability rather than absolute predictions. A property outside a mapped polygon is not proven stable; a property inside a broad susceptibility zone is not proven to be actively moving. Site grading, undocumented fills, small failures, altered drainage, recent fire or storms, and offsite source or runout paths may not appear at the map scale.",
            ("ol", [
                "Record the map title, agency, edition or date, scale or resolution, legend, modeled hazard, source inventory, and stated limitations.",
                "Locate the entire parcel, access route, uphill contributing area, downhill runout or channel, and planned improvements—not only the house pin.",
                "Check local and state geologic, landslide, steep-slope, flood, erosion, fire, grading, and critical-area sources in addition to national screening.",
                "Compare current and historical aerial imagery, topography, permits, reports, and seller records for site changes after the mapped data date.",
                "Give the source files and observations to the qualified professional; do not convert a color category into a repair budget or insurance conclusion yourself.",
            ]),
        ]),
        ("Soil surveys help screen, but field investigation answers the site question", [
            f"USDA NRCS operates <a href=\"{NRCS_WSS}\" rel=\"noopener\">Web Soil Survey</a>, which provides official soil-survey information and interpretations. NRCS states that onsite investigation is needed for some conservation and engineering applications. Its <a href=\"{NRCS_START}\" rel=\"noopener\">current Web Soil Survey instructions</a> show how to define an area of interest and review soil properties and suitability or limitation ratings.",
            "Use soil mapping to identify questions about mapped units, depth, drainage, hydrologic group, shrink-swell potential, flooding or ponding, erosion, excavation, septic suitability, shallow rock, and building-site limitations where available. Then ask the geotechnical professional what subsurface information is needed for this decision. A map unit can contain variation that a parcel-scale design or stability conclusion must address.",
            ("table", ["Evidence type", "What it can support", "What it cannot prove alone"], [
                ["Soil or geologic map", "Regional materials, mapped limitations, screening questions.", "Actual layer depths, strength, groundwater, fill, or stability at the improvement."],
                ["Landslide inventory", "Recorded or mapped prior events and pattern context.", "Absence of unrecorded, small, concealed, or future movement."],
                ["Topographic or lidar data", "Landform, slope, scarps, drainage, historic comparison where available.", "Subsurface geometry, current strength, or every artificial modification."],
                ["Dry-season walk-through", "Visible conditions on that date.", "Wet-season seepage, storm response, concealed drains, or transient groundwater."],
                ["Boring, test pit, monitoring, or lab work", "Property-specific data within the designed scope.", "Conditions outside explored locations or a guarantee against all future events."],
            ]),
        ]),
        ("Define the professional question and investigation level", [
            "A buyer may need a reconnaissance, records review, geologic evaluation, targeted geotechnical investigation, retaining-wall evaluation, drainage study, movement monitoring, or design-level work. Do not assume every concern requires drilling, and do not assume a visual letter can support a major stabilization design. Ask the responsible licensed professional to explain the scope needed for the contractual decision and the limitations of a smaller scope.",
            ("ul", [
                "Who is the client, intended user, and reliance party, and will the lender or insurer accept the report?",
                "What exact parcels, slopes, walls, roads, structures, utilities, channels, and planned improvements are included?",
                "Which records, maps, photographs, prior reports, weather or event history, and neighboring observations will be reviewed?",
                "Will the work include topographic survey, subsurface exploration, sampling, laboratory testing, groundwater observation, instrumentation, calculations, or only visual reconnaissance?",
                "What assumptions govern groundwater, seismic loading, rainfall, fire effects, drainage, future grading, occupancy, and the time period of the opinion?",
                "Will the report distinguish observed conditions, interpretations, uncertainty, immediate controls, further work, mitigation concepts, and design recommendations?",
                "What permits, access agreements, utility locating, traffic controls, excavation restoration, and safety planning are required for fieldwork?",
            ]),
            "Professional titles and practice authority vary by state. Confirm the individual's current license, discipline, landslide or local-geology experience, insurance, independence, and ability to seal the work product the lender, authority, designer, or contractor will require. A structural engineer's building review and a geotechnical professional's site review can be complementary rather than interchangeable.",
        ]),
        ("Water is usually part of the diligence story", [
            "Do not discuss slope movement without tracing water. Inventory roof drains, paved runoff, driveway ditches, culverts, springs, seeps, swales, foundation drains, wall drains, irrigation, pools and hot tubs, wells, septic, water and sewer lines, neighboring discharge, natural channels, and storm overflow. Identify where each starts, crosses, discharges, and can be maintained.",
            ("ol", [
                "Collect drainage plans, grading permits, as-built records, easements, maintenance records, repair invoices, utility leak history, and wet-season photographs.",
                "Walk the site after lawful access during or soon after representative rain when it is safe; never enter an active slide, unstable slope, flooded channel, or falling-rock area.",
                "Map ponding, concentrated discharge, sediment, rills, gullies, clogged inlets, wet walls, seepage, springs, soft shoulders, and water emerging where it was not expected.",
                "Ask the professional whether drainage is a cause, symptom, load, trigger, or mitigation dependency—and which data are still missing.",
                "Verify that proposed fixes have a lawful discharge point and do not transfer water or instability to a road, stream, neighbor, septic field, or downhill structure.",
            ]),
            "A French drain, wall drain, ditch, or pipe is not evidence of a complete solution. It can be undersized, unmaintainable, broken, unpermitted, disconnected, or discharging into the wrong place. Price inspection, cleaning, outlets, access, monitoring, and replacement—not only the visible inlet.",
        ]),
        ("Worked example: a cabin above a steep access road", [
            "Assume an illustrative buyer is evaluating a hillside cabin above a single-lane private road. The home inspection notes foundation cracks and a leaning timber wall. Listing photographs show a dry yard, while older aerial imagery suggests the parking pad was expanded. The seller provides an invoice for wall repair but no engineering, grading, or drainage records. The buyer plans a hot tub downhill of the cabin and overflow parking near the slope edge.",
            "The buyer's structural engineer evaluates the building but recommends geotechnical escalation because the wall, fill pad, drainage, road cut, and foundation response form one site system. A qualified geotechnical professional reviews available maps and records, walks the uphill drainage and downhill road, and designs targeted exploration. The report identifies undocumented fill and unresolved drainage assumptions, then defines additional data and interim restrictions before any design conclusion.",
            "The buyer pauses the hot tub and parking plan, obtains survey and drainage support, asks the lender and insurer to review the findings, and prices the specified investigation and potential stabilization pathways without pretending the highest or lowest concept is certain. Counsel preserves the inspection remedy while the evidence develops. The property, observations, reports, improvements, and responses are illustrative—not a client result, diagnosis, engineering opinion, or cost forecast.",
        ]),
        ("Turn findings into an acquisition decision", [
            "Separate immediate life-safety or access controls from investigation, design, construction, monitoring, and long-term maintenance. A conceptual mitigation option is not a buildable scope. A contractor estimate is not an engineering design. A seller credit is not a stability conclusion. Keep each dependency explicit through closing.",
            ("table", ["Finding state", "Buyer response to investigate", "Evidence before decision"], [
                ["No material indicator within adequate scope", "Proceed with stated limitations, maintenance, and event triggers.", "Signed report, mapped scope, assumptions, insurer and lender acceptance as needed."],
                ["Uncertainty can be reduced", "Extend diligence for records, survey, exploration, testing, monitoring, or wet-season observation.", "Professional scope tied to the unresolved mechanism and contract deadline."],
                ["Bounded mitigation is supportable", "Obtain design, permits, matched bids, access, sequencing, monitoring, and completion criteria.", "Issued design and complete scope—not a conceptual allowance alone."],
                ["Offsite or shared dependency", "Obtain easements, consent, association or road action, authority review, and legal analysis.", "Enforceable access and responsibility plus technical feasibility."],
                ["Risk or cost remains open-ended", "Redesign, reduce use, reprice, preserve contingency, or terminate.", "Do not close by converting missing evidence into a favorable assumption."],
            ]),
            "Put surveys, exploration, laboratory work, design, permits, grading, access, shoring, excavation, soil and rock handling, walls, anchors, piles, drainage, erosion control, utilities, road repair, septic impacts, landscaping, monitoring, professional observation, carrying cost, amenity loss, closure nights, and an uncertainty reserve into the <a href=\"/underwriting/\">STR underwriting framework</a>. Keep low, expected, and downside cases tied to evidence rather than arbitrary percentages.",
        ]),
        ("Protect the contract, financing, insurance, and closing", [
            "Coordinate the title, survey, inspection, financing, appraisal, insurance, association, permit, and feasibility deadlines. Site investigation may need seller permission for drilling or test pits, utility locating, restoration obligations, access across other parcels, disclosure handling, indemnity, report reliance, and time for laboratory results. Local counsel should draft or review the transaction language.",
            ("ul", [
                "Title and survey: access, drainage and slope easements, encroachments, maintenance duties, common walls, road rights, and affected parcels.",
                "Lender and appraisal: property eligibility, required reports, repairs, completion escrow, access, marketability, and final inspection.",
                "Insurance: landslide, earth movement, subsidence, water, retaining structures, access, vacancy, renovation, business use, and required mitigation under the actual policy and carrier decision.",
                "Authorities: grading, steep-slope, critical-area, flood, erosion, building, retaining-wall, septic, stream, wildfire, and right-of-way requirements.",
                "Closing evidence: approved design where required, recorded access, permits, contractor scope, funding, monitoring baseline, completion criteria, warranties, and post-work professional documentation.",
            ]),
            "Do not ask title insurance to insure physical stability, a lender to certify safety, or a permit to guarantee performance. Each participant answers a narrower question. The acquisition lead must reconcile the answers into one decision record.",
        ]),
        ("Build post-closing monitoring and emergency controls", [
            "If the property proceeds, turn the professional report into manager instructions. Map restricted zones, drains, walls, instruments, inspection points, road segments, utility shutoffs, and contacts. Define routine maintenance, professional observation, rainfall or event triggers, stop-use criteria, guest relocation, road closure, emergency notification, and records retention.",
            ("ol", [
                "Escalate new cracks, bulges, settlement, leaning features, blocked drainage, seepage, broken pipes, wall movement, rockfall, muddy flow, or unusual ground sounds without staff attempting a diagnosis.",
                "After intense or prolonged rain, wildfire, earthquake, flood, construction, excavation, utility failure, or known nearby movement, follow the professional event-response and reinspection plan.",
                "Keep guests and staff outside a suspected slide, rockfall, collapse, or runout area; contact emergency and local authorities when conditions warrant.",
                "Do not send cleaners or maintenance workers onto unstable ground to clear a drain, photograph damage, move debris, or reopen a road.",
                "Record the observation time, weather or event, location, photographs from a safe place, restrictions, notifications, professional response, and reopening authority.",
            ]),
            "USGS emphasizes that landslides are dangerous and difficult to predict. An STR emergency plan should never promise that staff can inspect or repair an actively moving site. Life safety and authority instructions take priority over bookings, property access, and documentation.",
        ]),
        ("Failure modes and the practical next step", [
            ("ul", [
                "Treating a broad susceptibility map or soil rating as a parcel-specific stability conclusion.",
                "Inspecting only the foundation while ignoring the uphill source, slope face, toe, road, drainage, walls, utilities, and downhill runout.",
                "Assuming dry-day conditions represent wet-season groundwater, storm discharge, or post-fire response.",
                "Accepting a repaired crack, patched road, new wall face, or seller invoice without the underlying cause, design, permit, and completion evidence.",
                "Ordering field exploration without a defined engineering question, utility locating, lawful access, restoration, or enough time for results.",
                "Using a contractor's allowance as proof that mitigation is technically feasible and fully scoped.",
                "Adding a hot tub, pool, parking pad, deck, road widening, trench, or drainage outlet without reassessing slope and water effects.",
                "Launching without event triggers, restricted zones, safe reporting, road-closure rules, and professional reopening authority.",
            ]),
            ("warn", "This guide summarizes USGS and USDA NRCS materials reviewed September 24, 2026. It is educational, not geotechnical, geological, civil, structural, hydrologic, environmental, emergency, legal, survey, insurance, lending, contracting, tax, or investment advice. Maps, site conditions, licensing, hazards, permits, coverage, and remedies vary. Landslides and related ground failures can occur suddenly and without visible warning. Use qualified local professionals and current authority instructions."),
            "The practical next step is to map the uphill-to-downhill terrain and drainage system, collect historical and current records, photograph indicators from safe lawful locations, write the exact acquisition and improvement questions, and request a qualified professional's scope before the inspection deadline expires.",
            ("callout", "Need a slope concern translated into a diligence scope, purchase decision, reserve, and realistic opening plan? <a href=\"/apply/\">Apply for a BNB Accelerator strategy call</a>. We can coordinate the acquisition framework while qualified local geotechnical, geological, engineering, legal, insurance, lending, surveying, and permitting professionals handle their conclusions."),
        ]),
    ],
    "faqs": [
        ("When should a buyer hire a geotechnical engineer for an STR?", "Escalate when mapped hazards, steep or modified terrain, cracks, bulges, seepage, retaining systems, road distress, prior movement, post-fire conditions, undocumented fill, or planned earthwork could change the acquisition."),
        ("Does a home inspection evaluate slope stability?", "Usually not as a site-specific geotechnical opinion. Read the inspection scope and obtain the qualified discipline needed for soils, rock, groundwater, earthwork, retaining, or landslide questions."),
        ("Can a landslide map prove a property is safe?", "No. Maps are screening and planning tools with limits in scale, data, date, trigger, coverage, and modeled processes. USGS states that susceptibility maps show relative conditions and do not replace site-specific investigation."),
        ("Is Web Soil Survey enough for a foundation or retaining-wall decision?", "No. It provides valuable official soil-survey data and interpretations, but NRCS notes that onsite investigation is needed for some engineering applications. The responsible professional defines property-specific work."),
        ("Should an STR buyer inspect uphill and downhill property?", "The professional scope should consider terrain and water that can affect the subject, including offsite source and runout areas, while respecting legal access. Parcel boundaries do not stop water or moving earth."),
        ("Can a seller credit solve slope-stability risk?", "A credit may reallocate a bounded cost, but it does not establish the cause, feasibility, permits, access, design, lender or insurer acceptance, offsite rights, or final construction cost."),
    ],
    "related": [
        '<a href="/blog/structural-engineer-foundation-cracks-before-buying-str/">Escalate foundation findings correctly</a>',
        '<a href="/blog/private-road-maintenance-agreement-before-buying-str/">Protect private-road access</a>',
        '<a href="/blog/tree-risk-assessment-before-buying-str/">Assess trees and changing slopes</a>',
        '<a href="/underwriting/">Model investigation and mitigation</a>',
        '<a href="/apply/">Discuss the acquisition strategy</a>',
    ],
    "cta_h": "Buying an STR on steep, modified, or uncertain ground?",
    "cta_p": "BNB Accelerator can help source and underwrite the property, coordinate diligence, and translate site findings into an acquisition and launch plan while qualified local professionals handle their conclusions.",
}


if __name__ == "__main__":
    blog.build([POST])
    print(f"candidate score: {sum(SCORE.values())}/100 — {SCORE}")
