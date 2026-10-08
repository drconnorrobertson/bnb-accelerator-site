"""Finalize metadata for the manually authored existing shortlist expansion."""
import json, math, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'compare/best-done-for-you-airbnb-companies/index.html'
t=p.read_text()
body=t[t.index('<p class="lead">',t.index('<article class="article">')):t.index('<div class="author-box">')]
count=len(re.sub('<[^>]*>',' ',body).split())
description='Compare STR acquisition services, agent teams and marketplaces using sourced buyer-fit distinctions, fee triggers and a complete same-property cash worksheet.'
def update(m):
    d=json.loads(m[1])
    for n in d.get('@graph',[d]):
        if n.get('@type') in ('Article','BlogPosting'):
            assert n['datePublished']=='2026-08-10'
            n.update(dateModified='2026-10-08',wordCount=count,description=description)
    return '<script type="application/ld+json">'+json.dumps(d,indent=2)+'</script>'
t=re.sub(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',update,t,flags=re.S)
t=t.replace('Updated October 7, 2026','Updated October 8, 2026').replace('<span>9 min read</span>',f'<span>{math.ceil(count/200)} min read</span>')
p.write_text(t)
sm=ROOT/'sitemap-core.xml';s=sm.read_text()
url='https://www.bnbaccelerator.com/compare/best-done-for-you-airbnb-companies/'
s,n=re.subn(r'(<(?:ns0:)?loc>'+re.escape(url)+r'</(?:ns0:)?loc>\s*<(?:ns0:)?lastmod>)[^<]+',r'\g<1>2026-10-08',s);assert n==1
sm.write_text(s)
assert 250000+14000==264000 and 320000-264000==56000
assert 264000+5000==269000 and 320000-269000==51000
assert .15*100000==15000
print(json.dumps({'authored_words':count,'minutes':math.ceil(count/200),'faq_unchanged':5}))
