# C3-S01 — Video Ingestion

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 3  
> Sprint: SPR-09 — Computer Vision Pipeline  
> Slice: C3-S01

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Implement a module that loads video files or live camera streams and emits a sequence of frames for downstream processing, with configurable frame-rate subsampling.

**Inputs**
- Recorded camera footage from the selected junction (C1-S21)
- Camera metadata (resolution, frame rate — to be produced in C3-S10)

**Outputs**
- `src/vision/video_ingestor.py`
- Frame generator interface (yields frames with timestamps)

**Acceptance Criteria**
- [ ] Accepts both file path and RTSP/stream URL inputs
- [ ] Frame-rate subsampling is configurable (process every N-th frame)
- [ ] Timestamp is attached to each emitted frame
- [ ] Module handles end-of-stream gracefully (no crash, emits termination signal)
- [ ] Unit test processes a short sample video clip without error

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
| Accepts both file path and RTSP/stream URL inputs | `Pending` | — |
| Frame-rate subsampling is configurable (process every N-th frame) | `Pending` | — |
| Timestamp is attached to each emitted frame | `Pending` | — |
| Module handles end-of-stream gracefully (no crash, emits termination signal) | `Pending` | — |
| Unit test processes a short sample video clip without error | `Pending` | — |

### Dependencies

C1-S21

### Notes / Decisions

Record implementation decisions, deviations, assumptions, and supervisor feedback here.

### Change Log

| Date | Change | Author |
|---|---|---|
| YYYY-MM-DD | Initial documentation entry | TBD |
