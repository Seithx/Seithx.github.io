---
layout: post
title: "Browser as backend: When fighting auth is the wrong fight"
date: 2026-05-29
source_draft: "drafts/browser-automation-journey"
tags: [Playwright, FastAPI, headless browser, authentication, API wrapper, debugging]
---

I just wrapped up the most frustrating, then most satisfying, engineering sprint in months. My goal was to build a REST API wrapper around a web application that has no public API. I wanted clean endpoints to integrate it with my other tools and build a custom chat interface.

Auth was the immediate nightmare. This app has aggressive session management and its login flow changes constantly. My first attempt, the textbook solution of extracting and replaying auth tokens, worked for about two hours before everything broke. Automated refresh (v2) was better, but token lifetimes were unpredictable. I was constantly firefighting.

Then it hit me: what if the browser *is* the backend? Instead of trying to reverse-engineer tokens, I could keep a persistent headless Playwright browser running and execute all API calls inside its JavaScript context. The browser handles cookies, CSRF, session refresh, everything. I just call `page.evaluate(fetch)` and the request goes out with full session context.

It sounds almost too simple, but getting here took weeks of iteration:

*   I replaced my custom HTTP client with a community SDK for encoding and decoding.
*   Built persistent browser profiles so the browser remembers its login across restarts.
*   Wrote a 16-endpoint smoke test to validate every API route.
*   A 24-hour endurance test simulates real user behavior across multiple sessions.
*   Added heartbeat monitoring with structured JSONL logging.
*   Built a keep-alive supervisor as a safety net.

The struggles were real. Periodically refreshing the page, counterintuitively, *killed* the session instead of keeping it alive. That one cost me hours of debugging. I also had to distinguish auth failures from transient network errors, which needed different retry strategies. Login UI selectors changed across app updates, breaking automation silently. Windows had encoding quirks that made logging output garbled, and the browser's cache got corrupted once, requiring a detection and cleanup mechanism.

The whole thing now runs as a FastAPI server backed by a headless Chromium instance. It's been stable for days. The architecture feels elegant in its simplicity: the browser does what browsers do best, and I just provide the REST interface on top. This project taught me that sometimes fighting a system's auth model is the wrong approach entirely. Instead of reverse-engineering the lock, just use the door. It connects back to something I keep learning: the best engineering solutions often feel obvious in hindsight.

Next: concurrent user support and a proper error recovery pipeline.
