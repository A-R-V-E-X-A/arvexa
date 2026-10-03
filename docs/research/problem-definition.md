# ARVEXA Research Problem Definition

## 1. Project Context

ARVEXA (Adaptive Resilient Vehicle–pedestrian eXchange Architecture) is a research framework for adaptive traffic signal control in heterogeneous urban traffic.

The project investigates whether a multi-objective reinforcement-learning controller can dynamically select both the next permissible signal phase and its duration while accounting for heterogeneous vehicle demand, vehicle efficiency, pedestrian crossing demand and safety, emergency-vehicle priority, imperfect observations, and real-camera-grounded SUMO validation.

The primary controlled environment is a selected real-world junction represented in SUMO. The model will be calibrated using available traffic observations and evaluated through controlled simulation experiments. Real camera footage will be processed through a vision pipeline to obtain traffic statistics and compare them with simulated traffic conditions.

## 2. Problem Statement

The central research problem is:

> How can a multi-objective reinforcement-learning traffic signal controller dynamically select safe signal phases and durations for heterogeneous urban traffic while balancing traffic efficiency, pedestrian safety, emergency-vehicle priority, and resilience to imperfect sensing?

The problem contains five connected dimensions.

### 2.1 Heterogeneous traffic

Aggregate vehicle count does not fully describe traffic demand. Vehicle type can affect occupancy, discharge rate, acceleration, and queue characteristics. ARVEXA therefore investigates state representations that retain relevant vehicle-type information.

### 2.2 Multi-objective control

A controller cannot optimize only one measure when pedestrians and emergency vehicles are also considered. ARVEXA therefore evaluates multiple objectives and their trade-offs rather than relying on a single traffic-efficiency score.

### 2.3 Safety-constrained decision making

Pedestrian clearance and valid signal transitions are safety requirements. They should not depend solely on a learned reward signal. ARVEXA therefore separates learned optimization from explicit signal and pedestrian safety constraints.

### 2.4 Imperfect sensing

Traffic-state observations may contain missing, noisy, or incorrectly classified information. ARVEXA evaluates controller degradation under controlled sensor-failure and observation-noise scenarios.

### 2.5 Simulation validity

SUMO provides a controlled and reproducible experimental environment, but its usefulness depends on how well its traffic assumptions represent the selected junction. Real camera observations are therefore used to ground and validate traffic demand and vehicle-composition assumptions.

## 3. Research Aim

To design and experimentally evaluate a resilient multi-objective reinforcement-learning framework for adaptive traffic signal control that balances traffic efficiency, pedestrian safety, emergency-vehicle priority, and sensing reliability under heterogeneous urban traffic conditions.

## 4. Research Questions

### RQ1 — Adaptive control
Can a multi-objective RL controller improve traffic-efficiency measures compared with appropriate conventional or rule-based baselines under variable traffic demand?

### RQ2 — Phase and duration
Does dynamically selecting both the next permissible phase and phase duration provide measurable benefits compared with fixed or partially adaptive timing?

### RQ3 — Heterogeneous traffic
Does explicit representation of vehicle types improve control decisions under mixed-traffic conditions compared with an aggregate-only representation?

### RQ4 — Pedestrian safety
How does incorporating pedestrian demand and safety constraints affect vehicle performance and pedestrian service?

### RQ5 — Emergency priority
How can emergency-vehicle priority be incorporated while controlling the effect of priority decisions on other traffic movements?

### RQ6 — Sensor resilience
How does controller performance degrade as traffic-state observations become missing, noisy, or incorrectly classified?

### RQ7 — Multi-objective trade-offs
What trade-offs occur between traffic efficiency, pedestrian service, emergency response, and controller stability?

### RQ8 — Simulation validity
How closely can the calibrated SUMO environment reproduce traffic characteristics observed from real camera footage?

## 5. Research Objectives

| ID | Objective |
|---|---|
| RO-01 | Model heterogeneous traffic using relevant vehicle-type and traffic-state information. |
| RO-02 | Develop adaptive signal phase and duration selection. |
| RO-03 | Incorporate pedestrian demand and explicit safety constraints. |
| RO-04 | Incorporate emergency-vehicle priority into the control framework. |
| RO-05 | Evaluate resilience to missing, noisy, and degraded traffic-state observations. |
| RO-06 | Develop and calibrate a SUMO model of a selected real-world junction. |
| RO-07 | Establish reproducible baseline and multi-scenario evaluation procedures. |
| RO-08 | Validate simulation traffic assumptions using camera-derived traffic observations. |

## 6. Scope

### In scope

- single-junction adaptive signal control as the initial research unit;
- heterogeneous vehicle classes;
- adaptive phase selection;
- adaptive phase duration;
- pedestrian demand and safety constraints;
- emergency-vehicle priority;
- sensor degradation scenarios;
- SUMO-based experimentation;
- quantitative baseline comparison;
- ablation studies;
- vision-based vehicle detection, tracking, and counting;
- real-versus-simulated traffic comparison.

### Out of scope for the core study

- live control of a public-road traffic signal;
- autonomous vehicle control;
- vehicle trajectory control;
- city-wide traffic optimization;
- production traffic-management infrastructure;
- direct online RL training on uncontrolled live traffic;
- replacement of physical traffic-signal hardware.

Network-level multi-agent control is a future extension and is not required for the core single-junction study.

## 7. Research Assumptions

1. A suitable real-world junction and usable traffic observations can be obtained.
2. The junction can be represented sufficiently in SUMO.
3. Traffic demand can be expressed using reproducible scenario configurations.
4. Pedestrian and emergency-vehicle behavior can be represented at an appropriate abstraction level.
5. Camera footage can provide useful vehicle-count and vehicle-class information.
6. The RL controller operates only within a safety-constrained action space.

## 8. Conceptual Research Model

Research flow:

Research literature → research problem → research gap → research questions → objectives → requirements → architecture → SUMO calibration → controller → experiments → camera validation → analysis.

The operational system flow is:

Real junction → camera observations → vision statistics → SUMO calibration → traffic state → multi-objective RL policy → safety-constrained action → signal phase and duration → traffic response → evaluation metrics.

## 9. Expected Research Contribution

ARVEXA does not assume that RL, pedestrian-aware control, emergency priority, sensor robustness, or computer vision are individually novel.

The proposed contribution is the experimentally evaluated integration of:

Heterogeneous traffic + multi-objective RL + pedestrian safety + emergency priority + sensor degradation + real-camera-grounded SUMO evaluation.

The final contribution claim must be based on experimental evidence.

## 10. Success Criteria

The research problem will be considered adequately addressed when:

- the controller produces only valid signal actions;
- baseline and ARVEXA experiments are reproducible;
- traffic-efficiency effects are quantitatively measured;
- pedestrian and emergency objectives are separately reported;
- degraded-sensing experiments quantify robustness;
- ablations identify the contribution of major components;
- SUMO traffic characteristics are compared with real camera observations; and
- each research question can be answered from documented experimental evidence.
