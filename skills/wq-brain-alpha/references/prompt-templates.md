# Prompt Templates

## Source Intake

```text
Use wq-brain-alpha.

Input source:
<path, URL, pasted text, alpha expression, or simulation result>

Task:
Extract source-grounded facts, assumptions, interpretations, and BRAIN alpha
research implications. Do not generate expressions yet.
```

## Research Card

```text
Use wq-brain-alpha.

Create an Alpha Research Card with:
- source
- economic mechanism
- expected sign
- universe
- required fields and BRAIN proxies
- horizon/delay
- neutralization/settings assumptions
- leakage checks
- kill criteria
```

## Candidate Batch

```text
Use wq-brain-alpha.

Generate 6 BRAIN expression candidates from this research card.
Constraints:
- preserve the same hypothesis
- include settings_json for each row
- prefer simple interpretable variants
- flag static risks before simulation
- do not run live BRAIN simulation
```

## Repair Loop

```text
Use wq-brain-alpha.

Diagnose this BRAIN result and propose the next repair batch:
<metrics, failed checks, warnings, expression, settings>

Rules:
- mutate from the observed failure mode
- keep lineage to the original hypothesis
- produce 3-8 repair candidates
- explain why each repair should address the failure
```

## Memory Update

```text
Use wq-brain-alpha.

Create a memory update for this run:
<research card, candidates, metrics, decisions>

Include passes, failures, repair lessons, and next action.
```
