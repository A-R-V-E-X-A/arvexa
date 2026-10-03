# C2-S27 — Pedestrian Conflict Handling

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 2  
> Sprint: SPR-07 — Multi-Objective & Safety  
> Slice: C2-S27

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Implement pedestrian phase protection in the constraint layer: guarantee minimum crossing time and prevent pedestrian phases from being interrupted by vehicle phase preemption (unless emergency vehicle).

**Inputs**
- `src/safety/constraint_layer.py` (C2-S25)
- Pedestrian state (C2-S06), pedestrian requirements (C1-S11)

**Outputs**
- Pedestrian protection logic embedded in `constraint_layer.py`

**Acceptance Criteria**
- [ ] Active pedestrian phase cannot be terminated before minimum crossing time elapses
- [ ] RL policy cannot skip a pedestrian phase that has been waiting beyond a configurable threshold
- [ ] Emergency vehicle preemption during pedestrian phase respects the EVR-PR conflict rule from C1-S10 and C1-S11
- [ ] All PRs from C1-S11 are satisfied and annotated

**Dependencies** — C2-S25, C2-S06, C1-S11, C1-S10

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
| Active pedestrian phase cannot be terminated before minimum crossing time elapses | `Pending` | — |
| RL policy cannot skip a pedestrian phase that has been waiting beyond a configurable threshold | `Pending` | — |
| Emergency vehicle preemption during pedestrian phase respects the EVR-PR conflict rule from C1-S10 and C1-S11 | `Pending` | — |
| All PRs from C1-S11 are satisfied and annotated | `Pending` | — |

### Dependencies

C2-S25, C2-S06, C1-S11, C1-S10

### Notes / Decisions

Record implementation decisions, deviations, assumptions, and supervisor feedback here.

### Change Log

| Date | Change | Author |
|---|---|---|
| YYYY-MM-DD | Initial documentation entry | TBD |
