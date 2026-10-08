"""Read-only exact serving checks; submissions and actual indexing remain separate."""
from pathlib import Path
source=(Path(__file__).parent/'verify_str_income_housing.py').read_text()
source=source.replace('airbnb-income-qualify-conventional-str-loan','how-to-finance-airbnb-investment-property')
source=source.replace("'current housing payment' in s and 'acceptance worksheet' in s","'cash schedule' in s and 'credited' in s")
source=source.replace("a['datePublished']=='2026-09-24'","a['datePublished']=='2026-08-10'")
source=source.replace("a['wordCount']==1972","a['wordCount']==1881")
source=source.replace('assert len(faq)==4','assert len(faq)==8').replace('==1972','==1859')
exec(compile(source,str(Path(__file__).parent/'verify_broad_financing.py'),'exec'))
