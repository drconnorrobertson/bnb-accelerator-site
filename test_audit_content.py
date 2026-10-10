"""Exercise the audit against tiny independent sites, including negative checks."""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

AUDIT = Path(__file__).with_name('audit_content.py')
SITE = 'https://www.bnbaccelerator.com'

class AuditTests(unittest.TestCase):
    def audit(self, href, include_target=True, sitemap_target=True, metadata_suffix="", link_markup=None):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'audit_content.py').write_text(AUDIT.read_text())
            (root / 'vercel.json').write_text('{"redirects": []}')
            (root / 'robots.txt').write_text('User-agent: *\nAllow: /\n')
            def page(route, link=''):
                path = root / route.strip('/') / 'index.html'
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(f'<title>{route}</title><meta name="description" content="Description {route}{metadata_suffix}">\n<link rel="canonical" href="{SITE}{route}"><h1>{route}</h1>{link}')
            page('/', link_markup if link_markup is not None else f'<a href="{href}">Target</a>')
            if include_target:
                page('/target/')
            urls = [SITE + '/'] + ([SITE + '/target/'] if sitemap_target else [])
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

if __name__ == '__main__':
    unittest.main()
