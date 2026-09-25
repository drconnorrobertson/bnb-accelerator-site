#!/usr/bin/env python3
"""Sitewide passes: replace shared navigation, then rebuild sitemap.xml.

The header and footer are generated once in tpl.py and stamped across every
page rather than maintained by hand in hundreds of files.
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
HEADER_RE = re.compile(
    r'(?:<a class="skip-link"[^>]*>.*?</a>\s*)?'
    r'<header class="site-header"[^>]*>.*?</header>',
    re.S,
)


def active_nav(path):
    """Map deep sections to one of the five primary navigation destinations."""
    section = path.strip("/").split("/", 1)[0]
    if section == "how-it-works":
        return "/how-it-works/"
    if section == "markets":
        return "/markets/"
    if section == "scenarios":
        return "/scenarios/"
    if section in {"case-studies", "deals", "wins", "testimonials", "reviews"}:
        return "/case-studies/"
    if section == "about":
        return "/about/"
    if section in {"blog", "guides", "topics", "answers", "data", "tools",
                   "regulations", "tax-strategy", "financing", "design",
                   "management", "compare"}:
        return "/blog/"
    return None


def rewrite_headers():
    n = 0
    for path, f in page_urls():
        s = open(f, encoding="utf-8").read()
        match = HEADER_RE.search(s)
        if not match:
            continue
        transparent = 'data-start="transparent"' in match.group(0)
        out = HEADER_RE.sub(
            lambda _: tpl.header(active=active_nav(path), transparent=transparent),
            s,
            count=1,
        )
        if out != s:
            open(f, "w", encoding="utf-8").write(out)
            n += 1
    print(f"header: rewritten on {n} pages")


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
    ("/scenarios/", "0.8", "weekly"),
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
    if path == "/blog/":
        dates = []
        for post_file in glob.glob(os.path.join(ROOT, "blog", "*", "index.html")):
            source = open(post_file, encoding="utf-8").read()
            match = re.search(r'"datePublished":\s*"([0-9-]+)"', source)
            if match:
                dates.append(match.group(1))
        return max(dates) if dates else TODAY
    if path in SEPTEMBER_22_RELEASE:
        return "2026-09-22"
    if path.startswith("/blog/") and path != "/blog/":
        s = open(f, encoding="utf-8").read()
        m = re.search(r'"dateModified":\s*"([0-9-]+)"', s)
        if m:
            return m.group(1)
        m = re.search(r'"datePublished":\s*"([0-9-]+)"', s)
        if m:
            return m.group(1)
    return TODAY


TODAY = datetime.date.today().isoformat()
SEPTEMBER_22_RELEASE = {
    "/blog/",
    "/markets/",
    "/markets/chandler/",
    "/markets/davenport/",
    "/markets/fort-walton-beach/",
    "/markets/gilbert/",
    "/markets/jacksonville/",
    "/markets/jim-thorpe/",
    "/markets/johnson-city/",
    "/markets/lake-harmony/",
    "/markets/manchaca/",
    "/markets/mesa/",
    "/markets/sevierville/",
    "/markets/tobyhanna/",
}


def sitemap_group(path):
    """Put each URL in one diagnostic sitemap without changing indexability."""
    if path.startswith("/guides/str-investment/"):
        return "investor-guides"
    if path.startswith("/blog/"):
        return "blog"
    if path.startswith("/scenarios/"):
        return "scenarios"
    if path.startswith("/markets/") or path.startswith("/regulations/"):
        return "markets"
    if path.startswith(("/case-studies/", "/wins/", "/testimonials/", "/reviews/")):
        return "proof"
    return "core"


def render_urlset(entries):
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for path, mod, freq, prio in entries:
        lines.append("  <url>")
        lines.append(f"    <loc>{tpl.SITE}{path}</loc>")
        lines.append(f"    <lastmod>{mod}</lastmod>")
        lines.append(f"    <changefreq>{freq}</changefreq>")
        lines.append(f"    <priority>{prio}</priority>")
        lines.append("  </url>")
    lines.extend(["</urlset>", ""])
    return "\n".join(lines)


def build_sitemap():
    entries = []
    for path, f in page_urls():
        prio, freq = classify(path)
        entries.append((path, lastmod_for(path, f), freq, prio))

    # sort by descending priority, then path, so the important URLs lead
    entries.sort(key=lambda e: (-float(e[3]), e[0]))

    groups = {name: [] for name in ("core", "investor-guides", "blog", "scenarios", "markets", "proof")}
    for entry in entries:
        groups[sitemap_group(entry[0])].append(entry)

    for name, grouped in groups.items():
        filename = f"sitemap-{name}.xml"
        open(os.path.join(ROOT, filename), "w", encoding="utf-8").write(render_urlset(grouped))

    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for name, grouped in groups.items():
        latest = max((entry[1] for entry in grouped), default=TODAY)
        lines.extend(["  <sitemap>",
                      f"    <loc>{tpl.SITE}/sitemap-{name}.xml</loc>",
                      f"    <lastmod>{latest}</lastmod>",
                      "  </sitemap>"])
    lines.extend(["</sitemapindex>", ""])
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write("\n".join(lines))
    summary = ", ".join(f"{name}={len(grouped)}" for name, grouped in groups.items())
    print(f"sitemap index: {len(entries)} URLs ({summary})")
    return entries


if __name__ == "__main__":
    rewrite_headers()
    rewrite_footers()
    build_sitemap()
