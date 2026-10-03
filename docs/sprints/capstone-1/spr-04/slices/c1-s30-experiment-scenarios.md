# C1-S30 — Experiment Scenarios

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 1  
> Sprint: SPR-04 — SUMO Baseline & Experiment Plan  
> Slice: C1-S30

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Define the complete set of simulation scenarios for ARVEXA evaluation. Each scenario specifies demand level, vehicle composition, pedestrian demand, sensor condition, and any special events.

**Inputs**
- `docs/experiments/traffic-demand-model.md` (C1-S23)
- Sensor-failure requirements (C1-S09), sensor degradation model (C1-S20)

**Outputs**
- `docs/experiments/experiment-scenarios.md`
- Scenario table: ID | Demand | Composition | Pedestrian Level | Sensor Condition | Special Events

**Acceptance Criteria**
- [ ] At least 6 distinct scenarios defined
- [ ] Scenarios cover: normal operation, high-demand, sensor-degraded, emergency vehicle, pedestrian-heavy
- [ ] Each scenario has a unique ID: SCN-01 … SCN-N
- [ ] Each scenario is linked to at least one RQ
- [ ] Scenario table is frozen before Capstone-2 begins

**Dependencies** — C1-S23, C1-S09, C1-S20

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
| At least 6 distinct scenarios defined | `Pending` | — |
| Scenarios cover: normal operation, high-demand, sensor-degraded, emergency vehicle, pedestrian-heavy | `Pending` | — |
| Each scenario has a unique ID: SCN-01 … SCN-N | `Pending` | — |
| Each scenario is linked to at least one RQ | `Pending` | — |
| Scenario table is frozen before Capstone-2 begins | `Pending` | — |

### Dependencies

C1-S23, C1-S09, C1-S20

### Notes / Decisions

Record implementation decisions, deviations, assumptions, and supervisor feedback here.

### Change Log

| Date | Change | Author |
|---|---|---|
| YYYY-MM-DD | Initial documentation entry | TBD |
