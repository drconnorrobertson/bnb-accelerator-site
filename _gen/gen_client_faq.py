#!/usr/bin/env python3
"""Publish the client FAQ source as linked topic pages, preserving every question."""
from pathlib import Path
import json
import re
import html
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import tpl

ROOT = Path(__file__).resolve().parent.parent
HUB = "/faq/client-questions/"
DATE = "2026-09-30"
TOPICS = [
 ("financing-preapproval", "STR Financing and Preapproval", "Compare second-home, conventional investment and DSCR loans, down payments, lender timing and seller-credit limits.", "/financing/"),
 ("evaluating-properties", "Evaluating an STR Property", "Learn how BNB Accelerator screens properties, compares deals and evaluates projected cash flow and cash-on-cash returns.", "/airbnb-investment-property/"),
 ("proforma-revenue", "STR Pro Forma and Revenue Assumptions", "Understand comparable rentals, revenue estimates, launch budgets, operating expenses and projected investment returns.", "/revenue-projections/"),
 ("compliance-regulations", "STR Compliance and Regulatory Risk", "Check address-specific city, county, HOA and permit requirements before purchasing a short-term rental property.", "/regulations/"),
 ("agents-offers", "Buyer Agents, Commission and Offers", "Understand agent introductions, buyer representation, negotiated commissions and the approvals needed to submit an STR offer.", "/how-it-works/"),
 ("offer-strategy-seller-credits", "STR Offer Strategy and Seller Credits", "Compare purchase price, seller concessions, furniture, counteroffers and contract protections when negotiating an STR purchase.", "/buy-a-short-term-rental/"),
 ("under-contract", "Your STR Purchase Under Contract", "Know what happens after acceptance, who coordinates the transaction, your responsibilities and the milestones before closing.", "/how-it-works/"),
 ("earnest-money-deadlines", "Earnest Money and Contract Deadlines", "Understand earnest-money deposits, contingency deadlines, extensions, termination notices and deposit-release procedures.", "/buy-a-short-term-rental/"),
 ("inspections-repairs", "STR Inspections and Repair Negotiations", "Plan inspections, specialist reviews, repair estimates, seller negotiations and reinspections before buying an STR.", "/airbnb-investment-property/"),
 ("appraisals", "STR Purchase Appraisals", "Understand appraisal ordering, timing, low valuations, price negotiations and the limits of appraisal-based equity.", "/financing/"),
 ("insurance", "Short-Term Rental Insurance", "Review STR use, guest liability, dwelling and contents coverage, deductibles, amenities and insurance quote changes.", "/management/"),
 ("llc-title-ownership", "STR LLCs, Title and Ownership", "Coordinate LLC formation, borrower requirements, deed transfers, business accounts and ownership structure with your advisers.", "/financing/"),
 ("existing-rentals-listing-transfer", "Buying an Existing STR and Listing Handoff", "Plan reservation, listing, review and management transitions when buying a property that already operates as an STR.", "/management/"),
 ("management-design-vendors", "STR Managers, Designers and Vendors", "Choose property managers and designers, compare their roles, and organize the vendors needed to launch your rental.", "/design/"),
 ("site-visits-material-participation", "Site Visits and Material Participation", "Plan property visits, operating work and participation records, and confirm qualifying hours and tax tests with your CPA.", "/tax-strategy/material-participation/"),
 ("title-escrow-closing", "Title, Escrow and STR Closing", "Understand title coordination, cash to close, wire verification, signing and the conditions for a completed closing.", "/buy-a-short-term-rental/"),
 ("closing-documents", "STR Closing Documents and Final Numbers", "Review lender disclosures, settlement statements, closing packages, fees and seller credits before funding your purchase.", "/buy-a-short-term-rental/"),
 ("after-closing", "Immediately After Your STR Closing", "Coordinate keys, locks, utilities, management, permitting and the path from ownership to a guest-ready short-term rental.", "/management/"),
 ("utilities-access", "STR Utilities and Property Access", "Resolve utility transfers, proof of ownership, property access and lock changes after buying a short-term rental.", "/management/"),
 ("vendor-payments-coordination", "Vendor Payments and Post-Close Coordination", "Organize approved vendor payments, invoices, repair lists and responsibility for work after closing.", "/design/"),
 ("bookkeeping", "STR Accounting and Bookkeeping", "Set up property records, track income and expenses, reconcile accounts and prepare organized documents for your CPA.", "/tax-strategy/"),
 ("cost-segregation-tax-setup", "Cost Segregation and STR Tax Setup", "Prepare cost segregation records, evaluate bonus depreciation, document improvements and coordinate tax treatment with your CPA.", "/tax-strategy/cost-segregation/"),
]

def clean(s):
    return s.replace("\u2014", ", ").replace("\u000b", "\n").replace("\r", "").strip()

def parse():
    source = json.loads((ROOT / "_gen/client_faq_source.json").read_text())
    groups = []
    current = None
    for p in source:
        if (p.get("style") or "").startswith("HEADING"):
            current = {"source_title": clean(p["text"]), "questions": []}
            groups.append(current)
            continue
        rich = ""
        for run in p["runs"]:
            value = html.escape(run["content"].replace("\u2014", ", ").replace("\u000b", "\n"))
            link = run.get("textStyle", {}).get("link", {}).get("url")
            if link:
                value = '<a href="' + html.escape(link, quote=True) + '">' + value + '</a>'
            rich += value
        for line in rich.splitlines():
            line = line.strip()
            if not line:
                continue
            plain = html.unescape(re.sub("<[^>]+>", "", line))
            if plain.startswith("Inspection + Repair Negotiations"):
                current = {"source_title": plain, "questions": []}
                groups.append(current)
                continue
            match = re.match(r"^((?:How|What|When|Who|Where|Why|Can|Could|Do|Does|Should|Will|Are|Is|Which|Once|If|Seller)[^?]*\?)\s*(.*)$", line)
            if match:
                current["questions"].append({"question": html.unescape(match[1]), "lines": [match[2]] if match[2] else []})
            elif current and current["questions"]:
                current["questions"][-1]["lines"].append(line)
            else:
                raise ValueError("Unassigned source content: " + plain)
    assert len(groups) == len(TOPICS), len(groups)
    return groups

def paragraphs(lines):
    out = []
    in_list = False
    for line in lines:
        bullet = re.match(r"^(?:-\s+|\d+[.)]\s+)(.*)$", line)
        if bullet:
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append("<li>" + bullet[1] + "</li>")
        else:
            if in_list:
                out.append("</ul>")
                in_list = False
            out.append("<p>" + line + "</p>")
    if in_list:
        out.append("</ul>")
    return "\n".join(out)

def hero(title, intro, label):
    return f'<section class="hero hero-page"><div class="wrap"><nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a><span class="sep">/</span><a href="/faq/">FAQ</a><span class="sep">/</span><a href="{HUB}">Client questions</a></nav><div class="hero-inner"><span class="eyebrow">{label}</span><h1>{tpl.esc(title)}</h1><p class="hero-sub">{tpl.esc(intro)}</p></div></div></section>'

def write(path, title, description, body, schema):
    target = ROOT / path.strip("/") / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    page = tpl.page(title=title + " | BNB Accelerator", description=description, path=path, body=body, extra_schema=schema, active="/blog/")
    reference = (ROOT / "faq/index.html").read_text()
    for asset in ("style.min.css", "main.js"):
        match = re.search(r'/assets/' + re.escape(asset) + r'\?v=[a-z0-9]+', reference)
        if match:
            page = page.replace("/assets/" + asset + '"', match[0] + '"')
    target.write_text(page)

def render():
    groups = parse()
    topics = list(TOPICS)
    for slug, title, intro, related, questions in json.loads((ROOT / "_gen/client_faq_expansion.json").read_text()):
        topics.append((slug, title, intro, related))
        groups.append({"source_title": title, "questions": [{"question": q, "lines": [html.escape(a)]} for q, a in questions]})
    overrides = json.loads((ROOT / "_gen/client_faq_edits.json").read_text())
    used = set()
    cards = []
    for i, (group, topic) in enumerate(zip(groups, topics)):
        slug, title, intro, related = topic
        path = HUB + slug + "/"
        items = []
        entities = []
        for n, item in enumerate(group["questions"], 1):
            q = item["question"]
            if q in overrides:
                item["lines"] = overrides[q]
                used.add(q)
            answer = paragraphs(item["lines"])
            assert answer, q
            items.append(f'<details class="faq" id="question-{n}"><summary>{tpl.esc(q)}</summary><div class="faq-answer">{answer}</div></details>')
            entities.append({"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": html.unescape(re.sub("<[^>]+>", " ", answer))}})
        prior = topics[max(0, i-1)]
        following = topics[min(len(topics)-1, i+1)]
        body = hero(title, intro, "Client FAQ") + f'<section><div class="wrap wrap-narrow"><p class="lead">Practical answers for buying and launching a short-term rental with BNB Accelerator. Updated September 30, 2026.</p><nav class="faq-nav" aria-label="Related resources"><a href="{HUB}">All client questions</a><a href="{related}">Read the related guide</a><a href="/apply/">Book a Call</a></nav>' + "".join(items) + f'<nav class="faq-nav" aria-label="More FAQ topics"><a href="{HUB}{prior[0]}/">{tpl.esc(prior[1])}</a><a href="{HUB}{following[0]}/">{tpl.esc(following[1])}</a></nav></div></section>' + tpl.cta_band("Plan your next STR purchase", "Discuss your budget, target markets and timeline with our acquisition team.")
        schema = tpl.graph(json.dumps({"@type": "FAQPage", "url": tpl.SITE + path, "dateModified": DATE, "mainEntity": entities}), tpl.breadcrumb_schema([("Home", "/"), ("FAQ", "/faq/"), ("Client questions", HUB), (title, path)]))
        write(path, title, intro, body, schema)
        cards.append(f'<a class="card" href="{path}"><div class="card-body"><span class="eyebrow">{len(entities)} questions</span><h2>{tpl.esc(title)}</h2><p>{tpl.esc(intro)}</p><span class="card-link">Read answers</span></div></a>')
    assert used == set(overrides), "Unused corrections: " + str(set(overrides)-used)
    count = sum(len(x["questions"]) for x in groups)
    description = f"Browse {count} client questions across financing, deal analysis, contracts, inspections, closing, launch, bookkeeping and STR tax setup."
    body = hero("Your STR purchase and launch: client FAQ", description, "BNB Accelerator client resources") + f'<section><div class="wrap"><p class="lead">Follow the purchase from preapproval to the first guest. Choose a topic for detailed answers, or read the <a href="/short-term-rental-questions/">10 essential buyer questions</a> for a shorter introduction.</p><div class="grid grid-3">{"".join(cards)}</div></div></section>' + tpl.cta_band("Get a clear acquisition plan", "Bring your goals and questions to a call with the BNB Accelerator team.")
    schema = tpl.graph(json.dumps({"@type": "CollectionPage", "name": "BNB Accelerator Client FAQ", "url": tpl.SITE + HUB, "dateModified": DATE}), tpl.breadcrumb_schema([("Home", "/"), ("FAQ", "/faq/"), ("Client questions", HUB)]))
    write(HUB, "STR Purchase and Launch Client FAQ", description, body, schema)
    print(json.dumps({"topics": len(groups), "questions": count, "corrections": len(used)}))

if __name__ == "__main__":
    render()
