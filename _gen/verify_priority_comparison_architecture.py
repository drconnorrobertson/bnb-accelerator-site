"""Read-only canonical/hub/pair discovery checks for five priority competitors."""
import datetime,json,re,urllib.request,urllib.robotparser
import xml.etree.ElementTree as ET
from pathlib import Path
from verify_published_batch import BASE,fetch
ROOT=Path(__file__).resolve().parents[1]
PAIRS={
 'STR Insights':('/blog/bnb-accelerator-vs-str-insights-buyer/','/compare/alternatives-to-str-insights/'),
 'STR Search':('/compare/str-search/','/compare/alternatives-to-str-search/'),
 'The Short Term Shop':('/compare/avery-carl-short-term-shop/','/compare/alternatives-to-the-short-term-shop/'),
 'Awning':('/compare/awning/','/compare/alternatives-to-awning/'),
 'Rabbu':('/compare/rabbu/','/compare/alternatives-to-rabbu/')}
def main_links(s):
 main=re.search(r'<main\b[^>]*>(.*?)</main>',s,re.S)[1]
 return set(re.findall(r'href="([^"?#]+/)"',main))
def main():
 hub,final=fetch(BASE+'/compare/');assert final==BASE+'/compare/' and hub==(ROOT/'public/compare/index.html').read_text()
 hub_links=main_links(hub)
 robot=urllib.robotparser.RobotFileParser();robot.parse(fetch(BASE+'/robots.txt')[0].splitlines())
 listed=[]
 for name in ['sitemap-blog.xml','sitemap-core.xml']:
  s,_=fetch(BASE+'/'+name);listed.extend(n.text for n in ET.fromstring(s).iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc'))
 records=[]
 for provider,pair in PAIRS.items():
  for route in pair:
   url=BASE+route;s,final=fetch(url)
   assert final==url and s==(ROOT/'public'/route.lstrip('/')/'index.html').read_text()
   assert re.findall(r'<link[^>]+rel="canonical"[^>]+href="([^"]+)"',s)==[url]
   assert not re.search(r'<meta[^>]+name="robots"[^>]+content="[^"]*noindex',s,re.I)
   assert robot.can_fetch('Googlebot',url) and listed.count(url)==1 and route in hub_links
   nodes=[]
   for block in re.findall(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',s,re.S):
    d=json.loads(block);nodes.extend(d.get('@graph',[d]))
   assert any(n.get('@type')=='BreadcrumbList' for n in nodes)
   links=main_links(s);other=pair[1] if route==pair[0] else pair[0]
   assert '/compare/' in links and other in links
   with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Googlebot'}),timeout=35) as response:
    assert response.status==200 and response.geturl()==url and 'noindex' not in response.headers.get('X-Robots-Tag','').lower() and response.read().decode()==s
   records.append({'provider':provider,'url':url,'http_status':200,'final_canonical_exact':True,'current_build_exact':True,'googlebot_ua_http_200':True,'robots_allowed':True,'noindex':False,'sitemap_entries':1,'breadcrumbs':True,'hub_main_link':True,'return_hub_main_link':True,'paired_owner_main_link':BASE+other})
 assert fetch(BASE+'/')[0]==(ROOT/'public/index.html').read_text()
 print(json.dumps({'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'hub_exact_current_build':True,'protected_homepage_exact':True,'records':records,'limits':'HTTP/source architecture verification, not browser rendering, a fresh provider-content review, Google crawl/indexing, rankings, search/AI summary placement or enquiries. No fresh Inspection or unchanged submissions.'},indent=2))
if __name__=='__main__':main()
