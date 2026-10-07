// Reviewed acquisition tasks. Two related query variants share one useful answer.
// The keyword inventory is editorial, not search-volume or ranking evidence.
import { readFileSync } from 'node:fs';
const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
export const profiles = [];
for (const line of readFileSync(new URL('./_gen/preclosing_keyword_profiles.txt', import.meta.url), 'utf8').split('\n')) {
  if (!line || line.startsWith('#')) continue;
  if (line.includes('|')) {
    const [slug, stage] = line.split('|'); profiles.push({ slug, stage, tasks: [] });
  } else {
    const split = line.indexOf('=');
    if (split < 0) throw new Error('Missing task answer');
    const task = line.slice(0, split), answer = line.slice(split + 1);
    const question = `How do I ${task}?`;
    const suffix = /before|during|at settlement/.test(task) ? '' : ' before buying';
    const queries = [`how to ${task}${suffix}`, `${task.replace(/\bSTR\b/g, 'short term rental')}${suffix}`];
    profiles.at(-1).tasks.push({ task, question, answer, queries });
  }
}
if (profiles.length !== 50 || profiles.some(p => p.tasks.length !== 5)) throw new Error('Expected 50 profiles with five tasks each');
export const keywordRows = profiles.flatMap(p => p.tasks.flatMap((t, i) => t.queries.map(query => ({ query, stage: p.stage, ownerUrl: `https://www.bnbaccelerator.com/blog/${p.slug}/`, answerAnchor: `purchase-check-${i + 1}`, coverage: 'Related query variants share the same answer; demand unmeasured' }))));
if (keywordRows.length !== 500 || new Set(keywordRows.map(r => r.query.toLowerCase())).size !== 500) throw new Error('Expected 500 unique queries');
const profileMap = new Map(profiles.map(p => [`blog/${p.slug}/index.html`, p]));
const links = {
  'Financing': ['/financing/', 'Compare acquisition financing'],
  'Revenue evidence': ['/blog/reconcile-airbnb-payout-export/', 'Verify seller income evidence'],
  'Offer and closing': ['/blog/str-due-diligence-checklist/', 'Review the purchase diligence checklist'],
  'Permission and restrictions': ['/blog/str-regulations-before-you-buy/', 'Verify property-specific rental permission'],
  'Physical diligence': ['/blog/str-due-diligence-checklist/', 'Turn inspection findings into an offer decision'],
  'Market and deal selection': ['/blog/short-term-rental-buy-box/', 'Define your acquisition criteria']
};
const sectionPattern = /<!-- preclosing-keywords:start -->[\s\S]*?<!-- preclosing-keywords:end -->\s*/g;
export function expandPreclosingKeywords(source, path) {
  const profile = profileMap.get(path);
  if (!profile && path !== 'blog/index.html') return source;
  let html = source.replace(sectionPattern, '');
  if (!profile) {
    const groups = [...new Set(profiles.map(p => p.stage))].map(stage => `<h3>${esc(stage)}</h3><ul>${profiles.filter(p => p.stage === stage).map(p => `<li><a href="/blog/${p.slug}/#preclosing-purchase-checks">${esc(p.tasks[0].task[0].toUpperCase() + p.tasks[0].task.slice(1))}</a></li>`).join('')}</ul>`).join('\n');
    const directory = `<!-- preclosing-keywords:start -->\n<section aria-labelledby="preclosing-guide-directory"><div class="wrap wrap-narrow"><h2 id="preclosing-guide-directory">Evaluate an asset before you close</h2><p>Find acquisition checks for the property you are considering: financing, verified income, rental permission, physical condition and offer protection. Use the linked questions to decide what evidence you still need before committing purchase capital.</p>${groups}</div></section>\n<!-- preclosing-keywords:end -->\n`;
    return html.replace('</main>', directory + '</main>');
  }
  const siblings = profiles.filter(p => p.stage === profile.stage && p.slug !== profile.slug);
  const index = profiles.filter(p => p.stage === profile.stage).findIndex(p => p.slug === profile.slug);
  const sibling = siblings[index % siblings.length];
  const [link, label] = links[profile.stage];
  const section = `<!-- preclosing-keywords:start -->\n<section aria-labelledby="preclosing-purchase-checks"><h2 id="preclosing-purchase-checks">Questions to resolve before committing to this purchase</h2>\n${profile.tasks.map((t, i) => `<h3 id="purchase-check-${i + 1}">${esc(t.question)}</h3><p>${esc(t.answer)}</p>`).join('\n')}\n<p>Record the evidence, responsible reviewer, cash effect and transaction deadline for any unresolved item. Bring those findings to the <a href="/apply/">STR acquisition call</a> before deciding whether to proceed, revise the offer or exercise available contract protection.</p><p><a href="${link}">${label}</a> · <a href="/blog/${sibling.slug}/#preclosing-purchase-checks">Related ${esc(profile.stage.toLowerCase())} checks</a> · <a href="/tools/first-str-purchase-budget/">Compare the total purchase cash budget</a></p></section>\n<!-- preclosing-keywords:end -->\n`;
  if (!html.includes('<div class="author-box">')) throw new Error(`Missing author insertion point: ${path}`);
  html = html.replace('<div class="author-box">', section + '<div class="author-box">');
  // Preserve evidenced publication dates; modification records the new substance.
  html = html.replace(/(<span>Published [^<]+<\/span>)(?:<span>&middot;<\/span><span>Updated [^<]+<\/span>)?/, '$1<span>&middot;</span><span>Updated October 6, 2026</span>');
  const text = html.match(/<article\b[^>]*>([\s\S]*?)<\/article>/)?.[1]?.replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim() || '';
  const words = text.split(' ').length;
  html = html.replace(/<span>\d+ min read<\/span>/, `<span>${Math.max(6, Math.ceil(words / 210))} min read</span>`);
  const questions = new Set(profile.tasks.map(t => t.question));
  if (!html.includes('"FAQPage"')) {
    const faq = { '@context': 'https://schema.org', '@type': 'FAQPage', mainEntity: profile.tasks.map(t => ({ '@type': 'Question', name: t.question, acceptedAnswer: { '@type': 'Answer', text: t.answer } })) };
    html = html.replace('</head>', `<script type="application/ld+json">${JSON.stringify(faq)}</script>\n</head>`);
  }
  return html.replace(/(<script[^>]*type="application\/ld\+json"[^>]*>)([\s\S]*?)(<\/script>)/g, (_, open, json, close) => {
    const data = JSON.parse(json);
    const nodes = data['@graph'] || [data];
    for (const node of nodes) {
      if (['Article', 'BlogPosting'].includes(node['@type'])) { node.dateModified = '2026-10-06'; node.wordCount = words; }
      if (node['@type'] === 'FAQPage') {
        node.mainEntity = (node.mainEntity || []).filter(q => !questions.has(q.name));
        node.mainEntity.push(...profile.tasks.map(t => ({ '@type': 'Question', name: t.question, acceptedAnswer: { '@type': 'Answer', text: t.answer } })));
      }
    }
    return open + JSON.stringify(data, null, 2).replace(/</g, '\\u003c') + close;
  });
}
