# C2-S02 — Vehicle Detection & State Extraction

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 2  
> Sprint: SPR-05 — SUMO & Traffic-State Pipeline  
> Slice: C2-S02

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Extract per-vehicle state data (position, speed, waiting time, lane) from the SUMO simulation using TraCI subscriptions for all vehicles within the junction influence area.

**Inputs**
- `src/environment/sumo_env.py` (C2-S01)
- State representation spec (C1-S14)

**Outputs**
- `src/environment/vehicle_detector.py`
- Vehicle state schema documentation (fields, types, units)

**Acceptance Criteria**
- [ ] Vehicle positions, speeds, and waiting times are retrieved via TraCI subscription (not polling)
- [ ] Detection is bounded to the junction influence area (configurable radius or lane list)
- [ ] Output is a dictionary keyed by vehicle ID
- [ ] Unit test validates detection output against a known SUMO scenario

**Dependencies** — C2-S01, C1-S14

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
| Vehicle positions, speeds, and waiting times are retrieved via TraCI subscription (not polling) | `Pending` | — |
| Detection is bounded to the junction influence area (configurable radius or lane list) | `Pending` | — |
| Output is a dictionary keyed by vehicle ID | `Pending` | — |
| Unit test validates detection output against a known SUMO scenario | `Pending` | — |

### Dependencies

C2-S01, C1-S14

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
