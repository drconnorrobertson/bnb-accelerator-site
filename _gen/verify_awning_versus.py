"""Read-only exact live comparison verification."""
from pathlib import Path
source=(Path(__file__).parent/'verify_short_term_shop_alternatives.py').read_text()
source=source.replace("ROUTE='/compare/alternatives-to-the-short-term-shop/'", "ROUTE='/compare/awning/'").replace('2026-09-27','2026-08-15')
source=source.replace("['$287,500','$290,500','$298,000','$301,000','Fictional illustration only','not firsthand testing']", "['$290,000','$303,000','$298,000','$2,000','Invented illustration','not firsthand testing']")
exec(compile(source,str(Path(__file__)),'exec'))
