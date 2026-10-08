from pathlib import Path
from collections import deque
import json,re,xml.etree.ElementTree as ET
from build_tracker_proformas import ROOT,load,group,DISCLAIMER,property_page
rows,excluded=load();assert len(rows)==9776 and excluded==[6528,10008]
assert group('Z_Kill - Income')=='terrible' and group('Z_Kill - Compliance')=='terrible'
assert group('Z__Sold')=='not-great' and group('01 - New Deal (Needs Review)')=='not-great'
assert group('03 - Secondary Review Complete (Ready for Video)')=='good'
source=json.loads((ROOT/'_gen/proformas/source-2026.json').read_text())
for row in source['rows']:
 for i in [0,4,5,6,12,17,18,19,20,21,22,23,24,25]:
  assert i>=len(row['values']) or row['values'][i] is None,'non-whitelisted field retained'
paths=json.loads((ROOT/'_gen/tracker-proforma-manifest.json').read_text());assert len(paths)==len(set(paths))
graph={};source_ids=set()
for path in paths:
 f=ROOT/path.strip('/')/'index.html';s=f.read_text()
 assert s.count('<h1>')==1 and DISCLAIMER in s
 assert 'href="https://www.bnbaccelerator.com'+path+'"' in s
 assert 'docs.google.com' not in s and 'file:///' not in s
 for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>',s,re.S):json.loads(b)
 graph[path]={x for x in re.findall(r'href="(/proformas/[^"]*)"',s)}
 for link in graph[path]:assert (ROOT/link.strip('/')/'index.html').exists(),link
seen=set();queue=deque(['/proformas/'])
while queue:
 p=queue.popleft()
 if p in seen:continue
 seen.add(p);queue.extend(graph.get(p,set())-seen)
assert set(paths)<=seen,'unreachable pro forma pages'
urls=[n.text for n in ET.parse(ROOT/'sitemap-proformas.xml').getroot().iter() if n.tag.endswith('loc')]
assert len(urls)==len(paths) and len(urls)==len(set(urls))
assert not (ROOT/'public/_gen/proformas/source-2026.json').exists()
print(f'PASS: {len(rows)} address pages, {len(paths)} reachable routes, source-only fields, disclaimers, classifications, canonicals, schema and sitemap')

# Verify every property has the review sections, source values and functioning contents anchors.
counts=[]
for d in rows:
 page=(ROOT/'proformas'/d['slug']/'index.html').read_text()
 for anchor in ['property-review','screening-analysis','income-explained','model-gaps','review-steps','property-faq']:
  assert page.count('id="'+anchor+'"')==1
  assert 'href="#'+anchor+'"' in page
 text=re.sub('<[^>]+>',' ',page.split('<main',1)[1].split('</main>',1)[0])
 counts.append(len(text.split()))
 assert counts[-1]>=900,(d['slug'],counts[-1])
assert property_page(rows[0])==property_page(rows[0]),'nondeterministic rendering'
print(f'PASS: long-form sections and navigation on every property; main word count {min(counts)}–{max(counts)}')
