"""Render the decision worksheets into the production output and sitemap."""
import csv
from dataclasses import dataclass
from io import StringIO
import html
from pathlib import Path
import sys
from urllib.parse import quote
import xml.etree.ElementTree as ET

NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
ET.register_namespace("", NS)
SECTION = "decision-worksheets"
START = "<!-- decision-worksheets:start -->"
END = "<!-- decision-worksheets:end -->"

BRAND = 'BNB Accelerator'
ORIGIN = 'https://www.bnbaccelerator.com'
HUB = '/buy-a-short-term-rental/'
HUB_LABEL = 'Short-term rental buyer worksheets'
STYLESHEET = '/assets/style.min.css'
CTA = '/short-term-rental-investment-service/'
CTA_LABEL = 'Explore acquisition support'
REFERENCES = ['/short-term-rental-investment-service/', '/blog/str-buyer-agent-vs-acquisition-team/', '/buy-a-short-term-rental/due-diligence-document-tracker/', '/underwriting/insurance-quote/', '/underwriting/permit-transfer/', '/financing/', '/revenue-projections/', '/tools/str-downside-calculator/', '/buy-a-short-term-rental/investment-memo-template/', '/buy-a-short-term-rental/launch-handoff-checklist/']

SCENARIOS = """
lake-house|a lake house|boat access, shoreline condition and peak-summer demand|dock documents, shoreline photos and a monthly payout export|the dock needs work and its use is limited during the strongest booking months
ski-condo|a ski condo|building access, seasonal demand and shared amenities|association rental rules, parking map and winter utility bills|a seasonal shuttle or advertised building amenity changes after the purchase
beach-house|a beach house|storm exposure, exterior wear and early-season readiness|recent inspection, insurance indications and maintenance history|exterior work pushes launch into the middle of the peak season
urban-condo|an urban condo|building restrictions, parking and noise|recorded declarations, guest entry instructions and the seller’s complaint history|the building changes the guest access process or extends a minimum stay
desert-home|a desert home|cooling reliability, outdoor use and electricity costs|summer utility bills, equipment service records and amenity photos|the cooling system fails during a period with few replacement contractors available
mountain-cabin|a mountain cabin|road access, utilities and winter turnover distance|private road agreement, service contacts and winter arrival instructions|a storm reduces access while the owner still owes the normal carrying costs
rural-farmhouse|a rural farmhouse|service coverage, water systems and group capacity|water and septic records, vendor travel charges and advertised guest count|local vendors need longer lead times and charge more for an urgent visit
a-frame|an A-frame cabin|loft access, usable floor area and furniture delivery|measured floor plan, stair photos and available bed configurations|the loft cannot support the guest count used in the seller’s projections
tiny-home|a tiny home|actual sleeping capacity, storage and utility connections|floor plan, utility service information and measured guest routes|the advertised sleeping arrangement is impractical for the target guest group
historic-home|a historic home|condition, specialized repairs and launch scope|inspection history, prior repair invoices and written alteration constraints|a repair needs a specialist and the original launch date becomes unrealistic
new-construction|a new construction home|completion dates, punch-list ownership and booking assumptions|builder schedule, punch list and comparable rental history|construction slips and the owner starts paying carrying costs before photography
waterfront-cabin|a waterfront cabin|shore access, weather exposure and amenities|boundary documentation, site photos and service invoices|seasonal water levels make a key advertised amenity unavailable
townhouse|a townhouse|shared walls, assigned parking and association obligations|parking assignment, association documents and noise complaint history|a second vehicle cannot park as advertised and the guest mix changes
duplex|a duplex|unit separation, combined revenue and shared systems|unit-level payouts, utility billing and separate entry photos|one unit remains unavailable while shared costs continue
triplex|a triplex|unit-level demand, cleaning overlap and common expenses|unit calendars, turnover logs and a shared-cost breakdown|one unit’s bookings weaken while all three still share insurance and maintenance costs
fourplex|a fourplex|unit-level performance, access and overlapping turnovers|separate unit records, site plan and a documented turnover schedule|several units turn on the same day and the existing crew cannot cover them
luxury-estate|a luxury estate|high-cost amenities, large-group turnover and specialist staffing|amenity service contracts, turnover quotes and occupancy rules|a signature amenity needs downtime and groups require a larger crew than planned
suburban-home|a suburban home|parking, neighbors and amenity fit for ordinary stays|parking photos, house rules and representative booking references|the property depends on group stays that are difficult to operate at the address
manufactured-home|a manufactured home|land arrangement, title records and local service availability|title material, site agreement and maintenance history|the site terms or delivery constraints add obligations absent from projected expenses
mixed-use|a mixed-use property|residential entrances, commercial activity and shared obligations|site plan, leases and operating expense reconciliations|the downstairs business changes its hours and guests experience more noise
property-with-pool|a rental with a pool|pool service, energy use and seasonal availability|equipment age, maintenance contract and recent utility bills|the pool is unavailable during strong booking weeks and still incurs service costs
seller-managed|a seller-managed rental|what the seller handles personally and what can transfer|operating calendar, task log and seller account inventory|the seller’s unpaid labor must be replaced at market rates after closing
manager-operated|a manager-operated rental|contract terms, account control and vendor continuity|management agreement, sample statements and an account ownership inventory|the manager exits and the buyer needs a short overlap to avoid disrupting confirmed stays
furnished-resale|a furnished rental resale|inventory condition, transfer exclusions and replacements|dated inventory, photos and purchase or warranty records|two high-use rooms need refurnishing despite the nominally furnished sale
conversion|a home being converted to a rental|launch timeline, missing rental history and setup scope|scope bids, room inventory and comparable property records|the first booked month arrives later than planned after unanticipated setup work
"""

DECISIONS = """
acquisition-support|Acquisition support|a sample screening memo and a written scope by phase|Ask who supplies the listing shortlist, who confirms the supporting evidence and who owns each handoff to the agent, lender or operator.|an agreement that assigns the diligence, closing and launch roles before you commit
buyer-agent|Buyer-agent selection|a representation agreement, fee schedule and example offer timeline|Compare the agent’s responsibility for offer terms and negotiations with any separate acquisition consultant’s research and coordination scope.|a representation and fee comparison that accounts for referrals and closing costs
due-diligence|Purchase due diligence|a property-specific documents and deadline register|Separate seller statements from independent records, record the exact question each document answers and set an owner for every open item before the relevant contingency date.|a diligence sign-off sheet that records unresolved evidence and who can act on it
insurance-quote|Insurance quote comparison|written indications for the same address and rental use|Give brokers the same occupancy, amenities, operating plan and timing. Compare exclusions, deductibles, inspection conditions and the evidence a lender needs.|an insurance comparison showing quote, outstanding conditions and coverage evidence on separate lines
permit-review|Short-term rental permission review|the address, parcel or unit identifier and written property-specific guidance|Ask the responsible office which approval applies and what changes at ownership transfer. Check association documents and other restrictions separately.|a permission record with the source, scope, date and dependencies for the first bookable night
financing|Rental financing comparison|written scenarios from lenders using the same address, price and loan amount|Compare qualification assumptions, funds due, reserves and terms under the same scenario. Ask what happens when the property’s documented rent is weaker than the projection.|a financing comparison with upfront cash, ongoing payment and approval conditions
revenue-model|Rental revenue underwriting|monthly revenue evidence, available nights and comparable listings|Separate rates, occupancy and available nights. Reconcile seller payouts with stays, adjustments and platform fees before using the records in the base case.|a monthly model with documented inputs and a clearly labeled downside case
cash-flow|Cash-flow stress test|operating expenses, debt payments, carrying costs and a reserve worksheet|Model the months in date order. Separate setup from operations and compare minimum cash balance, cumulative draw and the timing of a recovery.|a liquidity schedule with a base case, change in operating cash and a go-or-reprice trigger
offer-decision|Investment offer screening|a listing, an assumptions register and dated quotes for largest open costs|Compare the current offer case with a lower-revenue scenario and a delayed-launch scenario. Label costs still based on an estimate or allowance.|an offer memo that states which evidence changes the price, terms or decision
closing-handoff|Closing and launch handoff|a responsibility chart and first-bookable-night checklist|Confirm the timing and owner for access, existing reservations, vendor accounts and setup. Tie each handoff to evidence that can be checked before publication.|a dated checklist with an owner, backup contact and completion record for every launch dependency
"""


DECISION_NOTES = (
    ('Ask the team to walk through the issue on a sample deal. In the scope, assign one person to verify it and another to review the finding before the buyer spends money on the next diligence step.', 'A sample memo identifies the records actually checked and shows how the team would communicate a change in the purchase recommendation.'),
    ('Ask each agent which offer term, deadline or document request would protect your ability to investigate this issue. Compare how quickly each agent could get an answer and what it would cost to retain them.', 'The representation agreement explains compensation and the agent can name the evidence that will inform the offer.'),
    ('Create one line in the diligence register for this issue. Add the source needed, how you will verify it independently, the relevant deadline and the person who can act if the answer arrives late.', 'Each material issue has a dated record and a buyer decision that can be made before the applicable deadline.'),
    ('Give both brokers the same written description of this issue and ask which policy term, exclusion or inspection condition applies. Compare their written responses alongside the premium.', 'The broker identifies any open conditions and can explain the path from written indication to documented coverage.'),
    ('Ask whether this issue changes the proposed use or the practical ability to open. Record which answer requires written confirmation from the local office, association or another applicable party.', 'The record identifies applicable approvals for the exact address and which prerequisites must be satisfied before the proposed operation begins.'),
    ('Ask both lenders to quote the same revised assumption for this issue. Record changes to total cash due, reserve requirements and recurring payment in separate columns.', 'Both proposals use the same inputs, and you can identify what triggers a change in loan terms or timing.'),
    ('Enter the month this issue affects and identify which input changes first: available nights, booked nights, rate or an adjustment. Reconcile the revised total back to the original model.', 'Another reader can trace the change to a month and assumption, and distinguish gross room revenue from net payout.'),
    ('Put the first cost in the month you would pay it and carry any later effect through the model. Compare the lowest cash balance with your available reserves and note which obligation stays fixed.', 'The cash schedule shows when a shortfall occurs, how large it gets and which remaining obligations are time-sensitive.'),
    ('Write two offer cases: one with the original assumption and one with a verified change. Record the terms you would revisit and the supporting evidence you would need to do so.', 'The memo makes the price or terms conditional on specific evidence and shows who must confirm it.'),
    ('Put the issue on the closing-to-launch schedule. Identify the affected task, the backup route if it slips and who decides whether to keep the first bookable date.', 'The launch owner can verify the dependency and knows which other tasks or reservations need to change if it slips.'),
)

ADDITIONAL_SCENARIOS = """
carriage-house|a carriage-house rental|shared driveway access, detached utilities and privacy|parcel diagram, utility routing and driveway agreement|guest arrivals cross a shared driveway used by the main residence
basement-suite|a basement-suite rental|dedicated entrances, moisture history and shared utilities|entry photos, moisture inspection and utility allocation|the supplement to the utility bill shows a recurring cost the seller did not allocate
penthouse|a penthouse rental|freight access, association approvals and specialist servicing|elevator booking rules, association documents and recent service invoices|shared elevator reservations compress a planned furnishing window
bungalow|a bungalow rental|limited storage, porch condition and parking layout|floor plan, porch inspection and off-street parking photos|owner storage displaces supplies the turnover team needs to keep onsite
courtyard-property|a courtyard rental|shared-access routes, outdoor hours and separate entrances|site plan, recorded access terms and current house rules|the shared courtyard is unavailable for gatherings during the projected booking season
barn-conversion|a converted barn rental|conversion records, heating costs and service access|completion records, winter fuel bills and contractor service map|the heating system needs more frequent service than the operating budget assumed
log-home|a log home rental|exterior upkeep, weather exposure and specialist maintenance|envelope inspection, stain history and specialist maintenance quotes|exterior maintenance must be scheduled during a normally bookable week
modular-home|a modular home rental|installation records, site-built additions and financing documentation|manufacturer records, installer documents and site improvement invoices|the lender needs records for an addition that the seller cannot immediately supply
canal-home|a canal-front rental|access rights, seawall condition and waterfront upkeep|seawall inspection, waterfront access records and service bids|waterfront repairs restrict use of a key amenity during launch
hillside-home|a hillside rental|driveway grade, drainage and retaining structures|site survey, drainage notes and a retaining-wall inspection|delivery crews require smaller vehicles and additional trips to reach the property
golf-resort-condo|a golf-resort condo rental|resort access, amenity eligibility and seasonal fees|club access terms, fee notices and seller revenue by month|new guests lose access to an amenity assumed in the projected nightly rate
student-market-home|a rental near a university|event-driven demand, ordinary-week bookings and parking|event calendar, ordinary-week statements and parking rules|event weekends book strongly but weekday demand falls short of the annual model
hospital-market-home|a rental near a hospital|stay-length mix, practical commute and opportunity cost of blocked dates|booking lengths, arrival records and local comparable listings|longer stays reduce turnover work but displace several peak-date bookings
rail-access-condo|a rental condo near a rail station|guest access by foot, noise conditions and limited parking|actual walking route, in-unit noise observations and guest parking instructions|evening noise affects the usability of the sleeping area nearest the station
multi-building-compound|a rental property with multiple buildings|unit-level performance, shared operating costs and service capacity|building-level records, site map and shared service contracts|one building cannot launch on time while costs for the entire site begin immediately
"""
READY_WORKSHEETS = ('acquisition-support-barn-conversion', 'acquisition-support-basement-suite', 'acquisition-support-bungalow', 'acquisition-support-canal-home', 'acquisition-support-carriage-house', 'acquisition-support-courtyard-property', 'acquisition-support-golf-resort-condo', 'acquisition-support-hillside-home', 'acquisition-support-hospital-market-home', 'acquisition-support-log-home', 'acquisition-support-modular-home', 'acquisition-support-multi-building-compound', 'acquisition-support-penthouse', 'acquisition-support-rail-access-condo', 'acquisition-support-student-market-home', 'buyer-agent-barn-conversion', 'buyer-agent-basement-suite', 'buyer-agent-bungalow', 'buyer-agent-canal-home', 'buyer-agent-carriage-house', 'buyer-agent-courtyard-property', 'buyer-agent-golf-resort-condo', 'buyer-agent-hillside-home', 'buyer-agent-hospital-market-home', 'buyer-agent-log-home', 'buyer-agent-modular-home', 'buyer-agent-multi-building-compound', 'buyer-agent-penthouse', 'buyer-agent-rail-access-condo', 'buyer-agent-student-market-home', 'cash-flow-barn-conversion', 'cash-flow-basement-suite', 'cash-flow-bungalow', 'cash-flow-canal-home', 'cash-flow-carriage-house', 'cash-flow-courtyard-property', 'cash-flow-golf-resort-condo', 'cash-flow-hillside-home', 'cash-flow-hospital-market-home', 'cash-flow-log-home', 'cash-flow-modular-home', 'cash-flow-multi-building-compound', 'cash-flow-penthouse', 'cash-flow-rail-access-condo', 'cash-flow-student-market-home', 'closing-handoff-basement-suite', 'closing-handoff-bungalow', 'closing-handoff-carriage-house', 'closing-handoff-courtyard-property', 'closing-handoff-penthouse', 'due-diligence-barn-conversion', 'due-diligence-basement-suite', 'due-diligence-bungalow', 'due-diligence-canal-home', 'due-diligence-carriage-house', 'due-diligence-courtyard-property', 'due-diligence-golf-resort-condo', 'due-diligence-hillside-home', 'due-diligence-hospital-market-home', 'due-diligence-log-home', 'due-diligence-modular-home', 'due-diligence-multi-building-compound', 'due-diligence-penthouse', 'due-diligence-rail-access-condo', 'due-diligence-student-market-home', 'financing-barn-conversion', 'financing-basement-suite', 'financing-bungalow', 'financing-canal-home', 'financing-carriage-house', 'financing-courtyard-property', 'financing-golf-resort-condo', 'financing-hillside-home', 'financing-hospital-market-home', 'financing-log-home', 'financing-modular-home', 'financing-multi-building-compound', 'financing-penthouse', 'financing-rail-access-condo', 'financing-student-market-home', 'insurance-quote-barn-conversion', 'insurance-quote-basement-suite', 'insurance-quote-bungalow', 'insurance-quote-canal-home', 'insurance-quote-carriage-house', 'insurance-quote-courtyard-property', 'insurance-quote-golf-resort-condo', 'insurance-quote-hillside-home', 'insurance-quote-hospital-market-home', 'insurance-quote-log-home', 'insurance-quote-modular-home', 'insurance-quote-multi-building-compound', 'insurance-quote-penthouse', 'insurance-quote-rail-access-condo', 'insurance-quote-student-market-home', 'offer-decision-barn-conversion', 'offer-decision-basement-suite', 'offer-decision-bungalow', 'offer-decision-canal-home', 'offer-decision-carriage-house', 'offer-decision-courtyard-property', 'offer-decision-golf-resort-condo', 'offer-decision-hillside-home', 'offer-decision-hospital-market-home', 'offer-decision-log-home', 'offer-decision-modular-home', 'offer-decision-multi-building-compound', 'offer-decision-penthouse', 'offer-decision-rail-access-condo', 'offer-decision-student-market-home', 'permit-review-barn-conversion', 'permit-review-basement-suite', 'permit-review-bungalow', 'permit-review-canal-home', 'permit-review-carriage-house', 'permit-review-courtyard-property', 'permit-review-golf-resort-condo', 'permit-review-hillside-home', 'permit-review-hospital-market-home', 'permit-review-log-home', 'permit-review-modular-home', 'permit-review-multi-building-compound', 'permit-review-penthouse', 'permit-review-rail-access-condo', 'permit-review-student-market-home', 'revenue-model-barn-conversion', 'revenue-model-basement-suite', 'revenue-model-bungalow', 'revenue-model-canal-home', 'revenue-model-carriage-house', 'revenue-model-courtyard-property', 'revenue-model-golf-resort-condo', 'revenue-model-hillside-home', 'revenue-model-hospital-market-home', 'revenue-model-log-home', 'revenue-model-modular-home', 'revenue-model-multi-building-compound', 'revenue-model-penthouse', 'revenue-model-rail-access-condo', 'revenue-model-student-market-home')


@dataclass(frozen=True)
class Scenario:
    slug: str
    description: str
    priorities: str
    evidence: str
    complication: str


@dataclass(frozen=True)
class Decision:
    slug: str
    title: str
    inputs: str
    method: str
    deliverable: str


def records(data, cls):
    return [cls(*line.split("|")) for line in data.strip().splitlines()]


def route(decision, scenario):
    return f"/{SECTION}/{decision.slug}-{scenario.slug}/"


def title(decision, scenario):
    return f"{decision.title} for {scenario.description}"


def link(url, label):
    return f'<a href="{html.escape(url, quote=True)}">{html.escape(label)}</a>'


ORIGINAL_SCENARIO_SLUGS = {item.slug for item in records(SCENARIOS, Scenario)}

def worksheet_download(decision, scenario, priorities):
    output = StringIO(newline="")
    writer = csv.writer(output)
    writer.writerow(["Review item", "Evidence to request", "Source or quote", "Owner", "Due date", "Decision or follow-up"])
    writer.writerow([decision.title, decision.inputs, "", "", "", ""])
    writer.writerow(["Property records", scenario.evidence, "", "", "", ""])
    for item in priorities:
        writer.writerow([item.capitalize(), "", "", "", "", ""])
    writer.writerow(["Scenario to test", scenario.complication, "", "", "", ""])
    writer.writerow(["Before committing", decision.deliverable, "", "", "", ""])
    data_url = "data:text/csv;charset=utf-8," + quote(output.getvalue(), safe="")
    filename = f"{decision.slug}-{scenario.slug}.csv"
    return f'<a class="action" href="{data_url}" download="{filename}">Download this worksheet (CSV)</a>'


def article(decision, scenario, next_decision, next_scenario, reference, notes):
    heading = title(decision, scenario)
    meta = f"Use this worksheet to compare {decision.title.lower()} for {scenario.description}. Review {scenario.priorities} and record what changes your decision."
    other = [
        link(route(next_decision, scenario), title(next_decision, scenario)) if scenario.slug in ORIGINAL_SCENARIO_SLUGS else link(HUB + '#decision-worksheets', HUB_LABEL),
        link(route(decision, next_scenario), title(decision, next_scenario)),
        link(reference, decision.title + " guide"),
    ]
    priorities = scenario.priorities.rsplit(" and ", 1)[0].split(", ", 1) + [scenario.priorities.rsplit(" and ", 1)[-1]]
    checks = "".join(f"<li>{html.escape(item.capitalize())}</li>" for item in priorities)
    response, review = notes
    e = html.escape
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(heading)} | {BRAND}</title>
  <meta name="description" content="{e(meta, quote=True)}">
  <link rel="canonical" href="{ORIGIN}{route(decision, scenario)}">
  <link rel="stylesheet" href="{STYLESHEET}">
  <style>
    .worksheet {{max-width: 52rem; margin: auto; padding: clamp(1rem, 4vw, 3rem); color: #1e2e2a; background: #fff; line-height: 1.65}}
    .worksheet h1 {{font-size: clamp(2rem, 5vw, 3.25rem); line-height: 1.12; margin: 1.25rem 0}}
    .worksheet h2 {{font-size: 1.4rem; margin: 1.75rem 0 .65rem}}
    .worksheet a {{color:#205745; text-decoration: underline}}
    .worksheet table {{width: 100%; border-collapse: collapse; overflow-wrap: anywhere}}
    .worksheet th,.worksheet td {{padding: .55rem; border: 1px solid #bacac4; text-align: left; vertical-align: top}}
    .worksheet .action {{display:inline-block; padding:.65rem .9rem; background:#e9f3ef; margin-top:.7rem}}
  </style>
</head>
<body>
<main class="worksheet" id="main">
  <nav aria-label="Breadcrumb">{link("/", BRAND)} · {link(HUB + "#decision-worksheets", HUB_LABEL)}</nav>
  <article>
    <h1>{e(heading)}</h1>
    <p>Start with {e(decision.inputs)}. For {e(scenario.description)}, bring the following records to the comparison so the decision reflects the actual property rather than a generic brief.</p>
    <p><strong>Property evidence to gather:</strong> {e(scenario.evidence)}.</p>
    <h2>What to check at this property</h2>
    <ul>{checks}</ul>
    <p>{e(decision.method)}</p>
    <h2>Work through this example before committing</h2>
    <p>Suppose {e(scenario.complication)}. Identify which part of {e(decision.title.lower())} changes first, who can verify the impact and when you need their answer. Compare three responses: proceed with documented conditions, revise the scope or schedule, or pause until you have the missing evidence.</p>
    <p>{e(response)}</p>
    <p><strong>Before you proceed:</strong> {e(review)}</p>
    <h2>Record your decision</h2>
    <table>
      <thead><tr><th scope="col">Record</th><th scope="col">What to capture</th></tr></thead>
      <tbody>
        <tr><th scope="row">Evidence</th><td>{e(scenario.evidence.capitalize())}. Add the date, source and the question each record answers.</td></tr>
        <tr><th scope="row">Open issue</th><td>Record the affected room, unit or operating period, the person checking it and the deadline.</td></tr>
        <tr><th scope="row">Decision</th><td>Complete {e(decision.deliverable)}. Add the reason for proceeding, revising or pausing.</td></tr>
      </tbody>
    </table>
    <p>{worksheet_download(decision, scenario, priorities)}</p>
    <p class="action">{link(CTA, CTA_LABEL)}</p>
    <h2>Related guides and worksheets</h2>
    <ul>{"".join(f"<li>{item}</li>" for item in other)}</ul>
  </article>
</main>
</body>
</html>
"""


def add_hub(output, decisions, scenarios):
    groups = []
    for decision in decisions:
        links = "".join(
            f"<li>{link(route(decision, scenario), title(decision, scenario))}</li>"
            for scenario in scenarios
            if scenario.slug in ORIGINAL_SCENARIO_SLUGS or route(decision, scenario).split('/')[-2] in READY_WORKSHEETS
        )
        groups.append(f"<details><summary>{html.escape(decision.title)}</summary><ul>{links}</ul></details>")
    block = (
        START + '<section class="section" id="decision-worksheets"><div class="wrap" style="max-width:52rem;margin:auto;padding:1.5rem">'
        f"<h2>{HUB_LABEL}</h2><p>Pick the decision you’re making and the property type you’re working with. "
        "Each worksheet identifies the evidence to collect, a scenario to work through and what to record before you commit.</p>"
        + "".join(groups) + "</div></section>" + END
    )
    target = output / HUB.lstrip("/") / "index.html"
    existing = target.read_text()
    if START in existing:
        before, tail = existing.split(START, 1)
        _, after = tail.split(END, 1)
        updated = before + block + after
    else:
        close_main = existing.rfind("</main>")
        if close_main == -1:
            raise ValueError(f"No main element in {target}")
        updated = existing[:close_main] + block + existing[close_main:]
    target.write_text(updated)


def add_reference_links(output, decision, scenarios, reference):
    if reference == HUB:
        return
    target = output / reference.lstrip("/")
    if target.is_dir():
        target /= "index.html"
    existing = target.read_text()
    start = f"<!-- worksheet-links:{decision.slug}:start -->"
    end = f"<!-- worksheet-links:{decision.slug}:end -->"
    items = "".join(f"<li>{link(route(decision, scenario), title(decision, scenario))}</li>" for scenario in scenarios)
    block = (
        start + '<section class="section" style="max-width:52rem;margin:auto;padding:1.5rem">'
        f"<h2>{html.escape(decision.title)} worksheets by property type</h2>"
        f"<details><summary>Browse property-specific worksheets</summary><ul>{items}</ul></details></section>" + end
    )
    if start in existing:
        before, rest = existing.split(start, 1)
        _, after = rest.split(end, 1)
        updated = before + block + after
    else:
        marker = "</main>" if "</main>" in existing else "</body>"
        index = existing.rindex(marker)
        updated = existing[:index] + block + existing[index:]
    target.write_text(updated)


def tag(name):
    return f"{{{NS}}}{name}"


def add_sitemap(output, urls):
    main = output / "sitemap.xml"
    tree = ET.parse(main)
    root = tree.getroot()
    if root.tag == tag("sitemapindex"):
        filename = "sitemap-decision-worksheets.xml"
        sitemap_url = f"{ORIGIN}/{filename}"
        if not any(node.text == sitemap_url for node in root.iter(tag("loc"))):
            ET.SubElement(ET.SubElement(root, tag("sitemap")), tag("loc")).text = sitemap_url
        tree.write(main, encoding="utf-8", xml_declaration=True)
        root = ET.Element(tag("urlset"))
        tree = ET.ElementTree(root)
        target = output / filename
    elif root.tag == tag("urlset"):
        target = main
    else:
        raise ValueError(f"Unexpected sitemap format in {main}")
    known = {node.text for node in root.iter(tag("loc"))}
    for url in urls:
        if url not in known:
            ET.SubElement(ET.SubElement(root, tag("url")), tag("loc")).text = url
    tree.write(target, encoding="utf-8", xml_declaration=True)


def main(output):
    scenarios = records(SCENARIOS, Scenario)
    decisions = records(DECISIONS, Decision)
    additional = records(ADDITIONAL_SCENARIOS, Scenario)
    all_scenarios = scenarios + additional
    urls = []
    for index, decision in enumerate(decisions):
        for position, scenario in enumerate(all_scenarios):
            path = route(decision, scenario)
            if position >= len(scenarios) and path.split('/')[-2] not in READY_WORKSHEETS:
                continue
            target = output / path.lstrip("/") / "index.html"
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(article(
                decision, scenario,
                decisions[(index + 1) % len(decisions)] if position < len(scenarios) else decision,
                scenarios[(position + 1) % len(scenarios)],
                REFERENCES[index],
                DECISION_NOTES[index],
            ))
            urls.append(ORIGIN + path)
    if len(urls) != 250 + len(READY_WORKSHEETS) or len(set(urls)) != len(urls):
        raise ValueError("Unexpected worksheet count or duplicate route")
    for decision, reference in zip(decisions, REFERENCES):
        related = scenarios + [item for item in additional if route(decision, item).split('/')[-2] in READY_WORKSHEETS]
        add_reference_links(output, decision, related, reference)
    add_hub(output, decisions, all_scenarios)
    add_sitemap(output, urls)
    print(f"Published {len(urls)} {BRAND} decision worksheets")


if __name__ == "__main__":
    main(Path(sys.argv[1]))
