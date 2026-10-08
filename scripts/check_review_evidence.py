"""Validate review source coverage, arithmetic, links and repeatable generation."""
from pathlib import Path
import csv,hashlib,json,re,subprocess,sys,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'_gen'))
from expand_review_evidence import CASES,PAGES,START,DEALS
files=[ROOT/'reviews/index.html']+[ROOT/f'reviews/{s}/index.html' for s,t,d in PAGES]+[ROOT/f'case-studies/{r["slug"]}/index.html' for r in CASES]+[ROOT/f'{s}/index.html' for s in ['case-studies','deals','wins','testimonials']]
assert len(CASES)==32 and len(DEALS)==25
before={p:hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
subprocess.run([sys.executable,str(ROOT/'_gen/expand_review_evidence.py')],check=True)
assert before=={p:hashlib.sha256(p.read_bytes()).hexdigest() for p in files},'non-idempotent generation'
for p in files:
 s=p.read_text();assert s.count(START)==1 if p not in [ROOT/f'reviews/{slug}/index.html' for slug,t,d in PAGES] else s.count('<h1>')==1
 for link in re.findall(r'href="(/[^"]*)"',s):
  path=link.split('#')[0].split('?')[0]
  if not path:continue
  target=ROOT/path.lstrip('/')
  if path.endswith('/'):target=target/'index.html'
  assert target.exists(),f'{p.relative_to(ROOT)}: broken {link}'
for slug,title,desc in PAGES:
 path=f'/reviews/{slug}/';s=(ROOT/path.strip('/')/'index.html').read_text()
 assert 'href="https://www.bnbaccelerator.com'+path+'"' in s
 assert 'index, follow' in s
 graphs=[json.loads(x) for x in re.findall(r'<script type="application/ld\+json">(.*?)</script>',s,re.S)]
 assert any(x.get('@type')=='Article' for x in graphs)
 assert not any(x.get('@type')=='AggregateRating' for x in graphs)
 csvfile=ROOT/'public/assets/review-evidence/deal-entry-fields.csv';assert csvfile.exists()
rows=list(csv.DictReader(csvfile.open()));assert len(rows)==25
for row,d in zip(rows,DEALS):assert int(row['component_sum'])==d['down']+d['closing']+d['design']
lib=(ROOT/'reviews/case-study-library/index.html').read_text()
for r in CASES:assert f'/case-studies/{r["slug"]}/' in lib
print('Review evidence passed: 8 pages, 32 cases, 25 CSV records, links, metadata, arithmetic, idempotency')
