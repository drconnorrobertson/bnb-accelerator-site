// Normalize only the refreshed owner through its existing purchase-check workflow.
import { readFileSync, writeFileSync } from 'node:fs';
import { expandPreclosingKeywords } from '../preclosing_keywords.mjs';
const path = 'blog/airbnb-cash-on-cash-return/index.html';
const html = expandPreclosingKeywords(readFileSync(path, 'utf8'), path);
if (expandPreclosingKeywords(html, path) !== html) throw new Error('Non-idempotent cash-return owner');
writeFileSync(path, html);
const minutes = html.match(/<span>(\d+) min read<\/span>/)[1];
const archive = readFileSync('blog/index.html', 'utf8');
let changed = 0;
writeFileSync('blog/index.html', archive.replace(/<article class="post-card"[\s\S]*?<\/article>/g, card => {
  if (!card.includes('/blog/airbnb-cash-on-cash-return/')) return card;
  changed++;
  return card.replace(/<span>\d+ min read<\/span>/, `<span>${minutes} min read</span>`);
}));
if (changed !== 1) throw new Error('Expected one archive card');
console.log(`Cash return normalized: ${minutes} minutes; newer modification retained; nine schema answers.`);
