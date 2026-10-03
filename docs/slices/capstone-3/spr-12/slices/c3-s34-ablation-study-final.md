# C3-S34 — Ablation Study (Final)

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 3  
> Sprint: SPR-12 — Final Evaluation & Capstone-3  
> Slice: C3-S34

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Produce the final ablation study, removing each ARVEXA component in isolation and measuring the performance impact, using the fully integrated and calibrated final pipeline.

**Inputs**
- Final ARVEXA pipeline (C3-S23)
- Ablation variants from Capstone-2 (C2-S36) or retrained variants
- Statistical analysis (C3-S35 forward dependency)

**Outputs**
- `results/final/ablation/` — ablation variant results under final setup
- Ablation table: removed component | Δ metric | statistical significance

**Acceptance Criteria**
- [ ] Each reward component from C2-S19 to C2-S23 is ablated
- [ ] At least one architectural component is ablated (e.g., safety constraint layer removed)
- [ ] Ablation results are statistically analysed (significance tested)
- [ ] Table is thesis-ready

**Dependencies** — C3-S23, C2-S36, C3-S29

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
| Each reward component from C2-S19 to C2-S23 is ablated | `Pending` | — |
| At least one architectural component is ablated (e.g., safety constraint layer removed) | `Pending` | — |
| Ablation results are statistically analysed (significance tested) | `Pending` | — |
| Table is thesis-ready | `Pending` | — |

### Dependencies

C3-S23, C2-S36, C3-S29

### Notes / Decisions

Record implementation decisions, deviations, assumptions, and supervisor feedback here.

### Change Log

| Date | Change | Author |
|---|---|---|
| YYYY-MM-DD | Initial documentation entry | TBD |
