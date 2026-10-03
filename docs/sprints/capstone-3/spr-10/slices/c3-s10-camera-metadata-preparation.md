# C3-S10 — Camera Metadata Preparation

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 3  
> Sprint: SPR-10 — Real-to-SUMO Calibration & Validation  
> Slice: C3-S10

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Document the physical camera setup at the selected junction: position, mounting height, angle, field of view, resolution, and frame rate. This metadata underpins counting-line placement and calibration.

**Inputs**
- Physical camera installation at the junction (C1-S21)

**Outputs**
- `docs/vision/camera-metadata.md`
- Per-camera config YAML: position (GPS + height), angle, resolution, frame rate

**Acceptance Criteria**
- [ ] GPS coordinates and mounting height are recorded for each camera
- [ ] Field of view (horizontal and vertical degrees) is estimated or measured
- [ ] Resolution and frame rate are documented
- [ ] Metadata is sufficient to reconstruct counting-line placement (C3-S06)

**Dependencies** — C1-S21

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
| GPS coordinates and mounting height are recorded for each camera | `Pending` | — |
| Field of view (horizontal and vertical degrees) is estimated or measured | `Pending` | — |
| Resolution and frame rate are documented | `Pending` | — |
| Metadata is sufficient to reconstruct counting-line placement (C3-S06) | `Pending` | — |

### Dependencies

C1-S21

### Notes / Decisions

Record implementation decisions, deviations, assumptions, and supervisor feedback here.

### Change Log

| Date | Change | Author |
|---|---|---|
| YYYY-MM-DD | Initial documentation entry | TBD |
