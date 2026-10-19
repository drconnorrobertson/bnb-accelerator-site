import fs from 'node:fs';
import path from 'node:path';
const root=process.argv[2]||'public';
const target='/blog/pet-fence-roi-short-term-rental/';
const aliases=['budget','buying','design','inspection','insurance','maintenance','operations','repair-replace'].map(s=>'/blog/pet-fence-'+s+'-short-term-rental/');
let changed=0;
function walk(dir){for(const e of fs.readdirSync(dir,{withFileTypes:true})){const p=path.join(dir,e.name);if(e.isDirectory())walk(p);else if(e.name.endsWith('.html')){let s=fs.readFileSync(p,'utf8'),before=s;s=s.replace(/href=(['"])([^'"]+)\1/g,(tag,q,url)=>{for(const alias of aliases){for(const old of [alias,'https://www.bnbaccelerator.com'+alias])if(url===old||url.startsWith(old+'#')||url.startsWith(old+'?'))return 'href='+q+(old.startsWith('https:')?'https://www.bnbaccelerator.com':'')+target+url.slice(old.length)+q;}return tag;});if(s!==before){fs.writeFileSync(p,s);changed++;}}}}
walk(root);
const map=path.join(root,'sitemap-blog.xml');let xml=fs.readFileSync(map,'utf8');
xml=xml.replace(/<(?:\w+:)?url\b[^>]*>[\s\S]*?<\/(?:\w+:)?url>/g,block=>aliases.some(a=>block.includes('https://www.bnbaccelerator.com'+a+'<'))?'':block);
xml=xml.replace(/<(?:\w+:)?url\b[^>]*>[\s\S]*?<\/(?:\w+:)?url>/g,block=>block.includes('https://www.bnbaccelerator.com'+target+'<')?block.replace(/<(?:\w+:)?lastmod>.*?<\/(?:\w+:)?lastmod>/g,'<lastmod>2026-10-19</lastmod>'):block);
fs.writeFileSync(map,xml);
console.log('Consolidated eight overlapping article URLs; repaired links in '+changed+' pages.');
