# C3-S19 — Sensor Uncertainty Propagation

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 3  
> Sprint: SPR-11 — Full ARVEXA Integration  
> Slice: C3-S19

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Pass detection confidence scores from the vision pipeline through the state builder as uncertainty signals, updating the sensor-health state channel to reflect vision pipeline confidence.

**Inputs**
- `src/vision/vehicle_detector.py` (C3-S03): per-detection confidence
- `src/environment/sensor_health.py` (C2-S08)
- `src/integration/vision_state_adapter.py` (C3-S18)

**Outputs**
- Confidence-aware health channel: sensor health is a function of mean detection confidence in the current interval
- Updated `vision_state_adapter.py`

**Acceptance Criteria**
- [ ] Sensor health channel reflects current vision pipeline confidence (not a fixed value)
- [ ] Low-confidence frames produce reduced health indicator values
- [ ] Health channel changes are reflected in the state vector consumed by the controller
- [ ] Unit test demonstrates health channel response to varying confidence levels

**Dependencies** — C3-S18, C2-S08, C3-S03

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
| Sensor health channel reflects current vision pipeline confidence (not a fixed value) | `Pending` | — |
| Low-confidence frames produce reduced health indicator values | `Pending` | — |
| Health channel changes are reflected in the state vector consumed by the controller | `Pending` | — |
| Unit test demonstrates health channel response to varying confidence levels | `Pending` | — |

### Dependencies

C3-S18, C2-S08, C3-S03

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
