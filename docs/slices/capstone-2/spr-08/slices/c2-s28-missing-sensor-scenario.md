# C2-S28 — Missing Sensor Scenario

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 2  
> Sprint: SPR-08 — Sensor Resilience & Simulation Evaluation  
> Slice: C2-S28

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Run evaluation experiments where one or more entire state channels are dropped (simulating a failed sensor or camera that produces no output). Record ARVEXA performance vs baseline.

**Inputs**
- Sensor degradation model (C1-S20), mode: missing (dropout probability = 1.0 for affected channel)
- Trained ARVEXA controller (C2-S17), experiment scenarios (C1-S30)

**Outputs**
- Evaluation results CSV: `results/c2/missing-sensor/`
- Per-metric comparison: ARVEXA vs fixed-time baseline

**Acceptance Criteria**
- [ ] At least one complete sensor channel is dropped per run
- [ ] ARVEXA activates the missing-channel fallback (from SFR)
- [ ] Results include all metrics from C1-S31
- [ ] Experiments run across ≥ 3 scenarios from C1-S30

**Dependencies** — C1-S20, C2-S17, C2-S18, C1-S30, C1-S31

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
| At least one complete sensor channel is dropped per run | `Pending` | — |
| ARVEXA activates the missing-channel fallback (from SFR) | `Pending` | — |
| Results include all metrics from C1-S31 | `Pending` | — |
| Experiments run across ≥ 3 scenarios from C1-S30 | `Pending` | — |

### Dependencies

C1-S20, C2-S17, C2-S18, C1-S30, C1-S31

### Notes / Decisions

Record implementation decisions, deviations, assumptions, and supervisor feedback here.

### Change Log

| Date | Change | Author |
|---|---|---|
| YYYY-MM-DD | Initial documentation entry | TBD |
