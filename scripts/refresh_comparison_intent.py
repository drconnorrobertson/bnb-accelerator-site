#!/usr/bin/env python3
"""Refresh existing comparison owners; preserve URLs, evidence and publication dates.

Runs before the public build. This is buyer decision support, not a ranked review
or a promise of search placement. Provider re-checks are dated individually.
"""
from pathlib import Path
import html
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / '_gen'))
from expand_competitor_buyers import ALL, EXERCISES
DATE = '2026-11-15'
SITE = 'https://www.bnbaccelerator.com'

# slug: concise search focus, decision question, category
PROFILES = {
 'the-short-term-shop': ('Agents, Fees & Launch', 'Who will coordinate the work between your agent, the revenue analyst and the launch vendors?', 'Acquisition and brokerage'),
 'bnb-mastery': ('Coaching or Acquisition?', 'Do you want to learn co-hosting or investing, or pay a team to coordinate a property purchase?', 'Education and mentorship'),
 'techvestor': ('Portfolio or Direct Ownership?', 'Do you want a portfolio investment or control over one property you select and finance?', 'Ownership and investment models'),
 'rent-to-retirement': ('Turnkey or STR Search?', 'Are you comparing a particular turnkey listing with an STR search service, or comparing two similar rental strategies?', 'Acquisition and brokerage'),
 'kleer-circle': ('Launch & Operating Support', 'Who will cover guest operations after launch, and what changes if you want a manager from day one?', 'Acquisition and brokerage'),
 'elk-ridge-investments': ('Ownership & Operator Roles', 'What property and decision rights do you hold, and which active duties remain with you?', 'Ownership and investment models'),
 'str-search': ('Matching, Fees & Launch', 'What work continues after a property is matched, and who owns each step through opening?', 'Acquisition and brokerage'),
 'str-insights': ('Analysis & Acquisition Scope', 'Which analysis, transaction and setup deliverables are included in the exact package you are quoted?', 'Acquisition and brokerage'),
 'bnb-turnkey': ('Management & Buying Scope', 'Can you choose your operator, and what happens to access and records if management changes?', 'Acquisition and brokerage'),
 'awning': ('Buying & Management Scope', 'Are brokerage, furnishings and ongoing management separate agreements or a combined commitment?', 'Acquisition and brokerage'),
 'rabbu': ('Data or Purchase Support?', 'Do you need a revenue estimate, help finding a property or someone accountable for executing the purchase?', 'Data and property research'),
 'airdna': ('Data Tools or Buying Help?', 'Do you want another research tool or a team to turn property data into an acquisition decision?', 'Data and property research'),
 'alpha-geek-capital': ('Offering or Direct Purchase?', 'Are you comparing an investment offering, education or support to buy an individual property?', 'Ownership and investment models'),
 'robuilt': ('Coaching or Buying Support?', 'Do you want to develop a unique-stay concept yourself or coordinate the purchase of an existing property?', 'Education and mentorship'),
 'michael-elefante': ('Coaching & Buying Support', 'What work will you execute after training, and which deal-specific work would you rather hire?', 'Education and mentorship'),
 'real-estate-robinsons': ('Mentorship & Buying Help', 'Is your immediate need operator training or a team responsible for a live purchase timetable?', 'Education and mentorship'),
 'str-university': ('Courses or Buying Support?', 'Do you need a currently supported course or answers and execution for an active property purchase?', 'Education and mentorship'),
 'str-profit-academy': ('Training or Acquisition?', 'Have you verified a currently offered training product, or do you need purchase coordination now?', 'Education and mentorship'),
 'str-like-the-best': ('Concierge & Buyer Duties', 'Which search and launch tasks will you perform, and which will be delivered under the engagement?', 'Acquisition and brokerage'),
 'arrived': ('Shares or a Whole Property?', 'Is your goal an investment allocation or a whole-property purchase with cash reserved for closing?', 'Ownership and investment models'),
 'ember-flex': ('Shared Use or STR Ownership?', 'How much personal use do you need, and who controls rental dates and operating decisions?', 'Ownership and investment models'),
 'pacaso': ('Co-Ownership or STR Buying?', 'Are you choosing a shared vacation home for personal use or a property intended for a rental business?', 'Ownership and investment models'),
 'roofstock': ('Marketplace or STR Search?', 'Who verifies that the specific property can operate as your intended short-term rental?', 'Data and property research'),
 'stayrnr': ('Renovation & Launch Support', 'Who bears construction delays, approves changes and funds costs before the property opens?', 'Acquisition and brokerage'),
}
EXTRA = {
 'arrived': ('Arrived', '/blog/bnb-accelerator-vs-arrived-str-purchase/'),
 'ember-flex': ('Ember Flex', '/blog/bnb-accelerator-vs-ember-flex-str-purchase/'),
 'pacaso': ('Pacaso', '/compare/bnb-accelerator-vs-pacaso/'),
 'roofstock': ('Roofstock', '/blog/bnb-accelerator-vs-roofstock-str-buyer/'),
 'stayrnr': ('StayRnR', '/blog/bnb-accelerator-vs-stayrnr-str-buyer/'),
 'str-like-the-best': ('STR Like The Best', '/blog/bnb-accelerator-vs-str-like-the-best/'),
}
PROVIDERS = {r[0]: {'name': r[1], 'direct': r[4], 'fit': r[6], 'records': EXERCISES[r[0]][2]} for r in ALL}
for slug, (name, direct) in EXTRA.items():
 PROVIDERS[slug] = {'name': name, 'direct': direct, 'fit': '', 'records': ['Exact ownership and service agreement', 'Itemized cash commitments and timing', 'Named decision and operating responsibilities']}
# Fresh browser checks are restricted to these official pages and modest scope claims.
CHECKED = {
 'the-short-term-shop': ('https://theshorttermshop.com/how-to-buy-a-short-term-rental/', 'Its buying guide describes STR-focused local representation, vendor connections and post-closing systems and training. Compare the agreed services with any separate analysis and launch scope.'),
 'bnb-mastery': ('https://bnbmastery.com/', 'Its homepage offers separate co-hosting and investing education paths and the BNB Tribe community. Choose the relevant program before comparing instruction with contracted purchase execution.'),
 'techvestor': ('https://www.techvestor.com/', 'Its homepage describes passive investment in a portfolio of short-term rentals. Compare investor rights, liquidity and reporting with the responsibilities of buying a particular property; they are different ownership decisions.'),
 'rent-to-retirement': ('https://www.renttoretirement.com/turnkey-properties', 'Its inventory page presents turnkey rental listings and filters for new construction and turnkey rehab. Check the rental strategy and property documents for the actual listing rather than assuming every turnkey rental is an STR.'),
 'kleer-circle': ('https://kleercircle.com/', 'Its homepage describes sourcing, underwriting, transaction coordination, design and listing launch, plus a year-one operating playbook. Ask who will perform daily guest work and what your proposed management arrangement permits.'),
 'elk-ridge-investments': ('https://www.elkridgeinvestments.com/service/', 'Its current page describes an active capital partnership, ownership through the investor\'s holding company and support for sourcing, furnishings and ongoing operations. Do not treat this as a passive fund or assume it is the same contract as a standalone acquisition service.'),
 'str-search': ('https://strsearch.com/', 'Its homepage describes property matching and data analysis, alongside educational resources. Separate acceptance of a match from licensed representation, a completed closing and a guest-ready property.'),
 'str-insights': ('https://www.strinsights.com/introduction', 'Its introduction page advertises property finding, analysis, inspection and negotiation support, design, setup and operations support. Compare the deliverables in the proposed engagement; advertised scope is not proof of completed results.'),
}
SHORTLISTS = {
 'Acquisition and brokerage': ['str-search', 'the-short-term-shop'],
 'Education and mentorship': ['bnb-mastery', 'robuilt'],
 'Ownership and investment models': ['techvestor', 'elk-ridge-investments'],
 'Data and property research': ['airdna', 'rabbu'],
}
ROLES = {
 'str-search': 'Property matching and data analysis; establish which transaction and launch tasks are included.',
 'the-short-term-shop': 'STR-focused local representation, vendor connections and post-closing systems and training.',
 'str-insights': 'Advertised property finding, analysis, purchase coordination and setup support; confirm the proposed package.',
 'bnb-mastery': 'Co-hosting and investing education, plus a community; compare the relevant program and your execution work.',
 'robuilt': 'Education and unique-stay coaching in the dated analysis linked here; verify the current program before enrolling.',
 'techvestor': 'Passive investment in an STR portfolio; compare the offering and investor rights with a direct purchase.',
 'elk-ridge-investments': 'An active partnership with support for sourcing, furnishing and operations; confirm your holding-company rights and duties.',
 'airdna': 'Property and market research tools in the linked analysis; distinguish a data subscription from purchase execution.',
 'rabbu': 'Property research and a marketplace with service options in the linked analysis; verify the level quoted to you.',
}

def esc(s): return html.escape(str(s), quote=True)
def file_for(route): return ROOT / route.strip('/') / 'index.html'
def link(route, text): return f'<a href="{route}">{esc(text)}</a>'
def section(heading, body, ident=''):
 return f'<section class="section-sm"'+(f' id="{ident}"' if ident else '')+f'><div class="wrap wrap-narrow"><h2>{esc(heading)}</h2>{body}</div></section>'

def replace_block(text, marker, body, position='after-hero'):
 pattern=rf'<!-- {marker}:start -->.*?<!-- {marker}:end -->'
 block=f'<!-- {marker}:start -->{body}<!-- {marker}:end -->'
 if re.search(pattern,text,re.S): return re.sub(pattern,lambda _:block,text,flags=re.S)
 if position=='after-hero':
  start=text.index('<h1'); end=text.index('</section>',start)+len('</section>')
  return text[:end]+block+text[end:]
 return text.replace('</main>',block+'</main>',1)

def metadata(text,title,description):
 text=re.sub(r'Updated [A-Za-z]+ \d{1,2}, \d{4}', 'Updated November 15, 2026', text)
 text=re.sub(r'<title>.*?</title>','<title>'+esc(title)+'</title>',text,count=1,flags=re.S)
 for key,value in [('description',description),('og:title',title),('og:description',description),('twitter:title',title),('twitter:description',description)]:
  pattern=r'<meta\s+(?:name|property)="'+key+r'"\s+content="[^"]*"\s*/?>'
  text,n=re.subn(pattern,lambda _:f'<meta '+('property' if key.startswith('og:') else 'name')+f'="{key}" content="{esc(value)}">',text,count=1)
  if not n:raise ValueError(f'Missing metadata: {key}')
 def schema(m):
  doc=json.loads(m[1])
  def walk(node):
   if isinstance(node,dict):
    types=node.get('@type',[]); types=[types] if isinstance(types,str) else types
    if set(types)&{'Article','BlogPosting','WebPage','CollectionPage'}:
     if 'headline' in node:node['headline']=title
     if 'name' in node:node['name']=title
     if 'description' in node:node['description']=description
     if 'dateModified' in node:node['dateModified']=DATE
    if 'BreadcrumbList' in types and node.get('itemListElement'):
     node['itemListElement'][-1]['name']=title
    for v in node.values():walk(v)
   elif isinstance(node,list):
    for v in node:walk(v)
  walk(doc)
  return '<script type="application/ld+json">'+json.dumps(doc,ensure_ascii=False,indent=2)+'</script>'
 text=re.sub(r'<script type="application/ld\+json">(.*?)</script>',schema,text,flags=re.S)
 return text

def read_source_note(slug):
 if slug not in CHECKED:return '<p class="small text-muted">The detailed provider-source dates below apply to the existing analysis. Request current terms before choosing a service. BNB Accelerator publishes this comparison and sells acquisition support.</p>'
 url,summary=CHECKED[slug]
 return f'<p><strong>Published scope checked November 15, 2026:</strong> {esc(summary)} {link(url,"Read the provider source")}.</p><p class="small text-muted">Public-material review, not customer testing or verified investment results. BNB Accelerator is the commercially interested publisher. Fees and inclusions require a current written proposal.</p>'

def shortlist(slug):
 group=PROFILES[slug][2]; peers=[s for s in SHORTLISTS[group] if s!=slug]
 if len(peers)<2:peers+=[s for s in ['str-insights','str-search','robuilt'] if s!=slug and s not in peers][:2-len(peers)]
 # A research tool and an execution service are explicitly different choices.
 rows=[('BNB Accelerator', '/how-it-works/', 'Acquisition and launch coordination for a property you approve, including sourcing and underwriting.', 'Request the written scope and fee. Identify separate vendor bills, purchase decisions and the operating agreement.')]
 for peer in peers:
  p=PROVIDERS[peer]
  rows.append((p['name'],p['direct'],ROLES[peer],PROFILES[peer][1]))
 body='<p>'+esc(PROFILES[slug][1])+' Start with these named research paths; inclusion is not a ranking or a claim of equivalent service.</p>'
 body+='<div class="bc-table-scroll" role="region" aria-label="Alternative buying paths" tabindex="0"><table><caption>Named alternatives and the work to compare</caption><thead><tr><th scope="col">Path</th><th scope="col">Published role</th><th scope="col">What to verify</th></tr></thead><tbody>'
 for name,route,task,duty in rows:body+=f'<tr><th scope="row">{link(route,name)}</th><td>{esc(task)}</td><td>{esc(duty)}</td></tr>'
 body+='</tbody></table></div>'
 body+='<p>'+link(PROVIDERS[slug]['direct'],'Compare BNB Accelerator vs '+PROVIDERS[slug]['name'])+' for the direct two-provider decision. '+link('/compare/alternatives/','Browse all company alternatives')+' to build a wider shortlist.</p>'
 return body

def refresh_provider(slug):
 p=PROVIDERS[slug];name=p['name'];focus,question,group=PROFILES[slug]
 alt='/compare/alternatives-to-'+slug+'/'
 path=file_for(alt);text=path.read_text()
 title=f'{name} Alternatives: {focus}'
 if slug=='michael-elefante':title='Michael Elefante Alternatives: Coaching & Buying Support'
 desc=f'Compare alternatives to {name} by '+{'Acquisition and brokerage':'search, fees, launch work and management handoff.','Education and mentorship':'coaching, deal feedback and contracted purchase support.','Ownership and investment models':'ownership rights, operating work, cash commitments and exit terms.','Data and property research':'research tools, property analysis and purchase execution.'}[group]
 text=metadata(text,title,desc)
 # Answer the alternatives intent before the long contract exercises.
 text=re.sub(r'(<h1\b[^>]*>).*?(</h1>)',lambda m:m[1]+esc(name+' Alternatives')+m[2],text,count=1,flags=re.S)
 lead=f'Compare BNB Accelerator with other buying paths before choosing {name}. '+question
 text=re.sub(r'(<p class="lead">).*?(</p>)',lambda m:m[1]+esc(lead)+m[2],text,count=1,flags=re.S)
 content=section('Compare alternatives to '+name,shortlist(slug),'compare-options')
 content+=section('Check the scope before you shortlist',read_source_note(slug))
 text=replace_block(text,'comparison-intent',content)
 # Keep the older source paragraph from contradicting a fresh public-page check.
 if slug in CHECKED:
  text=re.sub(r'<section class="section-sm"><div class="wrap wrap-narrow"><h2>Start with the outcome you need</h2>.*?</div></section>', '', text, count=1, flags=re.S)
 if slug=='elk-ridge-investments':text=correct_elk(text)
 path.write_text(text)
 # Existing direct owner stays in its established compare or blog location.
 direct=p['direct'];path=file_for(direct);text=path.read_text()
 dtitle='BNB Accelerator vs '+name+': '+focus
 if len(dtitle)>88:dtitle='BNB Accelerator vs '+name
 ddesc=f'Compare BNB Accelerator and {name}: '+question+' Review written scope and fees.'
 text=metadata(text,dtitle,ddesc)
 duties=''.join('<li>'+esc(x)+'</li>' for x in p['records'])
 body='<p>'+esc(question)+'</p><p><strong>BNB Accelerator:</strong> evaluate a client-approved property purchase with acquisition and launch coordination. Confirm what is performed, coordinated or paid separately in '+link('/pricing/','the written scope and fee quote')+'.</p>'
 if slug in CHECKED:body+=read_source_note(slug)
 else:body+='<p><strong>'+esc(name)+':</strong> use the dated, source-linked analysis below and the exact product proposed to you. A provider name alone does not identify the work, ownership or support you are buying.</p>'
 body+='<h3>Bring these records to the comparison</h3><ul>'+duties+'</ul><p>'+link(alt,name+' alternatives')+' compares the wider shortlist. '+link('/guides/str-service-responsibility-matrix/','Map the agreed responsibilities')+' when two proposals are already on the table.</p>'
 text=replace_block(text,'comparison-intent',section('The decision before the fee',body,'compare-options'))
 if slug=='elk-ridge-investments':text=correct_elk(text)
 path.write_text(text)
 return [alt,direct]

def correct_elk(text):
 replacements={
  'Elk Ridge describes capital allocated into professionally managed STR real estate, acquisition through operation and exit, ownership participation, reporting and K-1 issuance. The specific legal ownership, voting rights and exit terms must come from the actual offering documents.':CHECKED['elk-ridge-investments'][1],
  'Investors who want a sponsor to select and operate assets.':'Investors evaluating an active partnership with operating support; confirm the property rights and work expected of each partner.',
  'A managed STR offering':'An active STR partnership',
  'managed STR ownership participation':'active STR partnership with operating support',
  'Elk Ridge’s <a href="https://www.elkridgeinvestments.com/service/" rel="noopener noreferrer">service page</a> describes sourcing, renovation, furnishing, operations, investor reporting and exit planning.':'Elk Ridge’s <a href="https://www.elkridgeinvestments.com/service/" rel="noopener noreferrer">current service page</a> describes sourcing, furnishing and support for ongoing operations, with an active role retained by the investor.',
 }
 for a,b in replacements.items():text=text.replace(a,b)
 text=text.replace('Do you want managed ownership participation or to approve and buy your own first STR?', PROFILES['elk-ridge-investments'][1])
 # Supersede the older partner-page summary rather than mixing review dates.
 text=re.sub(r'<section class="section-sm"><div class="wrap wrap-narrow"><h2>What Elk Ridge currently describes</h2>.*?</div></section>', '', text, flags=re.S)
 return text

def hub(kind):
 route='/compare/alternatives/' if kind=='alternatives' else '/compare/'
 path=file_for(route);text=path.read_text();oldmain=re.search(r'<main\b[^>]*>(.*?)</main>',text,re.S)[1]
 title='STR Company Alternatives: 24 Guides by Service & Ownership' if kind=='alternatives' else 'Compare STR Acquisition Companies, Services & Alternatives'
 heading='Find the right STR company alternative' if kind=='alternatives' else 'Compare the help you need to buy an STR'
 lead='Choose a service model, then compare providers on the work, cash and decisions left with you.'
 body=f'<section class="hero hero-page"><div class="wrap"><div class="hero-inner"><span class="eyebrow">STR buyer comparison library</span><h1>{heading}</h1><p class="lead">{lead}</p><div class="btn-row"><a class="btn btn-accent" href="/how-it-works/">Review BNB Acquisition Support</a><a class="btn btn-ghost-light" href="/tools/first-str-purchase-budget/">Check My Purchase Budget</a></div></div></div></section>'
 if kind=='alternatives':
  body+=section('Choose the provider you are researching','<p>Find the company or program below to compare other purchase paths. Each alternatives guide explains the ownership, work and fee questions behind the shortlist. For a direct BNB Accelerator comparison, use '+link('/compare/','the comparison directory')+'.</p><p>These groups organize the decision, not provider quality. BNB Accelerator publishes the library and sells acquisition services. The individual guides identify their sources and review dates.</p>')
 else:
  body+=section('Start with your decision','<p><strong>Building a shortlist?</strong> Use '+link('/compare/alternatives/','the company alternatives guides')+'. <strong>Choosing between two proposals?</strong> Use the direct comparisons below. <strong>Ready to sign?</strong> Map fees and handoffs in the '+link('/guides/str-service-responsibility-matrix/','responsibility worksheet')+'. A course, research subscription, investment interest and acquisition engagement are different purchases.</p><p>BNB Accelerator publishes these guides and offers acquisition services. This is a buyer research library, not independent customer testing or an investment-performance ranking. Each provider analysis retains its own source-review date.</p>')
 groups=list(SHORTLISTS)
 body+='<section class="section-sm"><div class="wrap"><nav class="bc-jump" aria-label="Provider categories">'+''.join(link('#provider-group-'+str(i),g) for i,g in enumerate(groups))+'</nav></div></section>'
 used=set()
 for i,g in enumerate(groups):
  body+=f'<section class="section-sm bc-category" id="provider-group-{i}"><div class="wrap"><h2>{esc(g)}</h2>'+('<ul class="bc-alternative-list">' if kind=='alternatives' else '<div class="bc-grid">')
  for slug,(focus,q,group) in PROFILES.items():
   if group!=g:continue
   p=PROVIDERS[slug];alt='/compare/alternatives-to-'+slug+'/';used.update([alt,p['direct']])
   if kind=='alternatives':
    body+='<li>'+link(alt,p['name']+' alternatives')+'<br><span class="text-muted">'+esc(focus)+'</span></li>'
   else:
    body+=f'<article class="bc-option"><span class="eyebrow">{esc(focus)}</span><h3>{esc(p["name"])}</h3><p>{esc(q)}</p><div class="bc-card-links">{link(p["direct"],"BNB Accelerator vs "+p["name"])}{link(alt,p["name"]+" alternatives")}</div></article>'
  body+=('</ul>' if kind=='alternatives' else '</div>')+'</div></section>'
 # Keep discovery of existing contract guides, market pairs and other comparisons.
 remaining=[]
 for href in dict.fromkeys(re.findall(r'href="(/(?:compare|blog|guides)/[^"?#]*/?)"',oldmain)):
  if href in used or href in ['/compare/','/compare/alternatives/']:continue
  f=file_for(href)
  if f.is_file():
   name=html.unescape(re.sub('<[^>]+>','',re.search(r'<h1\b[^>]*>(.*?)</h1>',f.read_text(),re.S)[1]))
   remaining.append((href,name))
 if kind!='alternatives':
  body+=section('More comparisons and proposal worksheets','<details><summary>Browse existing comparisons, contract questions and market guides</summary><ul class="bc-alternative-list">'+''.join('<li>'+link(u,n)+'</li>' for u,n in remaining)+'</ul></details>')
 body+=section('Compare a complete acquisition proposal','<p>Use the same property, financing assumptions and opening plan in each proposal. Record charges due before closing, work paid separately, retained reserves and the operating agreement. Use '+link('/pricing/','BNB Accelerator pricing and scope')+' alongside '+link('/reviews/','reviews and evidence sources')+' and '+link('/case-studies/','individual property examples')+'.</p><p>'+link('/apply/','Discuss your STR acquisition plan')+'</p>')
 if kind!='alternatives':
  body+=section('Check the service against your purchase','<p>Use the '+link('/buy-a-short-term-rental/','STR purchase roadmap')+' to identify the work you need. Review '+link('/research-bnb-accelerator/','BNB Accelerator company evidence')+' and '+link('/tools/str-downside-calculator/','test a downside purchase scenario')+' before committing to a provider.</p>')
 text=re.sub(r'(<main\b[^>]*>).*?(</main>)',lambda m:m[1]+body+m[2],text,count=1,flags=re.S)
 description=('Explore alternatives to 24 STR companies, courses and platforms. Compare named buying paths by ownership, fees, buyer work and operating responsibilities.'
              if kind=='alternatives' else
              'Compare BNB Accelerator with STR providers on sourcing, analysis, fees and launch support. Find direct comparisons, alternatives and proposal worksheets.')
 text=metadata(text,title,description)
 # Navigation order is not a quality ranking. Visible links and structured data match.
 schema={'@context':'https://schema.org','@type':'ItemList','name':heading,'itemListOrder':'https://schema.org/ItemListUnordered','numberOfItems':len(PROFILES),'itemListElement':[{'@type':'ListItem','position':i+1,'name':PROVIDERS[slug]['name'],'url':SITE+'/compare/alternatives-to-'+slug+'/'} for i,slug in enumerate(PROFILES)]}
 text=re.sub(r'<!-- comparison-list:start -->.*?<!-- comparison-list:end -->','',text,flags=re.S)
 text=text.replace('</head>','<!-- comparison-list:start --><script type="application/ld+json">'+json.dumps(schema)+'</script><!-- comparison-list:end --></head>')
 path.write_text(text)
 return route

def main():
 changed=[]
 for slug in PROFILES:changed.extend(refresh_provider(slug))
 changed.extend([hub('alternatives'),hub('compare')])
 for p in ROOT.glob('sitemap-*.xml'):
  def stamp(m):
   block=m[0];loc=re.search(r'<(?:\w+:)?loc>(.*?)</(?:\w+:)?loc>',block)
   if loc and loc[1].removeprefix(SITE) in changed:return re.sub(r'(<(?:\w+:)?lastmod>).*?(</(?:\w+:)?lastmod>)',lambda x:x[1]+DATE+x[2],block)
   return block
  p.write_text(re.sub(r'<(?:\w+:)?url\b[^>]*>.*?</(?:\w+:)?url>',stamp,p.read_text(),flags=re.S))
 print(f'Comparison intent: {len(set(changed))} existing owners; 24 alternatives, 24 direct comparisons, two hubs. No new URLs.')

if __name__=='__main__':main()
