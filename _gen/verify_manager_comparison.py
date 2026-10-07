"""Exact changed artifacts and bounded public eligibility checks."""
from pathlib import Path
c=Path(__file__).with_name('verify_short_term_shop_alternatives.py').read_text()
c=c.replace('/compare/alternatives-to-the-short-term-shop/','/compare/bnb-accelerator-vs-property-manager/').replace('2026-09-27','2026-08-11')
c=c.replace("['$287,500','$290,500','$298,000','$301,000','Fictional illustration only','not firsthand testing']","['$299,000','$314,000','$309,000','$324,000','$4,000 shortfall','Hypothetical only','not firsthand provider testing']")
exec(compile(c,__file__,'exec'))
