"""Render original buyer evidence guides without changing legacy content or dates."""
from pathlib import Path
import html,json,re,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
SITE='https://www.bnbaccelerator.com'
DATE='2026-11-20'
HUB='/field-guides/'
def e(value):return html.escape(value,quote=True)
def link(url,label):return '<a href="'+e(url)+'">'+e(label)+'</a>'
def page(g,body):
 path=HUB+g['slug']+'/'
 schema={'@context':'https://schema.org','@graph':[{'@type':'Organization','@id':SITE+'/#organization','name':'BNB Accelerator','url':SITE+'/'},{'@type':g.get('kind','Article'),'headline':g['title'],'description':g['description'],'datePublished':DATE,'dateModified':DATE,'mainEntityOfPage':SITE+path,'publisher':{'@id':SITE+'/#organization'},'author':{'@type':'Organization','name':'BNB Accelerator editorial'},'citation':[s['url'] for s in g['sources']]},{'@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':'Home','item':SITE+'/'},{'@type':'ListItem','position':2,'name':'Field guides','item':SITE+HUB},{'@type':'ListItem','position':3,'name':g['title'],'item':SITE+path}]}]}
 return '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+e(g['title'])+' | BNB Accelerator</title><meta name="description" content="'+e(g['description'])+'"><meta name="robots" content="index, follow"><link rel="canonical" href="'+SITE+path+'"><meta property="og:title" content="'+e(g['title'])+'"><meta property="og:description" content="'+e(g['description'])+'"><meta property="og:url" content="'+SITE+path+'"><meta property="og:type" content="article"><meta name="twitter:card" content="summary"><meta name="twitter:title" content="'+e(g['title'])+'"><meta name="twitter:description" content="'+e(g['description'])+'"><link rel="stylesheet" href="/assets/field-guides.css"><script defer src="/assets/field-guides.js"></script><style>h1,h2,a{overflow-wrap:anywhere}header nav a,nav.guide-nav a{display:inline-flex;align-items:center;min-height:44px}nav.guide-nav{gap:16px}.review-date{font-size:14px;color:#59625d}</style><script type="application/ld+json">'+json.dumps(schema).replace('<','\\u003c')+'</script></head><body><a class="skip" href="#main">Skip to content</a><header>'+link('/','BNB Accelerator')+'<nav aria-label="Primary">'+link(HUB,'Field guides')+link('/resources/str-investor-library/','Investor journey')+link('/apply/','Discuss acquisition support')+'</nav></header><main id="main">'+body+'</main><footer><p>BNB Accelerator · Acquisition and owner oversight. Examples are hypothetical and do not describe client results.</p><p>These planning guides organize evidence and decisions. Confirm property-specific requirements and professional conclusions with the responsible adviser or provider.</p>'+link(HUB,'Browse all field guides')+'</footer></body></html>'
def main():
 guides=json.loads((ROOT/'content/buyer-verification-guides.json').read_text());routes=[]
 for g in guides:
  path=HUB+g['slug']+'/';routes.append(path)
  body='<p class="eyebrow">'+e(g.get('category','Buyer verification and operating handoffs'))+'</p><h1>'+e(g['title'])+'</h1><p class="review-date">AI-assisted editorial guide · Published November 20, 2026</p><p class="lead">'+e(g['intro'])+'</p><nav class="guide-nav" aria-label="On this page">'+link('#decision','Decision process')+link('#checklist','Checklist')+link('#sources','Official sources')+'</nav><div id="decision">'
  body+=''.join('<section><h2>'+e(s['title'])+'</h2><p>'+e(s['text'])+'</p></section>' for s in g['sections'])+'</div>'
  body+='<section id="checklist"><h2>Prepare the evidence and next action</h2><ul>'+''.join('<li>'+e(s)+'</li>' for s in g['checklist'])+'</ul></section>'
  body+='<section id="sources"><h2>Official sources and review scope</h2><p>Sources checked November 20, 2026. This guide supports preparation; it does not certify safety, determine compliance, confirm coverage or establish investment performance.</p><ul>'+''.join('<li>'+link(s['url'],s['label'])+'</li>' for s in g['sources'])+'</ul></section>'
  body+='<section id="worksheet"><h2>Record your follow-up</h2><p>These optional notes stay in this page until you download them. They are not submitted or retained after a reload. Keep sensitive account credentials out of the notes.</p><form data-worksheet><label>Project reference<input type="text" name="project" autocomplete="off"></label><label>Source document and date<input type="text" name="source-date" autocomplete="off"></label><fieldset><legend>Action checklist</legend>'+''.join('<label><input type="checkbox" name="action-'+str(i)+'">'+e(s)+'</label>' for i,s in enumerate(g['checklist']))+'</fieldset><label>Unresolved question and responsible person<textarea name="next-step" rows="4"></textarea></label><p id="worksheet-status" role="status" aria-live="polite"></p><button type="button" id="export-worksheet">Download notes</button><button type="button" id="print-guide">Print guide</button></form></section>'
  body+='<section><h2>Continue the purchase review</h2><ul><li>'+link('/field-guides/acquisition-assumption-register/','Maintain an acquisition assumption register')+'</li><li>'+link('/field-guides/purchase-to-launch-responsibility-matrix/','Build a purchase-to-launch responsibility matrix')+'</li><li>'+link(HUB,'Browse all field guides')+'</li></ul></section>'
  dest=ROOT/path.strip('/')/'index.html';dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(page(g,body))
 hub=ROOT/'field-guides/index.html';s=hub.read_text();s=re.sub(r'<!-- buyer-verification:start -->.*?<!-- buyer-verification:end -->','',s,flags=re.S)
 page_count=(len(guides)+15)//16
 def cards(items):return ''.join('<article class="card" data-guide><h3>'+link(HUB+g['slug']+'/',g['title'])+'</h3><p>'+e(g['description'])+'</p></article>' for g in items)
 def pagination(number):return '<nav class="guide-pages" aria-label="Buyer guide pages">'+''.join('<span aria-current="page">'+str(n)+'</span>' if n==number else link(HUB if n==1 else HUB+'page/'+str(n)+'/',str(n)) for n in range(1,page_count+1))+'</nav>'
 navstyle='<style id="buyer-guide-navigation">.guide-pages{display:flex;flex-wrap:wrap;gap:12px;margin:24px 0}.guide-pages a,.guide-pages span{display:inline-flex;align-items:center;justify-content:center;min-width:44px;min-height:44px;padding:8px 14px;border:1px solid #d7d5ca}h1,h2,h3,a{overflow-wrap:anywhere}</style>'
 block='<!-- buyer-verification:start --><section><h2>Buyer verification and operating handoffs</h2><p>Browse '+str(len(guides))+' decision guides across '+str(page_count)+' pages. Search filters the cards shown on this page.</p>'+pagination(1)+'<div class="grid">'+cards(guides[:16])+'</div>'+pagination(1)+'</section><!-- buyer-verification:end -->'
 assert '<h2>Continue across the investor journey</h2>' in s
 s=s.replace('<h2>Continue across the investor journey</h2>',block+'<h2>Continue across the investor journey</h2>')
 s=re.sub(r'(<p id="search-status"[^>]*>)[^<]*',r'\g<1>22 guides shown on this page',s)
 s=re.sub(r'("dateModified"\s*:\s*")[^"]+',r'\g<1>'+DATE,s)
 s=re.sub(r'<style id="buyer-guide-navigation">.*?</style>','',s,flags=re.S).replace('</head>',navstyle+'</head>')
 hub.write_text(s)
 for number in range(2,page_count+1):
  route=HUB+'page/'+str(number)+'/'
  routes.append(route)
  title='BNB buyer verification and operating guides — page '+str(number)
  body='<p class="eyebrow">Field guides</p><h1>'+e(title)+'</h1><p>Explore practical operating decisions, current policy references and evidence checklists. Return to '+link(HUB,'all field guides')+' for the first page and the original owner worksheets.</p>'+pagination(number)+'<div class="grid">'+cards(guides[(number-1)*16:number*16])+'</div>'+pagination(number)
  g=dict(slug='page/'+str(number),title=title,description='Practical BNB buyer and operating decision guides, page '+str(number)+'.',sources=[],kind='CollectionPage')
  dest=ROOT/route.strip('/')/'index.html';dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(page(g,body).replace('</head>',navstyle+'</head>'))
 sm=ROOT/'sitemap-field-guides.xml';ET.register_namespace('','http://www.sitemaps.org/schemas/sitemap/0.9');tree=ET.parse(sm);r=tree.getroot();existing={n.find('{*}loc').text:n for n in r}
 for route in routes:
  if SITE+route in existing:continue
  n=ET.SubElement(r,'{http://www.sitemaps.org/schemas/sitemap/0.9}url');ET.SubElement(n,'{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text=SITE+route;ET.SubElement(n,'{http://www.sitemaps.org/schemas/sitemap/0.9}lastmod').text=DATE
 if SITE+HUB in existing:
  n=existing[SITE+HUB].find('{*}lastmod')
  if n is not None:n.text=DATE
 tree.write(sm,encoding='utf-8',xml_declaration=True)
 print(json.dumps({'buyerVerificationGuides':len(guides),'hubCards':22,'navigationPages':page_count,'date':DATE}))
if __name__=='__main__':main()
