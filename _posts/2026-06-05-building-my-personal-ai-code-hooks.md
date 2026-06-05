---
layout: post
title: "Building my personal AI code hooks"
date: 2026-06-05
source_draft: "drafts/claude-hooks"
tags: [AI, developer tools, bash, claude, python, workflow, debugging, documentation]
---

I've been using AI assistants a lot at work, and some patterns and scripts there are super useful. The idea behind `claude-hooks` is to pull those generic bits out and build a personal toolkit. I want AI directly in my dev workflow, making it easier to get quick answers, refactor suggestions, or understand complex code without leaving my terminal. It's about making my personal coding life smarter.

*   **Porting the `rtk` hook:** First up was getting `rtk` and its helper `rtk_report.py` into the new setup. This hook is great for generating summaries based on code context, and I somehow missed it in the very first commit. Classic.
*   **Fighting `grep` and `find` output:** The `rtk` hook had this annoying bug where it'd mess up output from `grep` or `find` commands. My workaround, `exclude_commands`, felt clunky but fixed it for now. Man, those little things really get you.
*   **Installation quirks:** Getting `claude-hooks` set up was a bit of a minefield. I had to document a "read-once copy-not-junction" approach (don't symlink, just copy files) to avoid weird issues. Plus, `tiktoken` for API cost management needed a mention, and another general `rtk` gotcha.
*   **`smart-ask-bash` integration:** Later, I pulled in `smart-ask-bash`. This one is fantastic for getting AI help directly in the bash shell, like "how do I do X with Y command?" It was mostly a copy-paste from a team config, but still needed some tweaking to make it truly generic.

Honestly, this whole process has been a mix of excitement and minor frustration. It's incredibly satisfying to build something for myself that I know will genuinely improve my workflow. But that `grep`/`find` bug in `rtk` was a head-scratcher for a bit, and the installation quirks made me realize how much friction there can be even in a simple setup. It really hammered home the importance of good, clear documentation, even if the user is just future me. Generalizing code from a specific context isn't always straightforward, you have to really think about dependencies and assumptions. Still, seeing these hooks come to life and knowing I'm building a powerful personal tool feels great.

Next: Refine existing hooks and explore adding more AI-powered refactoring tools.
