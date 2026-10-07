"""Exact live deployment and eligibility verification, without indexing inference."""
import datetime,json,re,urllib.request,urllib.robotparser
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urljoin,urlsplit
import xml.etree.ElementTree as ET
from verify_published_batch import BASE,fetch
ROOT=Path(__file__).resolve().parents[1]
ROUTE='/compare/alternatives-to-the-short-term-shop/'

def main():
    url=BASE+ROUTE;t,final=fetch(url)
    assert final==url and t==(ROOT/'public'/ROUTE.lstrip('/')/'index.html').read_text(),'Exact new deployment not yet live'
    sm,final=fetch(BASE+'/sitemap-core.xml');assert final==BASE+'/sitemap-core.xml' and sm==(ROOT/'public/sitemap-core.xml').read_text()
    ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
    e=[n for n in ET.fromstring(sm).findall('s:url',ns) if n.findtext('s:loc',namespaces=ns)==url]
    assert len(e)==1 and e[0].findtext('s:lastmod',namespaces=ns)=='2026-10-07'
    assert re.findall(r'<link[^>]+rel="canonical"[^>]+href="([^"]+)"',t)==[url]
    assert not re.search(r'<meta[^>]+name="robots"[^>]+content="[^"]*noindex',t,re.I)
    nodes=[]
    for b in re.findall(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',t,re.S):
        d=json.loads(b);nodes.extend(d.get('@graph',[d]))
    a=next(n for n in nodes if n.get('@type')=='Article');assert a['datePublished']=='2026-09-27' and a['dateModified']=='2026-10-07'
    assert all(v in t for v in ['$287,500','$290,500','$298,000','$301,000','Fictional illustration only','not firsthand testing'])
    robot=urllib.robotparser.RobotFileParser();robot.parse(fetch(BASE+'/robots.txt')[0].splitlines());assert robot.can_fetch('Googlebot',url)
    with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Googlebot'}),timeout=35) as r:
        assert r.status==200 and r.geturl()==url and 'noindex' not in r.headers.get('X-Robots-Tag','').lower() and r.read().decode()==t
    assert ROUTE in fetch(BASE+'/compare/')[0]
    assert fetch(BASE+'/')[0]==(ROOT/'public/index.html').read_text()
    targets={urljoin(url,x.split('#')[0]) for x in re.findall(r'(?:href|src)="([^"]+)"',t) if urlsplit(urljoin(url,x)).netloc==urlsplit(BASE).netloc}
    with ThreadPoolExecutor(max_workers=6) as pool:list(pool.map(fetch,sorted(targets)))
    inbound=sum(ROUTE in re.findall(r'href="([^"]+)"',p.read_text()) for p in (ROOT/'public').rglob('index.html'));assert inbound>0
    print(json.dumps({'verified_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'url':url,'http_status':200,'canonical':url,'final_url':url,'robots_allowed':True,'noindex':False,'googlebot_ua_http_200':True,'server_article_text':True,'exact_public_build_match':True,'exact_changed_public_artifacts':2,'compare_hub_discovery':True,'internal_links_assets_checked':len(targets),'inbound_public_pages':inbound,'publication_date':'2026-09-27','modified_date':'2026-10-07','sitemap':'sitemap-core.xml','sitemap_entries':1,'sitemap_lastmod':'2026-10-07','protected_homepage_exact':True,'limits':'Serving eligibility and submission acceptance do not establish actual Google crawl/indexing, browser rendering, rankings or qualified enquiries.'},indent=2))

if __name__=='__main__':main()
