"""Read-only reuse of exact-serving/FAQ checks for the foreclosure owner."""
from pathlib import Path
source=(Path(__file__).parent/'verify_str_income_housing.py').read_text()
source=source.replace('airbnb-income-qualify-conventional-str-loan','buy-foreclosure-as-short-term-rental').replace("'current housing payment' in s and 'acceptance worksheet' in s","'sale deadline' in s and 'funding allocation' in s").replace('1972','2132')
exec(compile(source,str(Path(__file__).parent/'verify_foreclosure_funding.py'),'exec'))
