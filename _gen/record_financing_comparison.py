"""Mechanical evidence/register update, preserving unrelated inventory bytes."""
import csv,io,json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
e=json.loads((R/'_gen/financing-comparison-live-evidence.json').read_text())
p=R/'_gen/expansion_509_progress.json';d=json.loads(p.read_text());a=d['separately_counted_comparison_refreshes']
assert not any(x['url']==e['url'] for x in a)
a.insert(0,{'url':e['url'],'content_commit':e['content_commit'],'hub_commit':e['hub_commit'],'verified_at':e['verified_at'],'evidence':'_gen/financing-comparison-live-evidence.json','counted_toward_509':False,'validation':e['validation'],'indexnow_status':e['indexnow'],'sitemap_status':'CoreXMLacceptedconfirmed2026-10-08T08:45:36.519Zpending/zero reportederrorswarnings;not indexing','google_indexing_evidence':e['google_indexing_evidence']})
assert d['verified_live_new_pages']==8 and len(a)==18
p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
p=R/'_gen/blog-indexing-inventory.csv';raw=p.read_bytes();s=raw.decode();fields=next(csv.reader(io.StringIO(s)))
assert not any(x['url']==e['url'] for x in csv.DictReader(io.StringIO(s)))
v={k:'' for k in fields};v.update(url=e['url'],observed_at=e['verified_at'],priority='True',indexing_verdict='unknown',indexing_state='unknown',coverage_state='Actual indexing not inspected in batch; settled impressions separate from refreshed-body receipt',http_status='200',final_url=e['url'],robots_allows_googlebot='True',source_noindex='False',live_noindex='False',source_canonical=e['url'],live_canonical=e['url'],sitemap_included='True',inbound_pages='6',topic_cluster='capital-funding/financing path selection',impressions='42',clicks='0',performance_start='2026-09-08',performance_end='2026-10-05',article_text_present='True',recommended_action='Exact live eligible; allow crawl and measure settled buyer queries after refresh; current actual indexing unknown. No unchanged repeat submissions or duplicate financing variant.')
buf=io.StringIO();csv.DictWriter(buf,fields,lineterminator='\n').writerow(v);cut=raw.index(b'\n')+1;p.write_bytes(raw[:cut]+buf.getvalue().encode()+raw[cut:])
print('PASS:18 separate comparison refreshes/8new509; one inventory insertion preserves old bytes')
