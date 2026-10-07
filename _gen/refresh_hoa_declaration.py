"""Scoped existing-guide refresh; primary Arizona sources reviewed October 6, 2026.
Preserves publication, preclosing answers, authorship, homepage and shared design.
"""
import html
import json
import math
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'reading-an-hoa-declaration'
TITLE = 'Read HOA Documents Before Buying an STR | BNB Accelerator'
DESCRIPTION = 'Review HOA declarations before an STR offer: reconcile amendments, rental rules, assessments and document conflicts with a buyer evidence worksheet.'
FAQS = [
    ('Can an HOA stop me from running a short-term rental?', 'Valid association restrictions can affect the proposed use even when public permission exists. Have local counsel review the exact documents, applicable law, buyer and stay length; a city permit does not establish private permission.'),
    ('What HOA documents should I request before buying?', 'Request the declaration and amendments, bylaws, current rules, available minutes, resale disclosures, budget, reserve information, assessments and relevant disputes. Statutory access and delivery requirements vary; track missing documents and actual purchase deadlines with counsel.'),
    ('What is a mandatory rental program?', 'It is a program the applicable documents may require an owner to join. Review successor obligations, operating control, charges and lender requirements before buying. Refer any tax-participation question to your CPA; the program label alone does not establish a tax result.'),
]
BODY = '''<p class="lead">Before buying an STR in an association, establish which documents apply to the exact property and whether their valid restrictions fit your proposed ownership and guest stays. A seller's listing, operating history or city permit is not a substitute for that review. Affluent buyers still need a documented answer before they pay for a nightly-rental income thesis. This guide helps you assemble the packet, reconcile conflicting versions and turn unresolved restrictions or charges into a purchase decision.</p>
<p><a href="/apply/">Bring the association document packet to an STR acquisition call</a> before your actual offer or review deadline. Legal interpretation belongs with qualified local counsel, not a sales summary.</p>
<h2>Public permission and private restrictions are separate questions</h2>
<p>Verify public STR permission through the <a href="/blog/parcel-jurisdiction-str/">parcel-authority worksheet</a>. Separately ask counsel which recorded covenants, amendments, bylaws and rules bind the buyer, whether they are valid and how they apply to the intended stay length. Neither review replaces the other. Do not assume every board rule is enforceable, that the strictest wording automatically resolves a conflict, or that a statewide rule eliminates private-document review.</p>
<p>For a narrowly scoped example, <a href="https://www.azleg.gov/ars/33/01806-01.htm" rel="noopener">Arizona's planned-community rental statute, §33-1806.01</a>, addresses declaration prohibitions and rental-time restrictions while also limiting certain association information requests and charges. That is not nationwide permission or a determination for a particular home. Community type, applicable law and the actual documents matter. Use authorized channels and appropriate privacy limits when requesting records; do not collect guest credit or personal records simply because they exist.</p>
<h2>Assemble a complete, dated HOA document packet</h2>
<p>Request the declaration with recorded amendments, bylaws, current rules and rental policies, applicable plats or exhibits, the resale disclosure package and property-specific compliance information. Ask whether a master association or another association also governs the parcel. Obtain available recent minutes, proposed amendments, budget, reserve information, approved or proposed assessments and relevant litigation disclosures. A request for two years of available minutes is a diligence preference, not a universal statutory entitlement.</p>
<p>As one state-specific example, <a href="https://www.azleg.gov/ars/33/01806.htm" rel="noopener">Arizona §33-1806</a> lists planned-community resale records including governing documents, recent approved board minutes, assessment and violation information, budget, reserve-study information if any, and specified lawsuit disclosures. It has applicability limits and exceptions. The section also allows good-faith reliance on association records without independent validation. A delivered packet therefore still needs review; do not apply its deadlines or record rights to every state or condominium.</p>
<p>Save the issuer, receipt date, document date, recording reference where available and any missing attachment. Ask counsel and the closing/title professionals how to obtain the controlling recorded materials. A management-company compilation can help, but a missing amendment or an unresolved version conflict is an unanswered purchase question. Do not mistake a document count for verified rental eligibility.</p>
<div class="table-scroll"><table><thead><tr><th>Review item</th><th>Evidence to reconcile</th><th>Buyer decision record</th></tr></thead><tbody>
<tr><td>Property and governing associations</td><td>Legal description, recorded declaration, exhibits and resale package</td><td>Exact unit/parcel and every applicable association; unresolved coverage goes to counsel</td></tr>
<tr><td>Rental use and duration</td><td>Declaration, amendments, current policies and proposed stay pattern</td><td>Relevant clause/version, reviewer and written interpretation; distinguish nightly stays from a different lawful use</td></tr>
<tr><td>Change and approval procedures</td><td>Amendment provisions, meeting records and pending proposals</td><td>What is effective now, what is proposed and what rights attach to this buyer; no assumed grandfathering</td></tr>
<tr><td>Money and compliance</td><td>Dues schedule, assessment notices, reserves and subject-property disclosures</td><td>Amount, actual due date, responsible payer and disputed or unpriced exposure</td></tr>
<tr><td>Purchase deadline</td><td>Signed contract, delivery record and adviser response</td><td>Named owner of each unanswered question and deadline before relevant protection changes</td></tr>
</tbody></table></div>
<p>A restriction allowing rentals does not establish a buyer's slot under a rental cap. Use the separate <a href="/blog/hoa-rental-cap-before-buying-str/">rental-cap and transfer guide</a> for allocation, waiting lists and buyer-specific approval. This worksheet identifies documents and conflicts; it does not forecast a waitlist or create permission.</p>
<h2>Worked example: reconcile evidence before pricing nightly income</h2>
<p>Hypothetical document conflict, not a client result or legal opinion: a listing says “weekly rentals allowed.” The seller supplies a declaration dated several years earlier, an amendment with a thirty-day minimum and a manager email saying the seller has an exception. The buyer plans three- to five-night stays. The email does not establish whether the amendment is valid, the exception's scope or whether it applies after this purchase.</p>
<p>The review register should identify the exact clause and recording reference, obtain the exception's underlying terms and ask counsel for the buyer-specific interpretation. Ask the authorized association representative to identify the documents behind its statement. An oral assurance or a promise to explain it after closing is not the missing evidence. If the restriction validly requires thirty-day stays for this buyer, the nightly-stay model fails; a longer-stay purchase would need independently verified permission, financing and economics.</p>
<p>Suppose the signed purchase contract has a review deadline on day12 and the unresolved document is expected on day15. Those invented dates illustrate a conflict, not a standard review period. Have counsel identify available contract protection and whether a timely agreed extension is possible. Do not presume the buyer may cancel, recover a deposit or extend unilaterally. If the decisive answer cannot arrive while acceptable protection remains, choose a protected delay or reject the nightly-rental thesis instead of treating a stronger revenue projection as evidence.</p>
<h2>Translate disclosed charges into cash timing, without guessing liability</h2>
<p>Separate recurring dues from special assessments, possible future work and property-specific arrears. Review the reserve information, inspection reports where relevant and actual assessment notices; an underfunded reserve is a question about future funding, not proof of an inevitable bill of a known size. Ask advisers what further evidence and downside allowance are appropriate. Track proposed assessments separately from approved obligations.</p>
<p>Illustrative accounting only: monthly dues of $450 represent $5,400 annually. A separately identified $12,000 assessment has three $4,000 installments. Assume counsel and the closing agent have confirmed for this hypothetical that the seller pays the first installment and the buyer owes the remaining two after closing. The buyer plans $8,000 of future cash outflows on their actual dates, not the entire $12,000 and not another $8,000 already included elsewhere. These numbers and payer allocations are invented, not statutory rules or market averages.</p>
<p>If the purchase model already includes the $5,400 dues in operating expenses, do not deduct it again. If $8,000 is ring-fenced for the installments, it remains cash until paid but is not free for furniture or another acquisition. A requested seller credit is neither agreed nor necessarily unrestricted cash; ask the lender and closing agent about permitted treatment. An unpriced dispute or proposed repair should remain visibly unresolved, rather than becoming a fabricated assessment forecast. Use the <a href="/underwriting/cash-needed-to-buy/">full acquisition cash framework</a> for the combined budget.</p>
<h2>Check operating obligations and future change exposure</h2>
<p>Read rental-program and management obligations separately. Ask who controls bookings, rates, owner stays and fees, and which agreements bind a successor. Link the actual documents to lender and insurer review. Use the <a href="/blog/mandatory-rental-pool-before-buying-str-condo/">mandatory rental-pool purchase guide</a> to review owner distributions and project financing. Ask your CPA to review any tax-participation implications using your actual work and facts. A program name or degree of pricing control alone does not establish a usable deduction.</p>
<p>For amendments, have counsel review adoption requirements, pending proposals and any claimed protection for existing uses or buyers. Do not predict a vote from owner-occupancy percentages or assume the seller's exception survives transfer. Where wording is silent or ambiguous, identify the interpretive question and qualified reviewer instead of declaring permission or prohibition from a general court-case summary.</p>
<h2>Make an evidence-backed purchase decision</h2>
<p>Proceed only when reviewed documents support the planned use, buyer-specific approvals and public permission are established, and costs fit the verified financing and cash plan. Renegotiate when a documented charge or operating limitation changes a still-viable offer. Delay only with valid protection while a specific decisive answer is pending. Reject an STR-priced purchase if valid restrictions defeat the intended use or critical documents remain unresolved beyond acceptable risk.</p>
<p><a href="/apply/">Compare this association-governed STR with other acquisition candidates through BNB Accelerator</a>. Bring the document register, written adviser findings, actual deadlines and reconciled cost schedule. Substantial deployable capital or a large tax bill does not repair a missing rental right. BNB Accelerator assists within its contracted acquisition scope; independent professionals determine their respective legal, tax, lending and insurance conclusions.</p>
<p class="small">Primary sources reviewed October 6, 2026. Educational information only, not legal, tax, insurance, lending or personalized investment advice. Examples are hypothetical. No association approval, financing, booking, tax benefit or investment result is guaranteed.</p>
<h2 id="faq">Frequently asked questions</h2>
'''

def main():
    path = ROOT / 'blog' / SLUG / 'index.html'
    s = path.read_text()
    original = s
    h1 = re.search(r'<h1>(.*?)</h1>', s).group(1)
    published = re.search(r'"datePublished":\s*"([^"]+)"', s).group(1)
    assert published == '2026-08-15'
    preclosing = re.search(r'<!-- preclosing-keywords:start -->.*?<!-- preclosing-keywords:end -->', s, re.S).group()
    author = re.search(r'<div class="author-box">.*?</div>\s*</div>', s, re.S).group()
    faqs = ''.join('<div class="faq-group"><h3>'+html.escape(q)+'</h3><div class="faq-answer"><p>'+html.escape(a)+'</p></div></div>\n' for q,a in FAQS)
    body = BODY + faqs + preclosing
    s = re.sub(r'(<article class="article">).*?</article>', lambda m: m.group(1)+'\n'+body+'\n'+author+'\n</article>', s, count=1, flags=re.S)
    s = re.sub(r'<title>.*?</title>', '<title>'+TITLE+'</title>', s, count=1)
    for name,value in [('description',DESCRIPTION),('og:description',DESCRIPTION),('twitter:description',DESCRIPTION),('og:title',TITLE),('twitter:title',TITLE)]:
        s = re.sub(r'(<meta (?:name|property)="'+name+r'" content=")[^"]*(")', lambda m:m.group(1)+html.escape(value,quote=True)+m.group(2),s)
    faq_count = 0
    def schema(m):
        data = json.loads(m.group(2))
        def walk(n):
            nonlocal faq_count
            if isinstance(n,dict):
                if n.get('@type') in ('Article','BlogPosting'):
                    n.update(description=DESCRIPTION,dateModified='2026-10-06')
                if n.get('@type')=='FAQPage':
                    faq_count += 1
                    n['mainEntity']=[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in FAQS]
                for v in n.values(): walk(v)
            elif isinstance(n,list):
                for v in n: walk(v)
        walk(data)
        return m.group(1)+json.dumps(data,indent=2)+m.group(3)
    s = re.sub(r'(<script[^>]*type="application/ld\+json"[^>]*>)(.*?)(</script>)',schema,s,flags=re.S)
    assert faq_count==1
    words = len(re.findall(r'\b\w+\b',html.unescape(re.sub('<[^>]+>',' ',body))))
    minutes = math.ceil(words/220)
    s = re.sub(r'<span>\d+ min read</span>',f'<span>{minutes} min read</span>',s,count=1)
    assert re.search(r'"datePublished":\s*"([^"]+)"',s).group(1)==published
    assert preclosing in s and author in s
    path.write_text(s)
    # Preserve the existing five purchase answers in schema and recompute its
    # Article wordCount through the approved single-page normalization module.
    subprocess.run(['node', '--input-type=module', '-e', "import {readFileSync,writeFileSync} from 'node:fs'; import {expandPreclosingKeywords} from './preclosing_keywords.mjs'; const p='blog/reading-an-hoa-declaration/index.html'; writeFileSync(p,expandPreclosingKeywords(readFileSync(p,'utf8'),p));"], cwd=ROOT, check=True)
    archive=ROOT/'blog/index.html'; matches=0
    def card(m):
        nonlocal matches
        c=m.group()
        if '/blog/'+SLUG+'/' not in c: return c
        matches+=1
        c=re.sub(r'<p>.*?</p>','<p>'+DESCRIPTION+'</p>',c,count=1,flags=re.S)
        c=re.sub(r'data-search="[^"]*"','data-search="'+html.escape((html.unescape(h1)+' '+DESCRIPTION+' document conflict amendment assessment evidence buyer').lower(),quote=True)+'"',c)
        return re.sub(r'<span>\d+ min read</span>',f'<span>{minutes} min read</span>',c)
    a=re.sub(r'<article class="post-card".*?</article>',card,archive.read_text(),flags=re.S)
    assert matches==1
    archive.write_text(a)
    hub=ROOT/'blog/buy-str-high-income-large-tax-bill/index.html'; h=hub.read_text()
    block='<p data-hoa-document-review-link>Reviewing an association-governed shortlist? Use the <a href="/blog/reading-an-hoa-declaration/">HOA document register and evidence-conflict example</a> to reconcile amendments, buyer restrictions and disclosed charges before committing to the purchase.</p>'
    h=re.sub(r'<p data-hoa-document-review-link>.*?</p>','',h,flags=re.S)
    h=h.replace('<div class="author-box">',block+'\n<div class="author-box">',1)
    hub.write_text(h)
    print(f'HOA refresh: {words} words; {minutes} minutes; original publication {published}; three FAQs aligned')

if __name__=='__main__':
    main()
