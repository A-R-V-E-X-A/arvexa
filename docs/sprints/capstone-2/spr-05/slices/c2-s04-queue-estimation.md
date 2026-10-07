# C2-S04 — Queue Estimation

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 2  
> Sprint: SPR-05 — SUMO & Traffic-State Pipeline  
> Slice: C2-S04

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Compute queue length (number of stopped or near-stopped vehicles) per lane and per approach from the vehicle detection output.

**Inputs**
- `src/environment/vehicle_detector.py` (C2-S02)
- State representation spec (C1-S14)

**Outputs**
- `src/environment/queue_estimator.py`
- Queue state: per-lane vehicle count at speed ≤ threshold

**Acceptance Criteria**
- [ ] Queue is computed per lane and aggregated per approach
- [ ] Stopped-vehicle threshold (speed ≤ X m/s) is configurable
- [ ] Output matches the queue state element specification in C1-S14
- [ ] Unit test validates queue count against a known scenario

**Dependencies** — C2-S02, C1-S14

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
| Queue is computed per lane and aggregated per approach | `Pending` | — |
| Stopped-vehicle threshold (speed ≤ X m/s) is configurable | `Pending` | — |
| Output matches the queue state element specification in C1-S14 | `Pending` | — |
| Unit test validates queue count against a known scenario | `Pending` | — |

### Dependencies

C2-S02, C1-S14

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
