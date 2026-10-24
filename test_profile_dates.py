"""Check Google's ProfilePage DateTime fields in source or public output.

Run: python3 test_profile_dates.py [public]
Google's requirements: https://developers.google.com/search/docs/appearance/structured-data/profile-page
"""
import json
from pathlib import Path
import re
import sys
from datetime import datetime


def objects(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from objects(child)
    elif isinstance(value, list):
        for child in value:
            yield from objects(child)


root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')
profiles = 0
for path in root.rglob('*.html'):
    if any(part in {'.git', 'node_modules', 'public'} for part in path.relative_to(root).parts[:-1]):
        continue
    html = path.read_text(encoding='utf-8')
    for raw in re.findall(r'<script\b[^>]*type=[\"\']application/ld\+json[\"\'][^>]*>(.*?)</script>', html, re.S | re.I):
        for obj in objects(json.loads(raw)):
            types = obj.get('@type', [])
            if isinstance(types, str):
                types = [types]
            if 'ProfilePage' not in types:
                continue
            profiles += 1
            for field in ('dateCreated', 'dateModified'):
                if field not in obj:
                    continue  # Both properties are recommended, not required.
                value = obj[field]
                assert isinstance(value, str) and re.fullmatch(
                    r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})', value
                ), f'{path}: {field} must be an ISO 8601 datetime with timezone: {value!r}'
                assert datetime.fromisoformat(value.replace('Z', '+00:00')).utcoffset() is not None
assert profiles, f'No ProfilePage found under {root}'
print(f'PASS: {profiles} ProfilePage objects have valid date/time fields ({root}).')
