---
layout: post
title: "From Meeting Mayhem to Prompt Precision"
date: 2025-11-27
source_draft: "drafts/261125"
---

Today was one of those days—a firehose of information from back-to-back meetings that left my head spinning. I felt like the only one in the room struggling to connect the million theoretical ideas being thrown around to a practical reality. Honestly, if I hadn't recorded the calls, I'd have no idea how to even write a summary. It's a reminder that sometimes the most important tool is the one that helps you process the chaos.

After untangling the meeting notes (with a lot of help from AI), I dove back into my video analysis project. The goal is to process a full hour of video without the model hallucinating, and I’m getting close.

Here’s a bit of the journey today:

*   **Tackling Information Overload:** Long, rambling meetings are a huge challenge for me. Recording them and using an AI to distill key points has become a non-negotiable part of my workflow. It helps me cut through the noise and focus on actionable tasks.
*   **Slicing the Video Salami:** My main strategy for analyzing long videos is to break them into 10-minute chunks and process each one separately. The real trick is stitching the results back together into a coherent whole without introducing errors or weird artifacts.
*   **A Two-Prompt System:** I'm using a main prompt for the overall task and a secondary, dynamic prompt for each video segment. Code injects relevant context into the secondary prompt for each chunk, which helps keep the model on track.
*   **Prompt Structure is Everything:** I noticed some small hallucinations still creeping in. It hit me that the *structure* of the prompt might be as important as the instructions themselves. Just throwing more instructions into a single block isn't effective. I need to explore how different formats impact the output.

It’s a strange feeling to be building trust with a new manager while also feeling like you’re trying to build a plane in mid-air. But I love the process of taking a messy problem, breaking it down, and methodically testing solutions. The new era of development feels less about knowing how to write every line of code by heart and more about being a good architect and problem-solver. It’s a good fit for how my brain works.

**Next:** Systematically test different prompt structures on the same video to see what minimizes hallucinations the most.

Tags: AI, Prompt Engineering, Video Analysis, LLMs, Developer Life, Productivity
