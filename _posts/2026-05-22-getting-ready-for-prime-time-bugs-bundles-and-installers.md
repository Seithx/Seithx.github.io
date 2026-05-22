---
layout: post
title: "Getting ready for prime time: Bugs, bundles, and installers"
date: 2026-05-22
source_draft: "drafts/enhanchedsynagouge"
tags: [desktop app, installer, data persistence, debugging, date time, Inno Setup]
---

This past week was a whirlwind getting the Synagogue Display System ready for actual deployment. For anyone new here, it's a custom app for showing service times, announcements, and Yahrzeit info in lobbies, aiming for easy management without a browser. This period was all about squashing bugs and making it a proper, installable application.

*   That midnight UTC date bug was a real pain. Date/time math, especially UTC versus local, always gets me. I finally tracked it down, which was messing with Yahrzeit calculations. Also fixed some jankiness with image drag and scale, sorted memorial ordering, and made sure both the general and Yahrzeit slideshows played nice together.
*   The biggest scare was realizing updates would wipe out all user data. I had a moment of panic thinking about all their carefully entered memorial data disappearing. I spent time figuring out how to persist user data, specifically the memorial list, outside the application bundle in `%APPDATA%`. This means updates won't nuke their data, which is a huge relief and a big win for usability.
*   Documentation always takes longer than you think. I added some demo videos, which are essential for showing people how to use it, and updated the TODO list with backup links and the distribution roadmap.
*   Finally, I built an Inno Setup installer. Getting Task Scheduler autostart working was key; the app needs to launch automatically when the computer boots up without any manual clicks. This is essential for a display system that needs to be "always on."

It feels good to see this project mature from a collection of scripts into a deployable desktop application. Tackling the "boring but essential" infrastructure tasks like data persistence and installers makes the whole thing feel much more professional. That midnight UTC bug was a real head-scratcher, and figuring out user data persistence outside the app bundle was new territory for me. Getting the Inno Setup script, especially the Task Scheduler part, also took some trial and error.

Next: Final testing and initial pilot deployment.
