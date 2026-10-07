import { readFileSync, writeFileSync } from 'node:fs';
import { profiles, keywordRows, expandPreclosingKeywords } from '../preclosing_keywords.mjs';
for (const p of profiles) {
  const path = `blog/${p.slug}/index.html`;
  writeFileSync(path, expandPreclosingKeywords(readFileSync(path, 'utf8'), path));
}
writeFileSync('blog/index.html', expandPreclosingKeywords(readFileSync('blog/index.html', 'utf8'), 'blog/index.html'));
const targets = new Set(profiles.map(p => `https://www.bnbaccelerator.com/blog/${p.slug}/`)); targets.add('https://www.bnbaccelerator.com/blog/');
let sitemap = readFileSync('sitemap-blog.xml', 'utf8').replace(/<url>[\s\S]*?<\/url>/g, block => {
  const url = block.match(/<loc>(.*?)<\/loc>/)[1];
  return targets.has(url) ? block.replace(/<lastmod>[^<]+<\/lastmod>/, '<lastmod>2026-10-06</lastmod>') : block;
});
writeFileSync('sitemap-blog.xml', sitemap);
writeFileSync('_gen/preclosing-keyword-map.json', JSON.stringify(keywordRows, null, 2) + '\n');
console.log('Expanded 50 existing articles; 250 purchase answers cover 500 unique related query targets. Blog directory and lastmod refreshed.');
