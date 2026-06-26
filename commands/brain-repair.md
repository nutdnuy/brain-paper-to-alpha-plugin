---
description: Diagnose failed BRAIN alpha results and propose a repair batch
argument-hint: "<result_path_or_pasted_metrics>"
allowed-tools: Read, Write, Bash(cd:*), Bash(python:*), Bash(python3:*)
---

Use `brain-paper-to-alpha-plugin` to repair a failed or near-pass BRAIN alpha.

Workflow:

1. Read `$ARGUMENTS` as the result path or pasted metrics.
2. Preserve the original expression, settings, warnings, and lineage.
3. Diagnose the observed failure mode: low Sharpe, low Fitness, turnover,
   concentration, sub-universe, self-correlation, IQC, or platform warnings.
4. Propose 3-8 repair candidates that mutate from the observed failure mode,
   not random formula churn.
5. State what evidence would promote, archive, or branch the candidate family.

Do not run live WorldQuant BRAIN simulations unless the user explicitly asks.
