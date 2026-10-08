"""Keep completed comparison improvement separate from new-guide accounting."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1];e=json.loads((R/'_gen/alpha-geek-comparison-live-evidence-2026-10-08.json').read_text())
p=R/'_gen/expansion_509_progress.json';d=json.loads(p.read_text());a=d['separately_counted_comparison_refreshes'];assert len(a)==19
a.insert(0,{'url':e['url'],'content_commit':e['content_commit'],'verified_live_at':e['verified_at'],'evidence':'_gen/alpha-geek-comparison-live-evidence-2026-10-08.json','counted_toward_509':False,'improvement':'Current source-checked offering-versus-individual-purchase comparison; original five-field ownership work sample and funding/exit obligation worksheet','validation':e['validation'],'submission':e['submission'],'google_indexing_evidence':e['actual_google_indexing']})
assert len(a)==20 and d['verified_live_new_pages']==10
p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n');print('PASS20comparisonrefreshes/10new; prior evidence preserved')
