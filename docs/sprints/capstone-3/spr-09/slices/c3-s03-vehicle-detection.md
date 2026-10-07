# C3-S03 — Vehicle Detection

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 3  
> Sprint: SPR-09 — Computer Vision Pipeline  
> Slice: C3-S03

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Integrate a pre-trained object detection model to locate vehicles in each frame, producing bounding boxes with confidence scores.

**Inputs**
- `src/vision/frame_preprocessor.py` (C3-S02)
- Detection model (e.g., YOLOv8 or equivalent) and weights

**Outputs**
- `src/vision/vehicle_detector.py`
- Per-frame detection output: list of (bbox, confidence, raw_class_id)

**Acceptance Criteria**
- [ ] Model is loaded from a local weights file (not downloaded at runtime)
- [ ] Detections below a configurable confidence threshold are filtered
- [ ] Output schema is documented: (x1, y1, x2, y2, confidence, class_id)
- [ ] Inference runs on CPU and optionally GPU; device is configurable
- [ ] Unit test runs on a sample frame with at least one vehicle present

**Dependencies** — C3-S02

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
| Model is loaded from a local weights file (not downloaded at runtime) | `Pending` | — |
| Detections below a configurable confidence threshold are filtered | `Pending` | — |
| Output schema is documented: (x1, y1, x2, y2, confidence, class_id) | `Pending` | — |
| Inference runs on CPU and optionally GPU; device is configurable | `Pending` | — |
| Unit test runs on a sample frame with at least one vehicle present | `Pending` | — |

### Dependencies

C3-S02

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
