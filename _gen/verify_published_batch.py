"""Read-only production checks before IndexNow; accepts blog slugs."""
import concurrent.futures
import json
import re
import sys
import time
import urllib.request
from urllib.parse import urljoin, urlparse
import xml.etree.ElementTree as ET

BASE = 'https://www.bnbaccelerator.com'

def fetch(url):
    for attempt in range(2):
        try:
            request = urllib.request.Request(url, headers={'User-Agent': 'BNB-Publication-Verification/1.0'})
            with urllib.request.urlopen(request, timeout=35) as response:
                assert response.status == 200, (url, response.status)
                return response.read().decode(), response.geturl()
        except Exception:
            if attempt:
                raise
            time.sleep(15)

def verify(slugs):
    sitemap, _ = fetch(BASE + '/sitemap-blog.xml')
    listed = [n.text for n in ET.fromstring(sitemap).iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
    main, _ = fetch(BASE + '/sitemap.xml')
    assert BASE + '/sitemap-blog.xml' in main
    hubs = [fetch(BASE + path)[0] for path in ['/blog/', '/sitemap/']]
    internal = set()
    for slug in slugs:
        route = '/blog/' + slug + '/'
        url = BASE + route
        html, final = fetch(url)
        assert final == url, (url, final)
        canonical = re.findall(r'<link[^>]+rel="canonical"[^>]+href="([^"]+)"', html)
        assert canonical == [url], canonical
        assert '<h1' in html and 'noindex' not in html
        nodes = []
        for block in re.findall(r'<script[^>]+type="application/ld\+json"[^>]*>(.*?)</script>', html, re.S):
            data = json.loads(block)
            nodes.extend(data.get('@graph', [data]))
        assert any(n.get('@type') in ['Article', 'BlogPosting'] for n in nodes)
        assert any(n.get('@type') == 'FAQPage' for n in nodes)
        assert listed.count(url) == 1, (url, listed.count(url))
        assert all(route in hub for hub in hubs), route
        if slug.startswith('bnb-accelerator-vs-'):
            assert route in fetch(BASE + '/compare/')[0], ('comparison discovery missing', route)
        for ref in re.findall(r'(?:href|src)="([^"]+)"', html):
            target = urljoin(url, ref)
            parsed = urlparse(target)
            if parsed.netloc == 'www.bnbaccelerator.com':
                internal.add(BASE + parsed.path + ('?' + parsed.query if parsed.query else ''))
        print('PASS live canonical, Article/FAQ JSON-LD, discovery hubs and sitemap:', url)
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        list(pool.map(fetch, sorted(internal)))
    print('PASS production internal links/assets:', len(internal))

if __name__ == '__main__':
    assert len(sys.argv) > 1, 'Supply one or more blog slugs'
    verify(sys.argv[1:])
