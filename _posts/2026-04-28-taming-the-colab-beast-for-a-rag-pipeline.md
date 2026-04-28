---
layout: post
title: "Taming the Colab beast for a RAG pipeline"
date: 2026-04-28
source_draft: "drafts/rabbai_oury_cherki_rag"
tags: [rag, colab, environment, python, debugging, data pipeline]
---

My "Rav Oury Cherki RAG pipeline" project is all about making his teachings accessible. This past week, I spent most of my time wrestling with environments and getting the data ingestion solid. The initial RAG idea was easy, but then the real work began: making it runnable in Google Colab.

*   **Colab environment was a nightmare.** I had to pin `lightning-fabric` to a specific version, deal with some weird `partial-numpy` swaps after an install cascade, and switch to `%pip` magic because regular `pip` was causing issues. Then came the "runtime shims" for things like `torchaudio.info` and `numpy.NAN`. It felt like I was constantly patching holes in a leaky boat.
*   **Dependency hell and `pyannote`:** The `numpy` issues were particularly frustrating. Getting `pyannote` (for diarization) to work consistently across different Colab runtimes and local `venv` setups was a nightmare. I spent a lot of time exploring `venv` theory just to understand why things were breaking.
*   **Data ingestion wins:** Despite the environment fight, I built `playlist recovery` to grab content, a `WhatsApp chat parser` (which was surprisingly tricky), and `name-variation search`. A `batch diarize notebook` is now working, and getting a `GDrive downloader` working was a big win for source material. I also added `candidate review tools` and fixed `needs_transcription` regeneration.
*   **Hacky solutions:** I even had to bypass SSL certificate verification for some URL shorteners just to follow redirects. Not ideal, but necessary to get the data.

When I finally got a "successful E2E run," it was a huge relief. All those little fixes, the constant debugging, the moments of wanting to throw my laptop across the room... it paid off. It really hammered home how much time environment setup can suck up, even on seemingly simple projects. The "glamorous" AI stuff often sits on a foundation of gritty, low-level engineering. I learned a ton about dependency management and the quirks of cloud notebooks.

Next: Focus on improving RAG retrieval quality and expanding data sources.
