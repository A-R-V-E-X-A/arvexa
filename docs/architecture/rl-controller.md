# ARVEXA RL Controller Architecture

## 1. Purpose

This document defines the research architecture of the ARVEXA reinforcement-learning controller.

The exact RL algorithm is intentionally not frozen until the state/action formulation, baseline implementation, and computational feasibility are evaluated.

## 2. RL Loop

State at time t
→ policy
→ candidate action
→ safety/action layer
→ valid signal action
→ SUMO transition
→ next state
→ objective measurements
→ reward/learning signal
→ policy update.

## 3. State Representation

### Traffic state

Potential features:

- vehicle count by approach;
- vehicle count by movement;
- queue length;
- waiting time;
- occupancy/density;
- current phase;
- elapsed phase time;
- vehicle-type distribution.

### Pedestrian state

Potential features:

- pedestrian demand;
- waiting pedestrians;
- active crossing state;
- clearance state;
- pedestrian waiting time.

### Emergency state

Potential features:

- emergency vehicle presence;
- approach;
- estimated queue ahead;
- priority activation;
- emergency waiting time.

### Sensor state

Potential features:

- observation availability;
- missingness indicators;
- confidence;
- degraded sensor channels;
- observation age.

The final state shall contain only variables that can be generated consistently in training and evaluation.

## 4. State Design Principle

The controller should avoid using information that would be unavailable during intended real-world observation.

If a variable can be measured perfectly in SUMO but cannot be estimated from the planned perception pipeline, it should be replaced with a measurable proxy, explicitly marked simulation-only, or excluded.

## 5. Action Space

The primary action is:

phase + duration.

The phase must be a legal next phase.

The duration may be represented as discrete duration classes or a bounded continuous value. A discrete duration formulation is preferred for the first reproducible implementation because it simplifies safety constraints and comparison.

The final representation will be selected after considering the junction phase plan and training stability.

## 6. Action Constraints

The RL policy shall not directly bypass:

- minimum green;
- maximum green;
- yellow interval;
- clearance interval;
- legal phase transitions;
- pedestrian clearance;
- emergency-transition safety requirements.

The action layer performs candidate action → constraint check → valid action.

If a candidate is invalid, the system shall use a documented masking, clipping, or safe-fallback mechanism.

## 7. Reward Architecture

Conceptually:

Reward = traffic-efficiency component + pedestrian component + emergency component + stability component + robustness component.

Potential traffic terms include waiting-time reduction, queue reduction, and throughput.

Potential pedestrian terms include reduced pedestrian waiting and valid service opportunities.

Potential emergency terms include reduced emergency waiting and response delay.

Potential stability terms include penalties for excessive switching and undesirable short green periods.

Robustness should primarily be evaluated through controlled degraded-observation scenarios and should not be reduced to rewarding healthy sensors.

## 8. Reward Design Rules

1. Every reward term must correspond to a research objective or control requirement.
2. Reward terms must use documented normalization/scaling.
3. Weights must be documented.
4. Weight sensitivity should be evaluated where feasible.
5. Reward must not be the only safety mechanism.
6. Final claims must use external evaluation metrics rather than reward alone.

## 9. Multi-Objective Strategy

The first implementation may use a normalized weighted objective:

R = sum of weighted normalized objective terms.

A weighted sum does not prove Pareto optimality. If time permits, later experiments may compare fixed weights with dynamically adjusted or vector-valued approaches.

## 10. Training Scenarios

Training should expose the controller to variation in:

- traffic demand;
- vehicle composition;
- pedestrian demand;
- emergency events;
- observation quality.

The training distribution should not simply reproduce one traffic trace.

## 11. Evaluation Scenarios

| ID | Scenario |
|---|---|
| E1 | Normal demand |
| E2 | Low demand |
| E3 | High demand |
| E4 | Heterogeneous traffic |
| E5 | Pedestrian surge |
| E6 | Emergency vehicle |
| E7 | Emergency during congestion |
| E8 | Sensor degradation |
| E9 | Demand shift |
| E10 | Combined stress scenario |

The combined scenario complements, rather than replaces, controlled single-factor experiments.

## 12. Baselines and Ablations

Baselines:

- fixed-time;
- rule-based/actuated;
- reduced RL where appropriate;
- full ARVEXA.

Ablations:

- no vehicle-type information;
- no pedestrian objective;
- no emergency component;
- no sensor-health information;
- fixed duration;
- phase-only adaptive control.

## 13. Training Reproducibility

Each RL experiment shall record:

- algorithm;
- network architecture;
- learning rate;
- discount factor;
- exploration settings;
- batch size;
- replay settings where applicable;
- reward weights;
- state version;
- action version;
- random seed;
- scenario configuration;
- training duration.

## 14. Evaluation Metrics

### Traffic

Mean waiting time, mean travel time, queue length, maximum queue, throughput, and stops.

### Pedestrians

Waiting time, service opportunity, and safety-constraint violations.

### Emergency

Waiting time and response/travel time.

### Robustness

Degradation under missing data, degradation under noise, and recovery after restoration.

### Controller

Phase changes, duration distribution, and inference latency.

## 15. Controller Pseudocode

1. Initialize environment and policy.
2. Initialize safety constraints.
3. Reset a scenario.
4. Build the current state.
5. Produce a candidate policy action.
6. Apply the safety filter.
7. Send the valid action to SUMO.
8. Obtain the next state and observations.
9. Calculate objective reward.
10. Update the policy during training.
11. Repeat until termination.
12. Save the model and configuration.

## 16. Algorithm Selection Decision

The exact algorithm should be selected after:

1. action-space finalization;
2. state-space finalization;
3. baseline implementation;
4. small-scale training tests;
5. computational feasibility assessment.

Selection must be justified by action-space compatibility, training stability, reproducibility, computational feasibility, and suitability for the single-junction problem.

## 17. Safety Boundary

The RL controller is not the authority for physical signal safety.

RL policy → candidate decision → safety/constraint layer → signal controller.

This is a fundamental ARVEXA design principle.
