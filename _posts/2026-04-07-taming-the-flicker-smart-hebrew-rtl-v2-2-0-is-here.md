---
layout: post
title: "Taming the Flicker: `smart-hebrew-rtl` v2.2.0 is Here!"
date: 2026-04-07
source_draft: "drafts/smart-hebrew-rtl"
tags: [browser extension, RTL, flicker-free, MutationObserver, web development, side project]
---

The past few months have been a wild ride getting `smart-hebrew-rtl` to a state I'm actually proud of, especially with the v2.2.0 release. This browser extension intelligently detects and reformats Hebrew text on web platforms, making it display correctly Right-to-Left (RTL) without breaking surrounding languages. The big push for v2.2.0 was all about achieving *instant* and *flicker-free* RTL rendering, especially for streaming content. It turned out to be a much bigger beast than I anticipated.

Getting v2.2.0 out the door involved wrestling with several challenges:

*   **The Flicker Nightmare:** Achieving truly *flicker-free* RTL for streaming content was a beast. I tried everything from "sticky CSS" to native `dir` attributes, eventually landing on a "two-phase streaming RTL" approach. Each fix felt like a whack-a-mole game, solving one problem only to reveal another.
*   A nasty bug caused input fields (like ChatGPT's) to freeze. Turns out, observing `characterData` mutations was too aggressive. The fix? Completely removing that observer and implementing smarter filtering to skip *all* mutations from editable areas. Less observation, more stability!
*   **Building My Own Tools:** To really debug streaming issues, I built a diagnostic tool using Chrome DevTools Protocol (CDP). This was invaluable for cross-platform testing, simulating rendering speeds, and inspecting DOM changes, especially for tricky platforms like Claude.ai.
*   I ran into classic Chrome manifest rejections (non-numeric suffixes, `_comment` key warnings). Small things, but they add up during release prep.
*   **The Polish Marathon:** Beyond the code, there was a lot of polish: refining the Chrome Web Store description, updating the popup with feedback links and post-update notifications, and reorganizing the project structure.

Honestly, this period felt like a marathon. There were moments of pure frustration, staring at a flickering screen, but also immense satisfaction in slowly chipping away at complex rendering problems. It reinforced that sometimes you need to build your own tools to understand and solve a problem, and that sticking with it, even when you feel like you're going in circles, is how you finally solve things. Shipping v2.2.0 feels like a huge weight off my shoulders.

Next: Monitor feedback and plan for minor bug fixes.
