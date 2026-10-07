"""Read-only scoped-diff, publication, archive and arithmetic protection."""
import hashlib, json, re, subprocess
from pathlib import Path
R=Path(__file__).resolve().parents[1]
def old(p):return subprocess.check_output(['git','show','HEAD:'+p],cwd=R,text=True)
target='blog/str-property-management-fees/index.html'
s=(R/target).read_text();o=old(target)
assert re.search(r'<h1>.*?</h1>',s)[0]==re.search(r'<h1>.*?</h1>',o)[0]
assert set(re.findall(r'id="([^"]+)"',o))<=set(re.findall(r'id="([^"]+)"',s))
author=r'<div class="author-box">.*?</div>\s*</div>'
assert re.search(author,s,re.S)[0]==re.search(author,o,re.S)[0]
cards=r'<article class="post-card".*?</article>'
a=(R/'blog/index.html').read_text();b=old('blog/index.html')
unchanged=lambda x:[c for c in re.findall(cards,x,re.S) if '/blog/str-property-management-fees/' not in c]
assert unchanged(a)==unchanged(b) and len(unchanged(a))==745
assert re.sub(cards,'',a,flags=re.S)==re.sub(cards,'',b,flags=re.S)
allowed={target,'blog/index.html','blog/buy-str-high-income-large-tax-bill/index.html','sitemap-blog.xml'}
changed=set(subprocess.check_output(['git','diff','--name-only'],cwd=R,text=True).splitlines())
assert changed==allowed,changed
assert hashlib.sha256((R/'index.html').read_bytes()).hexdigest()=='58db91a9ec1bd726f5d6d68052208b9153d04eecd60de82e723725e6bf2ee7e2'
assert hashlib.sha256((R/'public/index.html').read_bytes()).hexdigest()=='5a3fe67b5045fb0cfe7a6620b27e34e9149ed53cb4c6359f2aeb3ad770ce6484'
assert 140000*.18==25200 and 140000*.20==28000
assert 25200+4200==29400 and 29400+1500==30900 and 28000+2000==30000
assert 30900-30000==900 and 29400-28000==1400
assert 1500+5*29400==148500 and 2000+5*28000==142000 and 148500-142000==6500
assert 110000*.18+4200==24000 and 110000*.20==22000
assert 249000+1500-250000==500 and 249000+2000-250000==1000
nodes=[]
for x in re.findall(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',s,re.S):
 d=json.loads(x);nodes.extend(d.get('@graph',[d]))
article=next(n for n in nodes if n.get('@type')=='BlogPosting')
assert article['datePublished']=='2026-08-11' and article['dateModified']=='2026-10-07'
print('PASS: four scoped public diffs, original H1/author/fragments/publication,745 untouched archive cards/framing, source/built home hashes and independent arithmetic')
