import concurrent.futures
import json
import re
import urllib.request
import urllib.robotparser
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urljoin, urlsplit
from verify_published_batch import fetch, BASE

route='/blog/reading-a-dscr-term-sheet/'
url=BASE+route
s,final=fetch(url)
assert final==url and '$86,867' in s and '$221,000' in s
assert 'canonical" href="'+url+'"' in s and 'noindex' not in s.lower()
data=[json.loads(x) for x in re.findall(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',s,re.S)]
article=next(x for x in data if x.get('@type')=='Article')
assert article['datePublished']=='2026-08-15' and article['dateModified']=='2026-10-06'
faq=next(x for x in data if x.get('@type')=='FAQPage')
for q in faq['mainEntity']:assert q['name'] in s and q['acceptedAnswer']['text'] in s
xml=ET.fromstring(fetch(BASE+'/sitemap-blog.xml')[0]);ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
entries=[x for x in xml.findall('s:url',ns) if x.findtext('s:loc',namespaces=ns)==url]
assert len(entries)==1 and entries[0].findtext('s:lastmod',namespaces=ns)=='2026-10-06'
archive=fetch(BASE+'/blog/')[0]
card=next(x for x in re.findall(r'<article class="post-card".*?</article>',archive,re.S) if route in x)
assert 'DSCR Term Sheet: Compare Loans Before Buying an STR' in card and 'two-year payoff worksheet' in card
links={urljoin(url,x.split('#')[0]) for x in re.findall(r'(?:href|src)="([^"]+)"',s) if urlsplit(urljoin(url,x)).netloc==urlsplit(BASE).netloc}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:list(pool.map(fetch,sorted(links)))
req=urllib.request.Request(url,headers={'User-Agent':'Googlebot'})
with urllib.request.urlopen(req,timeout=30) as r:assert r.status==200 and 'noindex' not in r.headers.get('X-Robots-Tag','').lower() and '$86,867' in r.read().decode()
robot=urllib.robotparser.RobotFileParser();robot.parse(fetch(BASE+'/robots.txt')[0].splitlines());assert robot.can_fetch('Googlebot',url)
assert fetch(BASE+'/')[0]==Path('public/index.html').read_text()
inbound=sum(route in set(re.findall(r'href="(/blog/[^"?#]+/)"',p.read_text())) for p in Path('public').rglob('index.html'))
print(f'Live canonical/body/Article/FAQ/archive/sitemap verified; {len(links)} internal targets; {inbound} inbound pages; Googlebot-UA 200 and robots allowed; exact protected homepage match')
