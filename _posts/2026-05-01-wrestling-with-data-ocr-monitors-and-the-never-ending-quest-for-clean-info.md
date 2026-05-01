---
layout: post
title: "Wrestling with data: OCR, monitors, and the never-ending quest for clean info"
date: 2026-05-01
source_draft: "drafts/mikyab-rag-pipeline"
tags: [RAG, data engineering, OCR, content monitor, data pipeline, Hebrew]
---

This past week, I've been deep in the guts of our RAG knowledge base pipeline. The whole point is to build a system that can ingest a ton of diverse content, like articles, Q&As, and transcripts, and make it searchable for our RAG models. It's all about getting good, clean data into the system so the AI can actually do its job.

Here's what's been happening:

*   **Hebrew OCR notebook:** I finally tackled Hebrew OCR. A lot of our source material is scanned documents or images in Hebrew, so this was a big step. I put together a notebook, which feels like a solid foundation, and made sure to link up backup info for the processed files. Don't want to lose that output.
*   **New content monitor:** I built out a monitor for a specific source. This thing automatically downloads new content and pushes it through our conversion pipeline. It sounds simple, but getting it right was a beast.
    *   I refined the URL matching to be manifest-based, which is way more robust than my initial naive approach.
    *   Canonical URL checks were crucial to avoid downloading duplicates. Nothing worse than redundant data clogging the system.
    *   The `convert_all.py` script needed tweaks. Q&A content requires a different touch than regular articles, so it got some love to handle both properly.
    *   A small but annoying fix: parsing dates for answers. Sometimes an author prefix messes things up, so I added logic to strip that out and fall back to the published date if needed. Data cleaning, man, it's always the little things that bite you.
*   The hardest part was getting that content monitor to be truly reliable. It's one thing to write a script that downloads *some* stuff, another to build something that consistently ingests *all* new content without breaking or duplicating. Each "fix monitor" commit felt like a small battle won against the chaos of real-world data.
*   I've also got about 2,000 online lesson transcripts waiting in the wings, but that's currently blocked on someone else. Sometimes the biggest blockers aren't technical.

It's been a mix of satisfaction and mild frustration. There's a real sense of accomplishment when the monitor pulls in new content flawlessly, or when the OCR spits out readable Hebrew. But then there's the grind of debugging why a date isn't parsing correctly. It really hammers home the importance of robust, fault-tolerant data pipelines. You can have the fanciest RAG model, but if the data going in is garbage, the output will be too. This process is teaching me a lot about the "dirty work" of AI, the data engineering side that's absolutely critical.

Next: Get those ~2,000 online lesson transcripts processed once they're unblocked.
