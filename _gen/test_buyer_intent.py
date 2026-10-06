"""Meaningful arithmetic, source-priority and review-scope gates for this cohort."""
from decimal import Decimal
from itertools import combinations
from pathlib import Path
import html
import json
import re
import subprocess
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import blog
import gen_investor_purchase_guides as investor
import gen_local_markets as local
import tpl
from buyer_intent import (PAGES, COST, FURNISH, BREAK_EVEN, CHANDLER, ARIZONA,
                          REVPAR, OCCUPANCY, PRICING, curated_payload)
from buyer_intent_inputs import fourplex_threshold, validate_examples

ROOT = Path(__file__).resolve().parents[1]
BASELINE = '438d2cb11e60d938562f098a86857f569c5b25cd'
RELATIONSHIPS = [(PRICING, COST), (COST, FURNISH), (OCCUPANCY, BREAK_EVEN),
                 (ARIZONA, CHANDLER), (OCCUPANCY, REVPAR), (REVPAR, OCCUPANCY), (COST, PRICING)]


def source(route):
    return (ROOT / route.strip('/') / 'index.html').read_text()


def before(route):
    path = route.strip('/') + '/index.html' if route != '/' else 'index.html'
    return subprocess.check_output(['git', 'show', BASELINE + ':' + path], cwd=ROOT, text=True)


def main(markup):
    return re.search(r'<main[^>]*>(.*?)</main>', markup, re.S).group(1)


class BuyerIntentTests(unittest.TestCase):
    def test_disclosed_examples_and_credit_are_numerically_complete(self):
        results = validate_examples()
        self.assertEqual(results['beach_total'], 335000)
        self.assertEqual(results['furnishing_total_with_contingency'], 39600)
        for value in ('$335,000', '$208,000', '$107,000', 'fully credited', 'not a coastal price range'):
            self.assertIn(value, source(COST))
        self.assertIn('not BNB Accelerator’s published price', source(PRICING))
        self.assertIn('$10,000', source(PRICING))

    def test_fourplex_paid_nights_cover_costs_and_round_up(self):
        base = fourplex_threshold()
        self.assertEqual(base['available_unit_nights'], 1420)
        n, contribution = base['required_paid_unit_nights'], base['contribution_per_paid_unit_night']
        self.assertLess((n - 1) * contribution, base['fixed_obligations'])
        self.assertGreaterEqual(n * contribution, base['fixed_obligations'])
        self.assertFalse(fourplex_threshold(adr=100)['feasible_within_inventory'])
        for kwargs in ({'adr': 30}, {'unavailable_extra': 1420}):
            with self.assertRaises(ValueError):
                fourplex_threshold(**kwargs)
        for value in ('1,420', '1,089', '76.7%', '1,257', '88.5%', '1,330', '81.9%', '897', '84.2%'):
            self.assertIn(value, source(BREAK_EVEN))
        self.assertIn('not accounting NOI or a DSCR numerator', source(BREAK_EVEN))

    def test_occupancy_and_revpar_keep_the_period_and_unit_definition(self):
        self.assertEqual(Decimal(16) / 20 * 100, 80)
        self.assertEqual((Decimal(16) / 30 * 100).quantize(Decimal('.1')), Decimal('53.3'))
        for value in ('346', '190', '$36,145', '$190.24', '54.9%', '52.1%', 'not market ranges'):
            self.assertIn(value, source(OCCUPANCY))
        for value in ('one unit', 'Future reserved stays', '$120', '$128', '$2,430', '$2,112', '$318'):
            self.assertIn(value, source(REVPAR))

    def test_local_claims_and_historical_evidence_have_explicit_limits(self):
        chandler, arizona = main(source(CHANDLER)), main(source(ARIZONA))
        for text in ('$695K', '$9.6K', '12–16%', 'actively helps', 'active markets listed'):
            self.assertNotIn(text, chandler)
        for text in ('$1.15M', '$15.4K', '11-15%', '$9.6K', 'poison', 'six figure deduction'):
            self.assertNotIn(text, arizona)
        self.assertIn('does not establish current BNB Accelerator service availability', chandler)
        self.assertIn('$993,000', arizona)
        self.assertIn('not independent deed verification', arizona)
        self.assertIn('no annual rental income or return', arizona)
        blocks = [json.loads(x) for x in re.findall(r'<script type="application/ld\+json">(.*?)</script>', source(CHANDLER), re.S)]
        types = [node.get('@type') for b in blocks for node in b.get('@graph', [b])]
        self.assertNotIn('Service', types)

    def test_seven_delivered_relationships_are_contextual(self):
        from audit_internal_inbound import Page
        for source_route, target in RELATIONSHIPS:
            links = Page(source(source_route), source_route).links
            self.assertIn((target, 'contextual'), links, (source_route, target))

    def test_legacy_renderers_retain_the_curated_owners(self):
        for route in PAGES:
            generated = tpl.page(title='obsolete title', description='obsolete description',
                                 path=route, body='obsolete body', og_title='obsolete OG')
            self.assertEqual(main(generated), main(source(route)))
            self.assertNotIn('obsolete', generated)
        for asset_slug, decision_slug in [('beach-house', 'investment-cost'), ('beach-house', 'furnishing-budget'), ('fourplex', 'break-even-occupancy')]:
            asset = next(a for a in investor.ASSETS if a[1] == asset_slug)
            decision = next(d for d in investor.DECISIONS if d[0] == decision_slug)
            route, generated = investor.guide(asset, decision)
            self.assertEqual(main(generated), main(source(route)))
        generated = local.market_page(next(m for m in local.MARKETS if m['slug'] == 'chandler'))
        self.assertEqual(main(generated), main(source(CHANDLER)))
        for slug in ('arizona-str-investing', 'airbnb-occupancy-rates-explained'):
            # Legacy payload still arrives complete; reviewed content must take precedence.
            data = dict(slug=slug, title='legacy', title_tag='legacy', h1='legacy',
                        description='legacy', category='legacy', lead='legacy', date='2026-08-01',
                        related=[], sections=[], faqs=[])
            self.assertEqual(main(blog.render_post(data)), main(source('/blog/' + slug + '/')))
        plain = tpl.page(title='Untouched', description='Untouched', path='/unreviewed-example/', body='<p>Untouched</p>')
        self.assertIn('<p>Untouched</p>', plain)
        self.assertIsNone(curated_payload('/unreviewed-example/'))

    def test_publication_shell_and_first_release_are_preserved(self):
        for route in PAGES:
            current, previous = source(route), before(route)
            self.assertEqual(re.findall(r'"datePublished":\s*"([^"]+)"', current),
                             re.findall(r'"datePublished":\s*"([^"]+)"', previous))
            for pattern in (r'<header class="site-header".*?</header>', r'<footer class="site-footer">.*?</footer>'):
                self.assertEqual(re.search(pattern, current, re.S).group(), re.search(pattern, previous, re.S).group())
            for asset in ('style.min.css', 'main.js'):
                pattern = rf'/assets/{re.escape(asset)}(?:\?v=[a-z0-9]+)?'
                self.assertEqual(re.search(pattern, current).group(), re.search(pattern, previous).group())
        for route in ('/apply/', '/case-studies/', '/case-studies/adam-florida-panhandle/',
                      '/case-studies/ashley-billy-fort-walton-beach/', '/management/', '/financing/dscr-loans/'):
            self.assertEqual(source(route), before(route), route)
        self.assertIn('https://mybnbaccelerator.com/schedule-bnb', source('/apply/'))

    def test_late_market_enhancer_preserves_the_reviewed_local_owner(self):
        with tempfile.TemporaryDirectory(prefix='bnb-generator-check-') as directory:
            root = Path(directory)
            shutil.copytree(ROOT / '_gen', root / '_gen', ignore=shutil.ignore_patterns('__pycache__'))
            for route in ('/markets/', CHANDLER, '/markets/scottsdale/'):
                path = root / route.strip('/') / 'index.html'
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(source(route))
            subprocess.run([sys.executable, '_gen/enhance_market_intent.py'], cwd=root,
                           check=True, capture_output=True)
            self.assertEqual((root / CHANDLER.strip('/') / 'index.html').read_text(), source(CHANDLER))

    def test_reviewed_articles_are_distinct_and_regeneration_is_stable(self):
        articles = {}
        for route in PAGES:
            article = re.search(r'<article class="article">(.*?)</article>', source(route), re.S).group(1)
            words = re.findall(r'[a-z0-9]+', html.unescape(re.sub('<[^>]+>', ' ', article)).lower())
            articles[route] = set(zip(*(words[i:] for i in range(5))))
        for a, b in combinations(PAGES, 2):
            overlap = len(articles[a] & articles[b]) / len(articles[a] | articles[b])
            self.assertLess(overlap, .35, (a, b, overlap))
        paths = [ROOT / r.strip('/') / 'index.html' for r in PAGES] + list(ROOT.glob('sitemap*.xml'))
        original = {p: p.read_bytes() for p in paths}
        subprocess.run([sys.executable, '_gen/refresh_buyer_intent.py'], cwd=ROOT, check=True, capture_output=True)
        self.assertEqual(original, {p: p.read_bytes() for p in paths})


if __name__ == '__main__':
    unittest.main()
