# C3-S39 — Thesis / Report

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 3  
> Sprint: SPR-12 — Final Evaluation & Capstone-3  
> Slice: C3-S39

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Write and submit the complete capstone thesis or final report documenting the ARVEXA research: problem, methodology, implementation, experiments, results, and conclusions.

**Inputs**
- All research documents from Capstone-1 (`docs/research/`, `docs/requirements/`, `docs/architecture/`)
- All result documents and figures from Capstone-2 and Capstone-3
- C3-S35 (statistical analysis), C3-S36 (figures), C3-S38 (documentation)

**Outputs**
- `thesis/arvexa-thesis.pdf` (or institutional submission format)

**Acceptance Criteria**
- [ ] Thesis covers: Introduction, Literature Review, Methodology, System Architecture, Experiments, Results, Discussion, Conclusion
- [ ] Every figure and table is numbered and referenced in the text
- [ ] Every statistical claim is backed by a test result from C3-S35
- [ ] All requirement categories (FR, SR, SFR, EVR, PR) are referenced in the evaluation
- [ ] Reproducibility package is cited with access instructions
- [ ] Submitted by institutional deadline

**Dependencies** — C3-S30, C3-S31, C3-S32, C3-S33, C3-S34, C3-S35, C3-S36

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
| Thesis covers: Introduction, Literature Review, Methodology, System Architecture, Experiments, Results, Discussion, Conclusion | `Pending` | — |
| Every figure and table is numbered and referenced in the text | `Pending` | — |
| Every statistical claim is backed by a test result from C3-S35 | `Pending` | — |
| All requirement categories (FR, SR, SFR, EVR, PR) are referenced in the evaluation | `Pending` | — |
| Reproducibility package is cited with access instructions | `Pending` | — |
| Submitted by institutional deadline | `Pending` | — |

### Dependencies

C3-S30, C3-S31, C3-S32, C3-S33, C3-S34, C3-S35, C3-S36

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
