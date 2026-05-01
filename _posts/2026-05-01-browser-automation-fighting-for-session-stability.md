---
layout: post
title: "Browser automation: Fighting for session stability"
date: 2026-05-01
source_draft: "drafts/notebooklm-chatwrapper"
tags: [browser automation, playwright, authentication, web sessions, reliability, debugging, stateful systems]
---

This project wraps a complex web application in an API, letting other services interact with it programmatically. This past week was all about making that *actually* reliable, especially around authentication and session persistence.

*   **SDK integration and `storage_state.json`:** We ditched our custom client for the official SDK, which felt like a no-brainer for stability. The big win was getting native authentication working using Playwright's `storage_state.json` for session saving. This immediately led to tackling automated session refresh, because these things *will* expire.
*   Auth hardening was a beast. I added robust cookie validation after export, with backoff on repeated failures, and crucially, made sure we *never* overwrite a valid `storage_state.json` with invalid cookies. Distinguishing between genuine auth errors and transient network glitches in the `keep_alive` loop was a subtle but important fix.
*   Those pesky CSRF tokens were silently killing sessions. We started auto-rebuilding the client every 25-35 minutes with jitter to refresh them. Auto-retrying chat RPC errors with a rebuilt client was another key reliability improvement.
*   **Browser-as-runtime shift:** The biggest architectural change was moving all RPC calls through a persistent Playwright browser instance. This simplified the `keep_alive` logic significantly and felt much more robust. I also realized periodic page refreshes were inadvertently killing active sessions, so those got disabled.
*   Google login is always a "fun" challenge, especially with the account chooser. After all that, I ran 24-hour endurance tests, simulating human-like pacing across two separate notebooks. Brutal, but crucial for finding long-tail issues like memory leaks or services silently dropping connections after a few hours.

This past week felt like a deep dive into the trenches of making something truly robust. It wasn't about flashy new features, but grinding through the details, fixing subtle bugs, and building resilience. There were moments of frustration, especially when a session would mysteriously die after an hour. But the satisfaction of seeing the endurance tests run for 24 hours without a hitch was immense. Reliability isn't a feature you add; it's a continuous process of refinement and anticipating failure. I feel like I've leveled up my understanding of stateful systems and the sheer complexity of modern web applications.

Next: Scaling for concurrent users, multi-session support, and proper process supervision with Docker.
