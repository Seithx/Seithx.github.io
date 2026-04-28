---
layout: post
title: "RAG's dirty secret: data prep is the real fight"
date: 2026-04-28
source_draft: "drafts/rag-document-cleanup"
tags: [RAG, LLM, data quality, data pipeline, Gemini, Python]
---

I've been knee-deep in RAG lately, building knowledge bases for a couple of projects. Everyone talks about retrieval and generation, but the real monster? Data preparation. Garbage in, garbage out, especially when your source documents are a mess. Scanned PDFs with OCR artifacts, inconsistent formatting, tables that broke, duplicate content, irrelevant boilerplate – if you feed that raw, the AI's answers are mediocre at best.

So I built an LLM-powered cleanup pipeline. The idea was to run every document through Gemini to fix OCR errors, standardize formatting, and remove noise, but with strict guardrails to stop the AI from changing meaning.

Here's what went into it:

*   **The pipeline steps:** Everything converts to clean Markdown first. Then we score each document for RAG-readiness, detect duplicate content, and run the LLM cleanup via Gemini. I used async concurrent chunk processing for speed.
*   **The 105% quality gate:** This was the most important decision. I rejected any chunk where the output exceeded 105% of the input length. Without it, the LLM would "helpfully" paraphrase and expand, which is exactly what you don't want for reference material. I also had to explicitly tell the model not to reconstruct mathematical formulas; it kept "fixing" correct notation.
*   **Hebrew language surprises:** I built a benchmark to compare different AI platforms on Hebrew questions. The differences in multilingual support were pretty stark. Some platforms clearly invested more there.
*   **Async gotcha:** When processing multiple files sequentially with async code, you *have* to reset the Google SDK client between event loop runs. Otherwise, you get obscure connection pool errors that look like network issues. That cost me hours.

At the end of this phase, I archived 75 one-off scripts. Cleaning up that messy root directory to just the pipeline scripts and docs felt amazing.

This whole thing hammered home that AI-assisted workflows aren't about a smart model. It's about building the right pipeline around it: validation, quality gates, fallbacks, monitoring. The AI is just one step.

Next: Integrating this cleanup pipeline into our main ingestion flow.
