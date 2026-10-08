"""Mechanically update one mixed-line-ending inventory row from observed evidence."""
import csv,io
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'_gen/blog-indexing-inventory.csv'
u='https://www.bnbaccelerator.com/blog/cleaner-capacity-peak-season/'
raw=p.read_bytes().decode();lines=raw.splitlines(keepends=True);reader=csv.DictReader(io.StringIO(raw));fields=reader.fieldnames;row=next(x for x in reader if x['url']==u)
row.update(observed_at='2026-10-08T05:20:01.415762+00:00',priority='True',indexing_verdict='PASS',indexing_state='INDEXING_ALLOWED',coverage_state='Submitted and indexed',last_google_crawl='2026-10-08T02:13:34Z',recommended_action='First actual Inspection confirms indexed/mobile successful fetch; not indexing gain or performance. Preserve canonical and expand accepted peak-day crew/laundry/travel readiness decision support; no unchanged submissions. Evidence cleaner-capacity-indexing-baseline-2026-10-08.json.')
assert set(row)==set(fields)
i=next(i for i,l in enumerate(lines) if l.startswith(u+','));out=io.StringIO();writer=csv.DictWriter(out,fieldnames=fields,lineterminator='\r\n' if lines[i].endswith('\r\n') else '\n');writer.writerow(row);lines[i]=out.getvalue();p.write_bytes(''.join(lines).encode())
print('Updated one actual indexing baseline; no live eligibility or performance inferred.')
