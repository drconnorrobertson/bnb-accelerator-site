#!/usr/bin/env python3
"""Fast, dependency-free crawlability audit for the static content library.

Run after generating pages and before publishing: python3 audit_content.py
This checks eligibility and site wiring. Search engines still decide what to index.
"""
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree as ET
import json
import re
import sys

ROOT = Path(__file__).resolve().parent
SITE = "https://www.bnbaccelerator.com"
ERRORS = []


def route(path):
    relative = path.relative_to(ROOT)
    return "/" if relative == Path("index.html") else "/" + relative.parent.as_posix() + "/"


pages = {route(path): path for path in ROOT.rglob("index.html") if ".git" not in path.parts}
titles = Counter()
descriptions = Counter()

for url, path in pages.items():
    source = path.read_text(encoding="utf-8")
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
    if re.search(r'<meta name="robots"[^>]*noindex', source):
        ERRORS.append(f"{url}: noindex is present")
    if len(re.findall(r"<h1(?:\s|>)", source)) != 1:
        ERRORS.append(f"{url}: expected one H1")
    for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', source, re.S):
        try:
            json.loads(block)
        except json.JSONDecodeError as exc:
            ERRORS.append(f"{url}: invalid JSON-LD: {exc}")
    for href in re.findall(r'href=["\']([^"\']+)', source):
        if not href.startswith("/") or href.startswith("//"):
            continue
        target = href.split("?", 1)[0].split("#", 1)[0]
        if not target or target == "/" or target.startswith("/assets/"):
            continue
        if target.endswith((".xml", ".txt", ".html", ".svg")):
            if not (ROOT / target.lstrip("/")).exists():
                ERRORS.append(f"{url}: missing file link {target}")
            continue
        target = target.rstrip("/") + "/"
        if target not in pages:
            ERRORS.append(f"{url}: missing route link {target}")

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
    wanted = {SITE + url for url in pages}
    if set(listed) != wanted:
        ERRORS.append(f"sitemap mismatch: missing {len(wanted - set(listed))}, extra {len(set(listed) - wanted)}")
except (OSError, ET.ParseError) as exc:
    ERRORS.append(f"invalid sitemap: {exc}")

config = json.loads((ROOT / "vercel.json").read_text(encoding="utf-8"))
sources = [entry["source"] for entry in config.get("redirects", [])]
if len(sources) != len(set(sources)):
    ERRORS.append("duplicate redirect sources")
for entry in config.get("redirects", []):
    if config.get("trailingSlash") and not entry["source"].endswith("/"):
        ERRORS.append(f"redirect source lacks trailing slash: {entry['source']}")
    if entry["destination"] not in pages:
        ERRORS.append(f"redirect target missing: {entry['destination']}")

if ERRORS:
    print("Content audit failed:")
    for error in ERRORS[:60]:
        print(" -", error)
    if len(ERRORS) > 60:
        print(f" ... {len(ERRORS) - 60} more")
    sys.exit(1)

print(f"PASS: {len(pages)} HTML routes, {len(listed)} sitemap URLs, unique metadata, valid JSON-LD, live internal targets, and {len(sources)} valid redirect rules")
