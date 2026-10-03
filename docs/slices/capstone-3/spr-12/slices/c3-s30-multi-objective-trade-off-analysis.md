# C3-S30 — Multi-Objective Trade-Off Analysis

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 3  
> Sprint: SPR-12 — Final Evaluation & Capstone-3  
> Slice: C3-S30

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Analyse the relationship between competing objectives in ARVEXA's results: traffic efficiency vs pedestrian safety vs emergency priority. Determine whether gains in one metric come at a cost to others.

**Inputs**
- Final ARVEXA results (C3-S29)
- Reward weight configurations (C2-S24)

**Outputs**
- `docs/results/multi-objective-tradeoff-analysis.md`
- Trade-off plots: metric pairs plotted against each other across scenarios and weight configurations

**Acceptance Criteria**
- [ ] At least 3 metric pairs are analysed for trade-off (e.g., throughput vs pedestrian wait, throughput vs EV delay)
- [ ] Results are presented for at least 2 different reward weight configurations if available
- [ ] Conclusions reference the multi-objective reward architecture (C1-S16)
- [ ] Analysis is suitable for inclusion in the thesis discussion section

**Dependencies** — C3-S29, C2-S24, C1-S16

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
| At least 3 metric pairs are analysed for trade-off (e.g., throughput vs pedestrian wait, throughput vs EV delay) | `Pending` | — |
| Results are presented for at least 2 different reward weight configurations if available | `Pending` | — |
| Conclusions reference the multi-objective reward architecture (C1-S16) | `Pending` | — |
| Analysis is suitable for inclusion in the thesis discussion section | `Pending` | — |

### Dependencies

C3-S29, C2-S24, C1-S16

### Notes / Decisions

Record implementation decisions, deviations, assumptions, and supervisor feedback here.

### Change Log

| Date | Change | Author |
|---|---|---|
| YYYY-MM-DD | Initial documentation entry | TBD |
