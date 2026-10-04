#!/usr/bin/env python3
"""Distinct brand research, evidence and downside resources; safe to rerun."""
from pathlib import Path
import re
import tpl
from pillars import sections_html
ROOT = Path(__file__).resolve().parents[1]

def write(path, title, description, h1, lead, sections, extra=''):
    trail = [('Home', '/'), (h1, path)]
    body = '<section class="hero hero-page"><div class="wrap">' + tpl.breadcrumb_html(trail)
    body += '<span class="eyebrow">Investor resources</span><h1>' + h1 + '</h1></div></section>'
    body += '<section><div class="wrap wrap-narrow"><article class="article"><p class="lead">' + lead + '</p>'
    body += '<p>Published October 4, 2026 · BNB Accelerator editorial team</p>' + sections_html(sections) + extra + '</article></div></section>'
    body += tpl.cta_band('Discuss the purchase you are considering', 'Bring your budget, timeline and unanswered questions to the conversation.')
    schema = tpl.graph(tpl.ORG_SCHEMA, tpl.breadcrumb_schema(trail)) + tpl.article_schema(h1, description, tpl.SITE + path, '2026-10-04')
    target = ROOT / path.strip('/') / 'index.html'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(tpl.page(title=title, description=description, path=path, body=body, extra_schema=schema), encoding='utf-8')

write('/research-bnb-accelerator/', 'Research BNB Accelerator: Process, Costs & Evidence',
      'Research BNB Accelerator using its service scope, pricing questions, original public reviews, property examples and buyer responsibility guides.',
      'Research BNB Accelerator before choosing an acquisition service',
      'Use this company-published guide to connect the service description to the proposal, public feedback and property evidence. It is a navigation resource, not an independent review or rating.', [
    ('Start with the work you want help completing', [
        'BNB Accelerator helps buyers coordinate short-term rental sourcing, analysis, purchase milestones and launch planning. You provide the capital, approve the investment and retain responsibility for your decisions. Independent professionals perform their separately contracted services. The written engagement determines what your fee includes.',
        'Read the <a href="/done-for-you-airbnb/">acquisition service scope</a> and <a href="/how-it-works/">purchase process</a>. Use the <a href="/guides/str-service-responsibility-matrix/">responsibility matrix</a> to ask who performs, approves and pays for each deliverable.']),
    ('Find the right answer for your question', [
        ('table', ['Your question', 'Resource', 'What to check'], [
            ['What does it cost?', '<a href="/pricing/">Pricing and purchase budget</a>', 'Current written fee, milestones, exclusions and cancellation terms'],
            ['What do reviewers say?', '<a href="/reviews/">Public review source index</a>', 'Original post, date, context and company response'],
            ['What has happened on particular deals?', '<a href="/case-studies/">Client property examples</a>', 'Period, source, expenses and whether a figure is historical or modeled'],
            ['How do alternatives differ?', '<a href="/compare/">Service comparisons</a>', 'Ownership, deliverables and separately contracted work'],
            ['Where would I buy?', '<a href="/markets/">Market directory</a>', 'Property-specific economics and permitted use'],
            ['Who is behind the company?', '<a href="/about/">About BNB Accelerator</a>', 'Team roles and the business model']])]),
    ('Read reviews and results as different kinds of evidence', [
        'A review describes a person\'s experience. A property case study describes a particular transaction or operating example. Neither establishes a representative return for every buyer. This website and its summaries are published by BNB Accelerator; follow external links to read feedback on the source platform.',
        'The <a href="/reviews/">review index</a> includes critical and mixed feedback in its dated snapshot. Read the original review and any response rather than assuming a short summary settles a dispute. Use our <a href="/guides/reading-str-case-study-results/">case study evidence guide</a> to interpret financial figures.']),
    ('Questions to resolve before signing', [
        ('ol', ['What deliverables are included and which vendors invoice separately?', 'What is payable if no property closes or the purchase is delayed?', 'Which records support the revenue model, and what remains unverified?', 'Who checks address-specific rental permissions, insurance and financing?', 'What does the downside case show after reserves and debt payments?', 'Which launch tasks and ongoing owner responsibilities remain mine?']),
        'Keep answers with the proposal and contracts. If a service concern arises, use the contact instructions in your signed engagement and identify the deliverable, relevant dates, supporting records and resolution you are requesting. Preserve the original correspondence.']),
    ('Evaluate fit with a complete budget', [
        'Coordination can help a buyer who has capital and wants acquisition support. It still requires timely approvals, independent professional advice and oversight of the operating arrangement. Buyers who need guaranteed returns, have no reserve capacity or cannot participate in approvals should reassess the purchase before proceeding.',
        'Use the <a href="/buy-a-short-term-rental/acquisition-budget-worksheet/">acquisition budget worksheet</a> and <a href="/tools/str-downside-calculator/">downside calculator</a>. Review the property as an investment before relying on any possible tax outcome.'])])

write('/guides/reading-str-case-study-results/', 'How to Read STR Case Study Results | BNB Accelerator',
      'Evaluate STR case studies by separating purchase facts, forecasts, historical operating results and tax illustrations, with a checklist of source evidence.',
      'How to read short-term rental case study results',
      'A purchase price, forecast and operating result answer different questions. Before comparing properties, identify the source, covered period and expense definition behind each number.', [
    ('Classify every important figure', [
        ('table', ['Figure type', 'Evidence to request', 'Interpretation'], [
            ['Acquisition fact', 'Closing statement or final invoice', 'A transaction amount, not an operating return'],
            ['Forecast', 'Dated model with assumptions and comparable set', 'An estimate that may differ from future results'],
            ['Historical operating result', 'Same-period booking records, payouts and expense statements', 'A result for the stated period and operating arrangement'],
            ['Client-reported result', 'Original statement and supporting records where available', 'A report that may not have been independently verified'],
            ['Tax illustration', 'Explicit assumptions and a separate CPA analysis', 'A modeled scenario, not proof of a client deduction or refund']]),
        'If the source does not establish whether annual cash flow is a forecast or a full-year result, treat that classification as unresolved. Do not convert a monthly screenshot into an annual result or describe a modeled tax amount as a verified saving.']),
    ('Match the period and expense definition', [
        'Separate accommodation revenue from cleaning charges, taxes collected, cancellations and refunds. Ask whether expenses include management, platform charges, utilities, insurance, property taxes, repairs, debt payments and capital reserves. An operating statement that excludes debt service is different from cash available to the owner.',
        'Illustration: $100,000 annual accommodation revenue minus $25,000 variable expenses, $20,000 fixed costs, $30,000 debt service and $5,000 reserves leaves $20,000 modeled cash flow. On $160,000 cash invested, the modeled cash-on-cash return is 12.5%. These are invented inputs, not client results.']),
    ('Use a complete and consistent investment denominator', [
        'Ask whether cash invested includes down payment, closing costs, acquisition fees, improvements, furnishings and funded reserves. For financed purchases, total cash invested and property purchase price are different denominators. Compare returns only when both pages use the same definition.',
        'A $20,000 cash-flow figure divided by a $100,000 down payment is 20%; divided by $160,000 complete cash investment it is 12.5%. The arithmetic can be correct in both calculations while the labels describe different things.']),
    ('Check the selection and the limits', [
        'Selected case studies are examples, not a complete performance distribution. Ask how examples were chosen and whether comparable purchases with delays, higher costs or weaker performance are represented. Another buyer\'s repeat purchase or positive review does not prove what your property will earn.',
        'Do not infer independent auditing from a company-published table. Public summaries can omit private source documents; request the evidence relevant to your proposed purchase through the appropriate secure process.']),
    ('Apply the questions to your own deal', [
        'Browse <a href="/case-studies/">BNB Accelerator property examples</a>, then use the <a href="/guides/str-deal-evidence-register/">evidence register</a> to record sources and unresolved assumptions. Stress-test the inputs with the <a href="/tools/str-downside-calculator/">downside calculator</a>.',
        'For tax illustrations, have your own CPA evaluate eligibility and applicable loss limits. Acquisition coordination does not establish a usable tax deduction.'])])

FIELDS = [('revenue', 'Annual accommodation revenue ($)', 100000, None), ('variable', 'Variable costs (% of accommodation revenue)', 25, 100), ('fixed', 'Annual fixed operating costs ($)', 20000, None), ('debt', 'Annual debt payments ($)', 30000, None), ('reserve', 'Annual reserve allocation ($)', 5000, None), ('cash', 'Total cash invested, including funded reserves ($)', 160000, None), ('drop', 'Downside revenue decline (%)', 20, 100)]
fields = ''
for key, label, value, maximum in FIELDS:
    limit = f'max="{maximum}"' if maximum else ''
    fields += f'<div class="field"><label for="{key}">{label}</label><input id="{key}" name="{key}" type="number" min="0" {limit} step="any" value="{value}" required></div>'
calculator = '''<h2>Compare your base case with lower revenue</h2><p>Default values are invented examples. Replace every input with your own evidence-backed assumptions. Enter all expenses on an annual basis and avoid counting the same expense twice.</p>
<form id="downside-form" class="card"><div class="grid grid-2">''' + fields + '''</div><button type="submit" class="btn btn-primary">Calculate downside</button><p id="calc-error" role="alert"></p></form>
<div id="downside-results" aria-live="polite" aria-atomic="true"></div>
<noscript><p>Enable JavaScript to calculate interactively, or use the formulas below with your own inputs.</p></noscript>
<h2>How the calculation works</h2><p>Variable costs = accommodation revenue × variable-cost percentage. Cash flow = revenue − variable costs − fixed operating costs − debt payments − reserve allocation. Cash-on-cash = annual cash flow ÷ total cash invested × 100.</p>
<p>Break-even revenue = (fixed costs + debt payments + reserves) ÷ (1 − variable-cost percentage). This is an annual accommodation-revenue threshold, not an occupancy forecast. At 100% variable costs there is no positive contribution to cover fixed costs.</p>
<p>Downside revenue = base revenue × (1 − decline percentage). The model keeps fixed costs, debt payments and reserves unchanged and scales variable costs proportionally. Costs with minimums, tiered fees, major repairs or refinancing need a separate model. Tax effects, appreciation and sale proceeds are excluded.</p>
<script src="/assets/str-downside-calculator.js" defer></script>'''
write('/tools/str-downside-calculator/', 'STR Downside & Break-Even Calculator | BNB Accelerator',
      'Stress-test short-term rental cash flow against a revenue decline, calculate annual break-even revenue and compare cash-on-cash returns with explicit assumptions.',
      'Short-term rental downside and break-even calculator',
      'See how lower accommodation revenue changes modeled cash flow after operating costs, debt payments and reserves. Calculations are illustrations based on your inputs, not property forecasts.', [
    ('Build the inputs from evidence', ['Use same-period records and itemized quotes. The <a href="/guides/str-deal-evidence-register/">deal evidence register</a> helps track source quality. For acquisition cash requirements, use the <a href="/buy-a-short-term-rental/acquisition-budget-worksheet/">budget worksheet</a>.'])], calculator)

block = '''<!-- brand-decision-center:start --><section class="bg-alt"><div class="wrap wrap-narrow"><h2>Research the service and check the numbers</h2><p>Use the <a href="/research-bnb-accelerator/">BNB Accelerator research guide</a>, learn <a href="/guides/reading-str-case-study-results/">how to read case study results</a>, and test your assumptions with the <a href="/tools/str-downside-calculator/">downside and break-even calculator</a>.</p></div></section><!-- brand-decision-center:end -->'''
for file in ['index.html', 'about/index.html', 'pricing/index.html', 'reviews/index.html', 'case-studies/index.html', 'tools/index.html', 'guides/index.html', 'compare/index.html']:
    target = ROOT / file
    source = re.sub(r'<!-- brand-decision-center:start -->.*?<!-- brand-decision-center:end -->', '', target.read_text(), flags=re.S)
    target.write_text(source.replace('</main>', block + '\n</main>', 1))
print('Generated research hub, evidence guide and downside calculator; linked eight hubs.')

# Preserve the financial source labels and add interpretation guidance to every deal page.
note = '<!-- case-evidence-context:start --><section><div class="wrap wrap-narrow"><p><strong>Reading these figures:</strong> A number is not a verified full-year operating result unless its source and reporting period establish that. Financial summaries may include forecasts, client reports or illustrations. Tax illustrations are not verified client tax savings. Read the <a href="/guides/reading-str-case-study-results/">case study evidence guide</a> and request the source records relevant to your purchase.</p></div></section><!-- case-evidence-context:end -->'
for target in sorted((ROOT / 'case-studies').glob('*/index.html')):
    source = re.sub(r'<!-- case-evidence-context:start -->.*?<!-- case-evidence-context:end -->', '', target.read_text(), flags=re.S)
    source = source.replace('Year-one tax reduction', 'Illustrative tax reduction')
    target.write_text(source.replace('</main>', note + '\n</main>', 1))
