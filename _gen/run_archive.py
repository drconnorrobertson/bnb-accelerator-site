#!/usr/bin/env python3
"""Rebuild the whole blog archive across 2021 to August 2026.

Posts publish on Mondays and Thursdays. Era-written posts are pinned to their
own year; everything else is evergreen and fills the remaining slots in a
stable order. Clusters are assigned, pillar pages are built, and each post
gains a link to its cluster pillar.
"""
import datetime
import glob
import os
import re
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import blog
import era
import gen_market_updates
import gen_market_year
import gen_topic_year
import gen_topics
import posts_design
import posts_markets
import posts_markets_extra
import posts_ops
import posts_ops_extra
import posts_reg
import posts_strategy
import posts_tax
from pillars import write

ROOT = blog.ROOT
START = datetime.date(2021, 1, 4)       # first Monday of 2021
END = datetime.date(2026, 8, 13)        # last Thursday before the site's "today"


def slots():
    """Every Monday and Thursday in the window, oldest first."""
    out, d = [], START
    while d <= END:
        if d.weekday() in (0, 3):
            out.append(d)
        d += datetime.timedelta(days=1)
    return out


def collect_new():
    """The posts written for this archive, each already carrying a cluster."""
    posts = []
    modules = [
        (posts_markets, posts_markets_extra.EXTRA),
        (posts_tax, None),
        (posts_ops, posts_ops_extra.EXTRA),
        (posts_design, None),
        (posts_reg, getattr(posts_reg, "EXTRA", None)),
        (posts_strategy, getattr(posts_strategy, "EXTRA", None)),
    ]
    for mod, extra in modules:
        for p in mod.POSTS:
            p = dict(p)
            if extra and p["slug"] in extra and extra[p["slug"]] not in p["sections"]:
                p["sections"] = list(p["sections"]) + [extra[p["slug"]]]
            p.setdefault("cluster", era.cluster_for(p["category"]))
            posts.append(p)
    for p in (gen_market_year.all_posts() + gen_topic_year.all_posts()
              + gen_market_updates.all_posts()):
        posts.append(p)
    return posts


def existing_on_disk(new_slugs):
    """Hand-written posts already published, which keep their content."""
    out = []
    for d in sorted(glob.glob(os.path.join(ROOT, "blog", "*", "index.html"))):
        slug = os.path.basename(os.path.dirname(d))
        if slug in new_slugs:
            continue
        s = open(d, encoding="utf-8").read()
        m = re.search(r'<span class="eyebrow">(.*?)</span>', s, re.S)
        cat = re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else "Strategy"
        m = re.search(r"<h1>(.*?)</h1>", s, re.S)
        title = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", m.group(1))).strip() if m else slug
        m = re.search(r"<title>(.*?)</title>", s, re.S)
        ttag = m.group(1).strip() if m else title
        m = re.search(r'<meta name="description" content="(.*?)">', s, re.S)
        desc = m.group(1) if m else ""
        # Only a year in the H1 pins a post: that is genuine era content. A year
        # that appears solely in the <title> tag is the "(2026)" SEO suffix these
        # were written with, and it is reconciled to the assigned date instead.
        ym = re.search(r"\b(202[1-6])\b", title)
        out.append(dict(slug=slug, path=d, category=cat, title=title,
                        title_tag=ttag, cluster=era.cluster_for(cat),
                        pin_year=int(ym.group(1)) if ym else None,
                        existing=True))
    return out


def assign_dates(items, all_slots):
    """Pinned posts take a slot inside their year; the rest fill what is left."""
    by_year = defaultdict(list)
    for s in all_slots:
        by_year[s.year].append(s)
    used = set()
    pinned = [i for i in items if i.get("pin_year") or i.get("year")]
    free = [i for i in items if i not in pinned]

    # spread pinned posts evenly through their own year
    for yr, group in sorted(defaultdict(list, {
            y: [i for i in pinned if (i.get("year") or i.get("pin_year")) == y]
            for y in set((i.get("year") or i.get("pin_year")) for i in pinned)}).items()):
        avail = [s for s in by_year.get(yr, []) if s not in used]
        if not avail:
            continue
        step = max(1, len(avail) // max(1, len(group)))
        for n, item in enumerate(group):
            idx = min(n * step, len(avail) - 1)
            while avail[idx] in used and idx < len(avail) - 1:
                idx += 1
            item["date"] = avail[idx].isoformat()
            used.add(avail[idx])

    # Spread the evergreen posts evenly across every slot the pinned posts left,
    # rather than filling front to back, which would pile them all into 2021.
    remaining = [s for s in all_slots if s not in used]
    if free:
        stride = len(remaining) / len(free)
        for n, item in enumerate(free):
            idx = min(int(n * stride), len(remaining) - 1)
            item["date"] = remaining[idx].isoformat()
    return items


def interleave(posts):
    buckets = defaultdict(list)
    for p in posts:
        buckets[p["cluster"]].append(p)
    order = sorted(buckets, key=lambda k: -len(buckets[k]))
    out = []
    while any(buckets[k] for k in order):
        for k in order:
            if buckets[k]:
                out.append(buckets[k].pop(0))
    return out


def add_pillar_link(p):
    c = era.CLUSTERS[p["cluster"]]
    link = f'<a href="/topics/{p["cluster"]}/">More {c["name"].lower()} articles</a>'
    if not any("/topics/" in r for r in p["related"]):
        p["related"] = list(p["related"]) + [link]
    return p


def main():
    new = collect_new()
    new_slugs = {p["slug"] for p in new}
    if len(new_slugs) != len(new):
        seen, dupes = set(), set()
        for p in new:
            if p["slug"] in seen:
                dupes.add(p["slug"])
            seen.add(p["slug"])
        sys.exit(f"duplicate slugs: {dupes}")

    old = existing_on_disk(new_slugs)
    all_slots = slots()
    print(f"{len(all_slots)} Mon/Thu slots from {all_slots[0]} to {all_slots[-1]}")
    print(f"{len(new)} new posts + {len(old)} existing = {len(new) + len(old)}")

    items = interleave(new) + old
    assign_dates(items, all_slots)

    # write the new posts
    for p in new:
        add_pillar_link(p)
        write(f"/blog/{p['slug']}/", blog.render_post(p))

    # restamp dates and add the pillar link on the existing posts
    for o in old:
        s = open(o["path"], encoding="utf-8").read()
        d = datetime.date.fromisoformat(o["date"])
        s = re.sub(r'"datePublished":\s*"[0-9-]+"',
                   f'"datePublished": "{o["date"]}"', s)
        s = re.sub(r'"dateModified":\s*"[0-9-]+"',
                   f'"dateModified": "{o["date"]}"', s)
        s = re.sub(r"<span>Published [^<]*</span>",
                   f"<span>Published {d.strftime('%B %-d, %Y')}</span>", s)

        # Reconcile the "(2026)" style suffix in the <title> tag with the date
        # the post now carries. Dropping it is always safe; rewriting it to a
        # different year would not be, because some bodies discuss law that only
        # existed later.
        if not o["pin_year"] and d.year != 2026:
            def strip_year(m):
                t = m.group(1)
                t = re.sub(r"\s*\(20\d\d(?:[^)]*)\)", "", t)
                t = re.sub(r"\s*\b20\d\d\b(?=\s*(?:\||$))", "", t)
                t = re.sub(r"\s{2,}", " ", t).strip(" |-")
                return f"<title>{t}</title>"
            s = re.sub(r"<title>(.*?)</title>", strip_year, s, count=1, flags=re.S)
        c = era.CLUSTERS[o["cluster"]]
        link = f'<li><a href="/topics/{o["cluster"]}/">More {c["name"].lower()} articles</a></li>'
        if "/topics/" not in s:
            s = re.sub(r'(<div class="callout">\s*<h3>Keep reading</h3>\s*<ul>)',
                       lambda m: m.group(1) + "\n            " + link, s, count=1)
        open(o["path"], "w", encoding="utf-8").write(s)

    # cluster pillars
    by_cluster = defaultdict(list)
    for p in new + old:
        by_cluster[p["cluster"]].append(
            dict(slug=p["slug"], title=p["title"], date=p["date"]))
    gen_topics.main(by_cluster)

    entries = blog.scan_existing()
    write("/blog/", blog.render_index(entries))
    print(f"blog index: {len(entries)} posts")
    months = defaultdict(int)
    for e in entries:
        months[e["date"][:4]] += 1
    print("by year: " + ", ".join(f"{k}={v}" for k, v in sorted(months.items())))


if __name__ == "__main__":
    main()
