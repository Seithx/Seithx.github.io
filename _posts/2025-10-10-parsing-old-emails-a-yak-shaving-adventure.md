---
layout: post
title: "Parsing Old Emails: A Yak Shaving Adventure"
date: 2025-10-10
---

My goal today was to get a RAG proof-of-concept running on my personal email archives. I wanted to see if I could query years of my own history to pull out achievements, motivations, and answer tough questions. But before I could do any of that, I had to actually *get* the data, and that turned into a whole thing.

The journey to extract raw text from my `.ost` and `.pst` files was a deep dive into unexpected problems. Here’s a quick rundown of the hurdles:

*   **Parsing is a pain.** The libraries for this, like `pypff`, aren't the most modern and require a specific Linux environment. This isn't something you do every day, and there aren't many options to choose from.
*   **WSL just quit.** My Windows Subsystem for Linux setup decided to stop working out of the blue, so I lost time reinstalling it just to get the parsing script to run. Classic dev stuff.
*   **Data corruption is real.** My main `.ost` file turned out to be broken. Trying to extract it caused a Blue Screen of Death, likely due to corrupt attachments. I’m now running a repair tool on my smaller `.pst` archive, which thankfully holds my most important emails.
*   **Side project progress.** On a brighter note, I tested my RTL Chrome extension again. The on-screen styling for right-to-left text is working great now. However, there are still some edge cases with copy-pasting that I need to iron out.

### Reflection

Today was a classic case of yak shaving. The main goal was completely sidelined by the prerequisite task of data extraction. It’s a good reminder that sometimes the messiest part of a project is just getting your hands on clean, usable data. It was frustrating, but a necessary battle to fight before the fun part can begin.

**Next:** Hopefully finish the PST file extraction so I can *finally* start on the RAG part.

Tags: RAG, Data Engineering, Python, WSL, PST Files, Side Projects
