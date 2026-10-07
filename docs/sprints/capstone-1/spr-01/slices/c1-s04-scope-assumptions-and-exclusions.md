# C1-S04 — Scope, Assumptions and Exclusions

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 1  
> Sprint: SPR-01 — Research Foundation  
> Slice: C1-S04

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Explicitly bound what ARVEXA will and will not address. Document the assumptions the project relies on (e.g., simulation fidelity, camera availability) and the exclusions that are out of scope (e.g., multi-junction coordination, V2I communication).

**Inputs**
- `docs/research/problem-definition.md` (C1-S01)
- `docs/research/research-questions.md` (C1-S02)

**Outputs**
- `docs/research/scope-assumptions-exclusions.md`

**Acceptance Criteria**
- [ ] In-scope items are listed with justification referencing an RQ or RO
- [ ] Out-of-scope items are listed with justification for exclusion
- [ ] At least 5 explicit assumptions are documented
- [ ] No exclusion contradicts an active research objective
- [ ] Reviewed and approved by supervisor

**Dependencies** — C1-S01, C1-S02

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
| In-scope items are listed with justification referencing an RQ or RO | `Pending` | — |
| Out-of-scope items are listed with justification for exclusion | `Pending` | — |
| At least 5 explicit assumptions are documented | `Pending` | — |
| No exclusion contradicts an active research objective | `Pending` | — |
| Reviewed and approved by supervisor | `Pending` | — |

### Dependencies

C1-S01, C1-S02

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
