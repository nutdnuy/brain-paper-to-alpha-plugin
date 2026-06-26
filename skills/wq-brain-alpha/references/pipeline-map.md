# Pipeline Map

This plugin adapts the original `Paper_to_code` sequence into a WorldQuant
BRAIN alpha workflow.

## Source Pipeline

| Paper_to_code stage | Original role | BRAIN adaptation |
|---|---|---|
| `0_pdf_process.py` | Clean parsed paper JSON by removing spans and metadata noise. | Source intake: normalize local PDF/text/notes into a concise evidence packet. |
| `1_planning.py` / `1_planning_llm.py` | Ask an LLM for reproduction plan, architecture, task list, and config. | M0-M1: extract mechanism, create research card, map variables to BRAIN fields/operators/settings. |
| `1.1_extract_config.py` | Extract `config.yaml` and planning artifacts. | Emit alpha run artifacts: research card, candidate table, simulation queue, evaluation schema. |
| `2_analyzing.py` / `2_analyzing_llm.py` | Produce per-file logic analysis before code generation. | M2 static analysis: explain each expression family, expected behavior, risk, and failure mode. |
| `3_coding.py` / `3_coding_llm.py` | Generate repository files one at a time from plan and analysis. | M2-M3 handoff: generate BRAIN expressions, submit CSV rows, or local helper scripts without live execution. |
| `eval.py` | LLM judge evaluates paper-code fidelity. | M4-M5 evaluator: diagnose metrics, self-correlation, sub-universe, overfit risk, and portfolio fit. |

## BrainAlpha M0-M5 Mapping

```text
M0 Idea Generation
  Input: paper/report/idea/alpha example/result
  Output: source-backed mechanism and hypothesis list

M1 Seed Factory
  Input: hypotheses
  Output: BRAIN field/operator/settings map and seed templates

M2 Generator Agent
  Input: seed templates
  Output: controlled candidate family with static checks

M3 Brain Oracle
  Input: simulation queue
  Output: BRAIN metrics and platform warnings

M4 Evolution Engine
  Input: failures and near-passes
  Output: repair candidates driven by observed failure mode

M5 Portfolio Manager
  Input: passing candidates and correlations
  Output: low-correlation, submission-ready working set
```

## Default Run Folder

```text
<run_id>/
  00_source/
  01_research_card.md
  02_candidates.csv
  03_simulation_queue.csv
  04_results/
  05_evaluation_record.yaml
  06_memory_update.md
```

## Operating Principle

Preserve the thesis. Generate variants from the economic mechanism and observed
failure mode, not from random formula churn.
