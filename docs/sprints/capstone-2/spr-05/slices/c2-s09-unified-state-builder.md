# C2-S09 — Unified State Builder

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 2  
> Sprint: SPR-05 — SUMO & Traffic-State Pipeline  
> Slice: C2-S09

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Combine all state channels (vehicle queue, waiting time, pedestrian, emergency, sensor health) into a single normalised state vector ready for the RL controller.

**Inputs**
- C2-S04 (queue), C2-S05 (waiting time), C2-S06 (pedestrian), C2-S07 (emergency), C2-S08 (sensor health)
- State representation spec (C1-S14)

**Outputs**
- `src/environment/state_builder.py`
- Normalised numpy state vector matching the specification in C1-S14
- State schema validation test

**Acceptance Criteria**
- [ ] Output vector dimension matches the state spec in C1-S14 exactly
- [ ] All elements are normalised to a consistent range (e.g., [0, 1] or [-1, 1])
- [ ] Degradation mode injection is tested: degraded channel produces correct health indicator
- [ ] Schema validation raises an error if any element is out of range
- [ ] Integration test confirms end-to-end: SUMO step → state builder → vector

**Dependencies** — C2-S04, C2-S05, C2-S06, C2-S07, C2-S08, C1-S14

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
| Output vector dimension matches the state spec in C1-S14 exactly | `Pending` | — |
| All elements are normalised to a consistent range (e.g., [0, 1] or [-1, 1]) | `Pending` | — |
| Degradation mode injection is tested: degraded channel produces correct health indicator | `Pending` | — |
| Schema validation raises an error if any element is out of range | `Pending` | — |
| Integration test confirms end-to-end: SUMO step → state builder → vector | `Pending` | — |

### Dependencies

C2-S04, C2-S05, C2-S06, C2-S07, C2-S08, C1-S14

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
