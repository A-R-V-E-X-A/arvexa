# C1-S15 — Action Space

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 1  
> Sprint: SPR-03 — Architecture & Experimental Design  
> Slice: C1-S15

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Define the complete set of decisions the ARVEXA controller may take at each step: which signal phases may be selected and what duration values are permitted.

**Inputs**
- `docs/architecture/rl-state-representation.md` (C1-S14)
- Safety requirements (C1-S08)

**Outputs**
- `docs/architecture/action-space.md`
- Action space specification: type (discrete/continuous) | dimensions | valid range | constraints

**Acceptance Criteria**
- [ ] All valid signal phases are enumerated
- [ ] Duration action space is defined (range, step size or continuous bound)
- [ ] Every action is consistent with all SRs (minimum green times enforced)
- [ ] Invalid action handling policy is stated (masking, clipping, or penalty)
- [ ] Total action space size is documented

**Dependencies** — C1-S14, C1-S08

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
| All valid signal phases are enumerated | `Pending` | — |
| Duration action space is defined (range, step size or continuous bound) | `Pending` | — |
| Every action is consistent with all SRs (minimum green times enforced) | `Pending` | — |
| Invalid action handling policy is stated (masking, clipping, or penalty) | `Pending` | — |
| Total action space size is documented | `Pending` | — |

### Dependencies

C1-S14, C1-S08

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
