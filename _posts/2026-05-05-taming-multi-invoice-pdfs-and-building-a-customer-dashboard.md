---
layout: post
title: "Taming multi-invoice PDFs and building a customer dashboard"
date: 2026-05-05
source_draft: "drafts/invoice-system"
tags: [AI, LLM, Google Apps Script, data extraction, invoice processing, automation, dashboard, debugging]
---

This sprint was a beast. We're automating invoice processing with AI, pulling critical data like supplier, amounts, and line items, then spitting out structured files for accounting systems. It's all about cutting manual data entry and human error. This time, I tackled multi-invoice PDFs and built a full customer dashboard.

*   **Smarter AI extraction:** I enabled LLM "thinking mode" for better accuracy, clarified date prompts, and added robust validations (like 9-digit supplier HP, total matching subtotal + VAT). If validation fails or key fields are missing, it now falls back to a more powerful AI or flags for review.
*   **File management and auditing:** Built an `auditInvoiceFiles()` function to scan folders, hash files, and detect duplicates. It resumes gracefully and has a timeout. Squashed a bug with empty audit arrays. Also added utilities to manage the inbox, moving unique files and trashing duplicates, all while tracking full file paths.
*   **Multi-invoice PDFs were a nightmare.** This meant a full data model overhaul, adding `parent_row_id` and ensuring child rows inherited sources. The re-processing logic was brutal, managing existing child rows, deleting old data, and merging. It now falls back to the Pro model for these and skips duplicates. After much pain, it's finally working, exporting tricky batches.
*   **TXT export format update:** Dates are now `DD/MM/YY` (required a one-time fix for existing files), and the whole export is tab-delimited. Allocation numbers and the Google Drive URL for the original invoice are now included.
*   **Customer web dashboard (GAS):** Built a customer web dashboard using Google Apps Script. This is a huge UX win, with a full Hebrew UI, translated messages, and direct data editing. I added fallback chains for expense accounts, split settings, and per-status guidance. Users can now edit line items, rename suppliers, and compare amounts. Squashed a few UI bugs along the way.

This sprint was intense, but deeply satisfying. I had moments of pure frustration, especially wrestling with multi-invoice logic or getting the GAS UI to behave. But seeing those multi-invoice PDFs finally export, or the dashboard come alive with a localized UI, felt amazing. It really hammered home the importance of breaking down complex problems. I learned a ton about robust error handling, data integrity, and building a decent UI on a restrictive platform.

Next: Address remaining TODOs and refine the dashboard's user experience.
