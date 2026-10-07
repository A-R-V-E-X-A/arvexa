# C1-S28 — Baseline Fixed-Time Controller

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 1  
> Sprint: SPR-04 — SUMO Baseline & Experiment Plan  
> Slice: C1-S28

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Implement a fixed-time signal controller as the primary comparison baseline. The controller cycles through phases on a fixed schedule regardless of traffic state.

**Inputs**
- Signal-phase model (C1-S27)
- Junction timing plan (real-world or engineered)
- Reproducibility config (C1-S32 draft)

**Outputs**
- `src/baselines/fixed_time_controller.py`
- Baseline timing plan documented in config file

**Acceptance Criteria**
- [ ] Controller completes a full simulation run without errors
- [ ] Phase sequence and timing are configurable via config file, not hard-coded
- [ ] Per-step metrics (queue length, waiting time, throughput) are logged
- [ ] At least one complete run is committed with output logs
- [ ] Re-running with the same config and seed produces identical output

**Dependencies** — C1-S22, C1-S23, C1-S24, C1-S25, C1-S26, C1-S27

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
| Controller completes a full simulation run without errors | `Pending` | — |
| Phase sequence and timing are configurable via config file, not hard-coded | `Pending` | — |
| Per-step metrics (queue length, waiting time, throughput) are logged | `Pending` | — |
| At least one complete run is committed with output logs | `Pending` | — |
| Re-running with the same config and seed produces identical output | `Pending` | — |

### Dependencies

C1-S22, C1-S23, C1-S24, C1-S25, C1-S26, C1-S27

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
