"""Read-only priority URL probes; never regenerate the whole persistent inventory."""
import concurrent.futures,html,json,re,sys,urllib.robotparser
from pathlib import Path
from collections import Counter
from audit_blog_indexing_inventory import fetch,BASE,ROOT
def probe(slugs):
 _,_,robots,_=fetch(BASE+'/robots.txt');rp=urllib.robotparser.RobotFileParser();rp.parse(robots.splitlines())
 _,_,xml,_=fetch(BASE+'/sitemap-blog.xml');listed=Counter(html.unescape(x) for x in re.findall(r'<loc>(.*?)</loc>',xml))
 inbound=Counter()
 for p in (ROOT/'public').rglob('index.html'):
  for link in set(re.findall(r'href="(/blog/[^"?#]+/)"',p.read_text())):inbound[BASE+link]+=1
 def one(slug):
  url=BASE+'/blog/'+slug+'/'
  try:
   status,final,s,header=fetch(url,True)
   canon=re.findall(r'<link[^>]+rel="canonical"[^>]+href="([^"]+)"',s)
   article=re.search(r'<article class="article">(.*?)</article>',s,re.S)
   words=len(html.unescape(re.sub('<[^>]+>',' ',article.group(1))).split()) if article else 0
   noindex=bool(re.search(r'<meta[^>]+name="robots"[^>]+noindex',s,re.I) or 'noindex' in header.lower())
   nodes=[n for x in re.findall(r'<script[^>]+application/ld\+json[^>]*>(.*?)</script>',s,re.S) for n in (lambda d:d.get('@graph',[d]))(json.loads(x))]
   data=dict(url=url,http_status=status,final_url=final,live_canonical=canon[0] if len(canon)==1 else '',live_noindex=noindex,robots_allows_googlebot=rp.can_fetch('Googlebot',url),sitemap_occurrences=listed[url],inbound_pages=inbound[url],article_text_present=words>40,visible_article_words=words,article_schema=any(n.get('@type') in ['Article','BlogPosting'] for n in nodes),h1_count=len(re.findall('<h1(?:\\s|>)',s)))
   data['eligible']=status==200 and final==url and canon==[url] and not noindex and data['robots_allows_googlebot'] and listed[url]==1 and inbound[url]>0 and words>40 and data['article_schema'] and data['h1_count']==1
   return data
  except Exception as exc:return dict(url=url,eligible=False,probe_error=str(exc))
 with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:results=list(pool.map(one,slugs))
 assert fetch(BASE+'/')[2]==(ROOT/'public/index.html').read_text(),'Protected homepage live mismatch'
 return results
if __name__=='__main__':print(json.dumps(probe(sys.argv[1:]),indent=2))
