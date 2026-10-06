"""Run existing generators with scoped first-buyer and asset preservation."""
import ast
import importlib
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

def build(module_name):
    import blog
    posts = importlib.import_module(module_name).POSTS
    blog.build(posts)
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
    targets = ['blog/index.html', 'sitemap/index.html'] + ['blog/' + p['slug'] + '/index.html' for p in posts]
    build_assets.glob.glob = lambda *args, **kwargs: targets
    build_assets.main()

if __name__ == '__main__':
    assert len(sys.argv) == 2, 'Supply a reviewed post module name'
    build(sys.argv[1])
