# C2-S01 — SUMO Environment Wrapper

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 2  
> Sprint: SPR-05 — SUMO & Traffic-State Pipeline  
> Slice: C2-S01

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Implement a Python class that manages the SUMO process lifecycle (start, step, reset, close) via TraCI, providing a clean interface to the rest of the ARVEXA system.

**Inputs**
- `sumo/network/arvexa-junction.net.xml` (C1-S22)
- `sumo/demand/` files (C1-S23 to C1-S26)
- SUMO architecture spec (C1-S18)

**Outputs**
- `src/environment/sumo_env.py`
- Unit tests: `tests/test_sumo_env.py`

**Acceptance Criteria**
- [ ] `start()` launches a SUMO process via TraCI without error
- [ ] `step(action)` advances the simulation by one decision step and returns raw TraCI data
- [ ] `reset()` terminates and restarts the simulation with the configured seed
- [ ] `close()` terminates SUMO cleanly
- [ ] All 4 methods are unit-tested with a mock or live SUMO call

**Dependencies** — C1-S22, C1-S23, C1-S18

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
| `start()` launches a SUMO process via TraCI without error | `Pending` | — |
| `step(action)` advances the simulation by one decision step and returns raw TraCI data | `Pending` | — |
| `reset()` terminates and restarts the simulation with the configured seed | `Pending` | — |
| `close()` terminates SUMO cleanly | `Pending` | — |
| All 4 methods are unit-tested with a mock or live SUMO call | `Pending` | — |

### Dependencies

C1-S22, C1-S23, C1-S18

### Notes / Decisions

Record implementation decisions, deviations, assumptions, and supervisor feedback here.

### Change Log

| Date | Change | Author |
|---|---|---|
| YYYY-MM-DD | Initial documentation entry | TBD |
