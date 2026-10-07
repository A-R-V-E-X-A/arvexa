# C2-S16 — Training Pipeline

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 2  
> Sprint: SPR-06 — RL Controller  
> Slice: C2-S16

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Set up the RL training loop, integrating the chosen algorithm with the ARVEXA environment. The algorithm choice is finalised here based on state/action/baseline feasibility from Sprint 5.

**Inputs**
- `src/environment/arvexa_env.py` (C2-S10)
- `src/environment/reward.py` (C2-S15)
- `config/experiment-defaults.yaml` (C1-S32)

**Outputs**
- `src/training/train.py`
- Training configuration (algorithm hyperparameters, episode length, max steps)

**Acceptance Criteria**
- [ ] Training script runs to completion on the normal-demand scenario
- [ ] Training progress is logged (episode reward, episode length, per-component reward)
- [ ] Algorithm and all hyperparameters are specified in a config file
- [ ] Training can be interrupted and resumed from the latest checkpoint

**Dependencies** — C2-S10, C2-S15, C1-S32

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
| Training script runs to completion on the normal-demand scenario | `Pending` | — |
| Training progress is logged (episode reward, episode length, per-component reward) | `Pending` | — |
| Algorithm and all hyperparameters are specified in a config file | `Pending` | — |
| Training can be interrupted and resumed from the latest checkpoint | `Pending` | — |

### Dependencies

C2-S10, C2-S15, C1-S32

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
