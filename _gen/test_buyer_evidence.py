"""Numerical, claims and regeneration gates for the reviewed buyer cohort."""
from decimal import Decimal
from pathlib import Path
import json
import re
import subprocess
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import blog
import case_studies
import pillars
from buyer_evidence import GUIDES, POSTS, REVIEWED

ROOT = Path(__file__).resolve().parents[1]


def source(route):
    return (ROOT / route.strip("/") / "index.html").read_text()


def schemas(markup):
    return [json.loads(item) for item in re.findall(
        r'<script type="application/ld\+json">(.*?)</script>', markup, re.S)]


class BuyerEvidenceTests(unittest.TestCase):
    def test_booking_observation_period_is_not_a_launch_duration(self):
        records = case_studies.records()
        ashley = next(r for r in records if r["slug"] == "ashley-billy-fort-walton-beach")
        for markup in (source("/case-studies/ashley-billy-fort-walton-beach/"),
                       case_studies.render_landing(ashley, records)):
            self.assertNotIn("Reported launch window", markup)
            self.assertIn("Booking observation period after launch", markup)
            self.assertIn("the time from closing to opening", markup)
            self.assertIn("21 days after launch", markup)
        for markup in (source("/case-studies/"), case_studies.render_index(records)):
            card = next(card for card in re.findall(r'<article class="case-card".*?</article>', markup, re.S)
                        if '/case-studies/ashley-billy-fort-walton-beach/' in card)
            self.assertNotIn("Reported launch window", card)
            self.assertIn("Reported booked nights after launch", card)
            self.assertIn("~80 in 21 days", card)

    def test_case_arithmetic_is_an_evidence_gap_not_a_new_return(self):
        cases = {r["slug"]: r for r in case_studies.records()}
        adam = cases["adam-florida-panhandle"]["deals"][0]
        self.assertEqual(adam["down"] + adam["closing"] + adam["design"], adam["entry"])
        self.assertNotAlmostEqual(adam["cash_flow"] / adam["entry"] * 100, adam["coc"], places=1)
        ashley = cases["ashley-billy-fort-walton-beach"]["deals"][0]
        summed = ashley["down"] + ashley["closing"] + ashley["design"]
        self.assertEqual(summed, 224700)
        self.assertEqual(summed - ashley["entry"], 3900)
        for slug in ("adam-florida-panhandle", "ashley-billy-fort-walton-beach"):
            markup = source(f"/case-studies/{slug}/")
            hero = re.search(r'<h1>(.*?)</h1>', markup, re.S).group(1)
            stats = re.search(r'<div class="big-stats">(.*?)</div><p', markup, re.S).group(1)
            self.assertNotRegex(hero, r'\d[\d.]*%|a year')
            self.assertNotIn("cash flow", stats.lower())
            self.assertNotIn("%", stats)
            self.assertNotIn("Illustrative tax reduction", markup)
            article = next(s for s in schemas(markup) if s.get("@type") == "Article")
            self.assertNotRegex(article["headline"] + article["description"], r'\d[\d.]*%|a year in cash flow')
            self.assertEqual(article["dateModified"], REVIEWED)
            self.assertIn("denominator", markup)
        self.assertIn("$224,700", source("/case-studies/ashley-billy-fort-walton-beach/"))
        self.assertIn("$3,900", source("/case-studies/ashley-billy-fort-walton-beach/"))

    def test_reconciliation_example_keeps_periods_separate(self):
        net = 100000 - 8000 - 4000 - 3000
        receipts = net - 2000
        self.assertEqual((net, receipts, receipts + 1500), (85000, 83000, 84500))
        markup = source("/blog/reconcile-airbnb-payout-export/")
        for value in ("$85,000", "$83,000", "$84,500", "prior period"):
            self.assertIn(value, markup)

    def test_budget_and_delay_examples_do_not_spend_reserves_twice(self):
        budget = 600000 * Decimal(".25") + sum((18000, 35000, 8000, 4000, 6000, 18000))
        self.assertEqual(budget, 239000)
        self.assertEqual(budget - 225000, 14000)
        self.assertEqual(budget - 10000 - 225000, 4000)
        for value in ("$239,000", "$14,000", "$229,000", "$4,000"):
            self.assertIn(value, source("/financing/closing-costs-and-reserves/"))
        carry = 2 * 3200
        reserve = 3 * 3200
        self.assertEqual(carry + 5000 + reserve, 21000)
        self.assertEqual(carry + 3200 + 5000 + reserve, 24200)
        for value in ("$21,000", "$24,200", "Operating cushion retained at opening"):
            self.assertIn(value, source("/blog/str-purchase-to-launch-timeline/"))
        self.assertEqual(8 * 800 + 1200, 7600)
        self.assertEqual(12 * 800 + 1200, 10800)
        for value in ("$7,600", "$10,800", "zero STR revenue"):
            self.assertIn(value, source("/blog/permits-that-do-not-transfer/"))

    def test_dscr_can_pass_while_owner_cash_is_negative(self):
        self.assertEqual(Decimal(6000) / 4800, Decimal("1.25"))
        self.assertEqual(6000 - 1800 - 4800 - 300, -900)
        self.assertEqual(1800 + 4800 + 300, 6900)
        markup = source("/financing/dscr-loans/")
        for value in ("1.25", "−$900", "$6,900", "Do not mix the definitions", "Do not subtract property taxes"):
            self.assertIn(value, markup)

    def test_handoff_separates_bookings_cash_and_fee_scope(self):
        self.assertEqual(6000 + 9000, 15000)
        self.assertEqual(60000 * Decimal(".20") + 3000, 60000 * Decimal(".25"))
        markup = source("/management/")
        for value in ("$15,000", "$6,000", "$9,000", "$60,000", "modeled cost is equal"):
            self.assertIn(value, markup)

    def test_legacy_renderers_retain_the_curated_content(self):
        for slug, content in POSTS.items():
            generated = blog.render_post(dict(slug=slug, date="2026-08-15", h1="OLD CLAIM"))
            self.assertIn(content["h1"], generated)
            self.assertNotIn("OLD CLAIM", generated)
            article = next(s for s in schemas(generated) if s.get("@type") == "Article")
            self.assertEqual(article["datePublished"], "2026-08-15")
            self.assertEqual(article["dateModified"], REVIEWED)
        for route, content in GUIDES.items():
            parts = route.strip("/").split("/")
            generated = pillars.guide(
                slug=parts[1] if len(parts) > 1 else "", parent=f"/{parts[0]}/",
                parent_name=parts[0], title="OLD CLAIM", h1="OLD CLAIM", eyebrow="old",
                description="old", lead="old", sections=[], faqs=[], related=[])
            self.assertIn(content["h1"], generated)
            self.assertNotIn("OLD CLAIM", generated)
        cases = case_studies.records()
        for record in cases:
            if record.get("evidence_reviewed"):
                generated = case_studies.render_landing(record, cases)
                self.assertIn(record["headline"], generated)
                self.assertIn("What remains unresolved", generated)

    def test_dates_design_routes_and_funnel_are_preserved(self):
        routes = [f"/blog/{slug}/" for slug in POSTS] + list(GUIDES)
        routes += ["/case-studies/adam-florida-panhandle/", "/case-studies/ashley-billy-fort-walton-beach/", "/case-studies/"]
        for route in routes:
            path = route.strip("/") + "/index.html"
            previous = subprocess.check_output(["git", "show", f"origin/main:{path}"], cwd=ROOT, text=True)
            current = source(route)
            for pattern in (r'<header class="site-header".*?</header>', r'<footer class="site-footer">.*?</footer>'):
                self.assertEqual(re.search(pattern, previous, re.S).group(), re.search(pattern, current, re.S).group())
            self.assertIn('href="/apply/"', current)
            if route != "/case-studies/":
                for key in ("datePublished",):
                    self.assertEqual(re.search(rf'"{key}":\s*"([^"]+)"', previous).group(1), re.search(rf'"{key}":\s*"([^"]+)"', current).group(1))
        self.assertIn("https://mybnbaccelerator.com/schedule-bnb", source("/apply/"))
        self.assertEqual(subprocess.check_output(["git", "diff", "--", "apply/", "assets/", "vercel.json"], cwd=ROOT, text=True), "")
        permit = source("/blog/permits-that-do-not-transfer/")
        self.assertIn("Historical Colorado acquisition records and educational pages", permit)
        self.assertIn("do not establish a current active acquisition service area", permit)


if __name__ == "__main__":
    unittest.main()
