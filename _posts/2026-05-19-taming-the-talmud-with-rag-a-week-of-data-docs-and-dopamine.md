---
layout: post
title: "Taming the Talmud with RAG: A week of data, docs, and dopamine"
date: 2026-05-19
source_draft: "drafts/gemara-page-rag-experiment"
tags: [RAG, Talmud, Gemara, NLP, LLM, data engineering, evaluation]
---

This past week was a whirlwind on the `gemara-page-rag-experiment`. The goal: build a RAG system to make the Gemara (Talmud) accessible. Imagine asking complex questions about ancient texts and getting coherent, referenced answers. It's a huge challenge, the text is dense and multi-layered. My aim is to navigate that complexity.

*   First up, I dove deep into the "sugya" structure, a thematic unit in the Gemara. Understanding how these discussions are bounded, nested, and parallel is key for effective retrieval.
*   I spun up a RAG v0 proof-of-concept, pulling in lessons from past experiments (per-line tags, Sefaria topics). Expanded content to include Rashi and Tosafot, preserving text structure. Handling both English and Hebrew texts meant parallel file structures and language-split evaluations.
*   Data collection was a grind. I gathered hundreds of real Gemara questions, including Hebrew ones from otzar.org. The big win was building a gold standard dataset for Bava Batra (2a-25b). This meant downloading 87 Toshba PDFs and using a Gemini-Pro vision pipeline to extract 539 Bagrut questions and answers. Essential for evaluation, but man, that was a lot of PDF parsing.
*   Built a full evaluation framework: L2 Sefaria benchmarks, corpus ablation, L3 retrieval metrics, L4 end-to-end. Even played with L5 LLM-as-judge evaluations (pretty meta). Set up versioned experiments, locking baselines, and testing HyDE, RAPTOR, and a hybrid dense+BM25 RRF.
*   Struggles were real. Parsing Gemara references, especially multi-page or multi-cite prefixes, was a headache. Had to fix "drift cases" in gold data against live Sefaria. Dashboards needed constant tweaking to prevent text overlap. And yeah, some dead ends, like `v2_top_k_20 (LOST)`. Sometimes you just cut your losses.

Then, the breakthrough. After all that setup, implementing the v3 Voyage reranker was the first thing that *really* moved the needle, boosting L5 quality by almost 10 percentage points. That felt amazing, like finally seeing the light after slogging through dense text and data pipelines. It validated all the meticulous data and evaluation work.

Next: Integrate the Schottenstein edition and refine the LLM audit process.
