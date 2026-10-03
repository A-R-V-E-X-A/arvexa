# C2-S14 — Action Validity Constraints

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 2  
> Sprint: SPR-06 — RL Controller  
> Slice: C2-S14

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Implement the constraint checker that intercepts RL policy outputs before they reach the SUMO actuator, masking or clipping any action that would violate a safety requirement.

**Inputs**
- `src/environment/arvexa_env.py` (C2-S10)
- Safety constraint layer spec (C1-S17), safety requirements (C1-S08)

**Outputs**
- `src/environment/action_validator.py`
- Modified `step()` in `arvexa_env.py` that calls the validator before execution

**Acceptance Criteria**
- [ ] Validator rejects (clips or masks) any phase duration below minimum green time
- [ ] Validator rejects any phase duration above maximum green time
- [ ] Validator prevents selection of a phase that is currently in intergreen
- [ ] All constraint violations are logged with a reason code
- [ ] Unit test demonstrates each constraint is enforced

**Dependencies** — C2-S10, C1-S17, C1-S08

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
| Validator rejects (clips or masks) any phase duration below minimum green time | `Pending` | — |
| Validator rejects any phase duration above maximum green time | `Pending` | — |
| Validator prevents selection of a phase that is currently in intergreen | `Pending` | — |
| All constraint violations are logged with a reason code | `Pending` | — |
| Unit test demonstrates each constraint is enforced | `Pending` | — |

### Dependencies

C2-S10, C1-S17, C1-S08

### Notes / Decisions

Record implementation decisions, deviations, assumptions, and supervisor feedback here.

### Change Log

| Date | Change | Author |
|---|---|---|
| YYYY-MM-DD | Initial documentation entry | TBD |
