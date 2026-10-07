# C3-S15 — Real-vs-SUMO Traffic Comparison

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 3  
> Sprint: SPR-10 — Real-to-SUMO Calibration & Validation  
> Slice: C3-S15

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Compare simulated traffic metrics (post-calibration) against real traffic observations to quantify how well the calibrated SUMO model represents reality.

**Inputs**
- Calibrated demand (C3-S13) and parameters (C3-S14)
- `data/real-traffic/flow-counts.csv` (C3-S11)
- Evaluation metrics (C1-S31)

**Outputs**
- `docs/experiments/calibration-comparison-report.md`
- Comparison table: metric | real value | simulated value | GEH / RMSE / % error

**Acceptance Criteria**
- [ ] GEH ≤ 5 for ≥ 85% of directional flows (or alternative threshold justified)
- [ ] Per-approach comparison is presented
- [ ] Residual errors are analysed and their potential impact on ARVEXA evaluation is discussed
- [ ] Report is sufficient evidence of calibration quality for the thesis

**Dependencies** — C3-S13, C3-S14, C3-S11

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
| GEH ≤ 5 for ≥ 85% of directional flows (or alternative threshold justified) | `Pending` | — |
| Per-approach comparison is presented | `Pending` | — |
| Residual errors are analysed and their potential impact on ARVEXA evaluation is discussed | `Pending` | — |
| Report is sufficient evidence of calibration quality for the thesis | `Pending` | — |

### Dependencies

C3-S13, C3-S14, C3-S11

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
