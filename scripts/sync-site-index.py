"""Keep the human index aligned with the final, curated search inventory."""
import collections
import html
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlsplit

root = Path(sys.argv[1] if len(sys.argv) > 1 else 'public')
page = root / 'sitemap/index.html'
text = page.read_text()
text = re.sub(r'<!-- current-search-index:start -->.*?<!-- current-search-index:end -->', '', text, flags=re.S)
urls = set()
for sitemap in root.glob('sitemap-*.xml'):
    tree = ET.parse(sitemap)
    if tree.getroot().tag.endswith('urlset'):
        urls.update(urlsplit(n.text).path for n in tree.findall('.//{*}loc'))
linked = set(re.findall(r'href="(/[^"?#]*)"', text))
groups = collections.defaultdict(list)
for route in sorted(urls - linked):
    source = root / route.strip('/') / 'index.html'
    content = source.read_text()
    title = re.search(r'<h1\b[^>]*>(.*?)</h1>', content, re.S | re.I)
    label = html.unescape(re.sub('<[^>]*>', '', title.group(1))).strip() if title else route
    group = route.strip('/').split('/')[0].replace('-', ' ').title()
    groups[group].append((route, label))
blocks = ['<!-- current-search-index:start --><section class="section"><div class="wrap"><h2>More resources by topic</h2>']
for group, rows in sorted(groups.items()):
    blocks.append(f'<details><summary>{html.escape(group)} ({len(rows)})</summary><ul class="sitemap-list">')
    blocks.extend(f'<li><a href="{html.escape(route, quote=True)}">{html.escape(label)}</a></li>' for route, label in rows)
    blocks.append('</ul></details>')
blocks.append('</div></section><!-- current-search-index:end -->')
assert '</main>' in text
text = text.replace('</main>', '\n'.join(blocks) + '</main>', 1)
# The archive can contain unlisted utility pages; describe the curated set accurately.
text = re.sub(r'Site Index: All \d+ Pages', f'Site Index: {len(urls):,} Searchable Resources', text)
text = re.sub(r'Every page on this site, organised by section\. \d+ pages in total\.',
              f'Browse {len(urls):,} searchable resources, organised by section.', text)
text = re.sub(r'Every page on bnbaccelerator\.com, organised by section: \d+ pages',
              f'Browse {len(urls):,} searchable resources on bnbaccelerator.com', text)
page.write_text(text)
missing = urls - set(re.findall(r'href="(/[^"?#]*)"', text))
assert not missing, missing
print(f'Human index: {len(urls)} submitted routes; {sum(map(len, groups.values()))} missing links repaired.')
