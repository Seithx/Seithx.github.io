---
layout: post
title: "Shipping calculator: Bulk, sessions, and AI brain-bending"
date: 2026-04-17
source_draft: "drafts/ups-shipping-calculator"
tags: [shipping, bulk upload, session management, AI integration, debugging, web development]
---

This past sprint on the shipping cost calculator was a whirlwind. The tool helps users get quick estimates for shipping, plugging in dimensions, weight, and destination to ballpark figures for logistics or product pricing. It's grown from a simple form, and this sprint pushed it further.

*   **Bulk calculation beast:** Adding bulk scenarios was the main event. Previously, it was one item at a time. Now, users can upload files or input multiple items, which is a huge usability leap. But getting data parsing right, handling individual item errors, and making the UI display everything without melting down was a proper head-scratcher. I lost too much time debugging an off-by-one error that only showed up with exactly 17 items. Seventeen! Why 17? It felt like wrestling an octopus in a phone booth.

*   **Session management curveballs:** Implementing session changes meant maintaining state for complex, multi-item calculations. Remembering user choices across steps or navigations makes the experience smoother. The challenge was balancing persistence with backend complexity and security. My heart skipped a beat when a misconfigured session store almost wiped my test data.

*   **AI groundwork (Claude):** I added Claude settings for AI integration. It's early days for leveraging it (packaging suggestions, route optimization?), but the groundwork is in. Initial setup was surprisingly easy. The real challenge will be using the API to get useful, consistent output. Hello, prompt engineering.

*   **Validation scripts:** With bulk uploads, bad data is a real threat. I started building validation scripts to catch issues early and keep the system stable. Also, still normalizing line endings in 2024. Some battles never end.

Tackling these architectural challenges felt good. Moving to bulk processing forced me to think about scalability and error handling differently. It was frustrating, but seeing those bulk calculations fly and results pop up was genuinely satisfying. I'm definitely growing in anticipating edge cases and designing for complex user flows.

Next: Diving deeper into AI integration with Claude.
