#!/usr/bin/env python3
"""Sources checked 2026-10-02; purchase-ready funding decision.

Query: Can I use a securities-backed line of credit for an STR down payment?
Gate before writing: distinct 25, buyer relevance 29, evidence 13,
acquisition service fit 19, original decision support 9 = 95/100.
Primary search evidence: Schwab PAL FAQ explicitly covers home purchases;
Fannie Mae addresses asset-secured down payments; FINRA explains SBLOC risk.
No GSC connector/export, search volumes, rankings or conversion claims.
Distinct from HELOC, reserves and interest-only property loans: collateral
outside the property can require rapid repayment while cash is in the STR.
Rejected lender-brand swaps and generic portfolio borrowing education.
"""
import blog

POSTS = [{
    "slug": "securities-backed-str-down-payment",
    "title": "Securities-Backed Credit for an STR Down Payment",
    "title_tag": "Securities-Backed STR Down Payment | BNB Accelerator",
    "h1": "Can you use securities-backed credit for an STR down payment?",
    "description": "Buying an STR with a securities-backed down payment? Check lender acceptance, collateral calls and cash through launch before making an offer.",
    "date": "2026-10-02",
    "category": "Financing",
    "lead": "You may be able to fund an STR down payment with a securities-backed line of credit, but approval for the credit line is not approval for the property purchase. Your property lender must accept and document the borrowed funds, and your own cash plan must survive a collateral call after the money is tied up in the house. Before making an offer, compare borrowing against investments with using unencumbered cash, selling investments after tax review, or buying a less expensive STR. The decisive question is not whether your portfolio can support the draw today. It is whether you can close, launch, carry both debts and respond to a repayment demand without an emergency property sale.",
    "sections": [
        ("Get two approvals before using portfolio credit to buy an STR", [
            ("callout", 'Planning an STR purchase with a borrowed down payment? <a href="/apply/">Book a call</a> with BNB Accelerator to match your property budget and cash through launch to a funding plan your lenders can approve.'),
            'A securities-backed line of credit, or SBLOC, borrows against eligible investments rather than the STR itself. <a href="https://www.schwab.com/pledged-asset-line/faqs" rel="noopener">Schwab Bank\'s Pledged Asset Line FAQ</a> lists home purchases among permitted uses and distinguishes eligible non-retirement collateral from excluded assets. That establishes a possible funding route, not that a specific investment-property mortgage will accept it. Obtain the credit-line agreement and ask the provider to confirm the intended STR use, borrower or entity, collateral eligibility, draw availability and transfer process.',
            'Then show the property lender the source, balance and repayment terms before your offer becomes difficult to exit. <a href="https://selling-guide.fanniemae.com/sel/b3-4.3-15/borrowed-funds-secured-asset" rel="noopener">Fannie Mae\'s asset-secured borrowing guidance</a> permits this type of funding for down payments under its rules, requires documentation and addresses debt and reserve treatment. It is not a blanket rule for DSCR or private loans. Ask your actual lender whether its STR product accepts this source, how it treats the payment and pledged assets, and what transfer evidence it requires. Do not hide the borrowing or describe the proceeds as savings.',
            'Keep the two approvals separate: the portfolio lender authorizes the draw; the property lender authorizes the acquisition financing. Neither verifies the property\'s legal STR use or the seller\'s revenue. Complete those purchase checks independently. If either financing answer is provisional, keep appropriate contract protection and have your agent or attorney confirm the deadlines. Sources were checked October 2, 2026; eligibility and terms must be confirmed for your transaction.',
        ]),
        ("Separate cash to close from cash that must remain available", [
            'Build a funding ledger before choosing the purchase price. Record earnest money and when it is credited, down payment, closing charges, immediate repairs, furnishing, permit and launch costs, and retained operating reserves. Next to each item, show the exact funding account, amount, date and restrictions. A credit limit is not money already cleared for closing, and a pledged portfolio is not a separate pile of free cash.',
            ('table', ['Cash requirement', 'Buyer verification before committing'], [
                ['Down payment and closing', 'Property lender accepts the borrowing; draw and transfer can settle before the deadline'],
                ['Furnishing and opening work', 'Funds remain after closing; actual bids and payment dates fit the ledger'],
                ['Property operating buffer', 'Cash is retained for debt, bills and a slower launch, not spent on acquisition'],
                ['Collateral-call response', 'A separate repayment source is available within the credit contract\'s deadline'],
            ]),
            'Illustrative only: a $500,000 purchase with a $375,000 property mortgage requires $125,000 toward the price. Suppose closing costs are $15,000, setup is $35,000 and retained property reserves are $25,000. Total funding needed is $200,000, not just the down payment. If you borrow $125,000 against investments and contribute $75,000 cash, only $25,000 of that cash remains as the designated property buffer after the assumed closing and setup spending. No additional cash for a portfolio repayment demand has been identified. These assumptions are not lender quotes, actual deal costs or a minimum reserve recommendation.',
            'Use <a href="/tools/first-str-purchase-budget/">the first-STR purchase budget</a> to map the property funding gap, then add a separate portfolio-credit stress worksheet. Do not count the same dollar as furniture money, property reserves and collateral-call cash. Ask your property lender how it values encumbered assets: the Fannie Mae guidance requires a reduction when the same financial asset is also used as reserves. Even if a particular program allows a reserve figure, your practical ability to spend that money can be different.',
        ]),
        ("Stress the collateral and the STR at the same time", [
            '<a href="https://www.finra.org/investors/insights/securities-backed-lines-credit" rel="noopener">FINRA\'s SBLOC explanation</a> warns that declining collateral, eligibility changes or tighter collateral requirements can create a repayment or collateral demand. It also identifies demand-loan and interest-rate risk. Schwab\'s FAQ states that its bank can demand repayment or additional collateral and describes account restrictions. Read your agreement rather than assuming the line will behave like a fixed-term property mortgage. The risk relevant to this purchase is needing liquid funds while the borrowed money is already in a house.',
            'For a simplified hypothetical stress test, start with $300,000 of eligible investments and assume the credit agreement assigns them a 50% lending value. That produces $150,000 of lending value against a $125,000 draw. A 25% portfolio decline reduces market value to $225,000. With the assumed 50% factor unchanged, lending value becomes $112,500, leaving a $12,500 shortfall. If the factor instead falls to 40%, lending value is $90,000 and the shortfall is $35,000. These factors and declines are illustrative, not published provider advance rates or predictions. Actual securities can have different factors and eligibility rules.',
            'Ask the portfolio lender to calculate the required cure using your actual holdings and agreement. Repaying a shortfall with outside cash is different from pledging more securities: additional collateral must itself receive enough lending value. Do not assume adding $12,500 of securities fixes a $12,500 lending-value deficiency. Also test a full repayment demand, not just the partial shortfalls illustrated above. A portfolio test cannot establish that the lender will leave the loan outstanding.',
            'Now pair the cash demand with a weaker STR launch. As a separate hypothetical, $125,000 of credit-line debt at 8% annual interest costs about $833.33 monthly before fees, using annual interest divided by twelve. At 10%, it costs about $1,041.67. If the property leaves $900 monthly after operating costs, replacement reserves and its own mortgage, the first assumption leaves only $66.67 after portfolio interest; the second creates a $141.67 deficit. Neither repays the portfolio principal. Actual interest may accrue daily. Include this debt in the owner cash model even if a property lender\'s qualification calculation treats it differently.',
            'Run the collateral shock alongside delayed opening, softer collected revenue and unexpected setup spending. Property resale or an unapproved refinance is not cash available to meet a short deadline. Identify what can actually be transferred, by whom and when, without using the STR\'s operating buffer. Review the <a href="/underwriting/downside-scenario/">property downside scenario</a> and your investment exposure with qualified advisers; BNB Accelerator does not select portfolio collateral or provide securities advice.',
        ]),
        ("Choose a purchase price that survives the funding plan", [
            'Compare three acquisition plans for the same candidate: borrow against investments, sell enough investments to fund the purchase, or reduce the purchase and launch budget. Have your tax adviser estimate any consequences of a sale and your financial adviser assess portfolio exposure. Do not treat avoiding an immediate sale as eliminating tax risk or financing cost. Then compare total debt, monthly cash, retained unrestricted liquidity and the documented repayment source. A smaller STR purchase can be the better next step if it preserves a workable response to both risks.',
            ('table', ['Finding', 'Purchase decision'], [
                ['Both lenders approve the source; property downside and separate repayment liquidity are supportable', 'Proceed only within the reviewed funding and offer limits'],
                ['The property works, but the down-payment draw consumes collateral headroom and emergency liquidity', 'Reduce the price or borrowing; compare a smaller property or different source'],
                ['Approval, asset treatment, transfer timing or repayment rights remain unresolved', 'Delay commitment until written answers and contract deadlines align'],
                ['The only cure is a quick STR sale, future appreciation or an unapproved refinance', 'Reject that funding plan before buying'],
            ]),
            'Your pre-offer memo should name the maximum draw, lender-approved source, cash remaining after setup, stressed portfolio lending value, partial and full repayment responses, total monthly debt and a dated funding sequence. Include who monitors collateral and who can authorize transfers. If you cannot complete the memo without relying on projected bookings to meet an immediate cash demand, change the financing or candidate property. An accepted offer does not make the funding gap disappear.',
            '<a href="/apply/">Book a call</a> with BNB Accelerator to screen STR purchase candidates against your cash and financing constraints. We help buyers find, underwrite, negotiate, close and launch properties; your lenders and qualified tax, legal and financial advisers determine their own approvals and advice. This guide is educational, not lending, securities, tax, legal or investment advice. Loan availability, STR permission, revenue, refinancing, resale and returns are not guaranteed.',
        ]),
    ],
    "faqs": [
        ('Can a securities-backed loan fund an STR down payment?', 'It may be possible, but both the credit provider and property lender must approve the intended use and documentation. Do not assume rules for one conventional program apply to a DSCR or private loan.'),
        ('Is the pledged portfolio still available as my STR reserve?', 'It is encumbered. Ask the property lender how it values the assets, and distinguish its qualification rules from cash you can actually access. Keep launch reserves and a collateral-call response from competing for the same funds.'),
        ('What happens if investments fall after I buy the STR?', 'Your credit agreement can require repayment or additional collateral. Calculate the response under your actual holdings and terms before buying; a property sale or future refinance may not be available within the deadline.'),
        ('Does a securities-backed down payment improve STR cash flow?', 'Not automatically. Add portfolio-credit interest and any repayment plan to cash flow after the property mortgage and expenses. Stress higher rates and a slower launch before setting an offer.'),
    ],
    "related": [
        '<a href="/underwriting/cash-needed-to-buy/">Calculate cash needed through the STR launch</a>',
        '<a href="/blog/str-lender-reserve-requirements/">Separate lender reserves from your own liquidity</a>',
        '<a href="/blog/heloc-vs-cash-out-refi-for-str/">Compare home-equity funding alternatives</a>',
    ],
    "cta_h": "Match your STR purchase to a workable funding plan",
    "cta_p": "Screen property price, launch costs and retained cash before committing borrowed portfolio funds.",
}]

if __name__ == "__main__":
    blog.build(POSTS)
