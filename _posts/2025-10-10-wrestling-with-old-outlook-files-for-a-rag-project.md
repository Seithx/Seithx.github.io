---
layout: post
title: "Wrestling with Old Outlook Files for a RAG Project"
date: 2025-10-10
---

I was excited to start a proof-of-concept for a RAG project on my own email archives. The goal is to build a smart search over years of my own data to find achievements, answer tough questions, and rediscover old conversations. But before I could get to the fun AI part, I hit the first major hurdle: actually getting the data out of my massive `.pst` and `.ost` files. It turned out to be a much bigger headache than I expected.

This was a day of deep-diving into the unglamorous but necessary work of data extraction. Here’s what I ran into:

*   **Parsing old formats is tricky.** The go-to library for this, `pypff`, feels a bit dated and required a whole Linux environment to run. There aren't many modern, plug-and-play alternatives, so I had to roll with what was available.
*   **Environment setup will get you.** Of course, my WSL installation decided today was the day to stop working. I ended up having to reinstall it completely just to get the extraction tools running. A classic case of yak shaving.
*   **File corruption is real.** My main `.ost` file turned out to be broken, and my smaller `.pst` archive needed a repair run with `scanpst.exe`. I even hit a Blue Screen of Death during one extraction attempt, which I think was caused by corrupt attachments.
*   **Small wins on other fronts.** I did manage to do some more testing on my RTL Chrome extension. It’s applying styles correctly, but I’ve found some new edge cases around copy-pasting that I need to iron out.

Today was a reminder that most data projects are 80% data preparation. It was frustrating to spend hours just trying to get clean text from a file instead of building the cool stuff. Still, it’s a necessary step, and I’m slowly clearing the path to get this project moving.

**Next:** Hopefully, the file repair works so I can finally start extracting some clean text data.

Tags: RAG, Data Engineering, Python, Outlook, PST, WSL
