---
layout: post
title: "Automating the brain: Daily syncs and GitHub Actions fun"
date: 2026-04-24
source_draft: "drafts/rationalbelief-rag-pipeline"
tags: [RAG, GitHub Actions, automation, CI/CD, Python, knowledge base]
---

My RAG Knowledge Base Pipeline project is basically my attempt to build a smart, queryable brain for a specific domain. It pulls info, processes it, and lets me ask questions. The goal is to keep this "brain" fresh without me babysitting it.

This past week was all about making that automation a reality.

*   **Daily sync automation:** Getting the daily content sync fully automated with GitHub Actions was a huge win. No more manually kicking off scripts, it just runs on a schedule now. Big relief.
*   **Email notifications:** I also hooked up email notifications. They started barebones, but now they're actually useful, showing direct URLs to new content, who commented, and which "mega-files" (my term for aggregated content) were affected.
*   **GitHub Actions persistence was a head-scratcher.** My `sync_new_content.py` script would generate an output file, then it'd vanish in the next step. Turns out, I needed to explicitly "dual-write" to a `sync_output/` directory configured to persist. Classic "works on my machine" vs. CI.
*   The eternal battle with line endings popped up. A quick `.gitattributes` addition and a normalization commit fixed it, but man, that's always a minor annoyance.
*   A small refactor to align the sync output layout with an internal pattern just makes things cleaner and more consistent.

Honestly, getting this daily sync fully automated feels like a weight off my shoulders. It's a "set it and forget it" feature that makes the project feel more mature. I learned a lot about GitHub Actions quirks, especially how state and files are handled between steps. CI/CD isn't just for tests, it's a powerful orchestration tool. Seeing those daily emails, knowing the system updates itself without me, is super satisfying. It's a small step, but it feels like a big leap in making this project self-sustaining and reducing my cognitive load.

Next: I want to explore more sophisticated content change detection.
