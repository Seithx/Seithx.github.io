---
layout: post
title: "Refactoring, Rabbit Holes, and a Reverse-Engineering Breakthrough"
date: 2025-10-30
source_draft: "drafts/271025"
---

Today was one of those days that went in three directions at once. The main plan was to continue a major refactoring of our video routing project, but a couple of interesting side quests popped up and demanded attention. It was a classic juggling act between disciplined engineering, a tempting distraction, and a personal project that finally clicked.

I spent a good chunk of the day making sure our refactoring was solid. After migrating most of the code with AI assistance, I found it had missed a few old functions for exporting to Excel. Getting those back in was easy, but it tanked our `radon` code quality score. It took some focused work with `black` and `mypy` to clean things up and get back to an 'A' rating. If you're going to refactor, you have to do it right.

Here’s a snapshot of the day’s ups and downs:

*   **The Automation Rabbit Hole:** An interesting request came in for an automation involving `xlswings` and Outlook. While it was a fun chance to play with a new library, I sank too much time into it before realizing Google Sheets was probably a better tool for the job. I pushed the code to Git and decided to move on—a good lesson in choosing the right tool before diving in.
*   **A Surprise API Win:** I got an early start and decided to tackle a personal project I’ve picked up and dropped several times: reverse-engineering a notebook service's private API. The goal is to build a chat interface that uses it as a backend.
*   **It Actually Worked!** After a lot of trial and error, I finally got a coherent, Hebrew response from the service through my custom interface. Seeing it work was an incredible feeling.
*   **The Next Hurdle:** The connection isn't persistent and relies on manually refreshing cookies. The next step is figuring out how to maintain a stable session, which will probably mean setting up a VPS.

It’s easy to feel like I was all over the place, but the thrill of the API project breakthrough made the whole day feel like a win. Moving between grinding on code quality, exploring a new idea, and achieving a personal goal is what makes this work so engaging.

**Next:** Finish the simple 5S automation I’ve been putting off—it’s quick, valuable, and needs to get done.

---
*Tags: Python, Refactoring, API, Code Quality, Automation, Side Projects*
