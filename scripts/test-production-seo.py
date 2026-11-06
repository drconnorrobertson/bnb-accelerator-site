import tempfile,subprocess
from pathlib import Path
CHECK=Path(__file__).with_name('check-production-seo.py').resolve()
paths=['str-investing-for-business-owners','business-working-capital-before-str-purchase']
def run(mode):
 with tempfile.TemporaryDirectory() as d:
  r=Path(d);urls=[]
  for slug in paths:
   u='https://www.bnbaccelerator.com/blog/'+slug+'/';urls.append(u)
   p=r/'blog'/slug/'index.html';p.parent.mkdir(parents=True);p.write_text('<html><head><link rel="canonical" href="'+('https://example.com/' if mode=='canonical' else u)+'">'+('<meta name="robots" content="noindex,follow">' if mode=='noindex' else '')+'</head><body><h1>Test</h1>'+('<a href="/missing/">bad</a>' if mode=='link' else '')+'</body></html>')
  (r/'sitemap-blog.xml').write_text('<urlset>'+''.join('<url><loc>'+u+'</loc></url>' for u in urls+(urls[:1] if mode=='duplicate' else []))+'</urlset>')
  result=subprocess.run(['python3',str(CHECK),str(r)],capture_output=True,text=True)
  assert (result.returncode==0)==(mode=='valid'),(mode,result.stdout,result.stderr)
for mode in ['valid','canonical','noindex','link','duplicate']:run(mode)
print('Production SEO regression fixtures passed: valid plus four failure cases.')
