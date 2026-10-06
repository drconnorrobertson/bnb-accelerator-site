import assert from 'node:assert/strict';
import { readFileSync, readdirSync } from 'node:fs';
import { join, relative } from 'node:path';
import { normalizeNonhomeDesign } from './nonhome_design.mjs';
import { normalizeNonhomeSeo } from './nonhome_seo.mjs';
const home=readFileSync('index.html','utf8');
assert.equal(normalizeNonhomeDesign(home,'index.html'),home);
const header=home.match(/<header\b[\s\S]*?<\/header>/)[0];
const footer=home.match(/<footer\b[\s\S]*?<\/footer>/)[0];
let count=0;
const main = html => (html.match(/<main\b[\s\S]*?<\/main>/i)?.[0] || '').replace(/<script\b[\s\S]*?<\/script>/gi,'').replace(/<footer[^>]*>([\s\S]*?)<\/footer>/gi,'$1').replace(/<nav class="resource-footer"[^>]*>([\s\S]*?)<\/nav>/gi,'$1');
function walk(dir){for(const e of readdirSync(dir,{withFileTypes:true})){
 if(e.name.startsWith('.')||e.name.startsWith('_')||['public','node_modules'].includes(e.name))continue;
 const p=join(dir,e.name);if(e.isDirectory()){walk(p);continue;}if(!p.endsWith('.html')||p==='index.html')continue;
 const source=normalizeNonhomeSeo(readFileSync(p,'utf8'),p);
 const themed=normalizeNonhomeDesign(source,p);
 assert(themed.includes(header),`Shared header missing: ${p}`);
 assert(themed.includes(footer),`Shared footer missing: ${p}`);
 const text=html=>html.replace(/<[^>]*>/g,' ').replace(/\s+/g,' ').trim();
 assert.equal(text(main(themed)),text(main(source)),`Main text changed: ${p}`);
 for(const tag of ['input','iframe','select','textarea']) assert.deepEqual(main(themed).match(new RegExp('<'+tag+'\\b[^>]*>','gi')),main(source).match(new RegExp('<'+tag+'\\b[^>]*>','gi')),`Interactive controls changed: ${p}`);
 assert.equal((themed.match(/id="bnb-application"/g)||[]).length,1,`Duplicate popup ${p}`);
 assert.equal((themed.match(/<script[^>]+src="\/assets\/main.js/g)||[]).length,1,`Menu behavior ${p}`);
 assert.equal(normalizeNonhomeDesign(themed,p),themed,`Idempotence ${p}`);
 assert.match(themed,/data-bnb-design="homepage"/);
 count++;
}}
walk('.');
console.log(`PASS: homepage excluded; ${count} non-home HTML files share header, footer, popup and theme while preserving main content and existing menu scripts.`);
