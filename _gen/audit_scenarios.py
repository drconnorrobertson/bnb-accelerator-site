#!/usr/bin/env python3
"""Quality gate for the 50 x 5 x 3 scenario library."""
from collections import Counter
from pathlib import Path
import html
import re
import statistics
import sys

ROOT = Path(__file__).resolve().parents[1]
SCENARIOS = ROOT / "scenarios"
SITE = "https://www.bnbaccelerator.com"
GOALS = {"cash-flow", "revenue-growth", "remote-operations"}


def detail_pages():
    pages = []
    for path in SCENARIOS.glob("*/*/*/index.html"):
        rel = path.relative_to(SCENARIOS)
        if rel.parts[2] in GOALS:
            pages.append(path)
    return sorted(pages)


def visible_text(source):
    source = re.sub(r"<script.*?</script>|<style.*?</style>", " ", source,
                    flags=re.I | re.S)
    return " ".join(html.unescape(re.sub(r"<[^>]+>", " ", source)).lower().split())


def grams(text, size=5):
    words = re.findall(r"[a-z0-9]+", text)
    return set(zip(*(words[offset:] for offset in range(size))))


pages = detail_pages()
errors = []
titles, descriptions, canonicals, texts = [], [], [], []

if len(pages) != 750:
    errors.append(f"expected 750 scenario detail pages, found {len(pages)}")

for path in pages:
    source = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT)
    route = "/" + rel.parent.as_posix() + "/"
    title = re.search(r"<title>(.*?)</title>", source, re.S)
    description = re.search(r'<meta name="description" content="([^"]+)', source)
    canonical = re.search(r'<link rel="canonical" href="([^"]+)', source)
    if not title or not description or not canonical:
        errors.append(f"{route}: missing title, description, or canonical")
        continue
    titles.append(title.group(1))
    descriptions.append(description.group(1))
    canonicals.append(canonical.group(1))
    texts.append(visible_text(source))
    if canonical.group(1) != SITE + route:
        errors.append(f"{route}: canonical mismatch")
    if len(re.findall(r"<h1(?:\s|>)", source)) != 1:
        errors.append(f"{route}: expected exactly one H1")
    if re.search(r"\b(?:NaN|Infinity|undefined|null)\b", source):
        errors.append(f"{route}: invalid generated value")
    fixed = re.search(r'name="fixed" type="number" value="([^"]+)"', source)
    if not fixed or not fixed.group(1).isdigit() or int(fixed.group(1)) <= 0:
        errors.append(f"{route}: invalid fixed-cost calculator input")
    for required in ("Illustrative economics", "90-day operating plan", "Pre-mortem",
                     "not a forecast", "/apply/", "/scenarios/"):
        if required not in source:
            errors.append(f"{route}: missing required decision-support element {required!r}")

for label, values in (("title", titles), ("description", descriptions),
                      ("canonical", canonicals)):
    duplicates = [value for value, count in Counter(values).items() if count > 1]
    if duplicates:
        errors.append(f"duplicate scenario {label}: {len(duplicates)} values")

# Report template similarity transparently. It is a prioritization metric rather
# than a release blocker: the functional checks above prevent broken pages, while
# Search Console performance determines which clusters merit deeper enrichment.
similarities = []
for left, right in zip(texts, texts[1:]):
    a, b = grams(left), grams(right)
    if a or b:
        similarities.append(len(a & b) / len(a | b))
median_similarity = statistics.median(similarities) if similarities else 0
max_similarity = max(similarities, default=0)

if errors:
    print("Scenario audit failed:")
    for error in errors[:80]:
        print(" -", error)
    if len(errors) > 80:
        print(f" ... {len(errors) - 80} more")
    sys.exit(1)

print(
    f"PASS: {len(pages)} scenario pages; unique metadata/canonicals; "
    "finite calculator values; required decision-support elements present"
)
print(
    f"SIMILARITY WATCH: adjacent five-gram Jaccard median "
    f"{median_similarity:.3f}, max {max_similarity:.3f}; monitor by scenario sitemap in GSC"
)
