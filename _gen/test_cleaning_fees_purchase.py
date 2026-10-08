"""Independent arithmetic and unchanged artifact checks before commit."""
import hashlib,re,subprocess
from pathlib import Path
R=Path(__file__).resolve().parents[1]
assert 80*225==18000 and 80*(190+25)==17200
assert 18000-17200==800 and 18000-1800-17200==-1000
assert 114000-11400-19200-17200==66200
assert 96000-9600-19200-1000==66200
assert 96000-9600-19200+800==68000 and 68000-66200==1800
assert 80*270==21600 and 18000-1800-21600==-5400
assert 66200-4400==61800
assert 120*225==27000 and 120*270==32400
assert 27000-2700-32400==-8100 and 96000-9600-19200-8100==59100
assert 61800-59100==2700 and 40*(225-22.5-270)==-2700
assert 280000+600+1800+900==283300 and 300000-283300==16700
assert 8*(270-215)==440 and 283300+440==283740 and 300000-283740==16260
slug='cleaning-fees-gross-revenue'
old=subprocess.check_output(['git','show','HEAD:blog/index.html'],cwd=R,text=True)
new=(R/'blog/index.html').read_text()
cards=lambda s:[x for x in re.findall(r'<article class="post-card".*?</article>',s,re.S) if '/blog/'+slug+'/' not in x]
assert cards(old)==cards(new) and len(cards(new))==745
path='blog/'+slug+'/index.html'
old=subprocess.check_output(['git','show','HEAD:'+path],cwd=R,text=True);new=(R/path).read_text()
assert old.split('</article>',1)[1]==new.split('</article>',1)[1]
assert re.search(r'<div class="author-box">.*?</div>\s*</div>',old,re.S)[0]==re.search(r'<div class="author-box">.*?</div>\s*</div>',new,re.S)[0]
assert hashlib.sha256((R/'index.html').read_bytes()).hexdigest()=='58db91a9ec1bd726f5d6d68052208b9153d04eecd60de82e723725e6bf2ee7e2'
assert hashlib.sha256((R/'public/index.html').read_bytes()).hexdigest()=='5a3fe67b5045fb0cfe7a6620b27e34e9149ed53cb4c6359f2aeb3ad770ce6484'
print('PASS independent arithmetic, 745 other archive cards, author/outer conversion flow and source/built homepage hashes.')
