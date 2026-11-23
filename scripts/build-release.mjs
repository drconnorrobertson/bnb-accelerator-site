import { execFileSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
const cwd = fileURLToPath(new URL('../', import.meta.url));
const steps = [
  ['python3', ['scripts/build_social_library.py']],
  ['python3', ['scripts/build_buyer_verification_guides.py']],
  ['python3', ['scripts/build_operating_calculators.py']],
  ['python3', ['scripts/refresh_comparison_intent.py']],
  [process.execPath, ['build_public.mjs']],
  ['python3', ['scripts/commercial-comparisons.py', 'public']],
  [process.execPath, ['scripts/instrument-conversions.mjs', 'public', 'preserve-home']],
  [process.execPath, ['scripts/repair-index-discovery.mjs', 'public']],
  ['python3', ['scripts/curate-indexing.py', 'public']],
  ['python3', ['scripts/sync-site-index.py', 'public']],
  [process.execPath, ['scripts/contextual-crosslinks.cjs', 'public']],
  ['python3', ['scripts/apply-social-videos.py', 'public']],
  ['python3', ['scripts/apply-provider-research.py', 'public']],
  ['python3', ['scripts/test-social-provider-content.py', 'public']],
  [process.execPath, ['scripts/brand-check.mjs', 'public']],
  ['python3', ['scripts/check-social-library.py', 'public']],
  ['python3', ['scripts/check-production-seo.py', 'public']],
  ['python3', ['scripts/check-comparison-intent.py', 'public']],
];
for (const [command, args] of steps) {
  execFileSync(command, args, { cwd, stdio: 'inherit' });
}
