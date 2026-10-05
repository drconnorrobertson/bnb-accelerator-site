// Resource navigation belongs on the production site rather than legacy GitHub Pages microsites.
export const resourceRoutes = new Map([
  ['https://drconnorrobertson.github.io/bnb-your-first-str/', '/buy-a-short-term-rental/'],
  ['https://drconnorrobertson.github.io/bnb-case-study/', '/case-studies/'],
  ['https://drconnorrobertson.github.io/bnb-top-places-str-2026/', '/markets/'],
  ['https://drconnorrobertson.github.io/bnb-value-add-str-guide/', '/design/'],
  ['https://drconnorrobertson.github.io/bnb-acquisition-system/', '/how-it-works/'],
]);

export function normalizeResourceLinks(html) {
  return html.replace(/(<a\b[^>]*href=)(["'])(.*?)\2([^>]*>)([\s\S]*?)(<\/a>)/gi,
    (full, before, quote, href, attributes, label, closing) => {
      const route = resourceRoutes.get(href);
      if (!route) return full;
      const labels = {
        '/markets/': 'STR Markets',
        '/design/': 'STR Design & Launch',
      };
      return before + quote + route + quote + attributes + (labels[route] || label) + closing;
    });
}
