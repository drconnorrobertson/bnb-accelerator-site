"""Mechanical new-page registration after exact live evidence; prior CSV bytes preserved."""
import csv,io,json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
e=json.loads((R/'_gen/dst-replacement-live-evidence.json').read_text())
p=R/'_gen/expansion_509_progress.json';d=json.loads(p.read_text())
assert d['verified_live_new_pages']==8 and len(d['published'])==8
assert not any(x['url']==e['url'] for x in d['published'])
d['approved_candidates'].append({'slug':'dst-vs-direct-str-1031-replacement','score':{'distinct_intent':23,'imminent_buyer_relevance':28,'real_question_evidence':12,'acquisition_service_fit':18,'original_decision_support':10},'total':91,'score_basis':'Editorial, not measured search demand; six substantive neighbors and primary rulemaking/IRS/SEC review','review_brief':'_gen/dst-replacement-quality-review.md','status':'Distinct replacement acceptance and separately funded readiness guide validated and live','counted_as_published':True})
d['published'].insert(0,{'url':e['url'],'content_commit':e['content_commit'],'verified_live_at':e['verified_at'],'words':e['words'],'reading_minutes':e['reading_minutes'],'matched_faqs':4,'internal_targets_verified':56,'public_inbound_pages':3,'maximum_similarity':0.011,'validation':e['validation'],'submission_status':e['indexnow']+'; blogXMLacceptedconfirmed10:42:57.505UTC pending/zero reportederrorswarnings','google_indexing_evidence':e['confirmed_indexing'],'evidence':'_gen/dst-replacement-live-evidence.json','counted_toward_509':True})
d['verified_live_new_pages']=9
d['status']='9 of 509 additional new guides validated and live. Remaining 500 are a target, not established qualified gaps or completed pages. Existing refreshes are counted separately.'
assert len(d['published'])==9 and len(d['separately_counted_existing_refreshes'])==73
p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
p=R/'_gen/blog-indexing-inventory.csv';raw=p.read_bytes();fields=next(csv.reader(io.StringIO(raw.decode())))
assert e['url'].encode() not in raw and raw.endswith(b'\n')
row={k:'' for k in fields}
row.update(url=e['url'],observed_at=e['verified_at'],priority='True',indexing_verdict='unknown',indexing_state='unknown',coverage_state='No stored inspection; actual indexing unknown',last_google_crawl='not reported',http_status='200',final_url=e['url'],robots_allows_googlebot='True',source_noindex='False',live_noindex='False',source_canonical=e['url'],live_canonical=e['url'],sitemap_included='True',inbound_pages='3',topic_cluster='replacement-ownership/acquisition-funding',article_text_present='True',recommended_action='New c2e0b56 exactlive10:42:34UTC/fiveartifacts/56links/threeinbound; emptycompleteInspectionhistory meansunknown, not exclusion; performance not queried/unknown. Acceptedchangedsubmissions not indexing; allow crawl and collect a bounded actual baseline.')
out=io.StringIO();csv.DictWriter(out,fields,lineterminator='\r\n').writerow(row)
p.write_bytes(raw+out.getvalue().encode())
assert p.read_bytes().startswith(raw)
print('PASS nine new509/73 existing unchanged; one new inventory row appended; all prior bytes/performance preserved')
