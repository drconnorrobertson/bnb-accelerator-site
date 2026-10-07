"""Read-only scoped comparison diff and independent cash math."""
from pathlib import Path
import hashlib, re, subprocess
R=Path(__file__).resolve().parents[1]
p='compare/str-search/index.html';s=(R/p).read_text();o=subprocess.check_output(['git','show','HEAD:'+p],cwd=R,text=True)
assert re.search(r'<h1>.*?</h1>',s)[0]==re.search(r'<h1>.*?</h1>',o)[0]
assert s.split('<main id="main">')[0].replace('"dateModified": "2026-10-07"','"dateModified": "2026-10-01"')==o.split('<main id="main">')[0]
assert s.split('</main>')[1]==o.split('</main>')[1]
assert '"datePublished": "2026-10-01"' in s and '"dateModified": "2026-10-07"' in s
assert 'FAQPage' not in o and 'FAQPage' not in s
assert set(subprocess.check_output(['git','diff','--name-only'],cwd=R,text=True).splitlines())=={p,'sitemap-core.xml'}
assert hashlib.sha256((R/'index.html').read_bytes()).hexdigest()=='58db91a9ec1bd726f5d6d68052208b9153d04eecd60de82e723725e6bf2ee7e2'
assert hashlib.sha256((R/'public/index.html').read_bytes()).hexdigest()=='5a3fe67b5045fb0cfe7a6620b27e34e9149ed53cb4c6359f2aeb3ad770ce6484'
assert 220000+20000+30000+15000+45000==330000
assert 330000+8000+6000+4000==348000 and 330000+15000==345000
assert 350000-348000==2000 and 350000-345000==5000
assert 348000+6000==354000 and 345000+6000==351000
assert 354000-350000==4000 and 351000-350000==1000
print('PASS: two public diffs; original H1/title/publication/schema author/header/footer/flow; no old FAQ; exact source/built homepage hashes; independent arithmetic')
