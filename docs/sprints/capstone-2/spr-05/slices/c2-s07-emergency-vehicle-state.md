# C2-S07 — Emergency-Vehicle State

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 2  
> Sprint: SPR-05 — SUMO & Traffic-State Pipeline  
> Slice: C2-S07

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Detect and represent emergency vehicle presence, approach direction, and estimated time to junction in the state vector.

**Inputs**
- `src/environment/vehicle_detector.py` (C2-S02) with type classification (C2-S03)
- Emergency-vehicle model (C1-S26), state representation spec (C1-S14)

**Outputs**
- Emergency vehicle state channel: presence flag, approach lane, estimated time to junction

**Acceptance Criteria**
- [ ] Emergency vehicle is detected by type category (from C2-S03)
- [ ] Presence flag, approach lane ID, and distance/time to junction are populated
- [ ] Output matches emergency vehicle state element specification in C1-S14
- [ ] Unit test uses a scenario with an approaching emergency vehicle

**Dependencies** — C2-S02, C2-S03, C1-S26, C1-S14

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
| Emergency vehicle is detected by type category (from C2-S03) | `Pending` | — |
| Presence flag, approach lane ID, and distance/time to junction are populated | `Pending` | — |
| Output matches emergency vehicle state element specification in C1-S14 | `Pending` | — |
| Unit test uses a scenario with an approaching emergency vehicle | `Pending` | — |

### Dependencies

C2-S02, C2-S03, C1-S26, C1-S14

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
