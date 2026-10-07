# C2-S31 — Partial Sensor Failure

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 2  
> Sprint: SPR-08 — Sensor Resilience & Simulation Evaluation  
> Slice: C2-S31

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Run evaluation experiments where a subset of junction approaches (lanes) lose sensor coverage, while others remain operational. Assess how ARVEXA adapts with partial observability.

**Inputs**
- Sensor degradation model (C1-S20), mode: partial (lane/approach subset)
- Trained ARVEXA controller (C2-S17)

**Outputs**
- Evaluation results CSV: `results/c2/partial-failure/`

**Acceptance Criteria**
- [ ] At least 2 different subsets of failed approaches are tested
- [ ] Sensor health state channel reflects failed approaches
- [ ] Results show performance degradation curve as more approaches lose coverage
- [ ] Fallback behaviour (from SFR) is active and logged

**Dependencies** — C1-S20, C2-S08, C2-S17, C2-S18, C1-S30

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
| At least 2 different subsets of failed approaches are tested | `Pending` | — |
| Sensor health state channel reflects failed approaches | `Pending` | — |
| Results show performance degradation curve as more approaches lose coverage | `Pending` | — |
| Fallback behaviour (from SFR) is active and logged | `Pending` | — |

### Dependencies

C1-S20, C2-S08, C2-S17, C2-S18, C1-S30

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
