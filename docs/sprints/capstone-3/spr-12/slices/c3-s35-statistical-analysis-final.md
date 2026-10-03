# C3-S35 — Statistical Analysis (Final)

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 3  
> Sprint: SPR-12 — Final Evaluation & Capstone-3  
> Slice: C3-S35

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Apply appropriate inferential statistics to the final experiment results, comparing ARVEXA against baselines across all scenarios and degradation modes.

**Inputs**
- Final ARVEXA results (C3-S29), baseline results (C3-S28)
- Ablation results (C3-S34)

**Outputs**
- `src/analysis/final_statistics.py`
- Full statistical report: per-metric summary tables with mean ± std, 95% CI, p-value, effect size

**Acceptance Criteria**
- [ ] Appropriate test selected per metric (parametric if normality confirmed, otherwise non-parametric)
- [ ] Multiple comparison correction applied if testing across many scenarios
- [ ] Effect size (Cohen's d or rank-biserial r) reported alongside p-values
- [ ] All statistical decisions and assumptions are documented in the thesis

**Dependencies** — C3-S29, C3-S28, C3-S34

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
| Appropriate test selected per metric (parametric if normality confirmed, otherwise non-parametric) | `Pending` | — |
| Multiple comparison correction applied if testing across many scenarios | `Pending` | — |
| Effect size (Cohen's d or rank-biserial r) reported alongside p-values | `Pending` | — |
| All statistical decisions and assumptions are documented in the thesis | `Pending` | — |

### Dependencies

C3-S29, C3-S28, C3-S34

### Notes / Decisions

Record implementation decisions, deviations, assumptions, and supervisor feedback here.

### Change Log

| Date | Change | Author |
|---|---|---|
| YYYY-MM-DD | Initial documentation entry | TBD |
