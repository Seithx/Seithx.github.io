---
layout: post
title: "An Unexpected Day of APIs and Data Scraping"
date: 2025-10-30
source_draft: "drafts/301025"
---

I wasn't planning on coding today, but a quick request turned my day off into a surprisingly productive session. It started with a simple problem—finding neighborhoods for thousands of addresses in Jerusalem—and ended with me diving deep into a web scraping challenge for a new RAG project. It was a perfect example of two very different kinds of development work.

Here’s a bit of what I ran into:

*   **APIs beat agents for bulk data.** The request was to get the neighborhood for ~4,000 addresses. My gut told me an AI agent would be incredibly slow and unreliable for that scale. A quick search with Claude confirmed my suspicion: the OpenStreetMap API was the right tool for the job.
*   **AI is a killer co-pilot.** I used Claude for the whole mini-project: finding the right API, parsing the ugly JSON response (it pointed out the `suburb` field was what I needed), and then writing the entire Python script in a Google Colab notebook. It ran with minimal debugging, which was a pleasant surprise.
*   **Data quality is always the catch.** The script worked great, but the output wasn't 100% perfect because the input address list wasn't clean. Still, for a quick-and-dirty solution, it was a solid win.
*   **Scraping is the real grind.** After that quick win, I started a new project: building a RAG system for a Rabbi's website, which is packed with text. Getting access was easy, but extracting the content is proving to be the real beast.
*   **Backend data structure can be a nightmare.** My current headache is that on the site, questions and their answers are stored as separate files. I need to figure out how to reliably merge them. It’s a messy, foundational step that will determine the success of the whole project.

Today was a tale of two tasks. The first was a clean, satisfying win that went from problem to solution in no time, thanks to a clear API. The second is a reminder that most of the work in data projects is just getting your hands on clean, structured data. It’s a messy process, but I'm excited to see where it goes.

**Next:** Keep wrestling with this web scraping and figure out how to properly link all the questions and answers for the RAG dataset.

---
*Tags: API, Python, Web Scraping, RAG, Claude, OpenStreetMap*
