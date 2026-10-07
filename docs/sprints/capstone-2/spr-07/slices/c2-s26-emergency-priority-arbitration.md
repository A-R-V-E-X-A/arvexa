# C2-S26 — Emergency Priority Arbitration

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 2  
> Sprint: SPR-07 — Multi-Objective & Safety  
> Slice: C2-S26

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Implement emergency vehicle preemption logic in the constraint layer: when an emergency vehicle is detected, override the RL policy to grant immediate green on the EV's approach.

**Inputs**
- `src/safety/constraint_layer.py` (C2-S25)
- Emergency-vehicle state (C2-S07), emergency-vehicle requirements (C1-S10)

**Outputs**
- Emergency preemption logic embedded in `constraint_layer.py`

**Acceptance Criteria**
- [ ] Preemption triggers when emergency vehicle state flag is active
- [ ] Preemption grants green on the EV approach within the configured maximum delay
- [ ] Preemption overrides any conflicting RL policy action
- [ ] Post-priority recovery returns to normal policy control after EV clears
- [ ] All EVRs from C1-S10 are satisfied and annotated in the code

**Dependencies** — C2-S25, C2-S07, C1-S10

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
| Preemption triggers when emergency vehicle state flag is active | `Pending` | — |
| Preemption grants green on the EV approach within the configured maximum delay | `Pending` | — |
| Preemption overrides any conflicting RL policy action | `Pending` | — |
| Post-priority recovery returns to normal policy control after EV clears | `Pending` | — |
| All EVRs from C1-S10 are satisfied and annotated in the code | `Pending` | — |

### Dependencies

C2-S25, C2-S07, C1-S10

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
