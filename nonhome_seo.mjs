// SEO normalization for existing non-homepage routes. No generated facts or dates.
import { readdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';
const origin = 'https://www.bnbaccelerator.com';
const pages = new Map();
const decode = s => s.replace(/&amp;/g, '&').replace(/&quot;/g, '"').replace(/&#39;|&apos;/g, "'").replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&nbsp;/g, ' ');
const plain = s => decode(s.replace(/<[^>]*>/g, ' ').replace(/\s+/g, ' ').trim());
const escape = s => s.replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
function catalog(dir, prefix = '') {
 for (const e of readdirSync(dir, { withFileTypes: true })) {
  if (e.name.startsWith('.') || e.name.startsWith('_') || ['public', 'node_modules'].includes(e.name)) continue;
  const path = join(dir, e.name), relative = prefix + e.name;
  if (e.isDirectory()) catalog(path, relative + '/');
  else if (e.name === 'index.html') {
   const html = readFileSync(path, 'utf8');
   pages.set('/' + prefix, { title: plain(html.match(/<title>(.*?)<\/title>/is)?.[1] || prefix), h1: plain(html.match(/<h1\b[^>]*>(.*?)<\/h1>/is)?.[1] || prefix) });
  }
 }
}
catalog(process.cwd());
const overrides = {
 '/answers/what-is-revpar/': ['RevPAR Definition, Formula & STR Calculator | BNB Accelerator', 'RevPAR is room revenue per available night. Calculate it from revenue and availability, compare ADR and occupancy, and see why it does not measure profit.'],
 '/blog/airbnb-dynamic-pricing-tools/': ['Airbnb Dynamic Pricing: PriceLabs, Beyond and Wheelhouse', 'Compare PriceLabs, Beyond and Wheelhouse for Airbnb dynamic pricing. Learn how base rates, minimum stays and booking pace affect your pricing setup.'],
 '/blog/airbnb-occupancy-rates-explained/': ['Airbnb Occupancy Rates: Calculation and Revenue Tradeoffs', 'Learn how to calculate Airbnb occupancy, account for blocked nights and compare occupancy with ADR and RevPAR before underwriting a rental property.'],
 '/blog/airbnb-revenue-projections/': ['Airbnb Revenue Projections: Methods and Comparable Data', 'Build Airbnb revenue projections from seller records and comparable rentals. Evaluate seasonality, occupancy and expenses before making an offer.'],
 '/markets/': ['Short-Term Rental Investment Markets | BNB Accelerator', 'Compare short-term rental markets by purchase budget, seasonal demand, operating costs and local restrictions. Explore BNB Accelerator market guides.'],
 '/guides/str-investment/': ['Short-Term Rental Purchase Guides | BNB Accelerator', 'Explore STR purchase guides by property type and decision: financing, seller records, due diligence, setup costs, cash-flow downside and exit strategy.'],
 '/passive-airbnb-income/': ['Passive Airbnb Income: Ownership and Management Tradeoffs', 'Explore the responsibilities behind Airbnb income, from acquisition and setup to manager oversight, operating expenses and investment risk.']
};
export function normalizeNonhomeSeo(html, path) {
 if (path === 'index.html' || !path.endsWith('/index.html')) return html;
 const route = '/' + path.slice(0, -10);
 if (!pages.has(route)) throw new Error(`Unknown SEO route ${route}`);
 let title = plain(html.match(/<title>(.*?)<\/title>/is)?.[1] || pages.get(route).title);
 let description = decode(html.match(/<meta\s+name="description"\s+content="([^"]*)"/i)?.[1] || '');
 if (overrides[route]) [title, description] = overrides[route];
 if (route.startsWith('/regulations/') && route.split('/').filter(Boolean).length === 2) {
  const state = pages.get(route).h1.replace(/ Short-Term Rental Regulations.*$/i, '');
  description = `Review ${state} short-term rental regulations: local permits, zoning, tax obligations and the property-specific checks to complete before buying an Airbnb.`;
 }
 if (route.startsWith('/scenarios/') && route.split('/').filter(Boolean).length === 4) {
  const h1 = pages.get(route).h1;
  const [subject] = h1.split(':');
  const goal = { 'cash-flow': 'cash flow', 'revenue-growth': 'revenue growth', 'remote-operations': 'remote operations' }[route.split('/').filter(Boolean).at(-1)];
  if (goal) description = `Model ${subject.trim()} for ${goal}. Adjust rate, occupancy and expenses; review seasonality and the operating checklist. Estimates exclude financing and tax.`;
 }
 html = html.replace(/<title>.*?<\/title>/is, `<title>${escape(title)}</title>`);
 for (const key of ['description', 'og:description', 'twitter:description']) {
  html = html.replace(new RegExp(`(<meta\\s+(?:name|property)="${key}"\\s+content=")[^"]*(")`, 'i'), (_, before, after) => before + escape(description) + after);
 }
 for (const key of ['og:title', 'twitter:title']) html = html.replace(new RegExp(`(<meta\\s+(?:name|property)="${key}"\\s+content=")[^"]*(")`, 'i'), (_, before, after) => before + escape(title) + after);
 // Normalize only links with a known public target; preserve query strings/fragments.
 html = html.replace(/href="(\/[^"?#]*)([?#][^"]*)?"/g, (full, url, suffix = '') => {
  const canonical = url.endsWith('/') ? url : url + '/';
  return pages.has(canonical) ? `href="${canonical}${suffix}"` : full;
 });
 const graph = [];
 if (!html.includes('"WebPage"')) graph.push({ '@type': 'WebPage', '@id': origin + route + '#webpage', url: origin + route, name: title, description, inLanguage: 'en-US', isPartOf: { '@id': origin + '/#website' }, publisher: { '@id': origin + '/#organization' } });
 if (!html.includes('"BreadcrumbList"')) {
  const parts = route.split('/').filter(Boolean);
  const crumbs = [{ '@type': 'ListItem', position: 1, name: 'Home', item: origin + '/' }];
  parts.forEach((_, i) => {
   const ancestor = '/' + parts.slice(0, i + 1).join('/') + '/';
   if (pages.has(ancestor)) crumbs.push({ '@type': 'ListItem', position: crumbs.length + 1, name: pages.get(ancestor).h1, item: origin + ancestor });
  });
  graph.push({ '@type': 'BreadcrumbList', '@id': origin + route + '#breadcrumb', itemListElement: crumbs });
 }
 if (!/name="robots"/i.test(html)) html = html.replace('</head>', '<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1"></head>');
 if (graph.length) html = html.replace('</head>', `<script type="application/ld+json">${JSON.stringify({ '@context': 'https://schema.org', '@graph': graph }).replace(/</g, '\\u003c')}</script></head>`);
 if (route.startsWith('/scenarios/')) {
  const candidates = [['/revenue-projections/', 'How to validate rental revenue projections'], ['/tools/str-revenue-calculator/', 'Short-term rental revenue calculator'], ['/buy-a-short-term-rental/', 'Short-term rental purchase roadmap']];
  const links = candidates.filter(([url]) => pages.has(url) && !html.includes(`href="${url}"`));
  if (links.length) html = html.replace('</main>', `<section class="section"><div class="wrap"><h2>Before using this model to buy</h2><p>Scenario assumptions are illustrative. Verify the property’s actual revenue evidence, full expense budget and purchase requirements.</p><ul>${links.map(([url,label])=>`<li><a href="${url}">${label}</a></li>`).join('')}</ul></div></section></main>`);
 }
 return html;
}
