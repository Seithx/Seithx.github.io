---
layout: post
title: "Hardening My AI Blog's GitHub Actions Workflow"
date: 2026-03-27
source_draft: "drafts/test-draft"
tags: [GitHub Actions, LLM, Gemini, Security, CI/CD, Jekyll]
---

Today was all about giving my automated blog publishing workflow a serious tune-up. This GitHub Actions setup is pretty neat: it grabs my raw notes, sends them through a Gemini LLM for refinement, and then pushes out a polished blog post automatically. While it's been humming along, I dedicated some time to making it more robust, secure, and efficient.

Here's what I tackled:

*   **Security First**: Tackled a subtle but scary shell injection vulnerability. Turns out, directly interpolating LLM output (like a generated title) into bash variables is a no-go. The fix? Simple temp files for safe data handling.
*   **Smarter Scheduling**: Separated the workflow's schedule trigger into its own job. Now, the main publish job only runs when truly needed, saving resources and preventing unnecessary runs.
*   **LLM Swap**: Switched my Gemini model from 2.5 Pro to 2.5 Flash. It's faster and cheaper for my specific use case, which is a win-win for performance and cost.
*   **Cleaner Posts**: Moved post tags from the body directly into Jekyll frontmatter. This makes my posts much tidier and more compliant with Jekyll's best practices.
*   **Precise Git**: Narrowed down `git add` commands to specific directories instead of a blanket `-A`. This reduces the chance of accidentally committing something I shouldn't.

This whole process was a fantastic reminder that even seemingly "working" CI/CD pipelines need a diligent security review. That shell injection vulnerability, in particular, was quite subtle – the LLM's generated title was interpolated directly into a shell variable. It's a stark lesson that simple defensive patterns, like writing to temporary files before processing, are crucial and can prevent major headaches down the line.

Next up: I'm thinking about adding a PR-based review step to the workflow before anything gets auto-published.
