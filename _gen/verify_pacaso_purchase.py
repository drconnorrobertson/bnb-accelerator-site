"""Exact serving eligibility verification, not indexing evidence."""
from pathlib import Path
s=(Path(__file__).parent/'verify_short_term_shop_alternatives.py').read_text()
s=s.replace("ROUTE='/compare/alternatives-to-the-short-term-shop/'","ROUTE='/compare/bnb-accelerator-vs-pacaso/'")
s=s.replace('2026-09-27','2026-10-06').replace('2026-10-07','2026-10-08')
s=s.replace("['$287,500','$290,500','$298,000','$301,000','Fictional illustration only','not firsthand testing']","['$210,000','$265,000','$277,000','$307,000','Hypothetical arithmetic only','not firsthand testing']")
exec(compile(s,str(Path(__file__)),'exec'))
