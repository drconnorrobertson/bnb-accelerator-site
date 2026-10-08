"""Update one inventory row without rewriting unrelated evidence."""
import csv,io
from pathlib import Path
R=Path(__file__).resolve().parents[1];p=R/'_gen/blog-indexing-inventory.csv';raw=p.read_bytes();lines=raw.decode().splitlines(keepends=True);fields=next(csv.reader([lines[0]]));url='https://www.bnbaccelerator.com/blog/bnb-accelerator-vs-str-insights-buyer/';changed=0
for i,line in enumerate(lines[1:],1):
 d=dict(zip(fields,next(csv.reader([line]))))
 if d['url']!=url:continue
 d.update(observed_at='2026-10-08T06:44:49.631639+00:00',coverage_state='URL is unknown to Google',indexing_verdict='NEUTRAL',indexing_state='INDEXING_STATE_UNSPECIFIED',last_google_crawl='',inbound_pages='16',recommended_action='Actual06:44InspectionURLunknown/nocrawl versus Oct7discovered-not-indexed/nocrawl; not loss of indexing, trend or cause. Independent06:45eligibilityHTTP200/canonical/robots/noindex/sitemap/64links/16inbound; no revised crawl/receipt or gains. Allow crawl time, preserve owner and avoid unchanged submissions')
 out=io.StringIO();csv.DictWriter(out,fields,lineterminator='\r\n' if line.endswith('\r\n') else '\n').writerow(d);lines[i]=out.getvalue();changed+=1
assert changed==1;p.write_bytes(''.join(lines).encode());print('PASS: one actual evidence row updated; unrelated rows preserved')
