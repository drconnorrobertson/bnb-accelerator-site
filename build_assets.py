#!/usr/bin/env python3
"""Minify CSS, then point every page at the hashed asset filenames.

Run after editing assets/style.css or assets/main.js:

    python3 build_assets.py

style.css stays the readable source of truth. The build emits
assets/style.min.css and rewrites the <link> in every HTML file to
style.min.css?v=<content hash>, so a deploy always invalidates the old
cached copy. main.js is left unminified on purpose: it is small, and a
hand-rolled JS minifier is a correctness risk for no meaningful gain.
"""
import glob
import hashlib
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)


def minify_css(css: str) -> str:
    """Whitespace-collapsing minifier that never touches quoted strings.

    The stylesheet embeds `url("data:image/svg+xml,...")` values containing
    significant spaces, so a naive global whitespace collapse corrupts them.
    """
    out = []
    i, n = 0, len(css)
    quote = None
    while i < n:
        c = css[i]

        # inside a quoted string: copy verbatim until the matching quote
        if quote:
            out.append(c)
            if c == "\\" and i + 1 < n:
                out.append(css[i + 1])
                i += 2
                continue
            if c == quote:
                quote = None
            i += 1
            continue

        if c in "\"'":
            quote = c
            out.append(c)
            i += 1
            continue

        # comment
        if c == "/" and i + 1 < n and css[i + 1] == "*":
            end = css.find("*/", i + 2)
            i = n if end == -1 else end + 2
            continue

        # collapse runs of whitespace to a single space
        if c in " \t\r\n":
            j = i
            while j < n and css[j] in " \t\r\n":
                j += 1
            out.append(" ")
            i = j
            continue

        out.append(c)
        i += 1

    s = "".join(out)

    # Strip spaces around structural punctuation, but only at paren depth 0.
    # Inside parentheses the spaces are load-bearing: calc() requires
    # whitespace around + and -, and media features keep `feature: value`.
    res = []
    depth = 0
    quote = None
    i, n = 0, len(s)
    while i < n:
        c = s[i]
        if quote:
            res.append(c)
            if c == "\\" and i + 1 < n:
                res.append(s[i + 1]); i += 2; continue
            if c == quote:
                quote = None
            i += 1
            continue
        if c in "\"'":
            quote = c; res.append(c); i += 1; continue
        if c == "(":
            depth += 1; res.append(c); i += 1; continue
        if c == ")":
            depth = max(0, depth - 1); res.append(c); i += 1; continue

        if depth == 0 and c in "{}:;,>~+":
            while res and res[-1] == " ":
                res.pop()
            res.append(c)
            j = i + 1
            while j < n and s[j] == " ":
                j += 1
            i = j
            continue

        res.append(c)
        i += 1

    s = "".join(res)
    # trailing semicolon before a closing brace is redundant
    s = s.replace(";}", "}")
    return s.strip()


def main():
    css_src = open("assets/style.css", encoding="utf-8").read()
    css_min = minify_css(css_src)
    open("assets/style.min.css", "w", encoding="utf-8").write(css_min)

    saved = len(css_src) - len(css_min)
    print(f"css  {len(css_src):>7,} -> {len(css_min):>7,} bytes  "
          f"({saved:,} saved, {saved / len(css_src):.0%})")

    vcss = hashlib.sha256(css_min.encode()).hexdigest()[:8]
    vjs = hashlib.sha256(open("assets/main.js", "rb").read()).hexdigest()[:8]

    n = 0
    for f in sorted(glob.glob("**/*.html", recursive=True)):
        s = open(f, encoding="utf-8").read()
        o = s
        s = re.sub(r'href="/assets/style(?:\.min)?\.css(?:\?v=[a-f0-9]+)?"',
                   f'href="/assets/style.min.css?v={vcss}"', s)
        s = re.sub(r'src="/assets/main\.js(?:\?v=[a-f0-9]+)?"',
                   f'src="/assets/main.js?v={vjs}"', s)
        if s != o:
            open(f, "w", encoding="utf-8").write(s)
            n += 1

    print(f"stamped css={vcss} js={vjs} across {n} files")


if __name__ == "__main__":
    main()
