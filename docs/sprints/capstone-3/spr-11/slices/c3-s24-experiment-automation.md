# C3-S24 — Experiment Automation

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 3  
> Sprint: SPR-11 — Full ARVEXA Integration  
> Slice: C3-S24

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Implement scripts to run the full ARVEXA experiment suite automatically across all scenario configs, without manual intervention between scenarios.

**Inputs**
- Experiment scenarios (C1-S30)
- Reproducibility config (C1-S32)
- End-to-end pipeline (C3-S23), evaluation script (C2-S18)

**Outputs**
- `scripts/run_experiments.py`
- Experiment batch config: `config/experiments/batch.yaml`

**Acceptance Criteria**
- [ ] A single command runs all scenarios for both ARVEXA and all baselines
- [ ] Each run is tagged with a unique run-ID and scenario ID
- [ ] Failed runs are logged with error messages and do not abort the batch
- [ ] Estimated total runtime is documented so resource planning is possible

**Dependencies** — C3-S23, C1-S30, C1-S32, C2-S18

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
| A single command runs all scenarios for both ARVEXA and all baselines | `Pending` | — |
| Each run is tagged with a unique run-ID and scenario ID | `Pending` | — |
| Failed runs are logged with error messages and do not abort the batch | `Pending` | — |
| Estimated total runtime is documented so resource planning is possible | `Pending` | — |

### Dependencies

C3-S23, C1-S30, C1-S32, C2-S18

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
