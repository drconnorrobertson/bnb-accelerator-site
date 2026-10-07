"""Read-only resource deployment and eligibility checks, not indexing confirmation."""
from pathlib import Path
source=(Path(__file__).parent/'verify_responsibility_review.py').read_text()
source=source.replace("ROUTE='/guides/str-service-responsibility-matrix/'", "ROUTE='/guides/str-insights-service-tiers/'")
source=source.replace("assert 'A sent report, a completed call' in page and 'producing a $3,000 funding shortfall' in page", "assert all(x in page for x in ['$265,000','$257,000','$283,000','$275,000','not firsthand testing','installation unresolved'])")
exec(compile(source,str(Path(__file__)),'exec'))
