---
layout: post
title: "Auto-GIT: Trusting the machine (or, how I learned to stop worrying and love the auto-commit)"
date: 2026-06-09
source_draft: "drafts/auto-git"
tags: [git, automation, devops, workflow, ssh, config]
---

This past week, I dove deep into automating my personal Git workflow, which I'm calling "Auto-GIT." The whole point is to eliminate my own forgetfulness. I want my personal work always backed up, and my dev environment configs (like my `~/.claude` setup) perfectly consistent across all my machines, without me having to think about it. It's about reducing mental overhead and making sure I never lose a day's work because I forgot to push.

Here's what went down:

*   **Installer got a big upgrade.** It now generates SSH keys, rewrites existing HTTPS remotes to SSH (essential for unattended automation), and even opens GitHub to add the new key. Making it idempotent was a fun puzzle; it only opens the browser if a *new* key is generated.
*   **Config syncing.** I started syncing my `~/.claude` config to a special repo. Initially daily, I quickly bumped that to hourly, adding a "time-aware push window" to avoid pushing during active work or at odd hours.
*   **Hourly auto-commits.** This was the scariest part: implementing hourly auto-commits for my personal repos. This is where "trusting the machine" really comes in. To make it palatable, I built in "tier-3 safety": a local backup before any push, a dry-run mode, a "big-diff guard" to stop huge unintended changes, and a 7-day push window.
*   **Fighting the fear of automation gone wrong** was tough. Auto-committing and pushing is inherently risky. Defining what constitutes a "big diff" for the guard was a heuristic challenge, not a perfect science. The 7-day window logic needed careful thought to avoid pushing old stuff or missing new changes. Idempotency and time zones also threw some curveballs.

It's a weird mix of excitement and anxiety. Excitement because this is exactly the kind of automation I crave, but anxiety because I'm literally giving a script permission to commit and push my work. It's a big step in learning to trust my own code, and to build in enough safeguards that I *can* trust it. This project feels like a direct response to my own human fallibility, and it's incredibly satisfying to build tools that make my life easier.

Next: Refining the safety features and expanding to more config files.
