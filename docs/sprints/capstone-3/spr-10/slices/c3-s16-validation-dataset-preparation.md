# C3-S16 — Validation Dataset Preparation

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 3  
> Sprint: SPR-10 — Real-to-SUMO Calibration & Validation  
> Slice: C3-S16

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Prepare a held-out traffic dataset from a different time period (not used in calibration) to validate the calibrated SUMO model independently.

**Inputs**
- Camera footage from a different time period than the calibration footage

**Outputs**
- `data/real-traffic/validation-flow-counts.csv`
- Dataset notes: time period, duration, traffic conditions

**Acceptance Criteria**
- [ ] Validation footage covers a different time period than calibration footage
- [ ] Validation dataset includes at least 30 minutes of traffic
- [ ] Dataset is version-controlled and checksummed
- [ ] No data from the validation set was used in any calibration step

**Dependencies** — C3-S11

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
| Validation footage covers a different time period than calibration footage | `Pending` | — |
| Validation dataset includes at least 30 minutes of traffic | `Pending` | — |
| Dataset is version-controlled and checksummed | `Pending` | — |
| No data from the validation set was used in any calibration step | `Pending` | — |

### Dependencies

C3-S11

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
