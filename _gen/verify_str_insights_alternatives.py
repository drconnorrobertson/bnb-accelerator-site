"""Read-only exact deployment, eligibility, discovery and home protection checks."""
import concurrent.futures, datetime, json, re, urllib.request, urllib.robotparser
from pathlib import Path
from urllib.parse import urljoin, urlsplit
import xml.etree.ElementTree as ET
from verify_published_batch import BASE, fetch

ROOT = Path(__file__).resolve().parents[1]
ROUTE = '/compare/alternatives-to-str-insights/'
URL = BASE + ROUTE

def main():
    text, final = fetch(URL)
    assert final == URL and text == (ROOT / 'public/compare/alternatives-to-str-insights/index.html').read_text(), 'Deployment not yet serving exact current build'
    sitemap, final_sm = fetch(BASE + '/sitemap-core.xml')
    assert final_sm == BASE + '/sitemap-core.xml' and sitemap == (ROOT / 'public/sitemap-core.xml').read_text()
    ns = {'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
    entries = [n for n in ET.fromstring(sitemap).findall('s:url',ns) if n.findtext('s:loc',namespaces=ns)==URL]
    assert len(entries)==1 and entries[0].findtext('s:lastmod',namespaces=ns)=='2026-10-07'
    assert re.findall(r'<link[^>]+rel="canonical"[^>]+href="([^"]+)"',text)==[URL]
    assert not re.search(r'<meta[^>]+name="robots"[^>]+content="[^"]*noindex',text,re.I)
    nodes=[]
    for block in re.findall(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',text,re.S):
        d=json.loads(block);nodes.extend(d.get('@graph',[d]))
    article=next(n for n in nodes if n.get('@type')=='Article')
    assert article['datePublished']=='2026-10-01' and article['dateModified']=='2026-10-07'
    assert 'A fee-and-cash worksheet' in text and '$267,000' in text and '$263,000' in text
    assert '$245,000' in text and 'not provider pricing or a client result' in text
    robot=urllib.robotparser.RobotFileParser();robot.parse(fetch(BASE+'/robots.txt')[0].splitlines())
    assert robot.can_fetch('Googlebot',URL)
    with urllib.request.urlopen(urllib.request.Request(URL,headers={'User-Agent':'Googlebot'}),timeout=35) as r:
        assert r.status==200 and r.geturl()==URL and 'noindex' not in r.headers.get('X-Robots-Tag','').lower() and r.read().decode()==text
    hub=fetch(BASE+'/compare/')[0];assert ROUTE in hub
    assert fetch(BASE+'/')[0]==(ROOT/'public/index.html').read_text()
    targets={urljoin(URL,x.split('#')[0]) for x in re.findall(r'(?:href|src)="([^"]+)"',text) if urlsplit(urljoin(URL,x)).netloc==urlsplit(BASE).netloc}
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:list(pool.map(fetch,sorted(targets)))
    inbound=sum(ROUTE in re.findall(r'href="([^"]+)"',p.read_text()) for p in (ROOT/'public').rglob('index.html'))
    assert inbound>0
    print(json.dumps({'verified_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'url':URL,'http_status':200,'final_url':URL,'canonical':URL,'noindex':False,'robots_allowed':True,'googlebot_ua_http_200':True,'exact_changed_artifacts':2,'exact_public_build_match':True,'compare_hub_discovery':True,'internal_links_assets_checked':len(targets),'inbound_public_pages':inbound,'publication_date':'2026-10-01','modified_date':'2026-10-07','sitemap':'sitemap-core.xml','sitemap_entries':1,'sitemap_lastmod':'2026-10-07','protected_homepage_exact':True,'limits':'Serving and discovery checks are not confirmed Google indexing, browser rendering, rankings or enquiries.'},indent=2))

if __name__=='__main__': main()
