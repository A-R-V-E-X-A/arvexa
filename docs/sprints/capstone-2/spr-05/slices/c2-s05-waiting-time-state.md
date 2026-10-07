# C2-S05 — Waiting-Time State

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 2  
> Sprint: SPR-05 — SUMO & Traffic-State Pipeline  
> Slice: C2-S05

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Extract and aggregate cumulative waiting time per lane and per approach from the SUMO vehicle data.

**Inputs**
- `src/environment/vehicle_detector.py` (C2-S02)
- State representation spec (C1-S14)

**Outputs**
- Waiting-time aggregation module (may be part of `queue_estimator.py` or separate)
- Waiting-time state elements: per-lane and per-approach totals

**Acceptance Criteria**
- [ ] Cumulative waiting time is summed across all detected vehicles per lane
- [ ] Output matches waiting-time state element specification in C1-S14
- [ ] Reset correctly zeroes waiting-time accumulators between episodes
- [ ] Unit test validates against a known stopped-vehicle scenario

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
| Cumulative waiting time is summed across all detected vehicles per lane | `Pending` | — |
| Output matches waiting-time state element specification in C1-S14 | `Pending` | — |
| Reset correctly zeroes waiting-time accumulators between episodes | `Pending` | — |
| Unit test validates against a known stopped-vehicle scenario | `Pending` | — |

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
