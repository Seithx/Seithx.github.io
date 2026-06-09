---
layout: post
title: "RAG pipeline: Fighting segfaults and finding structure"
date: 2026-06-09
source_draft: "drafts/bidi-doc-rag-pipeline"
tags: [RAG, pipeline, debugging, segfaults, document processing, data quality]
---

This week, I dove into building my "bidi-doc-rag-pipeline" (yeah, a mouthful). It's all about making sense of complex, cross-referenced documentation, like manuals or technical specs, where context isn't linear. The goal is accurate answers from dense, messy documents.

*   **Core architecture and ingestion:** I set up the initial repo and started on the "corpus expansion pipeline." This finds and incorporates more related content, growing our knowledge base. Crucially, I also began implementing the "cross-reference graph." This maps how sections and documents link, vital for the "bidirectional" aspect. Without it, RAG just pulls isolated chunks.
*   **Hardening extraction (and segfaults):** Oh boy. My initial methods fell apart with gnarlier inputs. The biggest headache was "segfault protection." I was getting hard crashes, probably from underlying C/C++ libraries hitting bad memory or malformed data. Debugging segfaults is never fun, like finding a needle in a burning haystack. It took a lot of defensive programming, trying different parsing strategies, and adding robust error handling. Felt like I was constantly patching holes in a leaky boat.
*   **Auto quality check:** I realized I couldn't just trust the output. So, I added an auto quality check. This uses heuristics and checks to ensure extracted text isn't garbled, missing huge chunks, or just plain nonsense. It's a sanity check to avoid feeding garbage to the RAG system.
*   **Smarter heading detection:** For structured documents, knowing what's a main heading, a subheading, or just body text is vital for providing good context. The extractor was a bit dumb about this initially, but now it's much smarter, which should significantly improve retrieval quality.

This week was a rollercoaster. Pure frustration with those segfaults, I felt like I was banging my head against the wall trying to figure out why things were crashing. But then, tracking a tricky bug or seeing the auto quality check correctly flag a bad extraction felt great. It's a good reminder that robust systems need safeguards for when things go wrong. Defensive programming and understanding external library limits are key. Data quality is paramount, too: garbage in, garbage out.

Next: Integrating refined extraction with the cross-reference graph for initial RAG queries.
