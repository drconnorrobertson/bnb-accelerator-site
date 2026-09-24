# Scenario library generator

`scenario_engine.mjs` is the data-backed source for the 50-market, five-property,
three-goal scenario library. It generates 750 detail pages plus market and
reference hubs. Generated pages are published beneath `/scenarios/` so they do
not replace the site's established `/markets/` acquisition pages.

After generating or refreshing the scenario HTML, run:

```sh
node _gen/scenarios/integrate.mjs
python3 _gen/sitewide.py
python3 _gen/gen_site_index.py
python3 build_assets.py
```

The integration pass rewrites canonicals and internal links for the main
domain and removes links to non-existent intermediate routes.
