# C1-S23 — Traffic Demand Model

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 1  
> Sprint: SPR-04 — SUMO Baseline & Experiment Plan  
> Slice: C1-S23

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Define vehicle flow rates (vehicles/hour per approach and movement) for each experiment scenario. These form the input demand for all SUMO simulations.

**Inputs**
- Junction specification (C1-S21)
- Available traffic count data or engineering estimates

**Outputs**
- `sumo/demand/traffic-demand.rou.xml`
- `docs/experiments/traffic-demand-model.md`
- Demand table: Approach × Movement × Scenario × Flow Rate (veh/hr)

**Acceptance Criteria**
- [ ] At least 3 demand levels defined: low, medium, high
- [ ] Demand covers all junction approaches
- [ ] Demand file loads in SUMO without errors
- [ ] Demand parameters are version-controlled and not hard-coded

**Dependencies** — C1-S22

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
| At least 3 demand levels defined: low, medium, high | `Pending` | — |
| Demand covers all junction approaches | `Pending` | — |
| Demand file loads in SUMO without errors | `Pending` | — |
| Demand parameters are version-controlled and not hard-coded | `Pending` | — |

### Dependencies

C1-S22

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
