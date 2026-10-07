# C2-S18 — Deterministic Evaluation Mode

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 2  
> Sprint: SPR-06 — RL Controller  
> Slice: C2-S18

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Implement a script that loads a trained checkpoint and evaluates it deterministically (no exploration) across a specified set of scenarios, logging all metrics.

**Inputs**
- `src/training/train.py` (C2-S16), checkpoint system (C2-S17)
- Evaluation metrics spec (C1-S31)

**Outputs**
- `src/evaluation/evaluate.py`
- Evaluation output: per-episode metrics CSV, summary statistics

**Acceptance Criteria**
- [ ] Evaluation uses argmax / deterministic policy (no stochastic sampling)
- [ ] Running the same evaluation twice with the same checkpoint and seed produces identical results
- [ ] All metrics from C1-S31 are computed and logged
- [ ] Output is saved with run-ID tagging (C1-S32)

**Dependencies** — C2-S17, C1-S31, C1-S32

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
| Evaluation uses argmax / deterministic policy (no stochastic sampling) | `Pending` | — |
| Running the same evaluation twice with the same checkpoint and seed produces identical results | `Pending` | — |
| All metrics from C1-S31 are computed and logged | `Pending` | — |
| Output is saved with run-ID tagging (C1-S32) | `Pending` | — |

### Dependencies

C2-S17, C1-S31, C1-S32

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
