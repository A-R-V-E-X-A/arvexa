# C2-S33 — Baseline Comparison

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 2  
> Sprint: SPR-08 — Sensor Resilience & Simulation Evaluation  
> Slice: C2-S33

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Run the fixed-time baseline controller across all experiment scenarios used for ARVEXA evaluation, producing a complete baseline metrics dataset for comparison.

**Inputs**
- Fixed-time baseline controller (C1-S28)
- All experiment scenarios (C1-S30)
- Evaluation metrics (C1-S31), reproducibility config (C1-S32)

**Outputs**
- Baseline results CSV: `results/c2/baseline/`
- All metrics from C1-S31 populated for baseline

**Acceptance Criteria**
- [ ] Baseline is evaluated across all scenarios used for ARVEXA
- [ ] Baseline runs use the same demand files and seeds as ARVEXA runs
- [ ] All metrics from C1-S31 are present in baseline output
- [ ] Results are reproducible from run-ID

**Dependencies** — C1-S28, C1-S30, C1-S31, C1-S32

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
| Baseline is evaluated across all scenarios used for ARVEXA | `Pending` | — |
| Baseline runs use the same demand files and seeds as ARVEXA runs | `Pending` | — |
| All metrics from C1-S31 are present in baseline output | `Pending` | — |
| Results are reproducible from run-ID | `Pending` | — |

### Dependencies

C1-S28, C1-S30, C1-S31, C1-S32

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
