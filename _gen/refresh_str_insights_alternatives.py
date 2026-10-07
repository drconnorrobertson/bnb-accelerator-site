"""Scoped comparison refresh; no homepage, shared modules or new URLs."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
p = ROOT / 'compare/alternatives-to-str-insights/index.html'
text = p.read_text()
assert 'reviewed 2026-10-01' in text
text = text.replace('"dateModified": "2026-10-01"', '"dateModified": "2026-10-07"')
text = text.replace('STR Insights publishes a property-deals portal and software, and separately describes a turnkey acquisition path with deal selection, analysis, inspection, negotiation, design and setup. Match your comparison to the tier quoted to you.', 'STR Insights’s current homepage describes one-to-one consulting and property finding; its introduction page separately describes acquisition, setup and operations support. Its navigation also lists software and analysis services. Do not assume one proposal includes all of these paths. Match the exact package to the work you need before comparing alternatives.')
marker = '<section class="section-sm"><div class="wrap wrap-narrow"><h2>Choose before you sign</h2>'
assert text.count(marker) == 1
addition = '''<section class="section-sm"><div class="wrap wrap-narrow"><h2>Compare alternatives by the work left with you</h2>
<p>If you want a consulting relationship, investigate STR Insights’s property-finding package alongside <a href="/compare/str-search/">STR Search</a>. If you already have a market and need representation, investigate <a href="/compare/avery-carl-short-term-shop/">The Short Term Shop</a> and an independent local STR agent. If you need a wider acquisition-and-launch engagement, compare BNB Accelerator’s written scope with the specific STR Insights proposal. These are different buying paths, not interchangeable packages or a claim that one company is best for everyone.</p>
<p>A marketplace route such as <a href="/compare/rabbu/">Rabbu</a> may also belong on your shortlist when browsing properties is your immediate need. A management-oriented route such as <a href="/compare/awning/">Awning</a> belongs in a separate column until you confirm which acquisition duties the actual engagement covers. Use each linked comparison for the provider-specific starting point; ask the provider for current availability and terms.</p>
<div class="bc-docs"><h3>A responsibility register for every proposal</h3><ol>
<li><strong>Candidate accepted:</strong> Name the person delivering the address-level revenue model, comparable-property explanations and expense sources. Record whether you can reject a candidate and what happens to the fee or search engagement when you do.</li>
<li><strong>Offer and diligence:</strong> Identify the licensed agent and the person tracking inspection, insurance, legal-use evidence and lender conditions. Coordination is not a legal opinion, insurance binder or loan approval. Record which specialists are paid separately.</li>
<li><strong>Fee trigger:</strong> Copy the actual amount, due date and trigger—signing, accepted offer, closing, milestone or recurring access—plus cancellation and refund terms. Never substitute another customer’s fee or a free consultation for your quotation.</li>
<li><strong>Opening delivered:</strong> List furnishing procurement versus installation, listing ownership, account access, operator selection and unresolved work. Identify who approves spending above the agreed budget and when support ends.</li>
<li><strong>Decision rights:</strong> Write down who can authorize an offer, repair request, contingency release and vendor payment. Ask your agent or attorney how those rights are expressed in the documents. A marketed done-for-you service does not remove your ownership risk.</li>
</ol></div>
<p>Complete the same register for BNB Accelerator. Where its signed agreement does not assign a task, treat that task as unresolved or buyer-managed—not as automatically included. Keep professional fees, ongoing management and maintenance separate unless the proposal expressly covers them.</p>
</div></section>
<section class="section-sm"><div class="wrap wrap-narrow"><h2>A fee-and-cash worksheet for comparing two proposals</h2>
<p><strong>Hypothetical purchase, not provider pricing or a client result:</strong> A $600,000 property with a lender-approved 75% loan needs $150,000 down. Add $18,000 closing costs, $35,000 furnishing, $12,000 repairs and $30,000 retained reserves: $245,000 before service fees. The financing assumption is illustrative, not a commitment.</p>
<p>Suppose Proposal A quotes $8,000 but leaves $14,000 of separately priced launch work with you. Total required capital is $245,000 + $8,000 + $14,000 = <strong>$267,000</strong>. Proposal B quotes $18,000 and expressly includes that same launch work: $245,000 + $18,000 = <strong>$263,000</strong>. With $260,000 available, both fail the cash gate—A by $7,000 and B by $3,000. A lower headline fee does not establish a cheaper complete purchase.</p>
<p>Do not use these fictional amounts to estimate any named company’s fees. Replace each with a written quote, remove duplicated scope, and confirm whether either fee is already included in closing costs. Separately track money due before closing and charges that survive a failed purchase; a refundable or closing-contingent fee has a different timing risk from an upfront nonrefundable fee. Keep the $30,000 reserve intact unless you explicitly revise the risk plan. A projected tax benefit or future booking revenue is not available closing cash.</p>
<p><a href="/tools/first-str-purchase-budget/">Use the purchase-budget worksheet</a>, then bring the responsibility register to the <a href="/guides/str-insights-service-tiers/">service-tier contract questions</a>. The alternatives page helps choose a buying path; that guide helps examine the proposal after you have selected one.</p>
</div></section>'''
text = text.replace(marker, addition + marker)
text = text.replace('Provider facts summarized from <a href="https://www.strinsights.com/introduction" rel="noopener noreferrer">STR Insights’s public material</a>, reviewed 2026-10-01.', 'Document-based analysis of <a href="https://www.strinsights.com/" rel="noopener noreferrer">STR Insights’s homepage</a> and <a href="https://www.strinsights.com/introduction" rel="noopener noreferrer">introduction page</a>, reviewed 2026-10-07. This is not firsthand testing or a verified customer-experience review; advertised services are not proof of a specific contract’s inclusions or investment results. The named alternatives link to their separate buyer comparisons rather than imply identical services.')
p.write_text(text)
sitemap = ROOT / 'sitemap-core.xml'
st = sitemap.read_text()
pattern = r'(<loc>https://www.bnbaccelerator.com/compare/alternatives-to-str-insights/</loc>\s*<lastmod>)[^<]+(</lastmod>)'
st, count = re.subn(pattern, r'\g<1>2026-10-07\2', st)
assert count == 1
sitemap.write_text(st)
