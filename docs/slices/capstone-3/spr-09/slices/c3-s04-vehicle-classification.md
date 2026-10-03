# C3-S04 — Vehicle Classification

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 3  
> Sprint: SPR-09 — Computer Vision Pipeline  
> Slice: C3-S04

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Map raw detection class IDs to the ARVEXA vehicle type categories (car, truck/bus, motorcycle, emergency vehicle) used by the state representation.

**Inputs**
- `src/vision/vehicle_detector.py` (C3-S03)
- Vehicle-type model (C1-S24): ARVEXA category definitions

**Outputs**
- Vehicle classification output: each detection now carries an ARVEXA category label
- `config/vision/class-mapping.yaml`: raw model class → ARVEXA category

**Acceptance Criteria**
- [ ] Class mapping is fully configurable via YAML (no hard-coded label strings)
- [ ] Emergency vehicle category is mapped (e.g., from ambulance, fire truck classes)
- [ ] Unknown/unmapped class IDs are logged as 'unknown' and not silently dropped
- [ ] Unit test covers each ARVEXA category mapping

**Dependencies** — C3-S03, C1-S24

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
| Class mapping is fully configurable via YAML (no hard-coded label strings) | `Pending` | — |
| Emergency vehicle category is mapped (e.g., from ambulance, fire truck classes) | `Pending` | — |
| Unknown/unmapped class IDs are logged as 'unknown' and not silently dropped | `Pending` | — |
| Unit test covers each ARVEXA category mapping | `Pending` | — |

### Dependencies

C3-S03, C1-S24

### Notes / Decisions

Record implementation decisions, deviations, assumptions, and supervisor feedback here.

### Change Log

| Date | Change | Author |
|---|---|---|
| YYYY-MM-DD | Initial documentation entry | TBD |
