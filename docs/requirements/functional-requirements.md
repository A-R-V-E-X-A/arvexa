# ARVEXA Functional Requirements

## 1. Purpose

These requirements convert the research objectives into testable system capabilities.

## 2. Traffic-State Requirements

### FR-01 — Vehicle Count
The system shall represent vehicle counts for relevant traffic movements or lanes.

**Traceability:** RO-01, RO-02

### FR-02 — Vehicle Classification
The system shall support configurable vehicle classes relevant to the selected junction. Initial candidates are two-wheeler, car, auto-rickshaw, bus, truck, and emergency vehicle.

The final class set shall be based on observed traffic and perception quality.

**Traceability:** RO-01, RO-08

### FR-03 — Queue Representation
The system shall provide a queue or congestion representation sufficient for controller decisions and evaluation.

### FR-04 — Waiting-Time Representation
The system shall provide traffic waiting information or an equivalent state variable suitable for optimization.

### FR-05 — Sensor Health
The state pipeline shall represent whether required observations are available, degraded, or missing.

**Traceability:** RO-05

## 3. Signal-Control Requirements

### FR-06 — Valid Phase Enumeration
The system shall define valid signal phases for the selected junction.

### FR-07 — Phase Selection
The controller shall select the next permissible phase.

**Traceability:** RO-02

### FR-08 — Duration Selection
The controller shall select an allowed duration or duration class for the selected phase.

**Traceability:** RO-02

### FR-09 — Minimum/Maximum Green
The controller shall enforce configured minimum and maximum green durations.

### FR-10 — Yellow and Clearance
The signal controller shall enforce configured yellow and clearance intervals.

### FR-11 — Legal Phase Transitions
The action layer shall prevent transitions that violate configured phase-transition rules.

**Traceability:** RO-03

## 4. Pedestrian Requirements

### FR-12 — Pedestrian Demand
The system shall represent pedestrian crossing demand.

### FR-13 — Pedestrian Service
The controller shall provide valid pedestrian service opportunities according to the modeled signal plan.

### FR-14 — Pedestrian Clearance
The system shall prevent vehicle-serving actions that violate an active pedestrian clearance constraint.

### FR-15 — Pedestrian Metrics
The evaluation system shall measure pedestrian waiting/service performance.

## 5. Emergency-Vehicle Requirements

### FR-16 — Emergency Detection Input
The traffic state shall support emergency-vehicle presence and approach information.

### FR-17 — Priority State
The controller shall represent whether emergency priority is active.

### FR-18 — Emergency Priority Decision
The controller shall be able to allocate signal service to an emergency approach subject to safety constraints.

### FR-19 — Emergency Metrics
The evaluation system shall measure emergency waiting/travel response.

### FR-20 — Normal-Traffic Impact
The evaluation system shall separately report the effect of emergency priority on other traffic movements.

## 6. Sensor-Degradation Requirements

### FR-21 — Missing Observation Injection
The simulation pipeline shall support controlled removal of selected traffic observations.

### FR-22 — Noise Injection
The evaluation pipeline shall support configurable observation noise.

### FR-23 — Classification Error
The evaluation pipeline shall support controlled vehicle-classification errors where technically appropriate.

### FR-24 — Partial Failure
The system shall support scenarios in which a subset of observation channels becomes unavailable.

### FR-25 — Degradation Measurement
The evaluation system shall compare degraded-sensing performance with ideal-sensing conditions.

**Traceability:** RO-05

## 7. SUMO Requirements

### FR-26 — Junction Network
The system shall represent the selected real-world junction in SUMO.

### FR-27 — Traffic Routes
The system shall provide reproducible traffic routes and demand configurations.

### FR-28 — Vehicle Types
SUMO shall represent the relevant vehicle classes.

### FR-29 — Pedestrian Model
The simulation shall provide the minimum pedestrian representation required by research scenarios.

### FR-30 — Emergency Scenario
The simulation shall support reproducible emergency-vehicle scenarios.

### FR-31 — Signal Interface
The controller shall communicate with SUMO through a defined control interface.

### FR-32 — Scenario Configuration
Traffic demand, vehicle composition, pedestrian demand, emergency conditions, and sensor degradation shall be configurable without changing controller source code.

**Traceability:** RO-06, RO-07

## 8. RL Requirements

### FR-33 — State Construction
The controller shall construct a documented state representation from available observations.

### FR-34 — Action Construction
The controller shall map a policy output to a valid signal action.

### FR-35 — Reward Calculation
The system shall calculate documented objective components.

### FR-36 — Safety Filtering
The system shall apply safety constraints before a learned action affects the simulated signal.

### FR-37 — Model Persistence
The training system shall save model parameters and configuration required for evaluation.

### FR-38 — Deterministic Evaluation
The evaluation system shall support fixed random seeds where controlled stochastic evaluation is required.

## 9. Baseline Requirements

### FR-39 — Fixed-Time Baseline
The system shall support a fixed-time baseline.

### FR-40 — Rule-Based Baseline
The system shall support an appropriate demand-responsive or actuated/rule-based baseline.

### FR-41 — Reduced RL Baseline
The system should support a reduced RL controller for ablation, such as an efficiency-focused controller.

## 10. Evaluation Requirements

### FR-42 — Traffic Metrics
The system shall calculate at least mean waiting time, mean travel time where available, queue length, throughput, and number of stops where measurable.

### FR-43 — Pedestrian Metrics
The system shall calculate pedestrian waiting time, service/crossing opportunity, and safety-constraint violations.

### FR-44 — Emergency Metrics
The system shall calculate emergency waiting time and emergency travel or response time where available.

### FR-45 — Robustness Metrics
The system shall calculate performance degradation relative to ideal sensing.

### FR-46 — Repeated Runs
The experiment runner shall support multiple runs with controlled seeds.

### FR-47 — Result Metadata
Each result shall record scenario, controller, configuration, seed, metrics, and software/model version.

**Traceability:** RO-07

## 11. Vision Requirements

### FR-48 — Video Input
The perception pipeline shall accept recorded camera footage in supported formats.

### FR-49 — Vehicle Detection
The pipeline shall detect relevant vehicles.

### FR-50 — Vehicle Classification
The pipeline should classify vehicles into categories required for calibration.

### FR-51 — Tracking
The pipeline should associate detections across frames sufficiently to avoid double counting where tracking is used.

### FR-52 — Counting
The pipeline shall produce time-indexed traffic counts.

### FR-53 — Validation
The pipeline shall provide a mechanism for evaluating detection/counting quality on a reviewed sample.

**Traceability:** RO-08

## 12. Ablation Requirements

### FR-54 — Vehicle-Type Ablation
The system shall support comparison with and without vehicle-type information.

### FR-55 — Pedestrian Ablation
The system should support comparison with and without the pedestrian objective where the resulting controller remains safe.

### FR-56 — Emergency Ablation
The system should support comparison with and without emergency-priority logic.

### FR-57 — Sensor-Resilience Ablation
The system should support comparison between controllers developed/evaluated under ideal sensing and controllers incorporating degraded-sensing handling.

**Traceability:** RO-10

## 13. Acceptance Principle

A functional requirement is complete only when implementation, test, and evidence are available and traceable to its research objective.
