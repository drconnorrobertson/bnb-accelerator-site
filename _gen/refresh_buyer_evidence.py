#!/usr/bin/env python3
"""Refresh only the reviewed cohort; preserve shared design and publication dates.

Run: python3 _gen/refresh_buyer_evidence.py
The renderer hooks also apply the curated content during ordinary regeneration.
"""
from pathlib import Path
import re
import blog
import case_studies
import pillars
from buyer_evidence import GUIDES, POSTS, REVIEWED

ROOT = Path(__file__).resolve().parents[1]


def save(route, generated):
    path = ROOT / route.strip("/") / "index.html"
    existing = path.read_text()
    # No shared design work in this pass. Retain the deployed navigation/footer
    # and current asset URLs rather than restamping 2,412 unrelated pages.
    for pattern in (r'<header class="site-header".*?</header>',
                    r'<footer class="site-footer">.*?</footer>'):
        current = re.search(pattern, existing, re.S)
        if current:
            generated = re.sub(pattern, lambda _: current.group(), generated, count=1, flags=re.S)
    for asset in ("style.min.css", "main.js"):
        pattern = rf'/assets/{re.escape(asset)}(?:\?v=[a-z0-9]+)?'
        current = re.search(pattern, existing)
        if current:
            generated = re.sub(pattern, lambda _: current.group(), generated)
    path.write_text(generated)


def main():
    updated = set()
    recs = case_studies.records()
    for record in recs:
        if record.get("evidence_reviewed"):
            route = f'/case-studies/{record["slug"]}/'
            save(route, case_studies.render_landing(record, recs))
            updated.add(route)
    save("/case-studies/", case_studies.render_index(recs))
    updated.add("/case-studies/")
    for slug in POSTS:
        route = f"/blog/{slug}/"
        current = (ROOT / route.strip("/") / "index.html").read_text()
        date = re.search(r'"datePublished":\s*"([^"]+)"', current).group(1)
        save(route, blog.render_post(dict(slug=slug, date=date)))
        updated.add(route)
    for route, content in GUIDES.items():
        parts = route.strip("/").split("/")
        parent = "/" + parts[0] + "/"
        save(route, pillars.guide(
            slug=parts[1] if len(parts) > 1 else "", parent=parent,
            parent_name=parts[0].title(), related=[], section_name="STR Buyer Decisions",
            **content))
        updated.add(route)
    # Update only reviewed routes' lastmod values without reformatting XML.
    for path in ROOT.glob("sitemap-*.xml"):
        def stamp(match):
            block = match.group()
            location = re.search(r'<loc>(.*?)</loc>', block).group(1)
            route = location.removeprefix("https://www.bnbaccelerator.com")
            return re.sub(r'<lastmod>.*?</lastmod>', f'<lastmod>{REVIEWED}</lastmod>', block) if route in updated else block
        path.write_text(re.sub(r'<url>.*?</url>', stamp, path.read_text(), flags=re.S))
    print(f"Reviewed cohort: {len(updated)} existing routes refreshed; no new routes.")


if __name__ == "__main__":
    main()
