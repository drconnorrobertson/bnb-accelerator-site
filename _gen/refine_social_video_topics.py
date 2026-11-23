from pathlib import Path
import json,re,html,collections
R=Path(__file__).resolve().parents[1];E=html.escape
rules=[
('blog/airbnb-arbitrage-vs-ownership',r'\barbitrage\b','What should you compare before choosing arbitrage or ownership?','Identify who owns the home, who controls the lease, who bears furnishing and operating costs, and what happens if rental use is restricted. Compare the actual contracts and capital at risk instead of treating the two models as identical.'),
('blog/llc-for-short-term-rental',r'\bllc\b','What should be resolved before creating or using an entity for an STR?','Discuss ownership, financing, insurance, banking and the rental operation with your advisers. Entity formation does not itself establish rental permission or a specific tax outcome. Confirm how the actual property and agreements will be held.'),
('blog/1031-exchange-short-term-rental',r'1031','How should a buyer use an exchange video?','Use the recording to prepare questions for the qualified intermediary and tax adviser. Review the actual transaction sequence, eligibility, deadlines, replacement property and financing before committing. A general video cannot establish that your exchange qualifies.'),
('blog/depreciation-recapture-str',r'recapture','What should you evaluate before relying on a depreciation example?','Ask your tax adviser to model the holding period and potential disposition as well as the first year. Keep the property basis, study, depreciation schedules and transaction records available for that review.'),
('blog/cost-segregation-airbnb',r'cost.?segregation|cost seg\b','What evidence belongs beside a cost segregation video?','Request the actual study scope, property information, fee, timing and deliverables. Have the filing professional evaluate the study and your circumstances. A cost segregation illustration is not a completed tax return or an assured refund.'),
('blog/spouse-material-participation',r'spouse|wife|husband|married|couple','How should a household turn these videos into a work plan?','Identify each person’s actual operating tasks and available time. Keep records of the work performed and ask your adviser to evaluate the applicable requirements. A headline about household participation cannot settle eligibility.'),
('blog/material-participation-str',r'material participation|100.?hour|500.?hour|750.?hour|participation log','What should you verify after watching a participation video?','Document the actual activities, dates, time and responsible people. Separate owner work from work performed by other individuals and ask your tax adviser which test is relevant. Older videos may simplify conditions that matter in your case.'),
('blog/str-cash-out-refinance',r'refinanc|\brefi\b','What should you check before assuming a refinance will fund another purchase?','Obtain current lender terms and a realistic valuation, then include closing costs, payments and reserves in the model. Test a case in which the refinance is smaller, delayed or unavailable instead of treating it as committed funding.'),
('blog/str-appraisal-income-approach',r'apprais','What should you ask about the valuation shown in a video?','Identify whether the number is an appraisal, broker opinion, seller expectation or hypothetical value. Ask the lender which valuation and property evidence it will accept. A rental income projection does not by itself establish lendable value.'),
('blog/str-seller-credit-vs-price-reduction',r'seller credit|closing credit','How should you compare a seller credit with a lower purchase price?','Use the actual loan and contract terms to compare cash to close and future payments. Ask the lender and transaction professionals which credit limits and uses apply. A headline saving is not necessarily cash the buyer can receive.'),
('blog/negotiating-airbnb-purchase',r'negotiat','What should you use to support an STR purchase negotiation?','Bring verified property condition, operating records, comparable sales and current financing information. Decide which contract protections matter before trading them for price. Record the final terms in the signed agreement rather than relying on a conversation.'),
('blog/reading-an-hoa-declaration',r'\bhoa\b|homeowner.?association','What should be verified about an HOA before buying?','Obtain the governing documents, amendments, rental restrictions, fees and applicable approval requirements. Confirm the rules for the exact property and proposed use with the appropriate professionals before treating an existing listing as permission.'),
('blog/str-regulations-before-you-buy',r'permit|compliance|regulat|ordinance|city rules|state.?laws|different states','How should you verify a regulatory claim in a video?','Check the current jurisdiction, exact address, intended stay length and any private restrictions. Retain the underlying rules and written findings where available. A broad market statement does not establish that a particular buyer can operate a particular property.'),
('blog/str-insurance-quote-before-purchase-offer',r'insurance','What should you confirm before using an insurance example?','Request a quote for the exact property, ownership, rental use and amenities. Review coverage, exclusions, deductibles and business-income terms with a licensed professional. A generic premium estimate is not a policy offer.'),
('blog/str-bookkeeping-records',r'quickbooks|bookkeep|accounting','Which records should support the figures in these videos?','Reconcile reservations, platform statements, bank deposits and expenses for the same period. Separate owner contributions and debt activity from rental operating results. Keep original records so your accountant can review the classifications.'),
('blog/airbnb-cleaning-turnover-systems',r'cleaner|cleaning|turnover','What needs to happen between one guest leaving and the next arriving?','Assign cleaning, restocking, maintenance escalation and a final readiness check. Confirm how completion is verified and who provides backup when a cleaner cannot attend. A scheduled task does not establish that the home is ready.'),
('blog/airbnb-vs-long-term-rentals',r'long.?term rental','What should you compare between short- and long-term rental models?','Use a consistent property budget and include rent assumptions, vacancy, turnovers, utilities, management and financing. Review the contracts and legal use for each model. A higher gross rental figure does not necessarily mean more owner cash.'),
('blog/airbnb-vs-vrbo-vs-booking',r'vrbo|booking\.com|google.*(?:booking|rental)','How should you compare rental booking channels?','Use the applicable partner terms and a sample booking to compare fees, cancellations, payouts and guest communication. Confirm calendar coordination and who manages the listing. More distribution does not guarantee more profitable reservations.'),
('blog/airbnb-cash-on-cash-return',r'cash.?on.?cash|internal rate of return|\birr\b','How should you check the return calculation in a clip?','Identify the cash invested, the cash-flow period and the expenses and debt payments included. Keep a cash-on-cash calculation separate from an internal rate of return, which depends on the timing of all relevant cash flows and any exit assumptions.'),
('blog/airbnb-occupancy-rates-explained',r'occupancy','What should you compare alongside occupancy?','Use the same reporting period and document available nights, booked nights, rate and revenue definitions. Review blocked nights and property differences. High occupancy alone does not establish operating profit or the right purchase price.'),
('blog/airbnb-dynamic-pricing-tools',r'dynamic pric|pricing software|pricing tool','What should you test before choosing a pricing tool?','Confirm compatible channels, minimum and maximum rates, owner overrides, billing and support. Test the workflow on the actual property calendar and compare collected revenue after costs. A price recommendation does not guarantee a booking.'),
('blog/airbnb-pricing-strategy',r'nightly rate|underpric|overpric|pricing|price per night','How should you evaluate a nightly-rate example?','Match the property type, season, guest capacity and booking window. Compare net collected revenue and expenses over the same dates. An unusually strong night is not a reliable average for the year.'),
('blog/airbnb-amenities-that-increase-revenue',r'amenit|design|furnish|upgrade|hot tub|pool|golf simulator|game room|sofa|cover photo','What should you budget before copying a property upgrade?','Obtain an installed cost and operating estimate, compare similar rentals and model a case without additional revenue. Include carrying costs and opening delays. An attractive improvement may still fail to justify its cost for a particular property.'),
('blog/str-management-video-questions',r'property manager|management|co.?host|passive|hands.?off','What should you confirm about the operator behind a hands-off claim?','Identify the contracting manager, fee base, guest support, maintenance authority, owner records and exit terms. Assign physical work and emergency coverage. An acquisition introduction does not replace the separate operating agreement.'),
('blog/how-to-get-5-star-reviews',r'5.?star|guest review|reviews compound','What should a host take from a review-related video?','Focus on accurate listing information, a ready property, clear communication and prompt issue handling. Read the applicable platform policies and use guest feedback to identify operating problems. A recorded result does not promise the same review outcome.')]
p=R/'_gen/social-video-inventory-2026-11-22.json';d=json.loads(p.read_text());bp=R/'_gen/social-video-blocks.json';old=json.loads(bp.read_text());cards={}
for block in old.values():
 for c in re.findall(r'<article class="social-video-card">.*?</article>',block,re.S):
  m=re.search(r'data-video-id="([\w-]{11})"',c)
  if m:cards[m.group(1)]=c
spec={}
for line in (R/'_gen/social-video-topics.tsv').read_text().splitlines():
 k,path,terms,q,a=line.split('|');spec[path]=(q,a)
for path,pattern,q,a in rules:assert (R/path/'index.html').exists(),path;spec['/'+path+'/']=(q,a)
changed=0
for v in d['videos']:
 if v.get('topic') in ['property','victoria','testimonials'] or v['channel']=='website-linked':continue
 for path,pattern,q,a in rules:
  if re.search(pattern,v['title'],re.I):
   path='/'+path+'/';changed+=v['ownerPath']!=path;v['ownerPath']=path;break
groups=collections.defaultdict(list)
for v in d['videos']:groups[v['ownerPath']].append(v)
blocks={}
for path,vs in groups.items():
 # Property-specific block and its guidance are preserved.
 if all(v.get('topic')=='property' for v in vs) and path in old:blocks[path]=old[path];continue
 q,a=spec.get(path,('How should you evaluate the experience shown in a video?','Watch the complete recording and request the underlying property records. Client accounts and marketing examples are specific to their circumstances, not independently established typical results. Compare the reporting period, expenses, funding and responsibilities before applying an example.'))
 cs=''.join(cards[v['id']] for v in vs if v['id'] in cards)
 blocks[path]='<!-- social-video-library:start --><section class="section-sm social-video-library" id="related-video-answers"><div class="wrap wrap-narrow"><p class="eyebrow">Watch the source</p><h2>Related BNB Accelerator video answers</h2><p>Original channel titles are shown below. Check the recording date and context. Reported income, investment examples and tax illustrations do not establish typical or guaranteed outcomes.</p><h3>'+E(q)+'</h3><p>'+E(a)+'</p><div class="social-video-grid">'+cs+'</div><p><a href="/blog/video-library/">Browse every discovered video by topic</a></p></div></section><!-- social-video-library:end -->'
files=[]
for path in set(old)|set(blocks):
 dest=R/path.strip('/')/'index.html';s=dest.read_text();s=re.sub(r'<!-- social-video-library:start -->.*?<!-- social-video-library:end -->','',s,flags=re.S)
 if path in blocks:
  s=s.replace('</main>',blocks[path]+'</main>')
  if '/assets/social-video-library.css' not in s:s=s.replace('</head>','<link rel="stylesheet" href="/assets/social-video-library.css"></head>')
  if '/assets/video-facade.v1.js' not in s:s=s.replace('</body>','<script src="/assets/video-facade.v1.js" defer></script></body>')
 dest.write_text(s);files.append(str(dest.relative_to(R)))
d['coverage']['ownerPages']=len(groups);d['coverage']['modifiedPages']=list(groups);d['coverage']['topicRefinement']={'reassignedVideos':changed,'specificTopicRules':len(rules)};p.write_text(json.dumps(d,indent=2));bp.write_text(json.dumps(blocks,indent=2))
hub=R/'blog/video-library/index.html';s=hub.read_text();items=[]
for path,vs in groups.items():
 text=(R/path.strip('/')/'index.html').read_text();m=re.search('<h1[^>]*>(.*?)</h1>',text,re.S);title=html.unescape(re.sub('<[^>]+>','',m.group(1)))
 items.append('<li><a href="'+path+'#related-video-answers">'+E(title)+'</a> ('+str(len(vs))+' videos)</li>')
s=re.sub(r'(<h2>Choose your question</h2>)<ul>.*?</ul>',lambda m:m.group(1)+'<ul>'+''.join(items)+'</ul>',s,flags=re.S);hub.write_text(s)
files+=['_gen/social-video-inventory-2026-11-22.json','_gen/social-video-blocks.json','blog/video-library/index.html'];(R/'_gen/social-refinement-publish-files.json').write_text(json.dumps(sorted(set(files)),indent=2));(R/'_gen/social-topic-refinement-rules.json').write_text(json.dumps(rules,indent=2));print(json.dumps({'reassigned':changed,'ownerPages':len(groups),'videos':len(d['videos'])}))
