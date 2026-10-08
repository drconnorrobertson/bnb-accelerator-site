"""Exact deployment and serving eligibility, not actual indexing."""
from pathlib import Path
s=(Path(__file__).parent/'verify_short_term_shop_alternatives.py').read_text()
s=s.replace("ROUTE='/compare/alternatives-to-the-short-term-shop/'", "ROUTE='/compare/best-str-financing-options/'")
s=s.replace("a['datePublished']=='2026-09-27'", "a['datePublished']=='2026-08-11'")
s=s.replace("'publication_date':'2026-09-27'", "'publication_date':'2026-08-11'")
s=s.replace('2026-10-07','2026-10-08')
s=s.replace("['$287,500','$290,500','$298,000','$301,000','Fictional illustration only','not firsthand testing']", "['$244,000','$269,200','$258,982','$284,010','Invented figures only','not firsthand lender testing']")
exec(compile(s,str(Path(__file__)),'exec'))
