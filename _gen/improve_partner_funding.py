"""Targeted funding addition to existing partnership guide; retain useful body/FAQ."""
import html,json,math,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SLUG='str-partnership-structure'
DESC='Buying an STR with a partner? Test cash timing, launch reserves, lender signatures and capital-call terms before making a joint offer.'
ADDITION='''<h2 id="funding">Test each partner's purchase cash before making an offer</h2>
<p>Prepare one dated funding schedule for the property and a separate schedule for each buyer. Record amounts available now, amounts dependent on a sale or transfer, household/business liquidity excluded from the acquisition, approved contribution type and the date funds must arrive. Do not count an unfunded promise as closing cash or assume every source is lender-eligible. Confirm the required bank records and transfers through a secure channel; never publish account numbers.</p>
<p>Hypothetical example only, not a current loan quote, client transaction or required budget. Two unrelated partners propose equal ownership of a $600,000 STR with an assumed approved $450,000 loan. The budget contains $150,000 toward the purchase, $15,000 of separate cash-paid closing charges, $30,000 setup, $10,000 launch funding and $25,000 retained reserves. Total committed capital is $230,000. For this example, all funding must be evidenced before closing and retained funds are not restricted by the lender; actual requirements may differ.</p>
<div class="table-scroll"><table><thead><tr><th>Hypothetical funding test</th><th>Partner A</th><th>Partner B</th></tr></thead><tbody>
<tr><td>Agreed equal contribution</td><td>$115,000</td><td>$115,000</td></tr>
<tr><td>Available by the funding deadline</td><td>$140,000</td><td>$95,000</td></tr>
<tr><td>Later hoped-for receipt, not yet available</td><td>$0</td><td>$20,000</td></tr>
<tr><td>Unallocated cash after agreed contribution</td><td>$25,000</td><td>$20,000 shortfall</td></tr>
</tbody></table></div>
<p>Combined timely cash is $235,000, more than the property budget, but the agreed contributions still fail for B. A could supply an additional $20,000 only if willing, the source/structure is lender-approved and the documents address its treatment. A would then fund $135,000, B $95,000, and only $5,000 of their designated cash would remain outside the $230,000 property plan. The later receipt cannot fund today's requirement. Do not quietly relabel the imbalance a gift, loan or equity change.</p>
<p>Now assume a $24,000 setup overrun before opening. If the partners agree to preserve the $25,000 property reserve and neither has new funds, their remaining $5,000 outside the plan leaves a $19,000 funding gap. The reserve is not an incurred expense, but spending it changes the downside protection and may violate actual lender requirements. Reforecast costs and postpone distributions rather than counting it simultaneously as retained reserve and spendable setup money. A future bonus, tax refund or refinance remains conditional.</p>
<h2 id="approval">Align contribution terms with lender and signer approval</h2>
<p><a href="https://visiolending.com/lending-process/" rel="noopener">Visio Lending's published process</a> provides one current provider example: entity documentation identifies ownership and signing authority; its process requires personal guarantees from entity owners and may require spouse consent. Its purchase-contract requirements also address matching buyer vesting and authority. These are provider-specific statements, not universal rules or approval for your partnership. Ask your lender to review the actual ownership, source of funds and intended STR use before committing.</p>
<p>Give counsel and the lender a contribution-and-authority sheet: who funds each deadline, who may sign the offer, which people sign loan documents and which decisions need consent. Read the <a href="/blog/personal-guarantee-llc-str-purchase-loan/">separate guarantee review</a> for individual loan exposure. Equal ownership or an internal reimbursement promise does not itself establish equal lender exposure or release a guarantor. This guide's funding worksheet is not a guarantee valuation or contract clause.</p>
<ul><li>For uneven initial funding, ask advisers to document whether the excess is additional equity or permitted member debt, how it is repaid, and how distributions or ownership are affected.</li>
<li>For later capital calls, agree on notice, permitted purpose, approval threshold, each person's maximum willing commitment and the response if somebody cannot fund. Have counsel evaluate enforceability and alternatives; dilution or forced sale is not an automatic remedy.</li>
<li>For an exit, identify the valuation method, payment timing, available buyout funding and any required lender consent or release. A partner leaving the ownership agreement does not automatically leave the debt.</li></ul>
<p>Proceed when each promised contribution is available on time, approved signers accept their obligations and the property works without projected tax savings. Renegotiate the price, acquisition scale or documented contribution arrangement if the plan breaches a buyer's limit. Delay only with valid transaction protection while a specific funding or approval condition is unresolved. Reject a purchase requiring hidden member debt, an unwilling signer or reserves neither partner can replenish. <a href="/apply/">Book a call to compare your joint STR purchase budget with a smaller acquisition or a solo alternative</a>.</p>
'''
FAQ_ANSWER='Not automatically. Each buyer needs an adviser-reviewed tax analysis; ownership percentage alone does not establish usable losses. Material participation, activity classification and other loss limits matter, and spouse-participation rules can differ from those for unrelated partners. A fifty-fifty ownership split does not guarantee a fifty-fifty tax outcome.'

def main():
    p=ROOT/'blog'/SLUG/'index.html';s=p.read_text()
    s=re.sub(r'<p class="lead">.*?</p>','<p class="lead">Buying an STR with a partner can share acquisition funding and work, but it does not automatically halve your cash commitment or loan exposure. Before making a joint offer, agree on timely contributions, retained reserves, signing authority and what happens when one buyer cannot supply more capital. Use the funding worksheet below alongside the existing ownership, operating and exit checklist.</p><p><a href="/apply/">Book a call to screen STR purchases against both partners\' documented funding limits</a>.</p>',s,count=1,flags=re.S)
    s=s.replace('<h2 id="tax">Start with the tax question, because it is not intuitive</h2>','<h2 id="tax">Confirm the tax assumptions separately from purchase funding</h2>')
    s=s.replace('<p>A multi member arrangement is generally treated as a partnership for federal tax purposes by default, which changes the filing obligations and, importantly, the participation analysis.</p>','<p>The <a href="https://www.irs.gov/businesses/small-businesses-self-employed/limited-liability-company-llc" rel="noopener">IRS LLC classification guidance</a> describes a domestic LLC with at least two members as a partnership for federal income tax by default unless it elects corporate treatment. Ask your CPA about the actual owners, elections and any applicable spouse-specific treatment; a business label alone does not settle filing obligations.</p>')
    s=s.replace('<p>If both partners intend to use losses against ordinary income, both need a participation path, and that has to be designed rather than assumed. See','<p><a href="https://www.irs.gov/publications/p925" rel="noopener">IRS Publication 925</a> explains passive-activity, at-risk and participation rules, including spouse participation. For unrelated partners, do not credit one person\'s operating work automatically to the other. Participation alone does not guarantee usable losses: activity classification and other limits need individual CPA review. See')
    assert '<h2 id="document">' in s;s=s.replace('<h2 id="document">',ADDITION+'\n<h2 id="document">',1)
    s=s.replace('This is the single most common source of friction.','Peak-week conflicts should be resolved before buying.')
    s=s.replace('Solve it upfront with a management fee to the working partner, paid before distributions.','Agree on workload and any separately documented compensation before buying; have counsel and the CPA review its treatment and effect on distributions.')
    s=s.replace('Rotate it in writing, in advance, permanently.','Agree in writing on a rotation or another allocation, including how it can be changed.')
    q='Can two people share the short-term rental tax benefit?'
    s=re.sub(r'(<h3>'+re.escape(q)+r'</h3>\s*<div class="faq-answer"><p>).*?(</p>)',lambda m:m.group(1)+FAQ_ANSWER+m.group(2),s,count=1,flags=re.S)
    note='<p class="small">Primary sources reviewed October 6, 2026. Educational information, not legal, tax, lending or personalized investment advice. Examples are hypothetical. Obtain independent advice and actual written terms; no financing, tax benefit, partner reimbursement or investment result is guaranteed.</p>'
    s=s.replace('<div class="author-box">',note+'\n<div class="author-box">',1)
    body=re.search(r'<article class="article">(.*?)<div class="author-box">',s,re.S).group(1)
    words=len(re.findall(r'\b\w+\b',html.unescape(re.sub('<[^>]+>',' ',body))));minutes=math.ceil(words/220)
    for key in ['description','og:description','twitter:description']:
        s=re.sub(r'(<meta (?:name|property)="'+key+r'" content=")[^"]*(")',lambda m:m.group(1)+html.escape(DESC,quote=True)+m.group(2),s)
    s=re.sub(r'(<meta property="article:published_time" content=")[^"]+',r'\g<1>2026-08-11',s)
    s=s.replace('<span>Published August 11, 2026</span>','<span>Published August 11, 2026</span><span>&middot;</span><span>Updated October 6, 2026</span>',1)
    s=re.sub(r'<span>\d+ min read</span>',f'<span>{minutes} min read</span>',s,count=1)
    def schema(m):
        d=json.loads(m.group(2))
        for n in d.get('@graph',[d]):
            if n.get('@type') in ['Article','BlogPosting']:
                assert n['datePublished']=='2026-08-11';n.update(description=DESC,dateModified='2026-10-06',wordCount=words)
            if n.get('@type')=='FAQPage':
                for item in n['mainEntity']:
                    if item['name']==q:item['acceptedAnswer']['text']=FAQ_ANSWER
        return m.group(1)+json.dumps(d,indent=2)+m.group(3)
    s=re.sub(r'(<script[^>]*type="application/ld\+json"[^>]*>)(.*?)(</script>)',schema,s,flags=re.S);p.write_text(s)
    archive=ROOT/'blog/index.html';count=0
    def card(m):
        nonlocal count
        c=m.group()
        if '/blog/'+SLUG+'/' not in c:return c
        count+=1;c=re.sub(r'<p>.*?</p>','<p>'+DESC+'</p>',c,count=1,flags=re.S)
        c=re.sub(r'data-search="[^"]*"','data-search="'+html.escape(('Buying a Short-Term Rental With a Partner '+DESC+' contribution deadlines capital calls').lower(),quote=True)+'"',c)
        return re.sub(r'<span>\d+ min read</span>',f'<span>{minutes} min read</span>',c)
    a=re.sub(r'<article class="post-card".*?</article>',card,archive.read_text(),flags=re.S);assert count==1;archive.write_text(a)
    hub=ROOT/'blog/buy-str-high-income-large-tax-bill/index.html';h=hub.read_text();block='<p data-partner-funding-link>Buying jointly? Test <a href="/blog/str-partnership-structure/">each partner\'s cash deadline and capital-call capacity</a> before sharing an STR offer; combined wealth alone does not prove the agreed funding will arrive.</p>';assert 'data-partner-funding-link' not in h;hub.write_text(h.replace('<div class="author-box">',block+'\n<div class="author-box">',1))
    for xml in ROOT.glob('sitemap*.xml'):
        t=xml.read_text();n=re.sub(r'(<loc>https://www.bnbaccelerator.com/blog/'+SLUG+r'/</loc>\s*<lastmod>)[^<]+',r'\g<1>2026-10-06',t)
        if n!=t:xml.write_text(n)
    print(f'{words} words; {minutes} min; August11 publication preserved')

if __name__=='__main__':main()
