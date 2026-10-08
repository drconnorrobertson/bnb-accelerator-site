"""Reuse read-only exact-artifact serving checks with this owner's preserved FAQ/date assertions."""
from pathlib import Path
source=(Path(__file__).parent/'verify_camera_privacy.py').read_text()
source=source.replace("ROUTE='/blog/security-camera-privacy-str/'","ROUTE='/blog/airbnb-income-qualify-conventional-str-loan/'")
source=source.replace("'day 10' in s and 'acceptance register' in s","'current housing payment' in s and 'acceptance worksheet' in s")
source=source.replace("a['datePublished']=='2026-09-23'","a['datePublished']=='2026-09-24'")
source=source.replace("a['wordCount']==1399","a['wordCount']==1972")
source=source.replace("assert not any(n.get('@type')=='FAQPage' for n in nodes)","""faq=next(n for n in nodes if n.get('@type')=='FAQPage')['mainEntity']
assert len(faq)==4
for q in faq:
    assert q['name'] in s and q['acceptedAnswer']['text'] in s
body=re.search(r'<article class=\"article\">(.*?)<div class=\"author-box\">',s,re.S)[1]
body=re.sub(r'<aside class=\"buyer-next-step\".*?</aside>','',body,flags=re.S)
import html
assert len(re.findall(r'\\b\\w+\\b',html.unescape(re.sub('<[^>]+>',' ',body))))==1972""")
exec(compile(source,str(Path(__file__).parent/'verify_str_income_housing.py'),'exec'))
