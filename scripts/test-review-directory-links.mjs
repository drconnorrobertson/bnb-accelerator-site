import assert from 'node:assert/strict';
import { normalizePerformanceDisclosures } from '../performance_disclosures.mjs';

const overview = '<a href="/reviews/">Browse the dated review directory</a>';
assert.equal(normalizePerformanceDisclosures(overview, 'reviews/client-experience-and-review-sources/index.html'), overview,
  'The evidence overview must link to the source directory instead of itself.');
const testimonial = '<a href="/reviews/">Read selected public reviews</a>';
assert.equal(normalizePerformanceDisclosures(testimonial, 'testimonials/index.html'), testimonial,
  'Public-review links must keep their intended destination.');
assert.match(normalizePerformanceDisclosures('<strong>4.5/5</strong> on Trustpilot', 'index.html'),
  /href="\/reviews\/client-experience-and-review-sources\/"/,
  'The undated footer rating still points readers to the evidence explanation.');
console.log('Review-directory destinations preserved; footer evidence disclosure retained.');
