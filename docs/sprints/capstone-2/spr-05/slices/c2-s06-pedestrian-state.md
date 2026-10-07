# C2-S06 — Pedestrian State

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 2  
> Sprint: SPR-05 — SUMO & Traffic-State Pipeline  
> Slice: C2-S06

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Extract pedestrian presence, count, and waiting time at each crossing from SUMO and include them as state elements.

**Inputs**
- `src/environment/sumo_env.py` (C2-S01)
- Pedestrian model (C1-S25), state representation spec (C1-S14)

**Outputs**
- Pedestrian state channel in the detector/state pipeline
- Per-crossing pedestrian count and waiting time

**Acceptance Criteria**
- [ ] Pedestrian presence is detected per crossing via TraCI
- [ ] Pedestrian count and maximum waiting time are available as state elements
- [ ] Output matches pedestrian state element specification in C1-S14
- [ ] Unit test uses a scenario with pedestrians at a crossing

**Dependencies** — C2-S01, C1-S25, C1-S14

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
| Pedestrian presence is detected per crossing via TraCI | `Pending` | — |
| Pedestrian count and maximum waiting time are available as state elements | `Pending` | — |
| Output matches pedestrian state element specification in C1-S14 | `Pending` | — |
| Unit test uses a scenario with pedestrians at a crossing | `Pending` | — |

### Dependencies

C2-S01, C1-S25, C1-S14

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
