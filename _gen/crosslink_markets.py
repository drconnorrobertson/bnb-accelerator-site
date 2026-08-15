#!/usr/bin/env python3
"""Add a related-links block to each market page.

Every market page gains body links into the state regulation page, the
matching property type guide and the case studies transacted in that market,
so the new sections are reachable from the market layer rather than only
from the footer.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

MARKER = '<div class="callout" data-market-related>'

# market slug -> (state slug, state name, property type slug, property type label,
#                 [(case study slug, label)], [(blog slug, label)])
MAP = {
    "austin": ("texas", "Texas", "lake", "Lake house",
               [("laxman-sabitri-johnson-city-tx-6br", "Laxman and Sabitri, 6BR Johnson City at $680,000")],
               [("johnson-city-texas-hill-country", "Johnson City and the Hill Country wine corridor")]),
    "big-bear": ("california", "California", "ski", "Ski property", [],
                 [("big-bear-california-str-market", "Big Bear: LA demand and capped permits")]),
    "branson": ("missouri", "Missouri", "lake", "Lake house",
                [("dustin-branson-west-mo-8br", "Dustin, 8BR Branson West at $930,900")],
                [("table-rock-lake-branson-west", "Table Rock Lake and its second season")]),
    "broken-bow": ("oklahoma", "Oklahoma", "mountain", "Mountain cabin",
                   [("joe-s-broken-bow-ok-and-destin-fl", "Joe S, 4BR Broken Bow at $1,400,000")],
                   [("hochatown-oklahoma-str-market", "Hochatown after incorporation")]),
    "cape-coral": ("florida", "Florida", "beach", "Beach property",
                   [("antonio-fort-myers-fl-6br", "Antonio, 6BR Fort Myers, $17,000 February")],
                   [("cape-coral-fort-myers-str-market", "Southwest Florida's inverted calendar")]),
    "denver": ("colorado", "Colorado", "city", "City rental", [],
               [("denver-metro-str-restrictions", "Why the Denver deals are not in Denver")]),
    "destin": ("florida", "Florida", "beach", "Beach property",
               [("mark-farrah-destin-fl-4br", "Mark and Farrah, 4BR Destin at $950,000"),
                ("tiffany-destin-fl-5br", "Tiffany, 5BR Destin at $1,100,000"),
                ("ashley-billy-fort-walton-beach-fl", "Ashley and Billy, 80 nights in 21 days")],
               [("fort-walton-beach-value-thesis", "Fort Walton Beach: the Emerald Coast at a discount"),
                ("santa-rosa-beach-30a-str-market", "Santa Rosa Beach and 30A")]),
    "gatlinburg": ("tennessee", "Tennessee", "mountain", "Mountain cabin",
                   [("victoria-sevierville-tn-9br-cabin", "Victoria, 9BR cabin, $20,000 in June")],
                   [("smoky-mountains-submarket-differences", "Sevierville, Pigeon Forge and Gatlinburg compared")]),
    "gulf-shores": ("alabama", "Alabama", "beach", "Beach property", [],
                    [("gulf-shores-orange-beach-str-market", "Alabama's family Gulf market")]),
    "joshua-tree": ("california", "California", "desert", "Desert property", [],
                    [("joshua-tree-str-market", "Joshua Tree: design-led demand, tightening rules")]),
    "kissimmee": ("florida", "Florida", "beach", "Beach property",
                  [("jason-marissa-champions-gate-fl-8br", "Jason and Marissa, 8BR at $650,000"),
                   ("naveen-davenport-fl-8br", "Naveen, 8BR Davenport at $700,000")],
                  [("kissimmee-champions-gate-str-market", "The per-bedroom math near Disney")]),
    "lake-tahoe": ("california", "California", "ski", "Ski property", [],
                   [("lake-tahoe-str-market", "One lake, four jurisdictions")]),
    "nashville": ("tennessee", "Tennessee", "city", "City rental",
                  [("mahmoud-nashville-tn-4br", "Mahmoud, 4BR permitted Nashville STR"),
                   ("krystin-michael-nashville-tn-4br", "Krystin and Michael, 4BR Nashville")],
                  [("nashville-permit-value", "What a Nashville permit is actually worth")]),
    "panama-city-beach": ("florida", "Florida", "beach", "Beach property",
                          [("shardul-mayanka-panama-city-beach-fl", "Shardul and Mayanka, 4BR at $530,000")],
                          [("fort-walton-beach-value-thesis", "Buying the Emerald Coast at a discount")]),
    "park-city": ("utah", "Utah", "ski", "Ski property", [],
                  [("park-city-utah-str-market", "Park City: two seasons and a zoning map")]),
    "phoenix-mesa": ("arizona", "Arizona", "desert", "Desert property", [],
                     [("phoenix-mesa-gilbert-chandler-comparison", "East Valley submarkets compared")]),
    "poconos": ("pennsylvania", "Pennsylvania", "lake", "Lake house",
                [("julie-pocono-lake-pa-5br", "Julie, 5BR Pocono Lake at $880,000")],
                [("pocono-townships-regulation-map", "Why two cabins on one road follow different rules")]),
    "scottsdale": ("arizona", "Arizona", "desert", "Desert property", [],
                   [("scottsdale-event-compression", "When four weeks carry the quarter")]),
    "sedona": ("arizona", "Arizona", "desert", "Desert property", [],
               [("sedona-arizona-str-market", "Constrained supply, high rates, real politics")]),
    "smoky-mountains": ("tennessee", "Tennessee", "mountain", "Mountain cabin",
                        [("victoria-sevierville-tn-9br-cabin", "Victoria, 9BR cabin, $20,000 in June"),
                         ("vishal-sevierville-tn-5br", "Vishal, 5BR at $1,250,000"),
                         ("alfredo-millie-sevierville-tn-4br", "Alfredo and Millie, 4BR at $865,000"),
                         ("adam-sevierville-tn-4br", "Adam, 4BR at $775,000")],
                        [("smoky-mountains-submarket-differences", "The three submarkets compared")]),
}


def block(slug):
    state_slug, state_name, pt_slug, pt_label, cases, posts = MAP[slug]
    items = [
        f'<li><a href="/regulations/{state_slug}/">{state_name} short-term rental regulations</a></li>',
        f'<li><a href="/property-types/{pt_slug}/">{pt_label} investing guide</a></li>',
    ]
    for cs, label in cases:
        items.append(f'<li><a href="/case-studies/{cs}/">Case study: {label}</a></li>')
    for bp, label in posts:
        items.append(f'<li><a href="/blog/{bp}/">{label}</a></li>')
    items.append('<li><a href="/revenue-projections/">How to build a revenue projection for this market</a></li>')
    items.append('<li><a href="/financing/">Financing a purchase in this market</a></li>')
    inner = "\n".join(f"            {i}" for i in items)
    return f"""        {MARKER}
          <h3>More on this market</h3>
          <ul>
{inner}
          </ul>
        </div>
"""


def main():
    n = 0
    for slug in sorted(MAP):
        f = os.path.join(ROOT, "markets", slug, "index.html")
        if not os.path.exists(f):
            print(f"  missing: {slug}")
            continue
        s = open(f, encoding="utf-8").read()
        if MARKER in s:
            s = re.sub(re.escape(MARKER) + r".*?</div>\n", "", s, flags=re.S)
        # insert immediately before the article closes
        i = s.rfind("        </article>")
        if i == -1:
            print(f"  no article close: {slug}")
            continue
        s = s[:i] + block(slug) + s[i:]
        open(f, "w", encoding="utf-8").write(s)
        n += 1
    print(f"market cross-links: {n} pages")


if __name__ == "__main__":
    main()
