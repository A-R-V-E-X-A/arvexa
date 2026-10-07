# C3-S20 — Vision Degradation Handling

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 3  
> Sprint: SPR-11 — Full ARVEXA Integration  
> Slice: C3-S20

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Implement fallback behaviour in the vision-state adapter when the vision pipeline produces no detections, produces below-threshold confidence, or fails entirely.

**Inputs**
- `src/integration/vision_state_adapter.py` (C3-S18)
- Sensor degradation model (C1-S20), sensor-failure requirements (C1-S09)

**Outputs**
- Fallback logic in `vision_state_adapter.py`
- Fallback modes: last-known-value, zero-fill, or fixed-default (configurable per element)

**Acceptance Criteria**
- [ ] Fallback mode for each state element is configurable (not hard-coded)
- [ ] Fallback does not violate any SR (safety requirements still enforced)
- [ ] Fallback activation is logged with reason code and timestamp
- [ ] All SFRs from C1-S09 are satisfied and referenced in code comments

**Dependencies** — C3-S18, C1-S20, C1-S09

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
| Fallback mode for each state element is configurable (not hard-coded) | `Pending` | — |
| Fallback does not violate any SR (safety requirements still enforced) | `Pending` | — |
| Fallback activation is logged with reason code and timestamp | `Pending` | — |
| All SFRs from C1-S09 are satisfied and referenced in code comments | `Pending` | — |

### Dependencies

C3-S18, C1-S20, C1-S09

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
