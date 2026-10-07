"""Improve existing service-selection owner; preserve purchase checks and original FAQs."""
import json,re,subprocess
from pathlib import Path
from refresh_dscr_purchase_methods import refresh
ROOT=Path(__file__).resolve().parents[1]
SLUG='str-buyer-agent-vs-acquisition-team'
ADDITION='''<h2>Original two-agreement test: one property, two scopes</h2>
<p>Before hiring both a brokerage and a separate acquisition service, put their actual proposed agreements beside the same candidate address. This is an original review method, not a representation that either provider uses the clauses below. Ask the broker and appropriate counsel to identify inconsistent commitments; a coordinator's verbal assurance does not amend the brokerage agreement.</p>
<div class="table-wrap"><table><thead><tr><th>Review field</th><th>Record separately for each agreement</th><th>Decision before signing</th></tr></thead><tbody>
<tr><td>Covered purchase</td><td>Named buyer/entity, territory, property type and covered addresses</td><td>Identify overlap when the buyer brings the listing or switches markets</td></tr>
<tr><td>Delivered work</td><td>Search, analysis, representation, deadline tracking and launch outputs</td><td>Assign missing tasks and remove unwanted duplicated work</td></tr>
<tr><td>Compensation</td><td>Exact amount/calculation, payer, trigger and written offset</td><td>Do not presume one fee cancels another or the seller pays it</td></tr>
<tr><td>Exit and later purchase</td><td>Term, notice, termination, carryover, earned amounts and candidate records</td><td>Resolve continuing obligations before moving to a replacement provider</td></tr>
<tr><td>Authority and data</td><td>Who may submit, sign, approve costs and retain the analysis</td><td>Keep investment approval separate from delegated professional work</td></tr>
</tbody></table></div>
<p><a href="https://www.nar.realtor/the-facts/written-buyer-agreements-101">NAR's guidance</a> distinguishes its mandatory compensation provisions from optional agreement terms. It says policy does not dictate exclusivity, duration, services or compensation type/amount, and discusses possible termination carryover and retainer treatment. This is not a universal state-law rule or an automatic right to end your contract. Ask for the permitted, negotiated arrangement that fits this purchase.</p>
<h2>Worked decision sequence: a rejected candidate is not a closed engagement</h2>
<p><strong>Invented sequence, not a client story or a claim about BNB's terms:</strong> A buyer rejects the first candidate after an inspector identifies unacceptable conditions. The buyer then finds another property independently and wants a different local agent while keeping the original analyst's research. These are three separate decisions. Rejecting the property does not itself terminate either service agreement, authorize another broker or establish rights to reuse proprietary work.</p>
<p>First, have the retained transaction professional explain valid property-contract notices and deadlines. Second, request written confirmation of each service relationship's status: active scope, authorized termination process, any continuing fee obligation and treatment of a later purchase. Third, obtain permission to retain or use the analysis needed for the replacement decision under the actual terms. Do not invent a fee waiver because the provider did not find the next address or because no closing occurred.</p>
<p>If the brokerage term ends before the replacement offer, ask specifically whether a carryover provision covers that property or prior introduction. If the separate service continues, identify which new analysis or launch work is included and which needs fresh approval. Resolve conflicting promises through the actual parties and counsel before placing a second offer. No example here establishes that any fee is owed, refundable, enforceable or avoidable.</p>
<p>The <a href="/guides/str-service-responsibility-matrix/">responsibility matrix</a> assigns execution; this test isolates agreement overlap and decision rights. Use the <a href="/compare/">comparison hub</a> to investigate existing named alternatives, then obtain their actual scope rather than assuming all acquisition, brokerage and software offers are interchangeable. The <a href="/blog/bnb-accelerator-vs-str-insights-buyer/">STR Insights buyer comparison</a> separately tests service tiers and credited payments; it is not the agreement-overlap answer.</p>'''

def main():
    original=subprocess.check_output(['git','show','HEAD:blog/'+SLUG+'/index.html'],cwd=ROOT,text=True)
    body=re.search(r'<article class="article">(.*?)<h2 id="faq">',original,re.S)[1]
    body=body.replace('<h2>Choose a process that lets you say no</h2>',ADDITION+'\n<h2>Choose a process that lets you say no</h2>',1)
    body+='<p class="small">Primary NAR guidance and BNB published process reviewed October 7, 2026. BNB Accelerator is the commercially interested publisher and acquisition provider. This is document-based educational analysis, not firsthand provider testing or an independent ranking; no actual buyer engagement agreements were inspected. Signed scope and qualified professional advice govern the transaction.</p>'
    nodes=[]
    for block in re.findall(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',original,re.S):
        d=json.loads(block);nodes.extend(d.get('@graph',[d]))
    questions=next(n for n in nodes if n.get('@type')=='FAQPage')['mainEntity']
    faq=[(q['name'],q['acceptedAnswer']['text']) for q in questions if q['name'] not in re.search(r'<!-- preclosing-keywords:start -->.*?<!-- preclosing-keywords:end -->',original,re.S)[0]]
    assert len(faq)==4
    refresh(SLUG,'STR Buyer Agent vs. Acquisition Team | BNB Accelerator','Should an STR buyer use an agent or an acquisition team?',
      'Compare STR buyer-agent and acquisition-team scope before signing. Use a two-agreement test for overlapping fees, termination and purchase decision rights.',
      body,faq,'2026-09-24','data-agent-team-review-link',
      'Use the <a href="/blog/str-buyer-agent-vs-acquisition-team/">agent/team two-agreement review and rejected-candidate decision sequence</a>. Property rejection does not itself end a service relationship.')

if __name__=='__main__':main()
