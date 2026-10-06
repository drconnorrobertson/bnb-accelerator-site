import assert from 'node:assert/strict';
import { readdirSync,readFileSync,existsSync } from 'node:fs';
import { optimizeBlogBuyerIntent } from './blog_buyer_intent.mjs';
const home=readFileSync('index.html','utf8');
assert.equal(optimizeBlogBuyerIntent(home,'index.html'),home);
let count=0;const stages={};
for(const e of readdirSync('blog',{withFileTypes:true})){
 if(!e.isDirectory()||!existsSync(`blog/${e.name}/index.html`))continue;
 const path=`blog/${e.name}/index.html`,source=readFileSync(path,'utf8'),output=optimizeBlogBuyerIntent(source,path);
 assert.equal(optimizeBlogBuyerIntent(output,path),output,`Idempotence ${path}`);
 assert.equal((output.match(/class="buyer-next-step"/g)||[]).length,1,`Buyer next step ${path}`);
 const core=html=>html.match(/<article\b[^>]*>[\s\S]*?<\/article>/)?.[0];
 assert.equal(core(output).replace(/<aside class="buyer-next-step"[\s\S]*?<\/aside>/,''),core(source),`Original article altered ${path}`);
 const block=output.match(/<aside class="buyer-next-step"[\s\S]*?<\/aside>/)[0];
 for(const [,url] of block.matchAll(/href="(\/[^"?#]*)"/g))assert(existsSync('.'+url+'index.html'),`Broken buyer link ${path}: ${url}`);
 const stage=output.match(/data-purchase-stage="([^"]*)"/)[1];stages[stage]=(stages[stage]||0)+1;
 const built=readFileSync('public/'+path,'utf8');assert.match(built,/data-buyer-intent="purchase"/);assert.match(built,/nonhome-theme.css/);
 for(const [,json] of built.matchAll(/<script[^>]*type="application\/ld\+json"[^>]*>(.*?)<\/script>/gs))JSON.parse(json);
 count++;
}
const index=optimizeBlogBuyerIntent(readFileSync('blog/index.html','utf8'),'blog/index.html');
assert.match(index,/Find the guide for your next buying step/);assert.match(index,/Apply for an STR Purchase Call/);
assert.equal(optimizeBlogBuyerIntent(index,'blog/index.html'),index);
assert.equal((index.match(/data-blog-post/g)||[]).length,(readFileSync('blog/index.html','utf8').match(/data-blog-post/g)||[]).length,'Archive cards must remain');
console.log(`PASS: ${count} buyer pathways, intact original article bodies and archive cards, valid links/schema, homepage exclusion and idempotence. Stages: ${JSON.stringify(stages)}`);
