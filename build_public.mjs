// Deploy only public site output. Generator inputs and editorial records stay in Git.
import { readdir, mkdir, copyFile, rm, readFile, writeFile, access } from 'node:fs/promises';
import { dirname, extname, join, relative } from 'node:path';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
execFileSync('python3', ['scripts/upgrade_tools.py'], {stdio: 'inherit'});
execFileSync('python3', ['_gen/expand_review_evidence.py'], {stdio: 'inherit'});
execFileSync('python3', ['scripts/build_proformas.py'], {stdio: 'inherit'});
execFileSync('python3', ['scripts/build_tracker_proformas.py'], {stdio: 'inherit'});
import { normalizeResourceLinks, resourceRoutes } from './resource_links.mjs';
import { normalizePerformanceDisclosures } from './performance_disclosures.mjs';
import { addMetaPixel } from './meta_pixel.mjs';
import { normalizeNonhomeSeo } from './nonhome_seo.mjs';
import { normalizeNonhomeDesign } from './nonhome_design.mjs';
import { optimizeBlogBuyerIntent } from './blog_buyer_intent.mjs';
import { expandPreclosingKeywords } from './preclosing_keywords.mjs';
const root = process.cwd();
const out = join(root, 'public');
const publicExtensions = new Set(['.html', '.css', '.js', '.svg', '.jpg', '.jpeg', '.png', '.webp', '.gif', '.avif', '.ico', '.woff', '.woff2', '.ttf', '.eot', '.pdf', '.mp4', '.webm']);
const publicRootFiles = new Set(['robots.txt', 'llms.txt', 'sitemap.xml', 'sitemap-core.xml', 'sitemap-investor-guides.xml', 'sitemap-blog.xml', 'sitemap-scenarios.xml', 'sitemap-markets.xml', 'sitemap-proof.xml', 'sitemap-proformas.xml', 'c745eff13e89424cb1ed10f69adea860.txt']);
for (const route of resourceRoutes.values()) await access(join(root, route, 'index.html'));
await rm(out, { recursive: true, force: true });
let copied = 0;
async function walk(directory) {
 for (const entry of await readdir(directory, { withFileTypes: true })) {
  if (entry.name.startsWith('.') || entry.name.startsWith('_') || ['public', 'node_modules'].includes(entry.name)) continue;
  const source = join(directory, entry.name);
  if (entry.isDirectory()) { await walk(source); continue; }
  if (!entry.isFile()) continue;
  const path = relative(root, source);
  if (!publicExtensions.has(extname(source)) && !publicRootFiles.has(path) && path !== 'assets/review-evidence/deal-entry-fields.csv') continue;
  const target = join(out, path);
  await mkdir(dirname(target), { recursive: true });
  if (extname(source) === '.html') {
    await writeFile(target, expandPreclosingKeywords(addMetaPixel(normalizePerformanceDisclosures(normalizeResourceLinks(normalizeNonhomeDesign(optimizeBlogBuyerIntent(normalizeNonhomeSeo(await readFile(source, 'utf8'), path), path), path)), path)), path));
  } else {
    await copyFile(source, target);
  }
  copied++;
 }
}
await walk(root);
for (const required of ['index.html', '404.html', 'apply/index.html', 'assets/main.js', 'assets/style.min.css', ...publicRootFiles]) await access(join(out, required));
for (const forbidden of ['_gen/client_faq_source.json', '_gen/deals.json', 'README.md', 'build_public.mjs', 'vercel.json']) {
 let exists = true;
 try { await access(join(out, forbidden)); } catch { exists = false; }
 assert.equal(exists, false, `Internal file leaked: ${forbidden}`);
}
const sitemapFiles = [...publicRootFiles].filter(name => name.startsWith('sitemap-'));
let urls = 0;
for (const file of sitemapFiles) {
 const xml = await readFile(join(out, file), 'utf8');
 for (const [, location] of xml.matchAll(/<(?:\w+:)?loc>(.*?)<\/(?:\w+:)?loc>/g)) {
  const path = new URL(location).pathname;
  await access(join(out, path, 'index.html'));
  urls++;
 }
}
console.log(`Public build: ${copied} files; all ${urls} sitemap routes present; internal records excluded.`);
