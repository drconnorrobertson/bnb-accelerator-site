// Reuse the approved homepage shell; retain each page's main content and tools.
import { readFileSync } from 'node:fs';
import { createHash } from 'node:crypto';
const home = readFileSync('index.html', 'utf8');
const header = home.match(/<header\b[\s\S]*?<\/header>/)[0];
const footer = home.match(/<footer\b[\s\S]*?<\/footer>/)[0];
const menuNames = [...header.matchAll(/<a[^>]*href="([^"]*)"[^>]*>([^<]*)<\/a>/g)].map(([,url,name])=>({url:'https://www.bnbaccelerator.com'+url,name}));
const dialog = home.match(/<dialog\b[\s\S]*?<\/dialog>/)[0];
const revision = file => createHash('sha256').update(readFileSync(file)).digest('hex').slice(0, 12);
const style = `/assets/nonhome-theme.css?v=${revision('assets/nonhome-theme.css')}`;
const application = `/assets/nonhome-application.js?v=${revision('assets/nonhome-application.js')}`;
const base = `/assets/style.min.css?v=${revision('assets/style.min.css')}`;
const behavior = `/assets/main.js?v=${revision('assets/main.js')}`;
export function normalizeNonhomeDesign(html, path) {
 if (path === 'index.html' || !path.endsWith('.html')) return html;
 if (html.includes('data-bnb-design="homepage"')) return html;
 html = html.replace(/<body([^>]*)>/i, (_, attrs) => {
  const cls=attrs.match(/class="([^"]*)"/);
  return `<body${cls ? attrs.replace(cls[0], `class="${cls[1]} bnb-theme"`) : attrs + ' class="bnb-theme"'} data-bnb-design="homepage">`;
 });
 if (/<header\b/i.test(html)) html = html.replace(/<header\b[\s\S]*?<\/header>/i, header);
 else html = html.replace(/<body[^>]*>/i, '$&' + header).replace(/<nav class="research-nav"[\s\S]*?<\/nav>/i, '');
 const existingFooter=html.match(/<footer\b[\s\S]*?<\/footer>/i);
 if (existingFooter && html.indexOf(existingFooter[0]) < html.indexOf('</main>')) {
  const local=existingFooter[0].replace(/<footer[^>]*>/i,'<nav class="resource-footer" aria-label="Resource navigation">').replace(/<\/footer>/i,'</nav>');
  html=html.replace(existingFooter[0],local).replace('</main>','</main>'+footer);
 } else if(existingFooter) html=html.replace(existingFooter[0],footer);
 else html=html.replace('</body>',footer+'</body>');
 if (!html.includes('/assets/style.min.css')) html=html.replace('</head>',`<link rel="stylesheet" href="${base}"></head>`);
 if (!html.includes('fonts.googleapis.com')) html=html.replace('</head>','<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap"></head>');
 html=html.replace('</head>',`<link rel="stylesheet" href="${style}"></head>`);
 if (path.startsWith('resources/')) html=html.replace(/<main class="research-content">([\s\S]*?)<\/main>/i, (_,content)=>{
  const boundary=content.search(/<(?:section|aside)\b/i);
  const intro=boundary<0?content:content.slice(0,boundary), body=boundary<0?'':content.slice(boundary);
  return `<main id="main"><section class="hero hero-page"><div class="wrap"><div class="hero-inner">${intro}</div></div></section><div class="research-content">${body}</div></main>`;
 });

 if (path.startsWith('scenarios/')) {
  const nav='<nav class="library-nav" aria-label="Scenario library"><a href="/scenarios/">Scenario library</a><a href="/scenarios/playbooks/">Operator playbooks</a><a href="/scenarios/methodology/">Methodology</a><a href="/scenarios/glossary/">Glossary</a></nav>';
  html=html.replace('</header>','</header>'+nav);
  html=html.replace('<footer','<aside class="library-note"><div class="wrap">Scenario research is educational and does not represent BNB Accelerator’s active acquisition footprint. Models are illustrative: verify current local rules, insurance, financing and property-level evidence before acting.</div></aside><footer');
 }
 // Existing page scripts keep their behavior; supply the shared menu only if absent.
 if (!html.includes('/assets/main.js')) html=html.replace('</body>',`<script src="${behavior}" defer></script></body>`);
 html=html.replace('</body>',`${dialog}<script src="${application}" defer></script></body>`);
 // Navigation schema must describe the visible shared menu.
 html=html.replace(/(<script[^>]*type="application\/ld\+json"[^>]*>)([\s\S]*?)(<\/script>)/g, (_,open,json,close)=>{
  const data=JSON.parse(json);
  function update(node){
   if (!node || typeof node!=='object') return;
   if(node['@type']==='SiteNavigationElement'){node.name=menuNames.map(x=>x.name);node.url=menuNames.map(x=>x.url);}
   for(const value of Object.values(node)){if(Array.isArray(value)) value.forEach(update);else if(value && typeof value==='object') update(value);}
  }
  update(data);
  return open+JSON.stringify(data).replace(/</g,'\\u003c')+close;
 });
 return html;
}
