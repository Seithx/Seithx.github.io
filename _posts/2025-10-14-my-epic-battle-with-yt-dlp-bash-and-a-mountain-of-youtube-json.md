---
layout: post
title: "My Epic Battle with yt-dlp, Bash, and a Mountain of YouTube JSON"
date: 2025-10-14
---

I set out to build a "simple" script to pull metadata for Hebrew children's videos from YouTube. The plan was to use `yt-dlp`, pipe the JSON output to Python for filtering, and save it all as a clean TSV. Turns out, "simple" was optimistic. The whole thing turned into a multi-day debugging marathon, especially trying to get everything working smoothly inside Git Bash on Windows.

Here’s a rundown of the biggest hurdles and what I learned.

*   **Environment setup is half the battle.** My minimal MINGW64 environment was missing everything: `wget`, `sudo`, `jq`, and `stdbuf`. I spent hours finding workarounds, like using `curl` instead of `wget`, creating a Bash wrapper for the `jq.exe` binary, and using `PYTHONUNBUFFERED=1` to force real-time output when `stdbuf` wasn't available.

*   **`yt-dlp` can be a memory hog.** When pulling from a massive channel playlist, `yt-dlp` tried to load the entire list of videos into memory before outputting anything, causing it to hang. The magic flags were `--lazy-playlist` and `--flat-playlist`, which process the playlist item by item, turning a firehose into a manageable stream.

*   **Pipes are fragile.** My script kept dying with "Broken pipe" or "Invalid argument" errors. The culprit? My Python script was consuming `stdin` for itself, leaving the piped data from `yt-dlp` with nowhere to go. The fix was to pass file paths as arguments to the Python script (`python -c '...' "$OUT_FILE"`) instead of relying on the standard input stream.

*   **Unicode filtering is your friend.** My initial searches for Hebrew kids' content returned a lot of irrelevant videos. The most effective fix was a simple Python function to check if the video title or uploader name contained any characters within the Hebrew Unicode range (`\u0590`–`\u05FF`). It was a surprisingly precise way to filter out the noise.

This was one of those side projects that spiraled, but it was a fantastic learning experience. Untangling the mess of shell environments, process buffering, and API quirks was a powerful reminder that even with great tools, the real work is getting them to talk to each other without tripping over their own feet.

**Next:** Now that the data extraction is reliable, I might try converting the videos to audio and using an LLM to help me review the content.

---
*Tags: bash, python, yt-dlp, data-engineering, cli, debugging*
