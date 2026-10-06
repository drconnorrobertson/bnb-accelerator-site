// Contextual purchase paths for existing articles; preserve their original subject.
import { existsSync } from 'node:fs';
const esc=s=>s.replace(/&/g,'&amp;').replace(/"/g,'&quot;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
const stages={
 finance:{name:'Budget and financing',decision:'Confirm a financing path for the property before treating an approval or projected rent as purchasing power.',evidence:'Bring your available purchase cash, proposed ownership, property type and lender conditions. Separate the down payment, closing costs, setup budget and reserves.',links:[['/blog/str-mortgage-preapproval-before-property/','Set lender guardrails before searching'],['/financing/','Compare STR purchase financing'],['/tools/first-str-purchase-budget/','Calculate the cash needed to buy']]},
 rules:{name:'Permission and transfer',decision:'Verify what you, as the new owner, would be allowed to operate at the exact address.',evidence:'Bring the parcel address, jurisdiction, association documents and seller approvals. Identify which permissions require new applications or written confirmation before valuing future bookings.',links:[['/blog/str-regulations-before-you-buy/','Check the rules before buying'],['/blog/permits-that-do-not-transfer/','Review permit and HOA transfer'],['/blog/str-due-diligence-checklist/','Build a purchase diligence checklist']]},
 tax:{name:'Tax coordination before purchase',decision:'Evaluate the acquisition on its property economics, then confirm the tax assumptions with your own adviser.',evidence:'Bring the proposed purchase and opening dates, ownership plan, intended personal use and operating responsibilities. Keep a tax illustration separate from rental cash flow and financing.',links:[['/tax-strategy/','Review the STR tax-strategy framework'],['/tools/first-str-purchase-budget/','Budget the acquisition independently of tax savings'],['/blog/str-purchase-to-launch-timeline/','Plan purchase-to-launch timing']]},
 revenue:{name:'Seller evidence and underwriting',decision:'Translate the article’s revenue or pricing topic into a supportable purchase price and downside case.',evidence:'Bring listing-specific seller records, comparable properties, quoted operating costs and proposed debt terms. Separate historical income, future bookings and estimates before comparing returns.',links:[['/blog/reconcile-airbnb-payout-export/','Verify seller Airbnb income'],['/blog/compare-two-str-properties-before-offer/','Compare properties before an offer'],['/blog/str-maximum-offer-price-from-revenue/','Set a maximum offer from the numbers']]},
 market:{name:'Property search and market selection',decision:'Use market research to shortlist properties, then test the address rather than buying from a city ranking.',evidence:'Bring your purchase budget, preferred markets and two or three listing links. Compare guest appeal, legal use, seasonal demand and operating costs for each property.',links:[['/blog/how-to-find-str-properties-for-sale/','Find STR properties for sale'],['/blog/short-term-rental-buy-box/','Write your property buy box'],['/blog/compare-two-str-properties-before-offer/','Compare the shortlisted properties']]},
 contract:{name:'Offer and closing preparation',decision:'Resolve the open purchase conditions before committing to a price or closing date.',evidence:'Bring the listing, proposed price, evidence gaps, financing conditions and transaction timeline. Discuss property-specific contract questions with the qualified professionals handling the purchase.',links:[['/blog/str-maximum-offer-price-from-revenue/','Work out the offer ceiling'],['/blog/negotiating-airbnb-purchase/','Prepare an STR purchase negotiation'],['/blog/str-due-diligence-checklist/','Track diligence before closing']]},
 service:{name:'Choose acquisition support',decision:'Compare the written service scope with the work and responsibilities your purchase actually requires.',evidence:'Bring your budget, buying timeline and any property shortlist. Ask who owns sourcing, underwriting, diligence, closing coordination and launch, and which fees or vendor costs are excluded.',links:[['/done-for-you-airbnb/','Review done-for-you acquisition support'],['/pricing/','Understand service fees and purchase costs'],['/reviews/','Check public review sources']]},
 operations:{name:'Setup and operating handoff',decision:'Price the operating requirements before buying, rather than discovering them after closing.',evidence:'Bring the property’s condition, included inventory, vendor quotes and proposed management arrangement. Separate one-time setup costs from ongoing expenses and fund the period before the first guest.',links:[['/blog/buy-existing-airbnb-vs-start-from-scratch/','Compare an existing Airbnb with a new setup'],['/management/','Plan the management handoff'],['/blog/str-purchase-to-launch-timeline/','Budget a delayed launch']]},
 purchase:{name:'Prepare an STR purchase',decision:'Move from research to a property decision using a written budget, shortlist and evidence checklist.',evidence:'Bring your available cash, financing status, desired buying timeline and any listing links. Decide what must be verified before you make an offer.',links:[['/buy-a-short-term-rental/','Follow the STR buyer roadmap'],['/blog/how-to-find-str-properties-for-sale/','Build a property shortlist'],['/blog/compare-two-str-properties-before-offer/','Compare properties before buying']]}
};
function stageFor(category,slug){
 const text=(category+' '+slug).toLowerCase();
 if(/comparison|reviews|accelerator-vs|accelerator-worth|acquisition-team|buyer-agent/.test(text))return 'service';
 if(/tax|cost-seg|depreciation|material-participation|7-day|seven-day/.test(text))return 'tax';
 if(/regulat|rules|permit|hoa|zoning|license/.test(text))return 'rules';
 if(/financ|mortgage|loan|lender|down-payment|capital|funding|entry-cost|reserves|cash-out/.test(text))return 'finance';
 if(/contract|offer|closing|negotiat|escrow|title-commitment/.test(text))return 'contract';
 if(/market|chandler|scottsdale|sedona|branson|broken-bow|poconos|nashville/.test(text))return 'market';
 if(/revenue|occupancy|adr|revpar|pricing|cash-flow|cash-on-cash|underwrit|economics|comparable/.test(text))return 'revenue';
 if(/operat|management|maintenance|design|furnish|insurance|hazard|guest|vendor|risk|amenit|cleaning|supply|launch/.test(text))return 'operations';
 return 'purchase';
}
const metadata={
 'the-local-guide-guests-actually-use':['STR Guest Guides: Operating Handoff for Investors','Evaluate guest-guide preparation as part of an STR operating handoff. Plan property instructions, local information and manager responsibilities before launch.'],
 'handling-a-problem-mid-stay':['STR Incident Response: Management Standards for Investors','Assess how an STR manager handles guest incidents. Review response standards, local support and operating responsibilities before buying a rental.'],
 'airbnb-guest-experience':['STR Guest Experience: Operating Quality for Investors','Assess arrival instructions, property readiness and guest support as operating requirements when evaluating an Airbnb investment.'],
 'airbnb-supplies-checklist':['Airbnb Supplies Checklist for STR Investment Planning','Plan the supplies an STR property needs at launch and during operation. Include inventory, replenishment and owner responsibilities in your purchase budget.'],
 'airbnb-cancellation-policy':['Airbnb Cancellation Policies: Revenue Planning for STR Investors','Evaluate cancellation-policy tradeoffs when underwriting an STR investment. Consider booking flexibility, revenue uncertainty and operating decisions.'],
 'airbnb-vs-vrbo-vs-booking':['STR Booking Channels: Airbnb, Vrbo and Booking.com for Investors','Compare booking channels from an STR owner perspective. Review distribution, platform costs and operational tradeoffs when planning an investment.'],
 'pet-friendly-airbnb-strategy':['Pet-Friendly STR Investments: Costs and Operating Tradeoffs','Evaluate pet-friendly positioning for an STR investment. Consider property materials, cleaning, operating policies and costs before purchasing.'],
 'buying-an-operating-str':['Buying an Existing Airbnb: Income, Transfer and Diligence','Buying an operating Airbnb? Verify seller income, included assets, transfer requirements and financing before paying for an existing STR business.'],
 'str-due-diligence-checklist':['STR Due Diligence Checklist Before Buying a Property','Buying a short-term rental? Review the key property documents, legal-use checks and financial evidence before committing to an STR purchase.'],
 'negotiating-airbnb-purchase':['Buying an STR: Price, Terms and Purchase Negotiation','Prepare an STR purchase negotiation using alternatives, deal evidence and contract terms. Review the items to discuss beyond the listing price.'],
 'bnb-accelerator-vs-diy':['Buying an STR: BNB Accelerator vs DIY Acquisition','Compare buying an STR yourself with BNB Accelerator acquisition support. Review time, diligence responsibilities, service scope and purchase risk.'],
 'is-bnb-accelerator-worth-it':['Is BNB Accelerator Worth It for an STR Buyer?','Considering BNB Accelerator for an STR purchase? Review service costs, deliverables, buyer fit and situations where acquisition support may not suit you.'],
 'dscr-loans-for-airbnb':['DSCR Loans for Buying an Airbnb Investment Property','Explore DSCR financing for an Airbnb purchase: lender income assumptions, ratio calculations and loan terms to verify for the specific property.'],
 'what-total-entry-cost-means':['How Much Cash Does It Take to Buy and Launch an STR?','Budget more than the STR purchase price. Review down payment, transaction costs, setup, furnishing and operating reserves before buying a rental.']
};
function setMetadata(html,title,description){
 html=html.replace(/<title>[\s\S]*?<\/title>/i,`<title>${esc(title)}</title>`);
 for(const name of ['description','og:description','twitter:description'])html=html.replace(new RegExp(`(<meta\\s+(?:name|property)="${name}"\\s+content=")[^"]*(")`,'i'),(_,a,b)=>a+esc(description)+b);
 for(const name of ['og:title','twitter:title'])html=html.replace(new RegExp(`(<meta\\s+(?:name|property)="${name}"\\s+content=")[^"]*(")`,'i'),(_,a,b)=>a+esc(title)+b);
 html=html.replace(/(<script[^>]*type="application\/ld\+json"[^>]*>)([\s\S]*?)(<\/script>)/g,(_,open,json,close)=>{
  const data=JSON.parse(json);
  function align(node){
   if(!node||typeof node!=='object')return;
   if(['Article','BlogPosting','WebPage','Blog'].includes(node['@type'])){
    node.description=description;
    if(['WebPage','Blog'].includes(node['@type']))node.name=title;
   }
   for(const value of Object.values(node)){if(Array.isArray(value))value.forEach(align);else if(value&&typeof value==='object')align(value);}
  }
  align(data);
  return open+JSON.stringify(data).replace(/</g,'\\u003c')+close;
 });
 return html;
}
const linkList=links=>links.map(([url,label])=>{
 if(!existsSync('.'+url+'index.html'))throw new Error('Buyer link missing '+url);
 return `<li><a href="${url}">${label}</a></li>`;
}).join('');
export function optimizeBlogBuyerIntent(html,path){
 if(!path.startsWith('blog/')||!path.endsWith('/index.html')||html.includes('data-buyer-intent="purchase"'))return html;
 if(path==='blog/index.html'){
  html=setMetadata(html,'Short-Term Rental Buying Guides | BNB Accelerator','Ready to buy an STR? Explore guides to purchase budgets, financing, properties for sale, seller revenue, due diligence and offers before buying an Airbnb.');
  const groups=[['Plan the purchase',[['/blog/how-to-buy-first-airbnb/','How to buy your first Airbnb'],['/tools/first-str-purchase-budget/','Calculate your purchase cash'],['/blog/str-mortgage-preapproval-before-property/','Get financing guardrails']]],['Find and compare properties',[['/blog/how-to-find-str-properties-for-sale/','Find STR properties for sale'],['/blog/buy-existing-airbnb-vs-start-from-scratch/','Existing Airbnb or new setup?'],['/blog/compare-two-str-properties-before-offer/','Compare two properties']]],['Verify before an offer',[['/blog/reconcile-airbnb-payout-export/','Verify seller Airbnb income'],['/blog/permits-that-do-not-transfer/','Check permission and transfer'],['/blog/str-due-diligence-checklist/','Review the diligence checklist']]],['Set the price and choose help',[['/blog/str-maximum-offer-price-from-revenue/','Calculate the maximum offer'],['/blog/negotiating-airbnb-purchase/','Negotiate the purchase'],['/pricing/','Compare acquisition scope and costs']]]];
  const guide=`<!-- first-str:start --><section class="bg-alt" data-buyer-intent="purchase"><div class="wrap"><div class="section-head"><span class="eyebrow">STR purchase decisions</span><h2>Find the guide for your next buying step</h2><p>Work from your available cash to a verified property and an offer you can support.</p></div><div class="grid grid-2">${groups.map(([name,links])=>`<article class="card"><h3>${name}</h3><ul>${linkList(links)}</ul></article>`).join('')}</div><div class="buyer-review"><h3>Have a property or purchase budget in mind?</h3><p>Bring the listing links, available purchase cash, financing status and open diligence questions to a purchase discussion.</p><a class="btn btn-primary" href="/apply/">Apply for an STR Purchase Call</a></div></div></section><!-- first-str:end -->`;
  if(html.includes('<!-- first-str:start -->'))html=html.replace(/<!-- first-str:start -->[\s\S]*?<!-- first-str:end -->/,guide);
  else html=html.replace(/(<section class="hero hero-page">[\s\S]*?<\/section>)/,'$1'+guide);
  // Topic selection remains available in the searchable archive below.
  html=html.replace(/<section class="section-sm">[\s\S]*?<\/section>/, '<section class="section-sm"><div class="wrap"><h2>Search the complete STR article library</h2><p>Use the search and topic filters below for a specific property, financing question or diligence issue.</p></div></section>');
  html=purchaseCta(html);
  return html;
 }
 const slug=path.split('/')[1];
 const category=html.match(/<span class="eyebrow">([^<]*)<\/span>/)?.[1]||'';
 const key=stageFor(category,slug),stage=stages[key];
 if(metadata[slug])html=setMetadata(html,...metadata[slug]);
 const block=`<aside class="buyer-next-step" data-buyer-intent="purchase" data-purchase-stage="${key}" aria-label="STR purchase next step"><span class="eyebrow">${stage.name}</span><h2>Buying an STR? Turn this research into a purchase decision.</h2><p>${stage.decision}</p><p>${stage.evidence}</p><ul>${linkList(stage.links)}</ul><a class="btn btn-primary" href="/apply/">Discuss My STR Purchase</a></aside>`;
 if(html.includes('<div class="author-box">'))html=html.replace('<div class="author-box">',block+'<div class="author-box">');
 else html=html.replace('</article>',block+'</article>');
 html=purchaseCta(html);
 return html;
}

function purchaseCta(html){
 // Tailor the concluding conversion point while retaining the original article.
 html=html.replace(/(<section class="cta-band">[\s\S]*?<h2[^>]*>)[\s\S]*?(<\/h2>)/,(_,a,b)=>a+'Have an STR property or purchase budget to review?'+b);
 html=html.replace(/(<section class="cta-band">[\s\S]*?<p[^>]*>)[\s\S]*?(<\/p>)/,(_,a,b)=>a+'Bring your listing links, available cash, financing status and the questions this guide raised. Discuss the next acquisition step with BNB Accelerator.'+b);
 return html;
}
