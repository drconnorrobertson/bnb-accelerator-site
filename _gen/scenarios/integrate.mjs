#!/usr/bin/env node
/** Normalize generated scenario-library pages for the main BNB Accelerator site. */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const scenarioRoot = path.join(root, 'scenarios');
const files = [];

function walk(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const target = path.join(dir, entry.name);
    if (entry.isDirectory()) walk(target);
    else if (entry.name === 'index.html') files.push(target);
  }
}

walk(scenarioRoot);

for (const file of files) {
  let html = fs.readFileSync(file, 'utf8');
  html = html
    .replaceAll('https://bnb-accelerator-library.vercel.app/markets', 'https://www.bnbaccelerator.com/scenarios')
    .replaceAll('https://bnb-accelerator-library.vercel.app/playbooks', 'https://www.bnbaccelerator.com/scenarios/playbooks')
    .replaceAll('https://bnb-accelerator-library.vercel.app/methodology', 'https://www.bnbaccelerator.com/scenarios/methodology')
    .replaceAll('https://bnb-accelerator-library.vercel.app/glossary', 'https://www.bnbaccelerator.com/scenarios/glossary')
    .replaceAll('href="/markets', 'href="/scenarios')
    .replaceAll('href="/playbooks', 'href="/scenarios/playbooks')
    .replaceAll('href="/methodology', 'href="/scenarios/methodology')
    .replaceAll('href="/glossary', 'href="/scenarios/glossary')
    .replace(/href="\/scenarios\/(?!playbooks)([a-z0-9-]+)\/([a-z0-9-]+)"/g, 'href="/scenarios/$1/#scenarios"')
    .replace(/(<link rel="canonical" href="https:\/\/www\.bnbaccelerator\.com\/scenarios[^"#]*?)(?<!\/)(")/g, '$1/$2')
    .replace('href="/favicon.svg"', 'href="/assets/favicon.svg"')
    .replace('Research coverage is not a representation of BNB Accelerator’s active acquisition footprint.', 'Research coverage is educational and is not a representation of BNB Accelerator’s active acquisition footprint.')
    .replace('<a class="chip" href="https://www.bnbaccelerator.com/apply/">Work with us ↗</a>', '<a class="chip" href="/apply/">Work with us ↗</a>');
  fs.writeFileSync(file, html);
}

console.log(JSON.stringify({ normalizedScenarioPages: files.length }));
