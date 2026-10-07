"""Read-only exact serving eligibility check, not indexing evidence."""
from pathlib import Path
source=(Path(__file__).parent/'verify_responsibility_review.py').read_text()
source=source.replace("ROUTE='/guides/str-service-responsibility-matrix/'", "ROUTE='/guides/kleer-circle-year-one-operations/'")
source=source.replace("assert 'A sent report, a completed call' in page and 'producing a $3,000 funding shortfall' in page", "assert all(x in page for x in ['Original worked coverage-gap test','$1,380','four-hour Thursday gap','not firsthand testing','decision-ready exception'])")
exec(compile(source,str(Path(__file__)),'exec'))
