# C1-S16 — Reward & Objective Architecture

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 1  
> Sprint: SPR-03 — Architecture & Experimental Design  
> Slice: C1-S16

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Define the reward function structure: the individual objective components (traffic efficiency, pedestrian safety, emergency priority, stability, robustness), how each is measured, and how they are aggregated into a training signal.

**Inputs**
- Functional requirements (C1-S06), pedestrian requirements (C1-S11), emergency requirements (C1-S10)

**Outputs**
- `docs/architecture/reward-architecture.md`
- Reward component table: Component | Formula | Measurement Source | Range | Weight Placeholder

**Acceptance Criteria**
- [ ] At least 5 distinct reward components are defined
- [ ] Each component is measurable from simulation state
- [ ] Aggregation method is specified (weighted sum, Pareto front, or alternatives with decision criteria)
- [ ] Component range is documented for each element
- [ ] Reward architecture is consistent with all FRs and priority requirements

**Dependencies** — C1-S14, C1-S15

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
| At least 5 distinct reward components are defined | `Pending` | — |
| Each component is measurable from simulation state | `Pending` | — |
| Aggregation method is specified (weighted sum, Pareto front, or alternatives with decision criteria) | `Pending` | — |
| Component range is documented for each element | `Pending` | — |
| Reward architecture is consistent with all FRs and priority requirements | `Pending` | — |

### Dependencies

C1-S14, C1-S15

### Notes / Decisions

Record implementation decisions, deviations, assumptions, and supervisor feedback here.

### Change Log

| Date | Change | Author |
|---|---|---|
| YYYY-MM-DD | Initial documentation entry | TBD |
