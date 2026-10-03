# C3-S12 — Vehicle-Type Distribution Extraction

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 3  
> Sprint: SPR-10 — Real-to-SUMO Calibration & Validation  
> Slice: C3-S12

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Compute the proportion of each vehicle type in the real traffic flow from the camera dataset. This will be used to calibrate SUMO's vehicle type mix.

**Inputs**
- `data/real-traffic/flow-counts.csv` (C3-S11)
- Classification output (C3-S04)

**Outputs**
- `data/real-traffic/vehicle-type-distribution.csv`: approach | category | proportion
- Distribution documented per time period (AM peak, PM peak, off-peak)

**Acceptance Criteria**
- [ ] Type proportions sum to 1.0 per approach per period
- [ ] At least 3 time periods are analysed if sufficient footage is available
- [ ] Distribution is compared to the assumed distribution in C1-S24 (with delta noted)

**Dependencies** — C3-S11, C3-S04

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
| Type proportions sum to 1.0 per approach per period | `Pending` | — |
| At least 3 time periods are analysed if sufficient footage is available | `Pending` | — |
| Distribution is compared to the assumed distribution in C1-S24 (with delta noted) | `Pending` | — |

### Dependencies

C3-S11, C3-S04

### Notes / Decisions

Record implementation decisions, deviations, assumptions, and supervisor feedback here.

### Change Log

| Date | Change | Author |
|---|---|---|
| YYYY-MM-DD | Initial documentation entry | TBD |
