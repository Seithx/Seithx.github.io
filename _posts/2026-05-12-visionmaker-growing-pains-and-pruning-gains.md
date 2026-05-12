---
layout: post
title: "VisionMaker: Growing pains and pruning gains"
date: 2026-05-12
source_draft: "drafts/visionmaker"
tags: [computer vision, monorepo, YOLO, SSIM, refactoring, data annotation]
---

VisionMaker started as a focused pipeline for annotating visual data, specifically for material science involving silica. It's meant to be a smart assistant for our ARAD team, automating image and video frame labeling. This past week, things got wild.

*   **SSIM for data deduplication:** We got the initial ARAD silica pipeline running, but immediately hit a wall with data volume. Implementing SSIM (Structural Similarity Index Measure) for frame deduplication was a huge win. It verified a ~40% drop in frames at a 0.95 threshold, which felt amazing. That's a massive cut in processing time and storage.
*   **Monorepo architecture shift:** VisionMaker was outgrowing its initial structure. I bit the bullet and restructured everything into a monorepo with a proper per-project layout. This wasn't just moving files; it was rethinking how components interact and scale. The mental overhead of ensuring nothing broke was intense, like open-heart surgery on a running system.
*   **Massive cleanup and standardization:** Along with the monorepo, I dropped an old "junction" component that was more trouble than it was worth. Standardized all labeling naming conventions (finally!) and set up consistent subfolder reports. It's wild how much clearer things get when naming is consistent. I also pruned older `cluster` and `silica_filter` tools, plus some outdated `reports/` and `references/` directories. Clearing out that cruft felt good, even if some of those tools were "my babies" once.
*   **YOLO upgrade for object detection:** We retired OWLv2 and brought in YOLO. This meant setting up both training and prediction pipelines for YOLO, then restructuring the documentation to reflect all these changes. Switching core models is always a bit nerve-wracking, making sure the new one performs and integrates smoothly.

This week felt like a microcosm of software development. Start with a problem, build a solution, immediately hit a scaling issue, solve that, then realize the whole structure needs an overhaul because the project is growing. The satisfaction of seeing the SSIM dedupe work, and the clarity from the monorepo and cleanup, was immense. It's a constant reminder that code isn't just about new features; it's about tending the garden, pruning, reorganizing, and sometimes replanting entirely. I'm learning to embrace the messiness of growth and the discipline of cleanup.

Next: Integrating new data sources and refining the YOLO models further.
