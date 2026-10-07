import assert from 'node:assert/strict';
import { readFileSync, existsSync } from 'node:fs';
import { profiles, keywordRows, expandPreclosingKeywords } from './preclosing_keywords.mjs';
assert.equal(keywordRows.length, 500);
assert.equal(new Set(keywordRows.map(r => r.query.toLowerCase())).size, 500);
for (const p of profiles) {
  const path = `blog/${p.slug}/index.html`;
  const source = readFileSync(path, 'utf8');
  const built = readFileSync('public/' + path, 'utf8');
  for (const html of [source, built]) {
    assert.equal(expandPreclosingKeywords(html, path), html, `Non-idempotent ${path}`);
    assert.equal((html.match(/id="preclosing-purchase-checks"/g) || []).length, 1);
    assert.equal((html.match(/id="purchase-check-\d"/g) || []).length, 5);
    const schemas = [...html.matchAll(/<script[^>]*type="application\/ld\+json"[^>]*>(.*?)<\/script>/gs)].flatMap(m => { const d = JSON.parse(m[1]); return d['@graph'] || [d]; });
    const article = schemas.find(n => ['Article', 'BlogPosting'].includes(n['@type']));
    assert.equal(article.dateModified, ['airbnb-cash-on-cash-return', 'flood-zone-str-underwriting', 'dscr-loans-for-airbnb'].includes(p.slug) ? '2026-10-07' : '2026-10-06');
    // Synthetic later revision: regenerating the purchase checks must not backdate it.
    const later = expandPreclosingKeywords(html.replace(/"dateModified": "\d{4}-\d{2}-\d{2}"/, '"dateModified": "2030-01-02"'), path);
    assert(later.includes('"dateModified": "2030-01-02"'));
    assert(later.includes('<span>Updated January 2, 2030</span>'));
    const faqs = schemas.filter(n => n['@type'] === 'FAQPage').flatMap(n => n.mainEntity);
    for (const t of p.tasks) {
      assert(html.includes(t.question.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;')));
      const faq = faqs.find(q => q.name === t.question);
      assert.equal(faq.acceptedAnswer.text, t.answer);
      assert(!/after closing|after purchase|post.closing|guest messaging|dynamic pricing software/i.test(t.task), `Outside acquisition scope ${t.task}`);
    }
    const block = html.match(/<!-- preclosing-keywords:start -->[\s\S]*?<!-- preclosing-keywords:end -->/)[0];
    for (const [, route, anchor] of block.matchAll(/href="(\/[^"#]*)(?:#([^"]*))?"/g)) {
      assert(existsSync('.' + route + 'index.html'), `Missing related route ${route}`);
      if (anchor) assert(readFileSync('.' + route + 'index.html', 'utf8').includes(`id="${anchor}"`), `Missing anchor ${route}#${anchor}`);
    }
  }
}
const index = readFileSync('blog/index.html', 'utf8');
assert.equal(expandPreclosingKeywords(index, 'blog/index.html'), index);
for (const p of profiles) assert(index.includes(`/blog/${p.slug}/#preclosing-purchase-checks`));
assert.equal(expandPreclosingKeywords(readFileSync('index.html', 'utf8'), 'index.html'), readFileSync('index.html', 'utf8'));
console.log('PASS: 500 unique query targets; 50 existing owners; 250 visible answers/schema aligned; acquisition scope, internal anchors and regeneration persistence verified.');
