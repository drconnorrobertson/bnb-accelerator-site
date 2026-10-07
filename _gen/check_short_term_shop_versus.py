"""Read-only scope protection and independent credited-deposit arithmetic."""
from pathlib import Path
import hashlib,re,subprocess
R=Path(__file__).resolve().parents[1]
p='compare/avery-carl-short-term-shop/index.html';s=(R/p).read_text();o=subprocess.check_output(['git','show','HEAD:'+p],cwd=R,text=True)
assert re.search(r'<h1>.*?</h1>',s)[0]==re.search(r'<h1>.*?</h1>',o)[0]
assert s.split('<main id="main">')[0].replace('"dateModified": "2026-10-07"','"dateModified": "2026-10-01"')==o.split('<main id="main">')[0]
assert s.split('</main>')[1]==o.split('</main>')[1]
assert '"datePublished": "2026-08-15"' in s and 'FAQPage' not in o and 'FAQPage' not in s
assert set(subprocess.check_output(['git','diff','--name-only'],cwd=R,text=True).splitlines())=={p,'sitemap-core.xml'}
assert hashlib.sha256((R/'index.html').read_bytes()).hexdigest()=='58db91a9ec1bd726f5d6d68052208b9153d04eecd60de82e723725e6bf2ee7e2'
assert hashlib.sha256((R/'public/index.html').read_bytes()).hexdigest()=='5a3fe67b5045fb0cfe7a6620b27e34e9149ed53cb4c6359f2aeb3ad770ce6484'
assert 200000+16000+36000+12000+40000==304000
assert 180000+16000+36000+12000+40000==284000
assert 320000-304000==16000 and 300000-284000==16000
assert 304000-(320000-20000)==4000
assert 304000-(320000-20000-1000)==5000
assert 320000-1000-304000==15000
print('PASS: two public diffs; original H1/title/publication/author/header/footer/flow/noFAQ; exact source/built home hashes; independent earnest-credit/refund-timing math')
