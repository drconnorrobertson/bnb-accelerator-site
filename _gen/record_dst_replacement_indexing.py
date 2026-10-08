"""Mechanical first-inspection registration, not an indexing or crawl gain."""
import csv,io,json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
b=json.loads((R/'_gen/dst-replacement-indexing-baseline-2026-10-08.json').read_text())
i=b['inspection'];h=b['history_after']['inspections'][0];url=i['inspectionUrl']
assert b['history_before']['pagination']['hasMore'] is False and b['history_after']['pagination']['hasMore'] is False
assert len(b['history_before']['inspections'])==0 and len(b['history_after']['inspections'])==1
p=R/'_gen/dst-replacement-live-evidence.json';e=json.loads(p.read_text())
e['actual_inspection']={'observed_at':h['requested_at'],'id':h['id'],**i}
e['confirmed_indexing']='First actual Inspection NEUTRAL/URL is unknown to Google; no reported crawl; unspecified robots/indexing/fetch; not a diagnosed barrier, trend or content receipt'
p.write_text(json.dumps(e,indent=2,ensure_ascii=False)+'\n')
p=R/'_gen/expansion_509_progress.json';d=json.loads(p.read_text());a=d['published']
assert len(a)==9 and d['verified_live_new_pages']==9 and len(d['separately_counted_existing_refreshes'])==73
x=next(x for x in a if x['url']==url);x['google_indexing_evidence']=e['confirmed_indexing']+'; '+h['requested_at'];x['indexing_baseline']='_gen/dst-replacement-indexing-baseline-2026-10-08.json'
p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
p=R/'_gen/blog-indexing-inventory.csv';raw=p.read_bytes();fields=next(csv.reader(io.StringIO(raw.decode())))
lines=raw.splitlines(keepends=True);count=0
for n,line in enumerate(lines):
    if line.startswith((url+',').encode()):
        row=dict(zip(fields,next(csv.reader(io.StringIO(line.decode())))))
        row.update(observed_at=h['requested_at'],indexing_verdict=i['verdict'],indexing_state=i['indexingState'],coverage_state=i['coverageState'],last_google_crawl='not reported',recommended_action='First actual Inspection10:46:27UTC URLunknown/no reportedcrawl/unspecifiedstates; not technicalcause, duplication, trend or bodyreceipt. Exactlive10:44 fiveartifacts/56links/threeinbound/Googlebot200 separate; unqueriedperformance stays unknown. Allow crawl and continue buyer-owner work; no repeated unchanged submissions.')
        out=io.StringIO();csv.DictWriter(out,fields,lineterminator='\r\n' if line.endswith(b'\r\n') else '\n').writerow(row);lines[n]=out.getvalue().encode();count+=1
assert count==1
p.write_bytes(b''.join(lines))
assert [x for x in lines if not x.startswith((url+',').encode())]==[x for x in raw.splitlines(keepends=True) if not x.startswith((url+',').encode())]
print('PASS first actual baseline; one inventory row changed; nine new/73 existing and all unrelated rows preserved')
