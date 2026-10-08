"""Mechanical scoped evidence registration preserving unrelated CSV bytes and metrics."""
import csv,io,json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
e=json.loads((R/'_gen/str-income-housing-live-evidence.json').read_text())
p=R/'_gen/expansion_509_progress.json';d=json.loads(p.read_text());a=d['separately_counted_existing_refreshes']
record={'url':e['url'],'content_commit':e['content_commit'],'verified_live_at':e['verified_at'],'evidence':'_gen/str-income-housing-live-evidence.json','counted_toward_509':False,'improvement':'Primary-housing-payment acceptance gate, five-field lender worksheet, unresolved-file and funded-cash branches','validation':e['validation'],'submission':e['indexnow']+'; '+e['sitemap_submission'],'actual_google_indexing':e['actual_google_indexing']}
if not any(x['url']==e['url'] for x in a):
 assert len(a)==75;a.insert(0,record)
else:assert len(a)==76 and a[0]==record
assert d['verified_live_new_pages']==10 and len(a)==76;p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
p=R/'_gen/blog-indexing-inventory.csv';raw=p.read_bytes();fields=next(csv.reader(io.StringIO(raw.decode())));lines=raw.splitlines(keepends=True);count=0
for i,line in enumerate(lines):
 if line.startswith((e['url']+',').encode()):
  row=dict(zip(fields,next(csv.reader(io.StringIO(line.decode())))))
  row.update(observed_at=e['actual_google_indexing']['requested_at'],inspection_verdict='NEUTRAL',indexing_state='INDEXING_STATE_UNSPECIFIED',coverage_state='Discovered - currently not indexed',http_status='200',final_url=e['url'],robots_allows_googlebot='True',source_noindex='False',live_noindex='False',source_canonical=e['url'],live_canonical=e['url'],sitemap_included='True',inbound_pages='9',topic_cluster='finance/lender housing-payment acceptance',article_text_present='True',recommended_action='Expanded existingowner6620eb2 exactlive12:28:18/fourartifacts/57links/9inbound/Googlebot200/homeexact. ActualInspection12:27:46discovered-not-indexed/no reportedcrawl; priorOct7URLunknown/complete2rowhistory. Discovery not cause or revisedbody receipt. ThreeIndexNow200/blogXML12:28:41pending; allow crawl and measure later buyer queries; historical performance not queried.')
  row['indexing_verdict']=row.pop('inspection_verdict')
  assert not set(row)-set(fields),set(row)-set(fields)
  out=io.StringIO();csv.DictWriter(out,fields,lineterminator='\r\n' if line.endswith(b'\r\n') else '\n').writerow(row);lines[i]=out.getvalue().encode();count+=1
assert count==1;p.write_bytes(b''.join(lines));print('PASS 76 existing refreshes/10 new509; one inventory row changed; unrelated bytes and performance preserved')
