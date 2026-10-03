# C1-S25 — Pedestrian Model

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 1  
> Sprint: SPR-04 — SUMO Baseline & Experiment Plan  
> Slice: C1-S25

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Configure pedestrian movement in SUMO: crossing locations, pedestrian flow rates per scenario, and correct interaction with vehicle signal phases.

**Inputs**
- `sumo/network/arvexa-junction.net.xml` (C1-S22)
- Pedestrian requirements (C1-S11)

**Outputs**
- Updated network or additional file with pedestrian crossings and walkways
- `sumo/demand/pedestrian-demand.rou.xml`

**Acceptance Criteria**
- [ ] Pedestrian crossings exist at all relevant junction approaches
- [ ] Pedestrian flow rates are defined per demand scenario
- [ ] Pedestrians interact correctly with vehicle signal phases in SUMO
- [ ] Minimum crossing time from PR is enforceable by phase duration
- [ ] Simulation runs with pedestrians without errors

**Dependencies** — C1-S22, C1-S11

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
| Pedestrian crossings exist at all relevant junction approaches | `Pending` | — |
| Pedestrian flow rates are defined per demand scenario | `Pending` | — |
| Pedestrians interact correctly with vehicle signal phases in SUMO | `Pending` | — |
| Minimum crossing time from PR is enforceable by phase duration | `Pending` | — |
| Simulation runs with pedestrians without errors | `Pending` | — |

### Dependencies

C1-S22, C1-S11

### Notes / Decisions

Record implementation decisions, deviations, assumptions, and supervisor feedback here.

### Change Log

| Date | Change | Author |
|---|---|---|
| YYYY-MM-DD | Initial documentation entry | TBD |
