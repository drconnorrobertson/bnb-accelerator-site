"""Exercise the audit against tiny independent sites, including negative checks."""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

AUDIT = Path(__file__).with_name('audit_content.py')
SITE = 'https://www.bnbaccelerator.com'

class AuditTests(unittest.TestCase):
    def audit(self, href, include_target=True, sitemap_target=True):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'audit_content.py').write_text(AUDIT.read_text())
            (root / 'vercel.json').write_text('{"redirects": []}')
            (root / 'robots.txt').write_text('User-agent: *\nAllow: /\n')
            def page(route, link=''):
                path = root / route.strip('/') / 'index.html'
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(f'<title>{route}</title><meta name="description" content="Description {route}"><link rel="canonical" href="{SITE}{route}"><h1>{route}</h1>{link}')
            page('/', f'<a href="{href}">Target</a>')
            if include_target:
                page('/target/')
            urls = [SITE + '/'] + ([SITE + '/target/'] if sitemap_target else [])
            (root / 'sitemap.xml').write_text('<urlset>' + ''.join(f'<url><loc>{url}</loc></url>' for url in urls) + '</urlset>')
            return subprocess.run([sys.executable, str(root / 'audit_content.py')], text=True, capture_output=True)

    def test_internal_url_forms(self):
        for href in ['/target/', SITE + '/target/?x=1#section', '//www.bnbaccelerator.com/target/']:
            with self.subTest(href=href):
                result = self.audit(href)
                self.assertEqual(result.returncode, 0, result.stdout)

    def test_external_origins_do_not_establish_reachability(self):
        for href in ['https://example.com/target/', 'https://www.bnbaccelerator.com.evil.example/target/', 'http://www.bnbaccelerator.com/target/', 'https://www.bnbaccelerator.com:444/target/']:
            with self.subTest(href=href):
                result = self.audit(href)
                self.assertEqual(result.returncode, 1)
                self.assertIn('page unreachable', result.stdout)

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
