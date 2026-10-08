"""Mechanical evidence record; preserve actual prior indexing and other CSV bytes."""
import csv,io,json
from pathlib import Path
R=Path(__file__).resolve().parents[1];e=json.loads((R/'_gen/foreclosure-funding-live-evidence.json').read_text())
p=R/'_gen/expansion_509_progress.json';d=json.loads(p.read_text());a=d['separately_counted_existing_refreshes'];assert len(a)==76 and not any(x['url']==e['url'] for x in a)
a.insert(0,{'url':e['url'],'content_commit':e['content_commit'],'verified_live_at':e['verified_at'],'evidence':'_gen/foreclosure-funding-live-evidence.json','counted_toward_509':False,'improvement':'Six-gate sale/funding register and original bid-deadline versus financed-listing cash comparison with credited-deposit/reserve/overrun safeguards','validation':e['validation'],'submission':e['submission'],'actual_google_indexing':e['actual_google_indexing']})
assert d['verified_live_new_pages']==10 and len(a)==77;p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
p=R/'_gen/blog-indexing-inventory.csv';raw=p.read_bytes();fields=next(csv.reader(io.StringIO(raw.decode())));lines=raw.splitlines(keepends=True);count=0
for i,line in enumerate(lines):
 if line.startswith((e['url']+',').encode()):
  row=dict(zip(fields,next(csv.reader(io.StringIO(line.decode())))))
  row.update(http_status='200',final_url=e['url'],robots_allows_googlebot='True',source_noindex='False',live_noindex='False',source_canonical=e['url'],live_canonical=e['url'],sitemap_included='True',inbound_pages='6',topic_cluster='purchase/foreclosure deadline funding',article_text_present='True',recommended_action='Existingownere8c8d0c expanded/exactlive12:45:20UTC/fourartifacts/58links/6inbound/Googlebot200/homeexact. Retained actualOct7PASS/indexed withOct5crawl predating refresh;no new crawl/receipt/gain claimed. ThreeIndexNow200/blogXML12:45:45pending. Preserve visibility; later measure revised crawl and buyer queries; historical performance not queried.')
  out=io.StringIO();csv.DictWriter(out,fields,lineterminator='\r\n' if line.endswith(b'\r\n') else '\n').writerow(row);lines[i]=out.getvalue().encode();count+=1
assert count==1;p.write_bytes(b''.join(lines));print('PASS77existing/10new;one inventory row updated, indexing/performance and unrelated bytes preserved')
