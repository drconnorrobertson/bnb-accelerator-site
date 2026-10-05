// Keep public evidence wording consistent when older generators are rerun.
export function normalizePerformanceDisclosures(html, path) {
  let output = html.replaceAll(
    'Client results shown are actual outcomes for specific properties and are not typical or promised.',
    'Published examples may include recorded tracker figures, client reports, forecasts and tax illustrations. They are not independently verified typical returns; check the source, period, expenses and investment denominator on each example.'
  ).replaceAll(
    '<strong>4.5/5</strong> on Trustpilot',
    '<a href="/reviews/">Review sources and dates</a>'
  );
  if (/^case-studies\/.+\/index\.html$/.test(path)) {
    output = output.replace(
      /\$[\d,]+ a year in cash flow on \$[\d,]+ of cash invested, a [\d.]+% cash-on-cash return\./g,
      'The tracker records annual cash flow and a cash-on-cash percentage; confirm the reporting period, expense coverage and denominator before relying on those fields.'
    );
  }
  return output;
}
