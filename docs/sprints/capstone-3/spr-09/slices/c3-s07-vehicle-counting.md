# C3-S07 — Vehicle Counting

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 3  
> Sprint: SPR-09 — Computer Vision Pipeline  
> Slice: C3-S07

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Count vehicles crossing each defined counting line per time interval and direction, using the tracking output to avoid double-counting a single vehicle.

**Inputs**
- `src/vision/vehicle_tracker.py` (C3-S05)
- Counting line definitions (C3-S06)

**Outputs**
- `src/vision/vehicle_counter.py`
- Per-interval count: (approach, direction, vehicle_category, count, timestamp)

**Acceptance Criteria**
- [ ] Each unique track ID is counted at most once per crossing per line
- [ ] Counts are aggregated per configurable time interval (e.g., 30 s, 5 min)
- [ ] Category-level counts (car, truck, emergency) are available alongside total
- [ ] Counts are logged to CSV with timestamps

**Dependencies** — C3-S05, C3-S06

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
| Each unique track ID is counted at most once per crossing per line | `Pending` | — |
| Counts are aggregated per configurable time interval (e.g., 30 s, 5 min) | `Pending` | — |
| Category-level counts (car, truck, emergency) are available alongside total | `Pending` | — |
| Counts are logged to CSV with timestamps | `Pending` | — |

### Dependencies

C3-S05, C3-S06

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
