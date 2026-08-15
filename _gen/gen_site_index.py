#!/usr/bin/env python3
"""Rebuild /sitemap/ (the human site index) from what is actually on disk.

Every page gets its H1 as the link text, grouped by section in a deliberate
order so the index reads as navigation rather than as a dump.
"""
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tpl
from pillars import write

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

# (path prefix, section heading, blurb). Order controls the page.
SECTIONS = [
    ("__main__", "Main pages", None),
    ("/case-studies/", "Client case studies",
     "Documented outcomes with real markets, purchase prices and cash flow where the client authorised publication."),
    ("/markets/", "Market analyses",
     "Estimated revenue, nightly rate, occupancy and regulation for each market we track."),
    ("/property-types/", "Property type guides",
     "What drives revenue in beach, mountain, lake, city, ski and desert short-term rentals, and what breaks."),
    ("/regulations/", "Short-term rental rules by state",
     "Preemption laws, permit caps, city positions and what to verify before writing an offer."),
    ("/tax-strategy/", "Tax strategy",
     "The seven day rule, material participation and cost segregation, explained as mechanics rather than advice."),
    ("/financing/", "Financing",
     "DSCR loans, conventional investment financing, down payment sources and total entry cost."),
    ("__playbooks__", "Playbooks",
     "Design and furnishing, property management, and building a revenue projection you can defend."),
    ("/compare/", "Comparisons",
     "How our approach compares with other programs, providers and doing it yourself."),
    ("/answers/", "Short answers", None),
    ("/data/", "Market data", None),
    ("/guides/", "Guides and downloads", None),
    ("/tools/", "Tools and calculators", None),
    ("/blog/", "Blog", "Every article, newest first."),
]

MAIN = ["/", "/how-it-works/", "/markets/", "/case-studies/", "/testimonials/",
        "/tax-strategy/", "/property-types/", "/regulations/", "/financing/",
        "/revenue-projections/", "/design/", "/management/", "/compare/",
        "/faq/", "/apply/", "/partners/", "/blog/", "/answers/", "/data/",
        "/guides/", "/tools/"]

PLAYBOOKS = ["/design/", "/management/", "/revenue-projections/"]


def scan():
    """path -> (h1, datePublished or '')"""
    out = {}
    for f in glob.glob(os.path.join(ROOT, "**", "index.html"), recursive=True):
        rel = os.path.relpath(f, ROOT)
        d = os.path.dirname(rel).replace(os.sep, "/")
        path = "/" if d == "" else f"/{d}/"
        s = open(f, encoding="utf-8").read()
        m = re.search(r"<h1>(.*?)</h1>", s, re.S)
        h1 = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", m.group(1))).strip() if m else path
        m = re.search(r'"datePublished":\s*"([0-9-]+)"', s)
        out[path] = (h1, m.group(1) if m else "")
    return out


def li(path, h1):
    return f'          <li><a href="{path}">{tpl.esc(h1)}</a></li>'


def main():
    pages = scan()
    used = set()
    blocks = []
    total = len(pages)

    for prefix, heading, blurb in SECTIONS:
        if prefix == "__main__":
            items = [(p, pages[p][0]) for p in MAIN if p in pages]
        elif prefix == "__playbooks__":
            items = [(p, pages[p][0]) for p in PLAYBOOKS if p in pages]
        elif prefix == "/blog/":
            entries = [(p, v) for p, v in pages.items()
                       if p.startswith("/blog/") and p != "/blog/"]
            entries.sort(key=lambda e: (e[1][1], e[0]), reverse=True)
            items = [(p, v[0]) for p, v in entries]
        else:
            entries = sorted((p, v[0]) for p, v in pages.items()
                             if p.startswith(prefix) and p != prefix)
            items = entries
        # the two curated sections deliberately repeat pages listed elsewhere
        if prefix not in ("__main__", "__playbooks__"):
            items = [(p, h) for p, h in items if p not in used]
        if not items:
            continue
        for p, _ in items:
            used.add(p)
        b = [f'      <h2 class="section-heading">{heading} '
             f'<span class="count">{len(items)}</span></h2>']
        if blurb:
            b.append(f"      <p class=\"text-muted\">{blurb}</p>")
        b.append('      <ul class="sitemap-list">')
        b.extend(li(p, h) for p, h in items)
        b.append("      </ul>")
        blocks.append("\n".join(b))

    leftovers = sorted(p for p in pages if p not in used)
    if leftovers:
        b = [f'      <h2 class="section-heading">Other pages '
             f'<span class="count">{len(leftovers)}</span></h2>',
             '      <ul class="sitemap-list">']
        b.extend(li(p, pages[p][0]) for p in leftovers)
        b.append("      </ul>")
        blocks.append("\n".join(b))

    trail = [("Home", "/"), ("Site Index", "/sitemap/")]
    schema = tpl.graph(tpl.breadcrumb_schema(trail), tpl.ORG_SCHEMA)

    body = f"""
  <section class="hero hero-page">
    <div class="wrap">
      {tpl.breadcrumb_html(trail)}
      <div class="hero-inner">
        <span class="eyebrow">Sitemap</span>
        <h1>Site Index</h1>
        <p class="hero-sub">Every page on this site, organised by section. {total} pages in total. If you would rather browse by topic, the blog index groups the same articles by category.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="sitemap-index">
{chr(10).join(blocks)}
      </div>
    </div>
  </section>
{tpl.cta_band(
    "Found what you were looking for?",
    "A thirty minute call covers your income, your tax position, and which markets actually fit what you are trying to do.")}"""

    write("/sitemap/", tpl.page(
        title=f"Site Index: All {total} Pages | BNB Accelerator",
        description=f"Every page on mybnbaccelerator.com, organised by section: {total} pages covering markets, case studies, tax strategy, financing, regulations and the blog.",
        path="/sitemap/",
        body=body,
        extra_schema=schema,
        transparent=True,
    ))
    print(f"site index: {total} pages listed")


if __name__ == "__main__":
    main()
