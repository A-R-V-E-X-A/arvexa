# C1-S11 — Pedestrian Requirements

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 1  
> Sprint: SPR-02 — Requirements & Traceability  
> Slice: C1-S11

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Document requirements governing ARVEXA's handling of pedestrian demand, pedestrian phase scheduling, and minimum crossing-time protection.

**Inputs**
- `docs/requirements/functional-requirements.md` (C1-S06)
- `docs/requirements/safety-requirements.md` (C1-S08)

**Outputs**
- `docs/requirements/pedestrian-requirements.md`
- PR list with IDs: PR-001 … PR-N

**Acceptance Criteria**
- [ ] Minimum pedestrian crossing time is specified per crossing
- [ ] Pedestrian demand detection requirements are stated
- [ ] Conditions under which a pedestrian phase may be deferred are stated (if any)
- [ ] Pedestrian vs. vehicle phase priority arbitration rules are stated
- [ ] Conflict with emergency-vehicle preemption is explicitly addressed
- [ ] At least 5 PRs documented

**Dependencies** — C1-S06, C1-S08, C1-S10

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
| Minimum pedestrian crossing time is specified per crossing | `Pending` | — |
| Pedestrian demand detection requirements are stated | `Pending` | — |
| Conditions under which a pedestrian phase may be deferred are stated (if any) | `Pending` | — |
| Pedestrian vs. vehicle phase priority arbitration rules are stated | `Pending` | — |
| Conflict with emergency-vehicle preemption is explicitly addressed | `Pending` | — |
| At least 5 PRs documented | `Pending` | — |

### Dependencies

C1-S06, C1-S08, C1-S10

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
