"""Verify inventory completeness, build preservation, sitemap owners and sources."""
from pathlib import Path
from html.parser import HTMLParser
import json,re,sys,collections,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/(sys.argv[1] if len(sys.argv)>1 else 'public');errors=[]
inv=json.loads((ROOT/'_gen/social-video-inventory-2026-11-22.json').read_text());videos=inv['videos'];assert len({v['id'] for v in videos})==len(videos)
for v in videos:
 p=OUT/v['ownerPath'].strip('/')/'index.html';s=p.read_text()
 if 'data-video-id="'+v['id']+'"' not in s and '/embed/'+v['id'] not in s:errors.append('Missing video '+v['id'])
 if '/assets/video-facade.v1.js' not in s and 'data-video-id' in s:errors.append('Missing player script '+v['ownerPath'])
rows=json.loads((ROOT/'_gen/provider-content-manifest.json').read_text());assert len(rows)==300;assert len({x['provider'] for x in rows})==100;assert len({x['path'] for x in rows})==300
sources=json.loads((ROOT/'_gen/competitor-editorial-2026-11-22.json').read_text());assert len(sources)==100;assert all(v['verified'] and v['source']['status']==200 for v in sources)
submitted={n.text for f in OUT.glob('sitemap*.xml') for n in ET.parse(f).getroot().findall('.//{*}loc')}
for row in rows:
 path=row['path'];p=OUT/path.strip('/')/'index.html';s=p.read_text()
 if '<!-- provider-research:start -->' not in s:errors.append('Missing provider section '+path)
 can=re.search(r'<link\b[^>]*rel="canonical"[^>]*href="([^"]+)"',s)
 if not can or can.group(1)!='https://www.bnbaccelerator.com'+path:errors.append('Wrong canonical '+path)
 if 'https://www.bnbaccelerator.com'+path not in submitted:errors.append('Missing sitemap '+path)
 if 'noindex' in re.search(r'<meta name="robots"[^>]*>',s).group(0):errors.append('Provider noindex '+path)
 if len(re.findall(r'<h1\b',s))!=1:errors.append('H1 count '+path)
 for raw in re.findall(r'<script[^>]+type="application/ld\+json"[^>]*>(.*?)</script>',s,re.S):
  try:json.loads(raw)
  except Exception:errors.append('Invalid schema '+path)
 for href in re.findall(r'href="(/[^"?#]*)',s):
  if href.endswith('/') and not (OUT/href.strip('/')/'index.html').exists():errors.append('Broken link '+path+' '+href)
assert not errors,'\n'.join(errors[:100])
print(json.dumps({'youtubeVideosEmbedded':len(videos),'videoOwnerPages':inv['coverage']['ownerPages'],'providerGuides':len(rows),'providers':len(sources),'failures':0}))
