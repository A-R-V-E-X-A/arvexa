# C3-S22 — Pedestrian Input Integration

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 3  
> Sprint: SPR-11 — Full ARVEXA Integration  
> Slice: C3-S22

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Connect pedestrian detection/counting from the vision pipeline to the ARVEXA pedestrian state channel.

**Inputs**
- Pedestrian detection (requires extension of vision pipeline or separate pedestrian model)
- Pedestrian state channel (C2-S06)
- Pedestrian requirements (C1-S11)

**Outputs**
- Pedestrian state sourced from vision pipeline in `vision_state_adapter.py`
- Documentation of any pedestrian detection model used

**Acceptance Criteria**
- [ ] Pedestrian count per crossing is populated from vision output
- [ ] If pedestrian detection is not available, a documented fallback is used and justified
- [ ] Pedestrian state update respects the minimum crossing time requirement (from C1-S11)
- [ ] Unit test confirms pedestrian count is correctly mapped to state elements

**Dependencies** — C3-S18, C2-S06, C1-S11

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
| Pedestrian count per crossing is populated from vision output | `Pending` | — |
| If pedestrian detection is not available, a documented fallback is used and justified | `Pending` | — |
| Pedestrian state update respects the minimum crossing time requirement (from C1-S11) | `Pending` | — |
| Unit test confirms pedestrian count is correctly mapped to state elements | `Pending` | — |

### Dependencies

C3-S18, C2-S06, C1-S11

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
