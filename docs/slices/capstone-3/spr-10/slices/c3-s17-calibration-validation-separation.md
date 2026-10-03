# C3-S17 — Calibration / Validation Separation

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 3  
> Sprint: SPR-10 — Real-to-SUMO Calibration & Validation  
> Slice: C3-S17

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Document and enforce the strict separation between calibration and validation datasets. Produce a provenance record that makes the split auditable for academic review.

**Inputs**
- C3-S13 (calibration dataset), C3-S16 (validation dataset)

**Outputs**
- `docs/experiments/calibration-validation-protocol.md`
- Dataset provenance record: file | period | role (calibration/validation) | checksum

**Acceptance Criteria**
- [ ] Calibration and validation files are stored in separate directories
- [ ] No flow observation appears in both datasets
- [ ] Provenance record includes timestamps of data collection for each dataset
- [ ] Protocol document is referenced in the thesis as evidence of separation

**Dependencies** — C3-S13, C3-S16

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
| Calibration and validation files are stored in separate directories | `Pending` | — |
| No flow observation appears in both datasets | `Pending` | — |
| Provenance record includes timestamps of data collection for each dataset | `Pending` | — |
| Protocol document is referenced in the thesis as evidence of separation | `Pending` | — |

### Dependencies

C3-S13, C3-S16

### Notes / Decisions

Record implementation decisions, deviations, assumptions, and supervisor feedback here.

### Change Log

| Date | Change | Author |
|---|---|---|
| YYYY-MM-DD | Initial documentation entry | TBD |
