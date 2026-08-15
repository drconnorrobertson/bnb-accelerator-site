#!/usr/bin/env python3
"""Cluster pillar pages at /topics/<cluster>/, plus the /topics/ hub.

Each pillar links to every post in its cluster, grouped by year, which is what
makes it a pillar rather than a category listing. Posts link back to their
pillar through the related block, so the cluster is closed in both directions.
"""
import datetime
import os
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import era
import tpl
from pillars import hub, sections_html, write


def pillar(cluster_key, posts):
    c = era.CLUSTERS[cluster_key]
    path = f"/topics/{cluster_key}/"
    trail = [("Home", "/"), ("Topics", "/topics/"), (c["name"], path)]

    by_year = defaultdict(list)
    for p in posts:
        by_year[p["date"][:4]].append(p)

    blocks = []
    for yr in sorted(by_year, reverse=True):
        items = sorted(by_year[yr], key=lambda p: p["date"], reverse=True)
        lis = "\n".join(
            f'          <li><a href="/blog/{p["slug"]}/">{tpl.esc(p["title"])}</a>'
            f' <span class="text-muted">{datetime.date.fromisoformat(p["date"]).strftime("%b %-d")}</span></li>'
            for p in items)
        blocks.append(f"""      <h2 class="section-heading">{yr} <span class="count">{len(items)}</span></h2>
      <ul class="sitemap-list">
{lis}
      </ul>""")

    items_schema = ",\n".join(
        f'        {{ "@type": "ListItem", "position": {i}, '
        f'"url": "{tpl.SITE}/blog/{p["slug"]}/", "name": "{tpl.esc(p["title"])}" }}'
        for i, p in enumerate(sorted(posts, key=lambda x: x["date"], reverse=True), 1))

    others = "\n".join(
        f'            <li><a href="/topics/{k}/">{v["name"]}</a> &mdash; {v["blurb"]}</li>'
        for k, v in era.CLUSTERS.items() if k != cluster_key)

    schema = tpl.graph(
        tpl.breadcrumb_schema(trail),
        f"""    {{
      "@type": "CollectionPage",
      "name": "{tpl.esc(c['name'])} articles",
      "description": "{tpl.esc(c['intro'])}",
      "url": "{tpl.SITE}{path}",
      "isPartOf": {{ "@id": "https://mybnbaccelerator.com/#website" }}
    }}""",
        tpl.ORG_SCHEMA,
    ) + "\n" + tpl.graph(
        '    {\n      "@type": "ItemList",\n      "itemListElement": [\n'
        + items_schema + "\n      ]\n    }")

    body = f"""
  <section class="hero hero-page">
    <div class="wrap">
      {tpl.breadcrumb_html(trail)}
      <div class="hero-inner">
        <span class="eyebrow">Topic cluster</span>
        <h1>{c["name"]}</h1>
        <p class="hero-sub">{c["intro"]} {len(posts)} articles, from 2021 to today.</p>
        <div class="btn-row">
          <a class="btn btn-accent btn-lg" href="/apply/">Apply Now</a>
          <a class="btn btn-ghost-light btn-lg" href="/topics/">All topics</a>
        </div>
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

  <section class="bg-alt">
    <div class="wrap wrap-narrow">
      <article class="article">
        <h2>The other clusters</h2>
        <div class="callout">
          <ul>
{others}
          </ul>
        </div>
      </article>
    </div>
  </section>
{tpl.cta_band(
        "Reading is the cheap part",
        "A thirty minute call covers your income, your tax position, and whether any of this applies to your situation.")}"""

    write(path, tpl.page(
        title=f"{c['name']}: {len(posts)} Articles (2021-2026)",
        description=f"{c['intro']} {len(posts)} articles covering 2021 to 2026.",
        path=path,
        body=body,
        extra_schema=schema,
        active="/blog/",
        transparent=True,
    ))


def topics_hub(counts):
    total = sum(counts.values())
    cards = [(f"/topics/{k}/", v["name"],
              f'{v["blurb"]} <strong>{counts.get(k, 0)} articles.</strong>')
             for k, v in era.CLUSTERS.items()]
    write("/topics/", hub(
        path="/topics/",
        title="Topic Clusters: STR Investing Articles by Subject",
        h1="Every article, organised by subject",
        eyebrow="Topics",
        description=f"{total} short-term rental investing articles across ten topic clusters, from market analysis and tax strategy to design, pricing and regulation.",
        sub=f"{total} articles across ten clusters, written between 2021 and today. Each cluster page lists every article in it, grouped by year.",
        cards=cards,
        sections=[
            ("How this is organised", [
                "Each cluster has a pillar page listing every article in it by year, and each "
                "article links back to its pillar and across to its closest neighbours. That "
                "structure exists because short-term rental questions are rarely standalone: a "
                "pricing question is usually also an occupancy question, and a tax question is "
                "almost always also a management question.",
                "The archive runs from 2021, when BNB Accelerator started, through today. The "
                "older posts are kept as written rather than quietly updated, because what people "
                "believed in 2021 and 2023 is part of the record and the mistakes are instructive.",
                ("ul", [
                    "<strong>Year matters for tax posts.</strong> Bonus depreciation was 100% "
                    "through 2022, 80% in 2023, 60% in 2024, and split in 2025 before OBBBA "
                    "restored it to 100% permanently for qualifying acquisitions.",
                    "<strong>Year matters for market posts.</strong> A market that looked "
                    "unstoppable in 2021 frequently looked very different by 2023.",
                    "<strong>Year matters less for mechanics.</strong> The seven-day test, the "
                    "participation tests and the underwriting discipline have not changed.",
                ]),
            ]),
        ],
        faqs=[
            ("What is a topic cluster?",
             "A pillar page covering a subject, plus every article on that subject linking to it and to each other. It helps readers find the next useful thing and it helps search engines understand which pages belong together."),
            ("Why are old posts kept as written?",
             "Because the record is instructive. A 2021 post arguing from a market where everything filled, read next to a 2023 post arguing from the correction, teaches more than either would alone."),
            ("Which cluster should I start with?",
             "If you are deciding whether to buy at all, start with Tax Strategy and Acquisition & Financing. If you already own, start with Revenue Optimization and Property Management."),
        ],
        related=[
            '<a href="/blog/">The full blog archive by date</a>',
            '<a href="/sitemap/">Every page on the site</a>',
            '<a href="/case-studies/">Client case studies</a>',
            '<a href="/wins/">Client wins</a>',
        ],
        list_name="BNB Accelerator Topic Clusters",
    ))


def main(posts_by_cluster):
    counts = {}
    for k in era.CLUSTERS:
        ps = posts_by_cluster.get(k, [])
        counts[k] = len(ps)
        if ps:
            pillar(k, ps)
    topics_hub(counts)
    print("topics: " + ", ".join(f"{k}={v}" for k, v in counts.items()))
