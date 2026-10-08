"""Persist observed live checks/submissions, not a new probe."""
import csv,io,json
from pathlib import Path
R=Path(__file__).resolve().parents[1]/'_gen'
U='https://www.bnbaccelerator.com/blog/primary-residence-str-rule/'
C='810edf77a3bf1f6a6011023ea89a86eb898982b6'
T='2026-10-08T04:34:47.088541+00:00'
I='Prior actual04:21:27.525196UTC NEUTRAL/Discovered-currently-not-indexed/no reportedcrawl; not revised-body receipt, trend or diagnosed cause'
S='Three changed canonicals IndexNowHTTP200;blogXML2026-10-08T04:35:02.393Zacceptedconfirmedpending/zero reportederrorswarnings;not confirmed indexing'
e={'content_commit':C,'verified_at':T,'exact_changed_public_artifacts':4,'protected_homepage_exact':True,'independent_internal_links_assets_checked':56,'deployment_propagation':'Initial exact-body mismatch; single30second propagation retry passed','records':[{'url':U,'http_status':200,'final_url':U,'canonical':U,'robots_allowed':True,'noindex':False,'exact_public_build_match':True,'server_article_text':True,'publication_date':'2026-09-23','modified_date':'2026-10-08','words':1416,'matched_faqs':4,'sitemap_entries':1,'sitemap_lastmod':'2026-10-08','inbound_public_pages':4,'internal_targets':56,'googlebot_ua_http_200':True}],'indexnow':{'changed_urls':[U,'https://www.bnbaccelerator.com/blog/','https://www.bnbaccelerator.com/blog/buy-str-high-income-large-tax-bill/'],'http_status':200,'meaning':'Accepted for processing, not indexing'},'google_sitemap':{'url':'https://www.bnbaccelerator.com/sitemap-blog.xml','accepted':True,'confirmed':True,'last_submitted':'2026-10-08T04:35:02.393Z','pending':True,'reported_errors':0,'reported_warnings':0},'actual_google_indexing':I,'indexing_baseline':'_gen/primary-residence-indexing-baseline-2026-10-08.json','limits':'Independent serving/eligibility checks are not actual Google crawl, browser rendering, indexing or search/conversion gains; no authenticated Vercel deployment status asserted.'}
(R/'primary-residence-purchase-live-evidence.json').write_text(json.dumps(e,indent=2)+'\n')
p=R/'expansion_509_progress.json';raw=p.read_text();d=json.loads(raw);a=d['separately_counted_existing_refreshes'];assert len(a)==66 and not any(x['url']==U for x in a)
entry={'url':U,'content_commit':C,'verified_live_at':T,'evidence':'_gen/primary-residence-purchase-live-evidence.json','indexing_baseline':'_gen/primary-residence-indexing-baseline-2026-10-08.json','actual_google_indexing':I,'counted_toward_509':False,'improvement':'Five-field actual-residency evidence register, calendar-versus-entitlement worksheet and original residence-based/investment purchase-cash comparison with bounded current Nashville primary material','validation':'Required checks plus RevPAR/fullfourpublicdiff/745othercards/math/homehashes/similarity0.013;exactfourartifacts/56links/4inbound/fourmatchedFAQs/GooglebotUA200','submission':S}
# Insert only the new record; preserve original formatting/Unicode and all existing records.
needle='"separately_counted_existing_refreshes": ['
assert raw.count(needle)==1
block=json.dumps(entry,indent=2).splitlines();formatted='\n'.join('    '+x for x in block)
raw=raw.replace(needle,needle+'\n'+formatted+',',1);new=json.loads(raw)
assert new['separately_counted_existing_refreshes'][1:]==a and new['verified_live_new_pages']==8
p.write_text(raw)
p=R/'blog-indexing-inventory.csv';raw=p.read_bytes().decode();lines=raw.splitlines(keepends=True);reader=csv.DictReader(io.StringIO(raw));fields=reader.fieldnames;row=next(x for x in reader if x['url']==U)
row.update(http_status='200',final_url=U,robots_allows_googlebot='True',source_noindex='False',live_noindex='False',source_canonical=U,live_canonical=U,sitemap_included='True',inbound_pages='4',article_text_present='True',probe_error='',recommended_action=f'Existing expansion {C} exactlive {T}/fourartifacts/56links/4inbound. Prior actual04:21discovered/no reportedcrawl retained, not revisedreceipt or cause; changedonly submissions accepted not indexing. Measure later crawl and buyer queries.')
i=next(i for i,l in enumerate(lines) if l.startswith(U+','));b=io.StringIO();w=csv.DictWriter(b,fieldnames=fields,lineterminator='\r\n' if lines[i].endswith('\r\n') else '\n');w.writerow(row);lines[i]=b.getvalue();p.write_bytes(''.join(lines).encode())
completion=f'\nCompleted{C} exactlive{T} afterone30second propagation retry:fourartifacts/56links-assets/4inbound/1416words/fourmatchedFAQs/GooglebotUA200/selfcanonical/robotsallowed/noindexabsent/singleOct8XML/homeexact. {S}. {I}. Existingrefresh67/eightnewof509/sevenaccuracy; comparison15/resource7 unchanged. Content-creation skill shaped buyer-first evidence and comparison. Next substantive nonconforming-use and qualified long-tail comparison gaps; ACTIVEfive-minute schedule preserved.\n'
for name in ['primary-residence-purchase-quality-review.md','investor-coverage-ledger.md']:
 p=R/name;s=p.read_text();p.write_text(s+completion if name.startswith('primary') else s.replace('# Investor acquisition coverage ledger\n','# Investor acquisition coverage ledger\n'+completion,1))
print('Recorded existingrefresh67/new8/sevenaccuracy; actual Inspection unchanged, no new509 credit.')
