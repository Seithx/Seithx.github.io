---
layout: post
title: "Wrestling with Old Outlook Files for a RAG POC"
date: 2025-10-10
---

I sat down today planning to make some real progress on my RAG project. The goal was to build a proof-of-concept on my own Outlook archives to show how I could query years-old emails for achievements and insights. Instead, I spent the entire day just trying to get the data out. A classic case of data prep reality hitting hard.

It was a journey through obscure libraries, environment issues, and corrupted files. Here’s a breakdown of the struggle:

*   **Parsing `.pst` and `.ost` is a pain.** These files are big and unwieldy. The libraries for parsing them, like `pypff`, aren't the most modern and often require a specific Linux environment to run properly. There just isn't a lot of variety in the tooling.

*   **Environment woes.** Speaking of which, my WSL decided to stop working out of the blue, forcing a full reinstall. It was just one of those random, time-sinking issues that pops up for no apparent reason.

*   **File corruption is real.** My main `.ost` file turned out to be corrupt, causing a Blue Screen of Death during one extraction attempt. I’m now running `scanpst.exe` on my smaller `.pst` archive file, hoping to salvage it. It contains some really important emails, so fingers crossed.

*   **AI to the rescue (sort of).** I did manage to find a working extraction script by bouncing ideas off ChatGPT and Claude. Even when the tools are old, modern assistants can help navigate the mess.

It was a frustrating day, to be honest. I wanted to be working on the cool AI part but got stuck in the mud of data extraction and environment configuration. It’s a good reminder that this is often where the real work lies. On a brighter note, I did some quick tests on my RTL Chrome extension, and it’s looking good on Claude, so at least there was a small win.

**Next:** See if the file repair worked so I can finally start the extraction.

Tags: RAG, Data Engineering, Python, Outlook, PST, WSL
