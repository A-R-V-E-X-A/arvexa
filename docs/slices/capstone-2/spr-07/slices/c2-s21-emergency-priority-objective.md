# C2-S21 — Emergency-Priority Objective

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 2  
> Sprint: SPR-07 — Multi-Objective & Safety  
> Slice: C2-S21

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Implement the emergency vehicle priority reward component: rewards rapid clearance of the emergency vehicle's approach and penalises delay.

**Inputs**
- `src/environment/reward.py` (C2-S15)
- Emergency vehicle state (C2-S07)

**Outputs**
- `emergency_priority` component in `src/environment/reward.py`

**Acceptance Criteria**
- [ ] Reward is triggered when an emergency vehicle is present in the state
- [ ] Reward is proportional to the speed of clearing the emergency vehicle's path
- [ ] Penalty applies per-step while an emergency vehicle is waiting
- [ ] Logged separately in `info` dict
- [ ] Unit test covers emergency vehicle present and absent scenarios

**Dependencies** — C2-S15, C2-S07

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
| Reward is triggered when an emergency vehicle is present in the state | `Pending` | — |
| Reward is proportional to the speed of clearing the emergency vehicle's path | `Pending` | — |
| Penalty applies per-step while an emergency vehicle is waiting | `Pending` | — |
| Logged separately in `info` dict | `Pending` | — |
| Unit test covers emergency vehicle present and absent scenarios | `Pending` | — |

### Dependencies

C2-S15, C2-S07

### Notes / Decisions

Record implementation decisions, deviations, assumptions, and supervisor feedback here.

### Change Log

| Date | Change | Author |
|---|---|---|
| YYYY-MM-DD | Initial documentation entry | TBD |
