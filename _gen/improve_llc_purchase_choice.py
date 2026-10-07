"""Source corrections and distinct pre-offer LLC choice tree; preserve useful sections."""
import html,json,math,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SLUG='llc-for-short-term-rental'
TITLE='Should You Buy a Short-Term Rental in an LLC?'
DESC='Before buying an STR in an LLC, separate tax assumptions from legal protection, confirm permitted financing and test whether a later title transfer is acceptable.'
FAQ={
'Does an LLC help with short-term rental taxes?':'An LLC alone does not create an income-tax deduction. A single-member LLC without a corporate election is generally disregarded for federal income tax. Activity classification, participation and loss limits still need CPA review. Cost segregation is not a prerequisite for the passive-activity classification or participation tests, and no usable deduction is guaranteed.',
'Can I get a conventional mortgage in an LLC?':'Ask about the specific product. Fannie Mae generally requires natural-person borrowers, with listed exceptions; this is not a rule for every mortgage. If LLC ownership at closing is essential, obtain written confirmation of eligible vesting, owners, signers and guarantees before committing to the purchase.',
'What happens if I transfer my property to an LLC after closing?':'Do not assume every transfer accelerates the loan or that every LLC transfer is permitted. Fannie Mae publishes a conditional LLC transfer exemption for eligible loans; other loan terms and applicable law may differ. Have counsel and the servicer confirm the requirements before recording a deed, including occupancy and future refinance consequences.',
'Do I need an LLC or just insurance for my Airbnb?':'They address different risks. An LLC may provide limited protection under applicable law, while insurance responds only within its coverage terms. Neither automatically removes personal guarantees or protects every claim. Before buying, have counsel and a licensed insurance adviser review the proposed ownership and actual STR use.'}
TREE='''<h2 id="choice">Choose the purchase path before making an offer</h2>
<p>Write down the reason you want an LLC first. Then follow the branch that matches your proposed transaction. This is a decision aid, not a legal conclusion or a recommendation to choose a particular loan.</p>
<ol><li><strong>Your only reason is a hoped-for tax deduction.</strong> Do not form an entity on that assumption. Ask the CPA to evaluate the property activity and your participation separately, then have counsel evaluate ownership. Underwrite the acquisition without a refund paying for the down payment or launch.</li>
<li><strong>LLC ownership at closing is important for an adviser-reviewed legal or ownership reason.</strong> Obtain an eligible entity loan proposal and compare it with the available individual proposal. Check actual cash to close, payments, reserves, prepayment terms and guarantees, not the loan label. Proceed only when the chosen structure and full purchase budget are workable.</li>
<li><strong>You prefer an individual loan but intend to transfer title later.</strong> Treat the later transfer as unresolved until counsel and the servicer identify the applicable requirements. If you would not own the property personally for the holding period, a hoped-for transfer cannot justify proceeding. Resolve the structure or choose another purchase path before your protection expires.</li></ol>
<p>Hypothetical decision example: a buyer has an individual loan proposal for a candidate STR and wants an LLC because of significant other assets. The entity-lending alternative has not been approved, and the individual loan's later-transfer treatment is not confirmed. A CPA's statement that a disregarded LLC can preserve federal income-tax reporting does not resolve either condition. The buyer should not treat entity ownership as already secured. An offer can proceed only if the buyer accepts the counsel-reviewed individual ownership path or obtains the needed entity approvals with a viable budget; otherwise seek a valid extension or reject the transaction. No assumed rate, liability outcome or tax saving makes the missing approval disappear.</p>
<p>Use four outcomes: <strong>proceed</strong> with a documented acceptable ownership and funding path; <strong>renegotiate</strong> the price, loan or purchase scale if actual costs break the budget; <strong>delay</strong> within valid contractual protection while a named adviser resolves a specific condition; <strong>reject</strong> when the purchase requires an unacceptable ownership risk, inaccurate occupancy representation or unapproved transfer. The <a href="/blog/str-entity-structure-basics/">entity purchase approval guide</a> covers implementation once you have selected a path; the <a href="/blog/personal-guarantee-llc-str-purchase-loan/">personal-guarantee guide</a> addresses individual debt exposure separately.</p>
<p><a href="/apply/">Book a call to compare an LLC-ready STR purchase with your approved financing and deployable cash</a>. Bring the actual lender proposal and unresolved ownership questions, not private account numbers.</p>'''

def main():
 p=ROOT/'blog'/SLUG/'index.html';s=p.read_text()
 s=s.replace('Should You Put a Short-Term Rental in an LLC?',TITLE)
 s=re.sub(r'<p class="lead">.*?</p>','<p class="lead">Before buying a short-term rental, decide whether an LLC addresses a real legal or ownership need and whether your financing permits that purchase path. Forming an LLC does not itself create tax savings, eliminate personal loan exposure or make a later title transfer acceptable. Use the decision tree below before your first offer.</p><p><a href="/apply/">Book a call to screen STR purchases against your financing and ownership requirements</a>.</p>',s,count=1,flags=re.S)
 start=s.index('        <p>A single member LLC');end=s.index('        <h2 id="liability">',start)
 s=s[:start]+'''        <p>The <a href="https://www.irs.gov/businesses/small-businesses-self-employed/single-member-limited-liability-companies" rel="noopener">IRS single-member LLC guidance</a> says a single-member LLC without a corporate election is generally disregarded for federal income tax. This is not identical treatment for every tax: employment and certain excise taxes have separate rules, and state treatment needs review. The entity label alone does not establish a new income-tax deduction.</p>
        <p><a href="https://www.irs.gov/publications/p925" rel="noopener">IRS Publication 925</a> treats an average customer use of seven days or less as one exception to rental-activity classification for passive-activity purposes. Material participation and other loss limits still matter. Cost segregation is not a prerequisite for that exception or the participation tests; depreciation analysis is a separate question. None of these facts automatically makes a loss usable against wages. Ask the CPA to assess your actual activity, ownership and records before relying on a tax benefit in the purchase plan. See the <a href="/blog/str-tax-benefit-shortfall-purchase/">smaller or unavailable tax-benefit purchase test</a>.</p>

'''+s[end:]
 start=s.index('        <p>Here is the practical constraint');end=s.index('        <div class="inline-cta">',start)
 s=s[:start]+'''        <p><a href="https://selling-guide.fanniemae.com/sel/b2-2-01/general-borrower-eligibility-requirements" rel="noopener">Fannie Mae's borrower guidance</a> generally requires natural persons and lists specific exceptions. It is not a universal rule for all conventional or investment loans. Ask the lender to confirm eligibility for the exact proposed title holder and intended rental use before selecting financing.</p>
        <p>A later deed transfer is not an automatic workaround. <a href="https://servicing-guide.fanniemae.com/svc/d1-4.1-02/allowable-exemptions-due-type-transfer" rel="noopener">Fannie Mae's servicing guide</a> includes an LLC transfer exemption for loans it purchased or securitized on or after June 1, 2016, when the original borrower controls the LLC or owns a majority interest and any permitted occupancy change complies with the security instrument. It also requires notice about transferring back to a natural person for a qualifying Fannie Mae refinance. Other loans and applicable law differ. Have counsel and the servicer confirm the actual requirements before recording a transfer; do not infer approval or debt release from a general exemption.</p>
        <p>If buying directly through an LLC matters, ask prospective <a href="/blog/dscr-loans-for-airbnb/">DSCR</a> or other investment lenders whether their particular product permits it. Compare written terms through the <a href="/blog/how-to-finance-airbnb-investment-property/">purchase financing guide</a>. Neither an entity-friendly label nor a personal guarantee tells you whether the property is a good purchase.</p>

'''+s[end:]
 s=s.replace('Some states charge meaningful annual fees per entity, which multiplies across a portfolio.','Obtain the actual formation, registered-agent, recurring filing and tax costs for the proposed entity; do not borrow another state\'s estimate.')
 s=s.replace('An entity formed in one state and operating in another typically must register in the state where the property is located, which adds cost and filings.','Ask local counsel whether the proposed out-of-state entity must register for this activity and what filings and costs apply.')
 s=s.replace('A multi member LLC is generally treated as a partnership by default, which changes the filing obligations and can complicate the participation analysis for each member.','The IRS generally treats a domestic LLC with two or more members as a partnership unless it elects corporate treatment. Have the CPA review the actual owners, including any spouse-specific treatment, before buying jointly.')
 s=s.replace('Named insureds should match title. A policy naming you personally on a property titled to an entity is a problem you find out about during a claim.','Have a licensed adviser confirm the correct insured parties, ownership, intended rental use, exclusions and limits in the actual policy before closing or changing title. Do not assume an umbrella covers STR use or that every naming difference automatically defeats a claim.')
 start=s.index('        <p>For a first property purchased');end=s.index('        <div class="callout">',start)
 s=s[:start]+TREE.replace('<h2 id="choice">Choose the purchase path before making an offer</h2>','')+'\n\n'+s[end:]
 s=s.replace('<h2 id="answer">The practical answer</h2>','<h2 id="answer">Choose the purchase path before making an offer</h2>')
 s=s.replace('Some jurisdictions impose transfer tax on a transfer to an entity, even a wholly owned one.','Ask local counsel and the closing team whether a proposed deed transfer creates taxes, recording fees, title-policy changes or new permission requirements; obtain written estimates and any applicable exemption analysis.').replace('<strong>Transfer taxes.</strong>','<strong>Transfer costs.</strong>')
 for q,a in FAQ.items():
  pattern=r'(<h3>'+re.escape(q)+r'</h3>\s*<div class="faq-answer"><p>).*?(</p>)'
  s,n=re.subn(pattern,lambda m:m.group(1)+a+m.group(2),s,count=1,flags=re.S);assert n==1
 note='<p class="small">Primary sources reviewed October 6, 2026. Educational information, not legal, tax, insurance, lending or personalized investment advice. The example is hypothetical. Obtain independent professional advice and written transaction-specific terms; no financing, deduction, liability protection or investment result is guaranteed.</p>'
 s=s.replace('<div class="author-box">',note+'\n<div class="author-box">',1)
 words=len(re.findall(r'\b\w+\b',html.unescape(re.sub('<[^>]+>',' ',re.search(r'<article class="article">(.*?)<div class="author-box">',s,re.S).group(1)))));minutes=math.ceil(words/220)
 for key in ['description','og:description','twitter:description']:
  s=re.sub(r'(<meta (?:name|property)="'+key+r'" content=")[^"]*(")',lambda m:m.group(1)+html.escape(DESC,quote=True)+m.group(2),s)
 s=re.sub(r'(<meta property="article:published_time" content=")[^"]+',r'\g<1>2026-08-10',s)
 s=s.replace('<span>Published August 10, 2026</span>','<span>Published August 10, 2026</span><span>&middot;</span><span>Updated October 6, 2026</span>',1)
 s=re.sub(r'<span>\d+ min read</span>',f'<span>{minutes} min read</span>',s,count=1)
 def schema(m):
  d=json.loads(m.group(2))
  for n in d.get('@graph',[d]):
   if n.get('@type') in ['Article','BlogPosting']:
    assert n['datePublished']=='2026-08-10';n.update(headline=TITLE,description=DESC,dateModified='2026-10-06',wordCount=words)
   if n.get('@type')=='FAQPage':
    assert len(n['mainEntity'])==4
    for item in n['mainEntity']:item['acceptedAnswer']['text']=FAQ[item['name']]
  return m.group(1)+json.dumps(d,indent=2)+m.group(3)
 s=re.sub(r'(<script[^>]*type="application/ld\+json"[^>]*>)(.*?)(</script>)',schema,s,flags=re.S);p.write_text(s)
 archive=ROOT/'blog/index.html';count=0
 def card(m):
  nonlocal count
  c=m.group()
  if '/blog/'+SLUG+'/' not in c:return c
  count+=1;c=c.replace('Should You Put a Short-Term Rental in an LLC?',TITLE)
  c=re.sub(r'<p>.*?</p>','<p>'+DESC+'</p>',c,count=1,flags=re.S)
  c=re.sub(r'data-search="[^"]*"','data-search="'+html.escape((TITLE+' '+DESC+' pre-offer decision tree').lower(),quote=True)+'"',c)
  return re.sub(r'<span>\d+ min read</span>',f'<span>{minutes} min read</span>',c)
 a=re.sub(r'<article class="post-card".*?</article>',card,archive.read_text(),flags=re.S);assert count==1;archive.write_text(a)
 hub=ROOT/'blog/buy-str-high-income-large-tax-bill/index.html';h=hub.read_text();block='<p data-llc-choice-link>Before your first offer, use the <a href="/blog/llc-for-short-term-rental/">LLC purchase-choice decision tree</a> to separate tax assumptions from ownership needs and resolve financing or later-transfer conditions.</p>';assert 'data-llc-choice-link' not in h;hub.write_text(h.replace('<div class="author-box">',block+'\n<div class="author-box">',1))
 for xml in ROOT.glob('sitemap*.xml'):
  t=xml.read_text();n=re.sub(r'(<loc>https://www.bnbaccelerator.com/blog/'+SLUG+r'/</loc>\s*<lastmod>)[^<]+',r'\g<1>2026-10-06',t)
  if n!=t:xml.write_text(n)
 print(f'{words} words; {minutes} min; August10 publication preserved; four FAQs aligned')

if __name__=='__main__':main()
