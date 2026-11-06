"""Validate deployed sitemap owners after curation, never the unfiltered source archive."""
import json,re,sys,xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlsplit,unquote
ROOT=Path(sys.argv[1] if len(sys.argv)>1 else 'public')
HOST='www.bnbaccelerator.com'
errors=[];seen=set();count=0
for sitemap in sorted(ROOT.glob('sitemap-*.xml')):
    doc=ET.fromstring(sitemap.read_text())
    if doc.tag.rsplit('}',1)[-1]!='urlset':continue
    for node in doc:
        loc=next((n.text for n in node if n.tag.rsplit('}',1)[-1]=='loc'),None)
        if not loc:errors.append(f'{sitemap.name}: missing loc');continue
        u=urlsplit(loc)
        if u.scheme!='https' or u.netloc!=HOST or u.query or u.fragment:errors.append(f'Noncanonical sitemap URL: {loc}');continue
        if loc in seen:errors.append(f'Duplicate sitemap owner: {loc}')
        seen.add(loc);count+=1
        file=ROOT/unquote(u.path).strip('/')/'index.html'
        if not file.exists():errors.append(f'Missing route: {loc}');continue
        text=file.read_text()
        canon=re.findall(r'<link\b[^>]*rel=[\"\x27]canonical[\"\x27][^>]*href=[\"\x27]([^\"\x27]+)',text,re.I)
        if canon!=[loc]:errors.append(f'Canonical mismatch: {loc}: {canon}')
        if re.search(r'<meta\b(?=[^>]*name=[\"\x27]robots[\"\x27])(?=[^>]*content=[\"\x27][^\"\x27]*noindex)[^>]*>',text,re.I):errors.append(f'Noindex in sitemap: {loc}')
if not count:errors.append('Empty sitemap inventory')
for file in [ROOT/'blog/str-investing-for-business-owners/index.html',ROOT/'blog/business-working-capital-before-str-purchase/index.html']:
    text=file.read_text()
    if len(re.findall(r'<h1\b',text,re.I))!=1:errors.append(f'{file}: must have one H1')
    for schema in re.findall(r'<script\b[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',text,re.S):json.loads(schema)
    for href in re.findall(r'href=[\"\x27](/[^\"\x27]*)',text):
        p=urlsplit(href).path
        if p.startswith('//'):continue
        target=ROOT/unquote(p).lstrip('/')
        if not (target.is_file() or (target/'index.html').is_file()):errors.append(f'{file}: broken internal link {href}')
if errors:print('\n'.join(errors[:60]));raise SystemExit(f'{len(errors)} production SEO errors')
print(f'Production SEO passed: {count} sitemap owners; two business-owner pages and their internal links valid.')
