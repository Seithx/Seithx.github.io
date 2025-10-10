---
layout: post
title: "From a Simple RTL Fix to Compressing Files in Termux"
date: 2025-10-10
---

I just wanted to use the Claude Android app with proper right-to-left (RTL) text for Hebrew, as I much prefer the native app over the browser. What started as a simple UI annoyance quickly spiraled into a classic case of yak shaving, leading me far, far away from my original goal.

This whole journey started when I remembered a workaround for my RTL problem. Here’s a quick rundown of the rabbit hole I fell into:

*   **The Blunt Instrument:** I recalled that Android’s Developer Options has a "Force RTL layout direction" setting. Flipping it on fixed the Hebrew text rendering in Claude, but it also flipped the *entire* app UI, which was just as unusable and annoying.
*   **A New Idea:** This got me thinking. My goal wasn't to flip the whole layout, just the text. I started brainstorming with Claude about building a simple accessibility overlay app that could target and fix only the text elements. It felt like a neat little side project that others might find useful too.
*   **The Inevitable Roadblock:** To build an Android app, I needed the Android IDE. I went to install it and immediately hit a wall: I didn't have the 5GB of free space required. Of course.
*   **The Side-Quest Solution:** So, now my project was "free up disk space." I remembered struggling with this before, trying to find good tools to compress files (especially APKs) on-device. This time, I asked Perplexity and discovered a great solution: using Termux to create a Linux environment on my phone and run compression scripts directly.

It's funny how a small problem can lead you on a totally unexpected journey. I set out to fix some text and ended up learning a new way to manage files on my device. While I haven't solved the original RTL issue yet, this detour taught me something valuable about using Termux for on-device system tasks. Sometimes the side quests are where the real learning happens.

**Next:** Finish compressing my files to free up 5-7GB and *finally* install the Android IDE.

---
*Tags: Android, RTL, yak shaving, Termux, accessibility, developer log*
