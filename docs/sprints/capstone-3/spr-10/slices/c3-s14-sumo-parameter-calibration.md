# C3-S14 — SUMO Parameter Calibration

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 3  
> Sprint: SPR-10 — Real-to-SUMO Calibration & Validation  
> Slice: C3-S14

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Adjust SUMO microscopic behavioural parameters (headway distribution, speed distribution, driver aggressiveness) to match real observed traffic behaviour beyond flow counts.

**Inputs**
- `data/real-traffic/flow-counts.csv` (C3-S11)
- `data/real-traffic/vehicle-type-distribution.csv` (C3-S12)
- SUMO vehicle type file (C1-S24), calibration plan (C1-S29)

**Outputs**
- `sumo/demand/vehicle-types-calibrated.add.xml`
- Parameter calibration report: parameter | original value | calibrated value | justification

**Acceptance Criteria**
- [ ] At least 3 behavioural parameters are adjusted (e.g., τ (headway), σ (speed deviation), accel)
- [ ] Each change is justified by an observable difference between real and simulated behaviour
- [ ] Calibrated vehicle type file is version-controlled separately from original

**Dependencies** — C3-S12, C1-S24, C1-S29

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
| At least 3 behavioural parameters are adjusted (e.g., τ (headway), σ (speed deviation), accel) | `Pending` | — |
| Each change is justified by an observable difference between real and simulated behaviour | `Pending` | — |
| Calibrated vehicle type file is version-controlled separately from original | `Pending` | — |

### Dependencies

C3-S12, C1-S24, C1-S29

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
