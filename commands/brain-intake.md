---
description: Convert a paper, report, idea, alpha expression, or BRAIN result into a research card
argument-hint: "<source_path_or_pasted_context>"
allowed-tools: Read, Write, Bash(cd:*), Bash(python:*), Bash(python3:*)
---

Use `brain-paper-to-alpha-plugin` to perform source intake.

Workflow:

1. Read `$ARGUMENTS` as the source path or pasted context.
2. Separate Fact, Assumption, Interpretation, and Recommendation.
3. Draft an Alpha Research Card with mechanism, expected sign, horizon, BRAIN
   field proxies, settings assumptions, leakage checks, risks, kill criteria,
   and next action.
4. If a run folder is provided, write or update `01_research_card.md`.
5. Do not generate BRAIN expressions yet unless the user asks for candidates.

Do not run live WorldQuant BRAIN simulations.
