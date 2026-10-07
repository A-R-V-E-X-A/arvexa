# SPR-03 — Architecture & Experimental Design

> **ARVEXA Sprint Documentation**  
> Capstone: Capstone 1  
> Slice range: **C1-S13 → C1-S20**

## Sprint Purpose

This folder contains the implementation and evidence documentation for **SPR-03 — Architecture & Experimental Design**. Slice specifications are derived from the supplied ARVEXA Capstone specification.

## Sprint Status

- **Overall status:** `Not Started`
- **Owner:** `TBD`
- **Reviewer:** `TBD`
- **Start date:** `YYYY-MM-DD`
- **Target completion:** `YYYY-MM-DD`

## Slice Tracker

| Slice | Documentation | Status |
|---|---|---|
| C1-S13 | [Overall System Architecture](slices/c1-s13-overall-system-architecture.md) | `Not Started` |
| C1-S14 | [RL State Representation](slices/c1-s14-rl-state-representation.md) | `Not Started` |
| C1-S15 | [Action Space](slices/c1-s15-action-space.md) | `Not Started` |
| C1-S16 | [Reward & Objective Architecture](slices/c1-s16-reward-objective-architecture.md) | `Not Started` |
| C1-S17 | [Safety & Action Constraint Layer](slices/c1-s17-safety-action-constraint-layer.md) | `Not Started` |
| C1-S18 | [SUMO Architecture](slices/c1-s18-sumo-architecture.md) | `Not Started` |
| C1-S19 | [Vision Pipeline Architecture](slices/c1-s19-vision-pipeline-architecture.md) | `Not Started` |
| C1-S20 | [Sensor Degradation Model](slices/c1-s20-sensor-degradation-model.md) | `Not Started` |

## Sprint-Level Evidence

### Deliverables
- [ ] All slice deliverables completed
- [ ] Acceptance criteria reviewed
- [ ] Tests/evaluations executed
- [ ] Evidence linked from each completed slice
- [ ] Sprint-level review completed

### Evidence Directory

```text
evidence/
├── screenshots/
├── logs/
├── test-results/
├── plots/
└── reports/
```

## Sprint Review Notes

Record completed work, deviations, unresolved issues, and supervisor/team review comments.

## Sprint Exit Checklist

- [ ] All required slices are implemented or explicitly documented as deferred
- [ ] Acceptance criteria have evidence
- [ ] Dependencies are satisfied
- [ ] Deviations from the source specification are documented
- [ ] Reproducibility instructions are available where applicable
- [ ] Sprint reviewed and approved

## Change Log

| Date | Change | Author |
|---|---|---|
| YYYY-MM-DD | Initial sprint documentation | TBD |

## Research Direction Alignment — Reliability-Aware Study

These sprint/slice activities must remain aligned with the current ARVEXA research anchor:

> Does more traffic information always improve adaptive traffic-signal control when the reliability of that information varies?

The research should treat state richness and observation reliability as explicit experimental variables. R1–R4 representations, controlled degradation modes, matched comparisons, safety/priority constraints, and reproducible evaluation should follow the authoritative documents:

- `docs/research/research-direction.md`
- `docs/architecture/rl-state-representation.md`
- `docs/experiments/research-evaluation-protocol.md`

Do not present pedestrian handling, emergency priority, sensor failure, computer vision, heterogeneous traffic, or RL individually as the novelty. Their role is to create and evaluate the information–reliability decision-making problem.
