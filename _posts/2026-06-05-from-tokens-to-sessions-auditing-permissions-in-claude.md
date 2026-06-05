---
layout: post
title: "From tokens to sessions: auditing permissions in Claude"
date: 2026-06-05
source_draft: "drafts/claude-session-audit"
tags: [claude, audit, permissions, sessions, debugging, javascript]
---

My `claude-session-audit` project started life as `claude-token-audit`, focused on just tokens. But I quickly realized that wasn't enough. The goal is still to shine a light on permissions in the Claude system, making sure access is secure and well-defined. This past week, things really shifted.

*   The big one was renaming the project. It wasn't just cosmetic, it reflected a real pivot from just tokens to understanding full sessions. A bit humbling to admit the initial scope was off, but it feels right.
*   I landed `permission_audit.mjs`. This checks for "coverage gaps" in our `permissions.allow` definitions. Defining what a "gap" actually *is* was surprisingly tricky, not just allowed or denied but what *should* be allowed based on expected behavior.
*   Then came `permission_friction.mjs`. This one tries to spot where users hit friction because of permissions. Quantifying "friction" is a beast, I'm still tweaking the heuristics to avoid false positives and catch real pain points.
*   Usability got some love too. Smoother first-time install, per-file progress bars (makes scans feel faster), and better "sub-agent walk" logic. That walk logic, though, threw up some nasty recursion issues when dealing with different states, like trying to map a maze that keeps changing.

This period felt like a real turning point. The rename solidified the direction, which is a good reminder that it's fine to pivot and refine your understanding of a problem. I definitely felt the frustration fighting those tricky logic problems, but seeing the audit results start to make sense was super satisfying. Sometimes you just have to build the tool to understand the problem itself.

Next: Refine friction detection and start visualizing the audit results.
