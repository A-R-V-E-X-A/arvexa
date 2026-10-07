# C1-S01 — Problem Definition

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 1  
> Sprint: SPR-01 — Research Foundation  
> Slice: C1-S01

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Document the traffic signal control problem ARVEXA addresses. Articulate the limitations of current systems (fixed-time, single-objective, sensor-dependent) and why an RL-based multi-modal approach is warranted. The statement must be precise enough to anchor all subsequent requirements.

**Inputs**
- Existing problem notes or drafts
- Literature on fixed-time and conventional adaptive signal control
- Domain knowledge of the study environment

**Outputs**
- `docs/research/problem-definition.md`

**Acceptance Criteria**
- [ ] Problem statement is expressed in ≤ 3 paragraphs, unambiguously
- [ ] At least 3 concrete limitations of current signal control systems are enumerated
- [ ] Affected stakeholder groups (commuters, pedestrians, emergency services) are identified
- [ ] Document is reviewed and approved by the project supervisor

**Dependencies** — None

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
| Problem statement is expressed in ≤ 3 paragraphs, unambiguously | `Pending` | — |
| At least 3 concrete limitations of current signal control systems are enumerated | `Pending` | — |
| Affected stakeholder groups (commuters, pedestrians, emergency services) are identified | `Pending` | — |
| Document is reviewed and approved by the project supervisor | `Pending` | — |

### Dependencies

None

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
