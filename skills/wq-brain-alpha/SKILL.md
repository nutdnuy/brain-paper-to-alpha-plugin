---
name: wq-brain-alpha
description: Use for WorldQuant BRAIN alpha research, paper-to-alpha workflows, BrainAlpha M0-M5 candidate generation, BRAIN expression triage, failed-alpha repair, simulation handoff, low-correlation pool review, or when the user mentions Paper_to_code, WorldQuant BRAIN, Brain alpha mining, IQC, alpha examples, alpha mutation, alpha mixing, NoSID, self-correlation, sub-universe, Sharpe, Fitness, or BRAIN simulator results.
---

# WQ BRAIN Alpha

This skill converts papers, reports, raw ideas, alpha examples, and BRAIN
simulation feedback into reproducible WorldQuant BRAIN alpha research artifacts.
It adapts the source `Paper_to_code` pipeline into a BRAIN-specific
paper-to-alpha loop.

Default user-facing language is Thai. Write reusable artifacts, schemas,
formulas, prompts, and technical docs in English.

## Read First

Before producing candidates or making file changes, read the relevant local
reference files in this skill:

- `references/pipeline-map.md` for the Paper_to_code to BrainAlpha mapping.
- `references/artifact-schemas.md` for required outputs and columns.
- `references/brain-guardrails.md` for BRAIN validation and live-run safety.
- `references/prompt-templates.md` when drafting agent prompts.

## Core Workflow

Use this sequence unless the user asks for only one stage:

1. **Source intake:** identify whether the input is a paper, report, idea,
   existing alpha expression, or simulation result. Capture source path/URL,
   date, universe, data requirements, and unknowns.
2. **Evidence extraction:** separate Fact, Assumption, Interpretation, and
   Recommendation. Do not invent datasets, metrics, or BRAIN results.
3. **Research card:** write a falsifiable alpha thesis with economic mechanism,
   expected sign, horizon, required fields/proxies, and kill criteria.
4. **BRAIN primitive mapping:** map the thesis into available BRAIN-style
   fields, operators, neutralization choices, delay, decay, truncation, universe,
   and missing-data treatment.
5. **Candidate generation:** produce a small family of interpretable variants.
   Prefer 3-12 thesis-preserving expressions over random mutation.
6. **Static checks:** check syntax shape, balanced parentheses, missing fields,
   lookahead risk, sparse-field risk, turnover risk, concentration risk, and
   correlation risk before proposing a live run.
7. **Brain Oracle handoff:** prepare a simulation queue. Do not run live BRAIN
   simulations unless the user explicitly asks and the local workspace/auth
   runbook is already valid.
8. **Evaluation:** when results exist, diagnose Sharpe, Fitness, turnover,
   drawdown, margin, sub-universe, weight concentration, warnings, and
   self-correlation.
9. **Repair:** mutate from the observed failure mode: sign, horizon, smoothing,
   gating, neutralization, field proxy, universe, or correlation carrier.
10. **Memory:** record passes and failures with lineage, settings, metrics,
    decision, and next action.

## Artifact CLI

When filesystem access is available, prefer creating a run folder before
generating many artifacts:

```bash
python scripts/wq_brain_alpha.py init \
  --source-title "<paper or idea title>" \
  --source-path "<path-or-url>" \
  --output-root outputs
```

Append candidate rows:

```bash
python scripts/wq_brain_alpha.py append-candidate \
  --run-dir outputs/<run_id> \
  --candidate-id "<candidate-id>" \
  --hypothesis-id "H01" \
  --expression "<BRAIN expression>" \
  --settings-json '{"region":"USA","universe":"TOP3000","delay":1}'
```

Validate artifact shape:

```bash
python scripts/wq_brain_alpha.py validate --run-dir outputs/<run_id>
```

The CLI never stores credentials and never calls WorldQuant BRAIN.

## Safety Rules

- Never expose credentials, cookies, auth headers, or account secrets.
- Do not launch live BRAIN simulations unless the user explicitly asks.
- If live simulation is requested, default to one worker and a tiny run first.
- Treat all alpha outputs as research candidates requiring validation.
- Never imply certain future returns or guaranteed alpha.
- Preserve failed experiments; they are negative evidence for future search.

## Output Shape

For alpha research work, return:

- Research card path or markdown block.
- Candidate table or CSV path.
- Simulation queue or run instructions.
- Validation notes grouped as Fact, Assumption, Interpretation, Recommendation.
- Remaining risk/TODO, especially live BRAIN, field availability, self-corr,
  sub-universe, leakage, turnover, and overfit checks.
