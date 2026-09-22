#!/usr/bin/env python3
"""Fresh answers for legacy high-intent searches and a transparent pricing page."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import tpl
from pillars import guide, write

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATE = "2026-09-22"


def current(html):
    return html.replace("2026-08-15", DATE).replace("Updated August 2026", "Updated September 2026")


def pricing():
    trail = [("Home", "/"), ("Pricing", "/pricing/")]
    desc = "What BNB Accelerator's acquisition service costs, what the fee covers, and the separate cash needed to purchase, launch and reserve an STR."
    schema = tpl.graph(tpl.breadcrumb_schema(trail), tpl.ORG_SCHEMA,
        '{"@type":"WebPage","name":"BNB Accelerator Pricing and Total STR Entry Cost","url":"https://www.bnbaccelerator.com/pricing/","dateModified":"2026-09-22"}')
    body = f'''<section class="hero hero-page"><div class="wrap">{tpl.breadcrumb_html(trail)}
      <div class="hero-inner"><span class="eyebrow">Cost and scope</span>
        <h1>What does BNB Accelerator cost?</h1>
        <p class="hero-sub">Separate the service fee from the cost of buying and operating the property before you judge an offer.</p>
      </div></div></section>
    <section><div class="wrap"><article class="article">
      <p class="lead">BNB Accelerator does not publish a fixed service price. The fee depends on the scope agreed for a client, and you should ask for the exact amount, payment schedule, deliverables, and cancellation terms in writing before you commit. The acquisition service fee is separate from the money you invest in the property.</p>
      <h2>There are three budgets, not one</h2>
      <ol>
        <li><strong>Service fee.</strong> Ask which work is included: market research, property sourcing, underwriting, transaction coordination, design direction, launch support, and introductions to independent vendors. Clarify which activities are performed by BNB Accelerator and which by third parties.</li>
        <li><strong>Property entry cash.</strong> Count the down payment, lender and title charges, inspections, insurance deposits, immediate repairs, furniture, photography, permits, and listing setup. See the <a href="/underwriting/cash-needed-to-buy/">full entry-budget example</a>.</li>
        <li><strong>Operating reserves.</strong> Keep cash after closing for a slow ramp, seasonal losses, deductibles, maintenance, and replacement items. A deal that spends every dollar at launch has little room for error.</li>
      </ol>
      <h2>Questions to get answered on a pricing call</h2>
      <ul>
        <li>What is the total service fee for this scope, when is each payment due, and are any amounts refundable?</li>
        <li>What deliverables will I receive before I must approve a property?</li>
        <li>Which outside costs are excluded, including broker, lender, design, management, CPA, insurance, and cost segregation fees?</li>
        <li>Who chooses and pays each vendor, and are there any referral fees or other financial relationships?</li>
        <li>What happens if no suitable property is found within the expected timeline?</li>
      </ul>
      <p>These questions are more useful than comparing a service fee with a projected first-year return. Forecast cash flow is uncertain. An engagement agreement and a property-specific sources-and-uses schedule are documents you can inspect before signing.</p>
      <h2>How to compare the service with doing it yourself</h2>
      <p>Put the written service fee next to the actual tasks it replaces. Estimate what you would pay separately for data, sourcing, transaction help, furnishing coordination, and launch work. Also consider the time you can realistically devote and the decisions you still retain. Do not assign a made-up hourly value to your time merely to justify a fee.</p>
      <p>Review the <a href="/how-it-works/">process and responsibilities</a>, <a href="/reviews/">all public reviews</a>, and <a href="/case-studies/">documented deal examples</a>. Ask for a current written proposal. Neither a positive review nor a successful past deal guarantees that the service or a particular property is right for you.</p>
      <div class="callout"><p><strong>Practical next step:</strong> request an itemized proposal and a complete property budget for your target purchase range. If either is missing, you do not yet know the total commitment.</p></div>
    </article></div></section>
{tpl.cta_band("Get the current scope and fee in writing", "Use a strategy call to review the deliverables, property budget, and risks before signing.")}'''
    write("/pricing/", tpl.page(title="BNB Accelerator Cost and Pricing: What to Ask", description=desc, path="/pricing/", body=body, extra_schema=schema, body_class="blog"))


def response_rate():
    html = guide(slug="airbnb-response-rate", parent="/guides/", parent_name="Guides", title="Airbnb Response Rate: How to Measure and Improve It", h1="How to Improve Airbnb Response Rate Without Living in Your Inbox", eyebrow="Guest operations", description="Understand which Airbnb inquiries affect response rate, how to build reliable coverage, and what to audit when a team or automation handles guest messages.", lead="Response rate is an operating metric, not a reason to send empty automated messages. Airbnb says a host generally needs to respond to a new inquiry within 24 hours to maintain the metric. The real goal is to answer a prospective guest's question accurately while preventing an inquiry from being forgotten.", sections=[
        ("What Airbnb counts", ["Airbnb's current <a href=\"https://www.airbnb.com/help/article/430\" target=\"_blank\" rel=\"noopener\">response-rate help page</a> distinguishes an inquiry from a reservation request. A message sent through Message host needs a response within 24 hours. The platform explains how reservation requests are counted separately, so check the current help article before relying on an old blog's rule of thumb.", "Superhost criteria currently include a response rate of at least 90%, according to <a href=\"https://www.airbnb.com/resources/hosting-homes/a/how-to-become-a-superhost-702\" target=\"_blank\" rel=\"noopener\">Airbnb's Superhost guidance</a>. A 100% internal target leaves room for unexpected outages or handoff failures, but it is not a promise of search placement or bookings."]),
        ("Create an ownership rule", ["Assign one person or team to monitor each new inquiry, with a named backup for evenings, weekends, and time off. Turn on platform notifications and test them on the devices the team actually carries. If a property manager handles messages, put the response window, escalation path, and reporting cadence in the management agreement.", "Create short, editable answers for parking, pets, accessibility, sleeping layout, fees, and arrival instructions. The responder should check the listing and calendar before replying. A quick inaccurate answer can cause a cancellation or dispute even when it protects the response metric."]),
        ("Audit the misses each week", ["Review unanswered inquiries, time to first useful reply, booking conversion, and recurring questions. Group misses by cause: notification failure, unclear ownership, after-hours gaps, or a question that needs a vendor answer. Fix the underlying process rather than sending a generic acknowledgement to every guest.", "Automation can route and draft replies, but someone should own exceptions such as safety, accessibility, refunds, and special requests. The <a href=\"/guides/str-property-management-sop/\">management SOP guide</a> provides a broader handoff framework."])
    ], faqs=[("How fast do I need to answer an Airbnb inquiry?", "Airbnb currently says a new inquiry sent through Message host needs a response within 24 hours to maintain response rate. Faster, useful replies can help guests decide, but check Airbnb's current help article for metric details."), ("Can a co-host or manager maintain my response rate?", "A co-host or manager can handle messages, but the owner should define coverage, escalation, and reporting. Verify who is accountable for each inquiry and audit missed messages.")], related=['<a href="/guides/str-property-management-sop/">STR management SOPs</a>', '<a href="/blog/guest-communication-templates/">Guest communication templates</a>', '<a href="/blog/airbnb-automation-tools/">Automation tools</a>'], read_min=5, section_name="Guest Operations")
    write("/guides/airbnb-response-rate/", current(html))


def recession():
    html = guide(slug="airbnb-recession-risk", parent="/guides/", parent_name="Guides", title="Airbnb in a Recession: Stress-Test an STR", h1="How to Stress-Test an Airbnb for a Recession", eyebrow="Investment risk", description="Model weaker travel demand, lower nightly rates, higher costs and a slower sale before buying a short-term rental that must survive an economic downturn.", lead="No national recession percentage tells you what will happen to one Airbnb. Travel mix, local job demand, drive-to access, debt load, and the owner's cash reserves matter more than a blanket claim that short-term rentals are recession-proof. A useful recession analysis is a property-level downside model.", sections=[
        ("Build a demand shock, not a slogan", ["Start with verified monthly booking history for the property or a comparable set. Reduce booked nights and average daily rate together in the weak months. Remove revenue from the most discretionary booking segments first, such as expensive event weekends, if those segments dominate the base case.", "Do not assume a low nightly rate will automatically refill the calendar. Compare the lower rate with the variable cost of each stay and the minimum price that still contributes to fixed costs. The <a href=\"/underwriting/break-even-occupancy/\">break-even occupancy guide</a> shows the calculation."]),
        ("Hold fixed costs in place", ["Mortgage payments, property tax, insurance, utilities, software, and many management minimums do not fall proportionally with bookings. Run a month-by-month cash-flow table under a base, mild, and severe case. Add a delay in collecting any insurance claim or refund and a repair in the weakest quarter.", "For illustration, a property with $8,000 of monthly booking revenue, $2,000 of variable costs, and $5,000 of fixed costs produces $1,000 before owner taxes. If revenue falls to $6,000 while variable costs only fall to $1,600, it loses $600. The exact threshold changes with the property; the example shows why a 25% revenue decline can erase more than 25% of cash flow."]),
        ("Check survival and the exit", ["Add the negative monthly balances to estimate the liquidity needed until demand recovers. Then consider whether you could operate as a mid-term or long-term rental, subject to local rules and lender terms. Value that fallback on actual long-term rent and expenses, not the STR projection.", "Finally, test a sale after a weak year. A forced sale with transaction costs and a lower price may be the true downside. See <a href=\"/underwriting/downside-scenario/\">our downside-model guide</a> and <a href=\"/blog/str-exit-strategy/\">STR exit strategy</a> before deciding how much leverage to use."])
    ], faqs=[("Are Airbnbs recession-proof?", "No. Travel demand and pricing can weaken while fixed ownership costs continue. The impact varies by market, guest mix, financing, and reserves."), ("What should I model before buying an STR in a downturn?", "Model lower occupancy and nightly rate together, fixed costs, a slow season, repair risk, available reserves, and an alternative permitted use or sale value.")], related=['<a href="/underwriting/downside-scenario/">STR downside scenario</a>', '<a href="/underwriting/break-even-occupancy/">Break-even occupancy</a>', '<a href="/blog/str-exit-strategy/">STR exit strategy</a>'], read_min=5, section_name="Investment Risk")
    write("/guides/airbnb-recession-risk/", current(html))


if __name__ == "__main__":
    pricing()
    response_rate()
    recession()
