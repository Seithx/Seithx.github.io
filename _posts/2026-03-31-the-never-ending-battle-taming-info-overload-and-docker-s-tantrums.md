---
layout: post
title: "The Never-Ending Battle: Taming Info Overload (and Docker's Tantrums)"
date: 2026-03-31
source_draft: "drafts/waha-monitor"
tags: [LLM, Docker, System Design, Debugging, Information Overload, Python]
---

My personal info hub project is all about wrangling the daily firehose of information – WhatsApp, newsletters, articles – into a digestible, LLM-generated summary. This past couple of weeks has been a whirlwind of shoring up existing systems and pushing forward with new ingestion pipelines, all while battling some truly stubborn tech gremlins.

Here's the lowdown on the wins and the woes:

*   **Victory over Duplicates & System Fortification**: Purged over 2200 duplicate messages – felt *amazing*. Also gave the watchdog a massive upgrade, adding crash forensics, bumping log retention, and refining `keep_awake` logic for true robustness, especially around Shabbat.
*   **New Ingestion Streams**: Got email newsletter ingest working via Gmail IMAP polling, which is huge. Also laid the groundwork for a Medium article pipeline, involving Gemini for filtering, Freedium for fetching, and some custom TOON-lite compression.
*   **Docker & OS Headaches**: The watchdog battle was real. Docker Desktop crashing, WSL issues, and PowerShell syntax errors led to implementing escalating Docker recovery scripts – from a simple restart to unregistering WSL. Talk about fighting the OS!
*   **WhatsApp's Stubborn Side**: Discovered 6 groups are *permanently* failing to fetch messages with no upstream fix, meaning I'm missing chunks of personal data. Plus, getting RTL rendering right for WhatsApp digests was surprisingly fiddly, needing a regex fix for the *first meaningful character*.
*   **Obscure Tech Quirks**: From Windows' `SC_MONITORPOWER` triggering "Modern Standby" (the opposite of `keep_awake`) to an LLM SDK upgrade (`google-genai`) throwing an `AttributeError` until I figured out new `ThinkingConfig` syntax – it's always something unexpected.

This period felt like a grind, but a deeply productive one. It's a constant reminder that building robust systems isn't just about features; it's about anticipating failure, building layers of resilience, and debugging those obscure interactions between your code, the OS, and external APIs. The satisfaction of squashing those 2200 duplicates or getting Docker to reliably restart is immense, even if it feels like patching a leaky boat sometimes. Persistence and detailed logging are truly lifesavers.

Next up: Implement those admin API endpoints and get the full Medium pipeline running.
