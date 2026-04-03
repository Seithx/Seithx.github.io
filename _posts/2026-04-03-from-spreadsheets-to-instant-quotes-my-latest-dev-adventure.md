---
layout: post
title: "From Spreadsheets to Instant Quotes: My Latest Dev Adventure"
date: 2026-04-03
source_draft: "drafts/shipping-calculator"
tags: [React, TypeScript, Desktop App, Vitest, Refactoring, Logistics]
---

Hey everyone! Just wrapped up a pretty satisfying project this month: a shipping cost calculator for a logistics company. Their sales team was seriously bogged down, spending way too much time cross-referencing endless Excel spreadsheets to figure out rates – especially with multi-item shipments and tricky dimensional weight rules. My mission? Build a React + TypeScript desktop app that makes that whole process instant, accurate, and way less painful, even offering smart tips like 'reduce one dimension by 3cm to avoid the oversized surcharge.'

This month was mostly about hardening the codebase and making sure it was rock solid:

*   **Componentizing the Monolith:** Broke down the huge `App.tsx` into 6 focused, manageable components. Much cleaner now!
*   **TypeScript Strictness:** Crushed all 52 TypeScript strict-mode errors. The codebase was a bit `any`-heavy before, so this was a big win for type safety.
*   **Testing the Beast:** Wrote a solid suite of 74 Vitest tests, covering all sorts of weight ranges, zones, and tricky edge cases in the pricing logic.
*   **State Persistence:** Added `localStorage` to keep the form state persistent, so the app remembers where you left off even after a restart.
*   **Custom Icon:** Built a custom app icon for the Windows EXE build, giving it a nice polished feel.
*   **ESLint v9 Headache:** Battled ESLint v9 dropping mid-refactor, which completely broke my existing config. That took way too long to sort out.
*   **Windows GitBash Woes:** Dealt with the usual Windows GitBash `npm` output weirdness, resorting to redirecting output to temp files. A recurring theme on my setup!

This wasn't the kind of project that gets flashy headlines, but honestly, there's a deep, quiet satisfaction in building a tool that completely transforms a slow, error-prone manual process into something instant and reliable. The pricing logic, with all its dimensional weight comparisons, pallet thresholds, and quarterly zone changes, was a beast to tame. Knowing that my 74-test suite is there, meticulously checking every calculation, gives me huge confidence that every quote going out is spot on. That's the real win here.

Next: Diving into some new backend tech for an upcoming project.
