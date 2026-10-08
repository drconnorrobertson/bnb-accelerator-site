"""Mechanical first actual inspection update, no new publication credit."""
import csv,io,json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
e=json.loads((R/'_gen/camera-privacy-indexing-baseline-2026-10-08.json').read_text());i=e['after']['inspections'][0];url=i['url']
p=R/'_gen/expansion_509_progress.json';d=json.loads(p.read_text());a=d['separately_counted_existing_refreshes'];assert len(a)==75 and d['verified_live_new_pages']==9
t=next(x for x in a if x['url']==url);t['actual_google_indexing']='First actual inspection11:35:26UTC NEUTRAL/URL unknown to Google/no reported crawl; _gen/camera-privacy-indexing-baseline-2026-10-08.json. Not technical cause or post-refresh gain.';p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
p=R/'_gen/blog-indexing-inventory.csv';raw=p.read_bytes();fields=next(csv.reader(io.StringIO(raw.decode())));lines=raw.splitlines(keepends=True);count=0
for n,line in enumerate(lines):
    if line.startswith((url+',').encode()):
        row=dict(zip(fields,next(csv.reader(io.StringIO(line.decode())))));row.update(observed_at=i['requested_at'],indexing_verdict=i['verdict'],indexing_state=i['indexing_state'],coverage_state=i['coverage_state'],last_google_crawl='not reported',recommended_action='First actual inspection11:35:26UTC URLunknown/no reportedcrawl; complete history0before/1after/hasMorefalse. Not technical exclusion cause, revisedbody receipt or trend. Exactlive11:33:34UTC/Googlebot200 and acceptedchangedonlysubmissions separate. Allow discovery/crawl; continue independent buyer-quality work and measure later, preserving performance.')
        out=io.StringIO();csv.DictWriter(out,fields,lineterminator='\r\n' if line.endswith(b'\r\n') else '\n').writerow(row);lines[n]=out.getvalue().encode();count+=1
assert count==1;p.write_bytes(b''.join(lines));print('PASS first actual inspection recorded; counts and unrelated inventory/metrics preserved')
