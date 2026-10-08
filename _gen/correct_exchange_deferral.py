"""Scoped existing-owner accuracy correction, not library generation."""
import html, json, math, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SLUG='1031-exchange-short-term-rental'
DESC='Review STR exchange deadlines, investment use, asset-specific depreciation and replacement funding with independent advisers before committing to a purchase.'
p=ROOT/'blog'/SLUG/'index.html'
s=p.read_text()
def replace(old,new,count=1):
 global s
 assert s.count(old)==count,(old,s.count(old))
 s=s.replace(old,new)
replace('An exchange defers the gain, including the portion attributable to prior depreciation. The deferred amount carries into the basis of the replacement property, which means a lower starting basis than a straight purchase at the same price.', '<a href="https://www.irs.gov/publications/p544">IRS Publication 544</a> describes asset-specific exchange treatment and ordinary-income recapture that can arise for section 1245 or 1250 property. Do not assume every cost-segregation component or furnishing qualifies for deferral, even when no cash is received. Ask your CPA to identify each asset, recognized gain, deferred gain and replacement basis before accepting a purchase budget.')
replace('It is workable and it is done routinely, but it is not something to assume. Have your CPA model it before you commit.', 'Provide purchase allocations, prior study reports, depreciation schedules and proposed replacement assets to your CPA. Model the actual exchange basis and any current tax cash requirement before committing; the loan payoff is not adjusted tax basis. Use the <a href="/blog/cost-seg-timing-and-hold-period/">hold-period and disposition-cash guide</a> to separate future proceeds from money available now.')
replace('Yes. Exchange basis rules mean the replacement property starts with a lower basis than a straight purchase at the same price, because the deferred gain carries into it. A study on exchanged property is routine but more complex, and should be modeled before you commit.', 'Yes. Have your CPA establish asset-specific replacement basis, recognized and deferred gain, and any current recapture. Do not assume every cost-segregation component or furnishing is deferred. Fund any current tax obligation independently of restricted exchange proceeds.',2)
replace('Personal use of the property is the most common complication and should be evaluated against the applicable safe harbor conditions with a qualified professional.', 'Evaluate personal use and applicable safe harbor conditions with a qualified professional; this guide does not establish your property’s eligibility.',2)
replace('Personal use is the recurring failure','Review personal use before committing')
replace('The property that a family visits four times a year is the property most likely to create an issue in an exchange.', 'A count of family trips alone does not establish exchange eligibility.')
replace('In practice, exchanges do not fail on paperwork. They fail because the investor spends the first three weeks celebrating a sale and then discovers that finding an underwriteable replacement property in a market they do not know, under a hard deadline, with financing to arrange, is a difficult exercise.', 'Replacement search, documentation, permission checks and financing can each affect whether the planned transaction can close. Put the actual identification and receipt dates beside the outstanding conditions; do not treat a shortlist as a completed exchange.')
replace('The investors who handle this well begin identifying replacement candidates before the relinquished property closes.', 'Consider reviewing replacement candidates before the relinquished property closes.')
replace('It is the single highest leverage change you can make to the process, and it is the reason we start these engagements early.', 'Confirm the engagement’s actual scope and available inventory rather than assuming a compliant replacement is guaranteed.')
replace('the deadlines are the least forgiving in the tax code','the deadlines need advance planning')
replace('<h2 id="faq">Frequently asked questions</h2>', '<p class="small">Depreciation/exchange primary-source section reviewed October 7, 2026 using the currently published IRS Publication 544 (2025), not a newly issued 2026 edition. This scoped correction is not a professional review of every rule in this guide. BNB Accelerator is the interested acquisition-service publisher; this is document-based educational analysis, not tax, legal, lending or personalized investment advice. No exchange, deferral, refund, financing, replacement property or investment result is guaranteed. Share sensitive asset and tax records only through agreed secure channels.</p>\n\n        <h2 id="faq">Frequently asked questions</h2>')
s=re.sub(r'(<meta property="article:published_time" content=")[^"]+',r'\g<1>2026-08-10',s)
for key in ['description','og:description','twitter:description']:
 s=re.sub(r'(<meta (?:name|property)="'+key+r'" content=")[^"]*',lambda m:m[1]+html.escape(DESC,quote=True),s)
body=re.search(r'<article class="article">(.*?)</article>',s,re.S)[1]
words=len(html.unescape(re.sub('<[^>]+>',' ',body)).split());minutes=math.ceil(words/220)
def schema(m):
 d=json.loads(m[2])
 for n in d.get('@graph',[d]):
  if n.get('@type')=='BlogPosting':
   assert n['datePublished']=='2026-08-10'
   n.update(description=DESC,dateModified='2026-10-07',wordCount=words)
 return m[1]+json.dumps(d,indent=2,ensure_ascii=False)+m[3]
s=re.sub(r'(<script[^>]*type="application/ld\+json"[^>]*>)(.*?)(</script>)',schema,s,flags=re.S)
s=re.sub(r'<span>\d+ min read</span>',f'<span>{minutes} min read</span>',s,count=1);p.write_text(s)
p=ROOT/'blog/index.html';a=p.read_text();changed=0
def card(m):
 global changed
 c=m[0]
 if '/blog/'+SLUG+'/' not in c:return c
 changed+=1
 title=html.unescape(re.search(r'<h3><a[^>]*>(.*?)</a></h3>',c,re.S)[1])
 c=re.sub(r'<p>.*?</p>','<p>'+DESC+'</p>',c,count=1,flags=re.S)
 c=re.sub(r'data-search="[^"]*"','data-search="'+html.escape((title+' '+DESC).lower(),quote=True)+'"',c)
 return re.sub(r'<span>\d+ min read</span>',f'<span>{minutes} min read</span>',c)
a=re.sub(r'<article class="post-card".*?</article>',card,a,flags=re.S);assert changed==1;p.write_text(a)
p=ROOT/'sitemap-blog.xml';x=p.read_text();x,n=re.subn(r'(<loc>https://www.bnbaccelerator.com/blog/'+SLUG+r'/</loc>\s*<lastmod>)[^<]+',r'\g<1>2026-10-07',x);assert n==1;p.write_text(x)
print(words,minutes)
