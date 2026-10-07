# C1-S19 — Vision Pipeline Architecture

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 1  
> Sprint: SPR-03 — Architecture & Experimental Design  
> Slice: C1-S19

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Define the architecture of the computer vision subsystem that will process real camera footage to extract traffic state information in Capstone-3. This is a design document only; implementation is deferred.

**Inputs**
- `docs/architecture/system-architecture.md` (C1-S13)
- `docs/architecture/rl-state-representation.md` (C1-S14)

**Outputs**
- `docs/architecture/vision-pipeline-architecture.md`
- Pipeline diagram: Camera → Frames → Detection → Classification → Tracking → Counting → Traffic State

**Acceptance Criteria**
- [ ] Each pipeline stage is named and its input/output types are defined
- [ ] Output of each stage maps to specific state elements from C1-S14
- [ ] Failure modes of each stage are identified
- [ ] Interface between vision pipeline output and ARVEXA state builder is specified
- [ ] Document clearly notes that full implementation is deferred to Capstone-3

**Dependencies** — C1-S13, C1-S14

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
| Each pipeline stage is named and its input/output types are defined | `Pending` | — |
| Output of each stage maps to specific state elements from C1-S14 | `Pending` | — |
| Failure modes of each stage are identified | `Pending` | — |
| Interface between vision pipeline output and ARVEXA state builder is specified | `Pending` | — |
| Document clearly notes that full implementation is deferred to Capstone-3 | `Pending` | — |

### Dependencies

C1-S13, C1-S14

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
