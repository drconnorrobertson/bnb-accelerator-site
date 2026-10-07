"""Reuse bounded exact-deployment verifier with this owner's preserved schema."""
import html,re
from pathlib import Path
code=Path(__file__).with_name('verify_short_term_shop_alternatives.py').read_text()
code=code.replace('/compare/alternatives-to-the-short-term-shop/','/compare/best-done-for-you-airbnb-companies/').replace('2026-09-27','2026-08-10')
code=code.replace("n.get('@type')=='Article'","n.get('@type') in ('Article','BlogPosting')")
code=code.replace("['$287,500','$290,500','$298,000','$301,000','Fictional illustration only','not firsthand testing']","['$280,000','$278,000','$281,700','$38,300','Fictional illustration only','not firsthand testing','STR Insights','STR Search','The Short Term Shop','Awning','Rabbu']")
code=code.replace("    robot=", "    faq=next(n for n in nodes if n.get('@type')=='FAQPage')['mainEntity'];assert len(faq)==5\n    for n in faq:assert html.escape(n['name']) in t and html.escape(n['acceptedAnswer']['text']) in t\n    robot=")
exec(compile(code,__file__,'exec'))
