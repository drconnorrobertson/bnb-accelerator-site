"""Read-only serving/discovery baseline; not a browser render or indexing test."""
import datetime, json, re, urllib.request, urllib.robotparser
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlsplit
from verify_published_batch import BASE, fetch

ROOT=Path(__file__).resolve().parents[1]
ROUTES=['/compare/alternatives-to-str-search/','/compare/str-search/','/compare/alternatives-to-the-short-term-shop/','/compare/avery-carl-short-term-shop/','/compare/alternatives-to-awning/','/compare/awning/','/compare/alternatives-to-rabbu/','/compare/rabbu/','/blog/bnb-accelerator-vs-str-insights-buyer/']

def main():
    robot=urllib.robotparser.RobotFileParser();robot.parse(fetch(BASE+'/robots.txt')[0].splitlines())
    maps={p.name:p.read_text() for p in (ROOT/'public').glob('sitemap-*.xml')}
    pages={str(p.relative_to(ROOT/'public')):p.read_text() for p in (ROOT/'public').rglob('index.html')}
    hub=fetch(BASE+'/compare/')[0]
    def probe(route):
        url=BASE+route
        with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Googlebot'}),timeout=35) as response:
            text=response.read().decode();status=response.status;final=response.geturl();header=response.headers.get('X-Robots-Tag','')
        canonical=re.findall(r'<link[^>]+rel="canonical"[^>]+href="([^"]+)"',text)
        noindex=bool(re.search(r'<meta[^>]+name="robots"[^>]+content="[^"]*noindex',text,re.I)) or 'noindex' in header.lower()
        nodes=[]
        for block in re.findall(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',text,re.S):
            d=json.loads(block);nodes.extend(d.get('@graph',[d]))
        articles=[n for n in nodes if n.get('@type') in ['Article','BlogPosting']]
        main=re.search(r'<main\b.*?</main>',text,re.S)
        sitemaps=[name for name,xml in maps.items() if '<loc>'+url+'</loc>' in xml]
        inbound=sum(route in re.findall(r'href="([^"]+)"',p) for p in pages.values())
        indexable=status==200 and final==url and canonical==[url] and not noindex and robot.can_fetch('Googlebot',url)
        assert indexable and len(sitemaps)==1 and inbound>0 and main and articles and len(re.findall(r'<h1\b',text))==1
        return {'url':url,'http_status':status,'final_url':final,'canonical':canonical[0],'googlebot_ua':True,'robots_allowed':True,'noindex':noindex,'source_noindex':bool(re.search(r'<meta[^>]+name="robots"[^>]+content="[^"]*noindex',pages[route.lstrip('/')+'index.html'],re.I)),'exact_public_build_match':text==pages[route.lstrip('/')+'index.html'],'server_article_text':True,'sitemap_included':True,'sitemap':sitemaps[0],'inbound_public_pages':inbound,'compare_hub_discovery':route in hub,'topic_cluster':'STR acquisition service comparisons','impressions':None,'clicks':None,'performance_note':'Not newly queried; null is not zero','recommended_action':'Develop existing owner with provider-specific evidence and buyer work sample; retain indexing evidence distinction; no unchanged submission'}
    with ThreadPoolExecutor(max_workers=4) as pool:records=list(pool.map(probe,ROUTES))
    home=fetch(BASE+'/')[0]==(ROOT/'public/index.html').read_text();assert home
    print(json.dumps({'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'protected_homepage_exact':home,'records':records,'limits':'Googlebot user-agent access is not evidence of an actual Google crawl. Server text is not a browser rendering test. No rankings, enquiries, provider superiority or exclusion causes inferred.'},indent=2))

if __name__=='__main__':main()
