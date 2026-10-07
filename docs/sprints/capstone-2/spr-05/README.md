# SPR-05 — SUMO & Traffic-State Pipeline

> **ARVEXA Sprint Documentation**  
> Capstone: Capstone 2  
> Slice range: **C2-S01 → C2-S09**

## Sprint Purpose

This folder contains the implementation and evidence documentation for **SPR-05 — SUMO & Traffic-State Pipeline**. Slice specifications are derived from the supplied ARVEXA Capstone specification.

## Sprint Status

- **Overall status:** `Not Started`
- **Owner:** `TBD`
- **Reviewer:** `TBD`
- **Start date:** `YYYY-MM-DD`
- **Target completion:** `YYYY-MM-DD`

## Slice Tracker

| Slice | Documentation | Status |
|---|---|---|
| C2-S01 | [SUMO Environment Wrapper](slices/c2-s01-sumo-environment-wrapper.md) | `Not Started` |
| C2-S02 | [Vehicle Detection & State Extraction](slices/c2-s02-vehicle-detection-state-extraction.md) | `Not Started` |
| C2-S03 | [Vehicle Classification / Type State](slices/c2-s03-vehicle-classification-type-state.md) | `Not Started` |
| C2-S04 | [Queue Estimation](slices/c2-s04-queue-estimation.md) | `Not Started` |
| C2-S05 | [Waiting-Time State](slices/c2-s05-waiting-time-state.md) | `Not Started` |
| C2-S06 | [Pedestrian State](slices/c2-s06-pedestrian-state.md) | `Not Started` |
| C2-S07 | [Emergency-Vehicle State](slices/c2-s07-emergency-vehicle-state.md) | `Not Started` |
| C2-S08 | [Sensor-Health State](slices/c2-s08-sensor-health-state.md) | `Not Started` |
| C2-S09 | [Unified State Builder](slices/c2-s09-unified-state-builder.md) | `Not Started` |

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
