# ARVEXA Research Gap

## 1. Purpose

This document consolidates the research gaps identified from the ARVEXA literature survey and maps them to the proposed research direction.

The survey covered reinforcement-learning traffic signal control, multi-objective control, pedestrian safety, emergency-vehicle priority, sensor failure and missing data, vision-based traffic observation, SUMO/digital-twin validation, and safe or interpretable RL.

The review material reports approximately 141 papers surfaced across its searches and 113 papers curated into its bibliography. It also notes that the adversarial-robustness area was particularly thin and that recent missing-data and robustness research remains active.

## 2. G1 — Integrated Multi-Objective Control

### Existing knowledge

RL and deep RL have been extensively studied for adaptive traffic signal control. Multi-objective approaches also exist, including work combining traffic efficiency with safety and environmental objectives.

### Gap

The reviewed material did not identify a published system combining the complete ARVEXA requirement set in one controller: heterogeneous traffic, pedestrian safety, emergency-vehicle priority, degraded-sensor operation, and multi-objective traffic efficiency.

### ARVEXA response

ARVEXA will formulate the controller as a multi-objective decision problem and evaluate interactions between objectives rather than evaluating each feature independently.

## 3. G2 — Hard Safety Constraints Alongside Learned Optimization

### Existing knowledge

Safe RL and safety-aware control methods are mature in broader control and robotics research. Traffic-signal research also contains pedestrian and safety-aware approaches.

### Gap

A weighted reward can allow a safety-critical objective to be traded away when another objective produces a larger learned reward.

### ARVEXA response

ARVEXA separates learned optimization from explicit signal and pedestrian safety constraints. The policy will select from a constrained action space.

## 4. G3 — Pedestrian Safety + Emergency Priority + Sensor Resilience

### Existing knowledge

Pedestrian-aware RL, emergency-vehicle priority, and sensor-failure robustness are all established research areas.

### Gap

The reviewed material did not identify a unified controller that evaluates all three requirements together with a multi-objective traffic-efficiency controller.

### ARVEXA response

The three requirements will be represented in one architecture and tested in isolated and combined scenarios.

## 5. G4 — Priority Arbitration Under Conflicting Demands

### Existing knowledge

Emergency research often gives emergency traffic explicit priority, while pedestrian research separately considers crossing demand.

### Gap

Limited principled treatment was found for simultaneous conditions such as an emergency vehicle, active pedestrian demand, high traffic, and degraded sensors.

### ARVEXA response

ARVEXA will define explicit safety and priority constraints and evaluate controlled conflict scenarios.

## 6. G5 — End-to-End Robustness to Degraded Observations

### Existing knowledge

Research exists on missing-data reconstruction, fault-tolerant control, observation uncertainty, and robust RL.

### Gap

Much of the robustness literature evaluates reconstruction or controller performance separately. The reviewed work provides less evidence about whether degraded observations preserve downstream multi-objective traffic and safety outcomes.

### ARVEXA response

ARVEXA will inject controlled observation degradation into the traffic-control pipeline and measure traffic, pedestrian, emergency, stability, and degradation metrics.

## 7. G6 — Heterogeneous Mixed-Traffic Context

### Existing knowledge

Many traffic-control studies use standardized simulation traffic and vehicle categories.

### Gap

The survey identifies underrepresentation of heterogeneous mixed traffic characteristic of South and Southeast Asian environments.

### ARVEXA response

The selected junction will be represented using relevant vehicle classes and observed traffic distributions. Results will remain contextual to the studied environment.

## 8. G7 — Real-World Grounding of SUMO Evaluation

### Existing knowledge

SUMO is widely used for traffic-signal RL, while real-world validation is less common.

### Gap

Simulation-to-real validation remains much less common than simulation-only evaluation.

### ARVEXA response

Real camera observations will be used to estimate traffic volume, composition, and temporal demand and to compare those observations with the calibrated SUMO model.

## 9. G8 — Vision Failure Conditions

### Existing knowledge

Vision-based vehicle detection and counting are mature enough for traffic observation, but performance can degrade under occlusion, dense traffic, low light, and viewpoint limitations.

### Gap

Perception uncertainty can affect the simulation calibration used to validate the controller.

### ARVEXA response

The vision pipeline will report quality and known limitations and will not treat camera output as perfect ground truth.

## 10. G9 — Multi-Objective Trade-Off Evidence

### Existing knowledge

Multi-objective RL demonstrates that improving one objective can affect another.

### Gap

A single aggregate score can hide important trade-offs.

### ARVEXA response

ARVEXA will report objective-specific metrics in addition to any aggregate reward.

## 11. Gap-to-Research Mapping

| Gap | Research question | Primary evidence |
|---|---|---|
| G1 | RQ1, RQ7 | Full-controller experiments |
| G2 | RQ4 | Constraint compliance and pedestrian metrics |
| G3 | RQ4, RQ5, RQ6 | Combined scenarios |
| G4 | RQ5, RQ7 | Conflict scenarios |
| G5 | RQ6 | Degradation curves |
| G6 | RQ3 | Vehicle-type ablation |
| G7 | RQ8 | Real-versus-simulated comparison |
| G8 | RQ8 | Detection/counting validation |
| G9 | RQ7 | Multi-metric analysis |

## 12. Novelty Position

ARVEXA should use a conservative novelty position:

> The research investigates an integrated, safety-constrained, multi-objective adaptive traffic-signal-control framework that explicitly evaluates heterogeneous traffic, pedestrian demand, emergency priority, degraded sensing, and real-camera-grounded SUMO validation.

The project should not claim that each individual technique is novel.

Novelty must be rechecked against literature available immediately before final publication.

## 13. Evidence Required to Address the Gap

A gap is not considered addressed merely because a software feature exists.

ARVEXA must provide:

1. controlled baseline comparisons;
2. ablation studies;
3. sensor-degradation experiments;
4. pedestrian and emergency scenarios;
5. heterogeneous-traffic scenarios;
6. reproducible metrics;
7. real-camera-to-SUMO comparison.

The research claim must be reduced if the experiments do not support the expected outcome.
