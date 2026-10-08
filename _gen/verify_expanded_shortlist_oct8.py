"""Reuse the exact owner verifier with this meaningful modification date."""
from pathlib import Path
code=Path(__file__).with_name('verify_best_done_for_you.py').read_text()
code=code.replace("exec(compile(code,__file__,'exec'))", "code=code.replace('2026-10-07','2026-10-08')\ncode=code.replace('    robot=', \"    assert a['wordCount']==2322\\n    assert all(x in t for x in ['Suite Capacity','InvestSTR','Stay AZ','$264,000','$269,000','$51,000'])\\n    robot=\")\nexec(compile(code,__file__,'exec'))")
exec(compile(code,__file__,'exec'))
