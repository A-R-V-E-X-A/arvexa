# ARVEXA System Architecture

## 1. Architecture Goal

The ARVEXA architecture separates traffic perception, state construction, reinforcement learning, safety enforcement, simulation, and evaluation.

The architecture is designed so that individual components can be changed and evaluated without rewriting the complete system.

## 2. High-Level Architecture

Real-world junction
→ camera footage
→ vision pipeline
→ traffic statistics
→ SUMO calibration
→ SUMO junction environment
→ state builder
→ multi-objective RL controller
→ safety/action constraint layer
→ signal command
→ SUMO simulation
→ evaluation and metrics.

The real-world validation path is intentionally separate from direct RL control.

## 3. Major Components

### 3.1 Perception Layer

Converts camera footage into structured traffic observations such as vehicle count, class, movement/lane, timestamp, confidence, and tracking identifier where applicable.

The perception layer does not directly control signals.

### 3.2 Calibration/Data Layer

Transforms real observations into traffic-demand and composition information suitable for SUMO configuration.

Responsibilities include cleaning, aggregation, temporal analysis, vehicle-composition estimation, and quality checks.

### 3.3 SUMO Environment

Provides road geometry, traffic demand, vehicle behavior, pedestrians, signal phases, emergency vehicles, simulation time, and traffic-state feedback.

### 3.4 State Builder

Converts raw simulation or perception information into the RL state.

Potential state groups:

| Group | Example information |
|---|---|
| Traffic | counts, queues, waiting, occupancy/density, vehicle composition |
| Pedestrian | demand, waiting, active crossing, clearance |
| Emergency | presence, approach, priority state |
| Sensor | availability, confidence, missingness, observation age |

### 3.5 RL Controller

Consumes the state and selects a candidate signal action. Detailed design is defined in rl-controller.md.

### 3.6 Safety/Action Layer

Validates candidate actions against legal phase transitions, minimum/maximum green, yellow and clearance intervals, pedestrian clearance, and emergency safety requirements.

Only valid actions reach SUMO.

### 3.7 Evaluation Layer

Calculates traffic efficiency, pedestrian service, emergency response, robustness, signal stability, and computational metrics.

## 4. Data Flow

Observation
→ normalization and quality check
→ state construction
→ policy inference
→ candidate action
→ safety validation
→ signal command
→ traffic response
→ metric collection
→ learning or evaluation.

## 5. Training and Evaluation Modes

### Training

SUMO → state → RL policy → safety layer → action → reward → policy update.

### Evaluation

SUMO → state → frozen policy → safety layer → action → metrics.

No policy update should occur during the principal evaluation runs.

## 6. Baseline Architecture

The same scenario should be evaluated using fixed-time, rule-based/actuated, reduced-RL where appropriate, and ARVEXA controllers.

All controllers should use equivalent traffic demand and evaluation metrics.

## 7. Research Data Flow

Camera → vision → traffic statistics → SUMO calibration → controlled RL experiments.

This keeps the core experiments reproducible while grounding the simulation in real traffic.

## 8. Failure Handling

The architecture should handle missing observations, invalid perception values, simulation communication failures, invalid policy actions, and incomplete scenario configuration.

A failure must not silently become a valid-looking measurement.

## 9. Configuration Boundaries

The following should be configurable:

- junction/network;
- traffic demand;
- vehicle composition;
- signal constraints;
- pedestrian demand;
- emergency scenarios;
- sensor-degradation level;
- RL hyperparameters;
- reward configuration;
- experiment seeds.

Source code should not contain hidden experiment assumptions.

## 10. Architecture Principles

1. Safety before optimization.
2. Research traceability.
3. Separation of concerns.
4. Reproducibility.
5. Measured claims.
6. Replaceable algorithms.
7. Real-data grounding.

## 11. Architecture Traceability

| Component | Research objective |
|---|---|
| State Builder | RO-01, RO-05 |
| RL Controller | RO-02 |
| Safety Layer | RO-03 |
| Emergency Logic | RO-04 |
| Degradation Model | RO-05 |
| SUMO Environment | RO-06 |
| Experiment Runner | RO-07 |
| Vision Pipeline | RO-08 |
| Evaluation Layer | RO-09, RO-10 |
