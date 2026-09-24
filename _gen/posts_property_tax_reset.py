#!/usr/bin/env python3
"""Post-purchase property-tax underwriting for prospective STR buyers."""

import blog


POSTS = [{
    "slug": "property-tax-reset-after-buying-str",
    "title": "Property Tax Reset After Buying a Short-Term Rental",
    "title_tag": "Will STR Property Taxes Rise After Purchase? | BNB Accelerator",
    "h1": "Will property taxes rise after you buy a short-term rental?",
    "description": "Do not use the seller's tax bill as your STR forecast. Check reassessment rules, exemptions, districts, and the buyer's likely taxable value before offering.",
    "date": "2026-09-24",
    "category": "Acquisition Diligence",
    "lead": "They may, sometimes substantially. The seller's bill describes the seller's taxable value and exemptions under the rules in force for that tax year; it is not a quote for the buyer's first full year. Before relying on cash flow, get the parcel's current assessment record, identify any owner-occupant benefit or assessment limitation, and ask the local assessor how the proposed purchase and rental use will be treated. Underwrite a buyer-case tax line and a separate closing-year proration. The answer varies by jurisdiction, property, transaction, and tax year.",
    "sections": [
        ("The direct answer", [
            "Never copy the current tax bill directly into a short-term-rental acquisition model. First ask whether a sale changes the taxable value, whether the seller has an exemption or limitation that the buyer will not qualify for, and which taxing districts and non-ad-valorem charges apply. Then request an address-specific estimate or calculation method from the assessor or property appraiser. Use a conservative buyer-case figure until the next assessment notice confirms it.",
            ("callout", "Have a property whose cash flow depends on the seller's low tax bill? <a href=\"/apply/\">Book a BNB Accelerator acquisition call</a> to stress-test the post-purchase tax line alongside financing, insurance, and revenue. The local assessor, title company, and tax adviser must confirm the actual property and transaction facts."),
            "This is a property-tax underwriting question, not the transient occupancy or lodging tax collected on guest stays. It is also distinct from the general <a href=\"/blog/the-stress-tests-that-matter/\">STR stress-test guide</a>: the job here is to reconstruct one parcel's tax base and timing before the offer becomes difficult to change."
        ]),
        ("Reconstruct the seller's bill before replacing it", [
            "Pull the latest assessment notice and tax bill from the official county records. Record market or just value, assessed value, taxable value, exemptions, assessment limits, each district's rate, special assessments or non-ad-valorem fees, and the year represented. Those fields are not interchangeable. A low bill can result from a low value, a cap, a homestead exemption, a senior or veteran benefit, a low district rate, or a mix. A listing that only says 'taxes: $4,000' hides the reason.",
            ("table", ["Document or question", "What to capture", "Why it matters"], [
                ["Assessment record", "Market, assessed, and taxable values plus parcel class", "Shows whether the seller's base is below current value"],
                ["Exemption and cap history", "Type, amount, qualification, and change-of-ownership rule", "A buyer-operated STR may not inherit the seller's benefit"],
                ["Tax bill", "District rates, special assessments, and bill year", "The headline rate may omit parcel-specific charges"],
                ["Proposed purchase", "Price, planned ownership, use, renovation, and closing date", "All can change the estimate or timing"],
            ]),
            "The <a href=\"https://floridarevenue.com/property/Documents/pt107.pdf\" rel=\"noopener\">Florida Department of Revenue's buyer guide</a> explains that when ownership changes, the property appraiser removes exemptions and reassesses so assessed value equals just value. Florida's tax calculation uses taxable value and millage, as its <a href=\"https://floridarevenue.com/Property/Pages/Taxpayers.aspx\" rel=\"noopener\">property-tax overview</a> describes. This is a Florida example, not a nationwide rule or a prediction that the new bill equals a fixed percentage of the contract price. Ask the county appraiser about the actual parcel and the year of the reset."
        ]),
        ("Do not assume the seller's homestead treatment follows an investor", [
            "A property that was a primary residence can have a tax profile unlike a whole-home investment rental. The <a href=\"https://comptroller.texas.gov/taxes/property-tax/exemptions/\" rel=\"noopener\">Texas Comptroller says</a> its general residence homestead exemption requires an ownership interest and use as the individual's principal residence; local appraisal districts determine eligibility. An investor buying a home for guest stays should not underwrite the seller's homestead exemption without a property-specific eligibility answer. A buyer who will actually occupy the property has a different fact pattern and should ask the district directly.",
            "Texas appraisal districts generally appraise property as of January 1 each year, according to the <a href=\"https://comptroller.texas.gov/taxes/property-tax/basics.php\" rel=\"noopener\">Comptroller's property-tax basics</a>. That is a different mechanism from Florida's change-of-ownership explanation. This difference is why a universal 'taxes reset to purchase price' rule is not reliable. Confirm the timing, value standard, exemptions, and protest process with the jurisdiction that sends the actual notice.",
            "If the buyer plans to renovate, add sleeping capacity, or change the property's classification, ask whether that work creates a separate assessment change. Do not bury this question inside the furnishing budget: the tax line is recurring, while most launch spending is one-time."
        ]),
        ("Model the first full year, not only closing day", [
            "Ask the assessor or property appraiser for its public estimate tool, a written estimate, or the exact inputs needed to calculate one. Use the current adopted rates if available, note whether proposed rates or district changes are pending, and add parcel-specific fees. If the office cannot estimate a future assessment, build a documented range using the proposed acquisition price, comparable recent assessments, the jurisdiction's valuation rules, and a conservative sensitivity. Keep the source date and the official's response in the deal file; an online calculator is only as good as its assumptions.",
            "Illustrative only: the seller's bill is $4,000 a year, while the buyer's researched base case is $9,000 after losing an exemption and updating the value. The $5,000 difference reduces annual net operating income dollar for dollar before financing and income taxes. If the acquisition was expected to produce $40,000 of annual operating cash flow before debt service on the seller-tax assumption, the buyer-tax case is $35,000 before any other changes. These are invented sensitivity figures, not a tax estimate for any market or parcel. A $5,000 recurring miss is not fixed by a $5,000 one-time seller credit.",
            "Run a downside case if the assessment is uncertain. Recalculate debt-service coverage, cash-on-cash return, and reserves with the higher tax line rather than simply reducing the purchase price in the narrative. The <a href=\"/underwriting/downside-scenario/\">downside framework</a> is useful for that comparison. Do not count a future appeal win in the base case; treat it as optional upside after counsel or the assessor confirms the process and deadline."
        ]),
        ("Keep the closing statement and operating forecast separate", [
            "At closing, buyer and seller may prorate an existing or estimated tax bill under the contract. That adjustment allocates a period's tax burden between the parties; it does not establish the buyer's later annual tax expense. Ask the title company or closing attorney how a later supplemental or corrected bill will be handled, whether the lender's escrow payment uses the seller's bill, and when the new assessment notice is expected. Confirm who receives notices if the owner uses an LLC or a property manager.",
            "A useful acquisition file has two rows: 'tax settlement at closing' and 'stabilized annual property tax.' It also has an owner assigned to update the model when the first post-purchase notice arrives. This prevents a low initial escrow payment from being mistaken for permanent savings. <a href=\"/underwriting/seller-financials/\">Seller financials</a> can inform the historical record, but buyer-specific recurring expenses must replace them in the forecast."
        ]),
        ("Proceed, renegotiate, or stop", [
            "Proceed when the assessment mechanism is understood, the buyer's use and exemption status are verified, the conservative tax case still meets the investment threshold, and reserves cover timing uncertainty. Save the parcel record, assessor correspondence, rate calculation, and revised underwriting.",
            "Renegotiate when the higher recurring cost materially changes value and the seller's stated tax expense was used to justify price. Translate the annual difference into the buyer's own return threshold; do not claim a universal capitalization multiple. Counsel can address any closing proration or post-closing bill language in the contract.",
            "Stop or extend diligence when the jurisdiction cannot confirm a crucial exemption or valuation issue before the deadline, the deal only works if the seller's bill persists, or the downside case fails. <a href=\"/apply/\">Book a call to compare this deal with alternatives</a> before a recurring tax error becomes permanent. This guide is educational, not tax, legal, lending, insurance, or investment advice."
        ]),
    ],
    "faqs": [
        ("Will the new property-tax bill always equal a percentage of my purchase price?", "No. Assessment rules, taxable-value limits, exemptions, district rates, parcel charges, and timing vary. Ask the responsible local office for an address-specific estimate or calculation method."),
        ("Can an investor keep the seller's homestead exemption?", "Do not assume so. Homestead benefits generally depend on the owner's qualifying primary-residence facts. Check the jurisdiction's rules and the proposed buyer's exact use."),
        ("Does the tax proration at closing solve the underwriting issue?", "No. Proration allocates a closing-period bill between buyer and seller; it does not establish the recurring tax line after the next assessment."),
        ("What if the assessor's estimate is not final?", "Use a documented range and a conservative case, preserve the source and date, and update the model when the official notice arrives. Do not underwrite an unconfirmed appeal reduction."),
    ],
    "related": [
        '<a href="/blog/the-stress-tests-that-matter/">STR stress tests</a>',
        '<a href="/underwriting/seller-financials/">Seller financials</a>',
        '<a href="/underwriting/downside-scenario/">Downside underwriting</a>',
        '<a href="/apply/">Book an acquisition call</a>',
    ],
    "cta_h": "Use the buyer's tax bill, not the seller's",
    "cta_p": "We can put the post-purchase assessment estimate into the same model as revenue, financing, insurance, and reserves before you commit.",
}]


if __name__ == "__main__":
    blog.build(POSTS)
