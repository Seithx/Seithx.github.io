---
layout: post
title: "WhatsApp bot: From zero to (almost) hero"
date: 2026-07-14
source_draft: "drafts/notebooklm-whatsapp-bot"
tags: [whatsapp, bot, rag, kapso, ux, monitoring]
---

This past week, I took our internal RAG system, which is great for knowledge retrieval, and started making it available via WhatsApp. The idea is to use a layer I'm calling "Kapso" as the bridge: WhatsApp -> Kapso -> RAG -> Kapso -> WhatsApp. The goal is quick, conversational access to our knowledge base. It's been a sprint getting the core bot running and then hardening it like crazy.

Here's what went down:

*   **Initial setup and UX polish.** I got the core Kapso-to-RAG flow working, handling audio messages (referring them to "Eliezer" for now), and making sure new users got a friendly welcome message, but only once per user, ever. Then came the small but mighty UX wins, like read receipts and fixing the typing indicator to show *after* the initial ack, not before. That little detail made a huge difference in how janky it felt.
*   **Robustness and conversation management.** I implemented the 3900-character WhatsApp limit and crucial per-user serialization to prevent conversations from getting tangled. Imagine two messages from the same user arriving out of order, chaos! A `/reset` command is a lifesaver for clearing context. I also added "wait-fillers" with fun facts or openers, styled nicely, to keep users engaged during longer RAG queries.
*   **Fighting the system and error handling.** A lot of effort went into logging Kapso send failures (especially those annoying 429 rate limits) instead of silently dropping them. A critical fix was ensuring the RAG's `[1][2]` citation markers weren't stripped out. Losing those meant losing all grounding for the answers, which defeats the purpose of RAG. That was a facepalm moment. I also added a "queued-ack" for when a user sends a follow-up before the previous answer is done, which helps manage expectations.
*   **Monitoring for the unexpected.** I set up a wrapper health monitor with a liveness probe and a daily "DOM-drift canary." This canary checks if Kapso's key UI elements are still where they should be, because their web-based wrapper can be brittle. Pushover alerts for `***-py` version drift and Kapso number health were also quick wins.

This past week felt like a sprint. There were moments of pure flow, just cranking out features and fixes, and then moments of head-scratching frustration trying to debug why a typing indicator wasn't showing up or why messages were silently failing. It's a good reminder that building robust, user-facing systems isn't just about the core logic. It's about anticipating every possible failure mode and edge case, and then making the user experience as smooth as possible despite all that complexity under the hood. I feel like I've leveled up my defensive programming skills.

Next: Exploring more advanced conversational flows and integrating more RAG sources.
