"""Public-evidence corrections; source tracker fields remain unchanged.

No recomputed percentage is promoted to a client outcome. The source period,
expense coverage and denominator are unresolved. These two pages retain
acquisition facts and explicitly identify the reported-field discrepancies.
"""

REVIEWED = "2026-10-06"
SOURCE = "https://www.bnbaccelerator.com/deals/"


def review_record(record):
    slug = record["slug"]
    if slug not in {"adam-florida-panhandle", "ashley-billy-fort-walton-beach"}:
        return record
    d = record["deals"][0]
    record = dict(record, evidence_reviewed=REVIEWED)
    if slug == "adam-florida-panhandle":
        record.update(
            headline="A $645,000 Florida Panhandle acquisition with an unresolved return basis",
            summary="Adam's Florida Panhandle record lists a $645,000 purchase and $195,769 of entry costs. The public record does not verify a rental return.",
            result="The acquisition record supplies purchase and entry-cost fields. A realized annual return is not established by the public evidence.",
            metrics=[("Recorded purchase price", "$645,000", False),
                     ("Listed entry costs", "$195,769", False),
                     ("Rental return", "Not verified", False)],
            body=[
                "The company-published tracker records a $645,000 Florida Panhandle (30A) purchase for Adam in 2025. It lists $129,000 down, $24,188 in closing costs and $42,581 for design and furnishing. Those fields add to the listed $195,769 entry cost. They do not establish a complete buyer budget including launch carry and retained reserves.",
                "The earlier summary described $19,893 as annual cash flow alongside a 7.93% cash-on-cash figure. That percentage does not reconcile with the displayed $195,769 entry cost. The public summary does not establish the reporting dates, whether income is realized or projected, the complete expense coverage, or which invested-cash denominator produced the percentage. No corrected return is asserted here.",
                'Before relying on performance, obtain dated property-level income and expense records, debt-service statements and the cash-investment ledger for the same period. Use the <a href="/blog/reconcile-airbnb-payout-export/">seller-income reconciliation</a> and <a href="/financing/closing-costs-and-reserves/">buyer-budget checklist</a>. A new buyer also needs their own permission, financing, costs and opening schedule; historical acquisition fields alone cannot verify that forward case.',
            ],
            evidence_note="Return not verified: the previously reported $19,893 cash-flow field and 7.93% percentage do not establish a comparable annual return. Period, actual-versus-projected status, expense coverage and investment denominator remain unresolved.",
            faqs=[
                ("What does Adam's acquisition record show?", "A company-published 2025 Florida Panhandle record with a $645,000 purchase-price field and $195,769 in listed entry costs. These are recorded fields, not independent settlement verification."),
                ("Do the listed entry components add up?", "Yes. $129,000 down plus $24,188 closing plus $42,581 design equals $195,769. That does not prove every acquisition, launch or reserve cost is included."),
                ("What is the verified annual return?", "The public record does not establish one. The earlier cash-flow and percentage fields have unresolved period, expense and denominator definitions; no replacement return is claimed."),
            ],
        )
    else:
        record.update(
            headline="A reported launch of nearly 80 booked nights on a $630,000 Fort Walton Beach purchase",
            summary="Ashley and Billy's story reports a $630,000 purchase and nearly 80 booked nights within 21 days after launch; entry costs remain unreconciled.",
            result="The story reports nearly 80 nights booked within 21 days of going live. Booked nights do not establish completed stays, collected income or an annual return.",
            metrics=[("Recorded purchase price", "$630,000", False),
                     ("Reported booked nights", "~80", False),
                     ("Booking observation period after launch", "21 days", False)],
            hub_metric=("Reported booked nights after launch", "~80 in 21 days", False),
            body=[
                "The company-published story describes a four-bedroom Fort Walton Beach purchase at $630,000 and close to 80 nights booked within 21 days of launch. Keep that as a reported booking milestone. It does not establish completed stays, collected payouts, net profit, the time from closing to opening, or a repeatable launch result.",
                "The associated tracker lists $63,000 down, $1,950 closing and $159,750 design. Those line items sum to $224,700, while its entry-total field says $220,800, a $3,900 difference. The public summary does not show a settlement statement or itemized reconciliation that explains the difference. Both are retained as recorded fields; neither is promoted to a corrected all-in cost.",
                "The earlier tracker summary also displayed a $43,946 annual cash-flow field and 17.52% cash-on-cash percentage. The public record does not establish the period, actual-versus-projected status, expense coverage or investment denominator. They are not presented here as verified returns. No arithmetic replacement resolves missing source definitions.",
                'For a buyer, this is a prompt to reconcile closing figures and plan the launch sequence: possession, repairs, furnishing, photography, permission, coverage and manager readiness. Use the <a href="/blog/str-purchase-to-launch-timeline/">launch-delay budget</a> and <a href="/management/">management handoff register</a>. Future reservations require their own responsibility and payout checks before being counted in the buyer case.',
            ],
            evidence_note="Entry total unreconciled: the listed components sum to $224,700, but the tracker total is $220,800, a $3,900 difference. Return period, expense coverage and denominator are also unresolved. The booking milestone is a reported process fact, not a realized return.",
            faqs=[
                ("What does the launch story report?", "A $630,000 four-bedroom Fort Walton Beach purchase and close to 80 nights booked within 21 days of going live. Booked nights are not proof of stayed nights, receipts or profit."),
                ("What was the total cash invested?", "It is unresolved. Listed down payment, closing and design total $224,700, while the tracker says $220,800. Supporting records are needed to explain the $3,900 difference and any missing costs."),
                ("Is the reported percentage a verified annual return?", "No. The public summary does not establish reporting dates, realized versus projected income, complete expenses or the return denominator. No corrected percentage is claimed."),
            ],
        )
    assert d["price"] == (645000 if slug.startswith("adam") else 630000)
    return record


def acquisition_panel(record, usd):
    d = record["deals"][0]
    entry_label = "Tracker entry total (unreconciled)" if record["slug"].startswith("ashley") else "Listed entry costs"
    rows = [("Recorded purchase price", d["price"]), ("Down payment field", d["down"]),
            ("Closing-cost field", d["closing"]), ("Design/furnishing field", d["design"]),
            (entry_label, d["entry"])]
    items = "\n".join(f'<li><span class="k">{k}</span><span class="v">{usd(v)}</span></li>' for k, v in rows)
    return f'''        <h2 id="deal-numbers">The acquisition record</h2>
        <p>Company-published fields, reviewed October 6, 2026. They are not an independently verified closing statement or a complete buyer budget.</p>
        <ul class="spec-list">{items}</ul>
        <div class="callout"><h3>What remains unresolved</h3><p>{record["evidence_note"]}</p></div>
        <p>Public source: <a href="{SOURCE}">company-published results and tracker summaries</a>. Read the <a href="/guides/reading-str-case-study-results/">case-study evidence guide</a> before comparing outcomes.</p>
'''
