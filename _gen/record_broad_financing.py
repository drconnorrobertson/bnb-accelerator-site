"""Record verified refresh separately; preserve prior inspection/performance fields."""
import csv,io,json
from pathlib import Path
R=Path(__file__).resolve().parents[1];e=json.loads((R/'_gen/broad-financing-live-evidence.json').read_text())
p=R/'_gen/expansion_509_progress.json';d=json.loads(p.read_text());a=d['separately_counted_existing_refreshes'];assert len(a)==77 and not any(x['url']==e['url'] for x in a)
a.insert(0,{'url':e['url'],'content_commit':e['content_commit'],'verified_live_at':e['verified_at'],'evidence':'_gen/broad-financing-live-evidence.json','counted_toward_509':False,'improvement':'Correct unsupported loan eligibility, pricing, portfolio and refinance claims; original actual-proposal/credited-deposit cash worksheet','validation':e['validation'],'submission':e['submission'],'actual_google_indexing':e['actual_google_indexing']})
assert d['verified_live_new_pages']==10 and len(a)==78;p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
p=R/'_gen/blog-indexing-inventory.csv';raw=p.read_bytes();fields=next(csv.reader(io.StringIO(raw.decode())));lines=raw.splitlines(keepends=True);count=0
for i,line in enumerate(lines):
 if line.startswith((e['url']+',').encode()):
  row=dict(zip(fields,next(csv.reader(io.StringIO(line.decode())))))
  row.update(http_status='200',final_url=e['url'],robots_allows_googlebot='True',source_noindex='False',live_noindex='False',source_canonical=e['url'],live_canonical=e['url'],sitemap_included='True',inbound_pages='7',topic_cluster='financing/actual loan eligibility and purchase cash',article_text_present='True',recommended_action='Existingownerd6ae618 source-corrected/exactlive13:15UTC/fourartifacts/56links/7inbound/Googlebot200/homeexact. Retained Oct6PASS/indexed withSep23crawl predating refresh; no revised crawl/gain claim. ThreeIndexNow200; new blogXMLsubmission connector error twice, earlier13:01all-publicsubmission accepted. Later retry connector/check downloads; measure buyer queries independently.')
  out=io.StringIO();csv.DictWriter(out,fields,lineterminator='\n').writerow(row);lines[i]=out.getvalue().encode();count+=1
assert count==1;p.write_bytes(b''.join(lines));print('PASS78existing/10new;one inventory row updated, prior indexing/performance preserved')
