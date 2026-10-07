"""Existing deployment verifier specialized to the reviewed comparison."""
from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]
ROUTE='/compare/bnb-turnkey-vs-str-search/'
source=(ROOT/'_gen/verify_short_term_shop_alternatives.py').read_text()
source=source.replace("ROUTE='/compare/alternatives-to-the-short-term-shop/'",f"ROUTE='{ROUTE}'")
source=source.replace("'2026-09-27'","'2026-10-06'")
source=source.replace("['$287,500','$290,500','$298,000','$301,000','Fictional illustration only','not firsthand testing']","['$290,000','$294,500','$300,500','$7,500','$13,500','Hypothetical arithmetic only','not firsthand testing']")
source=source.replace("    robot=urllib.robotparser.RobotFileParser();", "    faq=next(n for n in nodes if n.get('@type')=='FAQPage');assert len(faq['mainEntity'])==4\n    for question in faq['mainEntity']:\n        assert question['name'] in t and question['acceptedAnswer']['text'] in t\n    robot=urllib.robotparser.RobotFileParser();")
exec(compile(source,__file__,'exec'))
