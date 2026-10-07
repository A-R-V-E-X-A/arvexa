# C2-S22 — Stability / Signal-Switching Objective

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 2  
> Sprint: SPR-07 — Multi-Objective & Safety  
> Slice: C2-S22

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Implement a penalty for excessive signal phase switching, discouraging the policy from oscillating phases rapidly in a way that would cause real-world operational issues.

**Inputs**
- `src/environment/reward.py` (C2-S15)

**Outputs**
- `stability` component in `src/environment/reward.py`

**Acceptance Criteria**
- [ ] Penalty is applied each time a phase change occurs within a configurable minimum interval
- [ ] Penalty magnitude is configurable
- [ ] Logged separately in `info` dict
- [ ] Unit test confirms penalty fires on rapid switching

**Dependencies** — C2-S15

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
| Penalty is applied each time a phase change occurs within a configurable minimum interval | `Pending` | — |
| Penalty magnitude is configurable | `Pending` | — |
| Logged separately in `info` dict | `Pending` | — |
| Unit test confirms penalty fires on rapid switching | `Pending` | — |

### Dependencies

C2-S15

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
