---
layout: post
title: "A Day of Yak Shaving: Parsing Old Emails for a RAG Project"
date: 2025-10-05
---

I started today with a clear goal: build a proof-of-concept for a RAG project using my old email archives. The idea was to show how I could query years of messages to find achievements, key discussions, and answers to tough questions. Naturally, the universe had other plans, and I spent most of my day wrestling with the data itself instead of building the cool stuff.

It was a classic case of diving into a rabbit hole. Here’s what went down:

*   **The `.PST` & `.OST` Problem:** My email archives are in massive `.pst` and `.ost` files. To even begin, I had to figure out how to parse them. I moved them to a separate drive to avoid bogging down my main machine.
*   **Library & Environment Hell:** Extracting the data required a specific Python library, `pypff`, which in turn needed a Linux environment. Of course, my WSL installation decided to break right at that moment, forcing me to reinstall it completely. These libraries for parsing email files aren't exactly modern or well-documented, so it took a lot of back-and-forth with ChatGPT and Claude to find a working solution.
*   **File Corruption:** Just when I thought I was getting somewhere, I discovered my `.ost` file was corrupted. An attempt to process it even led to a Blue Screen of Death. I’ve now switched focus to the smaller `.pst` file and am running `scanpst.exe` on it, hoping to repair it. That file holds my most important archives, so fingers crossed.
*   **Quick RTL Extension Update:** On a different note, I did some more tests on my RTL Chrome extension. It’s successfully applying right-to-left styling in Claude, which is great. However, I still need to fix some copy-paste edge cases. I added more symbols for it to handle, but I haven't had a chance to fully test the changes yet.

This was one of those days where all the energy went into setup and debugging instead of the core logic. It’s frustrating, but a necessary part of the process. At least I have a repair process running on the archive file, so I’m ending the day with a glimmer of hope for usable data.

**Next:** Hopefully, finish the data extraction and actually start building the RAG POC.

---
*Tags: RAG, Data Processing, Python, WSL, PST Files, Chrome Extension*
