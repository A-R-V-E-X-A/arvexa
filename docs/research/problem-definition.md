# Problem Definition

## Problem

Adaptive traffic-signal controllers depend on the traffic state supplied to the decision-making system. In heterogeneous urban traffic, increasingly rich representations can include vehicle counts, queues, vehicle classes, pedestrian state, emergency state, and other contextual information.

The difficulty is that this information is not always reliable. Sensors and vision systems can produce missing observations, noisy measurements, incorrect vehicle classifications, or partial failures.

The unresolved research question addressed by ARVEXA is:

> **When observation reliability varies, does adding richer traffic-state information continue to improve adaptive signal-control performance, or can additional unreliable information reduce control quality?**

## Variables

### Independent variables

- State representation level: R1–R4.
- Observation degradation mode.
- Degradation severity.

### Controlled variables

- Junction geometry.
- Traffic demand.
- Vehicle mix.
- Simulation duration.
- Random seeds.
- Signal action constraints.
- Reward definition.
- Evaluation procedure.

### Dependent variables

- Traffic efficiency.
- Queue and delay measures.
- Throughput.
- Pedestrian safety/timeliness.
- Emergency response.
- Signal stability.
- Overall research utility.

## Observation degradation

The study models missing data, measurement noise, semantic misclassification, and partial observation-channel failure.

The true SUMO state is retained separately from the degraded controller observation so that degradation is measurable and reproducible.

## Role of safety and emergency priority

Pedestrian and emergency information create important decision contexts but are not claimed as standalone novelty. Their role is to test whether the information–reliability relationship remains acceptable under safety-critical and priority-sensitive conditions.

## Expected contribution

ARVEXA aims to determine whether richer traffic-state representations have a reliability threshold beyond which their additional information is no longer beneficial, and whether explicit reliability information can improve robustness.

The result may show consistently positive benefit, diminishing benefit, a crossover from benefit to harm, or no meaningful advantage. Any of these outcomes is valuable if established through controlled experiments.
