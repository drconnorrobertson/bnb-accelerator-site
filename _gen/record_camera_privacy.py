"""Mechanical scoped evidence registration; preserve other CSV bytes and metrics."""
import csv,io,json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
e=json.loads((R/'_gen/camera-privacy-live-evidence.json').read_text())
p=R/'_gen/expansion_509_progress.json';d=json.loads(p.read_text());a=d['separately_counted_existing_refreshes']
assert len(a)==74 and not any(x['url']==e['url'] for x in a)
a.insert(0,{'url':e['url'],'content_commit':e['content_commit'],'verified_live_at':e['verified_at'],'evidence':'_gen/camera-privacy-live-evidence.json','counted_toward_509':False,'improvement':'Current Airbnb/Vrbo distinctions, original six-field device/control acceptance register and closing-deadline scenario','validation':e['validation'],'submission':e['indexnow']+'; '+e['sitemap_submission'],'actual_google_indexing':e['confirmed_indexing']})
assert d['verified_live_new_pages']==9 and len(a)==75
p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
p=R/'_gen/blog-indexing-inventory.csv';raw=p.read_bytes();fields=next(csv.reader(io.StringIO(raw.decode())))
lines=raw.splitlines(keepends=True);count=0
for i,line in enumerate(lines):
    if line.startswith((e['url']+',').encode()):
        row=dict(zip(fields,next(csv.reader(io.StringIO(line.decode())))))
        row.update(observed_at=e['verified_at'],priority='True',http_status='200',final_url=e['url'],robots_allows_googlebot='True',source_noindex='False',live_noindex='False',source_canonical=e['url'],live_canonical=e['url'],sitemap_included='True',inbound_pages='4',topic_cluster='permissions-privacy/camera acquisition handoff',article_text_present='True',recommended_action='Existing expansion53f82ea exactlive11:33:34UTC/fourartifacts/55links/fourinbound/Googlebot200. Retained actual indexing unknown; no fresh inspection or performance query. Changedonly IndexNow accepted and blogXML11:33:50UTCpending; allow crawl and later measure buyer queries, not exclusion inference.')
        out=io.StringIO();csv.DictWriter(out,fields,lineterminator='\r\n' if line.endswith(b'\r\n') else '\n').writerow(row);lines[i]=out.getvalue().encode();count+=1
assert count==1
p.write_bytes(b''.join(lines))
print('PASS 75 existing refreshes/nine new509; one inventory row changed, unrelated bytes and indexing/performance preserved')
