---
layout: post
title: "Agents, anonymization, and the DOCX deep dive"
date: 2026-04-21
source_draft: "drafts/weaverai_agents_mcp"
tags: [agents, AI, n8n, Flowise, DOCX, anonymization, vector database, debugging]
---

This week was all about pushing Weaverai_Agents_MCP, my AI agent system, further. The goal is to build agents that can handle complex, multi-step tasks by orchestrating Flowise with n8n for workflow automation. It's about making these agents smarter, capable of interacting with real-world data and processes.

Here's what went down:

*   **Building the n8n workflow skill library**
    I got the basic Flowise and n8n structure running, then focused on the n8n workflow vector database. Ingested 6902 workflows, which was a grind, but essential for the agent's "skill library." Had a minor Windows encoding hiccup early on, which is always fun. Integrated Voyage's rerank-2.5-lite, which really helped search relevance, and built out a "workflow build loop" for dynamic n8n workflow construction.

*   **The WAIP (Weaverai Anonymizer Pipeline) beast**
    This was a huge push, building a full anonymization service with n8n helpers and a LiteLLM skill. The big one was getting DOCX translation to work with the anonymizer.

*   **Fighting the DOCX structure**
    That DOCX translation was a rabbit hole. I had to dive deep into the document's XML to handle RTL/LTR bidirectional text, stripping it from styles, section properties, and even table visual properties. Debugging the AI prompts for `supergemma` and the `translate-docx` workflow was also tricky, getting the AI to "think" correctly without overthinking every request.

*   **Operational tweaks**
    Added a `/deploy` endpoint for remote updates, super handy for continuous integration. Also had to bump the Code node deadline to 290s to deal with task runner timeouts.

Honestly, this week felt like drinking from a firehose. The sheer volume of features and integrations was intense. The biggest struggle was definitely the DOCX manipulation and getting the anonymizer to be robust across different document structures and languages. The bidi text issue was a real head-scratcher, requiring a deep dive into XML and document standards I hadn't touched in ages. It felt like I was constantly context-switching between vector databases, AI prompts, n8n workflows, and low-level document parsing. But man, it's also incredibly satisfying to see it all come together. Building a system that can dynamically find, build, and execute complex workflows, and then handle something as complex as document anonymization and translation, feels like a huge leap. It shows what's possible when you just keep pushing through problems, one commit at a time.

Next: Refine the anonymizer's accuracy and expand its capabilities to more document types.
