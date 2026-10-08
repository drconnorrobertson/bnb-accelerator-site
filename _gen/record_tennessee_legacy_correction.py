"""Record already observed live verification and submission results, not fresh probes."""
import csv, io, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
URL='https://www.bnbaccelerator.com/blog/tennessee-grandfathering-explained/'
COMMIT='e680ff832799fe0477fa78eca93d81a939415a81'
STAMP='2026-10-08T04:14:14.016411+00:00'
SUBMISSION='Three changed canonicals IndexNow HTTP200; blogXML accepted/confirmed 2026-10-08T04:14:28.135Z pending/zero reported errors and warnings; not confirmed indexing'
INDEXING='Unknown: complete filtered stored URL Inspection history returned zero before correction; missing history is not exclusion evidence; no actual Google crawl or indexing claim'
evidence={
 'content_commit':COMMIT,'verified_at':STAMP,'exact_changed_public_artifacts':4,
 'protected_homepage_exact':True,'independent_internal_links_assets_checked':59,
 'deployment_propagation':'Initial exact-body mismatch; single 30-second propagation retry passed',
 'records':[{'url':URL,'http_status':200,'final_url':URL,'canonical':URL,'robots_allowed':True,'noindex':False,'exact_public_build_match':True,'server_article_text':True,'publication_date':'2026-08-15','modified_date':'2026-10-08','words':1264,'matched_faqs':3,'sitemap_entries':1,'sitemap_lastmod':'2026-10-08','inbound_public_pages':4,'internal_targets':59,'googlebot_ua_http_200':True}],
 'indexnow':{'changed_urls':[URL,'https://www.bnbaccelerator.com/blog/','https://www.bnbaccelerator.com/blog/buy-str-high-income-large-tax-bill/'],'http_status':200,'meaning':'Accepted for processing, not confirmed indexing'},
 'google_sitemap':{'url':'https://www.bnbaccelerator.com/sitemap-blog.xml','accepted':True,'confirmed':True,'last_submitted':'2026-10-08T04:14:28.135Z','pending':True,'reported_errors':0,'reported_warnings':0,'meaning':'Submission confirmation, not indexing'},
 'actual_google_indexing':INDEXING,
 'limits':'Serving/eligibility checks are not actual Google crawl, browser rendering, indexing, search or conversion gains. No authenticated Vercel deployment status asserted. GA4 authenticated scope unavailable (no_scope), not zero conversions.'}
(ROOT/'_gen/tennessee-legacy-correction-live-evidence.json').write_text(json.dumps(evidence,indent=2)+'\n')
p=ROOT/'_gen/expansion_509_progress.json'; d=json.loads(p.read_text())
records=d['separately_recorded_accuracy_corrections']
assert len(records)==6 and not any(x['url']==URL for x in records)
records.insert(0,{'url':URL,'content_commit':COMMIT,'verified_live_at':STAMP,'evidence':'_gen/tennessee-legacy-correction-live-evidence.json','actual_google_indexing':INDEXING,'counted_toward_509':False,'counted_as_substantive_expansion_batch':False,'correction':'Remove unsupported cap/rate, stability, timing and mismatched wage-tax conclusions; bounded current MTAS advisory/Nashville sources, ownership-event register and hypothetical no-continuity cash branches; preserve original publication/URL/author/flow/three FAQ questions','validation':'Required checks plus RevPAR/fullfourpublicdiff/similarity0.013/745unrelatedcards/homehashes/math; four exact public artifacts/59 linked destinations-assets/4 inbound/Googlebot-UA200','submission':SUBMISSION})
assert len(records)==7
p.write_text(json.dumps(d,indent=2)+'\n')
p=ROOT/'_gen/blog-indexing-inventory.csv'
with p.open(newline='') as f:
 reader=csv.DictReader(f); fields=reader.fieldnames; rows=list(reader)
row=next(x for x in rows if x['url']==URL)
row.update({'priority':'True','http_status':'200','final_url':URL,'robots_allows_googlebot':'True','source_noindex':'False','live_noindex':'False','source_canonical':URL,'live_canonical':URL,'sitemap_included':'True','inbound_pages':'4','article_text_present':'True','probe_error':'','recommended_action':f'Accuracy correction {COMMIT}; exact independent serving evidence {STAMP}; actual indexing unknown from empty stored history, not exclusion. Next first supported URL Inspection when available; no performance gain inferred.'})
# Preserve historical observed/indexing fields and unreturned performance metrics.
raw=p.read_bytes().decode()
lines=raw.splitlines(keepends=True)
for i,line in enumerate(lines):
 if line.startswith(URL+','):
  buf=io.StringIO(); writer=csv.DictWriter(buf,fieldnames=fields,lineterminator='\r\n' if line.endswith('\r\n') else '\n')
  writer.writerow(row); lines[i]=buf.getvalue(); break
p.write_bytes(''.join(lines).encode())
completion=f'\nCompleted {COMMIT}; exact live {STAMP}: four artifacts/59 linked destinations-assets/4 inbound/1264 words/three matching FAQs/Googlebot-UA200/selfcanonical/robotsallowed/noindexabsent/singleOct8XML/homeexact. {SUBMISSION}. {INDEXING}. Seventh separate accuracy correction; eight new of509 and66existing expansions unchanged. Next substantive nonconforming-use/primary-residence owner review. ACTIVEfive-minute schedule unchanged.\n'
p=ROOT/'_gen/tennessee-legacy-correction-quality-review.md'; p.write_text(p.read_text()+completion)
p=ROOT/'_gen/investor-coverage-ledger.md'; s=p.read_text(); marker='# Investor acquisition coverage ledger\n'; p.write_text(s.replace(marker,marker+completion,1))
print('Recorded verified live correction: new8/existing66/accuracy7; actual indexing unknown; no new509 credit.')
