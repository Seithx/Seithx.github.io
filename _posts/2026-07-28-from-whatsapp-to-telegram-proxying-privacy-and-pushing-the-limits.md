---
layout: post
title: "From WhatsApp to Telegram: Proxying, privacy, and pushing the limits"
date: 2026-07-28
source_draft: "drafts/hebrew-tts-bot"
tags: [TTS, Telegram, WhatsApp, Proxy, Privacy, Load Testing]
---

This week was a whirlwind getting my Hebrew Text-to-Speech bot ready for prime time. It started as a WhatsApp-only project, born from my own need for decent Hebrew audio. I got the initial bot imported, set up a deploy script, and immediately focused on cost. That meant optimizing OGG re-encoding and routing requests to hit cheaper providers like Hugging Face first, only overflowing to RunPod when needed.

Here's what went down:

*   Hardened the system with guards against duplicate webhooks and poison pills. I also fixed some tricky ordering issues in the reconciler. I spent a ton of time load testing, pushing it to 359 jobs with no drift. Throttling became the ceiling, which felt like a win for stability.
*   Adding Telegram support was a beast. After planning the integration and wiring up the transport, I hit a wall: Hugging Face datacenter IPs were blocked by Telegram for outgoing messages. This led to a scramble for proxying. First a Cloudflare Worker, then even a Deno Deploy proxy because Cloudflare itself got blocked. Talk about fighting the OS! It was a massive headache, but Telegram is finally live.
*   I drafted a detailed privacy policy. This wasn't just boilerplate; thinking through data retention and transparency took more brainpower than I expected. I also revamped usage stats logging from SQLite to append-only JSONL files, splitting them by channel for better scalability.
*   Audited docs for gaps, then built a load-test harness specifically for abuse scenarios. I ran dual-channel stress tests to ensure it wouldn't break or cost a fortune if someone tried to misuse it.

This week felt like a real level-up in operational thinking. I started just wanting to make a bot, but ended up wrestling with network infrastructure, scaling, cost management, and even privacy. The frustration with Telegram blocking was real, but pushing through it and finding a solution (even if it felt a bit hacky with multiple proxies) was incredibly satisfying. It taught me that sometimes the biggest challenges aren't in the code itself, but in the environment it runs in. It also reinforced the importance of robust testing, not just for functionality but for performance, cost, and abuse prevention. I feel like I'm growing beyond just a coder.

Next: Refine the Telegram integration and keep monitoring for abuse vectors.
