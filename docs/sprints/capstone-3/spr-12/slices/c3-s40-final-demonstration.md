# C3-S40 — Final Demonstration

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 3  
> Sprint: SPR-12 — Final Evaluation & Capstone-3  
> Slice: C3-S40

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Prepare and deliver the final project demonstration showing the end-to-end ARVEXA system: camera footage → vision pipeline → controller → SUMO simulation with signal commands.

**Inputs**
- End-to-end pipeline (C3-S23)
- Sample camera footage or live camera feed
- Result figures and thesis (C3-S36, C3-S39)

**Outputs**
- Demonstration presentation (slides + live demo)
- Demo setup instructions (so the demo can be reproduced on any machine)

**Acceptance Criteria**
- [ ] Demonstration runs end-to-end without manual intervention
- [ ] SUMO visualisation (SUMO-GUI) is shown with ARVEXA controlling signals in real time
- [ ] Key results (metric improvements over baseline) are presented clearly
- [ ] Emergency vehicle and pedestrian scenarios are demonstrated
- [ ] Demo can be set up from scratch in ≤ 30 minutes using the demo instructions

**Dependencies** — C3-S23, C3-S36, C3-S39

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
| Demonstration runs end-to-end without manual intervention | `Pending` | — |
| SUMO visualisation (SUMO-GUI) is shown with ARVEXA controlling signals in real time | `Pending` | — |
| Key results (metric improvements over baseline) are presented clearly | `Pending` | — |
| Emergency vehicle and pedestrian scenarios are demonstrated | `Pending` | — |
| Demo can be set up from scratch in ≤ 30 minutes using the demo instructions | `Pending` | — |

### Dependencies

C3-S23, C3-S36, C3-S39

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
