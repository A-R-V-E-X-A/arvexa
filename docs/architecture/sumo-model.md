# ARVEXA SUMO Model Architecture

## 1. Purpose

The SUMO model provides the controlled experimental environment for ARVEXA.

The goal is to construct a reproducible representation of a selected real-world junction and calibrate important traffic characteristics using observations.

## 2. SUMO Model Components

### Network

- junction geometry;
- lanes;
- connections;
- traffic lights.

### Demand

- routes;
- flows;
- vehicle types;
- temporal variation.

### Pedestrians

- pedestrian demand;
- crossing locations;
- crossing timing.

### Emergency

- emergency vehicle type;
- arrival scenario;
- priority condition.

### Control

- signal phases;
- duration limits;
- controller interface.

## 3. Junction Selection

The final junction should be selected using:

- availability of camera footage or observations;
- representative heterogeneous traffic;
- identifiable signal phases;
- manageable network complexity;
- observable pedestrian activity;
- possibility of emergency scenarios;
- sufficient data for calibration.

The exact junction should not be frozen until these criteria are checked.

## 4. Network Modeling

The SUMO network should reproduce, as far as practical:

- approach geometry;
- number of lanes;
- lane connectivity;
- turning movements;
- stop lines;
- pedestrian crossings;
- traffic-signal locations.

Any abstraction from the real junction must be documented.

## 5. Traffic Demand

Traffic demand should be derived from observations where possible.

Required dimensions include:

- vehicles per time interval;
- approach distribution;
- movement/turning distribution;
- vehicle-type composition;
- temporal variation.

Demand should be represented using reproducible route and flow configuration files.

## 6. Vehicle Types

The initial candidate classes are:

| Class | Role |
|---|---|
| Two-wheeler | Mixed traffic |
| Car | Passenger traffic |
| Auto-rickshaw | Mixed traffic |
| Bus | Large passenger vehicle |
| Truck | Heavy vehicle |
| Emergency | Priority scenario |

The final set should be based on observed traffic.

Relevant parameters may include length, speed, acceleration, deceleration, and vehicle class.

## 7. Pedestrian Model

The pedestrian model should represent crossing location, pedestrian arrival demand, waiting behavior, crossing duration/clearance, and signal interaction.

The model should be sufficiently detailed for evaluation without pretending to reproduce every individual pedestrian behavior.

## 8. Emergency-Vehicle Model

Emergency vehicles should have a distinct type, controlled arrival time, approach, movement, and priority state.

At minimum evaluate:

1. emergency vehicle during normal traffic;
2. emergency vehicle during congestion.

Multiple simultaneous emergency vehicles may be treated as an extension.

## 9. Signal Model

The signal model must define:

- legal phases;
- phase sequence;
- minimum green;
- maximum green;
- yellow;
- clearance/all-red intervals where applicable;
- pedestrian phases;
- emergency-priority transitions.

The RL controller shall operate through this defined interface.

## 10. Calibration Process

Calibration should proceed in stages:

1. geometry;
2. demand;
3. vehicle composition;
4. movement distribution;
5. behavioral parameters;
6. validation.

Behavioral parameters should be changed only where necessary to reproduce observed characteristics.

## 11. Calibration Metrics

Potential metrics:

- traffic volume;
- vehicle-class distribution;
- queue length;
- travel time;
- waiting time;
- arrival-rate profile.

The final metric set depends on what can be reliably measured from the real footage.

## 12. Scenario Generator

Scenario configuration should support:

- traffic level;
- vehicle composition;
- pedestrian level;
- emergency event;
- sensor failure rate;
- sensor noise;
- random seed;
- signal controller.

Changing a scenario should not require editing controller source code.

## 13. Sensor-Degradation Simulation

The simulator should produce the ideal state and then transform observations through an observation model:

True SUMO state → observation model → ideal/missing/noisy/misclassified state → RL controller.

This keeps the underlying traffic simulation consistent when a simulated sensor fails.

## 14. Experiment Separation

Training and evaluation configurations should be separate.

Recommended repository organization:

simulation/sumo/network/
simulation/sumo/routes/
simulation/sumo/scenarios/
simulation/sumo/config/

Scenario files define conditions; controller source defines decision logic.

## 15. Reproducibility

Each experiment should record:

- SUMO version;
- network version;
- route-file version;
- scenario configuration;
- controller version;
- random seed;
- simulation duration;
- calibration version.

## 16. Model Validation Principle

Calibration does not mean that the SUMO model is identical to reality.

The research claim should be:

> The SUMO environment reproduces selected measurable characteristics of the chosen junction within documented error or tolerance.

The tolerance and validation procedure must be defined before final results are interpreted.

## 17. SUMO Outputs

Where available, collect:

- vehicle waiting time;
- travel time;
- queue length;
- throughput;
- vehicle counts;
- phase information;
- pedestrian state;
- emergency response;
- simulation time.

## 18. SUMO-to-Controller Interface

SUMO → state adapter → state schema → RL controller → action schema → signal adapter → SUMO.

This makes the controller testable independently of SUMO.

## 19. Future Extension

The architecture can later support multiple intersections, multi-agent RL, corridor coordination, and richer digital-twin functionality. These are not required for the core ARVEXA research objectives.
