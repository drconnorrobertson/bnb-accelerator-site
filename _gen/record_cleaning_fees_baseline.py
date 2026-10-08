"""Update only the actual-evidence fields of one inventory row."""
import csv,io
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'_gen/blog-indexing-inventory.csv';u='https://www.bnbaccelerator.com/blog/cleaning-fees-gross-revenue/'
raw=p.read_bytes().decode();lines=raw.splitlines(keepends=True);reader=csv.DictReader(io.StringIO(raw));fields=reader.fieldnames;row=next(x for x in reader if x['url']==u)
row.update(observed_at='2026-10-08T05:35:33.870614+00:00',priority='True',indexing_verdict='NEUTRAL',indexing_state='INDEXING_STATE_UNSPECIFIED',coverage_state='Discovered - currently not indexed',last_google_crawl='not reported',recommended_action='First actual Inspection discovered/no reportedcrawl; not technicalcause/duplication/trend. Preserve canonical; expand matched cleaning receipts and per-turn purchase-underwriting reconciliation after overlap/source review. No unchanged submissions. Evidence cleaning-fees-indexing-baseline-2026-10-08.json.')
assert set(row)==set(fields)
i=next(i for i,l in enumerate(lines) if l.startswith(u+','));out=io.StringIO();writer=csv.DictWriter(out,fieldnames=fields,lineterminator='\r\n' if lines[i].endswith('\r\n') else '\n');writer.writerow(row);lines[i]=out.getvalue();p.write_bytes(''.join(lines).encode())
print('Recorded first actual cleaning-fee baseline; no fresh live or performance claim.')
