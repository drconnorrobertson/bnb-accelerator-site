"""Retain current provider research after legacy comparison generators."""
from pathlib import Path
import json,re,sys
ROOT=Path(__file__).resolve().parents[1]
def apply(target):
 blocks=json.loads((ROOT/'_gen/provider-comparison-blocks.json').read_text())
 for route,block in blocks.items():
  p=target/route.strip('/')/'index.html';s=p.read_text();s=re.sub(r'<!-- provider-research:start -->.*?<!-- provider-research:end -->','',s,flags=re.S);assert '</main>' in s,route;s=s.replace('</main>',block+'</main>')
  s=re.sub(r'<link\b[^>]*href="/assets/provider-research\.css"[^>]*>\s*','',s)
  if '/assets/provider-research.css' not in s:s=s.replace('</head>','<link rel="stylesheet" href="/assets/provider-research.css">\n</head>')
  p.write_text(s)
 for path,marker,body in [
  ('compare/index.html','provider-directory','<section class="section-sm"><div class="wrap"><h2>Research 100 STR providers</h2><p><a href="/compare/provider-directory/">Compare acquisition teams, education, managers, software and related services</a> with separate comparison, alternatives and pricing guides grounded in official sources.</p></div></section>'),
  ('blog/index.html','video-discovery','<section class="section-sm"><div class="wrap"><h2>Watch source videos and compare your options</h2><p><a href="/blog/video-library/">Browse every discovered BNB Accelerator YouTube video by topic</a> or <a href="/compare/provider-directory/">research 100 providers, alternatives and pricing questions</a>.</p></div></section>')]:
  p=target/path;s=p.read_text();pattern=r'<!-- '+marker+r':start -->.*?<!-- '+marker+r':end -->';s=re.sub(pattern,'',s,flags=re.S);s=s.replace('</main>','<!-- '+marker+':start -->'+body+'<!-- '+marker+':end --></main>');p.write_text(s)
 p=target/'sitemap.xml';s=p.read_text()
 if 'sitemap-providers.xml' not in s:
  close=re.search(r'</(?:\w+:)?sitemapindex>',s).group();prefix='ns0:' if 'ns0:sitemapindex' in s else '';s=s.replace(close,'<'+prefix+'sitemap><'+prefix+'loc>https://www.bnbaccelerator.com/sitemap-providers.xml</'+prefix+'loc></'+prefix+'sitemap>'+close);p.write_text(s)
 print(json.dumps({'preservedProviderOwners':len(blocks),'directoryLinked':True}))
if __name__=='__main__':apply(ROOT/(sys.argv[1] if len(sys.argv)>1 else 'public'))
