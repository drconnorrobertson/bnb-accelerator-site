"""Run existing generators with scoped first-buyer and asset preservation."""
import ast
import importlib
import html
import json
import re
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

def update_comparison_discovery():
    """Preserve the customized comparison directory and append scoped cards."""
    registry = ROOT / '_gen/purchase_comparison_cards.json'
    if not registry.exists():
        return []
    cards = json.loads(registry.read_text())
    links = []
    for card in cards:
        url = card['url']
        assert url.startswith('/blog/') and url.endswith('/')
        assert (ROOT / url.strip('/') / 'index.html').exists(), url
        links.append('<article class="bc-option"><h3><a href="' + html.escape(url, quote=True) + '">' + html.escape(card['title']) + '</a></h3><p>' + html.escape(card['description']) + '</p></article>')
    start, end = '<!-- buyer-comparison-expansion:start -->', '<!-- buyer-comparison-expansion:end -->'
    block = start + '<section class="section-sm"><div class="wrap"><div class="section-head"><span class="eyebrow">Purchase-ready comparisons</span><h2>Compare additional acquisition paths for your STR purchase</h2></div><div class="bc-grid">' + ''.join(links) + '</div></div></section>' + end
    path = ROOT / 'compare/index.html'
    content = path.read_text()
    if start in content:
        content = re.sub(re.escape(start) + r'.*?' + re.escape(end), lambda _: block, content, flags=re.S)
    else:
        assert content.count('</main>') == 1
        content = content.replace('</main>', block + '\n</main>')
    path.write_text(content)
    return ['compare/index.html']

def build(module_name):
    import blog
    posts = importlib.import_module(module_name).POSTS
    blog.build(posts)
    comparison_targets = update_comparison_discovery()
    script = ROOT / '_gen/optimize_first_str_buyers.py'
    tree = ast.parse(script.read_text())
    selected = []
    for node in tree.body:
        if isinstance(node, (ast.Import, ast.ImportFrom, ast.FunctionDef)):
            selected.append(node)
        elif isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id in {'ROOT', 'DATE', 'HUB', 'TOOL', 'CONFIG'} for t in node.targets):
            selected.append(node)
    namespace = {'__file__': str(script)}
    exec(compile(ast.Module(body=selected, type_ignores=[]), str(script), 'exec'), namespace)
    namespace['update']('blog/index.html', *namespace['CONFIG']['blog/index.html'])
    for node in tree.body:
        if node.lineno in [66, 67]:
            exec(compile(ast.Module(body=[node], type_ignores=[]), str(script), 'exec'), namespace)
    import gen_site_index
    gen_site_index.main()
    import sitewide
    sitewide.build_sitemap()
    import build_assets
    css = (ROOT / 'assets/style.min.css').read_text()
    build_assets.minify_css = lambda _: css
    targets = ['blog/index.html', 'sitemap/index.html'] + comparison_targets + ['blog/' + p['slug'] + '/index.html' for p in posts]
    build_assets.glob.glob = lambda *args, **kwargs: targets
    build_assets.main()

if __name__ == '__main__':
    assert len(sys.argv) == 2, 'Supply a reviewed post module name'
    build(sys.argv[1])
