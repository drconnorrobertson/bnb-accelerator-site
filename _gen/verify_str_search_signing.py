"""Read-only exact deployment, links and eligibility; not indexing confirmation."""
from pathlib import Path
source=(Path(__file__).parent/'verify_responsibility_review.py').read_text()
source=source.replace("ROUTE='/guides/str-service-responsibility-matrix/'", "ROUTE='/guides/str-search-property-match-questions/'")
source=source.replace("assert 'A sent report, a completed call' in page and 'producing a $3,000 funding shortfall' in page", "assert all(x in page for x in ['$275,000','$287,000','$312,000','$12,000 funding shortfall','not firsthand testing','insurance and permitted use unresolved'])")
exec(compile(source,str(Path(__file__)),'exec'))
