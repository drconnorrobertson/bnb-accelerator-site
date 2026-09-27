#!/usr/bin/env python3
"""Editorial alternatives pages for distinct STR buyer decisions.

Run before sitewide.py, gen_site_index.py, and build_assets.py.
Claims about other services are deliberately limited to their published scope.
"""
import os
import sys
from html import escape

sys.path.insert(0, os.path.dirname(__file__))
import tpl
from pillars import write

DATE = "2026-09-27"
# slug, company, category, official source, existing comparison, buyer question,
# strong fit, three genuine paths (name, fit, tradeoff), diligence question
PAGES = [
    ("the-short-term-shop", "The Short Term Shop", "specialist STR brokerage",
     "https://theshorttermshop.com/how-to-buy-a-short-term-rental/", "/compare/avery-carl-short-term-shop/",
     "Do you want an STR specialist agent in a chosen market, or a team coordinating the acquisition and launch across several disciplines?",
     "A specialist brokerage can be the right call when you have a market selected and want local representation while directing your own underwriting and launch.",
     [("BNB Accelerator", "Buyers who want sourcing, underwriting, purchase coordination, and launch planning in one engagement.", "Ask for the full scope and service fee before comparing economics with brokerage representation."),
      ("Another local STR agent", "Buyers who know the target market and want representation with local transaction experience.", "You will still need a revenue model, property-level regulatory review, and launch vendors."),
      ("Independent purchase", "Experienced investors with time to research and manage each specialist.", "You take responsibility for screening and coordinating the entire process.")],
     "Who owns the revenue assumptions, municipal and HOA checks, furnishing plan, and operating handoff?"),
    ("techvestor", "Techvestor", "passive STR investment platform",
     "https://www.techvestor.com/", "/compare/techvestor/",
     "Do you want exposure to an STR portfolio, or to buy a specific property whose decisions you control?",
     "Techvestor describes a passive portfolio investment. That can fit someone who values operator management and diversification over choosing an individual property.",
     [("BNB Accelerator", "Buyers seeking direct ownership of a property they approve, with acquisition work coordinated for them.", "You supply purchase capital and remain responsible for ownership decisions and property risk."),
      ("Another STR fund", "Investors who prefer diversified, professionally managed exposure.", "Review fees, liquidity, control, reporting, and tax documents in the offering materials."),
      ("Buy directly with an agent", "Buyers who want a deed and are prepared to direct the analysis and launch.", "Expect a substantial time commitment or separate professional fees.")],
     "Will I own a deed or an interest in a vehicle, and what are the liquidity and tax consequences for my situation?"),
    ("airdna", "AirDNA", "STR market data platform",
     "https://www.airdna.co/", "/compare/airdna/",
     "Are you looking for data to analyze a deal yourself, or help executing the purchase?",
     "AirDNA provides market and listing analytics. It is a useful research tool for investors who already know how to turn data into a property-specific underwriting model.",
     [("BNB Accelerator", "Buyers who want a team to screen properties, challenge assumptions, and coordinate a purchase.", "An acquisition service has a fee and remains limited to its service markets."),
      ("AirDNA plus your own team", "Investors who enjoy modeling, have agents and operators lined up, and want direct access to data.", "Model property taxes, insurance, permits, HOA rules, reserves, and seasonality separately."),
      ("Another data platform", "Buyers comparing forecast methods and comparable sets before making an offer.", "Data products do not replace local due diligence or execute a transaction.")],
     "Which actual comparable listings support the forecast, and what costs and restrictions sit outside it?"),
    ("rabbu", "Rabbu", "STR research and market data platform",
     "https://rabbu.com/airbnb-data", "/compare/rabbu/",
     "Do you need market estimates, or a buyer-side process that turns estimates into a closed and launched property?",
     "Rabbu publishes STR market data and revenue estimates. It can be a useful first screen before a buyer validates a specific property's restrictions and costs.",
     [("BNB Accelerator", "Buyers who want a sourced property, detailed underwriting, negotiation, and closing coordination.", "Confirm the exact deliverables, service territory, and engagement fee."),
      ("Rabbu plus local specialists", "Investors who want to research opportunities and assemble their own agent, lender, inspector, and operator.", "The buyer must reconcile model estimates with the home's condition and expense base."),
      ("A specialist STR brokerage", "Buyers wanting transaction representation after completing their own market screen.", "Ask who is responsible for projections and launch planning.")],
     "What do actual comparable bookings say after fees, tax, insurance, repair, and management assumptions?"),
    ("awning", "Awning", "STR brokerage and management provider",
     "https://awning.com/vacation-rental-buying", "/compare/awning/",
     "Would you rather combine search and ongoing management with one provider, or separate acquisition from operation?",
     "Awning advertises buying tools, investor agents, and property management. It deserves consideration if ongoing management through the same ecosystem matters to you.",
     [("BNB Accelerator", "Buyers seeking a buyer-side acquisition process and freedom to select an independent operator.", "You still need to select and contract with a manager if you will outsource operations."),
      ("Awning", "Buyers who want a connected property search, brokerage, and management path.", "Check which services are available in your exact market and the agreements for each."),
      ("Local agent and manager", "Investors who prefer to select specialists individually.", "You coordinate the underwriting, closing, furnishing, and management handoff.")],
     "Can I choose a different property manager, and how are each provider's fees and incentives disclosed?"),
    ("bnb-mastery", "BNB Mastery", "STR education and coaching program",
     "https://bnbmastery.com/", "/compare/bnb-accelerator-vs-bnb-mastery/",
     "Do you want to learn how to build an STR business yourself, or have an acquisition team execute your first purchase?",
     "BNB Mastery offers courses and coaching, including co-hosting education. It fits buyers who want to learn and apply the operating skill themselves.",
     [("BNB Accelerator", "People with purchase capital who want a team to source, underwrite, and coordinate the acquisition.", "This is a property purchase with financing, carrying costs, and ownership risk."),
      ("BNB Mastery", "People who want coaching, community, and a skill they can apply to future deals or co-hosting.", "Education does not purchase, finance, or launch a property on your behalf."),
      ("DIY with local specialists", "Buyers comfortable assembling a team while learning from free and paid resources.", "Your time and the quality of your own decisions become the main constraints.")],
     "At the end of the engagement, what work has been done for me versus what have I learned to do myself?"),
    ("robuilt", "Robuilt", "STR education and unique-stay coaching",
     "https://www.hostcamp.com/coaching", "/compare/bnb-accelerator-vs-robuilt/",
     "Do you want to create and operate a distinctive stay, or buy an existing property with an acquisition team?",
     "Robuilt's Host Camp coaching focuses on building a distinctive short-term-rental business. It may fit someone excited by the creative and operating work.",
     [("BNB Accelerator", "Buyers who want help acquiring and launching an existing STR without managing a custom build.", "Existing properties still need careful checks of rules, condition, and economics."),
      ("Host Camp coaching", "Operators who want to learn the process and actively design their own concept.", "You lead the project and carry execution, renovation, and timeline risk."),
      ("Local architect and agent", "Experienced buyers with a specific unique-stay site and a professional build team.", "Permits, budget overruns, and launch timing require hands-on management.")],
     "Is my goal to acquire an operating asset soon, or to develop a particular concept over a longer timeline?"),
    ("rent-to-retirement", "Rent to Retirement", "turnkey rental property provider",
     "https://www.renttoretirement.com/turnkey-properties", "/compare/rent-to-retirement/",
     "Are you shopping a prepared rental from available inventory, or searching broadly for an STR under your own buy box?",
     "Rent to Retirement markets turnkey rentals, including renovated or newly built property with management arrangements. It fits investors who want to evaluate available inventory.",
     [("BNB Accelerator", "Buyers focused on short-term rentals who want buy-side sourcing and an acquisition plan tailored to a buy box.", "A separate service fee and the costs of purchasing and launching must be modeled."),
      ("Rent to Retirement", "Buyers who prefer a turnkey rental already packaged for ownership and management.", "Check property price, rehab history, rental strategy, manager terms, and inventory incentives."),
      ("Independent local purchase", "Buyers comfortable sourcing a property beyond a provider's inventory.", "You will hire and supervise the diligence and management team yourself.")],
     "Who selected the property, who receives compensation from the transaction, and how does the projected rental model work?"),
    ("alpha-geek-capital", "Alpha Geek Capital", "STR fund and education provider",
     "https://alphageekcapital.com/faqs/", "/compare/alpha-geek-capital/",
     "Do you want to invest in an offering, learn to buy properties, or own a specific STR outright?",
     "Alpha Geek Capital describes fund and single-asset offerings; its related education offerings address active investors. Confirm which opportunity you are evaluating before comparing services.",
     [("BNB Accelerator", "Buyers who want to own and approve a specific property with acquisition coordination.", "Direct ownership requires purchase capital and ongoing asset-level decisions."),
      ("Alpha Geek offering", "Investors who prefer the terms and management of a particular fund or single-asset offering.", "Study the actual offering documents, control, fees, distributions, and liquidity."),
      ("Education and DIY purchase", "Buyers seeking to build their own acquisition and operating skills.", "A course does not guarantee access to a suitable property or execute a purchase.")],
     "Am I buying a property, subscribing to an offering, or purchasing education, and what rights follow?"),
]

def e(s):
    return escape(s, quote=True)

def render_page(row):
    slug, name, category, source, comparison, question, fit, options, diligence = row
    path = f"/compare/alternatives-to-{slug}/"
    title = f"Alternatives to {name} for STR Investors (2026)"
    desc = f"Considering alternatives to {name}? Compare direct STR acquisition, independent buying, and {category} options by the work you want done."
    trail = [("Home", "/"), ("Compare", "/compare/"), ("Alternatives", "/compare/alternatives/"), (f"{name} alternatives", path)]
    cards = "\n".join(f'<article class="card card-static"><h3>{e(label)}</h3><p><strong>Best fit:</strong> {e(who)}</p><p><strong>Check:</strong> {e(caution)}</p></article>' for label, who, caution in options)
    body = f'''<section class="hero hero-page"><div class="wrap">{tpl.breadcrumb_html(trail)}<div class="hero-inner"><span class="eyebrow">Buyer options · Updated September 2026</span><h1>Alternatives to {e(name)}</h1><p class="lead">{e(question)}</p></div></div></section>
<section class="section-sm"><div class="wrap wrap-narrow"><h2>First, decide what you are buying</h2><p>{e(fit)}</p><p>BNB Accelerator coordinates sourcing, property underwriting, negotiation, and the purchase-to-launch process for a property the client chooses to buy. Each option below solves a different part of the STR decision. Compare actual scope, fees, geographic availability, and who takes responsibility for each task before signing.</p></div></section>
<section class="bg-alt"><div class="wrap"><div class="section-head"><span class="eyebrow">Three paths</span><h2>Which alternative fits?</h2></div><div class="grid grid-3">{cards}</div></div></section>
<section class="section-sm"><div class="wrap wrap-narrow"><h2>The question to ask every provider</h2><div class="callout"><p>{e(diligence)}</p></div><p>Request a written list of deliverables and exclusions, a complete fee schedule, a property-specific underwriting model, and the names of the people responsible after closing. Independently verify local short-term-rental rules, financing, insurance, HOA restrictions, and tax treatment with appropriate professionals.</p><p>For a feature-by-feature look, read <a href="{comparison}">BNB Accelerator vs {e(name)}</a>. You can also <a href="/deals/">inspect published deal figures</a> and <a href="/pricing/">review how the acquisition fee is scoped</a>.</p><p class="small text-muted">Provider description checked against <a href="{e(source)}" rel="noopener noreferrer">{e(name)}'s published offering</a> on September 27, 2026. Offerings change. This independent guide is not affiliated with or endorsed by {e(name)}.</p></div></section>
{tpl.cta_band('Talk through your acquisition options', 'Bring your budget, target market, and desired level of involvement. We will discuss whether our service fits.', primary=('/apply/', 'Book a Call'), secondary=('/compare/', 'See more comparisons'))}'''
    schema = tpl.graph(tpl.breadcrumb_schema(trail), tpl.ORG_SCHEMA) + "\n" + tpl.article_schema(title, desc, tpl.SITE + path, DATE, DATE, section="STR Acquisition Alternatives")
    write(path, tpl.page(title=title, description=desc, path=path, body=body, extra_schema=schema, active="/compare/", transparent=True))

def main():
    for row in PAGES:
        render_page(row)
    links = "\n".join(f'<li><a href="/compare/alternatives-to-{slug}/">Alternatives to {e(name)}</a> <span class="text-muted">· {e(category)}</span></li>' for slug, name, category, *_ in PAGES)
    path = "/compare/alternatives/"
    trail = [("Home", "/"), ("Compare", "/compare/"), ("Alternatives", path)]
    body = f'<section class="hero hero-page"><div class="wrap">{tpl.breadcrumb_html(trail)}<div class="hero-inner"><span class="eyebrow">Buyer options</span><h1>STR company alternatives</h1><p class="lead">Choose a company to compare the work performed, ownership model, and decisions you keep.</p></div></div></section><section><div class="wrap wrap-narrow"><ul class="cmp-guides">{links}</ul><p>These guides are independent editorial comparisons. <a href="/compare/">See the full side-by-side comparisons</a>.</p></div></section>'
    write(path, tpl.page(title="STR Company Alternatives: 9 Buyer Guides (2026)", description="Nine practical alternatives guides for short-term-rental investors comparing acquisition services, education, data, brokerage, and passive investing.", path=path, body=body, extra_schema=tpl.graph(tpl.breadcrumb_schema(trail), tpl.ORG_SCHEMA), active="/compare/", transparent=True))
    # The main comparison hub is hand maintained. Keep this link idempotent.
    hub = os.path.join(os.path.dirname(__file__), "..", "compare", "index.html")
    html = open(hub, encoding="utf-8").read()
    marker = '<li><a href="/compare/alternatives/">Alternatives to STR companies</a></li>'
    if marker not in html:
        html = html.replace('<ul class="cmp-guides" data-reveal>', '<ul class="cmp-guides" data-reveal>\n        ' + marker, 1)
        open(hub, "w", encoding="utf-8").write(html)
    print(f"alternatives: {len(PAGES)} guides + hub")

if __name__ == "__main__":
    main()
