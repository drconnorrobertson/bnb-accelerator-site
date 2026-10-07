"""Scoped acquisition-use revision; IRS sources reviewed October 6, 2026."""
import html
import json
import math
import re
from expand_reservations_closing import ROOT, main

SLUG = 'str-personal-use-days'
FAQS = [
    ('Can I stay at my own short-term rental?', 'Evaluate your actual proposed use before buying. Confirm financing, insurance and local permissions separately, model the dates removed from rental availability, and have a qualified CPA assess personal-use treatment and limitations. There is no universal safe night count that guarantees a deduction.'),
    ('What counts as personal use of a rental property?', 'IRS guidance includes use by owners, specified family members, reciprocal-use arrangements and below-fair-rent stays, with exceptions and definitions. Give your CPA dates, users, amounts paid and fair-rent evidence rather than classifying every family visit the same way.'),
    ('Do work trips to my rental count as personal use?', 'IRS Publication 527 distinguishes substantially full-time repairing and maintaining from improving property. A furnishing or vendor trip is not automatically covered by that exception. Document actual work and mixed-purpose stays for adviser review; personal-use classification does not itself establish material participation.'),
    ('How should personal use change my STR purchase decision?', 'Put desired dates into the buyer forecast before making an offer. Compare after-use cash flow and complete acquisition cash with your requirements, and test whether the purchase remains acceptable without an assumed tax benefit. Resolve adviser questions before releasing available contract protections.')
]
BODY = '''<p class="lead">Personal use days belong in your short-term rental purchase decision, not in a tax-season reconstruction. Before buying, describe the dates your household wants, any family or discounted stays, and the work you expect to perform. Model the property with those plans disclosed. A few nights of use do not automatically preserve rental economics or establish eligibility for a deduction against high W-2 or business income.</p>
<p>My BnB Accelerator, LLC is an acquisition firm, not a CPA firm. AE Tax Advisors is an independent partner firm. <a href="/apply/">Book an STR acquisition call to align your intended use with the property search and buyer budget</a>; obtain personalized tax advice separately.</p>
<h2>Separate the questions your advisers need to answer</h2>
<p><a href="https://www.irs.gov/taxtopics/tc415" rel="noopener">IRS Topic 415</a> explains that personal use can affect rental-expense allocation and deduction limitations. Its definitions include more than the owner's own vacation nights and contain exceptions. Neither a seller's calendar category nor an investor's preferred financing label settles the buyer's tax treatment.</p>
<p>Ask the CPA to distinguish expense allocation, whether the dwelling is treated as a home, and applicable rental-loss limitations. Separately request an assessment of participation and other requirements relevant to your proposed tax position. Meeting one test does not answer all the others. Do not use days offered for rent as a substitute for actual fair-rent rental days.</p>
<p>Tell the lender and insurer the same actual use plan. Confirm address-specific rental permissions independently. The <a href="/blog/second-home-loan-rental-intent/">second-home loan intent guide</a> addresses product eligibility, while the <a href="/blog/normalize-owner-blocks-str/">owner-block inventory worksheet</a> addresses potential release of seller-personal-use dates. This page focuses on your own use and the evidence needed before relying on the purchase.</p>
<h2>Bring a proposed-use register before choosing a property</h2>
<p>Create a planning register before the offer, then replace planned entries with actual records after purchase. Record dates, occupants, purpose, amounts paid, fair-rent support and adviser questions. Keep private household, guest and financial details in a secure channel rather than a public example.</p>
<div class="table-wrap"><table><thead><tr><th>Proposed use</th><th>Evidence to prepare</th><th>Pre-purchase question</th></tr></thead><tbody>
<tr><td>Household vacation</td><td>Desired dates and actual rental alternatives for those periods</td><td>Does the after-use model still justify this property and price?</td></tr>
<tr><td>Family or discounted stay</td><td>Relationship, purpose, rent paid and comparable fair-rent support</td><td>What classification and exceptions apply to these specific facts?</td></tr>
<tr><td>Repair visit</td><td>Specific work, daily time, invoices and contemporaneous records</td><td>Does the actual activity fit the relevant repair/maintenance rule?</td></tr>
<tr><td>Furnishing, improvement or mixed trip</td><td>Separate activity schedule and recreational use</td><td>Which questions remain unresolved rather than automatically treated as repair days?</td></tr>
<tr><td>Changed plans</td><td>Revised dates, guest commitments and use assumptions</td><td>Who must reassess the financing, insurance, economics and tax position?</td></tr>
</tbody></table></div>
<p>The <a href="/blog/str-personal-use-calendar/">personal-use calendar note</a> supports ongoing recordkeeping. A planning worksheet is not evidence that future work happened or that a proposed stay was rented at fair value. Set an actual transaction deadline for important adviser answers with your agent and counsel.</p>
<h2>Do not equate every property work trip with a repair exception</h2>
<p><a href="https://www.irs.gov/publications/p527" rel="noopener">IRS Publication 527 (2025), Chapter 5</a> describes a personal-use exception for days spent working substantially full time repairing and maintaining, explicitly distinguishing that work from improving. It also explains that expense allocation and dwelling-as-home determinations can treat some facts differently. Read the relevant rule with your CPA, not a universal work-trip shortcut.</p>
<p>A receipt for furniture or a meeting with a contractor does not establish the whole day's treatment. Describe the actual work, who performed it and any vacation activity. Preserve contemporaneous documentation; do not relabel a family vacation after the fact. Personal-use classification also does not, by itself, establish qualifying participation hours. Ask the adviser to evaluate each question independently.</p>
<h2>Price the personal-use trade before approving the offer</h2>
<p>Illustrative acquisition arithmetic only: assume a buyer commits $200,000 of total cash and independently models $18,000 annual cash flow after operating costs and debt, before personal use and income taxes. That is 9% of the modeled cash commitment, not a promised return. Suppose desired dates would remove $2,800 of supported accommodation receipts and avoid $700 of modeled variable costs. The net modeled reduction is $2,100, leaving $15,900, or about 8.0% of $200,000 before income taxes.</p>
<p>Do not subtract the full $2,800 and then ignore avoided costs, or treat all fixed bills as avoided. Conversely, do not assume desired dates would have booked at their advertised rate. Replace the example with date-specific evidence and actual costs. If personal use requires extra travel or setup cash, include it separately; it is not automatically a property expense or tax deduction.</p>
<p>Decide whether the after-use economics and household commitment remain acceptable. Test the purchase without an assumed tax benefit using the <a href="/blog/str-tax-benefit-shortfall-purchase/">tax-benefit shortfall guide</a>. Do not fund closing or debt payments with a hoped-for refund. Keep required reserves and household/business liquidity separate from spendable launch cash.</p>
<h2>Resolve suitability before committing capital</h2>
<p>Proceed when truthful use, actual permissions, financing, funded launch and after-use economics fit your requirements. Revise the property search or offer if they do not. Discuss any unresolved answers and available contractual protections with your retained advisers; this checklist does not create extension or cancellation rights. For an eventual exchange or sale, bring personal-use plans to qualified tax and legal advisers before relying on an <a href="/blog/1031-exchange-short-term-rental/">exit strategy</a>.</p>
<p>For <a href="/blog/buy-str-high-income-large-tax-bill/">buyers with substantial deployable capital and a large tax bill</a>, the useful next step is a property purchase that fits actual household plans, not an unsupported promise that off-peak visits preserve nearly all revenue or tax treatment. <a href="/apply/">Book a call to compare acquisition options with your intended-use register</a>. BNB Accelerator assists within its contracted acquisition scope; independent professionals determine their respective advice and approvals.</p>
<p class="small">Primary sources reviewed October 6, 2026. Educational information only, not personalized investment, tax, lending, insurance or legal advice. Worked figures are hypothetical. No permission, deduction, refund, income or return is guaranteed.</p>'''

def rewrite_schema(text, transform):
    def replace(m):
        data=json.loads(m.group(2))
        transform(data)
        return m.group(1)+json.dumps(data,indent=2)+m.group(3)
    return re.sub(r'(<script[^>]*type="application/ld\+json"[^>]*>)(.*?)(</script>)',replace,text,flags=re.S)

if __name__ == '__main__':
    path=ROOT/'blog'/SLUG/'index.html'
    def remove_faq(data):
        if '@graph' in data:
            data['@graph']=[n for n in data['@graph'] if n.get('@type')!='FAQPage']
    path.write_text(rewrite_schema(path.read_text(),remove_faq))
    faq_html='<h2 id="faq">Frequently asked questions</h2>'+''.join('<div class="faq-group"><h3>'+html.escape(q)+'</h3><div class="faq-answer"><p>'+html.escape(a)+'</p></div></div>' for q,a in FAQS)
    body=BODY+faq_html
    main(slug=SLUG,title='STR Personal Use Days: Pre-Purchase Decision Worksheet',
         h1='Personal Use Days and Your Short-Term Rental',
         description='Plan STR personal use before buying: document intended stays, clarify repair trips and test after-use cash flow with qualified tax advice.',body=body,
         search_terms='personal use days repair maintenance family stays acquisition suitability',
         hub_attribute='data-personal-use-review-link',
         hub_block='<p data-personal-use-review-link>Planning to stay at the property yourself? Review the <a href="/blog/str-personal-use-days/">personal-use acquisition worksheet</a> before relying on rental economics or an estimated tax benefit.</p>')
    words=len(re.findall(r'\b\w+\b',html.unescape(re.sub('<[^>]+>',' ',body))))
    def align(data):
        if '@graph' in data:
            for n in data['@graph']:
                if n.get('@type') in ['Article','BlogPosting']: n['wordCount']=words
            if any(n.get('@type') in ['Article','BlogPosting'] for n in data['@graph']):
                data['@graph'].append({'@type':'FAQPage','mainEntity':[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in FAQS]})
    s=rewrite_schema(path.read_text(),align)
    for heading,anchor in [('Separate the questions your advisers need to answer','rules'),('Bring a proposed-use register before choosing a property','practical'),('Price the personal-use trade before approving the offer','cost'),('Resolve suitability before committing capital','honest')]:
        s=s.replace('<h2>'+heading+'</h2>','<h2 id="'+anchor+'">'+heading+'</h2>')
    s=re.sub(r'(<meta property="article:published_time" content=")[^"]+',r'\g<1>2026-08-11',s)
    s=s.replace('<span>Published August 11, 2026</span>','<span>Published August 11, 2026</span><span>&middot;</span><span>Updated October 6, 2026</span>',1) if 'Updated October 6, 2026' not in s else s
    path.write_text(s)
    sitemap=ROOT/'sitemap-blog.xml'
    sm=sitemap.read_text()
    sm,n=re.subn(r'(<loc>https://www.bnbaccelerator.com/blog/'+SLUG+r'/</loc>\s*<lastmod>)[^<]+',r'\g<1>2026-10-06',sm)
    assert n==1
    sitemap.write_text(sm)
    print(f'Four revised visible/schema FAQs; {words} words; {math.ceil(words/220)} minutes; honest dates and sitemap updated')
