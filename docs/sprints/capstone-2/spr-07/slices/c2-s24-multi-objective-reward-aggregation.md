# C2-S24 — Multi-Objective Reward Aggregation

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 2  
> Sprint: SPR-07 — Multi-Objective & Safety  
> Slice: C2-S24

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Implement the configurable weighted aggregation of all reward components into the scalar training signal used by the RL algorithm.

**Inputs**
- Components C2-S19 to C2-S23
- Reward architecture spec (C1-S16)

**Outputs**
- Updated `src/environment/reward.py` with weight configuration
- `config/reward-weights.yaml`

**Acceptance Criteria**
- [ ] Weights for all components are specified in a config file
- [ ] Total reward is a weighted sum (or other documented aggregation) of components
- [ ] Weights sum constraint is enforced or documented
- [ ] Changing weights via config changes training behaviour without code modification
- [ ] Integration test confirms all components contribute to the total

**Dependencies** — C2-S19, C2-S20, C2-S21, C2-S22, C2-S23, C1-S16

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
| Weights for all components are specified in a config file | `Pending` | — |
| Total reward is a weighted sum (or other documented aggregation) of components | `Pending` | — |
| Weights sum constraint is enforced or documented | `Pending` | — |
| Changing weights via config changes training behaviour without code modification | `Pending` | — |
| Integration test confirms all components contribute to the total | `Pending` | — |

### Dependencies

C2-S19, C2-S20, C2-S21, C2-S22, C2-S23, C1-S16

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
