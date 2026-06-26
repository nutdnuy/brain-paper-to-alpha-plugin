# Artifact Schemas

Use these shapes for run folders and handoffs.

## Research Card

```yaml
hypothesis_id:
source:
source_type: paper | report | idea | alpha_example | simulation_result
source_date:
mechanism:
expected_sign:
horizon:
universe:
required_fields:
candidate_proxies:
brain_settings:
  region:
  universe:
  delay:
  neutralization:
  decay:
  truncation:
  pasteurization:
  nan_handling:
leakage_checks:
kill_criteria:
next_action:
```

## Candidate CSV Columns

```text
candidate_id,hypothesis_id,source_id,family,expression,settings_json,
expected_effect,static_checks,status,notes
```

`status` should be one of:

```text
draft,static-pass,queued,simulated,hard-pass,near-pass,failed,archive
```

## Simulation Queue CSV Columns

```text
queue_id,candidate_id,expression,settings_json,priority,reason,run_policy,status
```

`run_policy` should say whether live simulation is allowed. Default:

```text
manual-only
```

## Evaluation Record

```yaml
candidate_id:
brain_alpha_id:
run_path:
settings:
  region:
  universe:
  delay:
  neutralization:
  decay:
  truncation:
metrics:
  sharpe:
  fitness:
  turnover:
  returns:
  drawdown:
  margin:
  subuniverse_sharpe:
checks:
  hard_checks:
  self_correlation:
  iqc_performance:
warnings:
diagnosis:
decision:
  status: pass | near-pass | fail | archive
  reason:
  next_repair:
```

## Memory Update

Every meaningful run should preserve:

- Source and hypothesis.
- Candidate lineage and expression.
- Settings.
- Metrics and failed checks.
- Repair lesson.
- Next action.
- Whether results were live BRAIN, offline proxy, or untested.
