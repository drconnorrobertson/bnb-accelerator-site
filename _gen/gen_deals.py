#!/usr/bin/env python3
"""Build /deals/ from the client deal tracker.

Every figure comes from the tracker. Nothing is rounded up and nothing is
inferred. Street addresses are deliberately not published: clients appear as a
first name and a market, which is the level of detail the tracker permits us to
share without exposing an identifiable property.

The aggregate figures on this page are computed from the 25 tracker deals that
carry a purchase price, an entry cost, a cash flow figure and a cash-on-cash
return. They describe those deals and are not a claim about every property
BNB Accelerator has ever closed.
"""
import json
import os
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tpl
from pillars import write

HERE = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(HERE, "deals.json")))
AGG, DEALS = D["aggregate"], D["deals"]


def usd(n):
    return f"${n:,.0f}"


def row(d):
    who = d["client"] or f"Client in {d['market'].split(',')[0]}"
    yr = f" &middot; {d['year']}" if d["year"] else ""
    return f"""              <tr>
                <td><strong>{tpl.esc(who)}</strong><span class="deal-sub">{tpl.esc(d['market'])}{yr}</span></td>
                <td>{usd(d['price'])}</td>
                <td>{usd(d['entry'])}</td>
                <td>{usd(d['cash_flow'])}</td>
                <td class="deal-coc"><strong>{d['coc']:.2f}%</strong></td>
              </tr>"""


def card(d):
    who = d["client"] or f"Client in {d['market'].split(',')[0]}"
    yr = f"<span class=\"deal-year\">{d['year']}</span>" if d["year"] else ""
    design = (f'<li><span class="k">Design budget</span><span class="v">{usd(d["design"])}</span></li>'
              if d["design"] else "")
    return f"""        <article class="deal-card" data-market="{d['market_slug']}" data-coc="{d['coc']}">
          <div class="deal-head">
            <h3>{tpl.esc(who)}</h3>
            {yr}
          </div>
          <a class="deal-market" href="/markets/{d['market_slug']}/">{tpl.esc(d['market'])}</a>
          <ul class="spec-list">
            <li><span class="k">Purchase price</span><span class="v">{usd(d['price'])}</span></li>
            <li><span class="k">Total entry cost</span><span class="v">{usd(d['entry'])}</span></li>
            {design}
            <li><span class="k">Annual cash flow</span><span class="v green">{usd(d['cash_flow'])}</span></li>
            <li><span class="k">Cash-on-cash return</span><span class="v green">{d['coc']:.2f}%</span></li>
          </ul>
        </article>"""


def main():
    by_market = defaultdict(list)
    for d in DEALS:
        by_market[d["market"]].append(d)

    market_rows = []
    for m, ds in sorted(by_market.items(), key=lambda x: -len(x[1])):
        avg_coc = sum(x["coc"] for x in ds) / len(ds)
        avg_cf = sum(x["cash_flow"] for x in ds) / len(ds)
        avg_p = sum(x["price"] for x in ds) / len(ds)
        slug = ds[0]["market_slug"]
        market_rows.append([
            f'<a href="/markets/{slug}/">{tpl.esc(m)}</a>', str(len(ds)),
            usd(avg_p), usd(avg_cf), f"{avg_coc:.1f}%"])

    filters = "".join(
        f'<button class="deal-filter" type="button" data-filter="{ds[0]["market_slug"]}">'
        f'{tpl.esc(m.split(",")[0])} <span>{len(ds)}</span></button>'
        for m, ds in sorted(by_market.items(), key=lambda x: -len(x[1])))

    trail = [("Home", "/"), ("Deal Tracker", "/deals/")]

    answer = (
        f"BNB Accelerator's client deal tracker documents {AGG['deals']} closed short-term rental "
        f"purchases across {AGG['markets']} markets, representing {usd(AGG['total_value'])} in "
        f"property value and {usd(AGG['total_cash_flow'])} in combined annual cash flow. The "
        f"average purchase price is {usd(AGG['avg_price'])}, the average total entry cost is "
        f"{usd(AGG['avg_entry'])}, and the average cash-on-cash return is {AGG['avg_coc']}% "
        f"with a median of {AGG['median_coc']}%. Returns on individual deals range from "
        f"{AGG['min_coc']}% to {AGG['max_coc']}%.")

    faqs = [
        ("What is the average cash-on-cash return on a BNB Accelerator deal?",
         f"Across the {AGG['deals']} deals in the published tracker, the average cash-on-cash "
         f"return is {AGG['avg_coc']}% and the median is {AGG['median_coc']}%. {AGG['over20']} of "
         f"{AGG['deals']} deals returned 20% or more, {AGG['over15']} returned 15% or more, and "
         f"{AGG['over10']} returned 10% or more. The full range is {AGG['min_coc']}% to "
         f"{AGG['max_coc']}%."),
        ("How much does a BNB Accelerator property cost?",
         f"The average purchase price across the tracker is {usd(AGG['avg_price'])}, ranging from "
         f"{usd(min(d['price'] for d in DEALS))} to {usd(max(d['price'] for d in DEALS))}. Total "
         f"entry cost, which includes down payment, closing costs and the design and enhancement "
         f"budget, averages {usd(AGG['avg_entry'])}."),
        ("How much cash flow does a BNB Accelerator property produce?",
         f"Average annual cash flow across the tracker is {usd(AGG['avg_cash_flow'])}, and the "
         f"{AGG['deals']} properties produce {usd(AGG['total_cash_flow'])} combined. Cash flow on "
         f"individual deals ranges from {usd(min(d['cash_flow'] for d in DEALS))} to "
         f"{usd(max(d['cash_flow'] for d in DEALS))}."),
        ("How much do you spend on design and furnishing?",
         f"The average design and enhancement budget across the tracker is {usd(AGG['avg_design'])}. "
         f"That is a separate line from the down payment and closing costs, and all three together "
         f"make up the total entry cost."),
        ("Are these results typical?",
         "No. These are the actual figures for these specific properties, published because they "
         "are documented. They are not typical, not projections, and not a promise of what any "
         "other property will do. Results depend on purchase price, financing, market performance, "
         "management quality and your own tax situation. Real estate involves risk, including loss "
         "of principal."),
        ("Does this tracker show every BNB Accelerator deal?",
         "No. It is the subset of closed purchases for which full financials have been documented "
         "and cleared for publication. BNB Accelerator has closed over 500 homes for more than 260 "
         "clients since 2021; this page covers the deals where every figure can be shown."),
    ]

    schema = tpl.graph(
        tpl.breadcrumb_schema(trail),
        f"""    {{
      "@type": "Dataset",
      "name": "BNB Accelerator client deal tracker",
      "description": "{tpl.esc(answer)}",
      "url": "{tpl.SITE}/deals/",
      "creator": {{ "@id": "https://mybnbaccelerator.com/#organization" }},
      "variableMeasured": [
        {{ "@type": "PropertyValue", "name": "Deals documented", "value": {AGG['deals']} }},
        {{ "@type": "PropertyValue", "name": "Total property value", "value": {AGG['total_value']}, "unitCode": "USD" }},
        {{ "@type": "PropertyValue", "name": "Combined annual cash flow", "value": {AGG['total_cash_flow']}, "unitCode": "USD" }},
        {{ "@type": "PropertyValue", "name": "Average cash-on-cash return", "value": {AGG['avg_coc']}, "unitText": "PERCENT" }},
        {{ "@type": "PropertyValue", "name": "Median cash-on-cash return", "value": {AGG['median_coc']}, "unitText": "PERCENT" }},
        {{ "@type": "PropertyValue", "name": "Average purchase price", "value": {AGG['avg_price']}, "unitCode": "USD" }},
        {{ "@type": "PropertyValue", "name": "Average total entry cost", "value": {AGG['avg_entry']}, "unitCode": "USD" }},
        {{ "@type": "PropertyValue", "name": "Markets represented", "value": {AGG['markets']} }}
      ]
    }}""",
        tpl.ORG_SCHEMA,
    ) + "\n" + tpl.faq_schema(faqs)

    body = f"""
  <section class="hero hero-page">
    <div class="wrap">
      {tpl.breadcrumb_html(trail)}
      <div class="hero-inner">
        <span class="eyebrow">Deal Tracker</span>
        <h1>{AGG['deals']} closed deals, with the actual numbers</h1>
        <p class="hero-sub speakable-answer">{answer}</p>
        <div class="btn-row">
          <a class="btn btn-accent btn-lg" href="/apply/">Apply Now</a>
          <a class="btn btn-ghost-light btn-lg" href="/wins/">See client wins</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section-sm">
    <div class="wrap">
      <div class="stats-grid">
        <div class="stat"><span class="stat-num">{AGG['deals']}</span><span class="stat-label">Deals documented</span></div>
        <div class="stat"><span class="stat-num">{usd(AGG['total_value'])}</span><span class="stat-label">Total property value</span></div>
        <div class="stat"><span class="stat-num">{usd(AGG['total_cash_flow'])}</span><span class="stat-label">Combined annual cash flow</span></div>
        <div class="stat"><span class="stat-num">{AGG['avg_coc']}%</span><span class="stat-label">Average cash-on-cash</span></div>
        <div class="stat"><span class="stat-num">{usd(AGG['avg_price'])}</span><span class="stat-label">Average purchase price</span></div>
        <div class="stat"><span class="stat-num">{AGG['markets']}</span><span class="stat-label">Markets represented</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="section-head" data-reveal>
        <span class="eyebrow">Every deal</span>
        <h2>The full tracker</h2>
        <p>Sorted by cash-on-cash return. Purchase price, total entry cost and annual cash flow are the figures recorded at closing and after the first full year of operation. Client surnames and street addresses are withheld.</p>
      </div>
      <div class="deal-filters">
        <button class="deal-filter is-active" type="button" data-filter="all">All markets <span>{AGG['deals']}</span></button>
        {filters}
      </div>
      <div class="deal-grid">
{chr(10).join(card(d) for d in DEALS)}
      </div>
      <p class="text-muted center mt-3" data-deal-empty hidden>No deals in that market yet.</p>
    </div>
  </section>

  <section class="bg-alt">
    <div class="wrap">
      <div class="section-head" data-reveal>
        <span class="eyebrow">By market</span>
        <h2>How the markets compare</h2>
        <p>Averages across the deals in the tracker. Small sample sizes in several markets, so read the deal count alongside the average.</p>
      </div>
      <div class="table-scroll">
        <table>
          <thead><tr><th>Market</th><th>Deals</th><th>Avg purchase price</th><th>Avg annual cash flow</th><th>Avg cash-on-cash</th></tr></thead>
          <tbody>
{chr(10).join("            <tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in market_rows)}
          </tbody>
        </table>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="table-scroll">
        <table>
          <thead><tr><th>Client</th><th>Purchase price</th><th>Total entry</th><th>Annual cash flow</th><th>Cash-on-cash</th></tr></thead>
          <tbody>
{chr(10).join(row(d) for d in DEALS)}
          </tbody>
        </table>
      </div>
      <p class="disclaimer mt-4">Figures are the actual recorded numbers for these specific properties. They are not typical, not projections, and not a promise of what any other property will do. Cash-on-cash return is annual cash flow divided by total entry cost. Real estate involves risk, including loss of principal.</p>
    </div>
  </section>

  <section class="bg-alt">
    <div class="wrap wrap-narrow">
      <article class="article">
{tpl.faq_html(faqs)}
        <div class="callout">
          <h3>Keep reading</h3>
          <ul>
            <li><a href="/case-studies/">The written case studies behind several of these deals</a></li>
            <li><a href="/wins/">Client wins with revenue and occupancy screenshots</a></li>
            <li><a href="/markets/">Market analysis for every market in this table</a></li>
            <li><a href="/revenue-projections/">How we underwrite a deal before it becomes a row here</a></li>
          </ul>
        </div>
      </article>
    </div>
  </section>
{tpl.cta_band(
        "Want to see what your numbers would look like?",
        "A thirty minute call covers your income, your tax position, and which of these markets actually fits what you are trying to do.")}"""

    write("/deals/", tpl.page(
        title=f"BNB Accelerator Deal Tracker: {AGG['deals']} Closed Deals With Real Numbers",
        description=(f"{AGG['deals']} documented BNB Accelerator deals: {usd(AGG['total_value'])} "
                     f"in property value, {AGG['avg_coc']}% average cash-on-cash return, "
                     f"{usd(AGG['avg_cash_flow'])} average annual cash flow across "
                     f"{AGG['markets']} markets."),
        path="/deals/",
        body=body,
        extra_schema=schema,
        active="/deals/",
        transparent=True,
    ))
    print(f"deals: {AGG['deals']} deals, {AGG['markets']} markets, avg CoC {AGG['avg_coc']}%")


if __name__ == "__main__":
    main()
