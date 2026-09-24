#!/usr/bin/env python3
"""STR acquisition decisions: converted sleeping rooms and lead service lines."""

import blog


POSTS = [
    {
        "slug": "converted-bedroom-count-before-buying-str",
        "title": "Can a Converted Room Count as an STR Bedroom?",
        "title_tag": "Can a Converted Room Count as an STR Bedroom? | BNB Accelerator",
        "h1": "Can you count a converted garage or basement as an STR bedroom?",
        "description": "Do not price an STR from its listing bedroom count alone. Verify permits, sleeping-room approval, rental rules, and an occupancy case without the converted space.",
        "date": "2026-09-24",
        "category": "Acquisition Diligence",
        "lead": "Only count a converted garage, basement, attic, or den as a guest bedroom after the local building and STR authorities confirm that the space is approved for sleeping and may be included in the rental's permitted capacity. A seller's listing label, staged bed, tax record, or prior Airbnb photos is not that confirmation. Request permit and final-inspection records, compare the approved floor plan with the actual space, and underwrite the property without the room until the issue is resolved.",
        "sections": [
            ("A furnished room is not an approved sleeping room", [
                "A purchase model may assume four bedrooms because the listing says four, even though the fourth is a converted garage or finished basement. If that room cannot be marketed for sleeping, the buyer may have to reduce advertised capacity, remove a bed, alter the layout, or complete permitted work after closing. This is a specific acquisition decision, not the general <a href=\"/blog/bedroom-configuration-and-rate/\">bedroom configuration and rate</a> question: first establish which spaces can be counted at all.",
                ("callout", "Does the target property's revenue depend on a converted sleeping room? <a href=\"/apply/\">Book a BNB Accelerator acquisition call</a> to compare the permitted-capacity case with the seller's advertised bedroom count before your contingency expires."),
                "Rules vary by jurisdiction and by when the conversion occurred. For example, <a href=\"https://rma.venturacounty.gov/divisions/planning/temporary-rental-unit-ordinance-frequently-asked-questions/\" rel=\"noopener\">Ventura County's STR FAQ</a> says a converted garage or den can be used as a bedroom for its temporary-rental program if the conversion was permitted and final inspection completed. That is a local rule, not a nationwide test. <a href=\"https://www.portland.gov/ppd/astr-permits/short-term-rentals-existing-buildings\" rel=\"noopener\">Portland's STR guidance</a> separately addresses whether attic or basement space was constructed or converted as a sleeping room under applicable historical code. Ask both the building department and rental-permit office for the target address."
            ]),
            ("Reconcile the listing, permit record, and actual floor plan", [
                "Obtain the permit history, approved plans, final inspection or certificate where applicable, current STR permit or eligibility correspondence, and the assessor's property description. Walk the actual room with an inspector: access path, emergency escape and rescue opening, ceiling and floor conditions, heat, ventilation, moisture, alarms, and any equipment that shares the space. These are issues to evaluate, not a universal code checklist; a qualified local inspector and authority must determine compliance.",
                ("table", ["Evidence", "Question it answers", "What to do if missing"], [
                    ["Approved conversion permit and final", "Was the specific work accepted as habitable or sleeping space?", "Ask building staff about record gaps and legalizing options"],
                    ["STR approval and capacity terms", "May this room and guest count be advertised under current rental rules?", "Request address-specific written clarification"],
                    ["Current floor plan and field inspection", "Does the physical room match approved records?", "Get a qualified inspection and updated scope"],
                    ["Parking and site plan", "Did converting a garage remove required parking?", "Recheck parking and guest-capacity assumptions"],
                ]),
                "<a href=\"https://www.portland.gov/ppd/residential-permitting/home-projects/attic-basement-or-garage-conversion\" rel=\"noopener\">Portland says</a> conversion of an attic, basement, or garage to living space requires a building permit there and may require trade permits. <a href=\"https://www.kirklandwa.gov/Government/Departments/Development-Services-Center/Do-you-need-a-permit/Garage-Conversions\" rel=\"noopener\">Kirkland's garage-conversion guidance</a> notes that loss of parking can affect whether conversion is allowed. These examples show why bedroom count, permitting, and parking need to be checked together; they do not establish the rule for another city."
            ]),
            ("Do not assume one egress window legalizes a room", [
                "Emergency escape is an important life-safety question, but it is not the only approval. A local building official may also need to review structural work, ceiling height, heating, insulation, electrical, moisture, or a change in use. <a href=\"https://owatonna.gov/DocumentCenter/View/154/Emergency-Escape-and-Rescue-Openings-PDF\" rel=\"noopener\">Owatonna's building guidance explicitly warns</a> that an egress-window permit by itself does not legalize an unpermitted basement bedroom. Seek a written, property-specific legalization path and cost before assuming a small window budget solves the issue.",
                "Separate a missing paper trail from a confirmed violation. A room built under an older code may have a different documentation path from a recent unpermitted conversion. Do not state to guests that a room is a bedroom, or count its sleeping capacity in underwriting, based solely on a contractor's verbal opinion. Have counsel and the local authority confirm the applicable rules and disclosure obligations."
            ]),
            ("Run the lower-capacity deal before bidding", [
                "Model two cases: an approved-room case supported by documents and a lower-capacity case that excludes the disputed sleeping space. Recompute comparable listings, nightly rate, eligible guest count, parking, cleaning scope, insurance quote, and any occupancy-based fees. Do not merely subtract one bed from a spreadsheet; a property marketed to large groups may move into a different competitive set. Use the <a href=\"/underwriting/downside-scenario/\">downside framework</a> for the lower-capacity case.",
                "Illustrative only: if the seller presents a four-bedroom home but only three sleeping rooms are confirmed, the buyer models a three-bedroom listing until the fourth is approved. A proposed $15,000 legalization budget and a three-month delay are hypothetical assumptions, not market estimates. The decisive comparison is the three-bedroom economics versus the buyer's return threshold, with legalization treated as possible upside only after the authority confirms a feasible path.",
                "Proceed when the approved room count and STR capacity are documented and the supported case works. Renegotiate when a lower count or verified legalization scope changes value. Extend diligence or stop when the extra room is necessary to the deal but the authority cannot confirm its status before the deadline. <a href=\"/apply/\">Book a call to compare the verified-capacity deal with alternatives</a>. This guide is educational, not building-code, legal, insurance, tax, or investment advice."
            ]),
        ],
        "faqs": [
            ("The listing says four bedrooms. Can I underwrite four?", "Only after verifying the approved sleeping rooms and applicable STR capacity. Use a lower-capacity case while a converted room is unresolved."),
            ("Does an egress window make a basement bedroom legal?", "Not by itself. The local authority may require additional approvals and work; obtain address-specific written guidance."),
            ("Does the assessor's bedroom count settle the issue?", "No. Compare tax records with building permits, final inspections, and STR requirements; they answer different questions."),
            ("What if the seller used the room for past guests?", "Historical use does not establish current approval or transferability. Verify before relying on the room in the acquisition model."),
        ],
        "related": [
            '<a href="/blog/bedroom-configuration-and-rate/">Bedroom configuration and rate</a>',
            '<a href="/blog/certificate-of-occupancy-str-remodel/">Certificate-of-occupancy diligence</a>',
            '<a href="/blog/parking-buying-short-term-rental/">Parking before purchase</a>',
            '<a href="/underwriting/downside-scenario/">Downside underwriting</a>',
        ],
        "cta_h": "Price only the sleeping rooms you can verify",
        "cta_p": "We can underwrite the approved-capacity case and compare it with the seller's advertised version before you commit.",
    },
    {
        "slug": "lead-service-line-before-buying-str",
        "title": "Lead Service Line Before Buying a Short-Term Rental",
        "title_tag": "Check a Lead Service Line Before Buying an STR | BNB Accelerator",
        "h1": "How do you check for a lead service line before buying an STR?",
        "description": "Check the utility inventory, both sides of the service line, water testing, replacement responsibility, and timing before buying an older STR property.",
        "date": "2026-09-24",
        "category": "Acquisition Diligence",
        "lead": "For a property on public water, ask the utility for the address-level service-line material classification and the evidence behind it. Check both the utility-owned and customer-owned segments, because ownership can be split. If a segment is lead, galvanized requiring replacement, or unknown, involve the utility, a licensed plumber, and an appropriate certified water-testing laboratory before closing. Obtain a written replacement path, cost responsibility, and timing rather than treating a seller's clean-looking faucet as proof of safe plumbing.",
        "sections": [
            ("Locate the line and separate it from indoor plumbing", [
                "A service line connects the water main to the building inlet. It is different from the home's interior pipes, fixtures, and drinking-water test result. <a href=\"https://www.epa.gov/ground-water-and-drinking-water/planning-and-developing-service-line-inventory\" rel=\"noopener\">EPA's service-line inventory guidance</a> says utilities classify both system and customer portions where ownership is split, using categories that include lead, galvanized requiring replacement, non-lead, and unknown. An 'unknown' record is not a confirmed lead line, but it is also not evidence that the line is non-lead.",
                ("callout", "Looking at an older property with an unknown or lead service-line record? <a href=\"/apply/\">Book a BNB Accelerator acquisition call</a> to compare the verified replacement and launch timeline with other properties before the offer becomes firm."),
                "This is not another general <a href=\"/blog/water-pressure-capacity-before-buying-str/\">water-pressure capacity</a> test. The question is water-supply material, exposure, ownership, replacement, and whether guest service can begin as planned. A strong shower says nothing about the pipe material."
            ]),
            ("Build an address-specific evidence chain", [
                "Start with the utility's publicly accessible inventory or direct written response for the exact address. Ask what material was observed on each side of any ownership split, how it was verified, whether a connector or galvanized section is flagged, and whether the record is merely based on an estimate or construction date. Then ask the seller for service-line replacement invoices, permits, utility correspondence, and any drinking-water results. Have a qualified plumber inspect accessible material; do not excavate or disturb a line based on a blog checklist.",
                ("table", ["Record", "What it can answer", "What it cannot settle alone"], [
                    ["Utility inventory", "Reported material and classification for service-line portions", "Every interior fixture or a definitive exposure result"],
                    ["Plumber's inspection", "Visible material and likely access or replacement route", "Buried material that cannot be observed without verification"],
                    ["Certified lab result", "Lead measured in a correctly collected water sample", "Material of every segment or future levels after disturbance"],
                    ["Replacement plan", "Scope, payer, permits, excavation, restoration, and schedule", "Final cost if exclusions or hidden site conditions remain"],
                ]),
                "<a href=\"https://www.epa.gov/ground-water-and-drinking-water/lcri-questions-and-answers\" rel=\"noopener\">EPA advises</a> contacting the utility or a licensed plumber to determine whether a service line is lead and notes that public inventories can help. Its <a href=\"https://www.epa.gov/ground-water-and-drinking-water/protect-your-tap-quick-check-lead\" rel=\"noopener\">Protect Your Tap guide</a> describes a preliminary check, but a buyer should have uncertainty resolved by qualified parties. Do not infer 'lead-free' from house age or a magnet test alone."
            ]),
            ("Separate sampling, replacement, and guest operations", [
                "A drinking-water sample answers a different question from a material inventory. Ask the local utility or health department which certified lab and sampling protocol applies, and follow that protocol; water chemistry and disturbance can affect results. If the line needs replacement, establish whether the utility or owner pays for each portion, what permits and street or landscaping restoration are needed, when work can occur, and what interim water-use measures the utility recommends. Do not assume a federal program pays the property owner's share or that a replacement can happen before launch.",
                "The <a href=\"https://www.epa.gov/ground-water-and-drinking-water/lead-service-lines\" rel=\"noopener\">EPA identifies lead service lines as a major source of lead exposure in drinking water</a>. Treat this as a health and operating issue, not just a negotiable repair credit. If the source is a private well, the public-water service-line workflow does not apply; follow the <a href=\"/blog/private-well-buying-short-term-rental/\">private-well diligence guide</a> and test the property-specific system."
            ]),
            ("Turn uncertainty into a go/no-go case", [
                "Ask for a written scope including both sides of the line, excavation, meter or curb-stop work, paving or landscaping restoration, water-service interruption, testing, and any exclusions. Confirm whether the utility's schedule controls the project. Get the proposed insurer and lender's requirements if replacement will be incomplete at closing. Keep a separate opening-date scenario if guests cannot be served on the original plan.",
                "Illustrative only: a buyer models $11,000 for owner-side work, $4,000 for pavement and landscaping restoration, and $3,000 for uncertainty, yielding $18,000 of incremental capital. Those are invented sensitivity figures, not a quote or public-program eligibility estimate. If a two-week delay falls in a peak booking period, model lost contribution margin separately from replacement capital using the <a href=\"/underwriting/downside-scenario/\">downside model</a>.",
                "Proceed when the material classification, payer, remediation plan, water-use guidance, and timing are documented and the revised deal works. Renegotiate around verified owner costs and schedule. Extend diligence or stop when the line remains unknown, replacement responsibility is disputed, or safe guest service cannot be established before launch. <a href=\"/apply/\">Book a call to compare the verified deal with cleaner alternatives</a>. This is educational guidance, not medical, plumbing, legal, insurance, tax, or investment advice."
            ]),
        ],
        "faqs": [
            ("Does an 'unknown' utility inventory entry mean the line is lead?", "No. It means the material is not established in that record. Ask the utility and a qualified plumber how to verify it."),
            ("Does a water test identify the service-line material?", "No. A properly collected sample measures lead in that sample; inventory and material investigation answer the pipe question."),
            ("Who pays to replace a lead line?", "Responsibility varies with the utility's ownership split, local program, and property conditions. Get a written, address-specific answer."),
            ("Can I open the STR while waiting for replacement?", "Do not assume so. Follow the utility and health authority's property-specific water-use guidance and confirm the operational, insurance, and rental requirements before advertising stays."),
        ],
        "related": [
            '<a href="/blog/water-pressure-capacity-before-buying-str/">Water-capacity diligence</a>',
            '<a href="/blog/private-well-buying-short-term-rental/">Private-well acquisition</a>',
            '<a href="/underwriting/downside-scenario/">Downside underwriting</a>',
        ],
        "cta_h": "Verify the water line before you price the deal",
        "cta_p": "We can compare the address-specific line record, replacement responsibility, and launch timing with other acquisition candidates.",
    },
]


if __name__ == "__main__":
    blog.build(POSTS)
