import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { runInNewContext } from 'node:vm';
const source = readFileSync('scb-precall/index.html', 'utf8');
const built = readFileSync('public/scb-precall/index.html', 'utf8');
assert.equal((source.match(/<h1\b/g) || []).length, 1);
assert.match(built, /name="robots" content="noindex, follow"/);
assert.match(built, /rel="canonical" href="https:\/\/www.bnbaccelerator.com\/scb-precall\/"/);
assert.match(built, /BreadcrumbList/);
assert.match(built, /data-bnb-design="homepage"/);
assert.match(built, /id="bnb-application"/);
assert(built.indexOf('history.replaceState') < built.indexOf("fbq('track'"), 'Contact query must be cleared before analytics');
assert.doesNotMatch(source, /__NUXT|leadconnectorhq|hotjar|funnelId|<form|mailto:|tel:/);
for (const xml of ['sitemap-core.xml','sitemap-blog.xml','sitemap-investor-guides.xml']) {
  assert(!readFileSync(xml, 'utf8').includes('/scb-precall/'), 'Appointment prep is not a search landing page');
}
for (const anchor of ['checklist','process','deals','case-studies','questions']) {
  assert(source.includes(`id="${anchor}"`) && source.includes(`href="#${anchor}"`));
}
assert.equal((source.match(/<iframe\b/g) || []).length, 22, 'Keep all original resource videos');
assert.equal((source.match(/class="bnb-img"/g) || []).length, 15, 'Keep original visual case studies');
assert.equal((source.match(/data-youtube=/g) || []).length, 3, 'Keep introduction and both testimonial videos');
const dealSection = source.slice(source.indexOf('id="deals"'),source.indexOf('id="case-studies"'));
assert.equal((dealSection.match(/<li>/g) || []).length, 103);
assert.match(source, /not a representative performance sample/);
assert.match(source, /not a current offer/);
for (const [,href] of source.matchAll(/href="([^"]*)"/g)) assert(!/^(?:javascript:|data:)/i.test(href));

const events = {}, status = {}, search = {value:'Mesa',addEventListener:(type,fn)=>events[type]=fn};
const deals = [{textContent:'Mesa, Arizona',hidden:false},{textContent:'Denver, Colorado',hidden:false}];
let activated;
const button = {addEventListener:(type,fn)=>events.play=fn,getAttribute:()=> 'Play introduction',replaceWith:frame=>activated=frame};
const player = {dataset:{youtube:'a2eo794BiLA'},querySelector:()=>button};
const doc = {
 querySelectorAll:selector=>selector==='[data-youtube]'?[player]:deals,
 querySelector:selector=>selector==='#deal-search'?search:status,
 createElement:()=>({})
};
runInNewContext(readFileSync('scb-precall/precall.js','utf8'), {document:doc});
assert.equal(deals[0].hidden,false); assert.equal(deals[1].hidden,true);
assert.equal(status.textContent,'1 of 2 source-provided examples');
search.value='absent'; events.input(); assert(deals.every(d=>d.hidden)); assert.match(status.textContent,/try another/);
search.value=''; events.input(); assert(deals.every(d=>!d.hidden));
events.play(); assert.equal(activated.src,'https://www.youtube-nocookie.com/embed/a2eo794BiLA?autoplay=1');
assert.equal(activated.referrerPolicy,'strict-origin'); assert.equal(activated.title,'introduction');
console.log('PASS: pre-call resource preservation, clean canonical/noindex, query privacy, shared flow, search and video activation.');
