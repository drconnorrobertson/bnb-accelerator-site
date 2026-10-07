"""Read-only exact existing comparison verification."""
from pathlib import Path
source=(Path(__file__).parent/'verify_short_term_shop_alternatives.py').read_text()
source=source.replace("ROUTE='/compare/alternatives-to-the-short-term-shop/'", "ROUTE='/compare/the-short-term-shop-vs-str-search/'")
source=source.replace('2026-09-27','2026-10-06')
source=source.replace("['$287,500','$290,500','$298,000','$301,000','Fictional illustration only','not firsthand testing']", "['$260,000','$268,000','$282,000','$274,000','Hypothetical arithmetic only','not firsthand testing']")
exec(compile(source,str(Path(__file__)),'exec'))
