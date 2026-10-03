# C2-S15 — Reward Implementation

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 2  
> Sprint: SPR-06 — RL Controller  
> Slice: C2-S15

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Implement the reward function skeleton, computing a scalar reward from the current environment state after each step. Individual objective components are placeholders here; full components are added in Sprint 7.

**Inputs**
- `src/environment/arvexa_env.py` (C2-S10)
- Reward architecture spec (C1-S16)

**Outputs**
- `src/environment/reward.py`
- Reward component registry (dict of component_name → compute_fn)

**Acceptance Criteria**
- [ ] `compute_reward(state, action, info)` returns a scalar float
- [ ] Reward components are individually togglable via config
- [ ] Each component's contribution is logged separately in the `info` dict
- [ ] Unit test confirms reward is a finite float for a valid state/action pair

**Dependencies** — C2-S10, C1-S16

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
| `compute_reward(state, action, info)` returns a scalar float | `Pending` | — |
| Reward components are individually togglable via config | `Pending` | — |
| Each component's contribution is logged separately in the `info` dict | `Pending` | — |
| Unit test confirms reward is a finite float for a valid state/action pair | `Pending` | — |

### Dependencies

C2-S10, C1-S16

### Notes / Decisions

Record implementation decisions, deviations, assumptions, and supervisor feedback here.

### Change Log

| Date | Change | Author |
|---|---|---|
| YYYY-MM-DD | Initial documentation entry | TBD |
