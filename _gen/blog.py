#!/usr/bin/env python3
"""Blog post renderer and index rebuilder.

Posts are defined as data in posts_*.py. Each post renders to
/blog/<slug>/index.html with Article + FAQPage schema, and the blog index is
regenerated from the union of new posts and the posts already on disk.
"""
import datetime
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tpl
from pillars import sections_html, write

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


def fmt_date(iso):
    d = datetime.date.fromisoformat(iso)
    return d.strftime("%B %-d, %Y")


def short_date(iso):
    d = datetime.date.fromisoformat(iso)
    return d.strftime("%b %-d, %Y")


def word_count(post):
    n = 0
    for _, blocks in post["sections"]:
        for b in blocks:
            if isinstance(b, str):
                n += len(b.split())
            elif b[0] in ("ul", "ol"):
                n += sum(len(i.split()) for i in b[1])
            elif b[0] in ("callout", "warn", "h3"):
                n += len(b[1].split())
            elif b[0] == "table":
                n += sum(len(" ".join(r).split()) for r in b[2])
    n += len(post["lead"].split())
    n += sum(len(q.split()) + len(a.split()) for q, a in post["faqs"])
    return n


def read_minutes(post):
    return max(6, round(word_count(post) / 210))


def render_post(post):
    slug = post["slug"]
    path = f"/blog/{slug}/"
    url = tpl.SITE + path
    trail = [("Home", "/"), ("Blog", "/blog/"), (post["title"], path)]
    mins = read_minutes(post)

    rel = "\n".join(f"            <li>{r}</li>" for r in post["related"])

    schema = tpl.graph(
        tpl.breadcrumb_schema(trail),
        tpl.ORG_SCHEMA,
    ) + "\n" + tpl.article_schema(
        post["h1"], post["description"], url, post["date"], section=post["category"]
    ) + "\n" + tpl.faq_schema(post["faqs"])

    body = f"""
  <section class="hero hero-page">
    <div class="wrap">
      {tpl.breadcrumb_html(trail)}
      <div class="hero-inner">
        <span class="eyebrow">{post["category"]}</span>
        <h1>{post["h1"]}</h1>
        <div class="article-meta">
          <span>Published {fmt_date(post["date"])}</span><span>&middot;</span><span>{mins} min read</span>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <article class="article">

        <p class="lead">{post["lead"]}</p>

{sections_html(post["sections"])}

        <div class="callout">
          <h3>Keep reading</h3>
          <ul>
{rel}
          </ul>
        </div>

{tpl.faq_html(post["faqs"])}

{tpl.AUTHOR_BOX}

      </article>
    </div>
  </section>
{tpl.cta_band(
    post.get("cta_h", "See whether the numbers work for you"),
    post.get("cta_p", "Thirty minutes covers your income, your tax position, and which markets actually fit what you are trying to do."),
    ("/apply/", "Apply Now"),
    ("/case-studies/", "See client results"))}"""

    return tpl.page(
        title=post["title_tag"],
        description=post["description"],
        path=path,
        body=body,
        extra_schema=schema,
        body_class="blog",
        active="/blog/",
    )


def scan_existing():
    """Read title, date, category and excerpt out of every post already on disk."""
    out = []
    for d in sorted(glob.glob(os.path.join(ROOT, "blog", "*", "index.html"))):
        slug = os.path.basename(os.path.dirname(d))
        s = open(d, encoding="utf-8").read()
        m = re.search(r'"datePublished":\s*"([0-9-]+)"', s)
        date = m.group(1) if m else "2026-01-01"
        m = re.search(r"<h1>(.*?)</h1>", s, re.S)
        title = re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else slug
        m = re.search(r'<span class="eyebrow">(.*?)</span>', s, re.S)
        cat = re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else "Strategy"
        m = re.search(r'<meta name="description" content="(.*?)">', s, re.S)
        desc = m.group(1) if m else ""
        m = re.search(r"<span>(\d+) min read</span>", s)
        mins = m.group(1) if m else "9"
        out.append(dict(slug=slug, date=date, title=title, category=cat,
                        excerpt=desc, mins=mins))
    return out


def render_index(entries):
    """entries: dicts with slug, date, title, category, excerpt, mins."""
    entries = sorted(entries, key=lambda e: (e["date"], e["slug"]), reverse=True)
    trail = [("Home", "/"), ("Blog", "/blog/")]

    cards = []
    for i, e in enumerate(entries):
        delay = f' data-reveal-delay="{i % 3}"' if i % 3 else ""
        excerpt = e["excerpt"]
        if len(excerpt) > 160:
            excerpt = excerpt[:157].rsplit(" ", 1)[0] + "..."
        cards.append(f"""        <article class="post-card" data-reveal{delay}>
          <div class="post-body">
            <div class="post-meta"><span class="post-cat">{tpl.esc(e["category"])}</span><time datetime="{e["date"]}">{short_date(e["date"])}</time><span>{e["mins"]} min read</span></div>
            <h3><a href="/blog/{e["slug"]}/">{tpl.esc(e["title"])}</a></h3>
            <p>{tpl.esc(excerpt)}</p>
            <a class="post-link" href="/blog/{e["slug"]}/">Read more</a>
          </div>
        </article>""")

    # group by year-month for the archive nav
    months = {}
    for e in entries:
        months.setdefault(e["date"][:7], 0)
        months[e["date"][:7]] += 1
    month_list = "\n".join(
        f'          <li>{datetime.date.fromisoformat(m + "-01").strftime("%B %Y")} '
        f'<span class="text-muted">({n})</span></li>'
        for m, n in sorted(months.items(), reverse=True))

    cats = {}
    for e in entries:
        cats[e["category"]] = cats.get(e["category"], 0) + 1
    cat_list = "\n".join(
        f'          <li>{tpl.esc(c)} <span class="text-muted">({n})</span></li>'
        for c, n in sorted(cats.items(), key=lambda x: -x[1]))

    items = ",\n".join(
        f'        {{ "@type": "ListItem", "position": {i}, "url": "{tpl.SITE}/blog/{e["slug"]}/", "name": "{tpl.esc(e["title"])}" }}'
        for i, e in enumerate(entries[:100], 1))

    schema = tpl.graph(
        tpl.breadcrumb_schema(trail),
        f"""    {{
      "@type": "Blog",
      "@id": "https://mybnbaccelerator.com/blog/#blog",
      "name": "The BNB Accelerator Blog",
      "description": "Short-term rental investing, tax strategy, market analysis and operations, written for high-income earners buying cash-flowing Airbnb properties.",
      "url": "https://mybnbaccelerator.com/blog/",
      "isPartOf": {{ "@id": "https://mybnbaccelerator.com/#website" }},
      "publisher": {{ "@id": "https://mybnbaccelerator.com/#organization" }}
    }}""",
        tpl.ORG_SCHEMA,
    ) + "\n" + tpl.graph(
        '    {\n      "@type": "ItemList",\n      "itemListElement": [\n' + items + "\n      ]\n    }")

    body = f"""
  <section class="hero hero-page">
    <div class="wrap">
      {tpl.breadcrumb_html(trail)}
      <div class="hero-inner">
        <span class="eyebrow">Blog</span>
        <h1>Short-term rental investing, written for people with a day job</h1>
        <p class="hero-sub">{len(entries)} articles on markets, tax strategy, financing, design and operations. No hype, no guru language, and no promises about what your property will do.</p>
        <div class="btn-row">
          <a class="btn btn-accent btn-lg" href="/apply/">Apply Now</a>
          <a class="btn btn-ghost-light btn-lg" href="/case-studies/">See client results</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section-sm">
    <div class="wrap">
      <div class="grid grid-3">
        <div class="card-static">
          <h2>By topic</h2>
          <ul class="sitemap-list">
{cat_list}
          </ul>
        </div>
        <div class="card-static">
          <h2>Start here</h2>
          <ul class="sitemap-list">
            <li><a href="/blog/short-term-rental-investing-2026/">STR investing in 2026</a></li>
            <li><a href="/blog/how-to-start-airbnb-business/">How to start an Airbnb business</a></li>
            <li><a href="/tax-strategy/7-day-rule/">The seven day rule</a></li>
            <li><a href="/revenue-projections/">Building a revenue projection</a></li>
            <li><a href="/financing/">Financing a short-term rental</a></li>
            <li><a href="/regulations/">Rules by state</a></li>
          </ul>
        </div>
        <div class="card-static">
          <h2>Archive</h2>
          <ul class="sitemap-list">
{month_list}
          </ul>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="post-grid">
{chr(10).join(cards)}
      </div>
    </div>
  </section>
{tpl.cta_band(
    "Reading is the cheap part",
    "A thirty minute call covers your income, your tax position, and whether any of this actually applies to your situation.")}"""

    return tpl.page(
        title=f"STR Investing Blog: {len(entries)} Articles on Airbnb Investing (2026)",
        description=f"{len(entries)} articles on short-term rental investing: market analysis, STR tax strategy, financing, design, pricing and operations for high-income earners.",
        path="/blog/",
        body=body,
        extra_schema=schema,
        active="/blog/",
        transparent=True,
    )


def build(posts):
    seen = set()
    for p in posts:
        if p["slug"] in seen:
            raise SystemExit(f"duplicate slug: {p['slug']}")
        seen.add(p["slug"])
        wc = word_count(p)
        if wc < 780:
            print(f"  short ({wc}w): {p['slug']}")
        write(f"/blog/{p['slug']}/", render_post(p))
    print(f"blog: wrote {len(posts)} posts")

    entries = scan_existing()
    write("/blog/", render_index(entries))
    print(f"blog index: {len(entries)} posts listed")
    return entries
