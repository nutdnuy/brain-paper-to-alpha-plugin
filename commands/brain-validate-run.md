---
description: Validate a local BRAIN alpha research run folder
argument-hint: "<run_dir>"
allowed-tools: Bash(cd:*), Bash(python:*), Bash(python3:*)
---

Validate the local artifact shape for a BRAIN alpha research run.

Run:

```bash
cd "${CLAUDE_PLUGIN_ROOT:-$PWD}" && python3 scripts/wq_brain_alpha.py validate --run-dir $ARGUMENTS
```

Report structural issues separately from research concerns. Call out remaining
checks that require the BRAIN platform: field availability, platform warnings,
Sharpe/Fitness gates, turnover, sub-universe, self-correlation, and IQC.
