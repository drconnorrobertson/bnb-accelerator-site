#!/usr/bin/env python3
"""Sitewide passes: replace the footer everywhere, then rebuild sitemap.xml.

The footer is the site's comprehensive navigation layer, so it is generated
once in tpl.footer() and stamped across every page rather than maintained by
hand in 300 files.
"""
import datetime
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tpl

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

FOOTER_RE = re.compile(r'<footer class="site-footer">.*?</html>\s*\Z', re.S)


def rewrite_footers():
    new = tpl.footer()
    n = 0
    for f in sorted(glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True)):
        if "/_gen/" in f:
            continue
        s = open(f, encoding="utf-8").read()
        if '<footer class="site-footer">' not in s:
            continue
        # keep whatever asset hash the page already carries; build_assets restamps
        out = FOOTER_RE.sub(lambda _: new, s, count=1)
        if out != s:
            open(f, "w", encoding="utf-8").write(out)
            n += 1
    print(f"footer: rewritten on {n} pages")


# ------------------------------------------------------------------ sitemap

# Higher priority sections first; anything not listed defaults to 0.6.
PRIORITY = [
    ("/", "1.0", "weekly"),
    ("/apply/", "0.9", "monthly"),
    ("/how-it-works/", "0.9", "monthly"),
    ("/case-studies/", "0.9", "weekly"),
    ("/tax-strategy/", "0.9", "monthly"),
    ("/markets/", "0.9", "weekly"),
    ("/property-types/", "0.8", "monthly"),
    ("/regulations/", "0.8", "monthly"),
    ("/financing/", "0.8", "monthly"),
    ("/revenue-projections/", "0.8", "monthly"),
    ("/management/", "0.8", "monthly"),
    ("/design/", "0.8", "monthly"),
    ("/compare/", "0.8", "weekly"),
    ("/blog/", "0.8", "daily"),
    ("/testimonials/", "0.8", "monthly"),
    ("/guides/", "0.7", "monthly"),
    ("/tools/", "0.7", "monthly"),
    ("/data/", "0.7", "monthly"),
    ("/answers/", "0.7", "monthly"),
    ("/faq/", "0.7", "monthly"),
    ("/partners/", "0.6", "monthly"),
    ("/sitemap/", "0.5", "monthly"),
]

SKIP = {"/404.html"}


def page_urls():
    """Every indexable page, as a site-root path with trailing slash."""
    out = []
    for f in sorted(glob.glob(os.path.join(ROOT, "**", "index.html"), recursive=True)):
        rel = os.path.relpath(f, ROOT)
        path = "/" + os.path.dirname(rel).replace(os.sep, "/")
        if path == "/.":
            path = "/"
        elif not path.endswith("/"):
            path += "/"
        if path in SKIP:
            continue
        s = open(f, encoding="utf-8").read()
        if 'name="robots" content="noindex' in s:
            continue
        out.append((path, f))
    return out


def classify(path):
    for prefix, prio, freq in PRIORITY:
        if path == prefix:
            return prio, freq
    for prefix, prio, freq in PRIORITY:
        if prefix != "/" and path.startswith(prefix):
            # child pages sit one step below their hub
            child = f"{max(0.5, float(prio) - 0.1):.1f}"
            return child, freq
    return "0.6", "monthly"


def lastmod_for(path, f):
    """Blog posts use their published date; everything else uses today."""
    if path.startswith("/blog/") and path != "/blog/":
        s = open(f, encoding="utf-8").read()
        m = re.search(r'"dateModified":\s*"([0-9-]+)"', s)
        if m:
            return m.group(1)
        m = re.search(r'"datePublished":\s*"([0-9-]+)"', s)
        if m:
            return m.group(1)
    return TODAY


TODAY = datetime.date(2026, 8, 15).isoformat()


def build_sitemap():
    entries = []
    for path, f in page_urls():
        prio, freq = classify(path)
        entries.append((path, lastmod_for(path, f), freq, prio))

    # sort by descending priority, then path, so the important URLs lead
    entries.sort(key=lambda e: (-float(e[3]), e[0]))

    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for path, mod, freq, prio in entries:
        lines.append("  <url>")
        lines.append(f"    <loc>{tpl.SITE}{path}</loc>")
        lines.append(f"    <lastmod>{mod}</lastmod>")
        lines.append(f"    <changefreq>{freq}</changefreq>")
        lines.append(f"    <priority>{prio}</priority>")
        lines.append("  </url>")
    lines.append("</urlset>")
    lines.append("")

    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write("\n".join(lines))
    print(f"sitemap: {len(entries)} URLs")
    return entries


if __name__ == "__main__":
    rewrite_footers()
    build_sitemap()
