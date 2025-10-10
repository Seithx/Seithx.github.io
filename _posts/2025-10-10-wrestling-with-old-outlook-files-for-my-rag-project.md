---
layout: post
title: "Wrestling with Old Outlook Files for My RAG Project"
date: 2025-10-10
---

Today I wanted to make some real progress on a personal RAG project: building a proof-of-concept to query my own email archives. The idea is to use my `.pst` and `.ost` files—some stretching back years—to find old achievements, answer tough questions, and just see what's possible. But before I could get to the cool AI stuff, I had to actually get the data out. And that turned into a whole thing.

The day was mostly a battle with data extraction and environment setup. It’s a good reminder that sometimes the "boring" part is the hardest part.

*   **Parsing Outlook files is a niche problem.** The libraries for this, like `pypff`, aren't exactly modern, and there isn't a lot of variety. It required a specific Linux environment, which sent me down a rabbit hole.
*   **WSL decided to take the day off.** For reasons I still don't understand, my WSL installation just stopped working. I ended up having to reinstall it completely just to get the Python library to run. Classic dev-ops-for-one struggle.
*   **Data corruption is real.** After finally getting a script to run on my huge `.ost` file, my computer blue-screened. It seems the file has corrupted attachments. I’ve now switched to my smaller `.pst` archive file.
*   **Running repairs and hoping for the best.** I’m currently running `scanpst.exe` on the archive file to fix any potential issues. That file contains some really important emails, so fingers crossed it works without a hitch.
*   **A small win on another front.** I did some more testing on my RTL Chrome extension. It’s now applying right-to-left styling correctly in Claude, which is great! Still have some edge cases to fix with copy-pasting, but it’s progress.

Today was a classic case of yak shaving. I spent almost all my time just trying to get the data ready instead of working on the actual RAG logic. It’s frustrating, but also a necessary step. You can't build on a broken foundation.

**Next:** Hopefully, the `.pst` file repair works so I can finally start the extraction process again.

Tags: RAG, Data Wrangling, Python, Outlook, PST, WSL
