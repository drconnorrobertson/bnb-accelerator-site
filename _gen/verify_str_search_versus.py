"""Read-only direct comparison verification using the established scoped verifier."""
from pathlib import Path
source=(Path(__file__).parent/'verify_str_search_alternatives.py').read_text()
source=source.replace("ROUTE='/compare/alternatives-to-str-search/'", "ROUTE='/compare/str-search/'")
source=source.replace("['$296,600','$302,600','$3,400','Illustrative only','not firsthand testing']", "['$348,000','$345,000','$354,000','$351,000','Hypothetical arithmetic only','not firsthand testing']")
exec(compile(source,str(Path(__file__)),'exec'))
