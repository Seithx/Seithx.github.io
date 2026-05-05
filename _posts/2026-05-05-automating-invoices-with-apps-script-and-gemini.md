---
layout: post
title: "Automating invoices with Apps Script and Gemini"
date: 2026-05-05
source_draft: "drafts/invoice-processing"
tags: [google-apps-script, gemini-ai, automation, pdf-extraction, accounting, rtl-support]
---

Just shipped something I'm genuinely proud of. A client's accounting team was buried under manual data entry, opening dozens of supplier invoice PDFs each week, reading details, and typing everything into their ERP. It took 15-30 minutes per invoice, mind-numbingly tedious work.

I built a system to automate this with AI, running entirely on Google Apps Script. No servers, no deployment pipeline, no infrastructure to maintain. The team already lives in Google Sheets, so the whole thing sits right inside their existing workflow. A file watcher monitors their inbox, Gemini AI extracts structured data, and if the fast model isn't confident, it upgrades to a larger one. Results land in a spreadsheet, and the system generates ERP export files. I even built a Hebrew web dashboard for review.

The challenges were not what I expected:

*   **Multi-invoice PDFs:** Some suppliers bundle five or more invoices into one file. I had to detect these, split them, extract unique invoice numbers, and then merge rows for the same invoice if they spanned pages. That was a fun puzzle.
*   **AI hallucinated dates:** Gemini just made up dates sometimes. Completely fabricated. I had to add validation ranges and trigger re-extraction with the stronger model when dates looked suspicious. Trust, but verify, right?
*   **Hebrew RTL rendering:** The web dashboard, built for review, was a headache with right-to-left text layout. Mixing Hebrew with numbers and English text broke in surprising ways. Fighting the OS on that one.
*   **Apps Script 6-minute timeout:** Processing dozens of invoices meant hitting Apps Script's execution limit. I had to build a checkpoint and resume system so processing could continue across multiple runs.
*   **Strict ERP import format:** The client's ERP expected an extremely specific format: specific tab delimiters, DD/MM/YY dates, exact column positions. One wrong character and the import would fail silently. Debugging those was a joy.

I'm especially proud of the model fallback logic. Flash handles about 85% of invoices correctly. The ones it struggles with (bad handwriting, unusual layouts) automatically escalate. I save both model responses for comparison, which helps me improve prompts over time.

What started as "just parse some PDFs" turned into full accounts payable automation. The client went from 30 minutes per batch to a 5-minute review workflow. Classic scope creep, but the result genuinely saves them hours every week. It reminds me that AI doesn't need to be a fancy chatbot to be valuable. Sometimes the biggest impact is just removing tedious manual work from someone's day. The accounting team doesn't care about the AI, they care that they don't have to squint at PDFs anymore.

Next: Refine prompt engineering for edge cases.
