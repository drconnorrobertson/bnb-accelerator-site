"""Reviewed replacement-first acquisition guide; scoped publication only.

Never calls blog.build or older generators. Preserves every existing archive
card and updates counts from actual cards. No homepage/shared module edits.
"""
import collections
import datetime
import html
import json
import re
from pathlib import Path
import blog

ROOT = Path(__file__).resolve().parent.parent
SLUG = 'reverse-1031-buy-str-before-selling'
DATE = '2026-10-07'
ROUTE = f'/blog/{SLUG}/'
TITLE = 'Reverse 1031: Buy an STR Before Selling Your Property'
DESC = 'Buying an STR before selling an investment property? Compare reverse-exchange setup, lender approval and peak cash with a worked two-property bridge.'
POST = {
 'slug': SLUG, 'title': TITLE, 'title_tag': TITLE,
 'h1': 'Can a reverse 1031 help you buy an STR before selling?',
 'description': DESC, 'date': DATE, 'category': 'Acquisition & Financing',
 'lead': 'Finding the replacement STR before your current investment property sells creates a sequencing problem, not just a tax question. A reverse exchange may offer a professionally structured replacement-first path, but you need acceptable ownership arrangements, financing and enough accessible cash to carry both properties. Do not close in your own name and assume an exchange provider can repair the sequence afterward. Before offering, compare a provider-approved reverse arrangement with selling first, delaying the purchase or buying without an assumed exchange benefit. <a href="/apply/">Discuss the property search and acquisition timetable</a> while your CPA, exchange professionals, lender and counsel evaluate their respective conditions.',
 'sections': [
 ('Resolve the ownership sequence before the STR purchase', [
 'The <a href="https://www.irs.gov/publications/p544">IRS Publication 544 discussion of qualified exchange accommodation arrangements</a> explains that buying replacement property before transferring relinquished property generally is not covered by the ordinary like-kind exchange rules; a qualifying accommodation arrangement may provide a path. An exchange accommodation titleholder, or EAT, holds qualifying ownership interests under the arrangement. The current publication is the 2025 edition, not a newly issued 2026 rule.',
 'The <a href="https://www.irs.gov/pub/irs-drop/rp-04-51.pdf">2004 modification to the reverse-exchange safe harbor</a> excludes replacement property the taxpayer owned within the 180-day period ending when qualifying ownership is transferred to the EAT. Buying personally and later parking the same property is therefore not a safe-harbor shortcut. Have qualified advisers determine the actual structure before purchase. No conclusion about a transaction outside that safe harbor is provided here.',
 'The existing <a href="/blog/1031-exchange-short-term-rental/">sell-first STR exchange guide</a> addresses the deferred sequence. This guide asks whether a replacement-first purchase can be executed and funded before the sale occurs. A large expected gain or attractive listing does not answer that question. Ask your CPA about investment use, ownership consistency, basis, personal use and any recognized gain; do not infer tax eligibility from an STR listing or projected depreciation.',
 'Request a written responsibility map: which professional structures the exchange, which party holds which interest, who borrows or guarantees obligations, who approves conveyance documents and who tracks completion. BNB Accelerator coordinates acquisition work within its agreement; it is not automatically your EAT, qualified intermediary, lender or tax adviser. Keep the exchange plan and the property diligence file connected without handing every vendor private tax records.',
 ]),
 ('Build a dependency calendar, not a generic 180-day promise', [
 'Publication 544 describes a written QEAA agreement within five business days after qualifying ownership transfers to the EAT, identification of relinquished property within 45 days when replacement property is parked, and required transfer/completion conditions within 180 days, including the combined parking period. These are safe-harbor conditions, not a complete implementation checklist. Have the exchange team supply the actual triggering events, identification requirements and dated deadlines.',
 ('table', ['Dependency', 'Evidence before committing', 'Purchase consequence'], [
 ['Exchange structure', 'Written adviser/provider plan and accountable deadline owner', 'Do not rely on later correction of ownership'],
 ['Replacement purchase financing', 'Lender accepts the actual title, borrower, security and transfer structure', 'An ordinary preapproval may not finance this arrangement'],
 ['Current-property sale', 'Sale timetable, required payoffs and credible proceeds schedule', 'An asking price is not released exchange cash'],
 ['STR use and possession', 'Address-specific permissions, insurer response and provider/counsel operating plan', 'Do not launch merely because the EAT acquired title'],
 ['Completion or fallback', 'Provider-reviewed sequence and independently funded downside', 'Missing a sale milestone requires immediate professional review'],
 ]),
 'Work backward from the seller’s requested purchase date. Can the provider establish the necessary arrangement, the lender approve it and the title team prepare documents while the contract still protects your decision? If the answer depends on an unsigned agreement or unapproved loan, mark the dependency unresolved. Do not assume a contract extension, deadline relief or return of earnest money.',
 'Keep rental readiness separate from exchange completion. Ask who may authorize repairs, insure the property, apply for permits, contract with a manager and receive rental payments during the actual holding arrangement. Do not assume a tax safe harbor gives operational permission. The <a href="/blog/str-purchase-to-launch-timeline/">purchase-to-launch timeline</a> identifies the separate opening gates; the <a href="/blog/title-commitment-before-buying-str/">title guide</a> addresses conveyed interests and proposed coverage.',
 ]),
 ('Worked cash bridge: fund the overlap before counting the sale', [
 'Hypothetical arithmetic only, not a lender quote, exchange fee estimate, tax calculation or client result. Assume the professionals have accepted a structure requiring $230,000 of buyer-funded purchase equity and closing outflows, $12,000 of distinct exchange/legal/financing setup costs and $38,000 of permitted launch spending. The buyer wants $40,000 to remain accessible as a reserve. Designated available funds are $360,000. No sale proceeds, tax refund or guest receipts are available initially.',
 'Assume combined net cash outflows from the existing and replacement properties are $8,000 per month during the overlap. This input already includes the example’s actual debt payments, operating receipts and continuing bills; do not add those payments again. The lender/provider must confirm that financing draws and the buyer funds can reach each required payee on time. The loan amount itself is not another unrestricted cash resource.',
 ('table', ['Allocation or scenario', 'Hypothetical amount'], [
 ['Purchase + distinct setup + launch + retained reserve', '$230,000 + $12,000 + $38,000 + $40,000 = $320,000'],
 ['Cash outside that plan before overlap', '$360,000 − $320,000 = $40,000'],
 ['Three-month overlap', '$24,000; total allocation $344,000; $16,000 outside plan'],
 ['Five-month overlap', '$40,000; total allocation $360,000; no outside-plan cash'],
 ['Five months plus $15,000 distinct additional work', '$375,000 allocation; $15,000 funding gap preserving reserve'],
 ]),
 'The $40,000 reserve is retained cash, not an incurred expense or deduction. In the five-month case, the buyer has not spent the reserve, but has exhausted all other modeled flexibility. The later $15,000 work requirement cannot be financed by an expected sale deposit or hoped-for tax outcome. Obtain actual quotes and determine whether the property still qualifies for the intended use; money alone does not resolve a permission problem.',
 'Suppose a sale schedule separately forecasts $260,000 after its specified mortgage payoff and sale costs. That forecast may support a future completion plan only when the exchange professionals reconcile restrictions, debt, transfer costs and permitted uses. Do not add $260,000 to the starting $360,000, describe restricted exchange money as available household cash or assume every dollar reimburses your earlier contribution. This worksheet tests peak pre-sale funding, not post-exchange reusable proceeds.',
 ]),
 ('Compare reverse, sell-first and no-exchange purchase paths', [
 'A reverse arrangement can change which property you secure first; it does not improve that property’s underlying demand, legal use or repairs. Compare all paths using the same independently supported STR income, complete setup scope and buyer risk limits. Obtain provider and lender terms for each path rather than applying an ordinary purchase loan to an ownership structure it has not approved.',
 'Selling first may reduce two-property overlap but creates its own replacement-search timing pressure. Waiting may lose this listing without obligating you to buy an unsuitable substitute. A separate purchase without assumed exchange treatment requires its own funding and adviser-estimated tax provision. None is automatically superior. Have your advisers compare actual tax consequences separately; a cash bridge cannot calculate deferred gain, basis or depreciation.',
 'Stress the relinquished property’s price and sale timing before approving the replacement offer. Identify who must fund additional carry if its buyer’s financing fails. Ask the exchange team about consequences and options before a decisive date passes. The <a href="https://www.irs.gov/pub/irs-drop/rp-00-37.pdf">original revenue procedure</a> states that failing its conditions removes that safe-harbor treatment; it does not supply automatic extensions or determine every outside-safe-harbor outcome. Do not invent a sale probability to make an unfunded plan look acceptable.',
 'Keep professional documents private. The acquisition team can work from a bounded memo: available early cash, provider-approved structure, lender status, sale milestones, property criteria and outstanding decisions. Your adviser’s tax analysis, account information and exchange documents belong in agreed secure channels, not a public application attachment or guest-facing listing.',
 ]),
 ('Make the replacement-first offer an executable decision', [
 'Proceed only when the professionals accept the structure, the lender supports the actual transaction, property diligence clears your standards and pre-sale funding survives your chosen downside. Renegotiate a feasible purchase date or price through approved contract terms when a specific constraint changes the plan. Delay while a decisive arrangement or financing condition remains unresolved under valid protection. Decline a purchase dependent on unsupported exchange treatment or inaccessible sale money.',
 '<a href="/apply/">Book an STR acquisition call with the replacement-property budget and actual sale timetable</a>. Bring a non-sensitive status memo, not confidential tax returns. Search and underwriting should produce a property worth owning independently of the intended exchange. The <a href="/blog/buy-str-high-income-large-tax-bill/">high-income buyer roadmap</a> connects capital, diligence and opening responsibilities without treating a tax benefit as purchase cash.',
 'Primary IRS materials reviewed October 7, 2026. Educational information only, not legal, tax, exchange-structuring, lending, title, insurance or personalized investment advice. Use qualified independent advisers and transaction-specific documents. All example figures are hypothetical. No exchange eligibility, tax deferral, sale, financing, permission, booking or investment result is guaranteed.',
 ]),
 ],
 'faqs': [
 ('Can I buy an STR personally and arrange a reverse exchange later?', 'Do not rely on that sequence. The IRS safe harbor has a prior-ownership limitation. Have exchange and tax professionals approve the structure before the purchase.'),
 ('Does a regular STR mortgage preapproval cover a reverse exchange?', 'Not automatically. The lender must review the actual titleholder, borrower, security, guarantees and transfer plan before the offer depends on that financing.'),
 ('Can expected sale proceeds fund the replacement purchase today?', 'Not before they are available through the approved arrangement. Model early purchase and overlap cash separately from conditional or restricted later proceeds.'),
 ('Does parking the STR mean it can immediately accept guests?', 'No. Confirm possession, operating authority, local permissions, insurance and the actual holding arrangement before committing to guest stays.'),
 ],
 'related': ['<a href="/blog/1031-exchange-short-term-rental/">Compare the sell-first exchange sequence</a>', '<a href="/financing/closing-costs-and-reserves/">Reconcile purchase cash and reserves</a>'],
 'cta_h': 'Plan the replacement purchase before committing',
 'cta_p': 'Connect a source-checked STR shortlist with real financing, sale milestones and pre-sale cash.',
}

def main():
    dest = ROOT / 'blog' / SLUG / 'index.html'
    assert not dest.exists()
    source = blog.render_post(POST)
    article = re.search(r'<article class="article">(.*?)</article>', source, re.S).group(1)
    words = len(html.unescape(re.sub('<[^>]+>', ' ', article)).split())
    minutes = (words + 219) // 220
    source = re.sub(r'\d+ min read', f'{minutes} min read', source)
    def schema(m):
        data = json.loads(m[1])
        if data.get('@type') == 'Article': data['wordCount'] = words
        return '<script type="application/ld+json">' + json.dumps(data, indent=2) + '</script>'
    source = re.sub(r'<script type="application/ld\+json">(.*?)</script>', schema, source, flags=re.S)
    dest.parent.mkdir(); dest.write_text(source)
    archive = ROOT / 'blog/index.html'; s = archive.read_text()
    old = re.findall(r'<article class="post-card".*?</article>', s, re.S)
    assert len(old) == 739 and ROUTE not in s
    search = html.escape((TITLE + ' ' + POST['category'] + ' ' + DESC).lower(), quote=True)
    card = f'<article class="post-card" data-blog-post data-category="{POST["category"]}" data-search="{search}" data-reveal><div class="post-body"><div class="post-meta"><span class="post-cat">{POST["category"]}</span><time datetime="{DATE}">Oct 7, 2026</time><span>{minutes} min read</span></div><h3><a href="{ROUTE}">{TITLE}</a></h3><p>{DESC}</p><a class="post-link" href="{ROUTE}">Read more</a></div></article>'
    s = s.replace('<div class="post-grid" data-blog-grid>', '<div class="post-grid" data-blog-grid>' + card, 1)
    s = s.replace('All topics (739)', 'All topics (740)').replace('Showing all 739 articles', 'Showing all 740 articles')
    cards = re.findall(r'<article class="post-card".*?</article>', s, re.S); assert cards[1:] == old
    cats = collections.Counter(html.unescape(re.search(r'data-category="([^"]+)"', c)[1]) for c in cards)
    months = collections.Counter(re.search(r'<time datetime="(\d{4}-\d{2})', c)[1] for c in cards)
    for cat, count in cats.items():
        esc = re.escape(html.escape(cat, quote=True))
        s = re.sub(r'(<li>' + esc + r' <span class="text-muted">\()\d+(\)</span></li>)', lambda m:m[1]+str(count)+m[2], s)
        s = re.sub(r'(<option value="' + esc + r'">' + esc + r' \()\d+(\)</option>)', lambda m:m[1]+str(count)+m[2], s)
    for month, count in months.items():
        label = datetime.date.fromisoformat(month+'-01').strftime('%B %Y')
        s = re.sub(r'(<li>'+re.escape(label)+r' <span class="text-muted">\()\d+(\)</span></li>)', lambda m:m[1]+str(count)+m[2], s)
    def itemlist(m):
        data = json.loads(m[1]); changed = False
        for n in data.get('@graph', [data]):
            if n.get('@type') == 'ItemList':
                n['itemListElement'] = ([{'@type':'ListItem','position':1,'url':blog.tpl.SITE+ROUTE,'name':POST['h1']}] + n['itemListElement'])[:100]
                for i, item in enumerate(n['itemListElement'], 1): item['position'] = i
                changed = True
        return '<script type="application/ld+json">'+json.dumps(data)+'</script>' if changed else m[0]
    archive.write_text(re.sub(r'<script type="application/ld\+json">(.*?)</script>', itemlist, s, flags=re.S))
    hub = ROOT / 'blog/buy-str-high-income-large-tax-bill/index.html'; s = hub.read_text(); assert ROUTE not in s
    link = f'<p data-reverse-exchange-link>Buying the replacement rental before selling? Test the <a href="{ROUTE}">reverse-exchange setup and two-property cash bridge</a> before relying on future sale proceeds.</p>\n'
    s = s.replace('<div class="author-box">', link+'<div class="author-box">', 1)
    s = s.replace('"dateModified": "2026-10-06"', '"dateModified": "2026-10-07"')
    hub.write_text(s)
    sitemap = ROOT / 'sitemap-blog.xml'; s = sitemap.read_text(); assert ROUTE not in s
    huburl = blog.tpl.SITE+'/blog/buy-str-high-income-large-tax-bill/'
    s = s.replace(f'<loc>{huburl}</loc>\n    <lastmod>2026-10-06</lastmod>', f'<loc>{huburl}</loc>\n    <lastmod>{DATE}</lastmod>')
    entry = f'  <url>\n    <loc>{blog.tpl.SITE}{ROUTE}</loc>\n    <lastmod>{DATE}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.7</priority>\n  </url>\n'
    sitemap.write_text(s.replace('</urlset>', entry+'</urlset>'))
    index = ROOT / 'sitemap/index.html'; s = index.read_text(); assert ROUTE not in s
    needle = '<h2 class="section-heading">Blog <span class="count">739</span></h2>\n      <p class="text-muted">Every article, newest first.</p>\n      <ul class="sitemap-list">'
    assert needle in s
    index.write_text(s.replace(needle, needle.replace('739','740')+f'\n          <li><a href="{ROUTE}">{TITLE}</a></li>', 1).replace('2480 pages in total','2481 pages in total'))
    print(f'{SLUG}: {words} words/{minutes} minutes; 740 archive cards; protected homepage untouched')

if __name__ == '__main__': main()
