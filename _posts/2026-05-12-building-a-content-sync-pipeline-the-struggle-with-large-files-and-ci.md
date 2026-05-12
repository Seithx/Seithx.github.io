---
layout: post
title: "Building a content sync pipeline: The struggle with large files and CI"
date: 2026-05-12
source_draft: "drafts/halachot-orvishua"
tags: [content-sync, CI/CD, git, large-files, automation, data-management]
---

This past week, I kicked off the `halachot-orvishua` project. The idea is a reliable pipeline to pull Jewish law content from `orvishua.net`. I want an automated system that checks for new content, downloads it, and then tells me what changed, especially which "mega-files" need re-uploading. It's about keeping a local, updated copy and knowing what's fresh.

This period was mostly about setting up the core infrastructure and figuring out the content flow.

*   **Scripts-only repo, content on Google Drive:** My first big decision was to make this a "scripts-only repo." The actual content wouldn't live in Git; it would be on Google Drive. This immediately caused problems.
*   **CI facepalm:** My initial CI setup tried to download content. That was a no-go, given the "scripts-only" decision and the sheer size of the content. I had to quickly fix it to a "detect-only" mode where the workflow doesn't try to pull down the actual files. Total facepalm moment, setting CI to do the exact opposite of what I wanted Git to manage.
*   **Core logic: change detection and notifications:** I got the system to detect changes. Crucially, it now specifies *which* sources needed re-uploading and *exactly which mega-files* were affected. This was a big win, the whole point of the project.
*   **Evolving content strategy:** The "scripts-only" idea felt clean, but then I realized I needed *some* representation of the output in Git for tracking. I implemented syncing the output to a git-tracked directory. It felt like a necessary compromise. Later, I reorganized everything: scripts into `scripts/`, tracked content into `content/`, using `new_content/` and `content_index.json` for systematic management. It's a constant battle between keeping it simple and making it robust for large, dynamic data.
*   **Line endings, of course:** Had to add `.gitattributes` and normalize them to LF. Always line endings.

I finally got a successful sync run, pulling down 2 new Q&A items and confirming 0 new articles. That little green checkmark felt good.

Honestly, the hardest part was wrestling with the content strategy. "Scripts-only, content on Drive" seemed clean, but the practicalities of CI, tracking changes, and needing *some* versioned output meant constant re-evaluation. It felt like I was building the plane while flying it. The "mega-files" aspect really drove home that Git isn't always the right tool for *all* data, but you still need a way to track *metadata* about that data. Architectural decisions are rarely one-and-done; they evolve as you understand the problem better.

Next: Refine the notification content and potentially add more robust error handling.
