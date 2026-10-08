#!/usr/bin/env python3
"""Publish whitelisted 2026-tab property snapshots; no linked workbook reads."""
from pathlib import Path
from collections import defaultdict,Counter
import hashlib,html,json,re,sys,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'_gen'))
import tpl
SITE=tpl.SITE;NS='http://www.sitemaps.org/schemas/sitemap/0.9';DATE='2026-10-08'
LABELS={'good':'Good candidates','not-great':'Not great / needs review','terrible':'Terrible at the screened assumptions'}
DISCLAIMER='Disclaimer: These pages reproduce selected property fields from the 2026 BNB deal-flow tracker as captured October 8, 2026. Income is projected, not actual rental income or net profit. Purchase prices, availability and screening decisions may change. The source yield field has no confirmed calculation basis. Good, not great and terrible describe the recorded screening stage or rejection reason, not guaranteed investment quality. Expenses, financing, cash required and cash-on-cash returns are not established by this tab. This is company-published information, not tax, legal or investment advice. Real estate involves risk, including loss of principal. Verify the property, legal use and all financial assumptions with qualified professionals before acting.'
def e(x):return html.escape(str(x),quote=True)
def slug(x):return re.sub('[^a-z0-9]+','-',str(x).lower()).strip('-')
def value(v,i):return str(v[i]).strip() if i<len(v) and v[i] is not None else ''
def group(status):
 s=status.lower().strip()
 if s in ['z_kill - income','z_kill - compliance']:return 'terrible'
 if re.match(r'^0[3-7] -',s) or s in ['z_closed','z__closed']:return 'good'
 return 'not-great'
def reason(status):
 s=status.lower()
 if 'kill - income' in s:return 'Rejected for income in the source tracker.'
 if 'kill - compliance' in s:return 'Rejected for compliance in the source tracker; no independent legal conclusion is asserted.'
 if 'sold' in s or 'off market' in s:return 'Recorded as sold or off market; availability is not established.'
 if 'pending' in s:return 'Pending status; the record does not establish an approved deal.'
 if 'uncooperative' in s:return 'Screening stopped because of seller cooperation; this is not a return assessment.'
 if group(status)=='good':return 'Advanced to secondary review, pairing, signatures, contract or closing in the tracker. This is a candidate classification, not proof of operating returns.'
 return 'Initial or unresolved review; the tracker does not establish an approved acquisition.'
def market(address):
 # Use only place text actually present in the supplied address.
 parts=[x.strip() for x in address.split(',') if x.strip()]
 if len(parts)>=3:
  city=parts[-2];state=re.sub(r'\s+\d{5}(?:-\d{4})?\s*$','',parts[-1]).strip()
  if len(city)<65 and re.fullmatch('[A-Za-z .]+',state):return city+', '+state
 return 'Market not separately specified'
def load():
 doc=json.loads((ROOT/'_gen/proformas/source-2026.json').read_text());assert doc['tab']=='2026' and doc['sheet_id']==591368209
 unique=defaultdict(list);excluded=[]
 for row in doc['rows']:
  if row['row']==1:continue
  address=re.sub(r'\s+',' ',value(row['values'],3)).strip()
  if not address or address.lower()=='property address:':excluded.append(row['row']);continue
  unique[address.casefold()].append(row)
 out=[];used=set()
 for key,history in unique.items():
  history.sort(key=lambda r:(value(r['values'],1),r['row']),reverse=True);r=history[0];v=r['values'];address=re.sub(r'\s+',' ',value(v,3));s=slug(address) or 'property'
  if s in used:s+='-'+hashlib.sha256(key.encode()).hexdigest()[:8]
  used.add(s)
  # No staff names, paired clients, phones, raw notes, emails, or private workbook links.
  out.append({'slug':s,'address':address,'market':market(address),'category':group(value(v,2)),'status':value(v,2),'reviewed_coc':r.get('reviewed_coc_field'),'reviewer_income':r.get('reviewer_income_assumption'),'date_added':value(v,1),'price':value(v,10),'income':value(v,9),'yield':value(v,8),'deal_type':value(v,11),'beds':value(v,13),'baths':value(v,14),'size':value(v,15),'furnished':value(v,16),'compliance':value(v,7),'history':[{'row':h['row'],'date':value(h['values'],1),'status':value(h['values'],2),'price':value(h['values'],10),'income':value(h['values'],9)} for h in history]})
 return sorted(out,key=lambda d:d['address'].casefold()),excluded
CSS='''<style>
.pf-wrap{max-width:1120px;margin:auto;padding:32px 20px}.pf-hero{background:#142b39;color:#fff;border-radius:24px;padding:36px;margin:24px 0}.pf-hero h1{font-size:clamp(28px,4vw,48px);line-height:1.12;color:#fff}.pf-hero p{color:#d8e8ed}.pf-tag{display:inline-block;padding:6px 12px;border-radius:20px;background:#dcefe6;color:#165d45;font-size:14px;font-weight:700}.pf-tag.not-great{background:#fff0c9;color:#704d00}.pf-tag.terrible{background:#fce0dd;color:#842d2d}.pf-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;margin:24px 0}.pf-card{padding:24px;border:1px solid #dde5e9;border-radius:16px;background:#fff;color:#142b39}.pf-card strong{display:block;font-size:clamp(22px,3vw,34px);margin:8px 0}.pf-card small{display:block;color:#526570}.pf-panel{padding:28px;border:1px solid #dde5e9;border-radius:20px;margin:24px 0;background:#fff}.pf-panel h2{font-size:25px;margin-top:0}.pf-details{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}.pf-detail{border-bottom:1px solid #e6ebee;padding:12px 0}.pf-detail dt{font-size:14px;color:#526570}.pf-detail dd{margin:4px 0;font-weight:600}.pf-links{display:flex;gap:12px;flex-wrap:wrap;margin:20px 0}.pf-links a{padding:10px 16px;border:1px solid #d5dfe3;border-radius:22px}.pf-items{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}.pf-items a{text-decoration:none}.pf-item{padding:20px;border:1px solid #d5dfe3;border-radius:16px}.pf-item h3{font-size:20px;margin:12px 0}.pf-disclaimer{border-top:2px solid #d9e2e7;margin-top:40px;padding-top:24px;color:#526570;font-size:14px}.pf-table{width:100%;border-collapse:collapse}.pf-table th,.pf-table td{padding:12px;text-align:left;border-bottom:1px solid #e4e9ec}.pf-wrap *{overflow-wrap:anywhere}@media(max-width:640px){.pf-grid,.pf-items,.pf-details{grid-template-columns:1fr}.pf-hero{padding:24px}.pf-panel{padding:20px}.pf-wrap{padding:20px 14px}}
</style>'''
def tag(cat):return '<span class="pf-tag '+cat+'">'+e(LABELS[cat])+'</span>'
def page(path,title,desc,body,article=False):
 schema={'@context':'https://schema.org','@type':'Article' if article else 'CollectionPage','headline':title,'name':title,'dateModified':DATE,'url':SITE+path}
 if article:schema.update(datePublished=DATE,author={'@type':'Organization','name':'BNB Accelerator'})
 body='<main id="main-content"><div class="pf-wrap">'+body+'<aside class="pf-disclaimer" aria-label="Disclaimer"><h2>Disclaimer</h2><p>'+e(DISCLAIMER)+'</p></aside></div></main>'
 return tpl.page(title=title+' | BNB Accelerator',description=desc,path=path,body=body,body_class='blog',extra_schema='<script type="application/ld+json">'+json.dumps(schema)+'</script>').replace('</head>',CSS+'</head>')
def hero(title,text):return '<header class="pf-hero"><p>BNB Accelerator · 2026 property screening</p><h1>'+e(title)+'</h1><p>'+e(text)+'</p></header>'
def card(label,number,note):return '<div class="pf-card"><span>'+e(label)+'</span><strong>'+e(number or 'Not supplied')+'</strong><small>'+e(note)+'</small></div>'
def property_page(d):
 path='/proformas/'+d['slug']+'/'
 body='<nav class="pf-links"><a href="/proformas/">All property reviews</a><a href="/proformas/'+d['category']+'/">'+e(LABELS[d['category']])+'</a></nav>'+hero(d['address']+' STR pro forma snapshot',reason(d['status']))+tag(d['category'])
 body+='<div class="pf-grid">'+card('Purchase-price field',d['price'],'Recorded price, not a current asking-price verification')+card('Projected annual income',d['income'],'Source projection; not net profit or earned income')+card('Screening decision',{'good':'Advanced candidate','not-great':'Needs review / unavailable','terrible':'Rejected'}[d['category']],'Source decision as captured October 8, 2026')+'</div>'
 body+='<section class="pf-panel"><h2>Property at a glance</h2><dl class="pf-details">'+''.join('<div class="pf-detail"><dt>'+e(k)+'</dt><dd>'+e(v or 'Not supplied')+'</dd></div>' for k,v in [('Address',d['address']),('Bedrooms',d['beds']),('Bathrooms',d['baths']),('Square footage',d['size']),('Furnishing',d['furnished']),('Deal type',d['deal_type']),('Date added',d['date_added']),('Compliance review',d['compliance'])])+'</dl></section>'
 if d.get('reviewed_coc') or d.get('reviewer_income'):
  body+='<section class="pf-panel"><h2>Financial fields recorded in the reviewer notes</h2><dl class="pf-details">'+''.join('<div class="pf-detail"><dt>'+e(k)+'</dt><dd>'+e(v or 'Not supplied')+'</dd></div>' for k,v in [('Reviewer income assumption',d.get('reviewer_income')),('Reviewer cash-on-cash field',d.get('reviewed_coc'))])+'</dl><p>These are numeric fields extracted from this row’s notes. They may differ from the tracker’s headline fields. Their complete calculation basis is not supplied; they are not verified operating results.</p></section>'
 body+='<section class="pf-panel"><h2>What this screening tells you</h2><p>'+e(reason(d['status']))+'</p><p>This tab does not supply complete operating expenses, debt payments, cash to close, furnishing budgets or a reproducible downside model. Those amounts remain unavailable here rather than being filled with assumptions from another source.</p></section>'
 if len(d['history'])>1:
  body+='<section class="pf-panel"><h2>Other tracker entries for this address</h2><p>The lead snapshot uses the most recent date-added field, then the later source row when dates match. Date added is not necessarily the last underwriting update. Each source entry remains below.</p><div class="table-scroll"><table class="pf-table"><thead><tr><th>Source row</th><th>Date added</th><th>Status</th><th>Purchase-price field</th><th>Projected income</th></tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+e(h[k] or 'Not supplied')+'</td>' for k in ['row','date','status','price','income'])+'</tr>' for h in d['history'])+'</tbody></table></div></section>'
 if d['market']!='Market not separately specified':body+='<p><a href="/proformas/markets/'+slug(d['market'])+'/">More STR deal reviews in '+e(d['market'])+'</a></p>'
 body+='<p>Source: supplied deal-flow tracker, tab “2026”, row '+str(d['history'][0]['row'])+'. No other tabs or linked workbooks used.</p>'
 return path,page(path,d['address']+' STR Pro Forma',f'Review {d["address"]}: recorded purchase price, projected annual income, property details and BNB screening classification from the 2026 tracker.',body,True)
def directory(path,title,ds,description,extra=''):
 output=[];size=96
 for offset in range(0,max(1,len(ds)),size):
  n=offset//size+1;p=path if n==1 else path+'page-'+str(n)+'/'
  heading=title if n==1 else title+' — page '+str(n)
  body=hero(heading,description)+extra+'<div class="pf-items">'+''.join('<article class="pf-item">'+tag(d['category'])+'<h3><a href="/proformas/'+d['slug']+'/">'+e(d['address'])+'</a></h3><p>Price field: '+e(d['price'] or 'Not supplied')+'<br>Projected annual income: '+e(d['income'] or 'Not supplied')+'</p></article>' for d in ds[offset:offset+size])+'</div><nav class="pf-links" aria-label="Directory pages">'
  if n>1:body+='<a href="'+(path if n==2 else path+'page-'+str(n-1)+'/')+'">Previous page</a>'
  if offset+size<len(ds):body+='<a href="'+path+'page-'+str(n+1)+'/">Next page</a>'
  body+='</nav>'
  output.append((p,page(p,heading,heading+'. '+description+f' Directory page {n}; browse property-specific records and screening decisions.',body)))
 return output
def build():
 ds,excluded=load();outputs=[];markets=defaultdict(list);counts=Counter(d['category'] for d in ds)
 for d in ds:
  outputs.append(property_page(d))
  if d['market']!='Market not separately specified':
   key=next((m for m in markets if slug(m)==slug(d['market'])),d['market']);markets[key].append(d)
 nav='<nav class="pf-links">'+''.join('<a href="/proformas/'+c+'/">'+e(LABELS[c])+': '+str(counts[c])+'</a>' for c in LABELS)+'<a href="/proformas/markets/">Browse markets</a></nav>'
 definition='<section class="pf-panel"><h2>How deals are grouped</h2><p>Good candidates advanced beyond initial review or reached closing. Not great includes unresolved, pending, sold, unavailable and incomplete-review records. Terrible means the source rejected the deal for income or compliance. These are screening groups, not verified return rankings. A passed deal can change at a different price or with new evidence.</p></section>'
 outputs+=directory('/proformas/','STR property deals and pro forma snapshots',ds,'Browse good candidates, unresolved deals and rejected STR acquisitions from the supplied 2026 tracker.',nav+definition)
 for cat in LABELS:outputs+=directory('/proformas/'+cat+'/',LABELS[cat]+' — STR deal reviews',[d for d in ds if d['category']==cat],'Compare address-level source records in this screening group; income figures are projections, not verified returns.',nav)
 for m,items in markets.items():outputs+=directory('/proformas/markets/'+slug(m)+'/','Short-term rental deal reviews in '+m,items,'Explore STR acquisition candidates and rejected deals in '+m+' using the 2026 tracker’s property fields and screening decisions.',nav)
 body=hero('Find STR deal reviews by market','Browse the places written in the supplied property addresses. These are tracked deals, not a current market-wide ranking of the best investments.')+'<div class="pf-items">'+''.join('<div class="pf-item"><h2><a href="/proformas/markets/'+slug(m)+'/">'+e(m)+'</a></h2><p>'+str(len(items))+' property snapshots</p></div>' for m,items in sorted(markets.items()))+'</div>'
 outputs.append(('/proformas/markets/',page('/proformas/markets/','STR deal reviews by city and state','Find source-based short-term rental property reviews by city and state, including good candidates, unresolved deals and rejected acquisitions.',body)))
 manifest=ROOT/'_gen/tracker-proforma-manifest.json';previous=json.loads(manifest.read_text()) if manifest.exists() else [];paths=[p for p,s in outputs]
 assert len(paths)==len(set(paths)),'route collision'
 for p in previous:
  if p not in paths and p.startswith('/proformas/') and '..' not in p:
   f=ROOT/p.strip('/')/'index.html'
   if f.exists():f.unlink()
 for p,s in outputs:
  f=ROOT/p.strip('/')/'index.html';f.parent.mkdir(parents=True,exist_ok=True);f.write_text(s)
 manifest.write_text(json.dumps(paths,indent=2)+'\n')
 ET.register_namespace('',NS);root=ET.Element('{'+NS+'}urlset')
 for p in paths:
  n=ET.SubElement(root,'{'+NS+'}url');ET.SubElement(n,'{'+NS+'}loc').text=SITE+p;ET.SubElement(n,'{'+NS+'}lastmod').text=DATE
 ET.ElementTree(root).write(ROOT/'sitemap-proformas.xml',encoding='utf-8',xml_declaration=True)
 proof=ROOT/'sitemap-proof.xml';tree=ET.parse(proof)
 for n in list(tree.getroot()):
  if '/proformas/' in n.find('{'+NS+'}loc').text:tree.getroot().remove(n)
 tree.write(proof,encoding='utf-8',xml_declaration=True)
 index=ROOT/'sitemap.xml';tree=ET.parse(index)
 if not any(n.find('{'+NS+'}loc').text==SITE+'/sitemap-proformas.xml' for n in tree.getroot()):
  n=ET.SubElement(tree.getroot(),'{'+NS+'}sitemap');ET.SubElement(n,'{'+NS+'}loc').text=SITE+'/sitemap-proformas.xml'
 tree.write(index,encoding='utf-8',xml_declaration=True)
 report={'source_tab':'2026','source_rows':10356,'unique_property_pages':len(ds),'excluded_rows':excluded,'duplicate_rows_preserved':sum(len(d['history'])-1 for d in ds),'categories':dict(counts),'market_directories':len(markets),'public_routes':len(paths),'private_fields_published':False,'linked_workbooks_read':False}
 (ROOT/'_gen/tracker-proforma-ingestion-report.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
if __name__=='__main__':build()
