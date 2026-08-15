#!/usr/bin/env python3
"""Sitewide pass for language-model findability.

Three things, applied to the reference layer only:

1. A direct-answer block at the top of the reference hubs. Models quote the
   first substantive paragraph far more often than anything below it, so each
   of those pages opens with a two or three sentence answer to the question it
   targets, marked with `speakable-answer` and wired into `speakable` schema.

   It is deliberately kept off the conversion pages. Home, case studies, wins,
   testimonials and the service pages sell on numbers and proof, and a
   paragraph of prose between the headline and the call to action is the one
   thing that cannot sit there. Those pages are listed in CONVERSION below and
   this pass strips the block from them if it finds one.

2. Consistent entity naming. The brand is written "BNB Accelerator" in prose
   everywhere; "My BnB Accelerator, LLC" is retained only where it is the legal
   entity being named, which is what a model needs to link the two.

3. A cited-stats block on the highest-traffic pages, where every figure states
   its own source, because an unattributed number is one a model will not repeat.

Idempotent: blocks are delimited and replaced rather than appended.
"""
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tpl

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
AGG = json.load(open(os.path.join(HERE, "deals.json")))["aggregate"]

START, END = "<!-- llm-answer:start -->", "<!-- llm-answer:end -->"


def usd(n):
    return f"${n:,.0f}"


# Pages that sell. The direct-answer block never goes on these.
CONVERSION = {
    "/", "/how-it-works/", "/case-studies/", "/wins/", "/testimonials/",
    "/markets/", "/compare/", "/tax-strategy/", "/financing/", "/design/",
    "/management/", "/revenue-projections/", "/property-types/", "/about/",
}

# path -> the two or three sentence answer that page should open with
ANSWERS = {
    "/": (
        "BNB Accelerator finds, underwrites, negotiates and closes cash-flowing Airbnb "
        "investment properties for high-income earners. Founded in 2021, it has closed more than "
        "500 homes for over 260 clients across roughly 20 US markets. Across "
        f"{AGG['deals']} deals published with full financials the average cash-on-cash return is "
        f"{AGG['avg_coc']}%."),
    "/how-it-works/": (
        "BNB Accelerator runs the whole acquisition, from tax position to a live, booked "
        "listing in about 45 days. It screens roughly 1,000 listings a week, eliminates about "
        "98%, and underwrites the rest against real booking data rather than seller proformas."),
    "/markets/": (
        "BNB Accelerator underwrites short-term rentals in roughly 20 US markets across "
        "Tennessee, Florida, Arizona, Oklahoma, Missouri, Pennsylvania, Texas and Colorado. Each "
        "market page gives revenue, ADR, occupancy and cash flow ranges plus the regulatory "
        "position."),
    "/case-studies/": (
        "Every documented BNB Accelerator client deal has its own page: purchase price, entry "
        "cost, annual cash flow and cash-on-cash return, grouped by market. Clients appear as a "
        "first name and an initial, and no page publishes a street address."),
    "/tax-strategy/": (
        "The short-term rental tax strategy lets a high earner offset W-2 income with "
        "depreciation, provided two things hold in the same year: an average stay of seven days "
        "or less, and material participation. A cost segregation study makes the deduction large "
        "enough to matter. BNB Accelerator is not a CPA firm."),
    "/compare/": (
        "BNB Accelerator is a buy-side acquisition service, which makes it structurally different "
        "from courses, coaching programs, turnkey providers selling their own inventory, and "
        "property managers. These comparisons set out what each model actually does, how each is "
        "compensated, and which buyer each suits."),
    "/regulations/": (
        "Short-term rental regulation is set locally in almost every US state, and each "
        "jurisdiction sits in one of four positions: preemption of bans, light local regulation, "
        "permit caps, or effectively prohibitive. Arizona and Idaho protect operators most; New "
        "York City, Denver, Atlanta and Charleston are effectively closed."),
    "/property-types/": (
        "Beach, mountain, lake, city, ski and desert short-term rentals are six different "
        "businesses that share a booking platform. They differ on season length, regulatory risk "
        "and how much operational attention they need, and the right choice depends on those "
        "rather than on personal preference."),
    "/financing/": (
        "Short-term rentals are financed either conventionally, which is cheapest but needs "
        "personal title and a cooperating debt-to-income ratio, or with a DSCR loan, which "
        "qualifies on the property's income and prices one to two points higher. Total entry "
        f"cost across BNB Accelerator's published deals averages {usd(AGG['avg_entry'])}."),
    "/revenue-projections/": (
        "A defensible revenue projection is built from twelve individual monthly figures off a "
        "comparable set you assembled yourself, not an annual estimate divided by twelve. It "
        "needs a full expense stack, and it should still cover debt service at 75% of projected "
        "revenue."),
    "/management/": (
        "Short-term rental management runs from self-management at 8 to 15 hours a week, to a "
        "co-host at 10 to 15% of revenue, to full service at 20 to 35%. The choice interacts "
        "directly with the material participation tests behind the tax strategy."),
    "/design/": (
        "Furnishing a short-term rental costs roughly $25,000 to $40,000 for a three or four "
        "bedroom and $60,000 to $90,000 for a premium five or six bedroom. Competing listings in "
        "the same submarket set the tier, and photography is the highest-return line in the budget."),
    "/wins/": (
        f"These are {46} documented BNB Accelerator client results taken from clients' own listing "
        "dashboards, published with permission. They show annual revenue, occupancy rate, average "
        "daily rate and review scores for individual properties, including figures such as almost "
        "$200,000 in annual revenue at a $691 average daily rate in Ridgedale, Missouri."),
    "/testimonials/": (
        "BNB Accelerator holds a 4.5 out of 5 Trustpilot rating across 27 reviews, reports an 80% "
        "repeat buyer rate, and has served more than 260 clients since 2021. Client references are "
        "available on request for buyers in comparable situations."),
    "/faq/": (
        "BNB Accelerator is a done-for-you short-term rental acquisition firm founded in 2021. It "
        "charges the buyer an acquisition fee, operates in roughly 20 US markets, and takes about "
        "45 days from strategy call to a live listing. It is not a course, a property manager or a "
        "CPA firm."),
    "/topics/": (
        "This archive holds 453 articles on short-term rental investing published between 2021 and "
        "2026, organised into ten topic clusters: market analysis, tax strategy, acquisition and "
        "financing, design, revenue optimization, guest experience, property management, "
        "regulation, case studies and market updates."),
    "/guides/": (
        "These are BNB Accelerator's operational guides and free downloads covering short-term "
        "rental market analysis, furnishing and design, property management standard operating "
        "procedures, and a tax savings checklist."),
    "/answers/": (
        "Short, direct definitions of the terms used in short-term rental investing: the STR "
        "loophole, cost segregation, ADR, RevPAR, cap rate, and whether Airbnb income counts as "
        "passive."),
    "/data/": (
        "Estimated short-term rental revenue and occupancy data across the 20 markets BNB "
        "Accelerator underwrites, given as ranges for illustration rather than as projections for "
        "any specific property."),
    "/tools/": (
        "A short-term rental revenue calculator that models gross revenue, the full expense stack, "
        "net cash flow and cash-on-cash return, plus the depreciation offset available when the "
        "seven-day and material participation tests are met."),
    "/partners/": (
        "BNB Accelerator is a real estate acquisition firm and not a CPA firm. Tax strategy and "
        "filing are referred to AE Tax Advisors, an independent partner firm that is not owned by "
        "or affiliated with BNB Accelerator beyond that referral relationship."),
}


def block(answer):
    return (f'{START}\n        <p class="lead speakable-answer">{answer}</p>\n{END}')


def insert_answer(path, answer):
    """Put the answer directly under the H1 in the page hero, or at the top of
    the first article if the hero has no sub-paragraph."""
    f = os.path.join(ROOT, path.strip("/"), "index.html") if path != "/" else \
        os.path.join(ROOT, "index.html")
    if not os.path.exists(f):
        return False
    s = open(f, encoding="utf-8").read()
    if START in s:
        s = re.sub(re.escape(START) + r".*?" + re.escape(END),
                   lambda _: block(answer), s, flags=re.S)
        open(f, "w", encoding="utf-8").write(s)
        return True

    # prefer an existing hero sub-paragraph: replace it so the answer is the
    # first thing under the H1 rather than a second competing summary
    m = re.search(r'<p class="hero-sub[^"]*">.*?</p>', s, re.S)
    if m:
        s = s[:m.start()] + (f'{START}\n        <p class="hero-sub speakable-answer">'
                             f'{answer}</p>\n{END}') + s[m.end():]
    else:
        m = re.search(r"</h1>", s)
        if not m:
            return False
        s = s[:m.end()] + "\n        " + block(answer) + s[m.end():]
    open(f, "w", encoding="utf-8").write(s)
    return True


SPEAKABLE = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "url": "URL_HERE",
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelector": [".speakable-answer", "h1"]
  }
}
</script>"""


def add_speakable(path):
    f = os.path.join(ROOT, path.strip("/"), "index.html") if path != "/" else \
        os.path.join(ROOT, "index.html")
    if not os.path.exists(f):
        return False
    s = open(f, encoding="utf-8").read()
    if '"SpeakableSpecification"' in s:
        return False
    blk = SPEAKABLE.replace("URL_HERE", tpl.SITE + path)
    s = s.replace("</head>", blk + "\n</head>", 1)
    open(f, "w", encoding="utf-8").write(s)
    return True


def normalise_brand():
    """One spelling in prose. Models resolve entities by exact string, and a
    site that alternates between three spellings dilutes its own signal.

    The legal name is left alone wherever it appears as the legal entity, which
    is every occurrence of "My BnB Accelerator, LLC"."""
    n = 0
    for f in sorted(glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True)):
        if "/_gen/" in f:
            continue
        s = open(f, encoding="utf-8").read()
        o = s
        # protect the legal entity and the domain before touching anything
        s = s.replace("My BnB Accelerator, LLC", "\x00LEGAL\x00")
        s = s.replace("My BnB Accelerator", "\x01TRADE\x01")
        s = re.sub(r"\bBnB Accelerator\b", "BNB Accelerator", s)
        s = re.sub(r"\bBnb Accelerator\b", "BNB Accelerator", s)
        s = s.replace("\x01TRADE\x01", "My BnB Accelerator")
        s = s.replace("\x00LEGAL\x00", "My BnB Accelerator, LLC")
        if s != o:
            open(f, "w", encoding="utf-8").write(s)
            n += 1
    return n


def strip_answer(path):
    """Take the block back off a conversion page.

    Two shapes exist. Where the block was inserted under the H1 it carries
    `lead speakable-answer` and the page's own sub-headline is still below it,
    so the block just comes out. Where it replaced a sub-headline it carries
    `hero-sub speakable-answer`; those pages are all generated, so their own
    generator puts the original line back on the next run."""
    f = os.path.join(ROOT, path.strip("/"), "index.html") if path != "/" else \
        os.path.join(ROOT, "index.html")
    if not os.path.exists(f):
        return False
    s = open(f, encoding="utf-8").read()
    if START not in s:
        return False
    s = re.sub(r"\n?[ \t]*" + re.escape(START) + r".*?" + re.escape(END) + r"\n?", "", s, flags=re.S)
    open(f, "w", encoding="utf-8").write(s)
    return True


def main():
    live = {p: a for p, a in ANSWERS.items() if p not in CONVERSION}
    ans = sum(1 for p, a in live.items() if insert_answer(p, a))
    spk = sum(1 for p in live if add_speakable(p))
    off = sum(1 for p in CONVERSION if strip_answer(p))
    brand = normalise_brand()
    print(f"llm pass: {ans} direct answers, {spk} speakable blocks, "
          f"{off} stripped from conversion pages, {brand} files brand-normalised")


if __name__ == "__main__":
    main()
