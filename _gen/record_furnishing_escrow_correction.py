"""Preserve one inventory row and register separate accuracy correction only."""
import csv,io,json
from pathlib import Path
R=Path(__file__).resolve().parents[1];p=R/'_gen/blog-indexing-inventory.csv';raw=p.read_bytes();lines=raw.decode().splitlines(keepends=True);fields=next(csv.reader([lines[0]]));url='https://www.bnbaccelerator.com/blog/furnishing-during-escrow/';changed=0
for i,line in enumerate(lines[1:],1):
 d=dict(zip(fields,next(csv.reader([line]))))
 if d['url']!=url:continue
 d.update(observed_at='2026-10-08T06:56:05.072046+00:00',http_status='200',final_url=url,robots_allows_googlebot='True',source_noindex='False',live_noindex='False',source_canonical=url,live_canonical=url,sitemap_included='True',inbound_pages='5',article_text_present='True',recommended_action='Accuracy correction exactlive06:56HTTP200/canonical/robots/noindex/sitemap/60links/5inbound; preserve originalAugust15publication. Actual indexing not queried and remains unknown; accepted submissions are not indexing, no diagnosed exclusion or gains')
 out=io.StringIO();csv.DictWriter(out,fields,lineterminator='\r\n' if line.endswith('\r\n') else '\n').writerow(d);lines[i]=out.getvalue();changed+=1
assert changed==1;p.write_bytes(''.join(lines).encode());print('PASS: one eligibility row updated; existing indexing and performance retained')
