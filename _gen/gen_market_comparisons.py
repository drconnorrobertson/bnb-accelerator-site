#!/usr/bin/env python3
"""Build 100 evidence-led STR market comparisons from the existing market dataset.

The explicit comparison set is deterministic. Each page compares two distinct
market records, gives the reader a purchase decision to make, and links back to
the underlying market guides. Ranges are editorial estimates, not forecasts.
"""
import itertools
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tpl
from pillars import write

HERE = os.path.dirname(os.path.abspath(__file__))
MARKETS = json.load(open(os.path.join(HERE, "market_data.json"), encoding="utf-8"))
PUBLISHED = "2026-09-25"

# These themes establish a useful reason to compare beyond alphabetic pairing.
THEMES = {
    "austin": ("event and city travel", "Check which events and trip purposes a specific address can actually serve; citywide event demand is not a property-level forecast."),
    "big-bear": ("mountain and lake trips", "Model the winter and summer peaks separately, then test access and carrying cost in the two softer shoulders."),
    "branson": ("family entertainment and lake trips", "Verify drive time to the attraction cluster and model the Christmas season separately from the long warm-weather run."),
    "broken-bow": ("cabin and lake trips", "Compare cabin amenities and lake access against genuinely similar listings; weekends carry a different thesis from weekdays."),
    "cape-coral": ("winter sun and waterfront trips", "Quote flood and wind coverage for the specific address and separate waterfront premiums from ordinary pool-home revenue."),
    "denver": ("urban and mountain access", "Identify the exact guest trip driver and verify local rental eligibility before using a metro-wide comparable set."),
    "destin": ("Gulf beach vacations", "Underwrite beach access, parking, storm exposure and the spring-to-summer revenue concentration at the address level."),
    "gatlinburg": ("Smokies cabin trips", "Check views, road grade, parking and cabin supply; do not use peak leaf-season weeks as the annual norm."),
    "gulf-shores": ("Gulf beach vacations", "Price storm insurance and building or HOA rules before comparing a lower purchase price with Florida beach markets."),
    "joshua-tree": ("desert and design-led stays", "Stress-test summer occupancy and the cost of keeping a distinctive desert property guest-ready."),
    "kissimmee": ("theme-park group travel", "Check resort or HOA rental permission, fees and pool costs for the actual community rather than the city average."),
    "lake-tahoe": ("ski and lake trips", "Verify the parcel's permit position and model both winter and summer peaks with the spring and fall troughs intact."),
    "nashville": ("event and city travel", "Confirm the permit category and location-specific eligibility; headline event weekends cannot stand in for a full year."),
    "panama-city-beach": ("Gulf beach vacations", "Separate spring-break and summer booking assumptions, then quote insurance and building fees for the property."),
    "park-city": ("ski and resort trips", "Verify nightly-rental zoning and building rules first; a ski-season revenue case cannot rescue an ineligible address."),
    "phoenix-mesa": ("winter sun and event travel", "Model March spring-training demand separately from summer and price pool, cooling and water costs."),
    "poconos": ("drive-to lake and ski trips", "Verify township and community rules together, plus septic, occupancy and winter access."),
    "scottsdale": ("winter sun and golf trips", "Compare pool homes with similar bedroom count and location, then stress-test summer revenue and cooling costs."),
    "sedona": ("desert and outdoor trips", "Check the exact rental permission and distinguish spring and fall demand from hot-weather assumptions."),
    "smoky-mountains": ("Smokies cabin trips", "Verify road access, parking, fire and weather exposure, and whether comparable cabins truly match the amenity set."),
}


def bounds(value):
    return [int(x.replace(",", "")) for x in re.findall(r"\$([\d,]+)", value)]


def midpoint(value):
    lo, hi = bounds(value)
    return (lo + hi) / 2


def pairs():
    """Select 100 comparisons with price proximity and trip-type relevance."""
    ranked = []
    for a, b in itertools.combinations(sorted(MARKETS), 2):
        ma, mb = MARKETS[a], MARKETS[b]
        type_match = THEMES[a][0] == THEMES[b][0]
        price_gap = abs(midpoint(ma["entry"]) - midpoint(mb["entry"]))
        net_gap = abs(midpoint(ma["net"]) - midpoint(mb["net"]))
        # Shared guest thesis matters most; similar acquisition budgets next.
        score = (0 if type_match else 1, price_gap, net_gap, a, b)
        ranked.append((score, a, b))
    chosen = [(a, b) for _, a, b in sorted(ranked)[:100]]
    assert len(chosen) == 100 and len(set(chosen)) == 100
    return sorted(chosen)


def key_decision(a, b):
    ma, mb = MARKETS[a], MARKETS[b]
    a_low, a_high = bounds(ma["entry"])
    b_low, b_high = bounds(mb["entry"])
    if a_low < b_low:
        entry = f"{ma['name']} has the lower starting purchase range ({ma['entry']} versus {mb['entry']})."
    elif b_low < a_low:
        entry = f"{mb['name']} has the lower starting purchase range ({mb['entry']} versus {ma['entry']})."
    else:
        entry = f"Both published purchase ranges start at ${a_low:,}; the property-level costs will decide the entry gap."
    if max(a_low, b_low) <= min(a_high, b_high):
        entry += " The ranges overlap, so price alone will not settle the choice."
    else:
        entry += " The published purchase ranges do not overlap."
    a_net, b_net = midpoint(ma["net"]), midpoint(mb["net"])
    if a_net == b_net:
        cash = "The midpoints of the estimated annual net ranges are equal; compare the spread and downside instead."
    else:
        higher, lower = (ma, mb) if a_net > b_net else (mb, ma)
        cash = (f"{higher['name']} has the higher midpoint of the estimated annual net range "
                f"(${int(max(a_net,b_net)):,} versus ${int(min(a_net,b_net)):,}). "
                "That is a screening observation, not a property return or a forecast.")
    return entry, cash


def comparison_page(a, b, related):
    ma, mb = MARKETS[a], MARKETS[b]
    na, nb = ma["name"], mb["name"]
    slug = f"{a}-vs-{b}"
    path = f"/compare/markets/{slug}/"
    title = f"{na} vs {nb}: Short-Term Rental Market Comparison"
    description = (f"Compare {na} and {nb} for an STR purchase: entry price, nightly rate, "
                   "occupancy, estimated cash flow, seasons and address-level checks.")
    entry, cash = key_decision(a, b)
    trail = [("Home", "/"), ("Compare", "/compare/"), ("Markets", "/compare/markets/"), (f"{na} vs {nb}", path)]
    rows = [
        ("Purchase price", "entry"), ("Average daily rate", "adr"),
        ("Occupancy", "occ"), ("Annual gross revenue", "gross"),
        ("Annual net cash flow", "net"), ("Demand pattern", "peak"),
    ]
    table_rows = "\n".join(
        f'<tr><th scope="row">{label}</th><td>{tpl.esc(ma[field])}</td><td>{tpl.esc(mb[field])}</td></tr>'
        for label, field in rows
    )
    related_html = "\n".join(
        f'<li><a href="/compare/markets/{x}-vs-{y}/">{tpl.esc(MARKETS[x]["name"])} vs {tpl.esc(MARKETS[y]["name"])}</a></li>'
        for x, y in related[:4]
    )
    body = f"""
  <section class="hero hero-page"><div class="wrap">
    {tpl.breadcrumb_html(trail)}
    <div class="hero-inner"><span class="eyebrow">STR market comparison</span><h1>{tpl.esc(na)} vs {tpl.esc(nb)}</h1>
      <p class="lead">Two markets, one purchase decision. Compare the ranges, the booking calendar and what must be checked for an actual address.</p>
    </div>
  </div></section>
  <section class="section-sm"><div class="wrap wrap-narrow">
    <div class="verdict"><span class="verdict-label">Decision in brief</span><p>{tpl.esc(entry)} {tpl.esc(cash)}</p></div>
    <p class="small text-muted mt-3">Published market ranges are screening estimates assembled from closings and active comparables. They are not returns promised for a specific property. Read <a href="/data/average-str-revenue-by-market/#method">how the estimates were assembled</a> and the underlying <a href="/markets/{a}/">{tpl.esc(na)} market guide</a> and <a href="/markets/{b}/">{tpl.esc(nb)} market guide</a>; refresh comparables, costs and permit status before an offer.</p>
  </div></section>
  <section class="bg-alt"><div class="wrap wrap-narrow">
    <div class="section-head"><span class="eyebrow">At a glance</span><h2>Side-by-side market ranges</h2></div>
    <div class="table-scroll"><table class="compare"><caption class="sr-only">Short-term rental estimates for {tpl.esc(na)} and {tpl.esc(nb)}</caption>
      <thead><tr><th scope="col">Metric</th><th scope="col">{tpl.esc(na)}</th><th scope="col">{tpl.esc(nb)}</th></tr></thead><tbody>{table_rows}</tbody></table></div>
  </div></section>
  <section><div class="wrap wrap-narrow">
    <div class="section-head"><span class="eyebrow">The real tradeoff</span><h2>What changes the decision</h2></div>
    <h3>Acquisition budget and cash flow</h3><p>{tpl.esc(entry)} {tpl.esc(cash)} Compare actual down payment, closing costs, furnishing, reserves, insurance and debt service before treating either range as an investment result.</p>
    <h3>Guest demand and calendar</h3><p>{tpl.esc(na)} is driven by {tpl.esc(THEMES[a][0])}: {tpl.esc(ma['peak'])}. {tpl.esc(nb)} is driven by {tpl.esc(THEMES[b][0])}: {tpl.esc(mb['peak'])}. Build a monthly model for each; equal annual gross estimates can conceal different low-season cash needs.</p>
    <h3>Property-level checks</h3><ul><li><strong>{tpl.esc(na)}:</strong> {tpl.esc(THEMES[a][1])}</li><li><strong>{tpl.esc(nb)}:</strong> {tpl.esc(THEMES[b][1])}</li></ul>
    <p>For either market, confirm permit eligibility, HOA or building rules, comparable listing quality and a written cost estimate for the property under consideration. Market averages cannot substitute for those checks.</p>
  </div></section>
  <section class="section-sm bg-alt"><div class="wrap wrap-narrow"><h2>Continue comparing</h2><ul>{related_html}</ul><p><a href="/compare/markets/">Browse all market comparisons</a> · <a href="/tools/str-revenue-calculator/">Model a specific property</a></p></div></section>
{tpl.cta_band("Need help choosing a market?", "Bring a real budget and purchase brief. We can discuss which markets fit and which assumptions need checking.", primary=("/apply/", "Discuss your search"), secondary=("/markets/", "Explore markets"))}
"""
    schema = tpl.graph(tpl.breadcrumb_schema(trail), tpl.ORG_SCHEMA) + "\n" + tpl.article_schema(title, description, tpl.SITE + path, PUBLISHED, section="Market comparison")
    write(path, tpl.page(title=title, description=description, path=path, body=body, extra_schema=schema, active="/blog/", transparent=True))


def hub(chosen):
    path = "/compare/markets/"
    title = "Compare 100 Short-Term Rental Market Pairs"
    description = "Compare STR markets side by side using purchase, revenue, occupancy, cash-flow and seasonality estimates, then check the property-level risks."
    groups = {}
    for a, b in chosen:
        groups.setdefault(a, []).append(b)
    sections = []
    for a, bs in groups.items():
        links = "\n".join(f'<li><a href="/compare/markets/{a}-vs-{b}/">{tpl.esc(MARKETS[a]["name"])} vs {tpl.esc(MARKETS[b]["name"])}</a></li>' for b in bs)
        sections.append(f'<section class="section-sm"><div class="wrap wrap-narrow"><h2>{tpl.esc(MARKETS[a]["name"])} comparisons</h2><ul class="cmp-guides">{links}</ul></div></section>')
    trail = [("Home", "/"), ("Compare", "/compare/"), ("Market comparisons", path)]
    body = f'<section class="hero hero-page"><div class="wrap">{tpl.breadcrumb_html(trail)}<div class="hero-inner"><span class="eyebrow">Market comparisons</span><h1>Compare 100 STR market pairs</h1><p class="lead">Start with two markets that fit your budget. Each comparison puts published ranges and distinct property checks on the same page.</p></div></div></section><section class="section-sm bg-alt"><div class="wrap wrap-narrow"><p>These estimates help narrow a search. Verify current listing comparables, local rules and all costs for a specific property before committing capital. <a href="/markets/">Explore individual market guides</a>.</p></div></section>{"".join(sections)}'
    schema = tpl.graph(tpl.breadcrumb_schema(trail), tpl.ORG_SCHEMA)
    write(path, tpl.page(title=title, description=description, path=path, body=body, extra_schema=schema, active="/blog/", transparent=True))


def link_existing_compare_hub():
    path = os.path.join(HERE, "..", "compare", "index.html")
    html = open(path, encoding="utf-8").read()
    marker = '<li><a href="/compare/markets/">Compare 100 STR market pairs</a></li>'
    if marker not in html:
        html = html.replace('<ul class="cmp-guides" data-reveal>', '<ul class="cmp-guides" data-reveal>\n        ' + marker, 1)
        html = html.replace('Pick anyone you are weighing us against and see the two of us side by side.', 'Compare acquisition options and STR markets side by side.')
        open(path, "w", encoding="utf-8").write(html)


def main():
    chosen = pairs()
    for a, b in chosen:
        related = [p for p in chosen if p != (a, b) and (a in p or b in p)]
        comparison_page(a, b, related)
    hub(chosen)
    link_existing_compare_hub()
    print(f"Generated {len(chosen)} market comparisons and one hub")


if __name__ == "__main__":
    main()
