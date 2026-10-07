# C2-S17 — Model Checkpointing

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 2  
> Sprint: SPR-06 — RL Controller  
> Slice: C2-S17

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Implement saving and loading of trained model checkpoints, including the model weights, training step, and associated config.

**Inputs**
- `src/training/train.py` (C2-S16)

**Outputs**
- Checkpoint save/load logic in `src/training/`
- `checkpoints/` directory structure with run-ID subdirectories

**Acceptance Criteria**
- [ ] Checkpoints are saved at configurable intervals (e.g., every N steps)
- [ ] Best checkpoint (by evaluation metric) is saved separately
- [ ] Loading a checkpoint and continuing training from it produces consistent behaviour
- [ ] Checkpoint includes: model weights, optimizer state, step count, config hash

**Dependencies** — C2-S16

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
| Checkpoints are saved at configurable intervals (e.g., every N steps) | `Pending` | — |
| Best checkpoint (by evaluation metric) is saved separately | `Pending` | — |
| Loading a checkpoint and continuing training from it produces consistent behaviour | `Pending` | — |
| Checkpoint includes: model weights, optimizer state, step count, config hash | `Pending` | — |

### Dependencies

C2-S16

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
