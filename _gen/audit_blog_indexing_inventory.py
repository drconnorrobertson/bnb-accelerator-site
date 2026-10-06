"""Persistent indexing evidence, not a guessed index count. Private _gen output.
Read current public build and actual GSC snapshot. Probe only priority URLs.
"""
import concurrent.futures, csv, html, json, re, urllib.request, urllib.robotparser
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE='https://www.bnbaccelerator.com'

def fetch(url,googlebot=False):
    req=urllib.request.Request(url,headers={'User-Agent':'Googlebot' if googlebot else 'BNB-SEO-Evidence-Audit/1.0'})
    for attempt in range(2):
        try:
            with urllib.request.urlopen(req,timeout=30) as r:return r.status,r.geturl(),r.read().decode(),r.headers.get('X-Robots-Tag','')
        except Exception:
            if attempt:raise

def main():
    evidence=json.loads((ROOT/'_gen/blog-indexing-evidence-2026-10-06.json').read_text())
    priorities=evidence['priority_urls'];perf={x['page']:x for x in evidence['performance_pages']}
    inspected={x['url']:x for x in evidence['inspection_results']}
    supplemental=ROOT/'_gen/blog-indexing-supplemental-evidence.json'
    if supplemental.exists():
        inspected.update({x['url']:x for x in json.loads(supplemental.read_text())['inspection_results']})
    sitemap={html.unescape(x) for x in re.findall(r'<loc>(.*?)</loc>',(ROOT/'public/sitemap-blog.xml').read_text())}
    inbound=Counter()
    for path in (ROOT/'public').rglob('index.html'):
        links=set(re.findall(r'href="(/blog/[^"?#]+/)"',path.read_text()))
        for link in links:inbound[BASE+link]+=1
    _,_,robots,_=fetch(BASE+'/robots.txt');rp=urllib.robotparser.RobotFileParser();rp.parse(robots.splitlines())
    def probe(url):
        try:
            status,final,s,xrobots=fetch(url,True)
            canon=re.findall(r'<link[^>]+rel="canonical"[^>]+href="([^"]+)"',s)
            article=re.search(r'<article class="article".*?</article>',s,re.S)
            return url,dict(http_status=status,final_url=final,live_canonical=canon[0] if len(canon)==1 else '',live_noindex=bool(re.search(r'<meta[^>]+name="robots"[^>]+noindex',s,re.I) or 'noindex' in xrobots.lower()),article_text_present=bool(article and len(re.sub('<[^>]+>',' ',article.group()).split())>40))
        except Exception as exc:return url,dict(probe_error=str(exc),http_status='unknown')
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:live=dict(pool.map(probe,priorities))
    rows=[]
    for path in sorted((ROOT/'public/blog').glob('*/index.html')):
        slug=path.parent.name;url=BASE+'/blog/'+slug+'/';s=path.read_text();p=perf.get(url);inspection=inspected.get(url,{});probe=live.get(url,{})
        canonical=re.findall(r'<link[^>]+rel="canonical"[^>]+href="([^"]+)"',s)
        noindex=bool(re.search(r'<meta[^>]+name="robots"[^>]+noindex',s,re.I))
        stage=re.search(r'data-purchase-stage="([^"]+)"',s)
        coverage=inspection.get('coverageState','unknown');error=inspection.get('error','')
        action='Review substantive buyer support; not an exclusion inference'
        if inspection.get('verdict')=='PASS':action='Preserve confirmed indexed page; improve buyer usefulness as needed'
        elif coverage!='unknown':action='Review returned coverage evidence and underlying cause before any intervention'
        if probe.get('http_status')==200 and probe.get('live_canonical')!=url:action='Investigate confirmed live canonical mismatch'
        if noindex or probe.get('live_noindex'):action='Investigate actual noindex directive'
        rows.append(dict(url=url,observed_at=evidence['observed_at'],priority=url in priorities,indexing_verdict=inspection.get('verdict','unknown'),indexing_state=inspection.get('indexingState','unknown'),coverage_state=coverage,last_google_crawl=inspection.get('lastCrawlTime','unknown'),inspection_error=error,http_status=probe.get('http_status','not probed'),final_url=probe.get('final_url','not probed'),robots_allows_googlebot=rp.can_fetch('Googlebot',url),source_noindex=noindex,live_noindex=probe.get('live_noindex','not probed'),source_canonical=canonical[0] if len(canonical)==1 else '',live_canonical=probe.get('live_canonical','not probed'),sitemap_included=url in sitemap,inbound_pages=inbound[url],topic_cluster=stage.group(1) if stage else 'review needed',impressions=p['impressions'] if p else 'not returned',clicks=p['clicks'] if p else 'not returned',performance_start=evidence['performance_start'],performance_end=evidence['performance_end'],article_text_present=probe.get('article_text_present','not probed'),probe_error=probe.get('probe_error',''),recommended_action=action))
    for row in rows:
        row['observed_at']=inspected.get(row['url'],{}).get('observed_at',row['observed_at'])
    output=ROOT/'_gen/blog-indexing-inventory.csv'
    with output.open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    checked=[r for r in rows if r['priority']]
    assert len(checked)==25
    assert all(r['http_status']==200 and r['final_url']==r['url'] and r['live_canonical']==r['url'] and r['article_text_present'] and not r['live_noindex'] and r['robots_allows_googlebot'] and r['sitemap_included'] and r['inbound_pages'] for r in checked),[(r['url'],r['probe_error']) for r in checked if r['http_status']!=200]
    print('PASS:',len(rows),'public blog article inventory rows;',len(checked),'priority production Googlebot-UA probes eligible with text, self canonicals, robots, sitemap and inbound links')
    print('Actual returned inspection verdicts:',dict(Counter(r['indexing_verdict'] for r in checked)))
    print('Googlebot-UA response is not proof of access by authenticated Google crawler IP or of rendering/indexing. Unreturned performance is not zero; API coverage is separately recorded.')

if __name__=='__main__':main()
