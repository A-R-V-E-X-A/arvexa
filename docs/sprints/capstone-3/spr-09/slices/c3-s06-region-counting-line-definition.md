# C3-S06 — Region & Counting Line Definition

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 3  
> Sprint: SPR-09 — Computer Vision Pipeline  
> Slice: C3-S06

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Define counting lines and regions of interest (ROIs) for each junction approach using the camera's perspective of the junction geometry.

**Inputs**
- Junction geometry (C1-S21): approach lanes and directions
- Camera metadata (C3-S10 — prepare early draft): field of view, mounting position

**Outputs**
- `config/vision/counting-lines.yaml`: per-approach line coordinates in image space
- Visual confirmation overlay image showing lines on a sample frame

**Acceptance Criteria**
- [ ] At least one counting line per junction approach
- [ ] Counting lines are defined in pixel coordinates and are camera-specific
- [ ] Direction of crossing (inbound/outbound) is defined per line
- [ ] Visual overlay confirms correct placement on a sample frame

**Dependencies** — C3-S05, C1-S21

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
| At least one counting line per junction approach | `Pending` | — |
| Counting lines are defined in pixel coordinates and are camera-specific | `Pending` | — |
| Direction of crossing (inbound/outbound) is defined per line | `Pending` | — |
| Visual overlay confirms correct placement on a sample frame | `Pending` | — |

### Dependencies

C3-S05, C1-S21

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
