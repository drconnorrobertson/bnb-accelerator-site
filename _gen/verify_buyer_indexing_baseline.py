"""Read-only serving evidence for ten first-inspected buyer owners; not content review."""
import concurrent.futures, datetime, json, re, urllib.robotparser
from pathlib import Path
from urllib.parse import urlsplit
from verify_published_batch import BASE, fetch

ROOT = Path(__file__).resolve().parents[1]
SLUGS = ['gilbert-chandler-airbnb-investing', 'nashville-airbnb-investing',
 'vrbo-listing-handoff-buying-str', 'short-term-rental-investing-2026',
 'str-portfolio-diversification', 'str-investing-mistakes', 'how-to-buy-first-airbnb',
 'how-to-choose-str-market', 'str-market-saturation', 'w2-to-wealth-str-portfolio']

def main():
    robots = urllib.robotparser.RobotFileParser()
    robots.parse(fetch(BASE+'/robots.txt')[0].splitlines())
    sitemap = fetch(BASE+'/sitemap-blog.xml')[0]
    pages = list((ROOT/'public').rglob('index.html'))
    def check(slug):
        route = '/blog/'+slug+'/'
        url = BASE+route
        body, final = fetch(url)
        local = ROOT/'public/blog'/slug/'index.html'
        assert final == url and body == local.read_text(), ('Serving mismatch', url)
        canonical = re.findall(r'<link[^>]+rel="canonical"[^>]+href="([^"]+)"', body)
        assert canonical == [url] and robots.can_fetch('Googlebot',url)
        assert not re.search(r'<meta[^>]+name="robots"[^>]+content="[^"]*noindex',body,re.I)
        assert '<loc>'+url+'</loc>' in sitemap
        article = re.search(r'<article class="article">(.*?)</article>',body,re.S)
        assert article and len(re.sub('<[^>]*>','',article[1]).strip()) > 500
        inbound = sum(route in set(re.findall(r'href="(/blog/[^"?#]+/)"',p.read_text())) for p in pages)
        assert inbound > 0
        return {'url':url,'http_status':200,'final_url':final,'canonical':url,
          'robots_allowed':True,'noindex':False,'exact_public_build_match':True,
          'server_article_text':True,'sitemap_included':True,'inbound_public_pages':inbound}
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        records = list(pool.map(check,SLUGS))
    assert fetch(BASE+'/')[0] == (ROOT/'public/index.html').read_text()
    print(json.dumps({'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
      'protected_homepage_exact':True,'records':records,
      'limits':'Live HTTP/robots/text evidence is distinct from actual Google Inspection, browser rendering, content accuracy and search/conversion gains.'},indent=2))

if __name__ == '__main__': main()
