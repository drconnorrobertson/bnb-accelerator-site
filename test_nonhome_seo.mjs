import assert from 'node:assert/strict';
import { readFileSync, readdirSync } from 'node:fs';
import { join } from 'node:path';
import { normalizeNonhomeSeo } from './nonhome_seo.mjs';
const home = readFileSync('index.html', 'utf8');
assert.equal(normalizeNonhomeSeo(home, 'index.html'), home);
const scenario = 'scenarios/hilton-head-island-sc/four-bedroom-group-stay/remote-operations/index.html';
const result = normalizeNonhomeSeo(readFileSync(scenario, 'utf8'), scenario);
assert.match(result, /BreadcrumbList/);
assert.match(result, /Before using this model to buy/);
assert.match(result, /href="\/scenarios\/hilton-head-island-sc\/"/);
assert.doesNotMatch(result, /for run the home/);
assert.equal(normalizeNonhomeSeo(result, scenario), result, 'normalizer must be idempotent');
let count = 0, breadcrumbs = 0, noncanonical = 0;
const titles = new Set(), descriptions = new Set(), routes = new Set();
function scan(dir, fn) { for (const e of readdirSync(dir, {withFileTypes:true})) { const p=join(dir,e.name); if(e.isDirectory()) scan(p,fn); else if(e.name==='index.html') fn(p); } }
scan('public', p => routes.add('/'+p.slice(7,-10)));
scan('public', p => {
 const html = readFileSync(p,'utf8');
 const title = html.match(/<title>(.*?)<\/title>/is)[1];
 const desc = html.match(/<meta name="description" content="([^"]*)"/i)[1];
 assert(!titles.has(title), `Duplicate title ${p}`); titles.add(title);
 assert(!descriptions.has(desc), `Duplicate description ${p}`); descriptions.add(desc);
 for (const [,json] of html.matchAll(/<script[^>]*type="application\/ld\+json"[^>]*>(.*?)<\/script>/gs)) JSON.parse(json);
 if(p!=='public/index.html') {
  assert(html.includes('BreadcrumbList'), `Missing breadcrumb ${p}`); breadcrumbs++;
  for(const [,url] of html.matchAll(/href="(\/[^"?#]*)(?:[?#][^"]*)?"/g)) if(!url.endsWith('/') && routes.has(url+'/')) noncanonical++;
 }
 count++;
});
assert.equal(noncanonical,0);
console.log(`PASS: ${count} generated routes, unique metadata, valid JSON-LD, ${breadcrumbs} non-home breadcrumbs, canonical internal route links, idempotence and homepage exclusion.`);
