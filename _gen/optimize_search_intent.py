#!/usr/bin/env python3
"""Apply focused search-intent updates after other page generators. Idempotent."""
from pathlib import Path
import re, json, html
ROOT=Path(__file__).resolve().parents[1]
CONFIG={
'index.html':('Short-Term Rental Acquisition | BNB Accelerator','Buy a short-term rental with BNB Accelerator. Explore property sourcing, underwriting, acquisition support, client examples and purchase planning resources.',None),
'done-for-you-airbnb/index.html':('Done-for-You Airbnb Investment Service | BNB Accelerator','Explore BNB Accelerator’s done-for-you Airbnb acquisition service: sourcing, underwriting, purchase coordination and launch planning. Review scope and costs.','Done-for-you Airbnb investment and acquisition service'),
'airbnb-investment-company/index.html':('Airbnb Investment Company & Services | BNB Accelerator','Compare Airbnb investment services with BNB Accelerator’s acquisition model. Review ownership, sourcing, underwriting, service fees and buyer responsibilities.','Airbnb investment services for short-term rental buyers'),
'how-it-works/index.html':('Short-Term Rental Acquisition Process | BNB Accelerator','See how BNB Accelerator coordinates short-term rental sourcing, underwriting, due diligence, closing and launch. Understand your role before buying a property.',None),
'pricing/index.html':('BNB Accelerator Cost & Pricing: Fees and Property Budget','Understand BNB Accelerator costs: service fees, property entry cash and operating reserves. Get the scope, payment terms and excluded vendor costs in writing.',None),
'testimonials/index.html':('BNB Accelerator Testimonials & Client Stories','Read BNB Accelerator client testimonials and property stories, then review the separate source-linked directory of public Trustpilot feedback, including criticism.','BNB Accelerator client testimonials and stories'),
'reviews/index.html':('BNB Accelerator Reviews: Public Trustpilot Feedback','Read BNB Accelerator’s source-linked directory of public Trustpilot reviews, including positive, mixed and critical feedback. Check the date and original sources.',None),
'buy-a-short-term-rental/index.html':('How to Buy a Short-Term Rental | BNB Accelerator','Use BNB Accelerator’s short-term rental buyer workbook to plan your budget, screen properties, verify revenue, complete due diligence and prepare the launch.',None),
'tax-strategy/index.html':('Short-Term Rental Tax Loophole & Rules | BNB Accelerator','Understand the short-term rental tax strategy, participation requirements and cost segregation considerations. Review the limits and discuss your facts with a CPA.','Short-term rental tax loophole: requirements and limits'),
}
BLOCKS={
'index.html':'''<h2>Choose the support for your short-term rental purchase</h2><p>Start with the <a href="/buy-a-short-term-rental/">short-term rental buyer workbook</a> if you are planning the acquisition yourself. If you want coordinated sourcing and purchase support, review our <a href="/done-for-you-airbnb/">done-for-you Airbnb investment service</a> and <a href="/how-it-works/">acquisition process</a>. Before choosing a provider, compare <a href="/pricing/">service fees and the full property budget</a>, <a href="/reviews/">public BNB Accelerator reviews</a> and <a href="/case-studies/">property-specific client examples</a>.</p>''',
'airbnb-investment-company/index.html':'''<h2>Compare Airbnb investment services before choosing a company</h2><p>An acquisition service helps you evaluate and buy a property that you own. A property manager operates the rental under a separate agreement; a course teaches skills; a fund offers exposure under its own ownership structure. Ask who owns the property, who receives each fee and who is responsible after closing.</p><p>Review our <a href="/done-for-you-airbnb/">done-for-you acquisition scope</a>, <a href="/pricing/">cost and pricing questions</a>, <a href="/management/">property management options</a> and <a href="/compare/">provider comparisons</a>. Request an itemized engagement proposal rather than assuming that every activity is included.</p>''',
'pricing/index.html':'''<h2>Is there a published BNB Accelerator service fee?</h2><p>There is no fixed public fee on this site. Request a current written quote for your scope; a property purchase price or client entry budget is not the service price. Ask whether furnishing, photography, permits, management and professional adviser charges are paid separately.</p><p>Use the <a href="/buy-a-short-term-rental/acquisition-budget-worksheet/">acquisition budget worksheet</a> to separate the engagement fee from property cash requirements. Check the <a href="/done-for-you-airbnb/">service responsibilities</a> and <a href="/reviews/">public reviews</a> before committing.</p>''',
'reviews/index.html':'''<h2>How to evaluate BNB Accelerator reviews</h2><p>Read the original source and its date, including critical feedback. Separate a comment about communication from a documented property outcome, and ask whether a financial figure is projected or realized. Review selection, observation periods and property differences limit what one client story can tell you.</p><p>Compare these public posts with <a href="/testimonials/">direct client testimonials</a>, <a href="/case-studies/">documented case studies</a> and <a href="/pricing/">the service fee and scope questions</a>. Request references and a written proposal for your own purchase. A review does not guarantee a return.</p>''',
'buy-a-short-term-rental/index.html':'''<h2>Need help with short-term rental acquisition?</h2><p>If you want help sourcing and coordinating a purchase, compare the <a href="/done-for-you-airbnb/">done-for-you Airbnb acquisition service</a> with completing this workbook yourself. Review the <a href="/how-it-works/">purchase process and buyer responsibilities</a>, <a href="/pricing/">service fee and entry budget</a>, and <a href="/reviews/">public reviews</a> before selecting a provider.</p>''',
}
for file,(title,desc,h1) in CONFIG.items():
 p=ROOT/file;s=p.read_text()
 s=re.sub(r'<title>.*?</title>','<title>'+html.escape(title)+'</title>',s,count=1,flags=re.S)
 for attr,key,value in [('name','description',desc),('property','og:title',title),('property','og:description',desc),('name','twitter:title',title),('name','twitter:description',desc)]:
  tag=f'<meta {attr}="{key}" content="{html.escape(value,quote=True)}">'
  pattern=rf'<meta {attr}="{key}" content="[^"]*"\s*/?>'
  if re.search(pattern,s):s=re.sub(pattern,lambda _:tag,s,count=1)
  else:s=s.replace('</head>',tag+'\n</head>',1)
 if h1:s=re.sub(r'<h1[^>]*>.*?</h1>','<h1>'+html.escape(h1)+'</h1>',s,count=1,flags=re.S)
 # Keep page-level structured metadata consistent with rendered metadata.
 def schema(match):
  data=json.loads(match.group(1))
  nodes=data.get('@graph',[data])
  for node in nodes:
   if node.get('@type')=='WebPage':node.update(name=h1 or title,description=desc)
  return '<script type="application/ld+json">'+json.dumps(data,ensure_ascii=False)+'</script>'
 s=re.sub(r'<script type="application/ld\+json">(.*?)</script>',schema,s,flags=re.S)
 if file in BLOCKS:
  block='<!-- search-intent:start --><section><div class="wrap wrap-narrow">'+BLOCKS[file]+'</div></section><!-- search-intent:end -->'
  s=re.sub(r'<!-- search-intent:start -->.*?<!-- search-intent:end -->','',s,flags=re.S)
  s=s.replace('</main>',block+'\n</main>',1)
 p.write_text(s)
# Replace the thin service page with concrete scope and decision support.
p=ROOT/'done-for-you-airbnb/index.html';s=p.read_text()
start=s.index('<section>',s.index('<h1>'));end=s.index('</main>')
body='''<section><div class="wrap wrap-narrow">
<h2>What the done-for-you Airbnb service includes</h2>
<p>BNB Accelerator coordinates short-term rental acquisition: market research, property sourcing, underwriting, purchase milestones and launch planning. You own the property and approve the decisions. Independent lenders, agents, attorneys, designers, property managers and tax advisers handle their contracted work. Confirm each party’s responsibilities in your written proposal.</p>
<h2>From property search to launch</h2>
<ol><li><strong>Define the purchase.</strong> Set your available capital, preferred markets, timeline and operating responsibilities.</li><li><strong>Source and underwrite.</strong> Review candidate properties against comparable revenue, seasonal demand, expenses, financing and a downside case.</li><li><strong>Verify before committing.</strong> Check permits, zoning, HOA restrictions, condition, insurance and financing with the appropriate professionals.</li><li><strong>Coordinate closing and setup.</strong> Track purchase milestones, furnishing requirements, photography and vendor handoffs.</li><li><strong>Prepare operations.</strong> Agree with your selected manager on pricing, guest support, cleaning, reporting and maintenance.</li></ol>
<p>Explore the <a href="/how-it-works/">full acquisition process</a>, <a href="/markets/">market research</a> and <a href="/underwriting/">underwriting resources</a>.</p>
<h2>What you remain responsible for</h2>
<p>You provide capital, review the assumptions, approve offers and vendor agreements, and make the final purchase decision. Ownership also requires reserves, oversight and an operating plan. Hiring a manager does not remove every owner responsibility or establish eligibility for a tax deduction. Review <a href="/management/">management options</a> and discuss tax eligibility with your own CPA.</p>
<h2>How much does done-for-you Airbnb investing cost?</h2>
<p>The service fee is separate from the property purchase, down payment, closing costs, repairs, furnishings and operating reserves. BNB Accelerator does not publish a fixed service fee. Request an itemized quote, payment schedule, cancellation terms and a list of excluded vendor costs. Use the <a href="/pricing/">BNB Accelerator cost and pricing guide</a> and <a href="/buy-a-short-term-rental/acquisition-budget-worksheet/">acquisition budget worksheet</a>.</p>
<h2>Acquisition support, coaching and property management</h2>
<p>Acquisition support coordinates a purchase. Coaching teaches you to do the work. Management handles rental operations under a separate agreement. Compare the actual deliverables and financial relationships before choosing a provider. Review <a href="/compare/">service comparisons</a> and our <a href="/airbnb-investment-company/">Airbnb investment company overview</a>.</p>
<h2>Review evidence before you apply</h2>
<p>Read <a href="/reviews/">public BNB Accelerator reviews</a>, <a href="/testimonials/">client testimonials</a> and <a href="/case-studies/">documented property examples</a>. Past results vary and do not promise your outcome. Ask for references and a property-specific analysis that identifies assumptions, costs and risks.</p>
<h2>Discuss your acquisition plan</h2>
<p>Bring your budget, timeline, target markets and open questions to a strategy call. Ask which work is included and which decisions you retain.</p><p><a class="btn btn-primary" href="/apply/">Discuss your property purchase</a> <a href="/buy-a-short-term-rental/">Start with the buyer workbook</a></p>
</div></section>
'''
s=s[:start]+body+s[end:];p.write_text(s)
print('Optimized',len(CONFIG),'pages')
