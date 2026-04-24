---
layout: post
title: "Fighting Google Recorder's export wall"
date: 2026-04-24
source_draft: "drafts/recorder-cli"
tags: [nodejs, cli, web scraping, accessibility, google recorder, devtools]
---

Google Recorder is awesome for transcribing meetings, but trying to get my recordings *out* of it? That's a whole different story. I had dozens of recordings stuck in there for a transcription project, and the web app only lets you download one at a time. Seriously? That's just not going to fly when you need to bulk export.

So, I spent a couple of days building a quick CLI tool in Node.js. It authenticates using saved browser credentials, lists all my recordings, and then batch-downloads the audio files along with their speaker diarization data.

Here's what I learned:

*   **Building the CLI:** I used `commander.js` for the command-line interface. It's pretty straightforward and got the job done quickly. The main challenge was figuring out the authentication flow without a public API.
*   **The accessibility tree breakthrough:** This was the real discovery. Instead of trying to parse the web app's HTML with fragile CSS selectors (which would break constantly as Google updates things), I queried the browser's accessibility tree. It gives you a clean, structured view of the page content that's way more stable than the underlying DOM. I've used a11y trees for testing before, but it never clicked that they're perfect for data extraction when there's no API.
*   **Chrome DevTools Protocol for the win:** Integrating the Chrome DevTools Protocol was a game-changer for development. Being able to inspect the live page state and interact with the browser while my script was running made debugging so much faster. It felt like I was inside the browser, poking around.

This was a short, two-day project, but it scratched a real itch and taught me a valuable new pattern. The accessibility tree approach is something I'll definitely be using again for interacting with web apps that lack proper APIs. It felt amazing to finally get my data out.

Next: Clean up the code and maybe open-source it.
