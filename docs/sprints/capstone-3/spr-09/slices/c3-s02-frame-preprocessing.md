# C3-S02 — Frame Preprocessing

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 3  
> Sprint: SPR-09 — Computer Vision Pipeline  
> Slice: C3-S02

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Implement frame preprocessing: resizing to model input dimensions, normalisation, and an optional quality/blur check to skip uninformative frames.

**Inputs**
- `src/vision/video_ingestor.py` (C3-S01)
- Detection model input requirements (C3-S03 forward reference)

**Outputs**
- `src/vision/frame_preprocessor.py`
- Preprocessed frame tensors ready for detection

**Acceptance Criteria**
- [ ] Output frame dimensions match the configured model input size
- [ ] Pixel values are normalised to [0, 1] or model-expected range
- [ ] Frames below a configurable blur score are flagged and optionally skipped
- [ ] Processing rate is logged (frames/second)

**Dependencies** — C3-S01

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
| Output frame dimensions match the configured model input size | `Pending` | — |
| Pixel values are normalised to [0, 1] or model-expected range | `Pending` | — |
| Frames below a configurable blur score are flagged and optionally skipped | `Pending` | — |
| Processing rate is logged (frames/second) | `Pending` | — |

### Dependencies

C3-S01

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
