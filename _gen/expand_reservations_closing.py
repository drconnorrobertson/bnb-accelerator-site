"""Refresh one existing closing guide, preserving dates, design and homepage.
Primary Airbnb articles 1431 and 990 checked October 6, 2026. This guide
addresses closing-day obligations/liquidity, not the calendar valuation,
seller listing cutoff or manager selection covered by neighboring pages.
"""
import html
import json
import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'future-reservations-at-closing'
TITLE = 'Future Airbnb Reservations at STR Closing: Buyer Checklist'
H1 = 'What happens to future Airbnb reservations when you buy the property?'
DESCRIPTION = 'Buying an STR with future bookings? Resolve platform limits, guest obligations, payouts and refund exposure with a closing ledger and buyer cash test.'
BODY = '''<p class="lead">Buying the house does not automatically transfer its Airbnb reservations. Before an STR purchase closes, resolve every stay spanning or following closing: who may host it, who owes the guest service, who receives money and who pays if the plan fails. A busy calendar is not buyer-controlled cash. This matters even for a well-funded investor whose purchase budget can absorb a slow launch.</p>
<p><a href="/apply/">Book an STR acquisition call to review the booked-guest handoff before committing to closing</a>.</p>
<h2>Separate ownership of the home from the platform reservation</h2>
<p><a href="https://www.airbnb.com/help/article/1431" rel="noopener">Airbnb's account-transfer guidance</a> says account ownership cannot transfer to a different host and reservations cannot transfer to a new host or account. A trip-change request is not a way to hand reservation management to a new owner. Co-host designation is not reservation transfer. Do not buy account credentials or treat the deed, a broker's promise or a private agreement as an exception to the platform's rules.</p>
<p>Have the seller contact Airbnb about the actual booked stays before either party promises continuity. Ask local counsel, the insurer and the relevant permitting authority whether any proposed arrangement is lawful and covered. The platform determines its permitted procedures; counsel determines transaction obligations. A manager remaining in place does not, by itself, resolve either question.</p>
<p>This page addresses guest duties and buyer liquidity at closing. The <a href="/blog/seller-airbnb-listing-still-live-at-closing/">seller-listing cutoff guide</a> covers preventing new booking collisions; the <a href="/blog/future-booking-calendar-value/">calendar-value guide</a> addresses what verified future receipts might be worth. Neither replaces a stay-by-stay closing plan.</p>
<h2>Build a reservation ledger before releasing purchase protections</h2>
<p>Request dated records from the authorized seller or manager. Use reservation IDs in the acquisition worksheet and share private guest information only through a secure channel, with an appropriate lawful purpose and permissions. Do not publish names or payment details. Reconcile the ledger again immediately before closing because bookings, changes and cancellations can occur after diligence.</p>
<div class="table-wrap"><table><thead><tr><th>Ledger field</th><th>Evidence to attach</th><th>Buyer decision</th></tr></thead><tbody>
<tr><td>Channel, stay dates and possession</td><td>Confirmed reservation record; closing and possession schedule</td><td>Flag every guest arrival or occupied night after the buyer takes possession</td></tr>
<tr><td>Party responsible for the stay</td><td>Platform response and counsel-reviewed written arrangement</td><td>Do not promise hosting until authority, insurance and required permission are established</td></tr>
<tr><td>Gross booking, paid amounts and payout recipient</td><td>Booking record, payout status and seller/manager reconciliation</td><td>Separate seller cash, unpaid amounts and money actually available to the buyer</td></tr>
<tr><td>Cleaning, management and other service costs</td><td>Named provider, accepted assignment and dated cost quote</td><td>Fund costs that fall due before any buyer receipts</td></tr>
<tr><td>Cancellation, refund and tax responsibilities</td><td>Applicable channel terms; written allocation reviewed by advisers</td><td>Identify who owes each obligation and how payment will be evidenced</td></tr>
<tr><td>Resolution status and deadline</td><td>Documented outcome for each stay; named seller contact</td><td>Keep unresolved stays out of the buyer's supported revenue case</td></tr>
</tbody></table></div>
<p>For stays entirely before closing, reconcile any liabilities that could survive the sale rather than assuming none exist. For stays crossing closing, resolve possession and services for each affected date. For later stays, distinguish the seller's existing reservation from any separately permitted new booking. A hoped-for rebooking is not a confirmed buyer reservation, and a guest is not obliged to follow the buyer's desired plan.</p>
<h2>Test service funding before relying on booked revenue</h2>
<p>Illustrative liquidity worksheet only: suppose the buyer has $210,000 of cash designated for the acquisition and launch. Closing, setup and baseline reserves consume $200,000, leaving $10,000 unallocated. A separately verified, lawful and platform-compliant guest-resolution plan requires another $8,000 of near-term services before any related buyer receipts arrive. Unallocated liquidity temporarily falls to $2,000.</p>
<p>Assume the written plan forecasts $12,000 of later receipts legitimately payable to the buyer. If those receipts arrive in full, the modeled incremental contribution is $12,000 minus $8,000, or $4,000, before other expenses, tax and debt. If only $7,000 arrives, it is a $1,000 shortfall. Neither figure pays the early $8,000 bill on its due date. These made-up inputs do not describe an Airbnb reservation transfer, a client transaction, a platform fee or guaranteed payout.</p>
<p>Now suppose advisers identify an additional $1,500 contingent refund exposure allocated to the buyer under the permitted arrangement. Ring-fencing that amount leaves only $500 of the temporary $2,000 liquidity buffer freely available. This reserve is not automatically an incurred expense: if a refund later becomes payable, record the actual outflow once rather than deducting both the reserve and the same refund in the cash-flow result.</p>
<p>Replace every assumption with actual terms and dates. Ask the closing agent and lender whether a proposed settlement adjustment, escrow or seller credit is permissible; none automatically makes platform money transferable or provides unrestricted operating cash. Use the <a href="/blog/how-much-money-to-start-airbnb/">complete STR purchase cash framework</a> and preserve household/business liquidity outside this property's budget.</p>
<h2>Choose a documented closing outcome, not a verbal handoff</h2>
<p><a href="https://www.airbnb.com/help/article/990" rel="noopener">Airbnb's host cancellation policy</a> warns of possible fees and other consequences. It says canceled reservations do not generate a host payout and hosts should not encourage guests to cancel for them. Waiver decisions depend on the circumstances and evidence; do not assume a property sale earns a penalty waiver. Obtain the platform's current answer rather than treating cancellation as cost-free.</p>
<p>Proceed when each affected stay has a documented lawful resolution, the responsible parties accept their duties, and the buyer can fund the timing gap. Renegotiate if a viable purchase requires a lower price or approved adjustment because transition costs or lost receipts are worse than represented. Delay only under valid contractual protection while a specific decisive answer is outstanding. Reject a supposed turnkey purchase that depends on prohibited reservation transfer or unidentified guest obligations.</p>
<p>Ask counsel to address the reservation schedule, changes before closing, seller cooperation, guest communications, payout accounting, expenses, refunds and remedies in transaction-specific documents. Do not use this checklist as a contract clause. If closing shifts, update the entire ledger and provider dates; a previously approved calendar can cease to fit the transaction.</p>
<p>For <a href="/blog/buy-str-high-income-large-tax-bill/">high-income buyers with substantial deployable capital</a>, the next step is an evidence-backed offer and opening-cash plan, not assuming booked stays support a tax result. <a href="/apply/">Book a call to compare this STR's documented reservation handoff with a clean-launch acquisition</a>. BNB Accelerator assists within its contracted acquisition scope; independent advisers and the platform determine their respective approvals.</p>
<p class="small">Primary sources reviewed October 6, 2026. Educational information only, not legal, tax, insurance, lending or personalized investment advice. Worked figures are hypothetical. No permit, booking, payout, tax benefit or return is guaranteed.</p>'''

def main():
    path = ROOT / 'blog' / SLUG / 'index.html'
    s = path.read_text()
    published = re.search(r'"datePublished":\s*"([^"]+)"', s).group(1)
    author = re.search(r'<div class="author-box">.*?</div>\s*</div>', s, re.S).group()
    s = re.sub(r'(<article class="article">).*?</article>', lambda m: m.group(1)+'\n'+BODY+'\n'+author+'\n</article>', s, count=1, flags=re.S)
    s = re.sub(r'<title>.*?</title>', '<title>'+TITLE+'</title>', s, count=1)
    s = re.sub(r'<h1>.*?</h1>', '<h1>'+html.escape(H1)+'</h1>', s, count=1)
    for name, value in [('description', DESCRIPTION), ('og:description', DESCRIPTION), ('twitter:description', DESCRIPTION), ('og:title', TITLE), ('twitter:title', TITLE)]:
        s = re.sub(r'(<meta (?:name|property)="'+name+r'" content=")[^"]*(")', lambda m: m.group(1)+html.escape(value, quote=True)+m.group(2), s)
    def schema(m):
        data = json.loads(m.group(2))
        def walk(n):
            if isinstance(n, dict):
                if n.get('@type') in ['Article', 'BlogPosting']:
                    n.update(headline=H1, description=DESCRIPTION, dateModified='2026-10-06')
                if n.get('@type') == 'FAQPage':
                    raise AssertionError('Old FAQ needs manual content review')
                for value in n.values(): walk(value)
            elif isinstance(n, list):
                for value in n: walk(value)
        walk(data)
        return m.group(1)+json.dumps(data, indent=2)+m.group(3)
    s = re.sub(r'(<script[^>]*type="application/ld\+json"[^>]*>)(.*?)(</script>)', schema, s, flags=re.S)
    words = len(re.findall(r'\b\w+\b', html.unescape(re.sub('<[^>]+>', ' ', BODY))))
    minutes = math.ceil(words/220)
    s = re.sub(r'<span>\d+ min read</span>', f'<span>{minutes} min read</span>', s, count=1)
    assert re.search(r'"datePublished":\s*"([^"]+)"', s).group(1) == published
    path.write_text(s)
    archive = ROOT / 'blog/index.html'
    matches = 0
    def card(m):
        nonlocal matches
        c = m.group()
        if '/blog/'+SLUG+'/' not in c: return c
        matches += 1
        c = re.sub(r'(<h3><a[^>]*>).*?(</a></h3>)', lambda z: z.group(1)+html.escape(H1)+z.group(2), c, flags=re.S)
        c = re.sub(r'<p>.*?</p>', '<p>'+DESCRIPTION+'</p>', c, count=1, flags=re.S)
        c = re.sub(r'data-search="[^"]*"', 'data-search="'+html.escape((H1+' '+DESCRIPTION+' reservation handoff closing cash').lower(), quote=True)+'"', c)
        return re.sub(r'<span>\d+ min read</span>', f'<span>{minutes} min read</span>', c)
    a = re.sub(r'<article class="post-card".*?</article>', card, archive.read_text(), flags=re.S)
    assert matches == 1
    archive.write_text(a)
    hub = ROOT / 'blog/buy-str-high-income-large-tax-bill/index.html'
    h = hub.read_text()
    block = '<p data-reservation-transition-link>Buying an operating property with guests already booked? Use the <a href="/blog/future-reservations-at-closing/">reservation closing ledger and liquidity test</a> to resolve guest duties, payout ownership and costs due before receipts arrive.</p>'
    h = re.sub(r'<p data-reservation-transition-link>.*?</p>', '', h, flags=re.S)
    h = h.replace('<div class="author-box">', block+'\n<div class="author-box">', 1)
    assert block in h
    hub.write_text(h)
    print(f'Scoped refresh: {words} words, {minutes} min; original publication {published}; homepage untouched')

if __name__ == '__main__':
    main()
