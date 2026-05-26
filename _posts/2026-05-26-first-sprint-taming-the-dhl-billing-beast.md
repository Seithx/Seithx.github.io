---
layout: post
title: "First sprint: Taming the DHL billing beast"
date: 2026-05-26
source_draft: "drafts/dhl_mybill_dashboard"
tags: [billing, automation, python, web scraping, rdp, cookies, data sync]
---

This new project, the 'MyBill Dashboard,' is all about making sense of our shipping costs. Before this, reconciling invoices against our internal records was a manual slog, downloading PDFs and tearing our hair out. The goal is to automate that whole process, pull the data, and present it in a digestible dashboard.

This week was the initial sprint. Got the basic framework up and running, then immediately jumped into getting the data sync working. The core idea is to log into their portal, grab the latest billing info, and bring it into our system.

*   **Cookie refresh in RDP was a nightmare.** Their portal uses cookies, naturally. Keeping those fresh and valid, especially when running the sync process in a remote desktop environment (RDP), was a pain. I had to really dig into their auth flow to ensure cookies weren't expiring mid-sync or getting invalidated. That was the "Fix cookie refresh" commit.
*   The RDP environment itself was a real curveball. I've worked with remote servers before, but something about this specific setup, maybe network latency or session management, made the cookie refresh super finicky. It wasn't just a simple `requests.Session()` and forget it. I needed more aggressive retry logic and constant cookie lifecycle monitoring. Felt like chasing a ghost for a bit.
*   **Robustness from day one.** The need for a PID lockfile and crash guards came up quicker than I expected. I added a PID lockfile to prevent multiple instances of the sync script from running, because nothing's worse than two processes fighting over the same data. Also put in some crash guards to ensure if something *does* go wrong, it fails gracefully and doesn't leave things in a half-baked state. Clearer logging helps future me, too. It's easy to defer these "best practices," but with critical data sync, it became clear fast that robustness had to be baked in.

Honestly, it felt good to get this off the ground. There's a certain satisfaction in taking a completely manual, frustrating process and starting to automate it. The initial struggles with the RDP environment and the cookie refresh were frustrating, but also a good reminder that real-world systems are messy. It's never just a clean API call. You have to deal with the quirks, the legacy, the specific environment. It pushed me to think more defensively about the code and anticipate failure points, which is definitely a growth area for me.

Next: Getting the actual data parsing and storage implemented.
