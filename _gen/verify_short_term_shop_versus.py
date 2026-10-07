"""Read-only scoped live verification using established comparison checks."""
from pathlib import Path
source=(Path(__file__).parent/'verify_short_term_shop_alternatives.py').read_text()
source=source.replace("ROUTE='/compare/alternatives-to-the-short-term-shop/'", "ROUTE='/compare/avery-carl-short-term-shop/'")
source=source.replace('2026-09-27','2026-08-15')
source=source.replace("['$287,500','$290,500','$298,000','$301,000','Fictional illustration only','not firsthand testing']", "['$304,000','$284,000','$299,000','$319,000','Hypothetical arithmetic only','not firsthand testing']")
exec(compile(source,str(Path(__file__)),'exec'))
