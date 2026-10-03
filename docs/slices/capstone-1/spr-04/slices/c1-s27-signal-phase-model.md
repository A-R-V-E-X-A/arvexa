# C1-S27 — Signal-Phase Model

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 1  
> Sprint: SPR-04 — SUMO Baseline & Experiment Plan  
> Slice: C1-S27

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Define the complete signal phase structure for the SUMO junction: valid signal states, intergreen logic, and the TraCI interface through which ARVEXA will command phase changes.

**Inputs**
- Junction specification (C1-S21)
- `docs/architecture/action-space.md` (C1-S15)

**Outputs**
- Signal phase definition (`.add.xml` or embedded in `.net.xml`)
- Phase diagram showing all valid signal states and transitions
- TraCI command mapping document

**Acceptance Criteria**
- [ ] All valid signal phases are defined and enumerated
- [ ] All-red intergreen transitions are included between conflicting phases
- [ ] Phase can be changed via a TraCI command in a standalone test script
- [ ] Phase definitions are consistent with the action space architecture (C1-S15)

**Dependencies** — C1-S22, C1-S15

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
| All valid signal phases are defined and enumerated | `Pending` | — |
| All-red intergreen transitions are included between conflicting phases | `Pending` | — |
| Phase can be changed via a TraCI command in a standalone test script | `Pending` | — |
| Phase definitions are consistent with the action space architecture (C1-S15) | `Pending` | — |

### Dependencies

C1-S22, C1-S15

### Notes / Decisions

Record implementation decisions, deviations, assumptions, and supervisor feedback here.

### Change Log

| Date | Change | Author |
|---|---|---|
| YYYY-MM-DD | Initial documentation entry | TBD |
