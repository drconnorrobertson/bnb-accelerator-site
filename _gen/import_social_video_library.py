from pathlib import Path
import json,re,html,collections,sys
R=Path(__file__).resolve().parents[1];sys.path.insert(0,str(R/'_gen'));import tpl
E=html.escape
spec=[]
for line in (R/'_gen/social-video-topics.tsv').read_text().splitlines():
 k,path,terms,q,a=line.split('|');spec.append(dict(key=k,path=path,terms=terms.split(','),q=q,a=a))
d=json.loads((R/'_gen/social-video-inventory-2026-11-22.json').read_text());groups=collections.defaultdict(list)
for v in d['videos']:
 t=v['title'].lower();candidates=[]
 for n,s in enumerate(spec):
  score=sum(2+len(term.split())*2 for term in s['terms'] if term in t)
  if score:candidates.append((score,-n,s))
 s=max(candidates,key=lambda x:x[:2])[2] if candidates else spec[-1]
 if v['channel']=='mybnbacceleratortestimonials' or 'client review' in t or 'testimonial' in t or 'client interview' in t:
  if 'victoria' in t:s=dict(spec[-1],path='/case-studies/victoria-sevierville/',key='victoria')
  elif 'pruthvi' in t:s=dict(spec[-1],path='/reviews/',key='testimonials')
  else:s=dict(spec[-1],path='/testimonials/',key='testimonials')
 # Website-linked property walk-throughs belong with the matching address if it exists.
 if v.get('channel')=='website-linked':
  match=None
  for li in re.findall(r'<li>.*?</li>',(R/'index.html').read_text(),re.S):
   if v['id'] in li:
    address=html.unescape(re.sub('<[^>]+>',' ',li)).split('|')[0].strip();slug=re.sub(r'[^a-z0-9]+','-',address.lower()).strip('-')
    if (R/'proformas'/slug/'index.html').exists():match='/proformas/'+slug+'/'
    break
  if match:s=dict(spec[-1],path=match,key='property')
  elif v.get('existingPages'):s=dict(spec[-1],path=v['existingPages'][0],key='property')
  else:s=dict(spec[-1],path='/blog/str-underwriting-video-questions/',key='underwriting')
 v['ownerPath']=s['path'];v['topic']=s['key'];groups[s['path']].append(v)
# Retain subject-focused page ownership; original channel titles are labels, not editorial assertions.
created=[];modified=[]
for path,vs in groups.items():
 dest=R/path.strip('/')/'index.html';specmatch=next((x for x in spec if x['path']==path),spec[-1]);q,a=specmatch['q'],specmatch['a']
 if dest.exists():s=dest.read_text()
 else:
  title=q.replace('What questions should an STR buyer ask after a tax video?','STR tax video FAQ: questions to ask before buying').replace('What needs to be written into a seller-financed STR proposal?','Seller financing for an STR: video FAQ')
  if path=='/blog/subject-to-str-video-questions/':title='Subject-to STR purchases: creative financing video FAQ'
  if path=='/blog/str-financing-video-questions/':title='STR financing video FAQ: comparing quotes and cash to close'
  if path=='/blog/str-management-video-questions/':title='STR management video FAQ: fees, handoffs and owner work'
  if path=='/blog/str-underwriting-video-questions/':title='STR underwriting video FAQ: revenue, expenses and cash flow'
  if path=='/blog/str-risk-video-questions/':title='STR risk video FAQ: test the downside before you buy'
  if path=='/blog/str-portfolio-video-questions/':title='STR portfolio video FAQ: planning your next purchase'
  if path=='/blog/bnb-accelerator-service-video-faq/':title='BNB Accelerator service video FAQ: scope and buyer decisions'
  body='<section class="hero hero-page"><div class="wrap wrap-narrow">'+tpl.breadcrumb_html([('Home','/'),('Blog','/blog/'),('Video FAQ',path)])+'<p class="eyebrow">BNB Accelerator video answers</p><h1>'+E(title)+'</h1><p class="lead">'+E(a)+'</p><p>Published November 22, 2026. Company videos and an editorial buyer checklist.</p></div></section><section class="section-sm"><div class="wrap wrap-narrow"><h2>Use the original recording with current evidence</h2><p>The videos below are source material from BNB Accelerator. This page groups recordings by their published titles. It does not present a transcript or claim that every statement in an older recording is current. Open the full recording for its context, then use the questions here to prepare your purchase file.</p><h2>'+E(q)+'</h2><p>'+E(a)+'</p><h2>What belongs in the purchase file?</h2><p>Keep the property address, source dates, seller records, financing quotes, vendor scopes, legal-use findings and unresolved questions in one file. Identify who owns each follow-up and the date it must be resolved. Separate a verified fact from a forecast or an example described in a recording.</p><h2>How should you compare two proposed deals?</h2><p>Use the same period, cash-investment definition and operating assumptions. Include acquisition charges, repair and furnishing costs, opening reserves and ongoing service fees. A higher revenue headline can still leave less cash after expenses and debt service.</p><p>Continue with <a href="/tools/first-str-purchase-budget/">the purchase budget worksheet</a>, <a href="/revenue-projections/">the revenue evidence guide</a> and <a href="/how-it-works/">the acquisition process</a>.</p></div></section>'+tpl.cta_band('Bring your next property question','Discuss the current scope, your purchase budget and the evidence you need to make a decision.')
  s=tpl.page(title=title+' | BNB Accelerator',description=a[:155],path=path,body=body,active='/blog/',extra_schema=tpl.article_schema(title,a[:155],tpl.SITE+path,'2026-11-22'))
  dest.parent.mkdir(parents=True,exist_ok=True);created.append(path)
 if path=='/case-studies/victoria-sevierville/':vs=[v for v in vs if v['id']!='up5-F-EAsTo']
 cards=[]
 for v in vs:
  title=v['title'] or 'Property video from the BNB Accelerator website';i=v['id'];short='/shorts/' in v['url'];cards.append('<article class="social-video-card"><h3>'+E(title)+'</h3><button class="social-video-play" type="button" data-video-id="'+i+'" data-video-title="'+E(title,quote=True)+'" aria-label="Play '+E(title,quote=True)+'"><img src="https://i.ytimg.com/vi/'+i+'/hqdefault.jpg" alt="" width="480" height="360" loading="lazy" decoding="async"><span>Play video</span></button><p><a href="'+E(v['url'],quote=True)+'" target="_blank" rel="noopener">Watch original '+('YouTube Short' if short else 'YouTube video')+'</a></p></article>')
 block='<!-- social-video-library:start --><section class="section-sm social-video-library" id="related-video-answers"><div class="wrap wrap-narrow"><p class="eyebrow">Watch the source</p><h2>Related BNB Accelerator video answers</h2><p>Original channel titles are shown below. Recorded examples, income headlines and tax illustrations describe their own context; they are not guaranteed outcomes or a current fee quote. Check the recording date and the evidence for your property.</p><h3>'+E(q)+'</h3><p>'+E(a)+'</p><div class="social-video-grid">'+''.join(cards)+'</div><p><a href="/blog/video-library/">Browse all BNB Accelerator videos by topic</a></p></div></section><!-- social-video-library:end -->'
 s=re.sub(r'<!-- social-video-library:start -->.*?<!-- social-video-library:end -->','',s,flags=re.S);s=s.replace('</main>',block+'\n</main>')
 s=s.replace('</head>','<link rel="stylesheet" href="/assets/social-video-library.css">\n</head>') if '/assets/social-video-library.css' not in s else s
 if '/assets/video-facade.v1.js' not in s:s=s.replace('</body>','<script src="/assets/video-facade.v1.js" defer></script>\n</body>')
 # Existing pages keep their existing FAQ structured data. New pages have matching visible questions.
 if path in created:
  faq={'@context':'https://schema.org','@type':'FAQPage','mainEntity':[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}}]};s=s.replace('</head>','<script type="application/ld+json">'+json.dumps(faq)+'</script></head>')
 dest.write_text(s);modified.append(path)
css='.social-video-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:2rem}.social-video-card{min-width:0}.social-video-card h3{font-size:1.05rem;line-height:1.5}.social-video-play{position:relative;display:block;padding:0;border:0;background:#1b2541;color:#fff;width:100%;cursor:pointer;aspect-ratio:16/9;overflow:hidden;border-radius:.5rem}.social-video-play img{width:100%;height:100%;object-fit:cover}.social-video-play span{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);background:#1b2541;padding:.75rem 1rem;border-radius:.3rem;font-size:1rem}.social-video-card iframe{width:100%;aspect-ratio:16/9;height:auto;border:0}.social-video-play:focus-visible{outline:3px solid #b56a24;outline-offset:4px}@media(max-width:600px){.social-video-grid{grid-template-columns:1fr}}'
(R/'assets/social-video-library.css').write_text(css)
hub='/blog/video-library/';title='BNB Accelerator video library: FAQ answers by topic';body='<section class="hero hero-page"><div class="wrap wrap-narrow"><p class="eyebrow">YouTube videos, Shorts and client interviews</p><h1>'+title+'</h1><p class="lead">Find the original recording beside the guide that helps you evaluate its subject. This inventory includes '+str(len(d['videos']))+' unique YouTube videos discovered across the main channel, testimonial channel and company website.</p><p>Collected November 22, 2026. Videos can subsequently become private or unavailable. Instagram is not included in the completeness count because its public profile required sign-in during collection.</p></div></section><section class="section-sm"><div class="wrap wrap-narrow"><h2>Choose your question</h2><ul>'+''.join('<li><a href="'+path+'#related-video-answers">'+E(re.sub('<[^>]+>','',re.search(r'<h1[^>]*>(.*?)</h1>',(R/path.strip('/')/'index.html').read_text(),re.S).group(1)))+'</a> ('+str(len(vs))+' videos)</li>' for path,vs in groups.items())+'</ul><h2>How should I use this library?</h2><p>Watch the complete recording and check its date. Treat the surrounding questions as an evidence checklist, not as a transcript. Ask for current property records, written service fees and advice specific to your circumstances.</p><h2>Does every video get a separate article?</h2><p>Videos on the same subject share a relevant existing guide. New FAQ guides fill subjects without a suitable page. This keeps related answers and evidence together instead of publishing multiple articles that answer the same question.</p></div></section>'
p=R/hub.strip('/')/'index.html';p.parent.mkdir(exist_ok=True);p.write_text(tpl.page(title=title,description='Browse BNB Accelerator videos and Shorts by buyer question, including financing, underwriting, markets, tax planning and client interviews.',path=hub,body=body,active='/blog/'));created.append(hub)
blog=R/'blog/index.html';s=blog.read_text();intro='<section class="section-sm"><div class="wrap"><h2>Watch BNB Accelerator video answers</h2><p><a href="/blog/video-library/">Browse the complete YouTube video library by buyer question</a>, including Shorts, client interviews and full-length explainers.</p></div></section>';s=s.replace('</main>',intro+'</main>');blog.write_text(s)
# Extend the existing blog sitemap, preserving all prior URLs.
p=R/'sitemap-blog.xml';s=p.read_text();newxml=''.join('<url><loc>'+tpl.SITE+path+'</loc><lastmod>2026-11-22</lastmod></url>' for path in created if tpl.SITE+path not in s);s=s.replace('</urlset>',newxml+'</urlset>');p.write_text(s)
d['coverage']={'uniqueYoutubeVideos':len(d['videos']),'ownerPages':len(groups),'createdFaqPages':created,'modifiedPages':modified,'instagramComplete':False};(R/'_gen/social-video-inventory-2026-11-22.json').write_text(json.dumps(d,indent=2));(R/'_gen/social-video-publish-files.json').write_text(json.dumps([path.strip('/')+'/index.html' for path in modified+created]+['assets/social-video-library.css','blog/index.html','sitemap-blog.xml','_gen/social-video-inventory-2026-11-22.json'],indent=2));print(json.dumps(d['coverage'],indent=2))
