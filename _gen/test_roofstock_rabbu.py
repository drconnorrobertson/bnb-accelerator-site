"""Independent arithmetic, FAQ consistency and preservation."""
import hashlib,html,json,re,subprocess
from pathlib import Path
R=Path(__file__).resolve().parents[1]
assert 18000+4000+3*4000==34000 and 285000+34000==319000
assert 320000-319000==1000
assert 285000+18000+4000+6*4000==331000 and 331000-320000==11000
assert 300000+4000==304000 and 320000-304000==16000
assert 285000+4000+12000==301000 and 320000-301000==19000
p='compare/roofstock-vs-rabbu/index.html';old=subprocess.check_output(['git','show','HEAD:'+p],cwd=R,text=True);s=(R/p).read_text()
assert old.split('<main id="main">')[0].replace('"dateModified": "2026-10-06"','"dateModified": "2026-10-08"')==s.split('<main id="main">')[0]
assert old.split('</main>',1)[1]==s.split('</main>',1)[1]
assert s.count('The two linked primary pages were reviewed; unseen signed agreements were not authenticated.')==1
faqs=[]
for block in re.findall(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',s,re.S):
 d=json.loads(block)
 for n in d.get('@graph',[d]):
  if n.get('@type')=='FAQPage':faqs=n['mainEntity']
assert len(faqs)==4
for q in faqs:assert q['name'] in html.unescape(s) and q['acceptedAnswer']['text'] in html.unescape(s)
assert hashlib.sha256((R/'index.html').read_bytes()).hexdigest()=='58db91a9ec1bd726f5d6d68052208b9153d04eecd60de82e723725e6bf2ee7e2'
assert hashlib.sha256((R/'public/index.html').read_bytes()).hexdigest()=='5a3fe67b5045fb0cfe7a6620b27e34e9149ed53cb4c6359f2aeb3ad770ce6484'
print('PASS: cash arithmetic/four original FAQs/metadata and outer-flow preservation/single disclosure/protected home hashes.')
