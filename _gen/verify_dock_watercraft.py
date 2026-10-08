"""Read-only exact production, discovery and eligibility verification."""
import concurrent.futures, datetime, hashlib, json, re, urllib.request, urllib.robotparser
from pathlib import Path
from urllib.parse import urljoin, urlsplit
import xml.etree.ElementTree as ET
from verify_published_batch import fetch, BASE
R=Path(__file__).resolve().parents[1]
ROUTE='/blog/dock-watercraft-str-liability/'
URL=BASE+ROUTE
paths=[ROUTE,'/blog/','/blog/buy-str-high-income-large-tax-bill/','/sitemap-blog.xml']
for path in paths:
    live,final=fetch(BASE+path)
    local=R/'public'/path.lstrip('/')
    if path.endswith('/'): local=local/'index.html'
    assert final==BASE+path and live==local.read_text(), ('not exact deployed artifact',path)
s=fetch(URL)[0]
assert re.findall(r'<link[^>]+rel="canonical"[^>]+href="([^"]+)"',s)==[URL]
assert 'noindex' not in s.lower() and '$304,000' in s and '$298,000' in s
nodes=[]
for block in re.findall(r'<script[^>]+type="application/ld\+json"[^>]*>(.*?)</script>',s,re.S):
    d=json.loads(block);nodes.extend(d.get('@graph',[d]))
a=next(n for n in nodes if n.get('@type') in ['Article','BlogPosting'])
assert a['datePublished']=='2026-09-23' and a['dateModified']=='2026-10-08'
assert not any(n.get('@type')=='FAQPage' for n in nodes), 'Original page has no FAQ; no obsolete FAQ added'
ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
x=ET.fromstring(fetch(BASE+'/sitemap-blog.xml')[0])
for route in [ROUTE,'/blog/','/blog/buy-str-high-income-large-tax-bill/']:
    entries=[n for n in x.findall('s:url',ns) if n.findtext('s:loc',namespaces=ns)==BASE+route]
    assert len(entries)==1 and entries[0].findtext('s:lastmod',namespaces=ns)=='2026-10-08'
req=urllib.request.Request(URL,headers={'User-Agent':'Googlebot'})
with urllib.request.urlopen(req,timeout=35) as response:
    assert response.status==200 and response.geturl()==URL
    assert 'noindex' not in response.headers.get('X-Robots-Tag','').lower()
    assert response.read().decode()==s
rp=urllib.robotparser.RobotFileParser();rp.parse(fetch(BASE+'/robots.txt')[0].splitlines())
assert rp.can_fetch('Googlebot',URL)
links=set()
for ref in re.findall(r'(?:href|src)="([^"]+)"',s):
    u=urljoin(URL,ref);p=urlsplit(u)
    if p.netloc=='www.bnbaccelerator.com':links.add(BASE+p.path+('?' + p.query if p.query else ''))
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:list(pool.map(fetch,sorted(links)))
inbound=[]
for p in (R/'public').rglob('*.html'):
    if p!=(R/'public'/ROUTE.lstrip('/')/'index.html') and ('href="'+ROUTE+'"') in p.read_text():inbound.append(str(p.relative_to(R/'public')))
assert 'blog/index.html' in inbound and 'blog/buy-str-high-income-large-tax-bill/index.html' in inbound
home=hashlib.sha256(fetch(BASE+'/')[0].encode()).hexdigest()
assert home=='5a3fe67b5045fb0cfe7a6620b27e34e9149ed53cb4c6359f2aeb3ad770ce6484'
print(json.dumps({'url':URL,'verified_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exact_artifacts':len(paths),'live_links_assets':len(links),'inbound_pages':inbound,'googlebot_http_status':200,'canonical':URL,'robots_allowed':True,'noindex':False,'article_text_present':True,'homepage_sha256':home,'confirmed_indexing':'unknown; serving eligibility and empty stored inspection history are not confirmation'},indent=2))
