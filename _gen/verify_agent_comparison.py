"""Bounded live verification using the established comparison verifier."""
from pathlib import Path
c=Path(__file__).with_name('verify_short_term_shop_alternatives.py').read_text()
c=c.replace('/compare/alternatives-to-the-short-term-shop/','/compare/bnb-accelerator-vs-real-estate-agent/').replace('2026-09-27','2026-08-11')
c=c.replace("['$287,500','$290,500','$298,000','$301,000','Fictional illustration only','not firsthand testing']","['$323,000','$340,000','$335,000','$352,000','$2,000 shortfall','Hypothetical only','not firsthand provider testing']")
exec(compile(c,__file__,'exec'))
