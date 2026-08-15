#!/usr/bin/env python3
"""Insert (or refresh) the Client Wins strip on the home page.

Idempotent: the block is delimited so re-running replaces it rather than
stacking another copy.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_wins
import tpl

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
START = "<!-- home-wins:start -->"
END = "<!-- home-wins:end -->"

# The eight that lead with the strongest verifiable numbers.
PICKS = ["hari-m", "murali", "antonio-a", "sara-o",
         "kenneth-m", "jason-h", "shardul", "randy-l"]


def main():
    man = {m["slug"]: m for m in json.load(
        open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          "wins_manifest.json")))}
    total = len(man)
    cards = []
    for s in PICKS:
        if s not in man:
            continue
        client, loc, headline, stats, cs = gen_wins.WINS[s]
        who = client or "BNB Accelerator client"
        stop = "" if who.endswith(".") else "."
        alt = f"{who}, {loc}. {headline}" if loc else f"{who}{stop} {headline}"
        chips = "".join(f'<span class="win-stat">{x}</span>' for x in stats[:3])
        meta = f'<span class="win-loc">{loc}</span>' if loc else ""
        m = man[s]
        cards.append(f"""        <figure class="win-card" style="--win-bg:#{m['bg']}">
          <button class="win-shot" type="button" data-win-open
                  data-full="/assets/wins/{s}.jpg"
                  data-caption="{tpl.esc(alt)}"
                  aria-label="Enlarge: {tpl.esc(alt)}">
            <img src="/assets/wins/{s}-card.jpg" alt="{tpl.esc(alt)}"
                 width="{m['card_w']}" height="{m['card_h']}" loading="lazy" decoding="async">
          </button>
          <figcaption class="win-body">
            <h3>{who}</h3>
            {meta}
            <div class="win-stats">{chips}</div>
          </figcaption>
        </figure>""")

    block = f"""{START}
  <section>
    <div class="wrap">
      <div class="section-head" data-reveal data-hub-heading>
        <span class="eyebrow">Client Wins</span>
        <h2>Real numbers, straight from their dashboards</h2>
        <p>Revenue, occupancy, average daily rate and review scores from actual client properties, published with each client's permission. {total} of them, and not one is a projection.</p>
      </div>
      <div class="win-grid win-strip">
{chr(10).join(cards)}
      </div>
      <div class="btn-row center mt-4" data-reveal>
        <a class="btn btn-outline" href="/wins/">See all {total} client wins</a>
      </div>
      <p class="disclaimer mt-3">Each graphic shows the actual reported result for one specific property, published with that client's permission. These are not typical, not projections, and not a promise of what any other property will do.</p>
    </div>
  </section>

  <div class="win-lightbox" data-win-lightbox hidden>
    <button class="win-lightbox-close" type="button" data-win-close aria-label="Close">&times;</button>
    <figure>
      <img src="" alt="" data-win-img>
      <figcaption data-win-cap></figcaption>
    </figure>
  </div>
{END}"""

    p = os.path.join(ROOT, "index.html")
    s = open(p, encoding="utf-8").read()
    if START in s:
        s = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: block,
                   s, flags=re.S)
    else:
        # directly after the stats bar, high on the page where proof belongs
        anchor = '  <section class="stats-bar">'
        i = s.index(anchor)
        j = s.index("</section>", i) + len("</section>\n")
        s = s[:j] + "\n" + block + "\n" + s[j:]
    open(p, "w", encoding="utf-8").write(s)
    print(f"home wins strip: {len(cards)} cards, links to all {total}")


if __name__ == "__main__":
    main()
