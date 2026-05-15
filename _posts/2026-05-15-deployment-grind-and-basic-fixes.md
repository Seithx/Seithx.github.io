---
layout: post
title: "Deployment grind and basic fixes"
date: 2026-05-15
source_draft: "drafts/floorsight"
tags: [deployment, coolify, docker, python, debugging, video-analysis]
---

This past week was a mixed bag for the FloorSight Video Analysis project. We're all about taking raw video and pulling out useful insights, like activity patterns or object tracking. The goal is to turn hours of unwatchable footage into actionable data. Most of my time went into deployment, but I squeezed in some bug fixes too.

*   **Upload crash fix:** I had a classic "duh" moment. Video uploads were crashing because I forgot to include `width` and `height` fields in the `VideoInfo` object. A simple data integrity check I completely missed, causing a real headache.
*   **Coolify deployment was a grind:** Getting Coolify to play nice took up most of my week. I spent ages documenting its API in `CLAUDE.md`, wrote a `coolify_manager.py` script for debugging, and dug into environment variables like `COOLIFY_API_TOKEN`.
*   **Real-time logs, finally:** The biggest win was adding `PYTHONUNBUFFERED=1` to the Dockerfile. This might sound small, but it was a game-changer for getting real-time logs. Before that, logs were delayed, making debugging a nightmare. Talk about fighting the OS for basic visibility.
*   **Schema validation and polite errors:** Tidied up some schema validation errors that kept popping up. Also, made sure our user-facing error messages were a bit more polite, hiding internal model names from users. Just good practice.

Honestly, it was frustrating at times. You fix one thing, and another deployment hurdle pops up. It felt like a constant battle against configuration and environment issues instead of building new features. But there's a certain satisfaction in wrestling with these infrastructure demons and coming out on top. It's a stark reminder that building software isn't just about writing features, it's about making sure it can actually live somewhere reliably. I learned a ton about deployment pipelines and the importance of good observability. Felt like a level-up in my devops understanding, even if it wasn't the 'fun' coding I usually prefer.

Next: Continue stabilizing deployment, and maybe, just maybe, some actual feature work.
