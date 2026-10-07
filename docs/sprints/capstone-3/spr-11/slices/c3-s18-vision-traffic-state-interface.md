# C3-S18 — Vision → Traffic-State Interface

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 3  
> Sprint: SPR-11 — Full ARVEXA Integration  
> Slice: C3-S18

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Implement the adapter that converts the vision pipeline's traffic statistics output into the ARVEXA state element format consumed by the state builder.

**Inputs**
- `src/vision/traffic_statistics.py` (C3-S08)
- State representation spec (C1-S14)
- `src/environment/state_builder.py` (C2-S09)

**Outputs**
- `src/integration/vision_state_adapter.py`
- Mapping table: vision statistic → state element (documented in code and in `docs/architecture/`)

**Acceptance Criteria**
- [ ] All state elements sourced from vision have a corresponding adapter mapping
- [ ] Adapter output is type-compatible with the state builder input interface
- [ ] No state element is silently dropped or left unset if vision pipeline is running
- [ ] Unit test confirms correct mapping for a sample traffic statistics input

**Dependencies** — C3-S08, C2-S09, C1-S14

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
| All state elements sourced from vision have a corresponding adapter mapping | `Pending` | — |
| Adapter output is type-compatible with the state builder input interface | `Pending` | — |
| No state element is silently dropped or left unset if vision pipeline is running | `Pending` | — |
| Unit test confirms correct mapping for a sample traffic statistics input | `Pending` | — |

### Dependencies

C3-S08, C2-S09, C1-S14

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
