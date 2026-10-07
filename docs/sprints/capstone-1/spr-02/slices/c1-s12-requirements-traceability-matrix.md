# C1-S12 — Requirements Traceability Matrix

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 1  
> Sprint: SPR-02 — Requirements & Traceability  
> Slice: C1-S12

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Produce the authoritative matrix linking every requirement upward to its RO and RQ, and noting the architectural component responsible for satisfying it. This is the single traceability artefact for the project.

**Inputs**
- All requirement documents: C1-S06 to C1-S11
- `docs/requirements/research-objectives.md` (C1-S03)

**Outputs**
- `docs/requirements/requirements-traceability-matrix.md` (or `.csv`)
- Columns: Req ID | Summary | Type | Parent RO | Parent RQ | Architecture Component | Sprint | Status

**Acceptance Criteria**
- [ ] Every requirement has exactly one row
- [ ] Every requirement is linked to at least one RO
- [ ] Every RO is linked to at least one RQ
- [ ] No orphan requirements exist (requirement with no RO)
- [ ] RTM is version-controlled and updated as architecture is defined in Sprint 3

**Dependencies** — C1-S03, C1-S06, C1-S07, C1-S08, C1-S09, C1-S10, C1-S11

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
| Every requirement has exactly one row | `Pending` | — |
| Every requirement is linked to at least one RO | `Pending` | — |
| Every RO is linked to at least one RQ | `Pending` | — |
| No orphan requirements exist (requirement with no RO) | `Pending` | — |
| RTM is version-controlled and updated as architecture is defined in Sprint 3 | `Pending` | — |

### Dependencies

C1-S03, C1-S06, C1-S07, C1-S08, C1-S09, C1-S10, C1-S11

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
