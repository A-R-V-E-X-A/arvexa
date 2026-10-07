# C1-S18 — SUMO Architecture

> **ARVEXA Slice Documentation**  
> Capstone: Capstone 1  
> Sprint: SPR-03 — Architecture & Experimental Design  
> Slice: C1-S18

## Status

- **Implementation status:** `Not Started`
- **Evidence status:** `Pending`
- **Last updated:** `YYYY-MM-DD`
- **Owner:** `TBD`
- **Reviewer:** `TBD`

## Source Specification

**Objective**
Define how SUMO is configured as the simulation backbone: network structure, vehicle types, signal control interface (TraCI), and how ARVEXA connects to it.

**Inputs**
- `docs/architecture/system-architecture.md` (C1-S13)
- SUMO and TraCI documentation

**Outputs**
- `docs/architecture/sumo-architecture.md`
- SUMO integration diagram: ARVEXA ↔ TraCI ↔ SUMO Network

**Acceptance Criteria**
- [ ] TraCI interface is specified (commands and subscriptions to be used)
- [ ] SUMO simulation step size and ARVEXA decision-step relationship are defined
- [ ] Signal phase → SUMO TLS state mapping is documented
- [ ] Vehicle type configuration approach is specified
- [ ] Headless/batch execution approach is described (for reproducible experiments)

**Dependencies** — C1-S13, C1-S15

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
| TraCI interface is specified (commands and subscriptions to be used) | `Pending` | — |
| SUMO simulation step size and ARVEXA decision-step relationship are defined | `Pending` | — |
| Signal phase → SUMO TLS state mapping is documented | `Pending` | — |
| Vehicle type configuration approach is specified | `Pending` | — |
| Headless/batch execution approach is described (for reproducible experiments) | `Pending` | — |

### Dependencies

C1-S13, C1-S15

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
