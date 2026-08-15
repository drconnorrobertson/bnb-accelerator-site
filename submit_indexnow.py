#!/usr/bin/env python3
"""Submit every URL in sitemap.xml to IndexNow.

IndexNow is a shared submission endpoint honoured by Bing, Yandex, Seznam and
Naver. Google does not participate. Brave runs an independent index and
publishes no submission endpoint, so the only levers there are the Bravebot
allow in robots.txt and the sitemap reference.

The key file must be live at https://mybnbaccelerator.com/<key>.txt before a
batch is accepted, so deploy first, then run this.

Usage:
    python3 submit_indexnow.py              # submit every sitemap URL
    python3 submit_indexnow.py --dry-run    # print what would be sent
    python3 submit_indexnow.py --since 2026-08-15
                                            # only URLs with lastmod >= date
    python3 submit_indexnow.py --force      # submit without key verification
"""

import json
import re
import sys
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

BASE_DIR = Path(__file__).parent
SITEMAP = BASE_DIR / "sitemap.xml"
HOST = "mybnbaccelerator.com"
SITE_URL = f"https://{HOST}"
ENDPOINT = "https://api.indexnow.org/indexnow"

# Must match the filename served at /<key>.txt, and that file's contents.
KEY = "c745eff13e89424cb1ed10f69adea860"

# IndexNow caps a single submission at 10,000 URLs.
BATCH = 10000


def sitemap_entries():
    if not SITEMAP.exists():
        sys.exit("sitemap.xml not found next to this script.")
    xml = SITEMAP.read_text(encoding="utf-8")
    out = []
    for block in re.findall(r"<url>(.*?)</url>", xml, re.S):
        loc = re.search(r"<loc>(.*?)</loc>", block)
        mod = re.search(r"<lastmod>(.*?)</lastmod>", block)
        if loc:
            out.append((loc.group(1).strip(), mod.group(1).strip() if mod else ""))
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
    entries = sitemap_entries()

    since = None
    if "--since" in sys.argv:
        since = sys.argv[sys.argv.index("--since") + 1]
        entries = [e for e in entries if e[1] >= since]
        print(f"filtered to lastmod >= {since}")

    urls = [u for u, _ in entries]
    print(f"{len(urls)} URLs to submit")

    if "--dry-run" in sys.argv:
        print("\n".join(urls))
        return

    if not urls:
        print("nothing to submit")
        return

    print(f"Checking local {KEY}.txt ...")
    local_key_matches()

    print(f"Checking {SITE_URL}/{KEY}.txt ...")
    if not key_is_live():
        if "--force" not in sys.argv:
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
