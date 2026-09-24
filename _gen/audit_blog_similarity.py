#!/usr/bin/env python3
"""Fail when a same-day blog batch contains suspiciously similar article copy."""
import argparse
import glob
import html
import os
import re
from itertools import combinations

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def article_text(path):
    source = open(path, encoding="utf-8").read()
    match = re.search(r'<article class="article".*?</article>', source, re.S)
    article = match.group(0) if match else source
    article = re.sub(r"<script.*?</script>|<style.*?</style>", " ", article, flags=re.S)
    article = re.sub(r"<[^>]+>", " ", article)
    return re.sub(r"\s+", " ", html.unescape(article)).strip().lower()


def shingles(text, width=5):
    words = re.findall(r"[a-z0-9']+", text)
    return {tuple(words[i:i + width]) for i in range(len(words) - width + 1)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", required=True)
    parser.add_argument("--expected", type=int, required=True)
    parser.add_argument("--max-jaccard", type=float, default=0.56)
    args = parser.parse_args()

    paths = []
    for path in glob.glob(os.path.join(ROOT, "blog", "*", "index.html")):
        source = open(path, encoding="utf-8").read()
        if f'"datePublished": "{args.date}"' in source:
            paths.append(path)
    if len(paths) != args.expected:
        raise SystemExit(f"expected {args.expected} dated pages, found {len(paths)}")

    sets = {path: shingles(article_text(path)) for path in paths}
    scored = []
    for left, right in combinations(paths, 2):
        union = sets[left] | sets[right]
        score = len(sets[left] & sets[right]) / len(union) if union else 1.0
        scored.append((score, left, right))
    scored.sort(reverse=True)
    top = scored[:5]
    for score, left, right in top:
        print(f"{score:.3f}  {os.path.basename(os.path.dirname(left))}  {os.path.basename(os.path.dirname(right))}")
    if top and top[0][0] > args.max_jaccard:
        raise SystemExit(f"maximum similarity {top[0][0]:.3f} exceeds {args.max_jaccard:.3f}")
    print(f"similarity audit: {len(paths)} pages, {len(scored)} pairs, max {top[0][0]:.3f}")


if __name__ == "__main__":
    main()
