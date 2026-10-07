"""Read-only comparison hub deployment check, not actual Google indexing."""
from pathlib import Path
source=(Path(__file__).parent/'verify_responsibility_review.py').read_text()
source=source.replace("ROUTE='/guides/str-service-responsibility-matrix/'", "ROUTE='/compare/'")
source=source.replace("assert 'A sent report, a completed call' in page and 'producing a $3,000 funding shortfall' in page", "assert all(x in page for x in ['buyer-evidence-path','Use one purchase file','/guides/str-market-analysis-report/','/guides/str-deal-evidence-register/','/blog/str-buyer-agent-vs-acquisition-team/'])")
exec(compile(source,str(Path(__file__)),'exec'))
