"""Record an existing comparison refresh without claiming new-page credit."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
e=json.loads((R/'_gen/expanded-shortlist-live-evidence-2026-10-08.json').read_text())
p=R/'_gen/expansion_509_progress.json';d=json.loads(p.read_text())
a=d['separately_counted_comparison_refreshes'];assert len(a)==18
a.insert(0,{'url':e['url'],'content_commit':e['content_commit'],'verified_live_at':e['verified_at'],'evidence':'_gen/expanded-shortlist-live-evidence-2026-10-08.json','counted_toward_509':False,'improvement':'Three sourced additional acquisition models and original management-connected cash/exit worksheet in existing shortlist owner','validation':e['validation'],'submission':e['submission'],'google_indexing_evidence':e['actual_google_indexing']})
assert len(a)==19 and d['verified_live_new_pages']==10
p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
print('PASS19comparisonrefreshes/10new; prior evidence preserved')
