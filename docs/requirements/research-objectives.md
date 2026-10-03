# ARVEXA Research Objectives

## 1. Objective Framework

ARVEXA uses the traceability chain:

Research Objective → Requirement → Architecture Component → Implementation Slice → Experiment → Metric → Result

This document freezes the research objectives that implementation must support.

## 2. Primary Objectives

### RO-01 — Heterogeneous Traffic Representation

Represent relevant vehicle classes and traffic-state variables in the controller state.

**Evidence:** vehicle-type ablation comparing type-aware and aggregate-only state representations.

### RO-02 — Adaptive Phase and Duration Selection

Develop a controller that dynamically selects the next permissible signal phase and an allowed duration or duration class.

**Evidence:** comparison against fixed-time and rule-based baselines.

### RO-03 — Pedestrian Safety

Represent pedestrian demand and enforce signal-safety and pedestrian-clearance constraints.

**Evidence:** pedestrian waiting/service metrics and constraint-violation count.

### RO-04 — Emergency-Vehicle Priority

Represent emergency-vehicle presence, approach, and priority state.

**Evidence:** emergency response metrics and non-emergency traffic impact.

### RO-05 — Sensor-Failure Resilience

Evaluate the controller under missing, noisy, and partially failed observations.

**Evidence:** performance-versus-degradation curves.

### RO-06 — Real-World-Grounded Simulation

Develop a SUMO representation of a selected real-world junction and calibrate traffic demand and composition using observations.

**Evidence:** real-versus-simulated traffic comparison.

### RO-07 — Reproducible Evaluation

Define a repeatable experimental protocol including scenarios, seeds, configurations, baselines, and metrics.

**Evidence:** repeated runs and documented experiment configurations.

### RO-08 — Vision-Based Traffic Observation

Develop a camera-processing pipeline that extracts useful traffic statistics.

**Evidence:** detection/counting validation and comparison with manually reviewed samples where feasible.

## 3. Secondary Objectives

### RO-09 — Multi-Objective Trade-Off Analysis

Quantify how traffic demand, pedestrian demand, emergency priority, and sensor quality affect competing objectives.

### RO-10 — Component Contribution

Use ablation studies to determine which ARVEXA components materially affect performance.

### RO-11 — Generalization within the Study Domain

Evaluate the controller under traffic conditions different from the primary training distribution while remaining within the modeled junction/domain.

## 4. Objective Layers

| Layer | Objectives |
|---|---|
| Foundation | RO-01, RO-06, RO-07 |
| Controller | RO-02, RO-03, RO-04 |
| Resilience | RO-05 |
| Validation | RO-08 |
| Analysis | RO-09, RO-10, RO-11 |

## 5. Completion Principle

An objective is complete only when evidence exists.

For example, sensor-failure code alone does not complete RO-05. Completion requires controlled failure scenarios, severity levels, baseline comparison, metrics, and analysis.

## 6. Traceability IDs

- RO-01: Heterogeneous traffic
- RO-02: Adaptive phase/duration
- RO-03: Pedestrian safety
- RO-04: Emergency priority
- RO-05: Sensor resilience
- RO-06: SUMO calibration
- RO-07: Reproducibility
- RO-08: Vision observation
- RO-09: Trade-off analysis
- RO-10: Ablation
- RO-11: Domain generalization
