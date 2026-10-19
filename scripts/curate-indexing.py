"""Curate search discovery without deleting the public screening archive."""
import collections
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from html import escape
from build_tracker_proformas import load, slug, SITE
from build_proformas import validate

OUT = Path(sys.argv[1] if len(sys.argv) > 1 else 'public').resolve()
records, _ = load()
# Advancement alone is not underwriting. Require property context and additional
# numeric reviewer evidence; this selection never labels projections as results.
selected = [d for d in records if d['category'] == 'good'
            and all(d.get(k) for k in ('price', 'income', 'beds'))
            and d['market'] != 'Market not separately specified'
            and (d.get('reviewed_coc') or d.get('reviewer_income'))]
native = []
for source in (Path(__file__).resolve().parents[1] / '_gen/proformas').glob('*.json'):
    record = json.loads(source.read_text())
    if record.get('publication_status') == 'published':
        native.append(validate(record))
if not records or not selected:
    raise ValueError('Refusing an empty candidate cohort; review source structure before deployment')
market_counts = collections.Counter(slug(d['market']) for d in selected)
allowed = {'/proformas/', '/proformas/good/', '/proformas/markets/'}
allowed.update('/proformas/' + d['slug'] + '/' for d in selected + native)
allowed.update('/proformas/markets/' + m + '/' for m, n in market_counts.items() if n >= 3)


def robots(text, value):
    tag = '<meta name="robots" content="' + value + '">'
    pattern = r'<meta\b(?=[^>]*\bname=[\"\x27]robots[\"\x27])[^>]*>'
    return re.sub(pattern, tag, text, flags=re.I) if re.search(pattern, text, re.I) else text.replace('</head>', tag + '\n</head>', 1)


excluded = []
for file in (OUT / 'proformas').rglob('index.html'):
    route = '/' + file.relative_to(OUT).as_posix()[:-10]
    if route not in allowed:
        file.write_text(robots(file.read_text(), 'noindex, follow'))
        excluded.append(route)

# Search-facing overview links directly to the evidence-selected cohort.
file = OUT / 'proformas/index.html'
text = file.read_text()
text = re.sub(r'<!-- curated-evidence:start -->.*?<!-- curated-evidence:end -->', '', text, flags=re.S)
panel = '<!-- curated-evidence:start --><section class="pf-panel"><h2>Compare selected acquisition candidates</h2>'
panel += '<p>This reading list selects ' + str(len(selected)) + ' advanced screening records with property details and additional financial reviewer fields. Source snapshot: October 8, 2026. Confirm availability, expenses and financing before making a purchase decision.</p>'
panel += '<p>Compare the recorded price with the revenue assumption, then list missing operating expenses, debt payments, cash required and downside evidence. A higher projected income is not necessarily a better purchase. Begin with <a href="/tools/first-str-purchase-budget/">your purchase budget</a> and the <a href="/field-guides/acquisition-assumption-register/">assumption register</a>.</p>'
panel += '<div class="pf-items">' + ''.join('<article class="pf-item"><h3><a href="/proformas/' + d['slug'] + '/">' + escape(d['address']) + '</a></h3><p>' + escape(d['market']) + '</p><p>Recorded price: ' + escape(d['price']) + '<br>Projected annual income: ' + escape(d['income']) + '</p></article>' for d in sorted(selected, key=lambda d: (d['market'], d['address']))[:6]) + '</div>'
panel += '<details><summary>Browse the ' + str(len(selected)) + ' selected records by market</summary><ul>'
for d in sorted(selected, key=lambda x: (x['market'], x['address'])):
    panel += '<li><a href="/proformas/' + d['slug'] + '/">' + escape(d['address']) + '</a> — ' + escape(d['market']) + '</li>'
panel += '</ul></details><p>The full screening archive stays available below, including rejected and incomplete records. Those records help explain the screening process but are not presented as complete property underwriting.</p></section><!-- curated-evidence:end -->'
text = re.sub(r'<!-- screening-archive:start --><details class="pf-panel"><summary>.*?</summary>(.*?)</details><!-- screening-archive:end -->', r'\1', text, flags=re.S)
archive_start = text.index('<div class="pf-items">')
archive_end = text.index('<aside class="pf-disclaimer"', archive_start)
archive = text[archive_start:archive_end]
# Keep all existing source links and pagination available under an archive control.
archive = '<details class="pf-panel"><summary>Browse the full screening archive and its directory pages</summary>' + archive + '</details>'
text = text[:archive_start] + panel + '<!-- screening-archive:start -->' + archive + '<!-- screening-archive:end -->' + text[archive_end:]
text = re.sub(r'("dateModified"\s*:\s*")[^"]+', r'\g<1>2026-10-19', text)
file.write_text(text)

# Remove utility-only URLs from every submitted sitemap, not just the child map.
NS = 'http://www.sitemaps.org/schemas/sitemap/0.9'
ET.register_namespace('', NS)
for file in OUT.glob('sitemap*.xml'):
    tree = ET.parse(file)
    if not tree.getroot().tag.endswith('urlset'):
        continue
    changed = False
    for row in list(tree.getroot()):
        loc = row.find('{*}loc')
        if loc is not None and loc.text.startswith(SITE + '/proformas/'):
            if loc.text == SITE + '/proformas/':
                lastmod = row.find('{*}lastmod')
                if lastmod is None:
                    lastmod = ET.SubElement(row, '{'+NS+'}lastmod')
                lastmod.text = '2026-10-19'
                changed = True
            if loc.text[len(SITE):] not in allowed:
                tree.getroot().remove(row)
                changed = True
    if changed:
        tree.write(file, encoding='utf-8', xml_declaration=True)

submitted = {loc.text for sitemap in OUT.glob('sitemap*.xml') for loc in ET.parse(sitemap).getroot().findall('.//{*}loc')}
assert not any(SITE + route in submitted for route in excluded), 'Utility URL leaked into a sitemap'
assert all(SITE + route in submitted for route in allowed), 'Selected owner missing from sitemaps'
assert all('/proformas/' + d['slug'] + '/' in text for d in selected), 'Selected record missing from overview'
report = dict(source_records=len(records), selected_property_records=len(selected),
              selected_directory_routes=len(allowed)-len(selected), utility_routes_noindex=len(excluded),
              policy='Advanced status + price/income/bedrooms/market + numeric reviewer evidence. Archive preserved.')
print(json.dumps(report))
