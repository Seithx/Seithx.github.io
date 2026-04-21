---
layout: post
title: "Shipping dashboard: Fighting the Angular ghost"
date: 2026-04-21
source_draft: "drafts/ups-tracking-dashboard"
tags: [Angular, reverse engineering, REST API, data pipeline, shipping, dashboard]
---

This past week on the shipping tracking dashboard project was a whirlwind. The goal is a real-time view of shipments, flagging issues before they blow up. Think mission control for packages, ensuring timely delivery and understanding delays.

Here's what went down:

*   Hooked up a direct REST API path. This pulls in much more reliable, up-to-the-minute data, which is essential.
*   Got the data-driven logic for "stuck" shipments and SLA detection working. It's not just a timer, it uses multiple data points to identify genuine delays. Seeing that light up when a shipment *is* stuck feels like a small victory.
*   Pushed out the new insights dashboard. This visualizes the raw data and detection logic, giving an overview.
*   Squeezed in a billing audit feature. It was a beast to get right, but super important for the business.
*   Codebase reorg and docs cleanup happened. Always good to tidy up.

The biggest headache, and most surprising, was the "Angular bundle reverse-engineering pipeline" chore. I had to dig into an existing Angular frontend, trying to understand its internals and data flows without source code or docs. Felt like a digital archaeologist, sifting minified JavaScript. I wanted to pull my hair out staring at obfuscated variable names, guessing their purpose. It was a rabbit hole, taking way more time than expected. It really showed the pain of legacy systems or integrating components without full control.

After that Angular deep dive, shipping the insights dashboard and billing audit felt incredibly satisfying. It's a good reminder that sometimes the grunt work, the detective work, enables the cool stuff. Connecting raw, messy data to actionable insights and a tangible feature felt good.

Next: Performance optimizations and more detailed reporting.
