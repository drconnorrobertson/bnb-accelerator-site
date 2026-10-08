"""Insert one actual inspection baseline, preserving every existing CSV row."""
import csv,io,json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
p=R/'_gen/blog-indexing-inventory.csv';raw=p.read_bytes();text=raw.decode();fields=next(csv.reader(io.StringIO(text)))
url='https://www.bnbaccelerator.com/compare/roofstock-vs-rabbu/'
assert not any(r['url']==url for r in csv.DictReader(io.StringIO(text)))
d={k:'' for k in fields}
d.update(url=url,observed_at='2026-10-08T06:33:56.314636+00:00',priority='True',indexing_verdict='NEUTRAL',indexing_state='INDEXING_STATE_UNSPECIFIED',coverage_state='URL is unknown to Google',http_status='200',final_url=url,robots_allows_googlebot='True',source_noindex='False',live_noindex='False',source_canonical=url,live_canonical=url,sitemap_included='True',inbound_pages='3',topic_cluster='service-selection/rental-use and possession',impressions='not returned',clicks='not returned',performance_start='not queried',performance_end='not queried',article_text_present='True',recommended_action='First actual baseline URL unknown/no reported crawl; no cause, duplication, trend or revised-body receipt inferred. Separate exact serving eligibility06:31:54UTC; allow crawl time and continue substantive acquisition work without repeated unchanged submissions')
nl='\r\n' if b'\r\n' in raw else '\n';line=io.StringIO();csv.DictWriter(line,fields,lineterminator=nl).writerow(d)
cut=raw.index(b'\n')+1;p.write_bytes(raw[:cut]+line.getvalue().encode()+raw[cut:])
p=R/'_gen/expansion_509_progress.json';s=p.read_text();old='Complete filtered stored history zero rows before publication; indexing/crawl/exclusion unknown, not proof of exclusion or revised-body receipt'
new='First actual Inspection2026-10-08T06:33:56.314636UTC NEUTRAL/URLunknown/unspecifiedrobots-indexing-fetch/no reportedcrawl; completehistoryzero before/oneafter/hasMorefalse. Not technical cause, trend or revised-body receipt; separate live eligibility. _gen/roofstock-rabbu-indexing-baseline-2026-10-08.json'
assert s.count(old)==1;p.write_text(s.replace(old,new))
print('PASS: one CSV insertion and one comparison evidence update; existing rows/counts preserved')
