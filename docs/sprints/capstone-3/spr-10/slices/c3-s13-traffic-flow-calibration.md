# C3-S13 — Traffic-Flow Calibration

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 3  
> Sprint: SPR-10 — Real-to-SUMO Calibration & Validation  
> Slice: C3-S13

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Adjust the SUMO demand files to match the real observed vehicle flow rates from the camera dataset. This is the primary demand-level calibration step.

**Inputs**
- `data/real-traffic/flow-counts.csv` (C3-S11)
- `sumo/demand/traffic-demand.rou.xml` (C1-S23)
- SUMO calibration plan (C1-S29)

**Outputs**
- `sumo/demand/traffic-demand-calibrated.rou.xml`
- Calibration report: observed flow vs simulated flow per approach (before and after)

**Acceptance Criteria**
- [ ] Calibrated demand file is distinct from the original (version-controlled separately)
- [ ] Calibration report includes GEH statistic or RMSE per approach
- [ ] Calibration metric from C1-S29 is evaluated and reported
- [ ] Calibration is documented step-by-step (reproducible without the researcher)

**Dependencies** — C3-S11, C1-S23, C1-S29

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
| Calibrated demand file is distinct from the original (version-controlled separately) | `Pending` | — |
| Calibration report includes GEH statistic or RMSE per approach | `Pending` | — |
| Calibration metric from C1-S29 is evaluated and reported | `Pending` | — |
| Calibration is documented step-by-step (reproducible without the researcher) | `Pending` | — |

### Dependencies

C3-S11, C1-S23, C1-S29

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
