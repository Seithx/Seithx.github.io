---
layout: post
title: "My Epic Debugging Log for a YouTube Data Scraper"
date: 2025-10-17
---

I wanted to build a simple script to pull video lists from YouTube—specifically, all uploads from a specific channel and custom searches for Hebrew kids' content. I figured it would be a quick job with `yt-dlp` and a bit of Bash. Of course, it turned into a deep dive into environment quirks, shell scripting pitfalls, and the nuances of data streaming. It was a bigger time sink than I planned, but I learned a ton.

Here’s a rundown of the key hurdles and what finally worked.

*   **Environment mismatches are deceptive.** My biggest headache was running Linux-style scripts in Git Bash on Windows. Commands like `sudo`, `wget`, and `stdbuf` were missing. Even getting `jq` to work required a wrapper script to call the `.exe` file. The final boss was invisible CRLF line endings breaking my scripts until I ran `sed` to fix them.

*   **Streaming is everything for large playlists.** My script kept hanging silently. The root cause? `yt-dlp` was trying to load massive channel playlists (thousands of videos) into memory all at once. The fix was two-fold: using the `--lazy-playlist` flag to process one item at a time and setting `PYTHONUNBUFFERED=1` to force real-time output from my Python parser.

*   **Bash will let you shoot yourself in the foot.** I love `set -euo pipefail` for making scripts safer, but it also makes them exit silently on the tiniest error. A simple typo (`$-flat-playlist` instead of `$COOKIES --flat-playlist`) cost me an hour. Using `bash -x` to trace execution and `trap` to catch errors became essential for finding the exact line where things went wrong.

*   **Filtering is a post-processing job.** The initial search queries for Hebrew content pulled in a lot of irrelevant videos. The most effective solution wasn't a fancier search, but a simple Python filter. I piped the JSON output through a script that checked if the title or uploader name contained any characters in the Hebrew Unicode range (`\u0590`–`\u05FF`).

### Reflection

This started as a "quick" side project and ended up being a reminder that the glue holding tools together—the shell scripts, the environment configuration—is where things usually break. Every error, from a simple typo to a fundamental misunderstanding of I/O buffering, was a learning opportunity. It was frustrating, but solving each piece of the puzzle was incredibly satisfying.

**Next:** Use this pipeline to actually build the filtered kids' content playlists I set out to create.

---
*Tags: yt-dlp, bash, python, data-engineering, debugging, automation*
