"""Mechanical actual-indexing evidence update, preserving unrelated CSV bytes."""
import csv,io,json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
f='_gen/coastal-capex-indexing-baseline-2026-10-08.json'
e=json.loads((R/f).read_text());n=e['stored_history']['inspections'][0];url=n['url']
note='First actual Inspection2026-10-08T09:25:34.070758UTC NEUTRAL/Discovered-currently-not-indexed/unspecified robots-indexing-fetch-agent/no reportedcrawl;completehistoryzero before/oneafter/hasMorefalse. Discovery baseline not cause, trend, revised-body receipt or gain. '+f+' Separate09:21serving eligibility/09:22submissions retained; allow crawl time without unchanged submissions.'
p=R/'_gen/blog-indexing-inventory.csv';raw=p.read_bytes();lines=raw.splitlines(keepends=True);fields=next(csv.reader(io.StringIO(lines[0].decode())));count=0
for i,line in enumerate(lines):
 if line.startswith((url+',').encode()):
  row=dict(zip(fields,next(csv.reader(io.StringIO(line.decode())))))
  row.update(observed_at=n['requested_at'],indexing_verdict=n['verdict'],indexing_state=n['indexing_state'],coverage_state=n['coverage_state'],last_google_crawl='not reported',recommended_action=note)
  b=io.StringIO();csv.DictWriter(b,fields,lineterminator='\r\n' if line.endswith(b'\r\n') else '\n').writerow(row);lines[i]=b.getvalue().encode();count+=1
assert count==1;p.write_bytes(b''.join(lines))
p=R/'_gen/expansion_509_progress.json';d=json.loads(p.read_text());a=next(x for x in d['separately_counted_existing_refreshes'] if x['url']==url);a['actual_google_indexing']=note;a['indexing_baseline']=f
assert d['verified_live_new_pages']==8 and len(d['separately_counted_existing_refreshes'])==71
p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
p=R/'_gen/coastal-capex-live-evidence.json';d=json.loads(p.read_text());d['google_indexing_evidence']=note;p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
print('PASS actual discovery baseline;71 existing/eight new unchanged;unrelated inventory bytes preserved')
