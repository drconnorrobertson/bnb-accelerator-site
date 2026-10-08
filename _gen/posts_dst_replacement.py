"""Scoped new owner; reuse reviewed registration, never older full generators."""
import re
import posts_reverse_exchange_str as publisher

SLUG = 'dst-vs-direct-str-1031-replacement'
DATE = '2026-10-08'
TITLE = 'DST vs Direct STR: Choose a 1031 Replacement'
DESC = 'Compare a DST interest with a direct STR replacement using an acceptance worksheet and separate exchange, launch and reserve cash before committing.'
POST = {
 'slug':SLUG, 'date':DATE, 'title':TITLE, 'title_tag':TITLE,
 'h1':'DST vs direct STR: which replacement can you actually execute?',
 'description':DESC, 'category':'Acquisition & Financing',
 'lead':'Selling an investment property and considering an STR purchase within six months? A Delaware statutory trust (DST) proposal and a directly purchased rental can lead to different ownership, funding and decision responsibilities. Do not choose solely from a promised tax deferral or advertised distribution. First establish what interest you would acquire, whether your independent professionals accept the exchange, and how you will fund obligations outside the exchange. This guide compares a specifically reviewed trust-interest replacement with acquiring a buyer-selected STR—not generic passive investing, a sponsor ranking or a recommendation to buy securities. <a href="/apply/">Discuss the direct STR acquisition work and purchase timetable</a> while your independent advisers review the alternative.',
 'sections':[
 ('A DST label is not exchange acceptance',[
 'The <a href="https://www.irs.gov/pub/irs-drop/rr-04-86.pdf">IRS Revenue Ruling 2004-86</a> describes a particular investment-trust arrangement with constrained powers. Its conditional result does not qualify every trust-labelled proposal. Have counsel and tax advisers assess the actual trust, classification and transaction; do not substitute a brochure or this article for that review.',
 'The <a href="https://www.govinfo.gov/content/pkg/FR-2020-12-02/html/2020-26313.htm">Treasury/IRS December 2, 2020 final-rule preamble, section IV.C</a> explains that the TCJA does not contradict treating a grantor-trust DST transfer as a transfer of underlying property. That is not a blanket exemption for every beneficial interest. Tax look-through also does not give you the same operational rights as a direct property owner.',
 'For direct STR ownership, the purchase file must establish the actual purchaser, conveyed interest, lawful rental use, supported financing and operating responsibilities. A listing advertised as turnkey does not settle those conditions. A trust proposal needs its own asset and governing-document review; do not assume its holdings are STRs or compare unrelated assets as though they were the same home.',
 'Use the existing <a href="/blog/1031-exchange-short-term-rental/">sell-first exchange guide</a> for the transaction sequence and <a href="/blog/reverse-1031-buy-str-before-selling/">reverse-exchange guide</a> for replacement-first ownership arrangements. The <a href="/blog/str-vs-real-estate-syndications/">direct ownership versus syndication comparison</a> owns the broader delegation and sponsor-risk question. Here the decision is narrower: can the accepted replacement close, with the rights and independently funded readiness you need?',
 ]),
 ('Original replacement acceptance worksheet',[
 'Complete this matrix for one actual proposal on each side. Record a document or clause, named reviewer, answer and commitment deadline. “Not yet answered” is an unresolved gate, not presumed acceptance. Neither a provider introduction nor an adviser appointment means the work has been completed.',
 ('table',['Decision gate','Direct STR purchase','Trust-interest proposal'],[
 ['Accepted interest','Deed/entity and buyer identity reconciled with exchange plan','Exact interest, governing documents and adviser-reviewed classification'],
 ['Closing deliverable','Title, seller performance, loan conditions and purchase completion','Exact subscription/conveyance process, available allocation and completion evidence'],
 ['Funding and fee trigger','Permitted closing sources plus separate service/launch invoices','Accepted exchange funding plus actual fees, obligations and payment terms'],
 ['Control after closing','Who approves repairs, operator contracts, use, debt and sale','Who controls assets, borrowing, fees, disposition and investor requests'],
 ['Missing or failed gate','Valid contract protections and owner of authorized notices','Actual withdrawal, refund, transfer and incomplete-transaction provisions'],
 ['Retained responsibilities','Fund and oversee work not included in written contracts','Reporting, adviser review and obligations under actual governing documents'],
 ]),
 'Ask each professional for acceptance of their own part, not a promise covering everyone else. The acquisition team can coordinate an STR shortlist; the lender accepts financing, local authorities and counsel address use, and the exchange and tax professionals address their respective conditions. For a trust proposal, an independent securities professional and counsel should assess suitability and binding terms. Do not assume BNB Accelerator selects, sells or endorses that interest.',
 'Test a failure before paying: the candidate cannot close under the accepted structure. Which party may stop, which amounts remain committed, what notice is required and what alternative remains valid? A theoretical second option is not a funded or contractually available substitute. Do not invent extension, cancellation or refund rights.',
 ]),
 ('Keep exchange proceeds separate from opening cash',[
 'The current <a href="https://www.irs.gov/publications/p544">IRS Publication 544 (2025 edition)</a> limits qualifying exchanges to appropriate real property and distinguishes incidental-property identification from tax treatment. It describes 45-day identification and receipt by the earlier of 180 days or the applicable return due date with extensions. Intermediary agreements restrict access to held proceeds; some closing-statement items, including repairs, are not exchange expenses. Obtain professional payment instructions and an asset-specific analysis, not a universal all-costs eligibility assumption.',
 'Build two funding schedules: the exchange-controlled pool and unrestricted cash available for expenses and retained reserves. For each invoice show its transaction, payee, deadline, accepted source and remaining commitment. Ask the professionals to reconcile replacement value, debt, basis and any recognized gain separately. This cash exercise does not calculate full deferral, taxes or depreciation.',
 'Hypothetical arithmetic only, not an offering, fee quote, loan approval or client result: Pool E contains $400,000 held under an adviser-reviewed exchange arrangement. Pool U contains $120,000 unrestricted purchase-support cash after separately excluded household and business liquidity. Assume each proposed route has an accepted plan using all of E for stipulated replacement closing obligations. These assumptions illustrate cash separation; they do not establish that either actual transaction qualifies.',
 ('table',['Unrestricted-cash allocation','Invented direct STR plan','Different invented trust-interest plan'],[
 ['Distinct review/transaction work','$12,000','$15,000'],
 ['Furnishings','$28,000','No separate amount stipulated here'],
 ['Net no-revenue carry','$20,000','No separate amount stipulated here'],
 ['Retained reserve or designated buffer','$40,000','$40,000'],
 ['Total allocated from U','$100,000','$55,000'],
 ['Cash outside the stipulated plan','$20,000','$65,000'],
 ]),
 'The direct case is $12,000 + $28,000 + $20,000 + $40,000 = $100,000, leaving $20,000. A distinct $25,000 required repair raises allocation to $125,000: a $5,000 gap preserving the reserve. Do not relabel E as unrestricted funds to fill it, or count the $40,000 as both retained and already available for that repair. Seek an independently approved funding or price change; otherwise the proposed purchase fails the stated cash limit.',
 'The different trust case allocates $15,000 + $40,000 = $55,000, leaving $65,000. A larger illustrative margin does not establish suitability or a better return: the assets, leverage, use and rights have not been aligned. Its designated buffer is not a contractual liability cap. Actual documents may reveal additional obligations that require a rebuilt model; no expense is asserted absent simply because the example does not stipulate it.',
 'No distribution, guest revenue, share sale, refinance, refund or tax benefit is available in either starting pool. A credited closing deposit belongs inside its total obligation, not on top of it; a pending refund from an abandoned transaction is not cash for a replacement. Keep the protected reserve visible and update remaining commitments as payments clear using the <a href="/financing/closing-costs-and-reserves/">closing-cost and reserve guide</a>.',
 ]),
 ('Do not buy an interest just because the clock is running',[
 'If the actual proposal is a private placement, the <a href="https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/private">SEC staff bulletin updated September 21, 2026</a> highlights potential loss, illiquidity and limited disclosure. Form D is not SEC approval. Confirm transfer restrictions and the investment professional’s compensation and conflicts. The bulletin is educational staff guidance, not approval of a sponsor or a guarantee of an exit.',
 'A proposed disposition year is not an enforceable cash-out date; a permitted transfer is not a matched buyer or cleared payment. Direct STR sale and refinancing also depend on actual market, loan and ownership conditions. Compare the control you need with the rights offered, not a universal passive-versus-active slogan. Use independent advisers to assess legal exposure and tax facts; a large tax bill alone does not establish suitability.',
 'Proceed only when classification, completion, actual rights and funded downside fit. Revise an independently supportable price or scope if that resolves a specific gap. Defer within valid protection while decisive documents are missing, or decline a replacement that requires unsupported assumptions. Ask the exchange team about consequences and lawful alternatives if completion fails; this guide does not promise deadline relief or a tax-free fallback.',
 'For direct acquisition support, request BNB Accelerator’s current written deliverables, fee triggers, exclusions and decision authority. Property funding, licensed advice and operating contracts remain separate. <a href="/apply/">Bring a non-sensitive replacement status memo and independently funded STR budget to an acquisition call</a>. Continue through the <a href="/blog/buy-str-high-income-large-tax-bill/">high-income buyer roadmap</a>; keep offering, banking and tax documents in agreed secure channels.',
 'Commercial-interest disclosure: BNB Accelerator publishes this guide and sells acquisition assistance. This is document-based educational analysis, not firsthand sponsor testing, an independent ranking, securities solicitation or personalized investment, legal, tax, exchange, insurance or lending advice. Primary materials reviewed October 8, 2026; historical rule dates and the currently published IRS edition are stated above. All cash inputs are invented. No exchange qualification, tax deferral, distribution, financing, liquidity, permission or investment result is guaranteed.',
 ]),
 ],
 'faqs':[
 ('Does every DST interest qualify as a 1031 replacement?','No blanket qualification is established here. Independent advisers must assess the actual trust classification, governing documents and exchange transaction rather than rely on the DST label.'),
 ('Can exchange proceeds automatically fund STR furniture and repairs?','Do not assume that. Separate exchange-controlled funds from unrestricted readiness cash and obtain asset-specific tax review and accepted payment instructions.'),
 ('Does tax look-through give a DST investor direct property control?','Not by itself. Read governing documents for actual decision rights, obligations, transfer restrictions and disposition authority.'),
 ('Is a larger remaining-cash balance evidence that a DST is better?','No. The illustrative plans acquire different exposure and rights. Evaluate actual suitability, completion, total obligations and risk without a return ranking.'),
 ],
 'related':['<a href="/blog/1031-exchange-short-term-rental/">Review the sell-first exchange sequence</a>','<a href="/blog/str-vs-real-estate-syndications/">Compare broader ownership responsibilities</a>'],
 'cta_h':'Test the direct STR replacement before committing',
 'cta_p':'Connect an actual replacement shortlist with professional acceptance, unrestricted launch cash and clear decision responsibilities.',
}

def main():
    publisher.SLUG=SLUG; publisher.DATE=DATE; publisher.ROUTE=f'/blog/{SLUG}/'
    publisher.TITLE=TITLE; publisher.DESC=DESC; publisher.POST=POST
    publisher.main(expected_articles=746, expected_total_pages=2487,
       hub_attribute='data-dst-replacement-link',
       hub_copy=f'Choosing a replacement ownership path? Compare a <a href="/blog/{SLUG}/">DST interest with a direct STR and separate exchange from launch cash</a>.')
    p=publisher.ROOT/'blog/index.html';s=p.read_text()
    card=re.search(r'<article class="post-card".*?</article>',s,re.S)[0]
    assert f'/blog/{SLUG}/' in card and 'datetime="2026-10-08">Oct 7, 2026' in card
    p.write_text(s.replace(card,card.replace('>Oct 7, 2026</time>','>Oct 8, 2026</time>'),1))

if __name__=='__main__': main()
