# C1-S31 — Evaluation Metrics

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 1  
> Sprint: SPR-04 — SUMO Baseline & Experiment Plan  
> Slice: C1-S31

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Define the exact metrics used to evaluate ARVEXA performance, including their formulae, collection methods, and the baselines against which they will be compared.

**Inputs**
- `docs/requirements/research-objectives.md` (C1-S03)
- Experiment scenarios (C1-S30)

**Outputs**
- `docs/experiments/evaluation-metrics.md`
- Metric table: ID | Name | Formula | Unit | Collection Method | Comparison Baseline

**Acceptance Criteria**
- [ ] At least 8 metrics defined
- [ ] Metrics cover: vehicle queue length, average waiting time, intersection throughput, pedestrian wait time, emergency vehicle clearance time, signal switching frequency
- [ ] Each metric maps to at least one RO
- [ ] Collection method is specified (TraCI subscription, log parsing, post-processing script)
- [ ] Metric list is frozen before Capstone-2 begins

**Dependencies** — C1-S03, C1-S30

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
| At least 8 metrics defined | `Pending` | — |
| Metrics cover: vehicle queue length, average waiting time, intersection throughput, pedestrian wait time, emergency vehicle clearance time, signal switching frequency | `Pending` | — |
| Each metric maps to at least one RO | `Pending` | — |
| Collection method is specified (TraCI subscription, log parsing, post-processing script) | `Pending` | — |
| Metric list is frozen before Capstone-2 begins | `Pending` | — |

### Dependencies

C1-S03, C1-S30

### Notes / Decisions

Record implementation decisions, deviations, assumptions, and supervisor feedback here.

### Change Log

| Date | Change | Author |
|---|---|---|
| YYYY-MM-DD | Initial documentation entry | TBD |
