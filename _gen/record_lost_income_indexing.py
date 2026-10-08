"""Mechanical actual-inspection evidence update; preserve unrelated rows."""
import csv,io,json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
b=json.loads((R/'_gen/lost-income-indexing-baseline-2026-10-08.json').read_text())
i=b['inspection'];h=b['after']['inspections'][0];url=i['inspectionUrl']
assert b['before']['pagination']['hasMore'] is False and b['after']['pagination']['hasMore'] is False
assert len(b['before']['inspections'])==0 and len(b['after']['inspections'])==1
p=R/'_gen/lost-income-live-evidence.json';e=json.loads(p.read_text())
e['actual_inspection']={'observed_at':h['requested_at'],'id':h['id'],**i}
e['confirmed_indexing']='First actual Inspection: Discovered - currently not indexed; no reported Google crawl; not a diagnosed barrier or revised-body receipt'
p.write_text(json.dumps(e,indent=2,ensure_ascii=False)+'\n')
p=R/'_gen/expansion_509_progress.json';d=json.loads(p.read_text());a=d['separately_counted_existing_refreshes']
assert len(a)==73 and d['verified_live_new_pages']==8
x=next(x for x in a if x['url']==url);x['actual_google_indexing']=e['confirmed_indexing']+'; '+h['requested_at']
p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
p=R/'_gen/blog-indexing-inventory.csv';raw=p.read_bytes();fields=next(csv.reader(io.StringIO(raw.decode())))
lines=raw.splitlines(keepends=True);count=0
for n,line in enumerate(lines):
    if line.startswith((url+',').encode()):
        row=dict(zip(fields,next(csv.reader(io.StringIO(line.decode())))))
        row.update(observed_at=h['requested_at'],indexing_verdict=i['verdict'],indexing_state=i['indexingState'],coverage_state=i['coverageState'],last_google_crawl='not reported',recommended_action='FirstactualInspection10:15:22UTC discovered-currently-not-indexed/no reportedcrawl/unspecifiedstates; not technicalcause, duplication, trend or revisedbodyreceipt. Exactlive10:12 fourartifacts/55links/3inbound/Googlebot200 separate; historicalperformance preserved. Allow crawl; continue buyer-owner work, no repeated unchanged submissions.')
        out=io.StringIO();csv.DictWriter(out,fields,lineterminator='\r\n' if line.endswith(b'\r\n') else '\n').writerow(row);lines[n]=out.getvalue().encode();count+=1
assert count==1
p.write_bytes(b''.join(lines))
print('PASS first actual baseline; one inventory row,73 existing/eight new counts preserved')
