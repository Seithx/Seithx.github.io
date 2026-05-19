---
layout: post
title: "The whack-a-mole of web extraction (and a Cloudflare Worker deep dive)"
date: 2026-05-19
source_draft: "drafts/extractorarticlesfromisraelinewssites"
tags: [web scraping, Cloudflare Workers, Cloud Run, REST API, debugging, JavaScript]
---

This past week, my Hebrew News Extractor project was a wild ride. I'm building a system to pull structured article data from various Hebrew news sites for personal analysis, a constant battle against website changes and anti-bot measures. It's a fantastic learning ground.

*   I added two more sites, Makor Rishon and Hakol Hayehudi, bringing the total to 17. Expanding the project always feels good.
*   Of course, more sites mean more maintenance. I spent a good chunk of time fixing four extraction bugs that popped up after a recent selector review. It's always whack-a-mole. Calcalist also gave me a headache with its DraftJS content, where fallback logic was outside the main selector loop, leading to empty articles. Got that sorted.
*   Site 14 (C14) was the biggest challenge. Protected by Cloudflare Turnstile, direct HTML scraping was a nightmare. I had a breakthrough earlier by discovering their internal WordPress REST API, which completely bypassed the need to render the full HTML page. This was a huge win for speed and reliability.
*   Even with the API, I hit new issues. API calls sometimes got blocked or timed out, especially on Cloud Run. This sent me down a proxy rabbit hole. I ended up implementing a Cloudflare Worker to proxy C14's API calls. Debugging network issues, increasing timeouts (from default to 30s!), and exposing detailed error messages from the Worker was a whole new level of complexity. The ultimate solution involved making the browser-side fetch directly to the Worker, bypassing Cloud Run's networking entirely for that specific request path. It felt like untangling a giant ball of yarn, but getting it to work reliably was incredibly satisfying.
*   On the more mundane side, I documented the Cloud Run configuration, especially around cold starts and site-specific limitations. I also put together a `deploy.sh` script and updated my `CLAUDE.md` notes.

This week felt like a mix of small wins and one giant, frustrating, but ultimately rewarding battle. Adapting to website changes can be draining, but finding elegant solutions, like the Cloudflare Worker proxy for C14, feels like a real level-up in my understanding of web infrastructure.

Next: Continue refining existing extractors and tackle the next batch of sites.
