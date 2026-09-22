#!/usr/bin/env python3
"""Source-linked index of public Trustpilot reviews, with original summaries."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import tpl

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BASE = "https://www.trustpilot.com/reviews/"
# Review order follows Trustpilot's public profile on 22 September 2026.
# Summaries are editorial paraphrases, not quotations or verified client facts.
REVIEWS = [
    ("Donte Jefferson", 5, "The reviewer praises help with cash-flow planning and longer-term financial goals.", "69ab623fd3b7ea2921702753"),
    ("abdullah asghar ali", 5, "A brief positive comment about an app; the post gives no details about an STR purchase.", "6984683205e1fa14e48c94c8"),
    ("Waifung Sit", 5, "Describes a Broken Bow purchase positively, while asking for a clearer transaction flow and communication around funds.", "67916cfbacdb45b218a755a0"),
    ("Peter Eck", 5, "Says the team handled much of the research and execution while he and his wife continued their jobs, and mentions a third purchase.", "678062880f9804759554c848"),
    ("Joe Sangiovanni", 5, "Highlights guidance, practical tools, and support for people learning short-term rental investing.", "677c7ae77ac415c1694210cb"),
    ("BU", 1, "Criticizes the program fee, tax and entity guidance, added transfer costs, and the deal comparables. The company disputes the review on Trustpilot.", "677842e946c728573fb336c5"),
    ("Chantal", 5, "Praises the deal sourcing and perceived revenue potential of the opportunities presented.", "65de92c99385056c3bdfa78c"),
    ("James Green", 5, "Describes the team as helpful, knowledgeable, and generous.", "65dde27666ea210d97f5ee48"),
    ("Peter Hu", 5, "Credits the team with a system for acquiring short-term rentals and pursuing long-term wealth.", "65dcfce674560b945515cee0"),
    ("Nick", 5, "Says Connor kept his word and helped identify bottlenecks and workable solutions over a long relationship.", "65dca0ac6d57fa81fbbe50af"),
    ("Customer", 5, "A short endorsement of the team's knowledge.", "65dc830614a5fa370fe76b4e"),
    ("Christopher Barker", 5, "Praises communication, process, helpfulness, and results.", "65dc0cf7d4d9a46114508f37"),
    ("Wes B.", 5, "Calls the team knowledgeable and helpful.", "65dbf7397b992054e6c58f60"),
    ("Dean Mora", 5, "Says the program helped him think differently about STR investing and his financial plans.", "65dbf3a9831996974977ae5a"),
    ("Luke Mansell-ward", 5, "Praises the team's strategy and execution.", "65dbde94c69f29177feb81f8"),
    ("Emily", 5, "Describes an easy process with Connor and Bryce and says she has begun building a real estate portfolio.", "65dbdab317134f799bd27794"),
    ("Hunter Ceroy", 5, "Says he acquired two properties with the team and plans to continue; also discusses tax strategies from his perspective.", "65dbd9e106bdccd817fa4eec"),
    ("Jim Godwin", 5, "Praises communication, professionalism, and process knowledge, and says he would work with the team again.", "65dbd97f2dd6a69aec6037dc"),
    ("Camryn Reed", 5, "Says the team works quickly and professionally and recommends them.", "65dbd5b16ecbe8f9cd0980cf"),
    ("Daniel Kaplan", 5, "Recommends the team for people who want guidance getting started in real estate.", "65dbd2bf93816b862a07bbec"),
    ("Morgan Reed", 5, "Praises the team's STR knowledge, efficiency, and working relationship, and looks forward to future work.", "65dbd1a59409c0611f630ab9"),
    ("Alison Thomas", 5, "Calls the team reliable and knowledgeable about real estate and cash-flowing assets.", "65dbce8b093c6a2b14525b40"),
    ("Rachel Withers", 5, "Praises industry knowledge, communication, and the approach to rental yields and guest experience.", "65dbb901fb5035f15784bdf0"),
    ("Fred Larsen", 5, "A brief positive note about working with the team.", "65dbb3b91f157916c6485b38"),
    ("Marcos Naccarati", 5, "Says the team was reliable and helped him feel comfortable with investment decisions.", "65dbaf5c46af6c59d7686db2"),
    ("ANDRI AN", 5, "Praises property-investment guidance and transaction coordination.", "65d0a4722c657007fc204c4c"),
    ("Kristopher Francisco", 5, "Describes guidance for launching an Airbnb venture and the speed of opportunities presented.", "64f8ea54996dcfea5b11b0b8"),
]


def render():
    cards = []
    items = []
    for i, (name, rating, summary, review_id) in enumerate(REVIEWS, 1):
        url = BASE + review_id
        cards.append(f'''<article class="card" id="review-{i}">
  <p class="post-meta">{rating} of 5 stars · Trustpilot review {i} of {len(REVIEWS)}</p>
  <h2>{tpl.esc(name)}</h2>
  <p>{tpl.esc(summary)}</p>
  <p><a href="{url}" target="_blank" rel="noopener noreferrer">Read the full review on Trustpilot</a></p>
</article>''')
        items.append(f'{{"@type":"ListItem","position":{i},"name":"Review by {tpl.esc(name)}","url":"{url}"}}')
    schema = tpl.graph(
        tpl.breadcrumb_schema([("Home", "/"), ("Reviews", "/reviews/")]),
        tpl.ORG_SCHEMA,
        f'''{{"@type":"CollectionPage","@id":"{tpl.SITE}/reviews/#page","name":"BNB Accelerator Reviews: Public Source Index","url":"{tpl.SITE}/reviews/","description":"Source-linked summaries of all 27 public Trustpilot reviews visible on 22 September 2026, including criticism.","isPartOf":{{"@id":"{tpl.SITE}/#website"}}}}''',
        '{"@type":"ItemList","itemListElement":[' + ','.join(items) + ']}',
    )
    body = f'''<section class="hero hero-page"><div class="wrap">
  {tpl.breadcrumb_html([("Home", "/"), ("Reviews", "/reviews/")])}
  <div class="hero-inner"><span class="eyebrow">Independent reviews</span>
    <h1>BNB Accelerator reviews: all 27 public Trustpilot posts</h1>
    <p class="hero-sub">A source-linked index of the positive, mixed, and critical feedback visible on Trustpilot on 22 September 2026.</p>
  </div>
</div></section>
<section><div class="wrap wrap-narrow"><article class="article">
  <p class="lead">Trustpilot displayed a 4.5 out of 5 TrustScore from 27 reviews when we checked. The 27 entries below are our brief summaries, not quotations or independently verified accounts of a client's results. Follow each link for the reviewer's full text, date, rating, and any company reply.</p>
  <p>We include the one-star review and mixed feedback. Trustpilot reviewers may edit or remove their posts, and the platform's count and TrustScore can change. The source profile is <a href="https://www.trustpilot.com/review/mybnbaccelerator.com" target="_blank" rel="noopener noreferrer">My BnB Accelerator on Trustpilot</a>. See our <a href="/testimonials/">direct feedback and client stories</a> separately.</p>
</article></div></section>
<section class="bg-alt"><div class="wrap"><div class="section-head left"><span class="eyebrow">Review directory</span><h2>Read every source</h2></div>
<div class="grid grid-2">{''.join(cards)}</div></div></section>
{tpl.cta_band("Evaluate the service and the evidence", "Review the original feedback and documented deals before deciding whether our acquisition process fits.", secondary=("/case-studies/", "See case studies"))}'''
    html = tpl.page(title="BNB Accelerator Reviews: All 27 Public Trustpilot Posts", description="Browse source-linked summaries of all 27 public BNB Accelerator Trustpilot reviews, including mixed and critical feedback. Read every original review.", path="/reviews/", body=body, extra_schema=schema, body_class="blog", active=None)
    out = os.path.join(ROOT, "reviews", "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)


if __name__ == "__main__":
    render()
