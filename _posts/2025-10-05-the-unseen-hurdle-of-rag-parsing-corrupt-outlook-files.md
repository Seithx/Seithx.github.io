---
layout: post
title: "The Unseen Hurdle of RAG: Parsing Corrupt Outlook Files"
date: 2025-10-05
---

My goal for the day was simple: get a proof-of-concept running for a RAG project on my own emails. I wanted to query years of my own history to find achievements and interesting threads. But instead of working with LLMs, I spent the entire day just trying to get the data out. It turns out, the first step is often the hardest.

I hit a wall trying to extract and parse my old Outlook `.ost` and `.pst` files. It was a journey through obscure libraries, environment issues, and corrupted data.

*   **The `.pst` and `.ost` nightmare:** These file formats are a real pain. The libraries for handling them, like `pypff`, feel a bit dated and require a specific setup. There aren't many modern alternatives, so you work with what you've got.
*   **Environment shenanigans:** The extraction process required a Linux environment. Of course, my WSL installation decided to stop working today, forcing me to go through a full reinstall just to get started.
*   **Corruption is everywhere:** My main `.ost` file turned out to be corrupt. The extraction script not only failed but triggered a blue screen of death. My smaller `.pst` archive also needed repairs with the classic `scanpst.exe` tool.
*   **Pivoting to the archive:** Because the live `.ost` file was so problematic (and larger), I shifted my focus to trying to repair and extract my archived `.pst` file. It contains incredibly important emails, so I’m hoping the repair process works.

Today was a classic reminder that in any data project, the "glamorous" AI part is tiny compared to the "boring" work of data extraction and cleaning. Before you can build a smart search, you have to wrestle your data out of its proprietary prison. On a small positive note, I did make some progress on my RTL Chrome extension, so the day wasn't a total loss.

**Next:** Hopefully, get a clean export from the repaired `.pst` file so I can finally start indexing.

Tags: RAG, Data Engineering, Python, Outlook, WSL, Learning in Public
