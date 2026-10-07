"""Read-only named handoff resource deployment check, not indexing evidence."""
from pathlib import Path
source=(Path(__file__).parent/'verify_responsibility_review.py').read_text()
source=source.replace("ROUTE='/guides/str-service-responsibility-matrix/'", "ROUTE='/guides/bnb-turnkey-management-handoff/'")
source=source.replace("assert 'A sent report, a completed call' in page and 'producing a $3,000 funding shortfall' in page", "assert all(x in page for x in ['Original one-address management acceptance sample','$18,400','$304,000','a $4,000 gap','not firsthand provider testing'])")
exec(compile(source,str(Path(__file__)),'exec'))
