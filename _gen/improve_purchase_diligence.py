"""Preserve checklist; correct unsupported absolutes and add offer-decision worksheet."""
import html,json,math,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];SLUG='str-due-diligence-checklist'
DESC='Buying an STR? Verify permission, seller records and capacity, then translate inspection findings into repair cash, revised income and an offer decision.'
FAQ={
'What should I inspect when buying a short-term rental?':'Confirm the general inspection scope and arrange qualified specialist reviews where needed. Test water, wastewater, electrical and equipment capacity against proposed lawful guest use, along with access, safety and internet service. An appraisal or a seller listing does not substitute for these checks.',
'What documents should I verify before buying a short-term rental?':'Verify address-specific government permission and buyer transfer requirements, HOA and deed restrictions, seller platform and expense records if operating, an insurance quote for actual use, utility history, relevant capacity records and written financing conditions. Assign an owner and review deadline to each decisive item.',
'Why does septic matter so much in cabin markets?':'A septic system can affect purchase cost, permitted capacity and launch timing. Obtain available health-department records and a qualified system inspection. Ask the controlling authority and specialist whether the proposed use is acceptable; do not infer capacity from the seller guest count or assume every group stay causes failure.',
'What if a bedroom does not have conforming egress?':'Have a qualified professional and the controlling authority determine the safety, legal bedroom and occupancy consequences. Revise the revenue model to the supported capacity and obtain any feasible corrective-work estimate. A lower price does not itself authorize the bedroom or make unsafe sleeping space acceptable.'}
WORKSHEET='''<h3>Worked hypothetical: a repair allowance is not a complete purchase answer</h3>
<p>Assume a $600,000 STR purchase with a hypothetical approved $450,000 loan. Baseline capital is $150,000 toward price, $15,000 cash-paid closing costs, $30,000 setup and $25,000 retained reserve: $220,000 total. The buyer designates $245,000, leaving $25,000 unallocated. No reserve is double-counted as spent money. These are invented inputs, not lender requirements, contractor quotes or a client result.</p>
<div class="table-scroll"><table><thead><tr><th>New diligence finding</th><th>Hypothetical modeled effect</th><th>Buyer decision</th></tr></thead><tbody>
<tr><td>Specialist identifies corrective work before opening</td><td>$18,000 incremental repair cash, not already in setup</td><td>Verify scope, access, price, approval and completion evidence</td></tr>
<tr><td>Work delays lawful opening</td><td>$7,000 additional carrying cash with zero STR receipts</td><td>Reconfirm lender, insurance and vendor dates; do not count seller bookings</td></tr>
<tr><td>Authority supports less guest capacity than advertised</td><td>Independent demand analysis revises annual revenue from $100,000 to $85,000</td><td>Re-underwrite the supported use; do not assume a repair restores capacity</td></tr>
</tbody></table></div>
<p>Repair and delay require another $25,000, taking capital to $245,000 and using all unallocated cash while retaining the original $25,000 reserve. The inspection is not a pass simply because the buyer can pay. If the original model has $30,000 annual owner cash after its assumed expenses and debt, and variable expenses fall by an assumed 20% of the $15,000 revenue reduction, costs decline $3,000 and annual cash drops $12,000 to $18,000 under otherwise unchanged inputs. Against a hypothetical buyer-chosen $24,000 annual hurdle, the revised case fails. The capacity/revenue change comes from separate assumed evidence, not a rule that guest count determines revenue proportionally.</p>
<p>Consider a $20,000 price reduction. If the lender still approves 75% of the lower $580,000 price, with no lower appraisal or changed costs, the loan is $435,000 and price cash is $145,000: only $5,000 less buyer price cash, not $20,000. Revised capital is $240,000, leaving $5,000 outside the plan. Requote debt payments and rerun the income case; the original $18,000 cash result assumed the old debt payment and is not the result after renegotiation. A permitted seller credit may affect eligible closing charges differently and does not automatically supply unrestricted repair cash. Ask the lender and closing team for the actual treatment.</p>
<p>Proceed only if permission and safety are resolved and both funding and revised income clear your own hurdles. Renegotiate when a documented price, completed repair or permissible adjustment makes the case viable. Delay only under valid contract protection for a named unresolved condition; use the <a href="/blog/permit-pending-due-diligence-extension/">separate extension decision</a> when permit evidence is pending. Reject the STR thesis if the supported use cannot meet the investment case or material safety/permission questions remain unresolved. A price cut cannot make prohibited use lawful.</p>
<h3>Close the evidence loop before releasing protection</h3>
<p>For each material finding, record its source, responsible professional, additional cash, change to permitted capacity or revenue, completion date and contract deadline. Distinguish a firm quote from an allowance and a completed repair from a seller promise. Verify paid work with the appropriate professional and obtain required approvals; do not rely solely on an invoice. Ask counsel about actual remedies and notices, and the lender about property-condition requirements. See the <a href="/blog/inspection-contingency-length-str/">diligence-window planning guide</a> for timing; this checklist addresses the purchase decision once findings arrive.</p>
<p><a href="/apply/">Book a call to compare this STR's corrected purchase budget and supported guest capacity with another candidate</a>. Bring the inspection findings, written use evidence and actual quotes. Do not publish private seller or lender records.</p>'''

def main():
 p=ROOT/'blog'/SLUG/'index.html';s=p.read_text()
 s=re.sub(r'<p class="lead">.*?</p>','<p class="lead">Before buying a short-term rental, verify more than the building condition: establish buyer permission, supported guest capacity, reliable seller records, insurability and cash through lawful opening. Use inspection findings to decide whether to proceed, renegotiate, delay or reject the purchase. A repair list without a revised acquisition model is incomplete.</p><p><a href="/apply/">Book a call to review STR diligence findings before committing to the purchase</a>.</p>',s,count=1,flags=re.S)
 pairs={
'In coastal and wildfire exposed markets this single item decides deals.':'Ask a licensed adviser about coverage, exclusions, deductibles and binding conditions for this address and rental use.',
'which reveals the real cost of heating a property that runs year round with heavy guest use.':'matched to the seller occupancy, actual use and intended buyer operation; historical bills are not automatically a forecast.',
'A property sleeping fourteen with a residential water heater will generate reviews about cold showers within the first month.':'Have a qualified specialist assess supply and recovery for the proposed use; equipment type alone does not predict a failed stay.',
'since guests set thermostats aggressively and a marginal system fails under that load.':'with a qualified assessment of condition and suitability for the proposed occupancy, not an assumed failure based on guest behavior.',
'which is the single most expensive surprise in rural cabin markets and is sized for a family rather than a rotating group of twelve.':'checked against available approvals, system records and the proposed lawful use rather than inferred from the number of advertised beds.',
'particularly in mountain markets, where a steep unpaved approach costs winter bookings and generates complaints year round.':'including legal access, maintenance responsibility and practical seasonal usability; verify the actual route without unsafe weather testing.',
'<h2 id="safety">Safety items that are frequently licensing requirements</h2>':'<h2 id="safety">Confirm safety and occupancy requirements for this address</h2>',
'A basement bedroom without conforming egress is a common issue, and it matters twice: it may not count as a bedroom for licensing, and it affects the sleeping capacity your revenue model assumed.':'Have qualified professionals and the authority confirm which spaces can lawfully and safely count as bedrooms and the permitted occupancy. Check the listed safety items against applicable local rules rather than treating this list as a national code. Unsupported sleeping capacity changes the revenue assumptions as well as any corrective-work budget.',
'Every diligence finding is either a price adjustment, a budget line, or a reason to walk. A septic system at the end of its life is a capital item to fund, not a surprise to absorb. An undersized water heater is a modest fix. An unpermitted addition counted as two bedrooms in the listing is a revenue model problem, not a repair.':'Classify material findings as a condition requiring evidence, incremental cash, a delay, a recurring expense change or a restriction on the supported use. A specialist estimate determines whether a repair is affordable; do not assume an equipment replacement is modest. An unsupported bedroom can reduce buyer revenue even if the physical defect appears repairable.'}
 for old,new in pairs.items():assert old in s;s=s.replace(old,new,1)
 source='''<p><a href="https://www.consumerfinance.gov/owning-a-home/close/schedule-a-home-inspection/" rel="noopener">CFPB inspection guidance</a> distinguishes a physical inspection from an appraisal and recommends allowing time for additional inspections. Repair negotiations and cancellation depend on actual contract terms; some loan programs also impose property-condition requirements. Confirm the inspector's scope rather than assuming it includes legal-use, specialist systems or your STR underwriting.</p>'''
 s=s.replace('<h2 id="physical">Physical items that matter more in a rental</h2>',source+'\n<h2 id="physical">Physical items that matter more in a rental</h2>',1)
 septic='''<p><a href="https://www.epa.gov/septic/new-homebuyers-brochure-and-guide-septic-systems" rel="noopener">EPA's homebuyer septic guide</a> recommends a septic service-provider inspection before purchase and identifies local health-department records as a source of system drawings. Review maintenance and inspection records, the system and drainfield condition, and applicable local requirements. Ask the specialist and authority about the proposed STR load and capacity; this is not proof that a particular guest count is permitted or that a general home inspector performed a septic inspection.</p>'''
 s=s.replace('<h2 id="safety">',septic+'\n<h2 id="safety">',1)
 anchor='<p>The purpose of diligence is not to produce a list.';s=s.replace(anchor,WORKSHEET+'\n'+anchor,1)
 for q,a in FAQ.items():
  s,n=re.subn(r'(<h3>'+re.escape(q)+r'</h3>\s*<div class="faq-answer"><p>).*?(</p>)',lambda m:m.group(1)+a+m.group(2),s,count=1,flags=re.S);assert n==1
 note='<p class="small">Primary sources reviewed October 6, 2026. Educational information, not legal, tax, engineering, insurance, lending or personalized investment advice. Worked amounts and financing terms are hypothetical. Obtain qualified independent reviews and written transaction-specific terms; no permit, repair outcome, financing, tax benefit or return is guaranteed.</p>'
 s=s.replace('<div class="author-box">',note+'\n<div class="author-box">',1)
 words=len(re.findall(r'\b\w+\b',html.unescape(re.sub('<[^>]+>',' ',re.search(r'<article class="article">(.*?)<div class="author-box">',s,re.S).group(1)))));minutes=math.ceil(words/220)
 for key in ['description','og:description','twitter:description']:
  s=re.sub(r'(<meta (?:name|property)="'+key+r'" content=")[^"]*(")',lambda m:m.group(1)+html.escape(DESC,quote=True)+m.group(2),s)
 s=re.sub(r'(<meta property="article:published_time" content=")[^"]+',r'\g<1>2026-08-11',s)
 s=s.replace('<span>Published August 11, 2026</span>','<span>Published August 11, 2026</span><span>&middot;</span><span>Updated October 6, 2026</span>',1)
 s=re.sub(r'<span>\d+ min read</span>',f'<span>{minutes} min read</span>',s,count=1)
 def schema(m):
  d=json.loads(m.group(2))
  for n in d.get('@graph',[d]):
   if n.get('@type') in ['Article','BlogPosting']:assert n['datePublished']=='2026-08-11';n.update(description=DESC,dateModified='2026-10-06',wordCount=words)
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
  count+=1;c=re.sub(r'<p>.*?</p>','<p>'+DESC+'</p>',c,count=1,flags=re.S);c=re.sub(r'data-search="[^"]*"','data-search="'+html.escape(('Short-Term Rental Due Diligence Checklist '+DESC+' repair cash supported occupancy purchase decision').lower(),quote=True)+'"',c)
  return re.sub(r'<span>\d+ min read</span>',f'<span>{minutes} min read</span>',c)
 a=re.sub(r'<article class="post-card".*?</article>',card,archive.read_text(),flags=re.S);assert count==1;archive.write_text(a)
 hub=ROOT/'blog/buy-str-high-income-large-tax-bill/index.html';h=hub.read_text();block='<p data-diligence-offer-link>Inspection findings can change more than repair costs. Use the <a href="/blog/str-due-diligence-checklist/">STR diligence purchase worksheet</a> to separate additional cash, supported capacity and revised income before approving an offer.</p>';assert 'data-diligence-offer-link' not in h;hub.write_text(h.replace('<div class="author-box">',block+'\n<div class="author-box">',1))
 for xml in ROOT.glob('sitemap*.xml'):
  t=xml.read_text();n=re.sub(r'(<loc>https://www.bnbaccelerator.com/blog/'+SLUG+r'/</loc>\s*<lastmod>)[^<]+',r'\g<1>2026-10-06',t)
  if n!=t:xml.write_text(n)
 print(f'{words}words;{minutes}min;August11publication;four FAQs aligned')

if __name__=='__main__':main()
