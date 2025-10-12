---
layout: post
title: "Wrangling yt-dlp: A Debugging Log for My YouTube Scraper"
date: 2025-10-12
---

I wanted to build a simple automation to pull video metadata from YouTube—specifically, for a Hebrew kids' channel and some general searches. I figured a little `yt-dlp`, Bash, and Python would do the trick. Of course, what seemed like a quick project turned into a multi-hour debugging session. It wasn't a top priority, but I definitely sank some time into wrestling with it.

Here are the key things I fought with and fixed along the way.

*   **The Environment Fought Back:** Scripting on Windows with Git Bash is its own adventure. I immediately hit a wall with missing commands like `sudo`, `wget`, and `stdbuf`. The biggest headache was getting `jq` to work; I had to create a custom Bash wrapper just to call the `.exe` file correctly from my scripts.
*   **Why is it Hanging?!** My script would often run and then just… stop. No errors, no progress. The two culprits were I/O buffering and huge channel playlists. The fix was a combination of setting `PYTHONUNBUFFERED=1` and adding the `--lazy-playlist` flag to `yt-dlp` so it would stream the video metadata instead of loading it all into memory.
*   **Classic Bash Gotchas:** I spent way too long on a silent failure caused by `set -e` combined with a tiny syntax error. Another classic was a typo: `$-flat-playlist` instead of `$COOKIES --flat-playlist`. The shell interpreted `$-` as a special variable, and everything broke. Using `bash -x` to trace execution was the only way I found these.
*   **Broken Pipes and Stolen Input:** Chaining commands is powerful but fragile. At one point, my Python script was consuming the standard input meant for `yt-dlp`, leading to a cascade of "Broken pipe" errors. The solution was to pass data as arguments (`python -c '...' "$VAR"`) instead of relying on a pipe.
*   **Filtering with Unicode:** My searches for Hebrew kids' content were pulling in all sorts of irrelevant videos. The most effective fix was a simple Python function to check if the title or uploader name contained any characters in the Hebrew Unicode range (`\u0590`–`\u05FF`). It worked beautifully.

This was a classic case of a simple idea getting tangled in the weeds of execution. The whole process was a potent reminder that in shell scripting, you have to understand exactly how data is flowing between each command. Breaking the pipeline down and testing each piece interactively was the only way I made it through. But hey, now it works reliably.

**Next:** Now that the data extraction is solid, I might try using an LLM to review the video metadata for content suitability.

---
*Tags: bash, python, yt-dlp, data-engineering, cli, debugging*
