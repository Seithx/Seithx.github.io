---
layout: post
title: "Excel, my old foe: Planning agent progress & roadmaps"
date: 2026-06-02
source_draft: "drafts/rh-planner-agent"
tags: [agent, excel, planning, backtesting, ux, workflow]
---

The RH-Planner-Agent project aims to help our human planners make smarter, faster inventory decisions, optimizing their "Hold/Release" process. This past week was a whirlwind, pushing the project forward on several fronts.

*   Integrating with existing Excel workflows is always a beast. I tried appending agent columns directly to the planner's main sheet, thinking it would be seamless. Nope. It completely broke their existing filters, causing a major headache. Had to pivot quickly to putting the agent review on its *own* clean tab to preserve their workflow. It's a constant reminder: you can't just drop new tech on top of old processes without careful consideration of the human element and their tools.
*   Implementing the "buy-window" as a primary rule was a huge win. It wasn't just a minor tweak; it boosted our backtest accuracy from 66% to a much more respectable 90%. We also added NDO enrichment with ABC intervals and neutralizations, key metrics planners rely on.
*   The sheer depth of the planning domain, with terms like "NDO enrichment" and the nuances of "Hold/Release" decisions, was a lot to absorb. Transcribing those manual flowcharts and confirming baselines felt like detective work at times.
*   While roadmaps were crucial, iterating through so many variations (swimlane, sequential, Hebrew, English, with/without emojis) to get the messaging just right for various audiences was surprisingly time-consuming. It really highlights how much of "dev" work is actually communication and stakeholder management.

This sprint felt like a real growth period. I started feeling a bit overwhelmed by the sheer volume of domain knowledge and the complexity of existing manual processes. There were definitely moments of frustration, especially with those Excel filter issues. But pushing through, clarifying requirements with the planners (Sahar and Yulia were invaluable!), and seeing the backtest numbers jump was incredibly rewarding. It reinforced the importance of truly understanding the user's existing workflow, even if it means adapting your technical solution to fit their tools rather than forcing them to adapt to yours. It's not just about writing code; it's about making that code land effectively and be adopted.

Next: Time to start thinking about the next set of rules and expanding the agent's scope.
