"""Develop an existing platform-specific purchase owner; do not generate a new variant."""
import json, re, subprocess
from pathlib import Path
from refresh_dscr_purchase_methods import refresh
ROOT=Path(__file__).resolve().parents[1]
SLUG='vrbo-listing-handoff-buying-str'
ADDITION='''<h2>Original transition work sample: prove the seller-held money split</h2>
<p>Ask the seller and proposed operator to complete one transition memo for the actual closing date. Record old/new listing identifiers, affected reservation IDs, guest choices, the Vrbo Support case and documented outcome, the parties' agreed money allocation, and each service provider's due date. Counsel should review authority and obligations; the platform determines its transfer process. Mark a request, an approved outcome and cleared funds as different milestones.</p>
<p>Keep the memo free of unnecessary guest names, payment credentials or other private data. Use authorized secure records to reconcile it. Recheck it if closing moves: a stay previously ending before the sale may now cross possession, and the payout recipient or service schedule may change. Do not ask a buyer to log into the seller's personal account to bypass an unresolved transition.</p>
<p><a href="https://www.vrbo.com/en-gb/tlp/trust-and-safety/property-sale-notice-policy">Vrbo's policy</a> also warns that sale or management-change cancellations may carry host-cancellation consequences and are not eligible for a cancellation waiver. A guest's cancellation choice does not establish a cost-free seller exit. Have the responsible host confirm its actual obligations; do not assign another person's fees to the buyer without a lawful, reviewed agreement.</p>
<h2>Worked payout split: guest charges are not buyer-controlled cash</h2>
<p><strong>Entirely hypothetical, not Vrbo's fees, a client result or a proposed contract:</strong> Assume two reservations have been validly transferred through the applicable process. Their total guest charges are $10,000. Stipulate that $6,000 was already received by the seller and $4,000 remains payable to the buyer later. Suppose the parties' adviser-reviewed reconciliation assigns $5,000 of the seller-held money to the buyer; the remaining $1,000 stays with the seller for separately identified obligations. Actual taxes, fees, refunds and responsible parties require their own evidence—these invented inputs do not describe how Vrbo calculates payouts.</p>
<div class="table-wrap"><table><thead><tr><th>Fictional cash item</th><th>Buyer treatment</th></tr></thead><tbody>
<tr><td>$10,000 total guest charges</td><td>Reconcile the total; do not record it as money already available</td></tr>
<tr><td>$5,000 seller-funded allocation</td><td>Count only when the approved arrangement actually delivers cleared spendable funds</td></tr>
<tr><td>$4,000 future buyer payment</td><td>Place it on its actual receipt date, subject to the supported payment and refund assumptions</td></tr>
<tr><td>$1,000 seller-retained amount</td><td>Do not add it to buyer cash or assert the underlying obligation is discharged</td></tr>
<tr><td>$3,000 distinct near-term service bills</td><td>Pay once; confirm they are not already included in the acquisition model</td></tr>
</tbody></table></div>
<p>For a deliberately simplified timing test, assume $2,000 spendable buyer cash is available outside the separately funded closing, setup and retained-reserve plan. If the $5,000 allocation clears before the $3,000 bills, this cash becomes $7,000, then $4,000 after payment. The later $4,000 receipt brings it to $8,000. Supported buyer receipts are $9,000, not the full $10,000 guest charge; $9,000 minus $3,000 gives $6,000 before all omitted operating costs, financing and taxes. It is not complete investment profit.</p>
<p>If the $5,000 seller allocation is delayed until after those bills, the buyer initially has $2,000 against $3,000 due—a $1,000 funding gap, even though the eventual arithmetic could be unchanged. A settlement price credit, restricted escrow and cleared operating-account transfer are not interchangeable. Ask the closing agent, lender and counsel which arrangement is actually permitted and when it provides usable cash. If the future $4,000 receipt fails, the simplified ending cash is $4,000 rather than $8,000. Reconcile any additional refund duty separately instead of silently counting the same reservation twice.</p>
<p>Replace all figures with the actual ledger and dates. This work sample isolates Vrbo's support-assisted transition and the agreed split of previously paid funds; the <a href="/blog/future-reservations-at-closing/">Airbnb reservation-duty guide</a> covers a different platform's limits. Use the <a href="/tools/first-str-purchase-budget/">purchase-budget worksheet</a> to fund the timing gap independently, not an assumed tax refund or review premium.</p>'''

def main():
    original=subprocess.check_output(['git','show','HEAD:blog/'+SLUG+'/index.html'],cwd=ROOT,text=True)
    body=re.search(r'<article class="article">(.*?)<h2 id="faq">',original,re.S)[1]
    body=body.replace('<h2>Use the handoff status to proceed, renegotiate, delay, or reject</h2>',ADDITION+'\n<h2>Use the handoff status to proceed, renegotiate, delay, or reject</h2>',1)
    disclosure='<p class="small">Primary Vrbo materials reviewed October 7, 2026. BNB Accelerator is the commercially interested publisher and acquisition service provider. This is document-based guidance, not firsthand platform testing, a customer review or a verified transaction outcome. Public policy does not establish approval for your accounts, guest obligations or signed service scope.</p>'
    body+=disclosure
    nodes=[]
    for block in re.findall(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',original,re.S):
        d=json.loads(block);nodes.extend(d.get('@graph',[d]))
    faq=[(q['name'],q['acceptedAnswer']['text']) for q in next(n for n in nodes if n.get('@type')=='FAQPage')['mainEntity']]
    refresh(SLUG,'Buying a Vrbo Rental: What Transfers? | BNB Accelerator','Buying a Vrbo rental: what actually transfers at closing?',
      'Before buying a Vrbo rental, verify new-listing and reservation handoff. Use a seller-held payout split and dated buyer-cash worksheet.',
      body,faq,'2026-09-25','data-vrbo-handoff-review-link',
      'Test the <a href="/blog/vrbo-listing-handoff-buying-str/">Vrbo seller-held payout split and dated cash gap</a>. Guest charges, transfer approval and spendable buyer funds are different evidence.')
    p=ROOT/'blog'/SLUG/'index.html';s=p.read_text()
    if 'Updated October 7, 2026' not in s:
        s=s.replace('<span>Published September 25, 2026</span>','<span>Published September 25, 2026</span><span>&middot;</span><span>Updated October 7, 2026</span>',1)
    p.write_text(s)

if __name__=='__main__':main()
