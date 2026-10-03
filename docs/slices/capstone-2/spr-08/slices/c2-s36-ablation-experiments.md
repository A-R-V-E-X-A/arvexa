# C2-S36 — Ablation Experiments

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 2  
> Sprint: SPR-08 — Sensor Resilience & Simulation Evaluation  
> Slice: C2-S36

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Systematically disable each reward component in isolation and evaluate the resulting performance to quantify each component's contribution to ARVEXA's behaviour.

**Inputs**
- Trained ARVEXA controller variants (retrained with each component removed)
- Multi-objective reward (C2-S24), evaluation script (C2-S18)

**Outputs**
- Ablation results CSV: `results/c2/ablation/`
- Ablation summary table: removed component → metric change vs full model

**Acceptance Criteria**
- [ ] Each of the 5+ reward components from C2-S19 to C2-S23 is ablated in isolation
- [ ] Each ablation variant is trained and evaluated using the same protocol as the full model
- [ ] Ablation table clearly shows the delta (Δ) for each metric vs the full model
- [ ] At least one ablation produces a statistically significant degradation

**Dependencies** — C2-S24, C2-S18, C2-S34, C2-S35

---

## Implementation Record

### What was implemented
- [ ] Implementation completed
- [ ] Configuration added/updated
- [ ] Tests added/updated
- [ ] Documentation updated

### Files / Components

```text
# Replace these placeholders with actual repository paths.
src/...
tests/...
configs/...
docs/...
```

### Verification Evidence

- [ ] Unit-test evidence
- [ ] Integration-test evidence
- [ ] Runtime / simulation evidence
- [ ] Screenshot/log evidence where applicable
- [ ] Result artifact linked

**Evidence links:**
```text
# Add GitHub-relative links here.
```

### Acceptance Criteria Verification

| Criterion | Status | Evidence |
|---|---|---|
| Each of the 5+ reward components from C2-S19 to C2-S23 is ablated in isolation | `Pending` | — |
| Each ablation variant is trained and evaluated using the same protocol as the full model | `Pending` | — |
| Ablation table clearly shows the delta (Δ) for each metric vs the full model | `Pending` | — |
| At least one ablation produces a statistically significant degradation | `Pending` | — |

### Dependencies

C2-S24, C2-S18, C2-S34, C2-S35

### Notes / Decisions

Record implementation decisions, deviations, assumptions, and supervisor feedback here.

### Change Log

| Date | Change | Author |
|---|---|---|
| YYYY-MM-DD | Initial documentation entry | TBD |
