"""Release gates for inventory coverage, article routing and embedded sources."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json, re, sys, xml.etree.ElementTree as ET

REPO=Path(__file__).resolve().parents[1]
ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else REPO
MANIFEST=json.loads((REPO/'_gen/social-library/publication-manifest.json').read_text())
INVENTORY=json.loads((REPO/'_gen/social-library/youtube-inventory.json').read_text())
issues=[]

class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True);self.h1=0;self.frames=[];self.links=[];self.canonical=[];self.ids=set();self.json=[];self.script=None
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='h1':self.h1+=1
        if tag=='iframe':self.frames.append(a)
        if tag=='a' and 'href' in a:self.links.append(a['href'])
        if tag=='link' and a.get('rel')=='canonical':self.canonical.append(a.get('href'))
        if a.get('id'):self.ids.add(a['id'])
        if tag=='script' and a.get('type')=='application/ld+json':self.script=''
    def handle_data(self,s):
        if self.script is not None:self.script+=s
    def handle_endtag(self,tag):
        if tag=='script' and self.script is not None:
            self.json.append(json.loads(self.script));self.script=None

expected={re.search(r'(?:v=|shorts/)([\w-]{11})',x['url'])[1] for kind in ['videos','shorts','additionalVideos'] for x in INVENTORY[kind]}
actual={x['id'] for x in MANIFEST['items'] if x['platform']=='YouTube'}
if len(expected)!=816 or actual!=expected:issues.append('YouTube publication does not exactly cover the 816 collected source IDs')
routes=MANIFEST['routes']; item_routes={x['path'] for x in MANIFEST['items']}
if len(routes)!=len(set(routes)) or len(item_routes)!=len(MANIFEST['items']):issues.append('Duplicate route or post identity')
submitted={urlsplit(x.text).path for x in ET.parse(ROOT/'sitemap-content.xml').findall('.//{*}loc')}
if submitted!=set(routes):issues.append('Content sitemap differs from the complete publication manifest')
if 'https://www.bnbaccelerator.com/sitemap-content.xml' not in {x.text for x in ET.parse(ROOT/'sitemap.xml').findall('.//{*}loc')}:issues.append('Content sitemap missing from sitemap index')
all_article_links=set(); transcript_pages=0
for item in MANIFEST['items']:
    f=ROOT/item['path'].strip('/')/'index.html'
    if not f.exists():issues.append('Missing article '+item['path']);continue
    text=f.read_text();page=Page();page.feed(text)
    if page.h1!=1:issues.append('Invalid heading hierarchy '+item['path'])
    if page.canonical!=['https://www.bnbaccelerator.com'+item['path']]:issues.append('Wrong canonical '+item['path'])
    if not {'watch','companion','written-version'}.issubset(page.ids):issues.append('Missing article or source section '+item['path'])
    source_frames=[f for f in page.frames if urlsplit(f.get('src','')).hostname in ('www.youtube-nocookie.com','www.instagram.com')]
    if len(source_frames)!=1 or not source_frames[0].get('title'):issues.append('Missing accessible embed '+item['path'])
    elif item['id'] not in source_frames[0].get('src',''):issues.append('Embed does not match source identity '+item['path'])
    if item['source_url'] not in page.links:issues.append('Original source link missing '+item['path'])
    if not item['source_checked']:issues.append('Source not collected '+item['id'])
    if item['transcriptSegments']:
        transcript_pages+=1
        if 'cl-transcript-paragraph' not in text:issues.append('Missing captured written content '+item['path'])
    companion=text.split('id="companion"',1)[-1].split('</article>',1)[0]
    if len(re.findall(r'\w+',re.sub('<[^>]*>',' ',companion)))<210:issues.append('Incomplete companion '+item['path'])
    for href in page.links:
        if href.startswith('/') and not href.startswith('//'):
            u=urlsplit(href);target=ROOT/unquote(u.path).lstrip('/')
            if not(target.is_file() or (target/'index.html').is_file()):issues.append('Broken internal link '+href)
        if href.startswith('/learn/'):all_article_links.add(href)
for route in routes:
    if route in item_routes:continue
    text=(ROOT/route.strip('/')/'index.html').read_text();p=Page();p.feed(text)
    all_article_links.update(href for href in p.links if href.startswith('/learn/'))
if not item_routes.issubset(all_article_links):issues.append('Orphaned article pages')
if transcript_pages!=MANIFEST['videoTranscripts']:issues.append('Transcript count differs from manifest')
if ROOT.name=='public':
    for forbidden in ['_gen/social-library','scripts/build_social_library.py','youtube-source-capture.json']:
        if (ROOT/forbidden).exists():issues.append('Private collection record leaked '+forbidden)
if issues:
    print('\n'.join(sorted(set(issues))[:40]));raise SystemExit(str(len(issues))+' content-library errors')
print(json.dumps({'posts':len(MANIFEST['items']),'routes':len(routes),'youtubeIDs':len(actual),'videoTranscripts':transcript_pages,'internalLinks':'valid','inventoryCoverage':'exact','sitemapCoverage':'exact'}))
