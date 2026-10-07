"""Read-only existing resource deployment verification, not indexing evidence."""
from pathlib import Path
source=(Path(__file__).parent/'verify_responsibility_review.py').read_text()
source=source.replace("ROUTE='/guides/str-service-responsibility-matrix/'", "ROUTE='/guides/str-market-analysis-report/'").replace('2026-10-01','2026-08-15')
source=source.replace("n.get('@type')=='Article'", "n.get('@type')=='WebPage'")
source=source.replace("assert 'A sent report, a completed call' in page and 'producing a $3,000 funding shortfall' in page", "assert all(x in page for x in ['Original report-acceptance worksheet','$54,000','$13,500','No fixed count establishes adequacy','not a custom-report request'])")
exec(compile(source,str(Path(__file__)),'exec'))
