# BNB social content library

The public library lives at `/learn/`. `scripts/build_social_library.py` produces one source-ID-backed page per verified post, static directory pagination, a public search data script, and `sitemap-content.xml`. The release build invokes the generator before assembling public output.

`youtube-inventory.json` contains 87 channel videos and 600 Shorts captured from the public channel on November 22, 2026. Those 687 distinct IDs match the main channel's reported total at collection. The additionalVideos collection adds 129 distinct testimonial-channel and website-linked property recordings, for 816 total YouTube IDs. It includes the older pre-call page's unlisted breakdown links. `youtube-sources.json` holds visible public captions and description evidence. Never represent a title-only record as a captured transcript.

`instagram-evidence.json` and `instagram-search-evidence.json` retain public discovery evidence. Publication requires the publisher-specific permalink to appear on the direct post page. Unrelated personal posts and unverified pages are recorded as exclusions in the publication manifest. Public search is not proof of a complete historical Instagram archive.

Each page has a source embed, a full written companion, related reading, and the collected caption text when available. Captions remain explicitly identified as publisher text or automatic transcription, and are not presented as independent verification of historical claims. The source recording remains linked. Personal-name and unrelated-brand references in transcripts are disclosed and omitted consistently with the existing site-wide editorial policy; the private source evidence is retained unchanged.

`companions.json` contains the editorial topic guides. Source-specific Instagram introductions live in the generator. The library is regenerated deterministically; obsolete generated routes from a previous manifest are removed only from this generator's known route set.

Before release, run `python3 scripts/check-social-library.py public` after the normal release build. It verifies exact coverage of the collected YouTube IDs, one accessible source embed per article, written sections, direct source links, sitemap membership, internal links, and absence of collection records in public output. Browser checks cover search, filters, pagination, source embeds and narrow layouts.
