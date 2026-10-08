"""Independent live eligibility, not actual Google crawling or indexing."""
import datetime, json, re, urllib.request, urllib.robotparser
from pathlib import Path
from verify_published_batch import BASE, fetch
ROOT=Path(__file__).resolve().parents[1]
URL=BASE+'/blog/cleaning-fees-gross-revenue/'
def main():
    with urllib.request.urlopen(urllib.request.Request(URL,headers={'User-Agent':'Googlebot'}),timeout=35) as response:
        status=response.status;final=response.geturl();headers=response.headers
        body=response.read().decode()
    assert status==200 and final==URL
    assert body==(ROOT/'public/blog/cleaning-fees-gross-revenue/index.html').read_text()
    assert re.findall(r'<link[^>]+rel="canonical"[^>]+href="([^"]+)"',body)==[URL]
    assert 'noindex' not in headers.get('X-Robots-Tag','').lower()
    assert not re.search(r'<meta[^>]+name="robots"[^>]+content="[^"]*noindex',body,re.I)
    article=re.search(r'<article class="article">(.*?)</article>',body,re.S)
    assert article and len(re.sub('<[^>]*>','',article[1]).strip())>500
    robots=urllib.robotparser.RobotFileParser();robots.parse(fetch(BASE+'/robots.txt')[0].splitlines())
    assert robots.can_fetch('Googlebot',URL)
    assert fetch(BASE+'/sitemap-blog.xml')[0].count('<loc>'+URL+'</loc>')==1
    route='/blog/cleaning-fees-gross-revenue/'
    inbound=sum(route in set(re.findall(r'href="(/blog/[^"?#]+/)"',p.read_text())) for p in (ROOT/'public').rglob('index.html'))
    assert inbound>0
    assert fetch(BASE+'/')[0]==(ROOT/'public/index.html').read_text()
    print(json.dumps({'verified_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'url':URL,'http_status':status,'final_url':final,'canonical':URL,'googlebot_ua_http_200':True,'robots_allowed':True,'noindex':False,'server_article_text':True,'exact_public_build_match':True,'sitemap_entries':1,'inbound_public_pages':inbound,'protected_homepage_exact':True,'limits':'Independent eligibility only, not actual Google crawling, browser rendering, indexing, exclusion cause, content review or performance gain.'},indent=2))
if __name__=='__main__':main()
