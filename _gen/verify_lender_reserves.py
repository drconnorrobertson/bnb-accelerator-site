import concurrent.futures
import json
import re
import urllib.request
import urllib.robotparser
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urljoin,urlsplit
from verify_published_batch import fetch,BASE

route='/blog/str-lender-reserve-requirements/'
all_links=set()
for path,marker in [(route,'$18,000 qualification gap'),('/blog/buy-str-high-income-large-tax-bill/','data-lender-reserves-link')]:
    url=BASE+path;s,final=fetch(url)
    assert final==url and marker in s and 'canonical" href="'+url+'"' in s and 'noindex' not in s.lower()
    data=[json.loads(x) for x in re.findall(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',s,re.S)]
    article=next(x for x in data if x.get('@type')=='Article');assert article['dateModified']=='2026-10-06'
    if path==route:assert article['datePublished']=='2026-09-23' and not any(x.get('@type')=='FAQPage' for x in data)
    all_links.update(urljoin(url,x.split('#')[0]) for x in re.findall(r'(?:href|src)="([^"]+)"',s) if urlsplit(urljoin(url,x)).netloc==urlsplit(BASE).netloc)
    xml=ET.fromstring(fetch(BASE+'/sitemap-blog.xml')[0]);ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
    assert len([x for x in xml.findall('s:url',ns) if x.findtext('s:loc',namespaces=ns)==url])==1
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:list(pool.map(fetch,sorted(all_links)))
archive=fetch(BASE+'/blog/')[0];card=next(x for x in re.findall(r'<article class="post-card".*?</article>',archive,re.S) if route in x)
assert 'worked qualification-gap example' in card and '6 min read' in card
url=BASE+route
with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Googlebot'}),timeout=30) as r:assert r.status==200 and 'noindex' not in r.headers.get('X-Robots-Tag','').lower() and '$18,000 qualification gap' in r.read().decode()
robot=urllib.robotparser.RobotFileParser();robot.parse(fetch(BASE+'/robots.txt')[0].splitlines());assert robot.can_fetch('Googlebot',url)
assert fetch(BASE+'/')[0]==Path('public/index.html').read_text()
inbound=sum(route in set(re.findall(r'href="(/blog/[^"?#]+/)"',p.read_text())) for p in Path('public').rglob('index.html'))
print(f'Both live canonicals/body/schema/sitemap/archive passed;{len(all_links)} internal targets;{inbound} inbound pages;Googlebot-UA200/robotsallowed;protected homepage exact match')
