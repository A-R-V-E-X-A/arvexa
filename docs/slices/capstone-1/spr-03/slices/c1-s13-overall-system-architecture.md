# C1-S13 — Overall System Architecture

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 1  
> Sprint: SPR-03 — Architecture & Experimental Design  
> Slice: C1-S13

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Produce a top-level architecture document and diagram showing all ARVEXA subsystems (RL controller, SUMO environment, vision pipeline, safety constraint layer, state builder) and the interfaces between them.

**Inputs**
- All requirements documents (C1-S06 to C1-S11)
- Existing architecture notes

**Outputs**
- `docs/architecture/system-architecture.md`
- Top-level architecture diagram (C4 Level 2 or equivalent)
- Interface table: subsystem → subsystem | data type | direction | frequency

**Acceptance Criteria**
- [ ] All major subsystems are identified and named
- [ ] All inter-subsystem interfaces are described (data format, direction, update frequency)
- [ ] Architecture is consistent with all FRs and NFRs
- [ ] No implementation-level detail (no specific library choices forced without justification)
- [ ] Reviewed and approved by supervisor

**Dependencies** — C1-S06, C1-S07, C1-S12

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
| All major subsystems are identified and named | `Pending` | — |
| All inter-subsystem interfaces are described (data format, direction, update frequency) | `Pending` | — |
| Architecture is consistent with all FRs and NFRs | `Pending` | — |
| No implementation-level detail (no specific library choices forced without justification) | `Pending` | — |
| Reviewed and approved by supervisor | `Pending` | — |

### Dependencies

C1-S06, C1-S07, C1-S12

### Notes / Decisions

Record implementation decisions, deviations, assumptions, and supervisor feedback here.

### Change Log

| Date | Change | Author |
|---|---|---|
| YYYY-MM-DD | Initial documentation entry | TBD |
