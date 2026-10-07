# C2-S03 — Vehicle Classification / Type State

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 2  
> Sprint: SPR-05 — SUMO & Traffic-State Pipeline  
> Slice: C2-S03

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Extract the vehicle type category (car, truck, motorcycle, emergency) for each detected vehicle and include it as a state channel.

**Inputs**
- `src/environment/vehicle_detector.py` (C2-S02)
- `sumo/demand/vehicle-types.add.xml` (C1-S24)

**Outputs**
- Vehicle type field added to vehicle detector output
- Type-to-category mapping config

**Acceptance Criteria**
- [ ] Each detected vehicle carries a type category field
- [ ] Emergency vehicle type is reliably distinguishable from non-emergency types
- [ ] Mapping from SUMO vType to ARVEXA category is configurable (not hard-coded)
- [ ] Unit test covers each vehicle type category

**Dependencies** — C2-S02, C1-S24

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
| Each detected vehicle carries a type category field | `Pending` | — |
| Emergency vehicle type is reliably distinguishable from non-emergency types | `Pending` | — |
| Mapping from SUMO vType to ARVEXA category is configurable (not hard-coded) | `Pending` | — |
| Unit test covers each vehicle type category | `Pending` | — |

### Dependencies

C2-S02, C1-S24

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
