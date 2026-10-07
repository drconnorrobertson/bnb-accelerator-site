"""Read-only exact production checks for one refreshed resource guide."""
import concurrent.futures,datetime,json,re,urllib.request,urllib.robotparser
from pathlib import Path
from urllib.parse import urljoin,urlsplit
import xml.etree.ElementTree as ET
from verify_published_batch import BASE,fetch
ROOT=Path(__file__).resolve().parents[1]
ROUTE='/guides/str-service-responsibility-matrix/'
def main():
    url=BASE+ROUTE
    page,final=fetch(url)
    assert final==url and page==(ROOT/('public'+ROUTE+'index.html')).read_text()
    sm,_=fetch(BASE+'/sitemap-core.xml');assert sm==(ROOT/'public/sitemap-core.xml').read_text()
    assert re.findall(r'<link[^>]+rel="canonical"[^>]+href="([^"]+)"',page)==[url]
    assert not re.search(r'<meta[^>]+name="robots"[^>]+content="[^"]*noindex',page,re.I)
    nodes=[]
    for block in re.findall(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',page,re.S):
        d=json.loads(block);nodes.extend(d.get('@graph',[d]))
    a=next(n for n in nodes if n.get('@type')=='Article')
    assert a['datePublished']=='2026-10-01' and a['dateModified']=='2026-10-07'
    assert 'A sent report, a completed call' in page and 'producing a $3,000 funding shortfall' in page
    ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
    entry=[n for n in ET.fromstring(sm).findall('s:url',ns) if n.findtext('s:loc',namespaces=ns)==url]
    assert len(entry)==1 and entry[0].findtext('s:lastmod',namespaces=ns)=='2026-10-07'
    robot=urllib.robotparser.RobotFileParser();robot.parse(fetch(BASE+'/robots.txt')[0].splitlines());assert robot.can_fetch('Googlebot',url)
    with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Googlebot'}),timeout=35) as r:
        assert r.status==200 and r.geturl()==url and 'noindex' not in r.headers.get('X-Robots-Tag','').lower() and r.read().decode()==page
    targets={urljoin(url,x.split('#')[0]) for x in re.findall(r'(?:href|src)="([^"]+)"',page) if urlsplit(urljoin(url,x)).netloc==urlsplit(BASE).netloc}
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:list(pool.map(fetch,sorted(targets)))
    inbound=sum(ROUTE in set(re.findall(r'href="(/[^"]+/)"',p.read_text())) for p in (ROOT/'public').rglob('index.html'));assert inbound>0
    assert fetch(BASE+'/')[0]==(ROOT/'public/index.html').read_text()
    print(json.dumps({'verified_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'url':url,'http_status':200,'exact_public_artifacts':2,'canonical':url,'robots_allowed':True,'noindex':False,'googlebot_ua_200':True,'publication_date':'2026-10-01','modified_date':'2026-10-07','sitemap_entries':1,'internal_targets_checked':len(targets),'inbound_public_pages':inbound,'protected_homepage_exact':True,'limits':'Serving/eligibility is not Google crawl, browser rendering, indexing or search/conversion gain; no authenticated Vercel status assertion.'},indent=2))
if __name__=='__main__':main()
