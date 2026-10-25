import { execFileSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
const cwd = fileURLToPath(new URL('../', import.meta.url));
const steps = [
  [process.execPath, ['build_public.mjs']],
  [process.execPath, ['scripts/instrument-conversions.mjs', 'public', 'preserve-home']],
  [process.execPath, ['scripts/repair-index-discovery.mjs', 'public']],
  ['python3', ['scripts/curate-indexing.py', 'public']],
  [process.execPath, ['scripts/contextual-crosslinks.cjs', 'public']],
  [process.execPath, ['scripts/brand-check.mjs', 'public']],
];
for (const [command, args] of steps) {
  execFileSync(command, args, { cwd, stdio: 'inherit' });
}
