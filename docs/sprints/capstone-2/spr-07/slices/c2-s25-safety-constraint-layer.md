# C2-S25 — Safety Constraint Layer

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 2  
> Sprint: SPR-07 — Multi-Objective & Safety  
> Slice: C2-S25

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Implement the constraint enforcement layer: the module that intercepts policy actions and enforces all safety requirements (minimum green, maximum green, all-red intergreen) unconditionally.

**Inputs**
- `src/environment/action_validator.py` (C2-S14)
- Safety constraint layer spec (C1-S17)

**Outputs**
- `src/safety/constraint_layer.py`
- Updated `arvexa_env.py` `step()` to route through constraint layer before SUMO command

**Acceptance Criteria**
- [ ] Every SR from C1-S08 is enforced and has a corresponding constraint
- [ ] Constraint layer is logically separate from the reward function and policy
- [ ] Constraint violations are logged with constraint ID and action modification
- [ ] No combination of RL policy output can produce a signal state that violates an SR
- [ ] Integration test confirms constraint fires on a policy that would otherwise violate an SR

**Dependencies** — C2-S14, C1-S17

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
| Every SR from C1-S08 is enforced and has a corresponding constraint | `Pending` | — |
| Constraint layer is logically separate from the reward function and policy | `Pending` | — |
| Constraint violations are logged with constraint ID and action modification | `Pending` | — |
| No combination of RL policy output can produce a signal state that violates an SR | `Pending` | — |
| Integration test confirms constraint fires on a policy that would otherwise violate an SR | `Pending` | — |

### Dependencies

C2-S14, C1-S17

### Notes / Decisions

Record implementation decisions, deviations, assumptions, and supervisor feedback here.

### Change Log

| Date | Change | Author |
|---|---|---|
| YYYY-MM-DD | Initial documentation entry | TBD |

## Research Direction Alignment — Reliability-Aware Study

These sprint/slice activities must remain aligned with the current ARVEXA research anchor:

> Does more traffic information always improve adaptive traffic-signal control when the reliability of that information varies?

The research should treat state richness and observation reliability as explicit experimental variables. R1–R4 representations, controlled degradation modes, matched comparisons, safety/priority constraints, and reproducible evaluation should follow the authoritative documents:

- `docs/research/research-direction.md`
- `docs/architecture/rl-state-representation.md`
- `docs/experiments/research-evaluation-protocol.md`

Do not present pedestrian handling, emergency priority, sensor failure, computer vision, heterogeneous traffic, or RL individually as the novelty. Their role is to create and evaluate the information–reliability decision-making problem.
