# C3-S23 — End-to-End Controller Integration

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 3  
> Sprint: SPR-11 — Full ARVEXA Integration  
> Slice: C3-S23

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Connect all components into a single runnable pipeline: camera footage or stream → vision pipeline → state builder → ARVEXA controller → SUMO signal command.

**Inputs**
- `src/vision/` (C3-S01 to C3-S08)
- `src/integration/vision_state_adapter.py` (C3-S18 to C3-S22)
- `src/environment/arvexa_env.py` (C2-S10)
- Trained controller checkpoint (C2-S17)

**Outputs**
- `src/integration/arvexa_pipeline.py`
- End-to-end integration test script

**Acceptance Criteria**
- [ ] Pipeline runs from a video file input to a SUMO simulation step without manual intervention
- [ ] All components are connected via documented interfaces (no direct imports across layers)
- [ ] Pipeline completes a 15-minute simulation without crashing
- [ ] Output matches the expected format from C1-S31 evaluation metrics

**Dependencies** — C3-S18, C3-S19, C3-S20, C3-S21, C3-S22, C2-S10, C2-S17

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
| Pipeline runs from a video file input to a SUMO simulation step without manual intervention | `Pending` | — |
| All components are connected via documented interfaces (no direct imports across layers) | `Pending` | — |
| Pipeline completes a 15-minute simulation without crashing | `Pending` | — |
| Output matches the expected format from C1-S31 evaluation metrics | `Pending` | — |

### Dependencies

C3-S18, C3-S19, C3-S20, C3-S21, C3-S22, C2-S10, C2-S17

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
