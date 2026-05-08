---
layout: post
title: "Scraping Hebrew news: A deep dive into unexpected complexity"
date: 2026-05-08
source_draft: "drafts/hebrew-text-challenges"
tags: [web scraping, python, google cloud run, hebrew, rtl, data extraction, maintenance]
---

I thought scraping clean article text from Israeli news sites would be a quick win. Just grab the body, right? Turns out, that's one of those problems that looks easy until you actually try it, especially with Hebrew content. I've now got a web service running on Google Cloud Run that handles 17 major Israeli news outlets, but getting here was a proper fight.

*   Most off-the-shelf extraction libraries (like newspaper3k) are built for English. They make assumptions about text direction, paragraph structure, and encoding that just fall apart with Hebrew. RTL text handling adds a whole layer of pain.
*   The tech stacks are wild. One site uses DraftJS, another is AMP, a third has a WordPress API, and a fourth runs on some custom CMS from the early 2000s. Each one needed a unique approach.
*   Some sites are actively hostile to automation. They serve completely different content depending on who's asking, or they're just plain unreachable from cloud infrastructure. Talk about fighting the OS!
*   My solution ended up being a chain of per-site extraction strategies. If the primary CSS selector fails, I try the next one. If that fails, I hit the site's API if it has one. Only as a last resort do I fall back to a generic library.
*   The real work isn't building it, it's keeping it alive. I've done two full audit rounds across all 17 sites, fixing bugs on about half of them. Selectors drift constantly as sites update their markup. It's a never-ending reverse-engineering project.

This project taught me that building a scraper is maybe 20% of the job. Maintaining it is the other 80%. Every site redesign or new content protection layer means another mini-battle. I'm seriously considering if a browser extension approach might be more sustainable long-term. The interesting part here isn't the code, it's the constant problem-solving and learning how the web actually works behind the scenes.

Next: Investigate browser extension feasibility for more robust, long-term extraction.
