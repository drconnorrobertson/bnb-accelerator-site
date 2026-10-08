"""Mechanical progress/inventory update only after saved exact-live evidence."""
import csv,io,json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
e=json.loads((R/'_gen/improvement-exchange-live-evidence.json').read_text())
p=R/'_gen/expansion_509_progress.json';d=json.loads(p.read_text())
assert d['verified_live_new_pages']==9 and len(d['published'])==9
assert not any(x['url']==e['url'] for x in d['published'])
d['approved_candidates'].append({'slug':'improvement-1031-vs-completed-str-purchase','score':{'distinct_intent':23,'imminent_buyer_relevance':28,'real_question_evidence':12,'acquisition_service_fit':18,'original_decision_support':10},'total':91,'score_basis':'Editorial, not measured demand; substantive neighbor and primary produced-property/ownership review','review_brief':'_gen/improvement-exchange-quality-review.md','status':'Receipt evidence, three dates and separately funded work guide validated and live','counted_as_published':True})
d['published'].insert(0,{'url':e['url'],'content_commit':e['content_commit'],'verified_live_at':e['verified_at'],'words':e['words'],'reading_minutes':e['reading_minutes'],'matched_faqs':4,'internal_targets_verified':e['live_links_assets'],'public_inbound_pages':len(e['inbound_pages']),'maximum_similarity':0.017,'validation':e['validation'],'submission_status':e['submission_status'],'google_indexing_evidence':e['confirmed_indexing'],'evidence':'_gen/improvement-exchange-live-evidence.json','counted_toward_509':True})
d['verified_live_new_pages']=10
d['status']='10 of 509 additional new guides validated and live. Remaining499 are a target, not established qualified gaps or completed pages. Existing refreshes are counted separately.'
assert len(d['published'])==10 and len(d['separately_counted_existing_refreshes'])==75
p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
p=R/'_gen/blog-indexing-inventory.csv';raw=p.read_bytes();fields=next(csv.reader(io.StringIO(raw.decode())))
assert e['url'].encode() not in raw and raw.endswith(b'\n')
row={k:'' for k in fields}
row.update(url=e['url'],observed_at=e['verified_at'],priority='True',indexing_verdict='unknown',indexing_state='unknown',coverage_state='Actual indexing unknown; eligibility is not confirmation',last_google_crawl='not reported',http_status='200',final_url=e['url'],robots_allows_googlebot='True',source_noindex='False',live_noindex='False',source_canonical=e['url'],live_canonical=e['url'],sitemap_included='True',inbound_pages=str(len(e['inbound_pages'])),topic_cluster='produced-replacement/receipt/acquisition-readiness',article_text_present='True',recommended_action='New b388109 exact live five artifacts and all linked internal targets; accepted changed submissions not indexing; allow crawl and collect bounded actual baseline. Performance not queried/unknown.')
out=io.StringIO();csv.DictWriter(out,fields,lineterminator='\r\n').writerow(row)
p.write_bytes(raw+out.getvalue().encode());assert p.read_bytes().startswith(raw)
print('PASS10new509/75existingunchanged; one inventory row; all prior CSV bytes/performance preserved')
