#!/usr/bin/env python3
"""Refresh only the eight reviewed owners; preserve the shared design shell."""
from pathlib import Path
import re
import tpl
from buyer_intent import PAGES, REVIEWED
from refresh_buyer_evidence import save

ROOT = Path(__file__).resolve().parents[1]


def main():
    for route in PAGES:
        assert (ROOT / route.strip('/') / 'index.html').is_file(), route
        save(route, tpl.page(title='', description='', path=route, body=''))
    for path in ROOT.glob('sitemap-*.xml'):
        def stamp(match):
            block = match.group()
            location = re.search(r'<loc>(.*?)</loc>', block).group(1)
            route = location.removeprefix(tpl.SITE)
            return re.sub(r'<lastmod>.*?</lastmod>', f'<lastmod>{REVIEWED}</lastmod>', block) if route in PAGES else block
        path.write_text(re.sub(r'<url>.*?</url>', stamp, path.read_text(), flags=re.S))
    print(f'Buyer-intent cohort: {len(PAGES)} existing routes refreshed; no new routes.')


if __name__ == '__main__':
    main()
