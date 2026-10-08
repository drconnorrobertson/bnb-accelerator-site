"""Mechanically update one CSV row, preserving actual inspection time."""
import csv,io
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'_gen/blog-indexing-inventory.csv'
url='https://www.bnbaccelerator.com/blog/cleaning-fees-gross-revenue/'
raw=p.read_bytes().decode();lines=raw.splitlines(keepends=True)
reader=csv.DictReader(io.StringIO(raw));fields=reader.fieldnames
row=next(x for x in reader if x['url']==url)
assert row['observed_at']=='2026-10-08T05:35:33.870614+00:00'
row.update(http_status='200',final_url=url,robots_allows_googlebot='True',live_noindex='False',live_canonical=url,sitemap_included='True',inbound_pages='2',article_text_present='True',probe_error='',recommended_action='Actual05:35Inspection discovered/no reportedcrawl; not technicalcause/duplication/trend. Independent05:40:40.348870UTC Googlebot-UA200/selfcanonical/exactbuild/robotsallowed/noindexabsent/servertext/singleXML/twoinbound/homeexact; not actualGooglecrawl/render/indexing. Evidence cleaning-fees-independent-eligibility-2026-10-08.json. Next matched cleaning receipts/per-turn purchase reconciliation after overlap/source review. No unchanged submissions.')
i=next(i for i,l in enumerate(lines) if l.startswith(url+','))
out=io.StringIO();writer=csv.DictWriter(out,fieldnames=fields,lineterminator='\r\n' if lines[i].endswith('\r\n') else '\n')
writer.writerow(row);lines[i]=out.getvalue();p.write_bytes(''.join(lines).encode())
print('One live-evidence row updated; actual inspection and performance preserved.')
