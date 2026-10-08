#!/usr/bin/env python3
"""Render approved property models as crawlable HTML, never draft data."""
from pathlib import Path
from datetime import date
import html,json,re,sys,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'_gen'))
import tpl
NS='http://www.sitemaps.org/schemas/sitemap/0.9'
def esc(x):return html.escape(str(x),quote=True)
def usd(x):return f'${x:,.0f}'
def amount(x,name):
 if isinstance(x,bool) or not isinstance(x,(int,float)) or x<0 or not __import__('math').isfinite(x):raise ValueError(name+' must be a finite nonnegative number')
 return x
def rowsum(rows,name):
 if not rows:raise ValueError(name+' needs explicit labeled rows')
 for r in rows:
  if not isinstance(r.get('label'),str) or not r['label'].strip():raise ValueError(name+' row label required')
  amount(r.get('amount'),name)
 return sum(r['amount'] for r in rows)
def validate(d):
 if not re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',d.get('slug','')):raise ValueError('invalid slug')
 if d.get('verdict') not in ['good','bad','watch']:raise ValueError('invalid verdict')
 if d.get('evidence_type') not in ['actual','projected']:raise ValueError('actual/projected label required')
 if d.get('editorial_review_complete') is not True:raise ValueError('editorial review required')
 for key in ['title','market','verdict_reason','period','reviewed_on']:
  if not isinstance(d.get(key),str) or not d[key].strip():raise ValueError(key+' required')
 if date.fromisoformat(d['reviewed_on'])>date.today():raise ValueError('future review date')
 if d.get('address') and d.get('address_public') is not True:raise ValueError('omit private address or explicitly approve public address')
 for key in ['purchase_price','annual_revenue','annual_debt_service','downside_annual_revenue']:amount(d.get(key),key)
 for key in ['annual_operating_costs','cash_required','downside_annual_operating_costs']:rowsum(d.get(key,[]),key)
 if not d.get('assumptions') or not d.get('risks') or not d.get('sources'):raise ValueError('assumptions, risks and sources required')
 for s in d['sources']:
  if not s.get('label') or not re.match(r'^https://',s.get('url','')):raise ValueError('labeled HTTPS source required')
 return d
def calculate(d):
 cost=rowsum(d['annual_operating_costs'],'expenses');cash=rowsum(d['cash_required'],'cash');net=d['annual_revenue']-cost-d['annual_debt_service'];down=d['downside_annual_revenue']-rowsum(d['downside_annual_operating_costs'],'downside costs')-d['annual_debt_service']
 return {'cost':cost,'cash':cash,'net':net,'down':down,'coc':net/cash*100 if cash else None}
def table(rows):return '<div class="table-scroll"><table><thead><tr><th scope="col">Item</th><th scope="col">Amount</th></tr></thead><tbody>'+''.join('<tr><th scope="row">'+esc(k)+'</th><td>'+esc(v)+'</td></tr>' for k,v in rows)+'</tbody></table></div>'
def section(h,b):return '<section class="section"><div class="container narrow"><h2>'+esc(h)+'</h2>'+b+'</div></section>'
def paras(items):return ''.join('<p>'+esc(x)+'</p>' for x in items)
def render(d):
 c=calculate(d);path='/proformas/'+d['slug']+'/'
 label={'good':'Fits the modeled buying criteria','bad':'Pass at these assumptions','watch':'More evidence needed'}[d['verdict']]
 body='<main id="main-content"><section class="page-hero"><div class="container narrow"><p class="eyebrow">'+esc(d['evidence_type'].capitalize())+' property model · '+esc(d['market'])+'</p><h1>'+esc(d['title'])+'</h1>'+('<p>'+esc(d['address'])+'</p>' if d.get('address_public') and d.get('address') else '')+'<p>'+esc(label)+': '+esc(d['verdict_reason'])+'</p><p>Reviewed '+esc(d['reviewed_on'])+' · Period: '+esc(d['period'])+'</p></div></section>'
 body+=section('The deal in plain English',table([('Purchase price',usd(d['purchase_price'])),('Cash needed, including listed reserves',usd(c['cash'])),('Annual rental revenue',usd(d['annual_revenue'])),('Annual operating costs',usd(c['cost'])),('Annual debt payments',usd(d['annual_debt_service'])),('Cash left after costs and debt',usd(c['net'])),('Monthly average of annual cash flow',usd(c['net']/12)),('Cash-on-cash on listed cash',f'{c["coc"]:.1f}%' if c['coc'] is not None else 'Undefined: cash investment is zero')])+paras(['The monthly figure is an annual average, not a promise of even monthly income. Purchase price is the building price; cash needed is the listed cash contribution. Cash-on-cash is annual cash left divided by that contribution. Tax effects and appreciation are excluded.']))
 body+=section('Where the money goes',table([(r['label'],usd(r['amount'])) for r in d['cash_required']])+paras(['These are the explicitly supplied cash components. Check their timing and whether earnest money is credited rather than added twice. An expense missing from the source is an unresolved input, not automatically zero.']))
 body+=section('Operating costs behind the annual result',table([(r['label'],usd(r['amount'])) for r in d['annual_operating_costs']])+paras(['Debt payments are separate from operating costs. Confirm the treatment of cleaning fees, platform fees, management, repairs, replacements, insurance and owner use in the assumptions below.']))
 body+=section('What happens in the downside case',table([('Downside annual revenue',usd(d['downside_annual_revenue'])),('Downside operating costs',usd(rowsum(d['downside_annual_operating_costs'],'downside'))),('Debt payments, unchanged assumption',usd(d['annual_debt_service'])),('Downside annual cash left',usd(c['down']))])+table([(r['label'],usd(r['amount'])) for r in d['downside_annual_operating_costs']])+paras(['This scenario is conditional on the supplied downside assumptions. It is not a probability forecast. A negative figure means additional cash would be needed to cover the modeled year.']))
 for h,key in [('Assumptions that drive the model','assumptions'),('What supports this deal','strengths'),('Why this deal could disappoint','risks'),('Evidence still needed','missing_evidence')]:
  body+=section(h,paras(d.get(key,[])) or '<p>No items supplied in this category; that does not establish there are no risks or missing records.</p>')
 body+=section('Sources and model limits','<ul>'+''.join('<li><a href="'+esc(s['url'])+'">'+esc(s['label'])+'</a></li>' for s in d['sources'])+'</ul>'+paras(['BNB Accelerator publishes this analysis of the supplied records and assumptions. A good or bad verdict applies to the modeled purchase, not every buyer or every future price. Projections are not earned income; actual records apply only to their stated period. Legal use, financing and tax conclusions require their own current review.'])+'<p><a href="/reviews/actual-results-vs-projections/">Reports versus forecasts</a> · <a href="/proformas/">All property models</a> · <a href="/reviews/pro-forma-library/">Published acquisition examples</a> · <a href="/apply/">Discuss your buying criteria</a></p>')+'</main>'
 schema={'@context':'https://schema.org','@type':'Article','headline':d['title'],'datePublished':d.get('published_on',d['reviewed_on']),'dateModified':d['reviewed_on'],'mainEntityOfPage':tpl.SITE+path,'author':{'@type':'Organization','name':'BNB Accelerator'}}
 return tpl.page(title=d['title']+' | BNB Accelerator Pro Forma',description=f'{d["market"]} property analysis: {label.lower()}. Review purchase costs, cash flow, downside assumptions and source evidence.',path=path,body=body,body_class='blog',extra_schema='<script type="application/ld+json">'+json.dumps(schema)+'</script>')
def build():
 data=[]
 for file in sorted((ROOT/'_gen/proformas').glob('*.json')):
  d=json.loads(file.read_text())
  if d.get('publication_status')=='published':data.append(validate(d))
 slugs=[d['slug'] for d in data]
 if len(slugs)!=len(set(slugs)):raise ValueError('duplicate property slug')
 manifest=ROOT/'_gen/proformas-manifest.json';previous=json.loads(manifest.read_text()) if manifest.exists() else []
 for slug in previous:
  if slug not in slugs:
   if not re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',slug):raise ValueError('invalid manifest route')
   page=ROOT/'proformas'/slug/'index.html'
   if page.exists():page.unlink()
 for d in data:
  dest=ROOT/'proformas'/d['slug']/'index.html';dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(render(d))
 directory='<ul>'+''.join('<li><a href="/proformas/'+esc(d['slug'])+'/">'+esc(d['title'])+'</a> · '+esc(d['verdict'])+' · '+esc(d['evidence_type'])+'</li>' for d in data)+'</ul>' if data else '<p>Address-level deal reviews will appear here as reviewed property records are supplied. No property forecast is published yet.</p>'
 body='<main id="main-content"><section class="page-hero"><div class="container narrow"><h1>BNB Accelerator property pro formas</h1><p>Understand the cash needed, annual cash flow and downside before choosing a short-term rental.</p></div></section>'+section('Property models and deal decisions',directory)+section('How to read a deal',paras(['Start with the verdict and its reason. Then compare the purchase price with the cash contribution, including furnishing and listed reserves. Look at cash left after operating costs and debt payments, and inspect the downside case before relying on the headline return. Each property keeps its assumptions, source links and missing evidence on the page.','Both attractive deals and deals we would pass on belong in this library. A pass can result from price, cash needs, operating costs or unverified assumptions. It is a decision about the modeled acquisition rather than a blanket claim about the property.','Every model is labeled projected or actual. An annual projection is not a completed operating year, and a monthly average does not describe seasonality. Check the covered period and review date. The library is company-published analysis, not independent assurance or a promise of returns.']))+section('Explore the available evidence','<p><a href="/reviews/pro-forma-library/">25 published acquisition records</a> · <a href="/reviews/case-study-library/">32 published case studies</a> · <a href="/reviews/">Public review sources</a></p>')+'</main>'
 dest=ROOT/'proformas/index.html';dest.parent.mkdir(exist_ok=True);dest.write_text(tpl.page(title='BNB Accelerator Property Pro Formas and Deal Reviews',description='Read native STR property models with acquisition costs, operating assumptions, cash flow, downside cases and clear good-deal or pass explanations.',path='/proformas/',body=body,body_class='blog'))
 manifest.write_text(json.dumps(slugs,indent=2)+'\n')
 ET.register_namespace('',NS);file=ROOT/'sitemap-proof.xml';tree=ET.parse(file);root=tree.getroot()
 for node in list(root):
  if '/proformas/' in node.find('{'+NS+'}loc').text:root.remove(node)
 for path,modified in [('/proformas/','2026-10-08')]+[('/proformas/'+d['slug']+'/',d['reviewed_on']) for d in data]:
  node=ET.SubElement(root,'{'+NS+'}url');ET.SubElement(node,'{'+NS+'}loc').text=tpl.SITE+path;ET.SubElement(node,'{'+NS+'}lastmod').text=modified
 tree.write(file,encoding='utf-8',xml_declaration=True)
 print(f'Native pro formas: {len(data)} approved properties; drafts excluded')
if __name__=='__main__':build()
