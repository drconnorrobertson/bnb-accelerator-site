"""Read-only exact production verification of this two-page refresh."""
import concurrent.futures, datetime, html, json, re
import urllib.request, urllib.robotparser
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urljoin, urlsplit
from verify_published_batch import BASE, fetch

ROOT=Path(__file__).resolve().parents[1]
SLUGS={'dscr-loans-for-airbnb':('2026-08-10',9),'dscr-vacancy-factor-str':('2026-09-23',4)}

def main():
    paths=['blog/'+v+'/index.html' for v in SLUGS]+['blog/index.html','blog/buy-str-high-income-large-tax-bill/index.html','sitemap-blog.xml']
    live={}
    for path in paths:
        route='/'+path.removesuffix('index.html')
        s,final=fetch(BASE+route)
        assert final==BASE+route and s==(ROOT/'public'/path).read_text(),('Deployment has not served exact current build',route)
        live[path]=s
    robot=urllib.robotparser.RobotFileParser();robot.parse(fetch(BASE+'/robots.txt')[0].splitlines())
    ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
    sm=ET.fromstring(live['sitemap-blog.xml']);links=set();records=[]
    for slug,(published,count) in SLUGS.items():
        path='blog/'+slug+'/index.html';s=live[path];route='/blog/'+slug+'/';url=BASE+route
        assert re.findall(r'<link[^>]+rel="canonical"[^>]+href="([^"]+)"',s)==[url]
        assert not re.search(r'<meta[^>]+name="robots"[^>]+content="[^"]*noindex',s,re.I)
        nodes=[]
        for block in re.findall(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',s,re.S):
            d=json.loads(block);nodes.extend(d.get('@graph',[d]))
        a=next(n for n in nodes if n.get('@type') in ['Article','BlogPosting'])
        assert a['datePublished']==published and a['dateModified']=='2026-10-07'
        faqs=next(n for n in nodes if n.get('@type')=='FAQPage')['mainEntity'];assert len(faqs)==count
        body=re.search(r'<article class="article">(.*?)</article>',s,re.S)[1]
        for q in faqs:assert q['name'] in html.unescape(body) and q['acceptedAnswer']['text'] in html.unescape(body)
        entries=[n for n in sm.findall('s:url',ns) if n.findtext('s:loc',namespaces=ns)==url]
        assert len(entries)==1 and entries[0].findtext('s:lastmod',namespaces=ns)=='2026-10-07'
        assert robot.can_fetch('Googlebot',url)
        with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Googlebot'}),timeout=35) as r:
            assert r.status==200 and r.geturl()==url and 'noindex' not in r.headers.get('X-Robots-Tag','').lower() and r.read().decode()==s
        targets={urljoin(url,x.split('#')[0]) for x in re.findall(r'(?:href|src)="([^"]+)"',s) if urlsplit(urljoin(url,x)).netloc==urlsplit(BASE).netloc}
        links.update(targets)
        inbound=sum(route in set(re.findall(r'href="(/blog/[^"?#]+/)"',p.read_text())) for p in (ROOT/'public').rglob('index.html'))
        assert inbound>0
        records.append({'url':url,'http_status':200,'final_url':url,'canonical':url,'robots_allowed':True,'noindex':False,'exact_public_build_match':True,'server_article_text':True,'publication_date':published,'modified_date':'2026-10-07','words':a['wordCount'],'matched_faqs':count,'sitemap_entries':1,'sitemap_lastmod':'2026-10-07','inbound_public_pages':inbound,'internal_targets':len(targets),'googlebot_ua_http_200':True})
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:list(pool.map(fetch,sorted(links)))
    assert fetch(BASE+'/')[0]==(ROOT/'public/index.html').read_text()
    print(json.dumps({'verified_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exact_changed_public_artifacts':len(paths),'protected_homepage_exact':True,'independent_internal_links_assets_checked':len(links),'records':records,'limits':'Serving/eligibility checks are not Google crawl, browser rendering, indexing or search/conversion gains; no authenticated Vercel status assertion.'},indent=2))

if __name__=='__main__':main()
