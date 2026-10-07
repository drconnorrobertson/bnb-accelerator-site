"""Read-only exact live comparison verification."""
from pathlib import Path
source=(Path(__file__).parent/'verify_rabbu_alternatives.py').read_text()
source=source.replace("ROUTE='/compare/alternatives-to-rabbu/'", "ROUTE='/compare/rabbu/'").replace('2026-09-27','2026-08-15')
source=source.replace("['$18,000','negative $6,000','$253,000','$3,000 short','Fictional example','not firsthand testing']", "['$268,000','$286,000','$282,000','$536,000','Hypothetical worksheet','not firsthand testing']")
exec(compile(source,str(Path(__file__)),'exec'))
