# C1-S26 — Emergency-Vehicle Model

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 1  
> Sprint: SPR-04 — SUMO Baseline & Experiment Plan  
> Slice: C1-S26

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Configure how emergency vehicles are represented and triggered in SUMO simulations, including their insertion logic and the observable state that ARVEXA will receive.

**Inputs**
- `sumo/demand/vehicle-types.add.xml` (C1-S24)
- Emergency-vehicle requirements (C1-S10)

**Outputs**
- Emergency vehicle route/trigger configuration file
- `docs/sumo/emergency-vehicle-simulation-notes.md`

**Acceptance Criteria**
- [ ] Emergency vehicles can be inserted on demand (scripted or on-schedule)
- [ ] Emergency vehicle route traverses the study junction
- [ ] TraCI can detect emergency vehicle presence and distance from junction
- [ ] A test run demonstrates detection and logging without errors

**Dependencies** — C1-S24, C1-S10

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
| Emergency vehicles can be inserted on demand (scripted or on-schedule) | `Pending` | — |
| Emergency vehicle route traverses the study junction | `Pending` | — |
| TraCI can detect emergency vehicle presence and distance from junction | `Pending` | — |
| A test run demonstrates detection and logging without errors | `Pending` | — |

### Dependencies

C1-S24, C1-S10

### Notes / Decisions

Record implementation decisions, deviations, assumptions, and supervisor feedback here.

### Change Log

| Date | Change | Author |
|---|---|---|
| YYYY-MM-DD | Initial documentation entry | TBD |
