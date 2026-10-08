"""Persist serving evidence separately from actual Google indexing."""
import csv,io,json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
e=json.loads((R/'_gen/pacaso-purchase-live-evidence.json').read_text())
p=R/'_gen/expansion_509_progress.json';d=json.loads(p.read_text());a=d['separately_counted_comparison_refreshes'];assert not any(x['url']==e['url'] for x in a)
a.insert(0,{'url':e['url'],'content_commit':e['content_commit'],'verified_at':e['verified_at'],'evidence':'_gen/pacaso-purchase-live-evidence.json','counted_toward_509':False,'validation':e['validation']+';two exact live artifacts/54 linked destinations-assets/5 inbound/Googlebot-UA200','indexnow_status':e['indexnow'],'sitemap_status':'CoreXMLacceptedconfirmed2026-10-08T07:37:44.054Zpending/zero reportederrorswarnings;not indexing','google_indexing_evidence':e['google_indexing_evidence']})
assert d['verified_live_new_pages']==8 and len(a)==17;p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
p=R/'_gen/blog-indexing-inventory.csv';raw=p.read_bytes();s=raw.decode();fields=next(csv.reader(io.StringIO(s)));assert not any(x['url']==e['url'] for x in csv.DictReader(io.StringIO(s)))
v={k:'' for k in fields};v.update(url=e['url'],observed_at=e['verified_at'],priority='True',indexing_verdict='unknown',indexing_state='unknown',coverage_state='No stored observation; not exclusion proof',http_status='200',final_url=e['url'],robots_allows_googlebot='True',source_noindex='False',live_noindex='False',source_canonical=e['url'],live_canonical=e['url'],sitemap_included='True',inbound_pages='5',topic_cluster='service-selection/ownership and rental-use',impressions='not returned',clicks='not returned',performance_start='not queried',performance_end='not queried',article_text_present='True',recommended_action='Exact live eligible; actual Google indexing unknown. Allow crawl time; no duplicate ownership-model variant or unchanged submission. Continue substantive acquisition-service gaps.')
buf=io.StringIO();csv.DictWriter(buf,fields,lineterminator='\n').writerow(v);cut=raw.index(b'\n')+1;p.write_bytes(raw[:cut]+buf.getvalue().encode()+raw[cut:])
print('PASS:17 separate comparison refreshes,8new509; one inventory insertion preserves old bytes')
