#!/usr/bin/env python3
"""Inventory canonical public inbound links; separate discovery from prose links.

Build public first. Usage: python3 _gen/audit_internal_inbound.py --output docs/orphan-audit-before
The contextual count is a structural screen, not a content quality or ranking score.
"""
import argparse
from collections import defaultdict
import csv
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import urljoin, urlsplit
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SITE = 'https://www.bnbaccelerator.com'
INDEX_ROUTES = {'/sitemap/', '/blog/', '/guides/str-investment/', '/scenarios/', '/answers/', '/topics/'}
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}


class Page(HTMLParser):
    def __init__(self, source, route):
        super().__init__(convert_charrefs=True)
        self.route = route
        self.stack = []
        self.title = ''
        self.h1 = ''
        self.canonical = None
        self.noindex = False
        self.nofollow = False
        self.links = []
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'link' and 'canonical' in attrs.get('rel', '').split():
            self.canonical = attrs.get('href')
        if tag == 'meta' and attrs.get('name', '').lower() in ('robots', 'googlebot'):
            tokens = attrs.get('content', '').lower()
            self.noindex |= 'noindex' in tokens or 'none' in tokens
            self.nofollow |= 'nofollow' in tokens or 'none' in tokens
        if tag == 'a' and 'href' in attrs:
            href = attrs['href'].strip()
            if href and not href.startswith('#') and 'nofollow' not in attrs.get('rel', '').lower().split():
                url = urlsplit(urljoin(SITE + self.route, href))
                if url.scheme in ('http', 'https') and url.netloc in ('www.bnbaccelerator.com', 'bnbaccelerator.com'):
                    target = url.path or '/'
                    if target.endswith('/index.html'):
                        target = target[:-len('index.html')]
                    elif target != '/' and not Path(target).suffix:
                        target = target.rstrip('/') + '/'
                    if target != self.route:
                        tags = {t for t, _ in self.stack}
                        classes = ' '.join(a.get('class', '') for _, a in self.stack)
                        in_main = 'main' in tags and not tags.intersection({'header', 'footer', 'nav'})
                        index = self.route in INDEX_ROUTES or self.route.startswith('/blog/page/')
                        related = any(x in classes for x in ('callout', 'author', 'breadcrumb', 'sitemap', 'article-meta'))
                        contextual = in_main and not index and not related and bool(tags.intersection({'p', 'td'}))
                        self.links.append((target, 'contextual' if contextual else 'main' if in_main and not index else 'index' if index else 'navigation'))
        if tag not in VOID:
            self.stack.append((tag, attrs))

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                self.stack = self.stack[:i]
                break

    def handle_data(self, data):
        tags = {t for t, _ in self.stack}
        if 'title' in tags:
            self.title += data
        if 'h1' in tags:
            self.h1 += data


def redirect_matches(pattern, route):
    pattern = re.escape(pattern)
    pattern = re.sub(r':\w+', '[^/]+', pattern)
    pattern = pattern.replace(r'\(\.\*\)', '.*')
    return re.fullmatch(pattern, route) is not None


def inventory(public):
    redirects = json.loads((ROOT / 'vercel.json').read_text())['redirects']
    pages = {}
    for path in sorted(public.rglob('*.html')):
        relative = path.relative_to(public).as_posix()
        route = '/' if relative == 'index.html' else '/' + relative[:-len('index.html')] if relative.endswith('/index.html') else '/' + relative
        page = Page(path.read_text(), route)
        reasons = []
        if page.noindex:
            reasons.append('noindex utility')
        if page.canonical != SITE + route:
            reasons.append('not a self-canonical public URL')
        if any(redirect_matches(r['source'], route) for r in redirects):
            reasons.append('redirect source')
        pages[route] = (page, '; '.join(reasons))
    eligible = {route for route, (_, reason) in pages.items() if not reason}
    incoming = {kind: defaultdict(set) for kind in ('all', 'contextual', 'main', 'index', 'navigation')}
    graph = defaultdict(set)
    for source in eligible:
        page = pages[source][0]
        if page.nofollow:
            continue
        for target, kind in page.links:
            if target in eligible:
                graph[source].add(target)
                incoming['all'][target].add(source)
                incoming[kind][target].add(source)
    reached, pending = set(), ['/']
    while pending:
        route = pending.pop()
        if route not in reached:
            reached.add(route)
            pending.extend(graph[route] - reached)
    sitemap = set()
    for path in public.glob('sitemap-*.xml'):
        sitemap.update(urlsplit(e.text).path for e in ET.parse(path).iter() if e.tag.endswith('loc'))
    rows = []
    for route, (page, reason) in sorted(pages.items()):
        indexable = route in eligible
        inbound = len(incoming['all'][route])
        rows.append(dict(url=SITE + route, title=page.title, canonical=page.canonical or '',
                         eligible=indexable, exclusion_reason=reason,
                         inbound_sources=inbound, contextual_sources=len(incoming['contextual'][route]),
                         main_other_sources=len(incoming['main'][route]), index_sources=len(incoming['index'][route]),
                         navigation_sources=len(incoming['navigation'][route]), homepage_reachable=route in reached,
                         in_sitemap=route in sitemap, true_orphan=indexable and inbound == 0,
                         sitemap_only=indexable and inbound == 0 and route in sitemap,
                         contextual_source_urls=' | '.join(SITE + x for x in sorted(incoming['contextual'][route])),
                         readiness='Unreviewed; count alone does not establish content quality',
                         gsc_page_clicks='', gsc_page_impressions='', gsc_page_average_position='',
                         gsc_note='Page-level GSC metrics were not supplied; no indexing inference'))
    summary = dict(public_html_files=len(pages), eligible_canonical_routes=len(eligible),
                   true_orphans=sum(r['true_orphan'] for r in rows), homepage_unreachable=len(eligible - reached),
                   sitemap_only=sum(r['sitemap_only'] for r in rows), excluded_html=sum(not r['eligible'] for r in rows),
                   zero_contextual_sources=sum(r['eligible'] and r['contextual_sources'] == 0 for r in rows),
                   redirect_rules=len(redirects), sitemap_routes=len(sitemap),
                   methodology='Distinct eligible source URLs; self, fragment-only and nofollow anchors excluded. Contextual means main-content paragraph/table anchors outside structural navigation, recognized indexes, related callouts and author blocks. This is a heuristic, not a relevance or content-quality certification.')
    gsc_file = ROOT / 'docs/gsc-link-source-shortlist.json'
    if gsc_file.exists():
        gsc = json.loads(gsc_file.read_text())
        metrics = {r['source_url']: r for r in gsc['rows']}
        for row in rows:
            metric = metrics.get(row['url'])
            if metric:
                row.update(gsc_page_clicks=metric['clicks'], gsc_page_impressions=metric['impressions'],
                           gsc_page_average_position=metric['average_position'],
                           gsc_note='Supplied page-dimension GSC export: Sep 6–Oct 3; daily coverage Sep 18 onward; sparse signal, not indexing or authority proof')
    return rows, summary, redirects


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default='docs/orphan-audit-after')
    parser.add_argument('--public', default='public')
    args = parser.parse_args()
    output = ROOT / args.output
    output.mkdir(parents=True, exist_ok=True)
    rows, summary, redirects = inventory(ROOT / args.public)
    with (output / 'public-route-inventory.csv').open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    with (output / 'redirect-exclusions.csv').open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['source', 'destination', 'permanent'])
        writer.writeheader()
        writer.writerows({k: row.get(k, '') for k in writer.fieldnames} for row in redirects)
    (output / 'summary.json').write_text(json.dumps(summary, indent=2) + '\n')
    with (output / 'weak-contextual-inventory.csv').open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(r for r in rows if r['eligible'] and r['contextual_sources'] == 0)
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
