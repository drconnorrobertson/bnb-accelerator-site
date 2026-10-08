"""Persist actual first inspection separately from serving evidence."""
import csv,io,json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
e=json.loads((R/'_gen/pacaso-indexing-baseline-2026-10-08.json').read_text());a=e['history']['inspections'][0];assert not e['history']['pagination']['hasMore'] and len(e['history']['inspections'])==1
note='First actual Inspection2026-10-08T07:39:54.627389UTC NEUTRAL/URLunknown/unspecifiedrobots-indexing-fetch/no reportedcrawl/nullagent;completehistoryzero before/oneafter/hasMorefalse. Not cause, duplication, trend, revised-content receipt or indexing gain. _gen/pacaso-indexing-baseline-2026-10-08.json'
p=R/'_gen/blog-indexing-inventory.csv';lines=p.read_bytes().decode().splitlines(keepends=True);fields=next(csv.reader([lines[0]]));n=0
for i,line in enumerate(lines[1:],1):
 d=dict(zip(fields,next(csv.reader([line]))))
 if d['url']!=a['url']:continue
 d.update(observed_at=a['requested_at'],indexing_verdict=a['verdict'],indexing_state=a['indexing_state'],coverage_state=a['coverage_state'],last_google_crawl='',recommended_action=note+' Separate07:37serving eligibility retained; allow crawl time without unchanged submissions.')
 out=io.StringIO();csv.DictWriter(out,fields,lineterminator='\n').writerow(d);lines[i]=out.getvalue();n+=1
assert n==1;p.write_bytes(''.join(lines).encode())
p=R/'_gen/expansion_509_progress.json';s=p.read_text();old='Complete filtered stored history empty before publishing; no actual indexing conclusion or exclusion diagnosis';assert s.count(old)==1;p.write_text(s.replace(old,note))
print('PASS: one actual inventory row and one evidence field; counts unchanged')
