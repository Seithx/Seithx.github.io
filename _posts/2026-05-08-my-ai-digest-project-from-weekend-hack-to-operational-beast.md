---
layout: post
title: "My AI digest project: From weekend hack to operational beast"
date: 2026-05-08
source_draft: "drafts/information-hub"
tags: [AI, LLM, Docker, Windows, Automation, Personal Project, Gemini, Debugging]
---

This whole thing started simple. I'm in dozens of messaging groups, everything from professional communities to neighborhood chats. Keeping up was impossible. I'd open an app and see 500+ unread messages across 30 groups. Most of it was noise, but the important stuff was buried deep.

So I built a monitor. It watches my groups and generates an AI-powered digest, a concise summary of everything important, organized by topic. Gemini handles the AI part. That worked great. Then, naturally, scope creep kicked in.

Now it also:
*   Ingests email newsletters via IMAP polling and includes them in the digest.
*   Filters online articles using the LLM as a relevance judge based on my interest profile.
*   Has separate digest pipelines for different content categories (tech, community, religious content).
*   Auto-forwards the daily digest to relevant groups with randomized timing.
*   Respects schedule constraints, it knows about holidays and off-hours.
*   Sends push notifications when something critical happens, like session loss or system failures.

Honestly, the operational side was half the project, maybe more.

*   **Fighting Windows and Docker:** My system runs in Docker on my Windows desktop. Docker Desktop crashes sometimes, and Windows loves sleep mode or random updates. I had to build a whole keep-awake system just to stop the PC from sleeping. Talk about fighting the OS!
*   I built a watchdog with escalating recovery: restart container, then restart Docker, then alert me.
*   **Catch-up logic and duplicates:** When the system came back from downtime, it needed to process missed messages without creating duplicates. I cleaned up over 2000 duplicate records from the early days before I got dedup right. Felt amazing when that finally worked.
*   **LLM prompt engineering:** Getting the digest quality right took many iterations. Gemini would either be too verbose (defeating the purpose) or miss important things. I ended up giving the prompt group names and content categories as context, telling it to be as long as needed but only skip truly redundant content.
*   Some messaging groups have permanently broken API responses. No fix available upstream. I just had to accept it and handle the errors gracefully.

This started as a weekend hack. Now it's the tool I check every morning before anything else. It's like having a personal research assistant that reads everything I can't and tells me what matters. I showed this to a friend and they said, "you built a product." I don't know about that, but it's definitely the most complex system I've built on my own.

Next: Migrating it to a Raspberry Pi so it doesn't depend on my desktop being awake.
