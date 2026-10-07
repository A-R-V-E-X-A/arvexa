# C1-S21 — Junction Selection

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 1  
> Sprint: SPR-04 — SUMO Baseline & Experiment Plan  
> Slice: C1-S21

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Select and justify the real-world junction that will serve as the ARVEXA study site. It must be representative of the target problem, accessible for camera data collection in Capstone-3, and of sufficient complexity.

**Inputs**
- `docs/research/scope-assumptions-exclusions.md` (C1-S04)
- Local geographic knowledge; camera placement accessibility assessment

**Outputs**
- `docs/experiments/junction-selection.md`
- Junction specification: GPS coordinates, junction type (4-way / T-junction etc.), geometry, existing phase plan

**Acceptance Criteria**
- [ ] Junction is identified with GPS coordinates and name
- [ ] Junction type and physical geometry are described
- [ ] Existing signal phase plan (if any) is documented or noted as absent
- [ ] Camera placement feasibility is assessed (line of sight, mounting options)
- [ ] Justification references at least one research objective

**Dependencies** — C1-S04

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
| Junction is identified with GPS coordinates and name | `Pending` | — |
| Junction type and physical geometry are described | `Pending` | — |
| Existing signal phase plan (if any) is documented or noted as absent | `Pending` | — |
| Camera placement feasibility is assessed (line of sight, mounting options) | `Pending` | — |
| Justification references at least one research objective | `Pending` | — |

### Dependencies

C1-S04

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
