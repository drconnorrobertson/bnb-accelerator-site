"""Scoped comparison live verifier with FAQ and exact build checks."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
source=(ROOT/'_gen/verify_short_term_shop_alternatives.py').read_text()
source=source.replace("ROUTE='/compare/alternatives-to-the-short-term-shop/'","ROUTE='/compare/kleer-circle-vs-str-insights/'")
source=source.replace("'2026-09-27'","'2026-10-06'")
source=source.replace("['$287,500','$290,500','$298,000','$301,000','Fictional illustration only','not firsthand testing']","['$285,000','$316,000','$313,000','$334,000','$331,000','Hypothetical proposals A and B','not firsthand testing']")
source=source.replace("    robot=urllib.robotparser.RobotFileParser();", "    faq=next(n for n in nodes if n.get('@type')=='FAQPage');assert len(faq['mainEntity'])==4\n    for question in faq['mainEntity']:\n        assert question['name'] in t and question['acceptedAnswer']['text'] in t\n    robot=urllib.robotparser.RobotFileParser();")
exec(compile(source,__file__,'exec'))
