"""Mechanical one-row actual-evidence update; preserve historical live evidence."""
import csv,io
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'_gen/blog-indexing-inventory.csv'
url='https://www.bnbaccelerator.com/blog/str-partnership-structure/'
raw=p.read_bytes().decode();lines=raw.splitlines(keepends=True)
r=csv.DictReader(io.StringIO(raw));fields=r.fieldnames;row=next(x for x in r if x['url']==url)
row.update(observed_at='2026-10-08T06:07:14.387853+00:00',indexing_verdict='NEUTRAL',indexing_state='INDEXING_STATE_UNSPECIFIED',coverage_state='URL is unknown to Google',last_google_crawl='not reported',recommended_action='Actual06:07Oct8 unchanged unknown/nocrawl versusOct6T23:49 complete two-row history; no diagnosed cause/duplication or revisedreceipt/gain. Full current funding/authority/FAQ body read; existing worksheet preserved. Historical live eligibility/performance separate, no freshprobe/submissions. Evidence partnership-indexing-followup-2026-10-08.json. Allow crawl time and continue independent buyer work.')
i=next(i for i,l in enumerate(lines) if l.startswith(url+','));o=io.StringIO();w=csv.DictWriter(o,fieldnames=fields,lineterminator='\r\n' if lines[i].endswith('\r\n') else '\n');w.writerow(row);lines[i]=o.getvalue();p.write_bytes(''.join(lines).encode())
print('One actual observation updated; historical live and performance fields preserved.')
