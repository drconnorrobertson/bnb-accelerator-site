import concurrent.futures
import html
import json
import re
import sys
import urllib.request
import urllib.robotparser
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urljoin,urlsplit
from verify_published_batch import fetch,BASE

route=sys.argv[1] if len(sys.argv)>1 else '/blog/str-lender-reserve-requirements/'
marker=sys.argv[2] if len(sys.argv)>2 else '$18,000 qualification gap'
hub_marker=sys.argv[3] if len(sys.argv)>3 else 'data-lender-reserves-link'
archive_marker=sys.argv[4] if len(sys.argv)>4 else 'worked qualification-gap example'
publication=sys.argv[5] if len(sys.argv)>5 else '2026-09-23'
read_minutes=sys.argv[6] if len(sys.argv)>6 else '6'
faq_count=int(sys.argv[7]) if len(sys.argv)>7 else 0
modification=sys.argv[8] if len(sys.argv)>8 else '2026-10-06'
all_links=set()
for path,expected in [(route,marker),('/blog/buy-str-high-income-large-tax-bill/',hub_marker)]:
    url=BASE+path;s,final=fetch(url)
    assert final==url and expected in s and 'canonical" href="'+url+'"' in s and 'noindex' not in s.lower()
    data=[json.loads(x) for x in re.findall(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',s,re.S)]
    nodes=[n for x in data for n in x.get('@graph',[x])]
    article=next(x for x in nodes if x.get('@type') in ['Article','BlogPosting']);assert article['dateModified']==modification
    if path==route:
        assert article['datePublished']==publication
        faqs=[x for x in nodes if x.get('@type')=='FAQPage']
        if faq_count:
            assert len(faqs)==1 and len(faqs[0]['mainEntity'])==faq_count
            visible=re.search(r'<article class="article">(.*?)</article>',s,re.S).group(1)
            plain=' '.join(html.unescape(re.sub('<[^>]+>',' ',visible)).split())
            for item in faqs[0]['mainEntity']:assert item['name'] in plain and item['acceptedAnswer']['text'] in plain
        else:assert not faqs
    all_links.update(urljoin(url,x.split('#')[0]) for x in re.findall(r'(?:href|src)="([^"]+)"',s) if urlsplit(urljoin(url,x)).netloc==urlsplit(BASE).netloc)
    xml=ET.fromstring(fetch(BASE+'/sitemap-blog.xml')[0]);ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
    assert len([x for x in xml.findall('s:url',ns) if x.findtext('s:loc',namespaces=ns)==url])==1
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:list(pool.map(fetch,sorted(all_links)))
archive=fetch(BASE+'/blog/')[0];card=next(x for x in re.findall(r'<article class="post-card".*?</article>',archive,re.S) if route in x)
assert archive_marker in card and read_minutes+' min read' in card
url=BASE+route
with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Googlebot'}),timeout=30) as r:assert r.status==200 and 'noindex' not in r.headers.get('X-Robots-Tag','').lower() and marker in r.read().decode()
robot=urllib.robotparser.RobotFileParser();robot.parse(fetch(BASE+'/robots.txt')[0].splitlines());assert robot.can_fetch('Googlebot',url)
assert fetch(BASE+'/')[0]==Path('public/index.html').read_text()
inbound=sum(route in set(re.findall(r'href="(/blog/[^"?#]+/)"',p.read_text())) for p in Path('public').rglob('index.html'))
print(f'Both live canonicals/body/schema/sitemap/archive passed;{len(all_links)} internal targets;{inbound} inbound pages;Googlebot-UA200/robotsallowed;protected homepage exact match')
