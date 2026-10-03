# C3-S21 — Emergency-Vehicle Detection / Input

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 3  
> Sprint: SPR-11 — Full ARVEXA Integration  
> Slice: C3-S21

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Connect the vision pipeline's emergency vehicle classification to the ARVEXA emergency vehicle state channel, enabling real-world emergency priority triggering.

**Inputs**
- `src/vision/vehicle_tracker.py` (C3-S05), classification (C3-S04): emergency category
- Emergency-vehicle state channel (C2-S07)
- Emergency-vehicle requirements (C1-S10)

**Outputs**
- Emergency vehicle state populated from vision pipeline in `vision_state_adapter.py`

**Acceptance Criteria**
- [ ] Emergency vehicle presence flag is set when a tracked vehicle is classified as emergency
- [ ] Approach lane and distance estimate are populated from tracker output
- [ ] False negative test: if EV is misclassified, fallback behaviour is logged
- [ ] Integration test confirms preemption is triggered when EV is detected via vision

**Dependencies** — C3-S18, C2-S07, C3-S05, C3-S04, C1-S10

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
| Emergency vehicle presence flag is set when a tracked vehicle is classified as emergency | `Pending` | — |
| Approach lane and distance estimate are populated from tracker output | `Pending` | — |
| False negative test: if EV is misclassified, fallback behaviour is logged | `Pending` | — |
| Integration test confirms preemption is triggered when EV is detected via vision | `Pending` | — |

### Dependencies

C3-S18, C2-S07, C3-S05, C3-S04, C1-S10

### Notes / Decisions

Record implementation decisions, deviations, assumptions, and supervisor feedback here.

### Change Log

| Date | Change | Author |
|---|---|---|
| YYYY-MM-DD | Initial documentation entry | TBD |
