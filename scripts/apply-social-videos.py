"""Preserve curated social embeds after upstream page generators and transforms."""
from pathlib import Path
import json,re,sys
ROOT=Path(__file__).resolve().parents[1]
def apply(target):
 blocks=json.loads((ROOT/'_gen/social-video-blocks.json').read_text())
 for oldpage in target.rglob('index.html'):
  route='/' + oldpage.relative_to(target).as_posix().removesuffix('index.html')
  if route not in blocks:
   oldtext=oldpage.read_text()
   if '<!-- social-video-library:start -->' in oldtext:
    oldpage.write_text(re.sub(r'<!-- social-video-library:start -->.*?<!-- social-video-library:end -->','',oldtext,flags=re.S))
 for route,block in blocks.items():
  p=target/route.strip('/')/'index.html'
  s=p.read_text();s=re.sub(r'<!-- social-video-library:start -->.*?<!-- social-video-library:end -->','',s,flags=re.S)
  assert '</main>' in s,route
  s=s.replace('</main>',block+'\n</main>')
  if '/assets/social-video-library.css' not in s:s=s.replace('</head>','<link rel="stylesheet" href="/assets/social-video-library.css">\n</head>')
  if '/assets/video-facade.v1.js' not in s:s=s.replace('</body>','<script src="/assets/video-facade.v1.js" defer></script>\n</body>')
  p.write_text(s)
 print(json.dumps({'socialVideoOwnerPages':len(blocks),'target':str(target)}))
if __name__=='__main__':apply(ROOT/(sys.argv[1] if len(sys.argv)>1 else 'public'))
