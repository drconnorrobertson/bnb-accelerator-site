"""Mechanical actual indexing baseline update; preserve other rows and counts."""
import csv,io,json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
b=json.loads((R/'_gen/pool-slide-indexing-baseline-2026-10-08.json').read_text());i=b['after']['inspections'][0]
assert b['before']['pagination']['returned']==0 and not b['before']['pagination']['hasMore']
assert b['after']['pagination']['returned']==1 and not b['after']['pagination']['hasMore']
assert i['coverage_state']=='Discovered - currently not indexed' and i['last_crawl_time'] is None
note='First actual Inspection '+i['requested_at']+' NEUTRAL/Discovered-currently-not-indexed; unspecified robots/indexing/fetch/agent, no reported crawl. Not cause, duplication, trend, revisedbodyreceipt or gain.'
p=R/'_gen/pool-slide-live-evidence.json';e=json.loads(p.read_text());e['confirmed_indexing']=note;e['actual_google_inspection']=b['inspection'];e['inspection_evidence']='_gen/pool-slide-indexing-baseline-2026-10-08.json';p.write_text(json.dumps(e,indent=2,ensure_ascii=False)+'\n')
p=R/'_gen/expansion_509_progress.json';d=json.loads(p.read_text());a=d['separately_counted_existing_refreshes'];assert len(a)==74 and d['verified_live_new_pages']==9
matches=[x for x in a if x['url']==b['url']];assert len(matches)==1;matches[0]['actual_google_indexing']=note;p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
p=R/'_gen/blog-indexing-inventory.csv';raw=p.read_bytes();fields=next(csv.reader(io.StringIO(raw.decode())));lines=raw.splitlines(keepends=True);count=0
for n,line in enumerate(lines):
    if line.startswith((b['url']+',').encode()):
        row=dict(zip(fields,next(csv.reader(io.StringIO(line.decode())))))
        row.update(indexing_verdict=i['verdict'],indexing_state=i['indexing_state'],coverage_state=i['coverage_state'],last_google_crawl='not reported',recommended_action=note+' Exactlive11:11 and accepted submissions separate. Allow crawl; continue substantive independent buyer work. Historical performance preserved; no new live probe.')
        out=io.StringIO();csv.DictWriter(out,fields,lineterminator='\r\n' if line.endswith(b'\r\n') else '\n').writerow(row);lines[n]=out.getvalue().encode();count+=1
assert count==1;p.write_bytes(b''.join(lines))
print('PASS first actual inspection recorded; one inventory row; historical performance/other rows/counts retained')
