#!/usr/bin/env python3
"""Fast, dependency-free crawlability audit for the static content library.

Run after generating pages and before publishing: python3 audit_content.py
This checks eligibility and site wiring. Search engines still decide what to index.
"""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from xml.etree import ElementTree as ET
import json
import re
import sys
from urllib.parse import urlparse, urlsplit

SOURCE_ROOT = Path(__file__).resolve().parent
# Optional output root lets the same checks validate the deployed build.
ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else SOURCE_ROOT
SITE = "https://www.bnbaccelerator.com"
ERRORS = []
# Post-appointment preparation is public but intentionally excluded from search.
# Keep this explicit: editorial pages must not silently bypass indexing checks.
NONINDEXABLE_ROUTES = {"/scb-precall/"}


class LinkParser(HTMLParser):
    """Read actual href attributes, excluding href-like text in metadata."""
    def __init__(self):
        super().__init__()
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        self.hrefs.extend(value for name, value in attrs if name == "href" and value is not None)


def route(path):
    relative = path.relative_to(ROOT)
    return "/" if relative == Path("index.html") else "/" + relative.parent.as_posix() + "/"


pages = {route(path): path for path in ROOT.rglob("index.html") if ".git" not in path.parts and "public" not in path.relative_to(ROOT).parts}
titles = Counter()
descriptions = Counter()
link_graph = {}

for url, path in pages.items():
    source = path.read_text(encoding="utf-8")
    link_graph[url] = set()
    title = re.search(r"<title>(.*?)</title>", source, re.S)
    description = re.search(r'<meta name="description" content="([^"]+)"', source)
    canonical = re.search(r'<link rel="canonical" href="([^"]+)"', source)
    if not title or not description or not canonical:
        ERRORS.append(f"{url}: missing title, description, or canonical")
        continue
    titles[title.group(1)] += 1
    descriptions[description.group(1)] += 1
    if canonical.group(1) != SITE + url:
        ERRORS.append(f"{url}: canonical points to {canonical.group(1)}")
    noindex = bool(re.search(r'<meta name="robots"[^>]*noindex', source))
    if url in NONINDEXABLE_ROUTES and not noindex:
        ERRORS.append(f"{url}: appointment preparation must remain noindex")
    if noindex and url not in NONINDEXABLE_ROUTES:
        ERRORS.append(f"{url}: noindex is present")
    if len(re.findall(r"<h1(?:\s|>)", source)) != 1:
        ERRORS.append(f"{url}: expected one H1")
    for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', source, re.S):
        try:
            json.loads(block)
        except json.JSONDecodeError as exc:
            ERRORS.append(f"{url}: invalid JSON-LD: {exc}")
    links = LinkParser()
    links.feed(source)
    for href in links.hrefs:
        # URL parsers strip controls, which can hide an external authority.
        # Reject the raw spelling before any parser normalization occurs.
        if any(ord(character) < 32 or ord(character) == 127 for character in href):
            ERRORS.append(f"{url}: control character in link {href!r}")
            continue
        # Browsers interpret extra leading slashes as an authority, while
        # urllib can parse them as a local path. Reject this ambiguous spelling.
        if href.startswith("///"):
            ERRORS.append(f"{url}: malformed authority link {href}")
            continue
        # Keep semicolons in the path: /target;missing is not /target/.
        parsed = urlsplit(href)
        if parsed.netloc:
            if (parsed.scheme or "https", parsed.netloc) != (urlparse(SITE).scheme, urlparse(SITE).netloc):
                continue
        elif parsed.scheme or not href.startswith("/"):
            continue
        target = parsed.path
        if not target or target == "/" or target.startswith("/assets/"):
            continue
        if target.endswith((".xml", ".txt", ".html", ".svg", ".css", ".js")):
            if not (ROOT / target.lstrip("/")).exists():
                ERRORS.append(f"{url}: missing file link {target}")
            continue
        target = target.rstrip("/") + "/"
        link_graph[url].add(target)
        if target not in pages:
            ERRORS.append(f"{url}: missing route link {target}")
    for asset in re.findall(r'(?:href|src)=["\'](/assets/[^"\']+)', source):
        asset_path = asset.split("?", 1)[0].split("#", 1)[0]
        if not (ROOT / asset_path.lstrip("/")).exists():
            ERRORS.append(f"{url}: missing asset {asset_path}")

robots = (ROOT / "robots.txt").read_text(encoding="utf-8")
if "Disallow: /*?*v=" in robots and any("/assets/style.min.css?v=" in p.read_text(encoding="utf-8") for p in pages.values()):
    ERRORS.append("robots.txt blocks the versioned CSS used by site pages")

for label, values in (("title", titles), ("description", descriptions)):
    for value, count in values.items():
        if count > 1:
            ERRORS.append(f"duplicate {label} ({count} pages): {value[:90]}")

try:
    sitemap = ET.parse(ROOT / "sitemap.xml")
    root_tag = sitemap.getroot().tag
    if root_tag.endswith("sitemapindex"):
        listed = []
        child_urls = [item.text for item in sitemap.iter() if item.tag.endswith("loc")]
        for child_url in child_urls:
            child_name = child_url.rsplit("/", 1)[-1]
            child_path = ROOT / child_name
            if not child_path.exists():
                ERRORS.append(f"sitemap index references missing file: {child_name}")
                continue
            child = ET.parse(child_path)
            listed.extend(item.text for item in child.iter() if item.tag.endswith("loc"))
    else:
        listed = [item.text for item in sitemap.iter() if item.tag.endswith("loc")]
    if len(listed) != len(set(listed)):
        ERRORS.append("sitemap contains duplicate URLs")
    wanted = {SITE + url for url in pages if url not in NONINDEXABLE_ROUTES}
    if set(listed) != wanted:
        ERRORS.append(f"sitemap mismatch: missing {len(wanted - set(listed))}, extra {len(set(listed) - wanted)}")
    for url in listed:
        if urlparse(url).netloc != urlparse(SITE).netloc:
            ERRORS.append(f"sitemap URL uses unexpected host: {url}")
except (OSError, ET.ParseError) as exc:
    ERRORS.append(f"invalid sitemap: {exc}")

config = json.loads((SOURCE_ROOT / "vercel.json").read_text(encoding="utf-8"))
sources = [entry["source"] for entry in config.get("redirects", [])]
if len(sources) != len(set(sources)):
    ERRORS.append("duplicate redirect sources")
for entry in config.get("redirects", []):
    if entry["source"] in pages:
        ERRORS.append(f"redirect shadows an indexable page: {entry['source']}")
    if config.get("trailingSlash") and not entry["source"].endswith("/"):
        ERRORS.append(f"redirect source lacks trailing slash: {entry['source']}")
    if entry["destination"] not in pages:
        ERRORS.append(f"redirect target missing: {entry['destination']}")

# A sitemap entry alone does not establish a navigable path from the homepage.
reachable = set()
pending = ["/"]
while pending:
    current = pending.pop()
    if current in reachable:
        continue
    reachable.add(current)
    pending.extend(link_graph.get(current, set()) - reachable)
for url in pages.keys() - reachable - NONINDEXABLE_ROUTES:
    ERRORS.append(f"page unreachable from homepage links: {url}")

if ERRORS:
    print("Content audit failed:")
    for error in ERRORS[:60]:
        print(" -", error)
    if len(ERRORS) > 60:
        print(f" ... {len(ERRORS) - 60} more")
    sys.exit(1)

print(f"PASS: {len(pages)} HTML routes, {len(listed)} sitemap URLs, unique metadata, valid JSON-LD, live internal targets, and {len(sources)} valid redirect rules")
