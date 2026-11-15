"""Check source or deploy output for the existing 50 comparison owners."""
import json
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit, unquote

REPO = Path(__file__).resolve().parents[1]
ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else REPO
BASELINE = json.loads((REPO / 'docs/comparisons-nov15/search-baseline.json').read_text())


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.h1 = 0
        self.links = []
        self.robots = []
        self.canonical = []
        self.description = []
        self.title = ''
        self.in_title = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'h1': self.h1 += 1
        if tag == 'title': self.in_title = True
        if tag == 'a' and a.get('href'): self.links.append(a['href'])
        if tag == 'link' and a.get('rel') == 'canonical': self.canonical.append(a.get('href'))
        if tag == 'meta' and a.get('name') == 'robots': self.robots.append(a.get('content', ''))
        if tag == 'meta' and a.get('name') == 'description': self.description.append(a.get('content'))

    def handle_endtag(self, tag):
        if tag == 'title': self.in_title = False

    def handle_data(self, data):
        if self.in_title: self.title += data


def dates(doc):
    found = []
    if isinstance(doc, dict):
        if 'datePublished' in doc: found.append(doc['datePublished'])
        for value in doc.values(): found.extend(dates(value))
    elif isinstance(doc, list):
        for value in doc: found.extend(dates(value))
    return found


titles, descriptions, pages = set(), set(), {}
for route, original_dates in BASELINE['publication_dates'].items():
    text = (ROOT / route.strip('/') / 'index.html').read_text()
    page = Page(); page.feed(text); pages[route] = page
    assert page.h1 == 1, (route, 'H1 count', page.h1)
    assert page.canonical == ['https://www.bnbaccelerator.com' + route], (route, page.canonical)
    assert not any('noindex' in value.lower() for value in page.robots), route
    assert page.title and page.title not in titles, (route, 'duplicate or empty title')
    assert len(page.description) == 1 and page.description[0] not in descriptions, (route, 'description')
    titles.add(page.title); descriptions.add(page.description[0])
    published = []
    for source in re.findall(r'<script type="application/ld\+json">(.*?)</script>', text, re.S):
        published.extend(dates(json.loads(source)))
    assert published == original_dates, (route, 'publication date changed', published, original_dates)
    for href in page.links:
        url = urlsplit(unescape(href))
        if url.scheme or url.netloc or not url.path.startswith('/'): continue
        target = ROOT / unquote(url.path).lstrip('/')
        assert target.is_file() or (target / 'index.html').is_file(), (route, href)
    if '/alternatives-to-' in route:
        assert text.count('id="compare-options"') == 1, route
        assert '<caption>Named alternatives and the work to compare</caption>' in text, route

alternatives = {route for route in pages if '/alternatives-to-' in route}
assert len(alternatives) == 24
for hub in ['/compare/', '/compare/alternatives/']:
    main = re.search(r'<main\b[^>]*>(.*?)</main>', (ROOT / hub.strip('/') / 'index.html').read_text(), re.S)[1]
    for route in alternatives: assert f'href="{route}"' in main, (hub, route)
    assert 'ItemListUnordered' in (ROOT / hub.strip('/') / 'index.html').read_text()

print('Comparison checks passed: 50 owners, unique metadata, 24 alternatives discoverable, valid internal links, unchanged publication dates.')
