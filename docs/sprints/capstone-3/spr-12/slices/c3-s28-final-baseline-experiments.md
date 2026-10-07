# C3-S28 — Final Baseline Experiments

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 3  
> Sprint: SPR-12 — Final Evaluation & Capstone-3  
> Slice: C3-S28

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Run all baseline controllers (fixed-time and any additional baselines from Capstone-2) across all final experiment scenarios using the calibrated SUMO model and the reproducibility pipeline.

**Inputs**
- Fixed-time baseline (C1-S28)
- Final experiment scenarios (C1-S30, using calibrated demand from C3-S13)
- Experiment automation (C3-S24), result logging (C3-S26)

**Outputs**
- `results/final/baseline/` — complete baseline results for all scenarios and seeds

**Acceptance Criteria**
- [ ] All scenarios from C1-S30 are covered
- [ ] At least 5 seeds per scenario
- [ ] All metrics from C1-S31 are recorded per run
- [ ] Results are tagged with run-IDs and reproducible

**Dependencies** — C1-S28, C1-S30, C3-S13, C3-S24, C3-S26

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
| All scenarios from C1-S30 are covered | `Pending` | — |
| At least 5 seeds per scenario | `Pending` | — |
| All metrics from C1-S31 are recorded per run | `Pending` | — |
| Results are tagged with run-IDs and reproducible | `Pending` | — |

### Dependencies

C1-S28, C1-S30, C3-S13, C3-S24, C3-S26

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
