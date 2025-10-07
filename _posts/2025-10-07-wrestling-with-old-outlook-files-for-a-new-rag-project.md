---
layout: post
title: "Wrestling with Old Outlook Files for a New RAG Project"
date: 2025-10-07
---

Today, I was excited to start a proof-of-concept for a RAG project using my own email archives. The goal is to query years of Outlook data to find achievements, tough questions, and key moments. I figured it would be a great way to test the power of RAG on a personal, messy dataset. Instead, I spent the entire day just trying to get the data out.

It turns out, preparing the data was a project in itself. The day was a classic deep-dive into unexpected technical hurdles.

Here’s a rundown of the struggles and what I learned:

*   **Parsing `.ost` and `.pst` files is a pain.** These files are large and not built for easy export. I found a Python library, `pypff`, but it required a Linux environment, which led to a whole new set of problems.
*   **WSL can be fickle.** For reasons I still don't understand, my WSL installation decided to stop working. After some troubleshooting with ChatGPT and Claude, the simplest solution was a full reinstall.
*   **Data corruption is real.** My main `.ost` file turned out to be corrupted. The extraction process even triggered a Blue Screen of Death at one point, likely due to corrupted attachments.
*   **Sometimes you have to fall back on old tools.** I pivoted to my smaller `.pst` archive file, which also seemed to have issues. I’m currently running the classic `scanpst.exe` utility on it, hoping to repair it enough to extract the contents.
*   **Small wins on the side project.** On a brighter note, I did some more testing on my RTL Chrome extension. It now correctly applies RTL styling in Claude's UI, which is great. I still need to fix some copy-paste edge cases, but it’s progress.

### Reflection

Today was a classic case of yak shaving. The "cool AI part" of the project had to wait while I got bogged down in the nitty-gritty of data extraction and environment setup. It’s a solid reminder that sometimes the most un-glamorous work is the most critical prerequisite for getting anything done.

**Next:** See if the `.pst` file repair worked and if I can finally extract my emails.

---
*Tags: RAG, Data Engineering, Python, Outlook, WSL, Learning Log*
