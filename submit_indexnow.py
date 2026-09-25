#!/usr/bin/env python3
"""Submit sitemap URLs, optionally restricted to verified live URLs, to IndexNow.

IndexNow is a shared submission endpoint honoured by Bing, Yandex, Seznam and
Naver. Google does not participate. Brave runs an independent index and
publishes no submission endpoint, so the only levers there are the Bravebot
allow in robots.txt and the sitemap reference.

The key file must be live at https://www.bnbaccelerator.com/<key>.txt before a
batch is accepted, so deploy first, then run this.

Usage:
    python3 submit_indexnow.py              # submit every sitemap URL
    python3 submit_indexnow.py --dry-run    # print what would be sent
    python3 submit_indexnow.py --url https://www.bnbaccelerator.com/blog/example/
                                            # submit one sitemap URL
    python3 submit_indexnow.py --since 2026-08-15
                                            # only URLs with lastmod >= date
    python3 submit_indexnow.py --prefix /guides/str-investment/
                                            # only URLs in a route section
    python3 submit_indexnow.py --force      # submit without key verification
"""

import argparse
import json
import sys
from pathlib import Path
from xml.etree import ElementTree as ET
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

BASE_DIR = Path(__file__).parent
SITEMAP = BASE_DIR / "sitemap.xml"
HOST = "www.bnbaccelerator.com"
SITE_URL = f"https://{HOST}"
ENDPOINT = "https://api.indexnow.org/indexnow"

# Must match the filename served at /<key>.txt, and that file's contents.
KEY = "c745eff13e89424cb1ed10f69adea860"

# IndexNow caps a single submission at 10,000 URLs.
BATCH = 10000


def sitemap_entries():
    if not SITEMAP.exists():
        sys.exit("sitemap.xml not found next to this script.")
    out = []

    def read_file(path):
        root = ET.parse(path).getroot()
        if root.tag.endswith("sitemapindex"):
            for item in root:
                loc = next((node.text for node in item if node.tag.endswith("loc")), None)
                if not loc:
                    continue
                child = BASE_DIR / loc.rsplit("/", 1)[-1]
                if not child.exists():
                    sys.exit(f"child sitemap not found: {child.name}")
                read_file(child)
            return
        for item in root:
            loc = next((node.text for node in item if node.tag.endswith("loc")), None)
            mod = next((node.text for node in item if node.tag.endswith("lastmod")), "")
            if loc:
                out.append((loc.strip(), mod.strip() if mod else ""))

    read_file(SITEMAP)
    return out


def key_is_live():
    """IndexNow rejects the batch unless /<key>.txt serves the key."""
    url = f"{SITE_URL}/{KEY}.txt"
    try:
        with urlopen(url, timeout=20) as r:
            return r.read().decode().strip() == KEY
    except (HTTPError, URLError) as e:
        print(f"  key file check failed: {e}")
        return False


def local_key_matches():
    """Catch a mismatch before deploying, which is the usual failure."""
    f = BASE_DIR / f"{KEY}.txt"
    if not f.exists():
        print(f"  warning: {f.name} is missing from the repo")
        return False
    if f.read_text().strip() != KEY:
        print(f"  warning: {f.name} does not contain the key")
        return False
    return True


def submit(urls):
    payload = json.dumps({
        "host": HOST,
        "key": KEY,
        "keyLocation": f"{SITE_URL}/{KEY}.txt",
        "urlList": urls,
    }).encode()
    req = Request(ENDPOINT, data=payload, method="POST",
                  headers={"Content-Type": "application/json; charset=utf-8"})
    with urlopen(req, timeout=30) as r:
        return r.status, r.read().decode()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", action="append", default=[],
                        help="Submit only this canonical sitemap URL (repeatable)")
    parser.add_argument("--since", help="Only URLs with lastmod on or after YYYY-MM-DD")
    parser.add_argument("--prefix", action="append", default=[],
                        help="Submit only canonical URLs under this site-root path (repeatable)")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    entries = sitemap_entries()

    if args.since:
        entries = [e for e in entries if e[1] >= args.since]
        print(f"filtered to lastmod >= {args.since}")

    if args.prefix:
        prefixes = tuple(SITE_URL + p for p in args.prefix)
        entries = [e for e in entries if e[0].startswith(prefixes)]
        print(f"filtered to route prefixes: {', '.join(args.prefix)}")

    if args.url:
        requested = set(args.url)
        known = {url for url, _ in entries}
        missing = requested - known
        if missing:
            parser.error(f"URL not present in selected sitemap entries: {sorted(missing)}")
        entries = [e for e in entries if e[0] in requested]

    urls = [u for u, _ in entries]
    print(f"{len(urls)} URLs to submit")

    if args.dry_run:
        print("\n".join(urls))
        return

    if not urls:
        print("nothing to submit")
        return

    print("Checking local IndexNow key file ...")
    local_key_matches()

    print("Checking live IndexNow key file ...")
    if not key_is_live():
        if not args.force:
            sys.exit("Key file is not live yet. Deploy first, then re-run. "
                     "Pass --force to submit anyway.")
        print("  key NOT verified; --force given, submitting anyway")
        print("  expect the endpoint to reject this: IndexNow validates the")
        print("  key file before accepting a batch.")
    else:
        print("  key verified")

    for i in range(0, len(urls), BATCH):
        chunk = urls[i:i + BATCH]
        try:
            status, body = submit(chunk)
            print(f"IndexNow responded {status} {body!r} for {len(chunk)} URLs")
            print("200 or 202 means the batch was accepted for processing.")
        except HTTPError as e:
            print(f"IndexNow rejected the batch: {e.code} {e.read().decode()[:300]}")
            sys.exit(1)
        except URLError as e:
            print(f"Could not reach IndexNow: {e}")
            sys.exit(1)


if __name__ == "__main__":
    main()
