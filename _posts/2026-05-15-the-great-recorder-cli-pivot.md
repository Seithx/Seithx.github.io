---
layout: post
title: "The great recorder CLI pivot"
date: 2026-05-15
source_draft: "drafts/google-recorder-cli"
tags: [cli, google recorder, api, headless browser, architecture, debugging]
---

My `google-recorder-cli` project is all about bringing Google Recorder's transcription and search to the command line. I use Recorder constantly, but I always wanted more programmatic control, like searching recordings from the terminal or bulk exporting transcripts. This is my personal quest to make that happen. The last week or so has been a whirlwind.

*   **API archaeology:** I kicked things off with a deep dive into the underlying service's API. I spent a "live discovery session" mapping out endpoints, requests, and responses. It felt like being an archaeologist, digging through network requests. Documenting a pretty full API surface felt like a huge win.
*   **Hitting the API wall:** After all that discovery, the hard truth hit: directly interacting with the API was going to be a nightmare. Authentication was complex, payloads intricate, and I felt like I was constantly fighting anti-bot measures. I made the tough call: a complete architectural rewrite for Phase 2-3.
*   **Browser-as-runtime:** I pivoted to a "browser-as-runtime" approach, using a headless browser to interact with the web interface, managed by a "watchdog" process. It feels a bit like admitting defeat on the direct API front, but it's a pragmatic solution. This also meant adding an API monitoring strategy to the TODO list, because a web interface can change.
*   **Squashing a classic:** I squashed a classic bug: a hardcoded path in `snapshot-a11y.js`. Rookie mistake, but it's always satisfying to replace a brittle path with `os.tmpdir()`.
*   **Polishing the CLI:** I've been looking at patterns from other great CLIs, like the `millionco/expect` style, and started incorporating some of those improvements. It's not just about making it work, it's about making it *feel* good to use. I also updated author credits in the docs, adding my Hebrew name and clarifying I *modified* it, not built the original service.

Honestly, the biggest struggle was that API wall. It was frustrating to spend so much time on discovery only to realize the direct approach was a dead end. But the pivot to "browser-as-runtime" felt like a creative workaround, even if it adds complexity I initially wanted to avoid. It's a reminder that sometimes the "ideal" solution isn't feasible, and you have to find a robust "working" solution. Adapting felt good, rather than getting stuck. Seeing the CLI start to feel more polished is always a boost.

Next: Implement core recording search and export functionality using the new architecture.
