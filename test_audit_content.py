"""Exercise the audit against tiny independent sites, including negative checks."""
import subprocess
import json
import sys
import tempfile
import unittest
from pathlib import Path

AUDIT = Path(__file__).with_name('audit_content.py')
SITE = 'https://www.bnbaccelerator.com'

class AuditTests(unittest.TestCase):
    def audit(self, href, include_target=True, sitemap_target=True, metadata_suffix="", link_markup=None, redirects=None, alias_file=False, sitemap_alias=False):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'audit_content.py').write_text(AUDIT.read_text())
            (root / 'vercel.json').write_text(json.dumps({'redirects': redirects or []}))
            (root / 'robots.txt').write_text('User-agent: *\nAllow: /\n')
            def page(route, link=''):
                path = root / route.strip('/') / 'index.html'
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(f'<title>{route}</title><meta name="description" content="Description {route}{metadata_suffix}">\n<link rel="canonical" href="{SITE}{route}"><h1>{route}</h1>{link}')
            page('/', link_markup if link_markup is not None else f'<a href="{href}">Target</a>')
            if include_target:
                page('/target/')
            if alias_file:
                page('/alias/', '<a href="/target/">Hidden link</a>')
            urls = ([SITE + '/alias/'] if sitemap_alias else []) + [SITE + '/'] + ([SITE + '/target/'] if sitemap_target else [])
            (root / 'sitemap.xml').write_text('<urlset>' + ''.join(f'<url><loc>{url}</loc></url>' for url in urls) + '</urlset>')
            return subprocess.run([sys.executable, str(root / 'audit_content.py')], text=True, capture_output=True)

    def test_internal_url_forms(self):
        for href in ['/target/', SITE + '/target/?x=1#section', '/target/?x=1&amp;y=2', '//www.bnbaccelerator.com/target/']:
            with self.subTest(href=href):
                result = self.audit(href)
                self.assertEqual(result.returncode, 0, result.stdout)

    def test_external_origins_do_not_establish_reachability(self):
        for href in ['https://example.com/target/', 'https://www.bnbaccelerator.com.evil.example/target/', 'http://www.bnbaccelerator.com/target/', 'https://www.bnbaccelerator.com:444/target/']:
            with self.subTest(href=href):
                result = self.audit(href)
                self.assertEqual(result.returncode, 1)
                self.assertIn('page unreachable', result.stdout)

    def test_multislash_authority_cannot_establish_reachability(self):
        result = self.audit('///target/')
        self.assertEqual(result.returncode, 1)
        self.assertIn('malformed authority link ///target/', result.stdout)
        self.assertIn('page unreachable from homepage links: /target/', result.stdout)

    def test_control_characters_cannot_hide_external_authority(self):
        for control in ['\t', '\n', '\r']:
            for href in ['//' + control + '/target/', '/' + control + '//target/']:
                with self.subTest(href=href):
                    result = self.audit(href)
                    self.assertEqual(result.returncode, 1)
                    self.assertIn('control character in link', result.stdout)
                    self.assertIn('page unreachable from homepage links: /target/', result.stdout)

    def test_all_empty_numeric_reference_decodings_fail_closed(self):
        points = (list(range(1, 9)) + [11] + list(range(14, 32)) + [127]
                  + list(range(0xFDD0, 0xFDF0))
                  + [plane * 0x10000 + suffix for plane in range(17) for suffix in [0xFFFE, 0xFFFF]])
        self.assertEqual(len(points), 94)
        for hexadecimal in [False, True]:
            for terminated in [False, True]:
                for offset in [0, 47]:
                    references = [('&#x' + format(point, 'x') if hexadecimal else '&#' + str(point))
                                  + (';' if terminated else '') for point in points[offset:offset + 47]]
                    markup = ''.join(f'<a href="/tar{reference}get/">Target</a>' for reference in references)
                    with self.subTest(hexadecimal=hexadecimal, terminated=terminated, offset=offset):
                        result = self.audit('', link_markup=markup)
                        self.assertEqual(result.returncode, 1)
                        self.assertEqual(result.stdout.count('control character in link'), 47)
                        self.assertIn('page unreachable from homepage links: /target/', result.stdout)

    def test_reference_guard_covers_html_attribute_forms(self):
        for markup in ['<a href="/tar&#1;get/">', "<a href='/tar&#127;get/'>",
                       '<a HREF=/tar&#x1f;get/>', '<a HREF="/tar&#1;get/"/>',
                       '<a href="/target/?x=&#1;">', '<a href="/target/#&#1;">']:
            with self.subTest(markup=markup):
                result = self.audit('', link_markup=markup)
                self.assertEqual(result.returncode, 1)
                self.assertIn('control character in link', result.stdout)
                self.assertIn('page unreachable from homepage links: /target/', result.stdout)

    def test_normal_entities_and_nonlink_lookalikes_remain_valid(self):
        for href in ['/target/?x=1&amp;y=2', '/target&#47;', '/t&#97;rget/']:
            with self.subTest(href=href):
                result = self.audit(href)
                self.assertEqual(result.returncode, 0, result.stdout)
        markup = '<a href="/target/">Target</a><!-- <a href="/tar&#1;get/"> --><script>const example = \'<a href="/tar&#1;get/">\';</script>'
        result = self.audit('', metadata_suffix=' &lt;a href=&#1;', link_markup=markup)
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_href_text_inside_metadata_is_not_a_link(self):
        result = self.audit('/target/', metadata_suffix=' &lt;a href=')
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_path_parameters_are_not_discarded(self):
        for href in ['/target;missing', '/target/;missing', SITE + '/target;missing', '//www.bnbaccelerator.com/target/;missing']:
            with self.subTest(href=href):
                result = self.audit(href)
                self.assertEqual(result.returncode, 1)
                self.assertIn('missing route link', result.stdout)
                self.assertIn(';missing/', result.stdout)
                self.assertIn('page unreachable from homepage links: /target/', result.stdout)

    def test_missing_absolute_route_still_fails(self):
        result = self.audit(SITE + '/target/', False, False)
        self.assertIn('missing route link /target/', result.stdout)
        self.assertEqual(result.returncode, 1)

    def test_missing_absolute_file_still_fails(self):
        result = self.audit(SITE + '/missing.html', False, False)
        self.assertIn('missing file link /missing.html', result.stdout)
        self.assertEqual(result.returncode, 1)

    def test_missing_sitemap_entry_still_fails(self):
        result = self.audit(SITE + '/target/', True, False)
        self.assertIn('sitemap mismatch: missing 1, extra 0', result.stdout)
        self.assertEqual(result.returncode, 1)

class RedirectAuditTests(unittest.TestCase):
    audit = AuditTests.audit
    def test_retained_alias_is_not_an_indexable_page(self):
        result = self.audit('/alias/', redirects=[{'source': '/alias/', 'destination': '/target/'}], alias_file=True)
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_redirect_without_html_establishes_owner_reachability(self):
        result = self.audit('/alias/', redirects=[{'source': '/alias/', 'destination': '/target/'}])
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_redirect_in_sitemap_still_fails(self):
        result = self.audit('/alias/', redirects=[{'source': '/alias/', 'destination': '/target/'}], alias_file=True, sitemap_alias=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn('sitemap contains redirect source', result.stdout)

    def test_missing_redirect_owner_still_fails(self):
        result = self.audit('/alias/', include_target=False, sitemap_target=False, redirects=[{'source': '/alias/', 'destination': '/target/'}], alias_file=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn('redirect target missing: /target/', result.stdout)

    def test_hidden_alias_links_cannot_make_owner_reachable(self):
        result = self.audit('/', redirects=[{'source': '/alias/', 'destination': '/target/'}], alias_file=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn('page unreachable from homepage links: /target/', result.stdout)

    def test_redirect_cycle_still_fails(self):
        result = self.audit('/alias/', redirects=[{'source': '/alias/', 'destination': '/target/'}, {'source': '/target/', 'destination': '/alias/'}], alias_file=True, sitemap_target=False)
        self.assertEqual(result.returncode, 1)
        self.assertIn('redirect target missing', result.stdout)

class RedirectSitemapGeneratorTests(unittest.TestCase):
    def test_rebuild_omits_redirect_files_and_preserves_owner_date(self):
        import importlib.util
        from unittest.mock import patch
        from xml.etree import ElementTree as ET
        spec = importlib.util.spec_from_file_location('redirect_test_sitewide', AUDIT.parent / '_gen/sitewide.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'vercel.json').write_text(json.dumps({'redirects': [{'source': '/blog/alias/', 'destination': '/blog/owner/'}]}))
            with patch.object(module, 'ROOT', directory), patch.object(module, 'page_urls', return_value=[('/', 'home'), ('/blog/alias/', 'retained-file'), ('/blog/owner/', 'owner')]), patch.object(module, 'lastmod_for', return_value='2026-10-19'):
                entries = module.build_sitemap()
            self.assertEqual({entry[0] for entry in entries}, {'/', '/blog/owner/'})
            rows = ET.parse(root / 'sitemap-blog.xml').getroot()
            values = [{node.tag.rsplit('}', 1)[-1]: node.text for node in row} for row in rows]
            self.assertEqual(len(values), 1)
            self.assertEqual(values[0]['loc'], SITE + '/blog/owner/')
            self.assertEqual(values[0]['lastmod'], '2026-10-19')

if __name__ == '__main__':
    unittest.main()
