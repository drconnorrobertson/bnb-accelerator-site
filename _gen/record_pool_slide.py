"""Mechanical scoped evidence registration, preserving unrelated CSV bytes."""
import csv,io,json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
e=json.loads((R/'_gen/pool-slide-live-evidence.json').read_text())
p=R/'_gen/expansion_509_progress.json';d=json.loads(p.read_text());a=d['separately_counted_existing_refreshes']
assert len(a)==73 and not any(x['url']==e['url'] for x in a)
a.insert(0,{'url':e['url'],'content_commit':e['content_commit'],'verified_live_at':e['verified_at'],'evidence':'_gen/pool-slide-live-evidence.json','counted_toward_509':False,'improvement':'Equipment-specific acceptance register, bounded CPSC/Proper primary references, corrected coverage implication and original funded keep/remove/delay branches','validation':e['validation'],'submission':e['indexnow']+'; blog XML11:11:58.724UTC accepted confirmed pending/zero reported errors warnings','actual_google_indexing':e['confirmed_indexing']})
assert d['verified_live_new_pages']==9 and len(a)==74
p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
p=R/'_gen/blog-indexing-inventory.csv';raw=p.read_bytes();fields=next(csv.reader(io.StringIO(raw.decode())))
lines=raw.splitlines(keepends=True);count=0
for i,line in enumerate(lines):
    if line.startswith((e['url']+',').encode()):
        row=dict(zip(fields,next(csv.reader(io.StringIO(line.decode())))))
        row.update(observed_at=e['verified_at'],priority='True',indexing_verdict='unknown',indexing_state='unknown',coverage_state='No stored inspection; actual indexing unknown',last_google_crawl='not reported',http_status='200',final_url=e['url'],robots_allows_googlebot='True',source_noindex='False',live_noindex='False',source_canonical=e['url'],live_canonical=e['url'],sitemap_included='True',inbound_pages='3',topic_cluster='permissions-insurance/pool equipment purchase',article_text_present='True',recommended_action='Existing expansion ee5b3d9 exactlive11:11:39UTC/fourartifacts/55links/threeinbound/Googlebot200. Actualindexingunknown emptycompletehistory, not exclusion. Performance preserved, not queried this batch. Changedonly submissions accepted; allow crawl and measure later buyer queries.')
        out=io.StringIO();csv.DictWriter(out,fields,lineterminator='\r\n' if line.endswith(b'\r\n') else '\n').writerow(row);lines[i]=out.getvalue().encode();count+=1
assert count==1
p.write_bytes(b''.join(lines))
print('PASS 74 existing refreshes/nine new509; one inventory row changed, unrelated bytes and performance preserved')
