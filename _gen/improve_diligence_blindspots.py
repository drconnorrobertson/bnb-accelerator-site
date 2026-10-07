"""Source-checked, in-place acquisition blind-spot review; preserve existing structure."""
import html,json,math,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SLUG='due-diligence-items-buyers-skip'
DESC='Buying an STR? Check overlooked permission, capacity, insurance and booking evidence before an offer, with a pre-offer decision matrix.'
REPLACEMENTS=[
('A standard residential inspection tells', 'Before buying a short-term rental, identify the evidence a general physical inspection cannot supply: buyer permission, supported capacity, coverage for intended use and credible operating records. This guide addresses pre-offer blind spots. The separate <a href="/blog/str-due-diligence-checklist/">purchase diligence checklist</a> translates findings into revised cash and income. Do not treat an unchecked item as either a pass or an automatic rejection.'),
('These are the highest-consequence', 'Confirm who controls each requirement and what the response actually proves. An application receipt is not approval, and a seller permit is not proof the buyer can operate. Obtain the controlling documents and professional interpretation rather than relying on the listing or a verbal reassurance.'),
('Septic capacity, in rural properties.', 'For a rural STR, obtain system records and a qualified septic inspection before purchase. Ask the specialist and controlling authority about the proposed lawful use; the seller bed count does not establish system capacity. Group stays do not automatically prove that a system will fail. <a href="https://www.epa.gov/septic/new-homebuyers-brochure-and-guide-septic-systems" rel="noopener">EPA homebuyer guidance</a> emphasizes a pre-purchase inspection.'),
('Well capacity and water availability,', 'Obtain available well records, recent testing and a qualified assessment of reliable water supply for the proposed use. Ask about seasonal limitations using address-specific evidence. A regional drought label or one successful faucet test does not establish whether this property can support the buyer occupancy plan.'),
('Electrical capacity for the amenity', 'Have a qualified electrical professional review the intended equipment load, existing service and any required upgrade or approval. Price only the documented scope into entry costs. A particular panel age or amenity list does not alone determine suitability.'),
('Confirm insurability for the specific', 'Seek a licensed insurance adviser\'s written quote for the address, ownership, occupancy and actual STR use early enough to act under the purchase contract. Confirm exclusions, deductibles, coverage limits, effective dates and binding conditions. Do not assume one policy form or a state residual-market product is available or sufficient for every wildfire-exposed property.'),
('On the coast, obtain actual', 'Ask about wind, flood and other relevant exposures for this address, not only coastal properties. Obtain needed risk records and quotes, including an elevation certificate when the adviser or lender requires one. <a href="https://www.floodsmart.gov/get-insured/buy-a-policy" rel="noopener">NFIP guidance</a> states that most homeowners, renters and business insurance does not cover flood damage. A flood quote is not proof that all rental-use coverage is adequate. Use actual premiums and deductible liquidity in the purchase case rather than an unsupported percentage.'),
('In condominium purchases, read', 'For a condominium, review available reserve studies, budgets, meeting minutes, announced assessments and structural reports with appropriate professionals. Deferred work and weak reserves are risk signals, not proof that a specific future assessment will occur. Determine what is known, what remains uncertain and whether the buyer can fund a labeled downside allowance.'),
('Drive the access road, ideally', 'Check lawful access, maintenance responsibility and practical seasonal usability. Visit safely and obtain reliable seasonal records or qualified local assessment; do not deliberately drive in hazardous conditions. Evaluate the intended guest vehicle and arrival pattern without predicting automatic cancellations or refunds.'),
('Verify the view from the actual', 'Verify the view from guest-usable spaces, not just listing photographs. Identify documented obstruction or change risks where relevant. Support any revenue premium with comparable evidence; a view is not a universal rate driver or guarantee of a durable premium.'),
('Verify walking distance to the beach', 'Verify the practical route to the demand anchor, including lawful public access, crossings and seasonal restrictions. Test the listing claim safely. A four-minute versus twelve-minute walk does not establish a universal pricing bracket; reflect the supported distinction in the comparable analysis.'),
('Confirm who holds the listing account.', 'Identify the listing account holder, management contract and permitted buyer launch path. Do not assume reviews, ranking or the listing account will transfer with title. Budget a new public presence where continuity is unsupported and separate manager promises from platform rules.'),
('Agree explicitly what happens to forward', 'Create an address-specific guest-obligation plan with counsel, the manager and the platform as appropriate. <a href="https://www.airbnb.com/help/article/1431" rel="noopener">Airbnb\'s current transfer guidance</a> says account ownership and reservations cannot be transferred to a different host or account, including through a trip-change request to hand management to a new owner. A purchase agreement does not override those rules. Do not count unsupported future bookings as buyer receipts. Use the <a href="/blog/future-reservations-at-closing/">reservation obligations guide</a> for a compliant closing evidence packet rather than assuming cancellation or a remittance arrangement is available.'),
('This is not usually thought', 'Assemble a dated, genuinely competitive set appropriate to this property and buyer plan; there is no universally sufficient listing count. Explain inclusion and exclusion based on supported location, access, lawful capacity, amenities and condition. Listing asking rates are not achieved revenue, and unavailable dates are not proof of paid demand.'),
('Price the gap. If the set', 'Separate feasible upgrades from constraints that cannot be corrected or are not approved. Obtain scope and cost evidence and test revenue without the upgrade. Matching a competitor amenity does not ensure matching its performance; an uncertain improvement should not be priced as guaranteed income.'),
('A property $60,000 below market', 'Hypothetical screening example: an independently supported $60,000 price advantage against a genuinely comparable alternative is outweighed by $110,000 of additional, non-overlapping setup spending by $50,000, before financing, timing and recurring costs. Neither number is a market fact or a client result. The alternative must have comparable supported use and total costs; do not call a property below market merely because its asking price is lower.'),
('Putting the regulatory work before', 'Resolve decisive use and coverage questions before an offer when feasible. If access, documents or final buyer approval cannot be obtained yet, ask counsel for specific contract protection, review deadlines and notice requirements rather than describing the unresolved item as verified. Do not waive protection or close on a prohibited-use assumption; alternative residential or long-term rental value needs separate analysis, not an automatic valuation rule.')]
FAQ={
'What does a standard home inspection miss on a short-term rental?':'Confirm the actual inspection scope. A physical report does not itself establish buyer STR permission, adequate insurance for intended use, platform booking continuity or reliable property revenue. Qualified specialist checks may be needed for water, wastewater and equipment capacity.',
'When should I verify the permit position?':'Resolve the controlling rules and buyer requirements before an offer when feasible. If final buyer approval is not available yet, obtain counsel-reviewed contract protection and a dated evidence plan. An application receipt or seller permit does not prove buyer approval, and a lower price cannot authorize prohibited use.',
'What should I check on a rural property?':'Obtain septic records and a qualified inspection, reliable well supply evidence, an electrical review for intended equipment and lawful, practical seasonal access. Ask professionals and the authority about the proposed use; do not infer approved capacity or certain failure from the advertised guest count.'}
MATRIX='''<h2>Pre-offer blind-spot evidence matrix</h2>
<p>Use one row per decisive claim. Record the address, proposed buyer use, dated source, who can verify it, what remains missing and the last safe contract decision date. Keep private seller and financing records secure. This is a verification plan, not a substitute for professional approval.</p>
<div class="table-scroll"><table><thead><tr><th>Seller claim</th><th>Evidence needed</th><th>If missing before an offer</th></tr></thead><tbody>
<tr><td>Existing permit covers your purchase</td><td>Controlling authority rules, current standing and buyer process</td><td>Do not assume continuity; seek specific protection or choose another candidate</td></tr>
<tr><td>Advertised beds support the revenue case</td><td>Lawful occupancy and specialist system review for intended use</td><td>Run the lower supported-use case, not the advertised maximum</td></tr>
<tr><td>Current insurance will work for you</td><td>Buyer-specific rental-use quote and binding conditions</td><td>Do not reuse the seller premium as a verified expense</td></tr>
<tr><td>Bookings and reviews come with the house</td><td>Platform rules and documented, compliant launch/guest-obligation plan</td><td>Exclude unsupported receipts and fund a fresh launch</td></tr>
<tr><td>Adding amenities closes the performance gap</td><td>Feasible approved scope, quotes and independent revenue evidence</td><td>Test the acquisition without promised uplift</td></tr>
</tbody></table></div>
<h3>Worked hypothetical: fewer unknowns can beat a lower price</h3>
<p>Suppose candidate A needs $210,000 capital through closing, setup and a separately retained reserve, versus $220,000 for B. The buyer designates $230,000. A therefore appears $10,000 cheaper. But A's original budget credited $8,000 of unsupported booking receipts against opening costs. Remove that offset, without double-counting already budgeted costs, and A needs $218,000. A separate, incremental $15,000 capacity-work allowance takes the downside total to $233,000, a $3,000 funding gap. B's $220,000 leaves $10,000 outside its plan, assuming its equivalent use, scope and receipts have been verified.</p>
<p>All amounts and evidence outcomes are hypothetical, not quotes or observed returns. The $15,000 allowance does not prove a fix is feasible or lawful; if capacity approval is unresolved, affordability alone cannot clear A. B is not automatically the better investment: compare supported income, debt, timing and remaining risks. This illustration isolates the cost of treating missing evidence as an approved purchase assumption.</p>
<p><strong>Proceed</strong> when material claims are independently supported and the corrected purchase case works. <strong>Renegotiate</strong> when a documented scope or price adjustment can make it viable. <strong>Delay</strong> only with valid, specific protection and a named evidence milestone. <strong>Reject</strong> the STR purchase thesis when supported use is prohibited, the downside is unfundable or decisive evidence cannot be obtained before protection ends.</p>
<p><a href="/apply/">Book a call to compare an STR shortlist using verified permission, capacity and opening cash</a>. Bring the evidence gaps and decision deadlines, not just the listing price.</p>
<p class="small">Primary sources reviewed October 6, 2026. Educational information, not legal, tax, engineering, insurance, lending or personalized investment advice. Obtain qualified independent reviews and transaction-specific written terms. No approval, financing, booking continuity, tax benefit or investment outcome is guaranteed.</p>'''
def main():
 p=ROOT/'blog'/SLUG/'index.html';s=p.read_text()
 for prefix,new in REPLACEMENTS:
  s,n=re.subn(r'<p(?: class="lead")?>'+re.escape(prefix)+r'.*?</p>',lambda m:('<p class="lead">' if 'class="lead"' in m.group() else '<p>')+new+'</p>',s,count=1,flags=re.S);assert n==1,prefix
 s=s.replace('<h2>Capacity items a residential inspection ignores</h2>','<h2>Capacity checks to confirm beyond the inspection scope</h2>',1)
 s=s.replace('<h2>The regulatory items</h2>','<p><a href="/apply/">Book a call to identify purchase-critical STR evidence gaps before making an offer</a>.</p><h2>The regulatory items</h2>',1)
 s=s.replace('<li>Regulatory: zoning, permit, transferability, association declaration. Before an offer.</li>','<li>Regulatory: establish controlling rules and buyer requirements before an offer where feasible; protect unresolved approval conditions.</li>',1)
 s=s.replace('<h2 id="faq">',MATRIX+'\n<h2 id="faq">',1)
 for q,a in FAQ.items():
  s,n=re.subn(r'(<h3>'+re.escape(q)+r'</h3>\s*<div class="faq-answer"><p>).*?(</p>)',lambda m:m.group(1)+a+m.group(2),s,count=1,flags=re.S);assert n==1
 s=s.replace('<span>Published August 15, 2026</span>','<span>Published August 15, 2026</span><span>&middot;</span><span>Updated October 6, 2026</span>',1)
 words=len(re.findall(r'\b\w+\b',html.unescape(re.sub('<[^>]+>',' ',re.search(r'<article class="article">(.*?)<div class="author-box">',s,re.S).group(1)))));minutes=math.ceil(words/220)
 s=re.sub(r'<span>\d+ min read</span>',f'<span>{minutes} min read</span>',s,count=1)
 for key in ['description','og:description','twitter:description']:
  s=re.sub(r'(<meta (?:name|property)="'+key+r'" content=")[^"]*(")',lambda m:m.group(1)+html.escape(DESC,quote=True)+m.group(2),s)
 def schema(m):
  d=json.loads(m.group(2))
  for node in d.get('@graph',[d]):
   if node.get('@type') in ['Article','BlogPosting']:assert node['datePublished']=='2026-08-15';node.update(description=DESC,dateModified='2026-10-06',wordCount=words)
   if node.get('@type')=='FAQPage':
    for item in node['mainEntity']:item['acceptedAnswer']['text']=FAQ[item['name']]
  return m.group(1)+json.dumps(d,indent=2)+m.group(3)
 s=re.sub(r'(<script[^>]*type="application/ld\+json"[^>]*>)(.*?)(</script>)',schema,s,flags=re.S);p.write_text(s)
 archive=ROOT/'blog/index.html';count=0
 def card(m):
  nonlocal count
  c=m.group()
  if '/blog/'+SLUG+'/' not in c:return c
  count+=1;c=re.sub(r'<p>.*?</p>','<p>'+DESC+'</p>',c,count=1,flags=re.S)
  c=re.sub(r'data-search="[^"]*"','data-search="'+html.escape(('STR due diligence items buyers miss '+DESC+' blind spot evidence matrix').lower(),quote=True)+'"',c)
  return re.sub(r'<span>\d+ min read</span>',f'<span>{minutes} min read</span>',c)
 archive.write_text(re.sub(r'<article class="post-card".*?</article>',card,archive.read_text(),flags=re.S));assert count==1
 hub=ROOT/'blog/buy-str-high-income-large-tax-bill/index.html';h=hub.read_text();assert 'data-blindspot-evidence-link' not in h
 hub.write_text(h.replace('<div class="author-box">','<p data-blindspot-evidence-link>Before trusting a cheaper STR shortlist candidate, use the <a href="/blog/due-diligence-items-buyers-skip/">pre-offer blind-spot evidence matrix</a> to distinguish missing permission, capacity and booking proof from verified purchase assumptions.</p>\n<div class="author-box">',1))
 for xml in ROOT.glob('sitemap*.xml'):
  t=xml.read_text();n=re.sub(r'(<loc>https://www.bnbaccelerator.com/blog/'+SLUG+r'/</loc>\s*<lastmod>)[^<]+',r'\g<1>2026-10-06',t)
  if n!=t:xml.write_text(n)
 print(f'{words} words; {minutes} minutes; preserved August15; three matching FAQs')
if __name__=='__main__':main()
