import fs from 'node:fs';
const path = 'scb-precall/index.html';
let html = fs.readFileSync(path, 'utf8').replace(/ target="_blank"/g, ' target="_self"');
html = html.replace(/(<div class="bnb-video"[^>]*>\s*<iframe[^>]*src="https:\/\/(?:www\.)?(?:youtube\.com|youtube-nocookie\.com)\/embed\/([\w-]{11})[^\"]*"[^>]*><\/iframe>\s*<\/div>)(?!<p class="embed-fallback")/g, (_, block, id) => block + '<p class="embed-fallback"><a href="https://www.youtube.com/watch?v=' + id + '" target="_self" rel="noopener noreferrer">Open this video on YouTube</a> if the player does not load.</p>');
html = html.replace(/<strong>Video Breakdown<\/strong>(?!<\/a>)/g, '<span class="resource-unavailable">Video not provided</span>');
const heading = 'Explore the original proformas and video breakdowns.</h3>';
if (!html.includes('Resource links open directly')) html = html.replace(heading, heading + '<p class="resource-note">Resource links open directly in this tab. Use your browser’s Back button to return; missing source videos are labeled below. Google Sheets or third-party resources may require access from their owner.</p>');
fs.writeFileSync(path, html);
// The copied California embed has a ten-character ID, not a valid YouTube ID.
html = html.replace(/<div class="bnb-video"><iframe src="https:\/\/www.youtube-nocookie.com\/embed\/TD07X-8Rok"[^>]*><\/iframe><\/div>/g, '<p class="resource-unavailable">This source video link is incomplete. Ask the team for the updated California market-selection video on your call.</p>');
fs.writeFileSync(path, html);
