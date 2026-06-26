---
description: Generate a small, source-grounded BRAIN alpha candidate batch
argument-hint: "<research_card_path_or_context> [run_dir]"
allowed-tools: Read, Write, Bash(cd:*), Bash(python:*), Bash(python3:*)
---

Generate BRAIN alpha expression candidates from a research card or source
context using the active Claude Code / Codex agent.

Agent workflow:

1. Read the research card or context from `$ARGUMENTS`.
2. Preserve the thesis and generate 3-12 interpretable expression variants.
3. For each row include `candidate_id`, `hypothesis_id`, `family`,
   `expression`, `settings_json`, expected effect, static checks, status, and
   notes.
4. Flag leakage, sparse-field, turnover, concentration, self-correlation, and
   sub-universe risks before any live run.
5. If a run directory is supplied, append rows with:

```bash
cd "${CLAUDE_PLUGIN_ROOT:-$PWD}" && python3 scripts/wq_brain_alpha.py append-candidate ...
```

Do not run live WorldQuant BRAIN simulations.
