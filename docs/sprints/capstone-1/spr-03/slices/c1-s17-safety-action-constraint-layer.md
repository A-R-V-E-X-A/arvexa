# C1-S17 — Safety & Action Constraint Layer

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 1  
> Sprint: SPR-03 — Architecture & Experimental Design  
> Slice: C1-S17

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Specify the constraint layer that sits between the RL policy output and the signal actuator, ensuring no unsafe action is ever executed regardless of policy recommendations.

**Inputs**
- `docs/architecture/action-space.md` (C1-S15)
- Safety requirements (C1-S08), emergency requirements (C1-S10), pedestrian requirements (C1-S11)

**Outputs**
- `docs/architecture/safety-constraint-layer.md`
- Constraint specification table: Trigger Condition | Enforced Action | Overrides | Parent SR/EVR/PR

**Acceptance Criteria**
- [ ] Every SR maps to at least one constraint in the layer
- [ ] Emergency priority preemption logic is specified in full
- [ ] Pedestrian minimum crossing protection is specified
- [ ] Constraint layer is described as logically separate from the RL policy
- [ ] No RL policy output may bypass the constraint layer under any condition

**Dependencies** — C1-S15, C1-S08, C1-S10, C1-S11

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
| Every SR maps to at least one constraint in the layer | `Pending` | — |
| Emergency priority preemption logic is specified in full | `Pending` | — |
| Pedestrian minimum crossing protection is specified | `Pending` | — |
| Constraint layer is described as logically separate from the RL policy | `Pending` | — |
| No RL policy output may bypass the constraint layer under any condition | `Pending` | — |

### Dependencies

C1-S15, C1-S08, C1-S10, C1-S11

### Notes / Decisions

Record implementation decisions, deviations, assumptions, and supervisor feedback here.

### Change Log

| Date | Change | Author |
|---|---|---|
| YYYY-MM-DD | Initial documentation entry | TBD |
