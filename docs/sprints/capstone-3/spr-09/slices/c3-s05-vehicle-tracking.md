# C3-S05 — Vehicle Tracking

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 3  
> Sprint: SPR-09 — Computer Vision Pipeline  
> Slice: C3-S05

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Implement multi-object tracking to maintain consistent vehicle IDs across frames, enabling counting of unique vehicles rather than per-frame detections.

**Inputs**
- `src/vision/vehicle_detector.py` (C3-S03), classification (C3-S04)
- Tracking algorithm (e.g., ByteTrack, SORT, or BoT-SORT)

**Outputs**
- `src/vision/vehicle_tracker.py`
- Per-frame tracked object list: (track_id, bbox, category, confidence)

**Acceptance Criteria**
- [ ] Each tracked vehicle maintains a consistent ID across frames
- [ ] Track ID is created on first detection and terminated after a configurable number of missed frames
- [ ] Tracker is configurable: maximum age, minimum hits before confirmation
- [ ] Unit test demonstrates consistent ID assignment across 10 consecutive frames

**Dependencies** — C3-S03, C3-S04

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
| Each tracked vehicle maintains a consistent ID across frames | `Pending` | — |
| Track ID is created on first detection and terminated after a configurable number of missed frames | `Pending` | — |
| Tracker is configurable: maximum age, minimum hits before confirmation | `Pending` | — |
| Unit test demonstrates consistent ID assignment across 10 consecutive frames | `Pending` | — |

### Dependencies

C3-S03, C3-S04

### Notes / Decisions

Record implementation decisions, deviations, assumptions, and supervisor feedback here.

### Change Log

| Date | Change | Author |
|---|---|---|
| YYYY-MM-DD | Initial documentation entry | TBD |
