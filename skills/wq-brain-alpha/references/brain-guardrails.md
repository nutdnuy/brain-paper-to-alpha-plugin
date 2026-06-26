# BRAIN Guardrails

## Live Simulation Boundary

Do not run live WorldQuant BRAIN simulation by default. Prepare artifacts and
handoffs unless the user explicitly requests live execution.

If live execution is requested:

- Use the user's active, trusted local BRAIN workspace.
- Do not print credentials, cookies, auth headers, or account data.
- Probe auth with a read-only endpoint or existing helper first.
- Start with one worker and a small candidate batch.
- Stop on `401`, `403`, `429`, repeated server errors, or Persona/auth issues.
- Preserve all run outputs; do not delete generated folders unless requested.

## Required Checks Before Promotion

- Hypothesis and expected sign are stated.
- Field availability and field cadence are plausible for the selected universe.
- No obvious lookahead/publication-timing leakage.
- Expression is syntactically balanced.
- Settings are explicit: region, universe, delay, neutralization, decay,
  truncation, pasteurization, NaN handling.
- Sparse-field, concentration, turnover, and sub-universe risks are noted.
- Existing alpha/family correlation risk is considered.

## WorldQuant BRAIN Gates

As of 2026-06-26 project memory, common BRAIN submission gates include:

- Delay 1 Sharpe greater than 1.25.
- Delay 1 Fitness greater than 1.0.
- Turnover between 1% and 70%.
- Max stock weight under 10%.
- Self-correlation below 0.7 unless the platform exception applies.
- Sub-universe Sharpe must clear the platform's scaled cutoff.

Treat these as project operating context, not as immutable platform law. Recheck
official documentation before relying on thresholds in a new competition cycle.

## Repair Diagnostics

| Failure | Repair direction |
|---|---|
| Low Sharpe | Check sign, horizon, field timing, neutralization, event window, and regime concentration. |
| Low Fitness | Improve return/turnover tradeoff through smoothing, gating, or broader breadth. |
| High Turnover | Use decay or slower windows only if they preserve the thesis horizon. |
| Low Turnover | Add dynamic component, change window, or avoid static level-only fields. |
| Concentrated Weight | Reduce sparse fields, extreme transforms, and narrow gates. |
| Low Sub-Universe | Remove illiquidity/small-cap dependence and avoid unbounded cap/liquidity multipliers. |
| High Self-Correlation | Change economic carrier, dataset, horizon, gate, or neutralization instead of only tuning windows. |
| Platform Warning | Preserve warning text and decide whether it blocks submission or only flags caution. |
