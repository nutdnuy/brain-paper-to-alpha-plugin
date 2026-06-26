---
description: Create a local BRAIN paper-to-alpha research run folder
argument-hint: "--source-title TITLE [--source-path PATH_OR_URL] [--output-root DIR] [--run-id ID]"
allowed-tools: Bash(cd:*), Bash(python:*), Bash(python3:*)
---

Create a local research run folder for a paper, report, alpha idea, or failed
BRAIN result.

Use `$ARGUMENTS` as options for:

```bash
cd "${CLAUDE_PLUGIN_ROOT:-$PWD}" && python3 scripts/wq_brain_alpha.py init $ARGUMENTS
```

After creation, summarize the run path and expected next artifacts: research
card, candidate CSV, simulation queue, evaluation record, and memory update.
