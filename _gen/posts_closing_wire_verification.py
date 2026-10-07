"""Reviewed new intent: STR closing-payment authenticity, score 24/30/14/17/9=94.

Five neighboring bodies reviewed; official CFPB/FBI sources checked Oct6.
Only renders the new article, never rebuilds the archive or homepage.
Scoped archive/count/schema, hub and sitemap updates preserve existing cards.
"""
import collections
import datetime
import html
import json
import re
from pathlib import Path
import blog

ROOT = Path(__file__).resolve().parent.parent
SLUG = "verify-closing-wire-before-buying-str"
DATE = "2026-10-06"
ROUTE = f"/blog/{SLUG}/"
TITLE = "Verify Closing Wire Instructions Before Buying an STR"
DESC = "Buying an STR remotely? Verify closing wire instructions, reconcile cash and confirm receipt before funding. Use a private checklist and loss stress test."
POST = {
    "slug": SLUG, "title": TITLE, "title_tag": TITLE,
    "h1": "How do you verify closing wire instructions before buying an STR?",
    "description": DESC, "date": DATE, "category": "Buying Strategy",
    "lead": "Before sending an STR closing payment, independently establish who is authorized to receive it, reconcile the actual amount and confirm the instructions through a trusted settlement contact. Then obtain the receiving team's confirmation through its approved process. A convincing email, a bank debit and a signed deed answer different questions. For a remote investor, this payment gate belongs in the acquisition calendar before a funding deadline creates pressure. It does not replace the lender's asset review, legal signing authority or title diligence. <a href=\"/apply/\">Discuss your STR acquisition timeline and unresolved funding conditions</a> without sharing account credentials or payment instructions in a public inquiry.",
    "sections": [
        ("Establish the closing contact before payment instructions arrive", [
            "The <a href=\"https://www.consumerfinance.gov/archive/blog/mortgage-closing-scams-how-protect-yourself-and-your-closing-funds/\">CFPB's closing-scam guidance</a> recommends establishing trusted representatives and previously agreed phone contacts, verifying instructions independently and avoiding contact details supplied in a suspicious message. Its article was published in 2019; the historical fraud statistics are not current estimates. The <a href=\"https://www.fbi.gov/how-we-can-help-you/common-frauds-and-scams/business-email-compromise\">FBI's business email compromise guidance</a> specifically identifies fraudulent homebuyer down-payment messages and explains that compromised correspondence can look legitimate. It recommends independently verifying payment changes and enabling multifactor authentication.",
            "For this purchase, identify the actual settlement firm, responsible professional and bank relationship early. Ask what approved verification and secure document channels it uses. Clarify the buyer's role and the authorized sending account; the acquisition coordinator should not improvise payment routing or collect bank passwords. Put the verified contact record in a restricted transaction file, separate from marketing emails and the manager's operational handoff.",
            "Resolve substantive funding conditions in parallel. The <a href=\"/blog/business-funds-str-down-payment/\">business-funds guide</a> addresses authority and acceptable source records. The <a href=\"/blog/power-of-attorney-buy-str/\">delegated-signing guide</a> addresses the actual signer. Neither an accepted source nor an approved signer authenticates a new recipient account. Read the <a href=\"/blog/title-commitment-before-buying-str/\">title commitment</a> separately; no title-insurance coverage for diverted funds is asserted here.",
        ]),
        ("Use a private verification record for this STR closing wire", [
            "Make a transaction-specific record instead of a public spreadsheet containing full account numbers. Store only the status, responsible reviewer, time and secure evidence reference in the acquisition checklist. The payment particulars belong in the bank and settlement team's approved channels. A checkmark records a completed process; it is not a warranty that fraud is impossible.",
            ("table", ["Gate", "Record privately", "Do not confuse it with"], [
                ["Trusted recipient", "Settlement contact independently established before the request", "A familiar display name or forwarded contact"],
                ["Amount", "Approved settlement amount and prior deposit credit reconciled", "A seller's informal balance calculation"],
                ["Instructions", "Recipient and account details confirmed through the approved independent process", "An emailed change or incoming caller's assurance"],
                ["Timing", "Sending bank and settlement deadlines/requirements confirmed", "A universal cutoff or assumed same-day clearance"],
                ["Receipt", "Receiving settlement team confirms the credited payment", "Only the sending account's debit or receipt"],
            ]),
            "Use the current settlement figures, not the original search-budget estimate. List paid deposits and credits once, reconcile the remaining payment and confirm any material change with the responsible professionals. Keep furnishing deposits, launch spending and retained reserves outside that closing total unless the actual statement includes them. The <a href=\"/financing/closing-costs-and-reserves/\">all-in buyer budget</a> provides the separate cash buckets; this guide concerns authentic delivery of the approved payment.",
            "If the instructions, payee or amount changes, pause the affected payment until the independent review is complete. Ask the actual bank and settlement team about limits, approvals and deadlines early enough to choose a feasible funding date. Do not move to a different account or payment method just because a message claims the old route is unavailable. An urgent closing date is not verification evidence.",
        ]),
        ("Stress-test diverted cash without assuming recovery", [
            "Hypothetical planning example only, not a client loss, fraud probability or instruction to fund twice. Assume $275,000 of designated cleared buyer cash, a separately reconciled $180,000 remaining closing payment, $45,000 of launch spending and $30,000 of cash intended to remain as a reserve. The closing amount already reflects any credited deposit; no additional deposit deduction is made. These are invented inputs, not recommended capital or reserve levels.",
            ("table", ["Cash question", "Illustrative amount"], [
                ["Starting accessible cash", "$275,000"],
                ["Legitimate closing + launch + retained reserve allocation", "$180,000 + $45,000 + $30,000 = $255,000"],
                ["Outside-plan cash if payment is legitimately credited", "$20,000"],
                ["Accessible balance if $180,000 is diverted and unavailable", "$95,000"],
                ["Unfunded amount to replace closing and preserve the same launch/reserve plan", "$255,000 − $95,000 = $160,000"],
            ]),
            "The $180,000 wrong payment does not satisfy the legitimate settlement balance. A recall request is not returned cash. Expected insurance proceeds, legal recovery, first guest payouts or a future tax refund do not eliminate the $160,000 funding gap. Do not manufacture an expected-value calculation with an invented recovery probability. Even a buyer able to supply more cash must resolve the compromised process before considering any further transfer.",
            "The reserve is money retained, not another incurred expense or tax deduction. Consuming it changes the buyer's downside protection; it does not repair the payment failure. Obtain advice about actual obligations, remaining purchase protections and any feasible timing change. A blog example cannot determine liability, cancellation rights, insurance coverage or whether a seller must extend closing. The <a href=\"/blog/earnest-money-release-str/\">deposit-release guide</a> handles a different risk: authorized early disbursement and recovery under amended terms.",
        ]),
        ("If a transfer looks wrong, escalate before another payment", [
            "Contact your financial institution immediately through a trusted channel. The CFPB recommends asking for a wire recall; the FBI recommends asking your institution to contact the receiving institution and reporting business email compromise at <a href=\"https://www.ic3.gov/\">IC3</a>. Prompt reporting does not guarantee recovery. Notify the legitimate settlement professional through the established channel and preserve records securely for the bank, investigators and qualified counsel.",
            "Record what happened, when, the instruction version and the bank's case reference. Follow the responsible professionals' incident process; do not publish private account or identity details in a review, shared deal memo or application form. Avoid retaliatory contact or unverified offers to recover money. Ask counsel and the transaction team what can lawfully happen to the closing calendar while the actual funding and document status are unresolved.",
            "A sending confirmation is one evidence item. Confirm recipient credit and then obtain the settlement team's actual closing status, recording and possession information as applicable. Do not tell the manager to admit guests merely because a payment left your bank. Property possession, lawful STR permission, insurance and rental readiness remain separate gates in the <a href=\"/blog/str-purchase-to-launch-timeline/\">purchase-to-launch plan</a>.",
        ]),
        ("Make the funding gate part of an executable acquisition", [
            "Proceed with the payment only after the actual professionals' verification process and funding conditions are satisfied. Seek a documented timing alternative when unresolved instructions or bank requirements make the proposed deadline infeasible; do not assume an automatic extension. Decline a request that requires bypassing verification, hiding the payor or sharing credentials. Keep the property's legal use and conservative economics under review regardless of how smoothly payment preparation proceeds.",
            "Bring the acquisition team a non-sensitive status memo: confirmed funding source, settlement contact established, amount reconciled, outstanding conditions, provider deadlines and launch cash protected. <a href=\"/apply/\">Book an STR acquisition call to coordinate the search, diligence and achievable closing timetable</a>. BNB Accelerator can coordinate within its contracted scope; it is not automatically the settlement agent, receiving bank, funds custodian, fraud investigator or legal adviser.",
            "Primary guidance reviewed October 6, 2026. Educational information only, not personalized banking, security, legal, lending, insurance, tax or investment advice. Follow actual bank and settlement requirements and use independent qualified professionals. Figures are hypothetical. No fraud prevention, recall, recovery, closing, permission, tax benefit, bookings or investment result is guaranteed.",
        ]),
    ],
    "faqs": [
        ("Does lender approval verify the closing wire recipient?", "No. Asset acceptance and payment authenticity are different checks. Complete the bank and settlement team's independent verification process for the actual recipient."),
        ("What should I do when closing wire instructions change?", "Pause the affected payment and independently confirm the change through an established trusted channel. Do not use the new message's contact details as verification."),
        ("Does a bank debit mean my STR purchase has closed?", "No. Obtain the legitimate settlement team's receipt and actual closing status. Recording, possession and lawful rental readiness require their own evidence."),
        ("Can an expected wire recall replace missing purchase funds?", "Do not count expected recovery as available cash. Report the incident immediately and have the bank, settlement team and counsel address actual funds and next steps."),
    ],
    "related": [
        '<a href="/financing/closing-costs-and-reserves/">Reconcile all-in acquisition cash</a>',
        '<a href="/blog/title-commitment-before-buying-str/">Review title separately</a>',
        '<a href="/blog/str-purchase-to-launch-timeline/">Coordinate funding and rental readiness</a>',
    ],
    "cta_h": "Make your STR closing timetable executable",
    "cta_p": "Coordinate documented funds, independent closing professionals and a launch plan that fits the purchase.",
}


def main():
    destination = ROOT / "blog" / SLUG / "index.html"
    assert not destination.exists(), "New-page helper refuses to replace an existing article"
    source = blog.render_post(POST)
    article = re.search(r'<article class="article">(.*?)</article>', source, re.S).group(1)
    words = len(html.unescape(re.sub(r'<[^>]+>', ' ', article)).split())
    minutes = max(1, (words + 219) // 220)
    source = re.sub(r'\d+ min read', f'{minutes} min read', source)
    def schema(match):
        data = json.loads(match.group(1))
        if data.get("@type") == "Article": data["wordCount"] = words
        return '<script type="application/ld+json">' + json.dumps(data, indent=2) + '</script>'
    source = re.sub(r'<script type="application/ld\+json">(.*?)</script>', schema, source, flags=re.S)
    destination.parent.mkdir()
    destination.write_text(source)

    archive = ROOT / "blog/index.html"
    current = archive.read_text()
    original_cards = re.findall(r'<article class="post-card".*?</article>', current, re.S)
    assert len(original_cards) == 738 and ROUTE not in current
    search = html.escape((TITLE + " Buying Strategy " + DESC).lower(), quote=True)
    card = f'<article class="post-card" data-blog-post data-category="Buying Strategy" data-search="{search}" data-reveal><div class="post-body"><div class="post-meta"><span class="post-cat">Buying Strategy</span><time datetime="{DATE}">Oct 6, 2026</time><span>{minutes} min read</span></div><h3><a href="{ROUTE}">{TITLE}</a></h3><p>{DESC}</p><a class="post-link" href="{ROUTE}">Read more</a></div></article>'
    current = current.replace('<div class="post-grid" data-blog-grid>', '<div class="post-grid" data-blog-grid>' + card, 1)
    current = current.replace('All topics (738)', 'All topics (739)').replace('Showing all 738 articles', 'Showing all 739 articles')
    cards = re.findall(r'<article class="post-card".*?</article>', current, re.S)
    assert cards[1:] == original_cards
    cats = collections.Counter(html.unescape(re.search(r'data-category="([^"]+)"', c).group(1)) for c in cards)
    months = collections.Counter(re.search(r'<time datetime="(\d{4}-\d{2})', c).group(1) for c in cards)
    for category, count in cats.items():
        escaped = re.escape(html.escape(category, quote=True))
        current = re.sub(r'(<li>' + escaped + r' <span class="text-muted">\()\d+(\)</span></li>)', lambda m:m[1]+str(count)+m[2], current)
        current = re.sub(r'(<option value="' + escaped + r'">' + escaped + r' \()\d+(\)</option>)', lambda m:m[1]+str(count)+m[2], current)
    for month, count in months.items():
        label = datetime.date.fromisoformat(month + '-01').strftime('%B %Y')
        current = re.sub(r'(<li>' + re.escape(label) + r' <span class="text-muted">\()\d+(\)</span></li>)', lambda m:m[1]+str(count)+m[2], current)
    def archive_schema(match):
        data = json.loads(match.group(1)); changed = False
        for node in data.get('@graph', [data]):
            if node.get('@type') == 'ItemList':
                items = [{'@type':'ListItem','position':1,'url':blog.tpl.SITE+ROUTE,'name':POST['h1']}] + node['itemListElement']
                node['itemListElement'] = items[:100]
                for i, item in enumerate(node['itemListElement'], 1): item['position'] = i
                changed = True
        return '<script type="application/ld+json">' + json.dumps(data) + '</script>' if changed else match[0]
    current = re.sub(r'<script type="application/ld\+json">(.*?)</script>', archive_schema, current, flags=re.S)
    archive.write_text(current)

    hub = ROOT / 'blog/buy-str-high-income-large-tax-bill/index.html'
    s = hub.read_text(); assert ROUTE not in s
    link = f'<p data-closing-wire-link>Before sending purchase cash, use the <a href="{ROUTE}">closing wire verification record and funding stress test</a>. An approved budget is not proof that payment instructions are authentic.</p>\n'
    hub.write_text(s.replace('<div class="author-box">', link + '<div class="author-box">', 1))
    sitemap = ROOT / 'sitemap-blog.xml'; s = sitemap.read_text(); assert ROUTE not in s
    entry = f'  <url>\n    <loc>{blog.tpl.SITE}{ROUTE}</loc>\n    <lastmod>{DATE}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.7</priority>\n  </url>\n'
    sitemap.write_text(s.replace('</urlset>', entry + '</urlset>'))
    site_index = ROOT / 'sitemap/index.html'; s = site_index.read_text(); assert ROUTE not in s
    needle = '<h2 class="section-heading">Blog <span class="count">738</span></h2>\n      <p class="text-muted">Every article, newest first.</p>\n      <ul class="sitemap-list">'
    assert needle in s
    s = s.replace(needle, needle.replace('738', '739') + '\n' + f'          <li><a href="{ROUTE}">{TITLE}</a></li>', 1)
    s = s.replace('2479 pages in total', '2480 pages in total')
    site_index.write_text(s)
    print(f'New article: {words} words/{minutes} minutes; 739 preserved-plus-one archive cards; homepage untouched')


if __name__ == '__main__': main()
