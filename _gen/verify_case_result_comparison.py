"""Read-only existing resource deployment check, without indexing inference."""
from pathlib import Path
source=(Path(__file__).parent/'verify_responsibility_review.py').read_text()
source=source.replace("ROUTE='/guides/str-service-responsibility-matrix/'", "ROUTE='/guides/reading-str-case-study-results/'").replace('2026-10-01','2026-10-04')
source=source.replace("assert 'A sent report, a completed call' in page and 'producing a $3,000 funding shortfall' in page", "assert all(x in page for x in ['$36,000','$5,000','2.5%','not firsthand provider testing','Original two-file comparison'])")
exec(compile(source,str(Path(__file__)),'exec'))
