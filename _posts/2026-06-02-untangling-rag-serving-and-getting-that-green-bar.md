---
layout: post
title: "Untangling RAG serving and getting that green bar"
date: 2026-06-02
source_draft: "drafts/qms_rh_rag_project"
tags: [RAG, QMS, microservices, deployment, Claude, refactoring]
---

This past week was all about the QMS RAG Service. The goal: pull its core serving logic out of a bigger AI agent platform and give it a dedicated, robust home. Basically, letting people ask questions about our internal Quality Management System documents and get smart answers.

*   `feat(serving): consolidate QMS RAG serving tier` was the big architectural push. We extracted the RAG serving components from a monolithic AI agent system, giving them their own service. This means clearer ownership and easier scaling for QMS.
*   Getting it deployed and verified was the next hurdle. Pushing that `docs: mark QMS serving verify bar green (deploy + /search confirmed)` commit felt *amazing*. It meant the standalone service was up, and critically, the `/search` endpoint was working. That's the heart of the RAG system, so seeing green was a huge relief.
*   The "consolidation" itself was trickier than I thought. Untangling dependencies from the larger agent system felt like playing Jenga; I definitely worried I'd break something fundamental. Mostly, it was careful refactoring.
*   Deployment wasn't entirely smooth. A few hiccups with environment variables and network configs ate up some time debugging before `/search` finally responded. Always the little things.
*   I also added `CLAUDE.md` to detail the serving tier's integration, then cleaned it up to make sure the root `CLAUDE.md` was the canonical source. Plus, a quick `chore: update local Claude Code permission allowlist` to keep things secure.

This week felt like a real win. Taking a critical piece of functionality, extracting it, and making it a standalone, deployable service is incredibly satisfying. Seeing that green bar for deployment and `/search` working was a genuine moment of accomplishment. It really reinforces that breaking down complex systems into smaller, manageable services is the way to go, even if the initial untangling is a bit painful.

Next: Expand capabilities and integrate more deeply with user-facing applications.
