#!/usr/bin/env python3
"""Generate the pillar sections: property types, financing, design, management,
revenue projections, tax strategy sub-pages, and STR regulations by state.

Each page is a long-form guide with Article + FAQPage schema, a breadcrumb,
internal links into the market, case study and blog layers, and the standard
CTA band.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tpl

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PUB = "2026-08-15"


def write(path, html):
    full = os.path.join(ROOT, path.strip("/"), "index.html")
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)


def sections_html(sections):
    """sections: list of (h2, [paragraph or ('ul', [items]) or ('table', head, rows)])"""
    out = []
    for h2, blocks in sections:
        out.append(f"        <h2>{h2}</h2>")
        for b in blocks:
            if isinstance(b, str):
                out.append(f"        <p>{b}</p>")
            elif b[0] == "ul":
                items = "\n".join(f"          <li>{i}</li>" for i in b[1])
                out.append(f"        <ul>\n{items}\n        </ul>")
            elif b[0] == "ol":
                items = "\n".join(f"          <li>{i}</li>" for i in b[1])
                out.append(f"        <ol>\n{items}\n        </ol>")
            elif b[0] == "table":
                head = "".join(f"<th>{h}</th>" for h in b[1])
                rows = "\n".join(
                    "              <tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>"
                    for r in b[2])
                out.append(f"""        <div class="table-scroll">
          <table>
            <thead><tr>{head}</tr></thead>
            <tbody>
{rows}
            </tbody>
          </table>
        </div>""")
            elif b[0] == "callout":
                out.append(f'        <div class="callout"><p>{b[1]}</p></div>')
            elif b[0] == "warn":
                out.append(f'        <div class="callout warn"><p>{b[1]}</p></div>')
            elif b[0] == "h3":
                out.append(f"        <h3>{b[1]}</h3>")
    return "\n\n".join(out)


def guide(*, slug, parent, parent_name, title, h1, eyebrow, description, lead,
          sections, faqs, related, read_min=11, section_name="Guides",
          cta=("Find out if this applies to your situation",
               "Thirty minutes tells you whether the strategy fits before you look at a single property.")):
    """Render a long-form guide page under `parent` (a path like '/financing/')."""
    path = f"{parent}{slug}/" if slug else parent
    url = tpl.SITE + path
    trail = [("Home", "/")]
    if slug:
        trail.append((parent_name, parent))
    trail.append((h1 if not slug else eyebrow, path))
    trail[-1] = (trail[-1][0], path)

    rel = "\n".join(f"            <li>{r}</li>" for r in related)

    schema = tpl.graph(
        tpl.breadcrumb_schema(trail),
        tpl.ORG_SCHEMA,
    ) + "\n" + tpl.article_schema(h1, description, url, PUB, section=section_name) \
      + "\n" + tpl.faq_schema(faqs)

    body = f"""
  <section class="hero hero-page">
    <div class="wrap">
      {tpl.breadcrumb_html(trail)}
      <div class="hero-inner">
        <span class="eyebrow">{eyebrow}</span>
        <h1>{h1}</h1>
        <div class="article-meta">
          <span>Updated August 2026</span><span>&middot;</span><span>{read_min} min read</span>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <article class="article">

        <p class="lead">{lead}</p>

{sections_html(sections)}

        <div class="callout">
          <h3>Keep reading</h3>
          <ul>
{rel}
          </ul>
        </div>

{tpl.faq_html(faqs)}

{tpl.AUTHOR_BOX}

      </article>
    </div>
  </section>
{tpl.cta_band(cta[0], cta[1])}"""

    return tpl.page(title=title, description=description, path=path, body=body,
                    extra_schema=schema, body_class="blog")


def hub(*, path, title, h1, eyebrow, description, sub, cards, sections=None,
        faqs=None, related=None, list_name=None):
    """Render a section hub page with a card grid."""
    trail = [("Home", "/"), (eyebrow, path)]
    faqs = faqs or []
    card_html = "\n".join(f"""        <article class="card" data-reveal>
          <h3><a href="{href}">{name}</a></h3>
          <p>{blurb}</p>
        </article>""" for href, name, blurb in cards)

    items = ",\n".join(
        f'        {{ "@type": "ListItem", "position": {i}, "url": "{tpl.SITE}{href}", "name": "{tpl.esc(name)}" }}'
        for i, (href, name, _) in enumerate(cards, 1))

    schema = tpl.graph(
        tpl.breadcrumb_schema(trail),
        f"""    {{
      "@type": "CollectionPage",
      "name": "{tpl.esc(list_name or h1)}",
      "description": "{tpl.esc(description)}",
      "url": "{tpl.SITE}{path}",
      "isPartOf": {{ "@id": "https://mybnbaccelerator.com/#website" }}
    }}""",
        tpl.ORG_SCHEMA,
    ) + "\n" + tpl.graph(
        '    {\n      "@type": "ItemList",\n      "itemListElement": [\n' + items + "\n      ]\n    }")
    if faqs:
        schema += "\n" + tpl.faq_schema(faqs)

    extra = ""
    if sections:
        extra = f"""
  <section class="bg-alt">
    <div class="wrap wrap-narrow">
      <article class="article">
{sections_html(sections)}
      </article>
    </div>
  </section>
"""
    faq_sec = ""
    if faqs:
        rel = ""
        if related:
            rel = ('\n        <div class="callout">\n          <h3>Keep reading</h3>\n          <ul>\n'
                   + "\n".join(f"            <li>{r}</li>" for r in related)
                   + "\n          </ul>\n        </div>\n")
        faq_sec = f"""
  <section>
    <div class="wrap wrap-narrow">
      <article class="article">
{tpl.faq_html(faqs)}
{rel}
      </article>
    </div>
  </section>
"""

    body = f"""
  <section class="hero hero-page">
    <div class="wrap">
      {tpl.breadcrumb_html(trail)}
      <div class="hero-inner">
        <span class="eyebrow">{eyebrow}</span>
        <h1>{h1}</h1>
        <p class="hero-sub">{sub}</p>
        <div class="btn-row">
          <a class="btn btn-accent btn-lg" href="/apply/">Apply Now</a>
          <a class="btn btn-ghost-light btn-lg" href="/case-studies/">See client results</a>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="grid grid-3">
{card_html}
      </div>
    </div>
  </section>
{extra}{faq_sec}{tpl.cta_band(
        "Tell us what you are trying to do",
        "We screen roughly a thousand deals a week and reject about 98%. A thirty minute call tells you whether this fits.")}"""

    return tpl.page(title=title, description=description, path=path, body=body,
                    extra_schema=schema, transparent=True)
