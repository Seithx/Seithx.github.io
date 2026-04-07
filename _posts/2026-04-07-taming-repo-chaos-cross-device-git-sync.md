---
layout: post
title: "Taming the Repo Chaos: Building a Cross-Device Git Sync Automation"
date: 2026-04-07
tags: [Git, Automation, PowerShell, DevOps]
---

The past few days have been a wild ride getting my multi-computer workspace to a state I'm actually proud of. Managing over 30 side projects--ranging from RAG pipelines to Chrome extensions--across three different machines (a Work PC, a Work Laptop, and a Personal Laptop) had turned into an absolute nightmare of scattered code and out-of-sync branches. The big push this week was all about achieving a seamless, automated synchronization workflow without accidentally wiping out uncommitted local work. It turned out to be a much bigger beast than I anticipated.

Here's what I wrestled with to get this sync system out the door:

*   **The Desktop Clutter Nightmare:** Achieving a truly unified workspace was a beast. I had repositories scattered across desktop roots, duplicate folders, and nested `.git` wrappers hiding the actual code. The fix? A massive PowerShell audit and consolidation script to move, merge, and clean up everything into a strict, unified `Projects` directory structure on all three machines.
*   **The Large File Pitfalls:** A nasty push rejection caused my `EnhanchedSynagouge` repo to completely freeze up. Turns out, 500MB+ Docker executables and 300MB `.tar` files were accidentally baked into the commit history, triggering GitHub's file size limits. The fix? A surgical `git reset --soft` and `git rm --cached` to rewrite the local Git history and aggressively ignore heavy binaries. Less bloat, faster pushes!
*   **Git Quirks and Detached HEADs:** Ran into classic Git horrors: locked `index.lock` files crashing operations, detached HEADs on my YouTube archive project, and `refusing to merge unrelated histories` errors after re-cloning. Small things, but they quickly add up when you're trying to batch-sync 30+ repositories at once.
*   **Building My Own Tools:** To really solve the daily sync issue, I built a custom PowerShell background automation. Instead of risky auto-commits, it runs daily via Windows Task Scheduler, smartly fetches updates (skipping repos that are already clean), pulls new remote changes, and generates a daily Markdown report. If there are dirty repos needing my attention, it triggers a persistent Windows Toast notification and drops a clickable shortcut right on my desktop.

Honestly, this period felt like a marathon. There were moments of pure frustration, staring at endless Git conflict errors and 1.5GB orphaned build folders, but also immense satisfaction in slowly chipping away at the organizational chaos. It reinforced that sometimes you need to step back and build your own tools to manage your workflow, and that persistence, even when you feel like you're going in circles with Git rebases, eventually pays off. Having all three computers perfectly in sync and monitoring themselves feels like a huge weight off my shoulders.

**Next:** Monitor the daily sync reports and actually get back to building things!

---
**GitHub**
**LinkedIn**
asaflecht@gmail.com
*Developer learning journal by Asaf Lecht. AI automation, browser tooling, RAG pipelines, and Hebrew tech.*
