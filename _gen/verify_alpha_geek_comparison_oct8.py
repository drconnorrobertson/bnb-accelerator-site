"""Exact public owner/sitemap/home verification with preserved publication."""
from pathlib import Path
code=Path(__file__).with_name('verify_short_term_shop_alternatives.py').read_text()
code=code.replace('/compare/alternatives-to-the-short-term-shop/','/compare/alpha-geek-capital/').replace('2026-09-27','2026-08-15').replace('2026-10-07','2026-10-08')
code=code.replace("['$287,500','$290,500','$298,000','$301,000','Fictional illustration only','not firsthand testing']", "['$280,000','$325,000','$255,000','$352,000','$2,000','$295,000','$55,000','Fictional comparison only','not firsthand testing','offering-decision-file','capital-comparison']")
exec(compile(code,__file__,'exec'))
