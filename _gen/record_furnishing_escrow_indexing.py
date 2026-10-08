"""Update actual inspection evidence without replacing serving/performance history."""
import csv,io
from pathlib import Path
R=Path(__file__).resolve().parents[1];p=R/'_gen/blog-indexing-inventory.csv';raw=p.read_bytes();lines=raw.decode().splitlines(keepends=True);fields=next(csv.reader([lines[0]]));url='https://www.bnbaccelerator.com/blog/furnishing-during-escrow/';count=0
for i,line in enumerate(lines[1:],1):
 d=dict(zip(fields,next(csv.reader([line]))))
 if d['url']!=url:continue
 d.update(observed_at='2026-10-08T06:57:56.251713+00:00',indexing_verdict='NEUTRAL',indexing_state='INDEXING_STATE_UNSPECIFIED',coverage_state='URL is unknown to Google',last_google_crawl='',recommended_action='First actual06:57InspectionURLunknown/no reportedcrawl; not cause, duplication, trend or revised-body receipt. Separate06:56exact servingHTTP200/canonical/robots/noindex/sitemap/60links/5inbound and accepted submissions retained; allow crawl time without unchanged submissions')
 out=io.StringIO();csv.DictWriter(out,fields,lineterminator='\r\n' if line.endswith('\r\n') else '\n').writerow(d);lines[i]=out.getvalue();count+=1
assert count==1;p.write_bytes(''.join(lines).encode())
p=R/'_gen/expansion_509_progress.json';s=p.read_text();old='Not queried this run; unknown actual indexing/crawl preserved separately from fresh serving eligibility';new='First actual Inspection2026-10-08T06:57:56.251713UTC NEUTRAL/URLunknown/unspecifiedrobots-indexing-fetch/no reportedcrawl; completehistoryzero before/oneafter/hasMorefalse. Not a diagnosed cause, trend or revised-body receipt. _gen/furnishing-escrow-indexing-baseline-2026-10-08.json';assert s.count(old)==1;p.write_text(s.replace(old,new))
print('PASS: one inventory row and one separate correction evidence field; counts unchanged')
