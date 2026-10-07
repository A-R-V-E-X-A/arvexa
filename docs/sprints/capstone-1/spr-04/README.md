# SPR-04 — SUMO Baseline & Experiment Plan

> **ARVEXA Sprint Documentation**  
> Capstone: Capstone 1  
> Slice range: **C1-S21 → C1-S32**

## Sprint Purpose

This folder contains the implementation and evidence documentation for **SPR-04 — SUMO Baseline & Experiment Plan**. Slice specifications are derived from the supplied ARVEXA Capstone specification.

## Sprint Status

- **Overall status:** `Not Started`
- **Owner:** `TBD`
- **Reviewer:** `TBD`
- **Start date:** `YYYY-MM-DD`
- **Target completion:** `YYYY-MM-DD`

## Slice Tracker

| Slice | Documentation | Status |
|---|---|---|
| C1-S21 | [Junction Selection](slices/c1-s21-junction-selection.md) | `Not Started` |
| C1-S22 | [SUMO Network Construction](slices/c1-s22-sumo-network-construction.md) | `Not Started` |
| C1-S23 | [Traffic Demand Model](slices/c1-s23-traffic-demand-model.md) | `Not Started` |
| C1-S24 | [Vehicle-Type Model](slices/c1-s24-vehicle-type-model.md) | `Not Started` |
| C1-S25 | [Pedestrian Model](slices/c1-s25-pedestrian-model.md) | `Not Started` |
| C1-S26 | [Emergency-Vehicle Model](slices/c1-s26-emergency-vehicle-model.md) | `Not Started` |
| C1-S27 | [Signal-Phase Model](slices/c1-s27-signal-phase-model.md) | `Not Started` |
| C1-S28 | [Baseline Fixed-Time Controller](slices/c1-s28-baseline-fixed-time-controller.md) | `Not Started` |
| C1-S29 | [SUMO Calibration Plan](slices/c1-s29-sumo-calibration-plan.md) | `Not Started` |
| C1-S30 | [Experiment Scenarios](slices/c1-s30-experiment-scenarios.md) | `Not Started` |
| C1-S31 | [Evaluation Metrics](slices/c1-s31-evaluation-metrics.md) | `Not Started` |
| C1-S32 | [Reproducibility Configuration](slices/c1-s32-reproducibility-configuration.md) | `Not Started` |

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
