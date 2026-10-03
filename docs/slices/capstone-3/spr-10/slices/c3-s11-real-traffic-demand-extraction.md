# C3-S11 — Real Traffic Demand Extraction

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 3  
> Sprint: SPR-10 — Real-to-SUMO Calibration & Validation  
> Slice: C3-S11

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Process the vision pipeline output to produce a time-series dataset of vehicle flow counts per junction approach from the real camera footage.

**Inputs**
- Traffic statistics output (C3-S08)
- Camera footage (calibration period)

**Outputs**
- `data/real-traffic/flow-counts.csv`: timestamp | approach | direction | category | count
- `docs/data/real-traffic-dataset-notes.md`

**Acceptance Criteria**
- [ ] Flow counts cover at least 1 hour of representative traffic
- [ ] All junction approaches are represented
- [ ] Vehicle category breakdown (car, truck, motorcycle, emergency) is included
- [ ] Dataset is version-controlled and checksum-logged for reproducibility

**Dependencies** — C3-S08

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
| Flow counts cover at least 1 hour of representative traffic | `Pending` | — |
| All junction approaches are represented | `Pending` | — |
| Vehicle category breakdown (car, truck, motorcycle, emergency) is included | `Pending` | — |
| Dataset is version-controlled and checksum-logged for reproducibility | `Pending` | — |

### Dependencies

C3-S08

### Notes / Decisions

Record implementation decisions, deviations, assumptions, and supervisor feedback here.

### Change Log

| Date | Change | Author |
|---|---|---|
| YYYY-MM-DD | Initial documentation entry | TBD |
