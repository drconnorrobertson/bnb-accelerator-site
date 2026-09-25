#!/usr/bin/env python3
"""Five STR acquisition, financing and management guides (September 24, 2026)."""

import blog

DATE = "2026-09-24"
POSTS = []

POSTS.append({
    "slug": "str-maximum-offer-price-from-revenue",
    "title": "How to Back Into a Maximum Offer Price on a Short-Term Rental",
    "title_tag": "STR Maximum Offer Price: Work Backward From Revenue | BNB Accelerator",
    "h1": "How to back into a maximum offer price on a short-term rental",
    "description": "Stop anchoring on list price. Work backward from supportable STR revenue, operating costs, debt terms and your return hurdle to find the most you should pay.",
    "date": DATE,
    "category": "Underwriting",
    "lead": "Most buyers start with the list price and ask whether the deal works. A disciplined buyer starts with the numbers the property can realistically produce and asks what price those numbers support. Working backward from revenue gives you a hard ceiling before emotion, bidding pressure or a persuasive listing agent enters the room. This guide walks through the sequence: supportable gross revenue, a full operating budget, net operating income, a debt test, a cash return test and a downside test. The lowest of those answers is your walk-away number.",
    "sections": [
        ("Why the list price is the wrong starting point", [
            "A listing price reflects what a seller hopes to receive, what nearby homes sold for as residences, and sometimes a pro forma built on the best year the market ever had. None of those inputs tells you what the property will earn for you under your financing, your management choice and current demand. When you begin at the list price, every later assumption tends to bend toward justifying it: occupancy creeps up, cleaning costs drift down, and the capital reserve quietly disappears.",
            "Reversing the order changes the conversation. You build the operating picture first, then solve for the price. If the result sits above the asking price, you have margin and can move quickly. If it sits below, you know exactly how far apart you are and why, which makes a counteroffer specific rather than arbitrary. Pair this with the <a href=\"/blog/seller-proforma-vs-trailing-revenue/\">seller pro forma versus trailing revenue</a> review so the seller's story does not set your anchor.",
        ]),
        ("Step one: set supportable gross revenue", [
            "Supportable revenue is not the peak year and not the average of every listing in the zip code. Build a comparable set of properties with similar bedroom count, sleeping capacity, amenities and location quality, then look at trailing twelve month revenue for the middle of that set rather than the top performers. If the subject property has its own operating history, compare it against the comps and ask why it outperforms or lags. A property that beats its comps by 30 percent usually has a reason, and you need to know whether that reason transfers to you.",
            "Adjust for ramp-up if the home is not currently operating or will change management. New listings often need several months to build reviews and ranking. The <a href=\"/blog/new-listing-ramp-underwriting/\">new listing ramp guide</a> covers how to haircut the first year. Use a base case you would be comfortable defending to a skeptical partner, and keep an optimistic case separate so it never becomes the number you pay for.",
        ]),
        ("Step two: build the full operating budget", [
            "Net operating income is gross revenue minus every recurring cost of running the property, before debt service. For a short-term rental that list is long: platform fees, management or co-hosting fees, cleaning and laundry, supplies and consumables, utilities including internet and streaming, property insurance written for STR use, property taxes at the post-sale assessed value, lodging tax if not remitted by the platform, pest control, landscaping or snow removal, pool or hot tub service, software, licensing and permit fees, and routine repairs.",
            "Add a capital reserve for furniture, appliances, linens and larger systems. Short-term rentals wear faster than long-term rentals because of turnover. Many operators reserve a fixed percentage of gross revenue, while others build a line-item replacement schedule using the <a href=\"/blog/str-capex-planning/\">STR capex planning</a> approach. Either method is acceptable as long as the reserve exists. A useful sanity check is the <a href=\"/underwriting/expense-ratio/\">expense ratio guide</a>: if your total operating costs land well below what similar properties run, revisit the inputs before trusting the result.",
            ("table", ["Line item", "How to estimate", "Common mistake"], [
                ["Cleaning", "Local turnover rate times projected stays", "Using the guest cleaning fee as if it were pure profit"],
                ["Management", "Quoted percentage of gross or net revenue", "Leaving it out because you plan to self-manage"],
                ["Property tax", "Post-sale assessed value and local rate", "Using the seller's current bill"],
                ["Insurance", "Written STR-specific quote", "Using a homeowner policy estimate"],
                ["Capital reserve", "Percentage of gross or replacement schedule", "Setting it to zero in year one"],
            ]),
        ]),
        ("Step three: solve for price three different ways", [
            "With net operating income in hand, run three independent tests. The first is a debt coverage test. Decide the minimum debt service coverage ratio you or your lender require, divide NOI by that ratio to find the maximum annual debt service, and convert that payment into a maximum loan amount at your quoted rate and term. Add your planned down payment and you have a price ceiling from the lending side. The <a href=\"/financing/dscr-loans/\">DSCR loan guide</a> explains how lenders typically view that ratio.",
            "The second is a cash-on-cash test. Decide the minimum annual pre-tax cash flow you require relative to the total cash you invest, including down payment, closing costs, furnishing, setup and initial reserves. Solve for the price at which your projected cash flow after debt service meets that hurdle. The third is a yield test: divide NOI by your required unlevered yield, sometimes called a cap rate, to get a value that ignores financing entirely. This keeps you honest when cheap debt makes an expensive property look attractive.",
            "Your maximum offer is the lowest of the three results, not the average. Each test protects against a different failure: running short on debt payments, tying up cash for a poor return, or overpaying relative to what the income stream is worth to the next buyer. The <a href=\"/blog/str-cap-rate-sale-price/\">STR cap rate and sale price article</a> is useful context for the third test.",
        ]),
        ("Step four: stress the answer before you write the offer", [
            "Run the same math with revenue 15 to 20 percent lower and costs 10 percent higher. If your maximum price under that downside case is dramatically lower, the deal depends on everything going right. That does not automatically mean walking away, but it should narrow how aggressively you bid. The <a href=\"/underwriting/downside-scenario/\">downside scenario framework</a> and <a href=\"/underwriting/break-even-occupancy/\">break-even occupancy guide</a> give you a structured way to see how much cushion exists.",
            "Also confirm the non-financial gates: legal STR use at that address, HOA rules, permit transferability and insurance availability. A property that cannot legally operate as a short-term rental is worth whatever it is worth as a residence, and your revenue-based price means nothing. Keep a written summary of your maximum price and the assumptions behind it so that if negotiations drag on, you are adjusting inputs deliberately rather than drifting upward.",
            ("callout", "Want a second set of eyes on a specific property? <a href=\"/apply/\">Book a BNB Accelerator call</a> and we will walk through supportable revenue, operating costs and a price ceiling before you write an offer."),
        ]),
        ("Using the number in negotiation", [
            "A revenue-based ceiling gives you a clear, explainable position. Instead of saying the price is too high, you can say the property supports a specific value at current operating costs and show the lines that drive it: an insurance quote, a reassessed tax bill, a cleaning rate. Sellers and agents may not agree with your revenue view, but documented cost inputs are harder to dismiss.",
            "Leave yourself room between the opening offer and the ceiling, and decide in advance which terms could substitute for price. A seller credit toward furniture, an extended inspection period, or inclusion of existing bookings can each be worth real money. Once the ceiling is reached, the discipline is to stop. There will be another property, and the buyers who struggle most are usually the ones who paid a price the numbers never supported.",
        ]),
    ],
    "faqs": [
        ("What is the fastest way to estimate a maximum offer on an Airbnb?", "Estimate supportable annual revenue from comparable listings, subtract a full operating budget including a capital reserve to get NOI, then solve for price using your required debt coverage, cash-on-cash return and unlevered yield. Use the lowest result."),
        ("Should I use the seller's revenue numbers?", "Use them as one input and verify them against platform statements and comparable properties. Seller figures often reflect a peak year or exclude costs such as management and capital replacement."),
        ("What if my maximum price is below the asking price?", "Share the specific cost and revenue inputs that drive your number, offer at or below your ceiling, and consider non-price terms such as seller credits. If the gap cannot close, walking away is a legitimate result."),
        ("Does a lower interest rate raise my maximum price?", "It can raise the debt and cash-on-cash ceilings, but the unlevered yield test does not change with financing. Keeping that test in the mix prevents cheap debt from pushing you into overpaying."),
    ],
    "related": [
        '<a href="/underwriting/break-even-occupancy/">Break-even occupancy</a>',
        '<a href="/underwriting/expense-ratio/">STR expense ratio</a>',
        '<a href="/blog/seller-proforma-vs-trailing-revenue/">Seller pro forma versus trailing revenue</a>',
        '<a href="/revenue-projections/">Revenue projections</a>',
    ],
    "cta_h": "Know your ceiling before you bid",
    "cta_p": "We help investors set a revenue-based price limit on specific STR properties so offers are driven by numbers, not pressure.",
})

POSTS.append({
    "slug": "str-owner-statement-review",
    "title": "How to Review a Property Manager's Monthly Owner Statement",
    "title_tag": "How to Review an STR Owner Statement | BNB Accelerator",
    "h1": "How to review a property manager's monthly owner statement",
    "description": "A practical checklist for reading STR owner statements: reconcile bookings, verify fees, catch pass-through markups and track the KPIs that show whether your manager is performing.",
    "date": DATE,
    "category": "Management",
    "lead": "If a professional manager or co-host runs your short-term rental, the monthly owner statement is the main window into how the property is performing and how your money is being handled. Many owners glance at the payout number and move on. That habit makes it easy to miss duplicated cleaning charges, fees calculated on the wrong base, maintenance invoices without support, and slow revenue erosion that only shows up when you compare months side by side. A fifteen minute monthly review, done the same way each time, catches most of these issues early.",
    "sections": [
        ("Know what a complete statement should contain", [
            "A useful owner statement shows every reservation that checked out or was booked in the period, with dates, nights, the channel it came from, the nightly rate, cleaning fee, any extra fees and the platform commission. It then shows the management fee and the base it was calculated on, each expense with vendor and description, any reserve contributions or draws, and the net amount paid to you. Supporting invoices or receipts should be available on request or attached.",
            "If your statement is a single number with a short summary, ask for the detail. Most property management software can export a reservation-level report. Your management agreement should already say what reporting you are entitled to; if it does not, add that at renewal. The <a href=\"/blog/str-property-management-fees/\">property management fees guide</a> explains common fee structures so you know what base the percentage should be applied to.",
        ]),
        ("Reconcile bookings against the platform", [
            "Once a quarter, and whenever something looks off, compare the reservation list on the statement against the calendar and payout history in the listing platforms. If you have owner access to the Airbnb or Vrbo account, this takes a few minutes. You are checking that every stay appears, that nights and rates match, and that cancellations with partial payouts were credited correctly.",
            "Pay attention to direct bookings and owner or friends-and-family stays. Direct bookings are harder to verify because there is no third-party record, so ask for the payment processor report. Blocked nights labeled as maintenance or owner use deserve a quick question if they cluster in high-demand weeks. The <a href=\"/blog/blocked-calendar-demand-signal/\">blocked calendar article</a> covers how blocked nights distort occupancy data.",
        ]),
        ("Check fees and pass-through charges", [
            "Confirm that the management percentage is applied to the base stated in the contract. Some agreements calculate the fee on gross booking revenue including cleaning fees, others on net revenue after platform fees, others on rent only. A fee applied to gross when the contract says net can quietly cost several hundred dollars a month on a busy property.",
            "Next, look at cleaning. If guests pay a cleaning fee and the cleaner is paid separately, the statement should show both and the difference should match what your agreement allows. Watch for linen, supply or restocking charges that duplicate items already included in the cleaning rate. For maintenance, ask whether the manager adds a markup or coordination fee to vendor invoices; that is common and often permitted, but it should be disclosed and consistent with the agreement.",
            ("table", ["Item", "What to verify", "Red flag"], [
                ["Management fee", "Rate and calculation base match the contract", "Fee applied to cleaning revenue when contract excludes it"],
                ["Cleaning", "Number of cleans equals number of checkouts", "More cleans than stays with no explanation"],
                ["Maintenance", "Invoice, vendor and description for each charge", "Round-number charges with no support"],
                ["Supplies", "Reasonable cost per stay, trending stable", "Sudden jump without a change in occupancy"],
                ["Reserve", "Contributions and draws itemized", "Reserve balance falling without listed repairs"],
            ]),
        ]),
        ("Track performance, not just payout", [
            "The payout number mixes performance, seasonality and expenses together. Pull out a few metrics each month and keep them in a simple spreadsheet: occupancy, average daily rate, revenue per available night, number of stays, average length of stay, average review score, and total operating cost as a share of revenue. Compare each month to the same month last year and to comparable listings in your market.",
            "Falling occupancy with a stable rate may point to weaker ranking or a pricing tool set too high. Rising occupancy with a falling rate may mean the manager is discounting to fill the calendar. A creeping expense ratio can signal inefficient turnovers or vendor pricing that no one is renegotiating. The <a href=\"/blog/occupancy-versus-rate-which-to-optimize/\">occupancy versus rate article</a> and the <a href=\"/underwriting/expense-ratio/\">expense ratio benchmark</a> help you interpret what you see.",
            ("callout", "Not sure whether your manager's results are competitive for your market? <a href=\"/apply/\">Book a call with BNB Accelerator</a> and we will benchmark your statements against comparable properties."),
        ]),
        ("Raising issues and escalating", [
            "When you find a discrepancy, send a short written note listing the reservation or charge, what you expected and what the statement shows, and ask for an explanation or correction. Most errors are clerical and get fixed quickly. Keep the tone factual. Managers handle many properties, and a clear request is easier to act on than a general complaint.",
            "If issues repeat, or if explanations are vague, review the performance and termination terms of your agreement. Many contracts allow termination with notice, sometimes with a fee or restrictions on transferring future bookings. Knowing those terms before a problem escalates keeps your options open. The <a href=\"/blog/str-management-agreement-termination/\">management agreement termination guide</a> covers what to look for, and <a href=\"/blog/cohosting-vs-self-managing/\">co-hosting versus self-managing</a> outlines alternatives if you decide to change structure.",
        ]),
        ("Build a routine you will actually keep", [
            "Put a recurring fifteen minute block on your calendar within a few days of each statement arriving. Use the same checklist every month: payout matches bank deposit, every checkout has one clean, fee base is correct, each expense over a set threshold has an invoice, KPIs logged. Once a quarter, add the platform reconciliation and a comparison against last year.",
            "This routine does more than catch errors. It signals to your manager that you are paying attention, which tends to improve reporting quality on its own. It also gives you clean records if you ever refinance, sell the property or bring in a partner, because buyers and lenders will ask for the same information you have already organized.",
        ]),
    ],
    "faqs": [
        ("How often should I review my STR owner statement?", "Review it monthly with a short checklist, and do a deeper reconciliation against platform payout records each quarter."),
        ("What should a property manager's owner statement include?", "Reservation-level detail with dates, channels, rates and fees, the management fee and its calculation base, itemized expenses with support, reserve activity and the net payout."),
        ("Is it normal for managers to mark up maintenance invoices?", "Many managers add a coordination fee or markup. It is generally acceptable when disclosed in the agreement and applied consistently. Undisclosed or inconsistent markups are worth raising."),
        ("Which KPIs matter most when reviewing a manager?", "Occupancy, average daily rate, revenue per available night, review score and operating cost as a percentage of revenue, each compared year over year and against comparable listings."),
    ],
    "related": [
        '<a href="/blog/str-property-management-fees/">STR property management fees</a>',
        '<a href="/blog/cohosting-vs-self-managing/">Co-hosting versus self-managing</a>',
        '<a href="/underwriting/expense-ratio/">STR expense ratio</a>',
        '<a href="/management/">Management resources</a>',
    ],
    "cta_h": "Make sure your manager is earning the fee",
    "cta_p": "We benchmark management performance against comparable listings and help owners decide whether to optimize, renegotiate or switch.",
})

POSTS.append({
    "slug": "str-management-agreement-termination",
    "title": "STR Management Agreement Termination Clauses: What to Check Before You Sign",
    "title_tag": "STR Management Agreement Termination Clauses | BNB Accelerator",
    "h1": "STR management agreement termination clauses: what to check before you sign",
    "description": "Before signing with an Airbnb property manager, review notice periods, termination fees, future bookings, listing ownership, reviews and data handover so you can leave cleanly.",
    "date": DATE,
    "category": "Management",
    "lead": "Most owners read a property management agreement for the fee and skip to the signature line. The clauses that matter most, though, are the ones that govern how the relationship ends. Termination terms decide how long you are locked in, what it costs to leave, who keeps the listing and its reviews, what happens to guests already booked, and whether you walk away with the data you need to keep operating. Negotiating these points at the start is far easier than arguing about them after trust has broken down.",
    "sections": [
        ("Notice periods and initial terms", [
            "Many agreements run for an initial term of six to twelve months and then renew automatically, with a notice period of thirty to ninety days to terminate. Some allow termination without cause at any time with notice; others restrict termination during the initial term except for cause. Read both the renewal language and the notice mechanics, including how notice must be delivered. A contract that requires written notice by certified mail sixty days before the renewal date can accidentally lock you in for another year.",
            "Ask for termination without cause on thirty days notice after a reasonable initial period, and immediate termination for cause such as failure to remit funds, loss of required licenses, or material breach. If the manager insists on a longer term, ask for performance benchmarks that let you exit early if results fall well below an agreed standard.",
        ]),
        ("Termination fees and what they cover", [
            "Some managers charge a termination fee, often framed as recovering onboarding costs such as photography, listing setup and furnishing coordination. That can be reasonable in the first year. Look at how the fee is calculated: a flat amount, a percentage of trailing revenue, or the management fee on future bookings. A fee equal to several months of projected commissions is expensive and worth negotiating down or phasing out over time.",
            "Clarify whether the fee applies when you sell the property, convert it to a long-term rental, or move in yourself. A sale-related fee can complicate an exit, a point covered in the <a href=\"/blog/assign-str-management-contract-sale/\">management contract assignment on sale</a> guide. Many owners negotiate a clause that waives the fee upon sale to an unrelated buyer.",
        ]),
        ("Future bookings and guest handoff", [
            "At any moment a busy short-term rental may have months of reservations on the calendar. The agreement should state what happens to them. Common approaches include the manager honoring and servicing all stays through a cutoff date and earning its fee on them, the owner taking over bookings with the manager paid a reduced fee, or bookings being transferred where the platform allows it. Each approach has tradeoffs, but ambiguity is the real problem: guests can be caught in the middle and your reviews can suffer.",
            "Also confirm who holds guest payments and security deposits for future stays and when they are remitted. Funds collected for bookings after the termination date should be accounted for and transferred on a defined timeline, not simply held until the final statement.",
            ("table", ["Clause", "Owner-friendly version", "Watch out for"], [
                ["Notice", "30 days without cause after the initial term", "Auto-renewal with a narrow notice window"],
                ["Termination fee", "Flat fee that declines to zero after year one", "Fee equal to projected future commissions"],
                ["Future bookings", "Clear cutoff with defined servicing and fee", "Silence on who services existing reservations"],
                ["Listing ownership", "Listing held in the owner's account", "Listing held only in the manager's account"],
                ["Data handover", "Guest, vendor, access code and financial records within 10 days", "No obligation to provide records"],
            ]),
        ]),
        ("Listing ownership and reviews", [
            "This is the clause that surprises owners most often. If the Airbnb or Vrbo listing sits in the manager's account, it usually stays with the manager when you leave. You would then relaunch as a new listing with no reviews, which can depress rates and occupancy for months. The <a href=\"/blog/first-90-days-airbnb-launch/\">first 90 days launch guide</a> shows how much effort rebuilding momentum takes.",
            "Where possible, keep the listing in an account you own and add the manager as a co-host with appropriate permissions. If the manager requires its own account, ask whether it will support a transfer at termination and put that in writing. Also agree on ownership of listing photography, the property's direct booking website or domain if one exists, and any custom guidebooks or house manuals.",
        ]),
        ("Records, access and vendor relationships", [
            "When management ends you need to keep operating the next day. The agreement should require the manager to deliver, within a set number of days, the guest communication history for upcoming stays, vendor contacts and pricing for cleaning and maintenance, smart lock and wifi credentials, inventory lists, warranty information, and a final accounting with supporting documents. Access codes should be reset as part of the handoff.",
            "Check for non-solicitation clauses that prevent you from hiring the cleaners or maintenance vendors the manager used. Some restriction is understandable, but a broad clause can leave you scrambling for turnover coverage at the worst possible time. Negotiate an exception for vendors who worked at your property, or at minimum a short restriction period.",
            ("callout", "Evaluating a manager or reviewing an agreement before signing? <a href=\"/apply/\">Book a BNB Accelerator call</a> to compare management options and the operating terms that protect your property's performance."),
        ]),
        ("Negotiating and documenting the terms", [
            "Managers generally expect some negotiation, especially from owners with well-performing properties. Prioritize the terms with the biggest downside: listing ownership, future booking handling and the termination fee. Propose specific language rather than general objections. If a manager refuses reasonable exit terms, treat that as information about how the relationship might go.",
            "Keep a signed copy of the agreement and any amendments with your property records, and set a calendar reminder ahead of each renewal notice deadline. Pair this with a monthly <a href=\"/blog/str-owner-statement-review/\">owner statement review</a> so that if performance slips, you have documentation and a clear path out. For a broader view of fee structures, see the <a href=\"/blog/str-property-management-fees/\">property management fees guide</a>. This article is general education, not legal advice; have a qualified attorney review any contract before signing.",
        ]),
    ],
    "faqs": [
        ("Can I cancel an Airbnb property management contract early?", "It depends on the agreement. Many allow termination with thirty to ninety days notice after an initial term, and immediate termination for cause. Read the renewal and notice provisions carefully."),
        ("Who keeps the Airbnb listing and reviews when I change managers?", "Whoever owns the platform account usually keeps the listing. Keeping the listing in your own account with the manager as a co-host is the most reliable way to retain reviews."),
        ("Are termination fees normal for STR managers?", "They are common, often justified by onboarding costs. A modest flat fee that declines over time is typical; a fee equal to months of projected commissions is worth negotiating."),
        ("What records should a manager hand over at termination?", "Upcoming guest communications, vendor contacts and rates, access credentials, inventory and warranty information, and a final accounting with supporting documents."),
    ],
    "related": [
        '<a href="/blog/str-property-management-fees/">STR property management fees</a>',
        '<a href="/blog/assign-str-management-contract-sale/">Assigning a management contract on sale</a>',
        '<a href="/blog/cohosting-vs-self-managing/">Co-hosting versus self-managing</a>',
        '<a href="/management/">Management resources</a>',
    ],
    "cta_h": "Sign a management agreement you can exit",
    "cta_p": "We help owners compare managers and structure operations so the listing, reviews and data stay with the property.",
})

POSTS.append({
    "slug": "blanket-loan-vs-individual-mortgages-str",
    "title": "Blanket Loans vs Individual Mortgages for a Short-Term Rental Portfolio",
    "title_tag": "Blanket Loan vs Individual Mortgages for STRs | BNB Accelerator",
    "h1": "Blanket loans vs individual mortgages for a short-term rental portfolio",
    "description": "Compare blanket portfolio loans with separate mortgages for multiple STRs: rates, cross-collateral risk, release clauses, prepayment terms and when each structure fits.",
    "date": DATE,
    "category": "Acquisition Financing",
    "lead": "Once an investor owns two or three short-term rentals, lenders start offering a different option: roll the properties into a single blanket or portfolio loan. One closing, one payment and sometimes access to more capital can be appealing. The tradeoff is that the properties become tied together, and the terms that govern selling, refinancing or losing one property matter far more than the headline rate. This guide compares the two structures so you can decide which fits your portfolio and plans.",
    "sections": [
        ("How each structure works", [
            "With individual mortgages, each property carries its own loan, secured only by that property. You might use a conventional investment loan on one, a DSCR loan on another and a local bank loan on a third. Each has its own rate, term, payment and qualification. If one property underperforms, only that loan is directly affected, and you can sell or refinance one property without touching the others.",
            "A blanket loan is a single loan secured by multiple properties. It is usually offered by portfolio lenders, commercial banks, credit unions and some DSCR lenders. Qualification tends to focus on the combined cash flow of the portfolio and the borrower's experience rather than personal income alone. The <a href=\"/financing/dscr-loans/\">DSCR loan guide</a> explains how property-level income is typically evaluated, and many blanket programs apply similar logic at the portfolio level.",
        ]),
        ("Where blanket loans help", [
            "The practical benefits are simplicity and capacity. One closing replaces several, which can reduce total lender and title costs even though each property still needs its own appraisal and title work. One payment and one set of reporting requirements simplify administration. Investors who have reached the limit on the number of conventional loans they can hold sometimes use a blanket loan to keep growing.",
            "A blanket loan can also allow stronger properties to support weaker ones. If one property has an excellent debt coverage ratio and another is still ramping up, the combined numbers may qualify when the weaker property alone would not. Some blanket structures also allow cash-out on existing equity across several properties at once, which can fund the next acquisition.",
        ]),
        ("The risks that come with cross-collateralization", [
            "Tying properties together means a default on the loan affects every property securing it. If one market suffers a regulatory change or a demand shock, the stress is shared across the whole portfolio rather than isolated. Before choosing a blanket structure, review your <a href=\"/blog/str-portfolio-diversification/\">portfolio diversification</a> and ask whether the properties are exposed to the same risks.",
            "The most important clause is the partial release provision. It governs whether and how you can sell or refinance one property without paying off the entire loan. A typical release requires paying down a set percentage of that property's allocated loan amount, often more than 100 percent, and may require the remaining properties to still meet a minimum coverage ratio. Without a workable release clause, selling a single property can force a full refinance.",
            ("table", ["Feature", "Individual mortgages", "Blanket loan"], [
                ["Collateral", "One property per loan", "Multiple properties on one loan"],
                ["Selling one property", "Pay off that loan only", "Subject to release clause and paydown"],
                ["Rate and term", "Each loan priced separately, often longer fixed terms", "Often shorter fixed periods or balloons"],
                ["Qualification", "Per property and per borrower", "Combined portfolio cash flow and experience"],
                ["Default impact", "Isolated to one property", "Affects all pledged properties"],
            ]),
        ]),
        ("Rates, terms and prepayment", [
            "Blanket loans from portfolio and commercial lenders often carry shorter fixed-rate periods, commonly five to ten years, sometimes with a balloon payment at maturity. That creates refinance risk if rates are higher or lending standards are tighter when the loan comes due. Individual residential mortgages, especially conventional loans, may offer thirty-year fixed terms that remove that timing risk entirely.",
            "Prepayment penalties are also common on blanket and DSCR loans, structured as step-downs or yield maintenance. These can make an early sale or refinance expensive. Read the term sheet with the same care you would give any DSCR offer; the <a href=\"/blog/reading-a-dscr-term-sheet/\">DSCR term sheet guide</a> walks through the clauses that matter. Compare total cost over your realistic hold period, not just the rate.",
            ("callout", "Planning your second or third STR and weighing how to finance it? <a href=\"/apply/\">Book a BNB Accelerator acquisition call</a> to align deal selection with a financing structure that fits your growth plan."),
        ]),
        ("How to decide", [
            "Individual mortgages usually fit investors who value flexibility, expect to sell or refinance properties at different times, own properties in different markets with different risk profiles, or can access long fixed-rate terms. They also keep problems contained. The main costs are more paperwork and potentially hitting limits on the number of conventional loans.",
            "A blanket loan can fit investors with several stabilized properties that will be held together for a similar period, who want to consolidate administration, pull equity efficiently or qualify on portfolio-level cash flow. It works best with a clear release clause, a fixed period that matches your hold, and properties whose combined coverage ratio has meaningful cushion under a downside case. Run that case using the <a href=\"/underwriting/downside-scenario/\">downside scenario framework</a> at the portfolio level.",
            "Whichever structure you choose, get written term sheets from more than one lender and compare them side by side, including release terms, prepayment, reserves and reporting. See <a href=\"/financing/conventional-vs-dscr/\">conventional versus DSCR financing</a> for how residential options compare. BNB Accelerator does not lend or arrange loans, and this article is educational rather than lending or legal advice. Confirm terms with qualified lenders and advisers.",
        ]),
    ],
    "faqs": [
        ("What is a blanket loan for rental properties?", "A single loan secured by two or more properties. It consolidates financing into one closing and payment, and qualification often looks at combined portfolio cash flow."),
        ("Can I sell one property under a blanket loan?", "Usually only through a partial release clause, which typically requires paying down a set percentage of that property's allocated balance and keeping the remaining properties above a minimum coverage ratio."),
        ("Are blanket loan rates higher than individual mortgages?", "They are often priced as portfolio or commercial loans, which may mean shorter fixed periods, balloons and prepayment penalties. Compare total cost across your hold period rather than rate alone."),
        ("When do individual mortgages make more sense?", "When you want flexibility to sell or refinance properties independently, own properties in different markets, or can secure long fixed-rate terms."),
    ],
    "related": [
        '<a href="/financing/dscr-loans/">DSCR loans</a>',
        '<a href="/financing/conventional-vs-dscr/">Conventional versus DSCR financing</a>',
        '<a href="/blog/reading-a-dscr-term-sheet/">Reading a DSCR term sheet</a>',
        '<a href="/blog/str-portfolio-diversification/">STR portfolio diversification</a>',
    ],
    "cta_h": "Grow a portfolio on terms you control",
    "cta_p": "We help investors pick the next STR and think through how it fits their existing properties and financing.",
})

POSTS.append({
    "slug": "str-revenue-guarantee-offers",
    "title": "Should You Accept a Guaranteed Rent Offer for Your Short-Term Rental?",
    "title_tag": "Guaranteed Rent and Master Lease Offers for STRs | BNB Accelerator",
    "h1": "Should you accept a guaranteed rent offer for your short-term rental?",
    "description": "How to evaluate guaranteed rent, master lease and revenue floor offers from STR operators: compare against managed returns, check operator credit, insurance, wear and exit terms.",
    "date": DATE,
    "category": "Management",
    "lead": "Some operators offer owners a fixed monthly payment in exchange for the right to run the property as a short-term rental. The pitch is attractive: no seasonality, no guest issues, predictable income. These arrangements go by several names, including guaranteed rent, master lease, corporate lease and revenue floor management. They can make sense in the right situation, but the guarantee is only as reliable as the operator behind it, and the price of certainty is usually a meaningful share of the property's upside. Here is how to evaluate an offer.",
    "sections": [
        ("Understand which structure you are being offered", [
            "A master lease or guaranteed rent agreement is typically a lease. The operator pays you a fixed rent and keeps whatever it earns above that after its costs. You become a landlord to a business tenant rather than an STR owner. A revenue floor is different: the manager runs the property under a management agreement and promises that your payout will not fall below a set amount, usually in exchange for a higher fee or a larger share of revenue above the floor.",
            "The difference matters for who holds the platform listing, who carries operating risk, how insurance should be structured and what happens at the end. Read the document to see whether it is a lease, a management agreement, or a hybrid, and do not rely on the marketing summary.",
        ]),
        ("Compare the guarantee to a realistic managed outcome", [
            "The core question is how much expected income you give up for certainty. Estimate what the property would net under conventional management using supportable revenue from comparable listings, then subtract management, cleaning, supplies, utilities, repairs and a capital reserve. The <a href=\"/revenue-projections/\">revenue projections framework</a> and <a href=\"/underwriting/expense-ratio/\">expense ratio guide</a> help build that estimate.",
            "Then compare that expected net to the guaranteed payment after the costs you still carry under the offer. In a master lease you may still pay the mortgage, property tax, insurance and major repairs, while the operator pays utilities and furnishing upkeep. If the guarantee is 20 to 30 percent below your expected managed net, you are paying a large premium for predictability. That can still be rational if your priority is stable cash flow, but it should be a deliberate choice.",
            ("table", ["Question", "Why it matters"], [
                ["Who pays utilities, supplies, furnishing replacement?", "Shifts real cost between you and the operator"],
                ["Who pays for repairs and at what threshold?", "Heavy turnover increases wear on systems"],
                ["Is the rent fixed or does it escalate?", "Fixed rent loses value over a multi-year term"],
                ["Is the guarantee backed by a deposit or parent company?", "Determines what you can recover if the operator fails"],
                ["What are the exit and early termination terms?", "Controls whether you can sell or change strategy"],
            ]),
        ]),
        ("Evaluate the operator, not the promise", [
            "A guarantee from a thinly capitalized operator is weak protection. If the operator runs into trouble, owners often discover that the guarantee sits with a small entity with few assets. Ask how many properties the operator runs, how long it has been operating, whether it has ever missed payments, and whether a parent company or principal will guarantee the lease. Request references from owners who have been with the operator for several years, including through a slow season.",
            "Ask for a security deposit of at least one to two months of rent, held in a way you can access. Look for regular reporting even under a lease, so you can see how the property is being run and how it is wearing. An operator that refuses any visibility into operations deserves extra caution.",
        ]),
        ("Check legality, lender consent and insurance", [
            "Many local rules require the property owner, or in some cases a local resident, to hold the short-term rental permit. Subleasing to an operator can conflict with those rules, with HOA covenants or with your mortgage terms. Confirm that the arrangement is permitted by local ordinance, HOA documents and your lender. The <a href=\"/underwriting/permit-transfer/\">permit transfer guide</a> and <a href=\"/underwriting/hoa-restrictions/\">HOA restrictions guide</a> cover what to look for.",
            "Insurance needs to reflect the structure. The operator should carry commercial liability insurance naming you as additional insured, and your property policy must allow the use. A standard landlord policy may not cover a commercial short-term rental operation run by a tenant. Get written confirmation from your insurer before signing.",
            ("callout", "Weighing a guaranteed rent offer against managing the property yourself or with a manager? <a href=\"/apply/\">Book a BNB Accelerator call</a> and we will model both outcomes for your specific property and market."),
        ]),
        ("Protect the asset and your exit", [
            "Heavy guest turnover wears floors, furniture, appliances and mechanical systems faster than a residential lease. The agreement should specify the condition the property must be returned in, who replaces furnishings and when, inspection rights during the term, and how damage beyond normal wear is handled. Document condition with photos and an inventory at the start.",
            "Also think about your own plans. A multi-year lease can complicate a sale, since buyers may not want to inherit it, and it can limit a refinance if a lender views the operator lease unfavorably. Negotiate an early termination right on sale with reasonable notice, or keep the initial term short with renewal options. The <a href=\"/blog/str-exit-strategy/\">STR exit strategy guide</a> covers how different operating structures affect sale value.",
        ]),
        ("When a guarantee makes sense", [
            "Guaranteed rent can fit owners who value predictable income above upside, who are far from the property and do not want operational involvement, or who are testing STR use on a property they plan to keep long term. It can also fit a property in a market where you lack confidence in local management options.",
            "It fits poorly when the guarantee sits far below realistic managed net income, when the operator is new or unbacked, when local rules or the HOA restrict the arrangement, or when you expect to sell within a few years. Compare the offer against <a href=\"/blog/cohosting-vs-self-managing/\">co-hosting and self-management</a> options before deciding. This article is educational only and not legal or investment advice; have an attorney review any lease or management agreement.",
        ]),
    ],
    "faqs": [
        ("What is a guaranteed rent agreement for a short-term rental?", "An arrangement where an operator pays the owner a fixed monthly amount, usually under a lease, and runs the property as a short-term rental, keeping any income above its costs and the rent."),
        ("Is guaranteed rent better than hiring a property manager?", "It offers predictability but typically yields less than realistic managed net income. Compare the two using supportable revenue and full costs before deciding."),
        ("What protections should an owner ask for?", "A security deposit, a parent or personal guarantee, regular reporting, clear repair and furnishing responsibilities, insurance naming the owner, and an early termination right on sale."),
        ("Can local rules prevent a master lease arrangement?", "Yes. Some jurisdictions require the owner or a resident to hold the permit, and HOA covenants or mortgage terms may restrict subleasing. Confirm all three before signing."),
    ],
    "related": [
        '<a href="/blog/cohosting-vs-self-managing/">Co-hosting versus self-managing</a>',
        '<a href="/underwriting/permit-transfer/">STR permit transfer</a>',
        '<a href="/revenue-projections/">Revenue projections</a>',
        '<a href="/blog/str-exit-strategy/">STR exit strategy</a>',
    ],
    "cta_h": "Put a price on certainty",
    "cta_p": "We model managed versus guaranteed outcomes so owners can choose the operating structure that fits their goals.",
})

EXTRA = {
    "str-owner-statement-review": ("Common patterns worth a closer look", [
        "A few patterns show up again and again in owner statements. The first is a gradual rise in per-stay costs, such as supplies or laundry, with no change in the property or guest count. Small increases compound over a year and often reflect vendor price changes no one challenged. The second is a cluster of repair charges shortly before or after a contract renewal, which may be legitimate deferred work but deserves invoices and photos.",
        "The third is revenue that trails comparable listings for several consecutive months while the statement shows no change in pricing strategy. That usually means the pricing tool settings, minimum stay rules or listing content need attention. The fourth is a reserve balance that keeps getting drawn down for small items that should be routine operating costs. Spotting these patterns early lets you have a specific, constructive conversation with your manager rather than a frustrated one at year end. Keep notes on each item you raise and how it was resolved, so you can see whether the same issues recur and judge the manager on responsiveness as well as results.",
    ]),
    "str-management-agreement-termination": ("Other clauses that interact with termination", [
        "Several clauses outside the termination section affect how an exit plays out. Indemnification language determines who is responsible for guest injuries, damage claims or platform penalties that surface after the relationship ends. Make sure obligations are mutual and survive termination for a reasonable period. Reserve and deposit provisions should state that any owner funds held by the manager are returned with the final accounting, less documented charges.",
        "Exclusivity clauses matter too. Some agreements give the manager exclusive rights to rent the property, which can block you from listing it yourself or through another channel during a notice period. Insurance requirements should state that the manager carries its own liability and professional coverage and names you as additional insured while it operates the property. Finally, look for dispute resolution terms such as mandatory arbitration or a specific venue. None of these are unusual, but reading them together with the termination section gives a complete picture of what leaving will actually involve.",
    ]),
    "blanket-loan-vs-individual-mortgages-str": ("Questions to ask a blanket lender", [
        "Before committing to a blanket loan, ask each lender a consistent set of questions and get the answers in writing. How is each property's allocated loan amount set, and what paydown percentage is required to release it? Does the remaining portfolio need to meet a minimum debt coverage ratio or loan-to-value after a release? Can a property be substituted with another of similar value, and at what cost?",
        "Ask how the lender will measure short-term rental income at underwriting and during the loan, what reporting is required each year, and whether there are covenants that could trigger a default if coverage falls. Confirm the fixed-rate period, what happens at the end of it, the prepayment penalty schedule, and whether there is a balloon. Ask about reserve requirements and whether they are held per property or for the whole loan. Finally, ask whether the lender allows properties to be held in an LLC and whether a personal guarantee is required. Comparing these answers across two or three lenders usually reveals large differences in flexibility that the rate quote alone would never show.",
        "It also helps to model a specific future event, such as selling the weakest property in year three, and ask each lender to walk through exactly what that would cost. The answer often decides the structure.",
    ]),
    "str-revenue-guarantee-offers": ("Running the numbers on a sample offer", [
        "Consider an illustrative property where realistic managed operations would produce about $90,000 in annual gross revenue. After platform fees, management, cleaning, supplies, utilities, repairs and a capital reserve, the owner might expect around $45,000 of net operating income before the mortgage, property tax and insurance. An operator offers a fixed $3,000 per month, or $36,000 per year, and agrees to cover utilities, supplies and furnishing upkeep, while the owner still pays the mortgage, property tax, insurance and major repairs.",
        "In this example the owner gives up roughly $9,000 a year of expected income, about 20 percent, in exchange for a predictable payment and no operational involvement. Whether that is worthwhile depends on how confident the owner is in the $45,000 estimate, how volatile the market is, how much the owner values time, and how strong the operator's guarantee is. These figures are hypothetical and meant only to show the comparison method. Use your own supportable revenue and cost estimates, and run a downside case on the managed scenario to see how often the guarantee would actually have come out ahead.",
    ]),
}

for _p in POSTS:
    if _p["slug"] in EXTRA:
        _p["sections"] = list(_p["sections"][:-1]) + [EXTRA[_p["slug"]], _p["sections"][-1]]


if __name__ == "__main__":
    blog.build(POSTS)
