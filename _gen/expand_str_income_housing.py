"""Bounded existing-owner insertion; preserve all original sections and FAQ questions."""
import html,json,math,re
from pathlib import Path
R=Path(__file__).resolve().parents[1]
SLUG='airbnb-income-qualify-conventional-str-loan'
DESCRIPTION='Can Airbnb income help finance an STR purchase? Check Fannie Mae rent evidence, current housing-payment documentation and a lender-acceptance worksheet.'
BLOCK='''<h2>Document your current housing payment before relying on the rent</h2>
<p>The specific <a href="https://selling-guide.fanniemae.com/sel/b3-3.8-03/rental-income-subject-property-short-term-rental" rel="noopener">subject-property STR topic</a> requires the lender to document the borrower's current housing payment to use subject-property rental income for qualification. A satisfactory comparable-rent report does not close this separate borrower-evidence gate. Ask the loan officer which evidence is accepted for your actual primary residence and whether anything remains unresolved before setting an offer price around rental-income qualification.</p>
<p>The <a href="https://selling-guide.fanniemae.com/sel/b3-3.8-01/general-rental-income-information" rel="noopener">general rental-income topic</a> defines current housing payments to include rent, mortgage PITIA and applicable leasehold payments, or property taxes and applicable leasehold payments for a non-mortgaged primary residence. Mortgage-free does not automatically mean no qualifying housing payment. Where the liability is absent from the credit report, its documentation examples include rent verification, six months of bank statements or canceled checks showing housing payments, or the latest property-tax payment. These are policy examples, not a promise that one document resolves every file. Let the lender specify what is needed and confirm acceptance.</p>
<p>Hiring a property manager is also not proof of the borrower's own rental-income or property-management history. Do not use the general topic's treatment of other rental situations to override the specific STR purchase topic's offset-only treatment of a positive result. Have the lender reconcile the applicable topics and its actual implementation date rather than selecting whichever paragraph produces the largest modeled buying power.</p>
<h2>Use an acceptance worksheet, not just a rent calculator</h2>
<div class="table-scroll"><table><thead><tr><th>Offer-file field</th><th>Record before relying on it</th><th>Unresolved outcome</th></tr></thead><tbody>
<tr><td>Policy and product</td><td>Named lender, application date, adopted policy version and overlays</td><td>A future implementation date is not today's approval</td></tr>
<tr><td>Primary housing payment</td><td>Residence, payment type, requested documents and lender acceptance</td><td>Do not assume the subject rent can be used while evidence is outstanding</td></tr>
<tr><td>Subject property and rent</td><td>Legal STR use, accepted rent source, monthly units and complete PITIA</td><td>Keep an unaccepted projection outside the supported qualification case</td></tr>
<tr><td>Whole borrower file</td><td>Income, debts, credit and remaining underwriting conditions</td><td>Accepted rent evidence is not a final mortgage approval</td></tr>
<tr><td>Purchase cash</td><td>Cleared funds, dated closing and launch payments, retained reserves</td><td>Qualification does not supply cash for an earlier payment</td></tr>
</tbody></table></div>
<p>Hypothetical comparison: two buyers consider the same property with the $8,000 gross-rent and $3,500 PITIA assumptions above. Buyer A's lender has accepted the current-housing-payment evidence and rent documentation under the applicable policy. The lender may apply the specified offset-only calculation, subject to all remaining loan requirements. Buyer B has the same rent report but no accepted housing-payment evidence. The arithmetic is identical; the supported qualification file is not. Buyer B should ask whether verified employment or other income supports a loan without this subject rent, or whether another legitimate product is available. Missing evidence does not establish universal ineligibility for every mortgage.</p>
<p>Separately, suppose either buyer has $280,000 of cleared acquisition funds and a $260,000 closing-and-launch allocation that already includes $35,000 of retained reserves. The unallocated margin is $20,000. A genuinely available alternative loan requiring $12,000 more cash reduces that margin to $8,000; an additional, non-overlapping $11,000 opening obligation then creates a $3,000 funding gap. Do not spend the protected reserve or count expected rent or a future tax benefit as cleared funds. These invented inputs illustrate a decision, not actual loan pricing, approval, customer results or an operating forecast.</p>
<p>Keep tax returns, bank records and identifying borrower documents in authorized secure channels, not a public worksheet or seller email chain. BNB Accelerator is an interested acquisition-service provider working within its contracted scope, not the approving lender. For <a href="/blog/buy-str-high-income-large-tax-bill/">high-income buyers deploying substantial capital</a>, a lender-accepted file and a separately funded downside plan are both necessary purchase questions.</p>
<p class="small">Fannie Mae's specific STR-income and general rental-income topics, dated September 2, 2026, and its September 23 reissued announcement reviewed October 8, 2026. Document-based educational guidance, not a professional review of your loan or personalized lending, legal, tax or investment advice. No financing, deduction or return is guaranteed.</p>'''
if __name__=='__main__':
 p=R/'blog'/SLUG/'index.html';s=p.read_text();old=s
 assert '<h2>Document your current housing payment' not in s
 s=s.replace('        <h2>Make the financing answer part of the buy decision</h2>',BLOCK+'\n        <h2>Make the financing answer part of the buy decision</h2>')
 s=s.replace('https://selling-guide.fanniemae.com/sel/b3-3.8-01/rental-income"','https://selling-guide.fanniemae.com/sel/b3-3.8-01/general-rental-income-information"')
 s=s.replace('Obtain actual Loan Estimates and compare total payment and cash needed, not merely a headline rate.','Obtain Loan Estimates where applicable or the product\'s written financing proposal, and compare total payment and cash needed, not merely a headline rate.')
 oldanswer="Potentially, for an eligible one-unit investment property legally permitted for STR use, using the lender's approved rent evidence and calculation. Ask when the lender implements the September 2026 policy and whether any overlays apply."
 newanswer=oldanswer+' The lender must also document the borrower\'s current housing payment before using subject-property rent.'
 assert s.count(oldanswer)==2;s=s.replace(oldanswer,newanswer)
 for name in ['description','og:description','twitter:description']:
  s=re.sub(r'(<meta (?:name|property)="'+name+r'" content=")[^"]*(")',lambda m:m[1]+html.escape(DESCRIPTION,quote=True)+m[2],s)
 body=re.search(r'<article class="article">(.*?)<div class="author-box">',s,re.S)[1]
 words=len(re.findall(r'\b\w+\b',html.unescape(re.sub('<[^>]+>',' ',body))));minutes=math.ceil(words/220)
 def schema(m):
  d=json.loads(m[2])
  for n in d.get('@graph',[d]):
   if n.get('@type') in ['Article','BlogPosting']:n.update(description=DESCRIPTION,dateModified='2026-10-08',wordCount=words)
  return m[1]+json.dumps(d,indent=2)+m[3]
 s=re.sub(r'(<script[^>]*type="application/ld\+json"[^>]*>)(.*?)(</script>)',schema,s,flags=re.S)
 s=re.sub(r'<span>\d+ min read</span>',f'<span>{minutes} min read</span>',s,count=1)
 s=s.replace('<span>Published September 24, 2026</span>','<span>Published September 24, 2026</span><span>Updated October 8, 2026</span>')
 assert '"datePublished": "2026-09-24"' in s;p.write_text(s)
 p=R/'blog/index.html';a=p.read_text();matches=0
 def card(m):
  global matches
  c=m[0]
  if '/blog/'+SLUG+'/' not in c:return c
  matches+=1
  c=re.sub(r'<p>.*?</p>','<p>'+DESCRIPTION+'</p>',c,count=1,flags=re.S)
  c=re.sub(r'data-search="[^"]*"','data-search="'+html.escape(('Can projected Airbnb income help you qualify to buy an STR? '+DESCRIPTION+' housing payment lender acceptance purchase cash').lower(),quote=True)+'"',c)
  return re.sub(r'<span>\d+ min read</span>',f'<span>{minutes} min read</span>',c)
 a=re.sub(r'<article class="post-card".*?</article>',card,a,flags=re.S);assert matches==1;p.write_text(a)
 p=R/'blog/buy-str-high-income-large-tax-bill/index.html';h=p.read_text();assert 'data-str-housing-payment-link' not in h
 h=h.replace('<div class="author-box">','<p data-str-housing-payment-link>Planning to use projected rent in a conventional STR purchase? Complete the <a href="/blog/airbnb-income-qualify-conventional-str-loan/">lender housing-payment acceptance and purchase-cash worksheet</a> before relying on that financing path.</p>\n<div class="author-box">',1);p.write_text(h)
 p=R/'sitemap-blog.xml';x=p.read_text();url='https://www.bnbaccelerator.com/blog/'+SLUG+'/'
 x,n=re.subn(r'(<loc>'+re.escape(url)+r'</loc>\s*<lastmod>)[^<]*(</lastmod>)',lambda m:m[1]+'2026-10-08'+m[2],x);assert n==1;p.write_text(x)
 print(json.dumps({'words':words,'minutes':minutes,'original_publication':'2026-09-24','FAQ_questions':4,'new509':False}))
