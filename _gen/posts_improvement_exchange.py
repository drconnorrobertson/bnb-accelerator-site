"""One reviewed purchase intent; reuse scoped registration, not older generators."""
import re
import posts_reverse_exchange_str as publisher

SLUG='improvement-1031-vs-completed-str-purchase'
DATE='2026-10-08'
TITLE='Improvement 1031 vs a Completed STR Purchase'
DESC='Compare an improvement exchange, a completed STR and later renovation using receipt evidence, three separate dates and an unfinished-work cash worksheet.'
POST={
 'slug':SLUG,'date':DATE,'title':TITLE,'title_tag':TITLE,
 'h1':'Improvement exchange or completed STR: what can you receive?',
 'description':DESC,'category':'Acquisition & Financing',
 'lead':'An unfinished rental can look attractive when you are replacing an investment property, but an improvement 1031 exchange is not simply buying a home and spending the remaining proceeds on repairs. For an STR purchase in the next six months, compare the property you can actually receive with a completed alternative and an ordinary purchase followed by separately funded work. Construction delivery, exchange receipt and lawful rental opening are different milestones. A large expected gain does not make an unfinished property executable. This guide supplies a receipt-evidence register and an original cash comparison—not a transaction structure, tax calculation or recommendation to proceed. <a href="/apply/">Discuss the STR acquisition shortlist and delivery constraints</a> while independent exchange, legal, tax and lending professionals assess their own requirements.',
 'sections':[
 ('Identify the replacement, not just a renovation budget',[
 'Current <a href="https://www.ecfr.gov/current/title-26/section-1.1031%28k%29-1">26 CFR 1.1031(k)-1(e)</a> addresses replacement property being produced. Identification includes the land description and practicable improvement detail; substantial changes matter. Its incomplete-real-property test concerns the property actually received. Work produced after taxpayer receipt is not additional like-kind property received in that exchange. Contractor deposits and progress invoices alone do not establish received real-property value. Have advisers assess the actual interest, identified scope and receipt evidence before committing.',
 'The current <a href="https://www.irs.gov/publications/p544">IRS Publication 544, 2025 edition</a> describes deferred exchanges with 45-day identification and receipt by the earlier of 180 days or the applicable return due date, including extensions. Ask your exchange team to provide the actual dates and requirements. Do not assume construction delay extends this timetable. Deadline relief discussed for condemnation or other involuntary conversions is not an automatic extension for this voluntary exchange.',
 'Use the <a href="/blog/1031-exchange-short-term-rental/">sell-first exchange guide</a> for the general sequence and the <a href="/blog/reverse-1031-buy-str-before-selling/">reverse-exchange guide</a> for replacement-first ownership and early cash. Here the distinct decision is whether the accepted replacement can be delivered with sufficiently supported scope before receipt, and whether unfinished work remains affordable afterward.',
 'Keep asset classification separate: <a href="https://www.ecfr.gov/current/title-26/section-1.1031%28a%29-3">26 CFR 1.1031(a)-3</a> addresses real property, including distinct assets and structural components. Its classification is not a determination of depreciation or recapture treatment. Neither a cost-segregation label nor a materials invoice makes every proposed expenditure qualifying replacement property. Use qualified professionals for an asset-specific conclusion; this guide calculates no deferred gain or basis.',
 ]),
 ('Approve ownership and responsibility before purchase',[
 'A professionally accepted holding arrangement may be necessary; do not take ownership personally and assume a provider can reconstruct the transaction later. The <a href="https://www.irs.gov/pub/irs-irbs/irb00-40.pdf">full Revenue Procedure 2000-37 in IRB 2000-40, pages 308–310</a>, together with <a href="https://www.irs.gov/pub/irs-drop/rp-04-51.pdf">Revenue Procedure 2004-51</a>, describes a limited accommodation safe harbor. The modification excludes replacement property owned by the taxpayer within the specified preceding 180-day period. The safe harbor does not itself establish that every replacement qualifies.',
 'Ask counsel and exchange professionals to reconcile the titleholder, buyer, lender, guarantees, payment authority and conveyance sequence. Safe-harbor conditions include written agreements and timed identification/transfers; this article is not an implementation checklist. Permission to supervise improvements under a tax arrangement does not approve a building permit, insurance policy, loan or guest stay. No outside-safe-harbor workaround is proposed here.',
 'BNB Accelerator is an interested acquisition-service publisher, not automatically your qualified intermediary, exchange accommodation titleholder, general contractor, lender or tax adviser. Request its current written deliverables, fee triggers, exclusions and decision authority. A property-search introduction is not completed engineering, accepted exchange treatment or a contractor commitment. Keep sensitive account and tax records in agreed secure channels.',
 ]),
 ('Original receipt-evidence register: keep three dates separate',[
 'Complete this register for the actual property, with a named reviewer, document, unresolved answer and decision deadline in every row. A percentage-complete statement is not an accepted receipt valuation. Reconcile what is built, what is conveyed and what remains payable; do not substitute a seller photograph or deposit receipt for professional evidence.',
 ('table',['Gate','Evidence to reconcile','Buyer decision'],[
 ['Identified replacement','Legal description, identified improvement scope and accepted changes','Can the actual delivery still match the reviewed identification?'],
 ['Ownership and funding','Accepted title/borrower/holding documents and permitted payees','Can the purchase and work occur under the approved arrangement?'],
 ['Built versus unbuilt at receipt','Dated inspection, installed scope, conveyance and adviser-reviewed valuation','What property is actually received, rather than merely ordered?'],
 ['Remaining obligations','Contract scope, paid-to-date reconciliation, balance, liens and handoff','Who owes each unfinished item after receipt?'],
 ['Lawful STR readiness','Address-specific use, inspections, insurance, possession and operator acceptance','What separately blocks the first guest?'],
 ['Failure authority','Actual notices, contract protections and authorized decision-maker','What can stop, change or end the purchase before a decisive date?'],
 ]),
 'Record three independent dates: the professional exchange receipt deadline, actual conveyance/receipt and first lawful guest readiness. A contractor target is none of these by itself. The title team documents the interest conveyed; advisers assess exchange receipt; authorities, insurers and the operator address their respective opening conditions. One sign-off does not replace another.',
 'Invented timing example, not a deadline computation: suppose your professionals identify day 150 as the applicable receipt deadline. Delivery is targeted for day 130, transfer for day 140 and lawful rental readiness for day 175. A 20-day delivery slip moves the proposed transfer to day 160 if the same sequence holds. That proposed transfer misses the stipulated day-150 limit. Earlier receipt with incomplete work needs its own professional review; neither an invoice nor an automatic extension cures the gap. Later opening alone does not decide exchange qualification.',
 'Before offering, ask what happens if this sequence fails while a contract commitment remains. Do not assume termination rights, a returned deposit or a second replacement is available. Compare a completed candidate before your valid decision window closes. The <a href="/blog/new-construction-vs-existing-str-purchase/">new-construction versus existing-property guide</a> addresses broader delivery risk; the <a href="/blog/str-repair-vs-improvement-records/">repair and improvement records guide</a> addresses the separate expense evidence.',
 ]),
 ('Worked comparison: separately fund unfinished work',[
 'Hypothetical inputs only, not a provider fee quote, appraisal, loan approval or client result. Assume independent professionals accept each stipulated purchase structure. Restricted Pool E contains $400,000 earmarked for its accepted replacement closing obligations; unrestricted Pool U contains $150,000 after household and business liquidity are excluded. Assume all E is allocated under each respective plan. This assumption illustrates separation, not full deferral or equivalent property value. No exchange funds, tax refund, refinancing or guest income are added to U.',
 ('table',['Allocation from unrestricted U','Improved replacement route','Completed STR route','Ordinary purchase + later work'],[
 ['Distinct review/setup costs','$20,000','$10,000','$10,000'],
 ['Required post-receipt work','$45,000','$10,000','$65,000'],
 ['Furnishings','$25,000','$25,000','$25,000'],
 ['Net no-revenue carry','$15,000','$10,000','$20,000'],
 ['Retained reserve','$35,000','$35,000','$35,000'],
 ['Total allocation','$140,000','$90,000','$155,000'],
 ['Outside-plan margin or gap','$10,000 margin','$60,000 margin','$5,000 gap'],
 ]),
 'The first column is $20,000 + $45,000 + $25,000 + $15,000 + $35,000 = $140,000. An additional distinct $18,000 of unfinished work raises it to $158,000: an $8,000 gap preserving the reserve. The $45,000 already includes its stipulated credited deposits; do not add them again. No remaining restricted proceeds are assumed available to solve the gap. Obtain accepted payment instructions and independently available financing or revise the purchase.',
 'The completed route allocates $90,000, leaving $60,000; the ordinary later-work route allocates $155,000, already exceeding U by $5,000. These are deliberately different illustrative scopes, not evidence that completed homes are always cheaper or that an exchange saves $65,000. Compare actual purchase prices, financing, installed condition and supported income before selecting a candidate. The ordinary-purchase route assumes no improvement-exchange treatment for work performed after receipt; advisers must separately assess its purchase and tax consequences.',
 'Carry is the stipulated net cash outflow, not lost gross booking revenue plus the same bills a second time. The reserve stays retained; it is neither an expense nor extra outside-plan cash. Replace invented amounts with actual remaining commitments and payment dates. The <a href="/financing/closing-costs-and-reserves/">closing-cost and reserve worksheet</a> and <a href="/blog/dst-vs-direct-str-1031-replacement/">replacement ownership comparison</a> help reconcile funding without converting restricted proceeds into operating cash.',
 ]),
 ('Choose an executable property, not a hoped-for tax outcome',[
 'Proceed only when the actual structure, identified/received scope, financing, property diligence and independently funded unfinished work meet your limits. Revise an executable price, scope or delivery term through authorized professionals when that resolves a specific gap. Defer under valid protection while decisive evidence is missing. Decline a candidate that relies on unsupported timing, classification or inaccessible funds. Ask advisers about failed-completion consequences; no tax-free fallback is promised.',
 '<a href="/apply/">Bring an STR acquisition call a non-sensitive receipt-status memo and funded readiness budget</a>. Ask the acquisition team to compare a completed candidate against the unfinished property on realistic ownership merits, not promised deductions. Follow the <a href="/blog/buy-str-high-income-large-tax-bill/">high-income buyer roadmap</a> for the broader purchase journey. Source review: October 8, 2026; eCFR title 26 current as of October 6, IRS publication is the 2025 edition, and historical procedure dates are not new rules. This is document-based education, not firsthand transaction testing or personalized legal, tax, exchange, construction, insurance, lending or investment advice. All examples are invented. No qualification, deferral, refund, financing, rental permission or investment outcome is guaranteed.',
 ]),
 ],
 'faqs':[
 ('Can buying an STR and renovating afterward make the work exchange replacement property?','Do not assume that. The produced-property regulation distinguishes actual receipt from production afterward. Obtain professional review before ownership and fund remaining obligations independently.'),
 ('Do contractor invoices prove the value received in an improvement exchange?','Not by themselves. Reconcile installed real-property scope, actual conveyance and qualified professional valuation and classification; ordered or paid work is not automatically received property.'),
 ('Does a construction delay automatically extend the exchange deadline?','No automatic extension is established here. Have exchange professionals determine the applicable deadline and lawful options rather than assume a contractor delay provides relief.'),
 ('Is exchange receipt the same as permission to accept STR guests?','No. Actual receipt, the professional exchange deadline and lawful rental readiness are separate milestones with different evidence and decision owners.'),
 ],
 'related':['<a href="/blog/1031-exchange-short-term-rental/">Review the sell-first sequence</a>','<a href="/blog/new-construction-vs-existing-str-purchase/">Compare broader construction delivery risk</a>'],
 'cta_h':'Compare a deliverable STR before committing',
 'cta_p':'Connect the accepted purchase structure with actual delivery evidence, independently funded unfinished work and rental-readiness gates.',
}

def main():
    publisher.SLUG=SLUG;publisher.DATE=DATE;publisher.ROUTE=f'/blog/{SLUG}/'
    publisher.TITLE=TITLE;publisher.DESC=DESC;publisher.POST=POST
    publisher.main(expected_articles=747,expected_total_pages=2488,
      hub_attribute='data-improvement-exchange-link',
      hub_copy=f'Considering unfinished replacement property? Compare an <a href="/blog/{SLUG}/">improvement exchange with a completed STR and separately funded later work</a>.')
    p=publisher.ROOT/'blog/index.html';s=p.read_text()
    card=re.search(r'<article class="post-card".*?</article>',s,re.S)[0]
    assert f'/blog/{SLUG}/' in card
    p.write_text(s.replace(card,card.replace('>Oct 7, 2026</time>','>Oct 8, 2026</time>'),1))

if __name__=='__main__':main()
