#!/usr/bin/env python3
"""Assign backdates to the new posts, render them, and rebuild the blog index.

Dates are spaced across the twelve months to August 2026, concentrated in the
window the existing 140 posts did not cover (August 2025 through April 2026),
at three posts per week on a rotating day pattern so the cadence reads
naturally rather than mechanically.
"""
import datetime
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import blog
import posts_markets
import posts_markets_extra
import posts_ops
import posts_ops_extra
import posts_tax
import posts_design
import posts_reg
import posts_strategy

# Week 0 begins Monday 18 August 2025. Three posts a week, alternating between
# Mon/Wed/Fri and Tue/Thu/Sat so consecutive weeks do not look templated.
START = datetime.date(2025, 8, 18)
DAY_PATTERNS = [(0, 2, 4), (1, 3, 5), (0, 2, 4), (1, 3, 5), (0, 3, 5), (1, 2, 4)]


def date_slots(n):
    """Yield n dates, three per week, cycling the day-of-week pattern."""
    out = []
    week = 0
    while len(out) < n:
        for d in DAY_PATTERNS[week % len(DAY_PATTERNS)]:
            if len(out) >= n:
                break
            out.append(START + datetime.timedelta(weeks=week, days=d))
        week += 1
    return out


def collect():
    """Merge each module's posts with its EXTRA closing sections, if any."""
    modules = [
        (posts_markets, posts_markets_extra.EXTRA),
        (posts_tax, None),
        (posts_ops, posts_ops_extra.EXTRA),
        (posts_design, None),
        (posts_reg, getattr(posts_reg, "EXTRA", None)),
        (posts_strategy, getattr(posts_strategy, "EXTRA", None)),
    ]
    posts = []
    for mod, extra in modules:
        for p in mod.POSTS:
            if extra and p["slug"] in extra:
                p["sections"] = list(p["sections"]) + [extra[p["slug"]]]
            posts.append(p)
    return posts


def interleave(posts):
    """Round-robin the categories so consecutive dates are not all one topic."""
    buckets = {}
    for p in posts:
        buckets.setdefault(p["category"], []).append(p)
    order = sorted(buckets, key=lambda k: -len(buckets[k]))
    out = []
    while any(buckets[k] for k in order):
        for k in order:
            if buckets[k]:
                out.append(buckets[k].pop(0))
    return out


def main():
    posts = collect()
    slugs = [p["slug"] for p in posts]
    if len(set(slugs)) != len(slugs):
        dupes = {s for s in slugs if slugs.count(s) > 1}
        sys.exit(f"duplicate slugs: {dupes}")

    existing = {d for d in os.listdir(os.path.join(blog.ROOT, "blog"))
                if os.path.isdir(os.path.join(blog.ROOT, "blog", d))}
    clash = set(slugs) & existing
    if clash:
        sys.exit(f"slugs already on disk: {clash}")

    posts = interleave(posts)
    dates = date_slots(len(posts))
    for p, d in zip(posts, dates):
        p["date"] = d.isoformat()

    print(f"dating {len(posts)} posts from {dates[0]} to {dates[-1]}")
    blog.build(posts)


if __name__ == "__main__":
    main()
