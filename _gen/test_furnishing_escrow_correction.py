"""Independent math, preservation, schema and archive checks."""
import hashlib,html,json,re,subprocess
from pathlib import Path
R=Path(__file__).resolve().parents[1];slug='furnishing-during-escrow'
assert 30000-9000==21000 and 9000-7500==1500
assert 3*250==750 and 30000+750==30750 and 30750-9000==21750
assert 280000-268000==12000 and 280000-9000==271000 and 268000-9000==259000
assert 271000-259000==12000 and 259000+750==259750 and 271000-259750==11250
old=subprocess.check_output(['git','show','HEAD:blog/index.html'],cwd=R,text=True);new=(R/'blog/index.html').read_text()
cards=lambda s:[x for x in re.findall(r'<article class="post-card".*?</article>',s,re.S) if '/blog/'+slug+'/' not in x]
assert cards(old)==cards(new) and len(cards(new))==745
p='blog/'+slug+'/index.html';old=subprocess.check_output(['git','show','HEAD:'+p],cwd=R,text=True);s=(R/p).read_text()
assert old.split('</article>',1)[1]==s.split('</article>',1)[1]
assert re.search(r'<header class="site-header">.*?</header>',old,re.S)[0]==re.search(r'<header class="site-header">.*?</header>',s,re.S)[0]
assert re.search(r'<div class="author-box">.*?</div>\s*</div>',old,re.S)[0]==re.search(r'<div class="author-box">.*?</div>\s*</div>',s,re.S)[0]
assert re.findall(r'<title>.*?</title>|<h1>.*?</h1>',old)==re.findall(r'<title>.*?</title>|<h1>.*?</h1>',s)
for b in re.findall(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',s,re.S):
 d=json.loads(b)
 if d.get('@type')=='FAQPage':
  assert len(d['mainEntity'])==3
  for q in d['mainEntity']:assert q['name'] in html.unescape(s) and q['acceptedAnswer']['text'] in html.unescape(s)
assert hashlib.sha256((R/'index.html').read_bytes()).hexdigest()=='58db91a9ec1bd726f5d6d68052208b9153d04eecd60de82e723725e6bf2ee7e2'
assert hashlib.sha256((R/'public/index.html').read_bytes()).hexdigest()=='5a3fe67b5045fb0cfe7a6620b27e34e9149ed53cb4c6359f2aeb3ad770ce6484'
print('PASS: hypothetical cash, 745 other archive cards, three FAQ answers, title/H1/author/outer flow and protected home hashes')
