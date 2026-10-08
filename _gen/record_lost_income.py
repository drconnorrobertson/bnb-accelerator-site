"""Mechanical registration; preserve unrelated inventory bytes and performance."""
import csv,io,json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
e=json.loads((R/'_gen/lost-income-live-evidence.json').read_text())
p=R/'_gen/expansion_509_progress.json';d=json.loads(p.read_text());a=d['separately_counted_existing_refreshes']
assert len(a)==72 and not any(x['url']==e['url'] for x in a)
a.insert(0,{'url':e['url'],'content_commit':e['content_commit'],'verified_live_at':e['verified_at'],'evidence':'_gen/lost-income-live-evidence.json','counted_toward_509':False,'improvement':'Policy-answer register, original seasonal interruption economic exposure and independently funded delayed/no-payment cash bridge; current Travelers and Proper primary sources','validation':e['validation'],'submission':e['indexnow']+'; blogXMLacceptedconfirmed10:13:11.892UTC pending/zero reportederrorswarnings','actual_google_indexing':e['confirmed_indexing']})
assert d['verified_live_new_pages']==8 and len(a)==73
p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
p=R/'_gen/blog-indexing-inventory.csv';raw=p.read_bytes();fields=next(csv.reader(io.StringIO(raw.decode())))
lines=raw.splitlines(keepends=True);count=0
for i,line in enumerate(lines):
    if line.startswith((e['url']+',').encode()):
        row=dict(zip(fields,next(csv.reader(io.StringIO(line.decode())))))
        row.update(observed_at=e['verified_at'],priority='True',indexing_verdict='unknown',indexing_state='unknown',coverage_state='No stored inspection; actual indexing unknown',last_google_crawl='not reported',http_status='200',final_url=e['url'],robots_allows_googlebot='True',source_noindex='False',live_noindex='False',source_canonical=e['url'],live_canonical=e['url'],sitemap_included='True',inbound_pages='3',topic_cluster='permissions-insurance/interruption purchase',article_text_present='True',recommended_action='Existing expansion e6ac0cb exactlive10:12:52UTC/fourartifacts/55links/3inbound/Googlebot200; actualindexingunknown emptycompletehistory, not exclusion; preserve historical performance, not queried this batch. Changedonly submissions accepted; allow crawl and measure later buyer queries.')
        out=io.StringIO();csv.DictWriter(out,fields,lineterminator='\r\n' if line.endswith(b'\r\n') else '\n').writerow(row);lines[i]=out.getvalue().encode();count+=1
assert count==1
p.write_bytes(b''.join(lines))
print('PASS 73 existing expansions/eight new509; one inventory row changed, unrelated bytes and performance preserved')
