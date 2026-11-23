"""Build one permanent, source-backed page per verified social post.

Inputs stay in _gen; only public articles, caption text, and search metadata ship.
The manifest records caption availability separately from article publication.
"""
from pathlib import Path
from html import escape, unescape
from collections import Counter
import json, re, math, sys, hashlib, xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / '_gen/social-library'
SITE = 'https://www.bnbaccelerator.com'
DATE = '2026-11-22'
HUB = '/learn/'
SIZE = 24
PROFILES = json.loads((DATA / 'companions.json').read_text())
e = lambda value: escape(str(value), quote=True)
link = lambda url, label: '<a href="' + e(url) + '">' + e(label) + '</a>'

IG_OVERRIDES = {
 'DdEgfTJuqwn': ('Short-term rentals and a $120,000 income: the tax questions to ask', 'This Reel introduces a tax-planning discussion for an investor earning $120,000. Income alone does not establish eligibility for a rental loss deduction. The practical question is which rules apply to the property and taxpayer, and what evidence supports the proposed treatment.'),
 'DdEjJGYNcId': ('Investing the first $100,000 in an Airbnb', 'This Reel contrasts deploying the first $100,000 into a rental investment with increasing lifestyle spending. Treat the amount as starting capital to allocate across the purchase, launch and reserve, rather than as a complete property budget by itself.'),
 'C3VAKViP52O': ('How to use BNB Accelerator educational videos', 'This post explains the educational scope of the channel. The acquisition team and independent professional advisers perform different roles. Use the recording to prepare questions, then obtain property-specific conclusions from the people responsible for tax, legal, lending, insurance and construction work.'),
 'Df2qr3XoLMz': ('Why the presentation of a client case study matters', 'This carousel looks back at client-case-study presentation before professional design support. Better formatting should make the underlying evidence easier to read. It should preserve the dates, assumptions, expense definitions and distinction between projections and reported results.'),
 'Df5P1vIka9h': ('Reading BNB Accelerator client results and property stories', 'This carousel brings together reported client experiences, including occupancy, bookings and performance compared with projections. Each example needs its own period and cost context. A strong month, a forward booking calendar and a full year of cash flow answer different questions.'),
 'Df-Ym9TvHdO': ('Large group rentals: matching property size to guest demand', 'The post argues for looking at larger homes that serve groups rather than assuming a small property is the best first purchase. Test the bedroom count, legal capacity, amenities and total cost against comparable group listings before adopting that approach.'),
 'Df-j_2DBeHv': ('Why wealthy investors reconsider traditional real estate purchases', 'This recording uses a broad statement about wealthy investors as the starting point for a real-estate discussion. Evaluate the actual ownership, financing, tax and operating choices rather than treating a headline about wealthy people as a universal investment rule.'),
 'Df-i79BslVZ': ('Evaluating a tax strategy for high-income investors', 'The post introduces a tax-strategy discussion for high-income investors. Compare the projected benefit with the capital committed, the operating risk and the requirements for using the deduction. The relevant result is the taxpayer’s supported outcome, not a label such as “the number one strategy.”'),
 'Df-h6cpPm8f': ('Why an Airbnb property may fail to produce cash flow', 'This recording focuses on the gap between an attractive rental idea and cash that remains after costs. Reconcile the income assumptions, launch improvements, operating scope and financing before concluding that a property will support the intended return.'),
 'DfSXSDLhJbC': ('Who handles furnishing deliveries, assembly and the rest of the launch?', 'The caption walks through work that begins when furniture arrives: deliveries, assembly, staging, painting, outdoor amenities and contractor coordination. A turnkey quote needs to identify which of those tasks are included and which decisions remain with the owner.'),
 'DeXLnIxtrtm': ('Could rental cash flow eventually replace a salary?', 'The post frames retirement around recurring property cash flow and discusses how technology can assist revenue management, guest communication and vendor coordination. A replacement-income target still needs allowances for debt, repairs, reserves and periods of weaker bookings.'),
 'De6ZtUfpAUP': ('Small Airbnbs compete with hotels as well as other rentals', 'The caption explains why the competitive set changes with guest group size. A smaller rental can compete with a hotel room, while a larger home may serve a different need. Compare the actual traveler alternatives rather than relying on the total number of listings in a city.'),
 'DeAPBTgswwW': ('Use comparable scopes to evaluate Airbnb design fees', 'This post compares design pricing by square foot or room count with the use of comparable completed projects. The useful comparison includes scope, furniture quantities, installation, local labor and the guest standard. A pricing unit alone does not establish whether a quote is fair.'),
 'Dd6iUQkN0is': ('When a vacation home becomes part of the reason to book', 'The caption discusses differentiation in premium group travel: the house itself can be part of the experience. Translate that positioning into a specific guest need, comparable listings and an improvement budget before assuming a more memorable design will command a higher rate.'),
 'Dc9S3dxvkEt': ('A rental distribution plan beyond one booking platform', 'This post discusses reaching travelers through multiple booking channels. Broader distribution needs synchronized calendars, consistent rules, clear fee assumptions and an owner-controlled reporting process. Additional exposure is a hypothesis to measure against net bookings, not a guaranteed revenue increase.'),
 'Dfj5uGMvRqo': ('Premium group rentals and the question of market saturation', 'The post contrasts a broad saturation narrative with the performance of larger group homes. Check listing supply and booked revenue in the precise property segment. A high nightly-rate example does not establish the annual occupancy, expenses or return for another property.'),
 'DfnTZpGvdBN': ('Buying before year end: participation and tax planning', 'This post introduces the more-than-100-hour and substantially-all participation concepts. These are distinct tests with different requirements. Establish the actual operating arrangement, rental classification and records with the CPA before using an expected loss in a year-end plan.'),
 'Df5Jiq9P6UQ': ('A $1.3 million Airbnb: separating reported revenue, cash flow and tax savings', 'The caption presents a client example involving a roughly $1.3 million property and reported tax and cash-flow figures. Those numbers describe different measures. Reconcile the period, purchase cash, design spending, debt service and tax assumptions before interpreting an effective out-of-pocket amount.'),
 'DcylXmWvBXi': ('Choose an STR market by its overall tradeoffs', 'The caption explains why strong demand, lower competition and attractive property economics do not always appear together. It uses expensive land in Austin and waterfront Florida as examples of a tradeoff. Compare the complete operating case and capital required rather than selecting a market from one metric.'),
 'Dcnt4PnvLWh': ('Compare two bids before choosing how to build out a rental', 'This post recommends pricing the same build-out through alternative teams before choosing who coordinates the work. Use matching scopes, schedules and exclusions so the difference reflects a real choice. The percentage mentioned in the recording is not a universal measure of DIY savings.'),
 'Df2vA2fv3wG': ('A $600,000 W-2 income and the property-planning conversation', 'This recording uses a $600,000 salary example to discuss real estate and tax planning. High income is a reason to review the full plan with an adviser; it does not establish that a particular purchase, deduction or ownership structure is suitable.'),
 'DdyMvoYvhd5': ('Plan rental design before closing to reduce launch delays', 'The caption describes a launch sequence that begins with design decisions before closing and continues through ordering, delivery, assembly and staging. The approximately 30-day timeline is a described example. Build the schedule around the actual property, supplier lead times, approvals and contractor availability.'),
}
EXCLUDED = {'CWWE4CVgsWj': 'Unrelated personal dance post', 'Cop30qQgKEB': 'Unrelated personal cruise post'}

def clean_title(title):
    title = re.sub(r'(?:\s+#[A-Za-z][\w]*)+\s*$', '', title)
    title = re.sub(r'\s*https?://\S+', '', title)
    title = title.strip(' ]|…')
    return title or 'BNB Accelerator video'

def slug(value):
    return re.sub(r'[^a-z0-9]+', '-', value.lower()).strip('-')[:88].rstrip('-')

def profile_for(title, text=''):
    # A title is the strongest topic signal. Captions resolve vague titles.
    if re.search(r'client (?:review|interview|win)|case.stud|victoria|pruthvi|peter.eck|eino|testimoni|repeat.buyer|what.our.clients|bnb.accelerator.review',title,re.I):
        return next(p for p in PROFILES if p['key']=='case-studies')
    for p in PROFILES:
        if re.search(p['match'], title, re.I):
            if p['key'] != 'process': return p
    for p in PROFILES:
        if p['key'] != 'process' and re.search(p['match'], text[:1800], re.I): return p
    return PROFILES[-1]

def caption_from_snapshot(snapshot):
    # Only use the first publisher caption; never turn visitor comments into copy.
    first = re.search(r'^\s*- time: \d+[wdhms]\s*$', snapshot, re.M)
    if not first: return ''
    block = snapshot[first.end():].split('  - button "Load more comments"')[0].split('  - button "Like"')[0]
    lines=[]
    for line in block.splitlines():
        text=re.match(r'^  - (?:text|generic): (.+)$',line)
        label=re.match(r'^  - link "([#@][^"]+)":',line)
        if text:lines.append(text[1].strip('"'))
        elif label:lines.append(label[1])
    return '\n'.join(lines)

def load_posts():
    inv = json.loads((DATA / 'youtube-inventory.json').read_text())
    sources = json.loads((DATA / 'youtube-sources.json').read_text()) if (DATA / 'youtube-sources.json').exists() else {}
    posts, excluded = [], []
    for kind in ('videos', 'shorts', 'additionalVideos'):
        for original in inv[kind]:
            ident = re.search(r'(?:v=|shorts/)([\w-]{11})', original['url'])[1]
            source = sources.get(ident, {})
            segments = source.get('transcript', [])
            text = ' '.join(row['text'] for row in segments)
            posts.append(dict(id=ident, platform='YouTube', kind=original.get('kind', 'Short' if kind == 'shorts' else 'Video'), title=clean_title(source.get('page_title','').removesuffix(' - YouTube') if kind=='additionalVideos' and source.get('page_title','').endswith(' - YouTube') else original['title']), original_title=source.get('page_title','').removesuffix(' - YouTube') if kind=='additionalVideos' and source.get('page_title','').endswith(' - YouTube') else original['title'], source_url='https://www.youtube.com/watch?v='+ident, segments=segments, source_text=text, caption_status=source.get('status','not_collected'), source_checked=bool(source), source_status=source.get('status'), article_intro='This archived property breakdown is presented for educational review. Asking prices, financing terms, revenue projections and availability in the recording may have changed. Use the written source and companion to review the property-level assumptions rather than as an offer of a currently available home.' if original.get('channel')=='website-linked' else ''))
    for original in json.loads((DATA / 'instagram-evidence.json').read_text()):
        ident = re.search(r'/(?:reel|p)/([^/]+)', original['url'])[1]
        if ident in EXCLUDED:
            excluded.append(dict(id=ident, reason=EXCLUDED[ident])); continue
        snapshot = original['pageText']
        canonical = re.search(r'/((?:bnbaccelerator|nicholaskorom))/(reel|p)/'+re.escape(ident)+r'/', snapshot)
        if not canonical:
            excluded.append(dict(id=ident, reason='Public source did not verify publisher/permalink')); continue
        caption = '' if ident in ('DdElcOBOnwj','DdEgOl0xpel') else caption_from_snapshot(snapshot)
        date = re.search(r'Photo by .*? on ([A-Za-z]+ \d{2}, \d{4})',snapshot) or re.search(r'Video by .*? on ([A-Za-z]+ \d{2}, \d{4})', snapshot)
        if ident in IG_OVERRIDES:
            title, intro = IG_OVERRIDES[ident]
        elif caption:
            title, intro = caption.split('\n')[0][:140], ''
        else:
            date_label = re.search(r'(?:on |· )([A-Za-z]+ \d{1,2},? (?:202\d))', original.get('text',''))
            title = 'BNB Accelerator Instagram '+('post' if canonical[2]=='p' else 'Reel')+' — '+(date_label[1] if date_label else ident)
            intro = 'This page preserves the original BNB business post with its own permanent link and embedded source. The public page did not expose a complete spoken transcript. The companion below provides a framework for researching an STR purchase; watch the original post for its specific discussion.'
        posts.append(dict(id=ident,platform='Instagram',kind='Carousel' if canonical[2]=='p' else 'Reel',title=title,original_title=title,source_url='https://www.instagram.com/'+canonical[1]+'/'+canonical[2]+'/'+ident+'/',segments=[],source_text=caption,caption_status='publisher_caption' if caption else 'caption_not_available',source_checked=True,article_intro=intro))
    seen=set()
    for p in posts:
        key=p['platform']+':'+p['id']; assert key not in seen, key; seen.add(key)
        p['path']=HUB+('youtube/video-' if p['platform']=='YouTube' else 'instagram/post-')+p['id']+'/'
        p['topic']='cash-flow' if p['article_intro'].startswith('This archived property breakdown') else profile_for(p['title'],p['source_text'])['key']
    return posts,excluded

def page(title, description, path, body, schema=None):
    def asset(path):
        return '/'+path+'?v='+hashlib.sha256((ROOT/path).read_bytes()).hexdigest()[:12]
    if 'src="/assets/content-library-data.js"' in body:
        body=body.replace('src="/assets/content-library-data.js"','src="'+asset('assets/content-library-data.js')+'"')
    data = json.dumps(schema or {'@context':'https://schema.org','@type':'CollectionPage','name':title,'url':SITE+path},ensure_ascii=False).replace('<','\\u003c')
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(title)} | BNB Accelerator</title><meta name="description" content="{e(description)}"><meta name="robots" content="index, follow, max-image-preview:large"><link rel="canonical" href="{SITE+path}"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(description)}"><meta property="og:url" content="{SITE+path}"><meta property="og:type" content="article"><meta property="og:image" content="{SITE}/assets/og-image.svg"><meta name="twitter:card" content="summary_large_image"><link rel="icon" href="/assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="{asset("assets/content-library.css")}"><script defer src="{asset("assets/content-library.js")}"></script><script type="application/ld+json">{data}</script></head><body><a class="skip-link" href="#main">Skip to content</a><header></header><main id="main" class="content-library">{body}</main><footer></footer></body></html>'''

def embed(p):
    if p['platform']=='YouTube':
        return f'<div class="cl-player{ " cl-player-short" if p["kind"]=="Short" else ""}"><iframe loading="lazy" src="https://www.youtube-nocookie.com/embed/{e(p["id"])}?rel=0" title="{e(p["title"])}" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div>'
    return f'<div class="cl-player cl-player-instagram"><iframe loading="lazy" src="https://www.instagram.com/p/{e(p["id"])}/embed/captioned/" title="Instagram post: {e(p["title"])}" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div>'

def timestamp(row):
    if row.get('timestamp'): return row['timestamp']
    nums=re.findall(r'(\d+) (hours?|minutes?|seconds?)',row.get('time',''))
    total=sum(int(n)*({'hour':3600,'minute':60,'second':1}[unit.rstrip('s')]) for n,unit in nums)
    return (str(total//3600)+':' if total>=3600 else '')+f'{(total//60)%60:02d}:{total%60:02d}'

def seconds(mark):
    out=0
    for part in mark.split(':'):out=out*60+int(part)
    return out

def written_source(p):
    if p['segments']:
        parts=['<section id="written-version" class="cl-transcript"><h2>Written version of the video</h2><p class="cl-note">Transcribed from the public YouTube captions. Wording, names and figures may contain automatic-caption errors. The original recording remains the source of record. Timestamp links open the corresponding point on YouTube.</p>']
        redacted=False
        for start in range(0,len(p['segments']),6):
            group=p['segments'][start:start+6]; mark=timestamp(group[0]); text=' '.join(x['text'] for x in group)
            before=text
            text=re.sub(r'\b(?:Dr\.?\s*)?Connor\s+Robertson\b|drconnor+robertson|connorrobertson', '[name omitted]', text, flags=re.I)
            text=re.sub(r'\bConnor\b(?!\s+Davis\b)', '[name omitted]', text, flags=re.I)
            policy=json.loads((ROOT/'brand-check-policy.json').read_text())
            for domain in sorted(set(policy['blockedDomains']),key=len,reverse=True):
                text=re.sub(re.escape(domain),'[personal link omitted]',text,flags=re.I)
            for pattern in policy.get('blockedBrandPatterns',[]):
                text=re.sub(pattern,'[unrelated brand omitted]',text,flags=re.I)
            redacted=redacted or before!=text
            parts.append('<p class="cl-transcript-paragraph">'+link(p['source_url']+'&t='+str(seconds(mark))+'s',mark)+' <span>'+e(text)+'</span></p>')
        if redacted:parts.insert(1,'<p class="cl-note">Personal-name or unrelated-brand references are omitted under this site’s editorial policy. The source recording is linked above.</p>')
        return ''.join(parts)+'</section>'
    if p['platform']=='Instagram' and p['source_text']:
        return '<section id="written-version" class="cl-transcript"><h2>Written caption from the original post</h2><p class="cl-note">Publisher caption captured from the public post. This is the caption, rather than a transcript of the spoken audio. Reported figures and opinions belong to the original post.</p>'+''.join('<p>'+e(t)+'</p>' for t in p['source_text'].split('\n') if t.strip())+'</section>'
    if p.get('source_status')=='source_unavailable':
        return '<section id="written-version"><h2>Archived recording</h2><p>YouTube reported that this video was no longer available when checked on November 22, 2026. Its original link and archive page are retained, but a transcript could not be retrieved. The written companion is an editorial property-review guide, rather than a reconstruction of the missing recording.</p></section>'
    return '<section id="written-version"><h2>Original recording</h2><p>A complete public caption transcript was not available for this post during collection. The written companion above is an editorial guide to its topic; it is not a verbatim transcript. '+link(p['source_url'],'Watch the original post')+' for the complete recording.</p></section>'

def card(p):
    visual = f'<img src="https://i.ytimg.com/vi/{e(p["id"])}/hqdefault.jpg" alt="" loading="lazy" width="480" height="360">' if p['platform']=='YouTube' else '<span class="cl-instagram-art" aria-hidden="true">BNB<br>Instagram</span>'
    topic=next(x['name'] for x in PROFILES if x['key']==p['topic'])
    return f'<article class="cl-card"><a class="cl-card-image" href="{e(p["path"])}" tabindex="-1" aria-hidden="true">{visual}</a><div class="cl-card-copy"><p class="cl-label">{e(p["platform"])} · {e(p["kind"])}</p><h2>{link(p["path"],p["title"])}</h2><p>{e(topic)}</p><a class="cl-read" href="{e(p["path"])}">Watch and read<span class="cl-sr">: {e(p["title"])}</span></a></div></article>'

def write(route, html):
    dest=ROOT/route.strip('/')/'index.html';dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(html)

def main():
    posts,excluded=load_posts(); routes=[]
    # Surface every format immediately; preserve source order within each format.
    featured=[p for p in posts if p['platform']=='YouTube' and p['kind']=='Video'][:2]
    featured += [p for p in posts if p['platform']=='YouTube' and p['kind']=='Short'][:2]
    featured += [p for p in posts if p['platform']=='Instagram'][:2]
    featured_paths={p['path'] for p in featured}
    posts=featured+[p for p in posts if p['path'] not in featured_paths]
    youtube_count=sum(p['platform']=='YouTube' for p in posts)
    public=[{k:p[k] for k in ['id','platform','kind','title','path','topic']} for p in posts]
    (ROOT/'assets/content-library-data.js').write_text('window.BNB_CONTENT_LIBRARY='+json.dumps(public,ensure_ascii=False).replace('<','\\u003c')+';\nwindow.dispatchEvent(new Event("bnb-content-ready"));\n')
    previous_path=DATA/'publication-manifest.json'
    previous_routes=set(json.loads(previous_path.read_text()).get('routes',[])) if previous_path.exists() else set()
    for p in posts:
        profile=next(x for x in PROFILES if x['key']==p['topic'])
        intro=p['article_intro'] or profile['lead']
        desc=(p['title']+'. Watch the original '+p['kind'].lower()+' and read the written companion on BNB Accelerator.')[:165]
        related=[x for x in posts if x['topic']==p['topic'] and x['path']!=p['path']][:4]
        trail='<nav class="cl-breadcrumb" aria-label="Breadcrumb">'+link('/','Home')+' / '+link(HUB,'Video and post library')+' / '+e(p['platform'])+'</nav>'
        body='<section class="cl-hero"><div class="wrap">'+trail+'<p class="cl-label">'+e(p['platform'])+' · '+e(p['kind'])+' · '+e(profile['name'])+'</p><h1>'+e(p['title'])+'</h1><p class="cl-lead">'+e(intro)+'</p><p class="cl-meta">BNB Accelerator editorial · Written companion published November 22, 2026</p><nav class="cl-jump" aria-label="On this page">'+link('#watch','Watch the post')+link('#companion','Read the article')+link('#written-version','Source text')+'</nav></div></section>'
        body+='<div class="wrap cl-layout"><div><section id="watch" class="cl-watch"><h2>Watch the original '+e(p['kind'].lower())+'</h2>'+embed(p)+'<p class="cl-source">'+link(p['source_url'],'Open the original on '+p['platform'])+' · If the player is unavailable, use the original source link.</p></section>'
        body+='<article id="companion" class="cl-article"><p class="cl-label">Written companion</p><h2>'+e(profile['name'])+': put the idea into a property decision</h2>'
        if p['article_intro']:body+='<p>'+e(profile['lead'])+'</p>'
        else:body+='<p>The source post is titled “'+e(p['original_title'])+'”. The recording and written source below preserve its discussion. This companion explains how to evaluate the topic in a property purchase or operating plan.</p>'
        for heading,text in profile['sections']:body+='<h3>'+e(heading)+'</h3><p>'+e(text)+'</p>'
        if re.search(r'\$|\d+%|guarantee|no.risk|only.risk|never|always|zero|100.hour|only.required|all.tax.deduct',p['title'],re.I):
            body+='<aside class="cl-evidence-note"><h3>Read the headline with its assumptions</h3><p>The original title is preserved to identify this specific post. A dollar amount, percentage, tax outcome or broad claim in a recording is not a promised result for another buyer. Check the source period, capital invested, expenses, financing and applicable rules before using the example in your own plan.</p></aside>'
        body+='<h3>Continue with the property-specific work</h3><p>Keep the relevant property records, quotes and unanswered questions together. Use '+', '.join(link(u,l) for u,l in profile['links'])+' to turn the discussion into the next decision.</p>'
        if profile['official']:body+='<p class="cl-note">Current reference: '+', '.join(link(u,l) for u,l in profile['official'])+'. Recorded tax discussions may reflect earlier rules; confirm the applicable year and facts with your adviser.</p>'
        body+='</article>'+written_source(p)+'</div><aside class="cl-sidebar"><div class="cl-side-panel"><p class="cl-label">Explore the library</p><h2>Keep learning</h2><p>Browse videos, Shorts, Reels and written posts by subject.</p>'+link(HUB,'Browse all posts')+'<h3>Related posts</h3><ul>'+''.join('<li>'+link(x['path'],x['title'])+'</li>' for x in related)+'</ul></div><div class="cl-side-panel"><h2>Discuss your STR plan</h2><p>Talk through capital, markets, timing and the support you need from acquisition through launch.</p>'+link('/apply/','Book an acquisition call')+'</div></aside></div>'
        schema={'@context':'https://schema.org','@graph':[{'@type':'Article','headline':p['title'],'description':desc,'datePublished':DATE,'dateModified':DATE,'mainEntityOfPage':SITE+p['path'],'author':{'@type':'Organization','name':'BNB Accelerator editorial'},'publisher':{'@type':'Organization','name':'BNB Accelerator','url':SITE},'citation':p['source_url'],'articleSection':profile['name']},{'@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':'Home','item':SITE+'/'},{'@type':'ListItem','position':2,'name':'Video and post library','item':SITE+HUB},{'@type':'ListItem','position':3,'name':p['title'],'item':SITE+p['path']}]}]}
        write(p['path'],page(p['title'],desc,p['path'],body,schema));routes.append(p['path'])
    count=math.ceil(len(posts)/SIZE)
    for n in range(1,count+1):
        route=HUB if n==1 else HUB+'page/'+str(n)+'/'
        pagination='<nav class="cl-pagination" aria-label="Library pages">'+''.join('<span aria-current="page">'+str(i)+'</span>' if i==n else link(HUB if i==1 else HUB+'page/'+str(i)+'/',str(i)) for i in range(1,count+1))+'</nav>'
        filters='<form id="cl-filters" role="search"><label>Search posts<input type="search" id="cl-search" name="q" placeholder="Try cash flow, co-hosts or design"></label><label>Platform<select id="cl-platform"><option value="">All platforms</option><option>YouTube</option><option>Instagram</option></select></label><label>Format<select id="cl-kind"><option value="">All formats</option>'+''.join('<option>'+e(x)+'</option>' for x in ['Video','Short','Reel','Carousel'])+'</select></label><label>Topic<select id="cl-topic"><option value="">All topics</option>'+''.join('<option value="'+e(p['key'])+'">'+e(p['name'])+'</option>' for p in PROFILES)+'</select></label><button type="reset">Reset filters</button></form>'
        body='<section class="cl-hero"><div class="wrap"><nav class="cl-breadcrumb" aria-label="Breadcrumb">'+link('/','Home')+' / Video and post library</nav><p class="cl-label">BNB Accelerator · Watch and read</p><h1>Real estate ideas. Written out.</h1><p class="cl-lead">Explore '+str(len(posts))+' videos and social posts on buying, designing and operating short-term rentals. Every post has its own page, the original embed and a written companion.</p><div class="cl-stats"><span><strong>'+str(youtube_count)+'</strong> YouTube videos and Shorts</span><span><strong>'+str(sum(p['platform']=='Instagram' for p in posts))+'</strong> verified Instagram posts</span><span><strong>'+str(sum(bool(p['segments']) for p in posts))+'</strong> video transcripts</span></div></div></section><section class="wrap cl-directory">'+filters+'<p id="cl-status" role="status" aria-live="polite">Showing posts '+str((n-1)*SIZE+1)+'–'+str(min(n*SIZE,len(posts)))+' of '+str(len(posts))+'. Search covers the complete library.</p><div id="cl-grid" class="cl-grid">'+''.join(card(p) for p in posts[(n-1)*SIZE:n*SIZE])+'</div><p id="cl-empty" hidden>No posts match these filters. Try a broader search or reset the filters.</p><button id="cl-more" type="button" hidden>Show more results</button><div id="cl-pagination">'+pagination+'</div><noscript><p>Use the page links to browse every post. Search and filters require JavaScript.</p></noscript><p class="cl-note">Public-source inventory collected November 22, 2026. Main-channel inventory: 87 videos and 600 Shorts, matching the reported total at collection, plus testimonial-channel uploads and additional website-linked property breakdowns. Instagram includes verified public BNB business posts and relevant collaborations found through public discovery; search indexing does not establish a complete historical Instagram archive.</p></section><script src="/assets/content-library-data.js" defer></script>'
        write(route,page('BNB Accelerator video and post library'+(' — page '+str(n) if n>1 else ''),'Watch BNB Accelerator videos and Instagram posts with written companions, source captions and practical STR investing guides.',route,body));routes.append(route)
    public=[{k:p[k] for k in ['id','platform','kind','title','path','topic']} for p in posts]
    (ROOT/'assets/content-library-data.js').write_text('window.BNB_CONTENT_LIBRARY='+json.dumps(public,ensure_ascii=False).replace('<','\\u003c')+';\nwindow.dispatchEvent(new Event("bnb-content-ready"));\n')
    ns='http://www.sitemaps.org/schemas/sitemap/0.9';ET.register_namespace('',ns)
    sm=ET.Element('{'+ns+'}urlset')
    for route in routes:
        row=ET.SubElement(sm,'{'+ns+'}url');ET.SubElement(row,'{'+ns+'}loc').text=SITE+route;ET.SubElement(row,'{'+ns+'}lastmod').text=DATE
    ET.ElementTree(sm).write(ROOT/'sitemap-content.xml',encoding='utf-8',xml_declaration=True)
    index=ET.parse(ROOT/'sitemap.xml'); doc=index.getroot()
    if SITE+'/sitemap-content.xml' not in {x.text for x in doc.findall('.//{*}loc')}:
        row=ET.SubElement(doc,'{'+ns+'}sitemap');ET.SubElement(row,'{'+ns+'}loc').text=SITE+'/sitemap-content.xml';ET.SubElement(row,'{'+ns+'}lastmod').text=DATE
    index.write(ROOT/'sitemap.xml',encoding='utf-8',xml_declaration=True)
    manifest={'publishedAt':DATE,'posts':len(posts),'platforms':dict(Counter(x['platform'] for x in posts)),'videoTranscripts':sum(bool(x['segments']) for x in posts),'instagramCaptions':sum(x['platform']=='Instagram' and bool(x['source_text']) for x in posts),'routes':routes,'excluded':excluded,'instagramArchiveComplete':False,'items':[{**{k:p[k] for k in ['id','title','platform','kind','path','source_url','caption_status','source_checked']},'articlePublished':True,'embedIncluded':True,'transcriptSegments':len(p['segments'])} for p in posts]}
    (DATA/'publication-manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False))
    for stale in previous_routes-set(routes):
        target=ROOT/stale.strip('/')/'index.html'
        if target.exists():target.unlink()
        parent=target.parent
        while parent!=ROOT/'learn' and parent.is_dir() and not any(parent.iterdir()):
            parent.rmdir();parent=parent.parent
    print(json.dumps({k:v for k,v in manifest.items() if k not in ('routes','items')},ensure_ascii=False))

if __name__=='__main__':main()
