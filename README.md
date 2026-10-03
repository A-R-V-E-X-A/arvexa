# ARVEXA

**Adaptive Resilient Vehicle–pedestrian eXchange Architecture**

ARVEXA is a research framework for adaptive traffic signal control using multi-objective reinforcement learning.

The system is designed for heterogeneous urban traffic and considers:

- Vehicle counts and vehicle types
- Adaptive signal phase and duration selection
- Pedestrian crossing safety
- Emergency-vehicle priority
- Sensor failure and noisy traffic-state information
- SUMO-based traffic simulation
- Vision-based vehicle detection and counting
- Quantitative evaluation against baseline signal-control strategies

## Project Goal

ARVEXA aims to develop and evaluate an adaptive traffic-signal controller that balances traffic efficiency, pedestrian safety, emergency response, and resilience under mixed-traffic conditions.

## Repository Structure

```text
controller/      Reinforcement-learning controller
simulation/      SUMO networks, routes, scenarios, and configurations
perception/      Vehicle detection, tracking, and counting
evaluation/      Baselines, metrics, and experiments
tests/           Automated tests
docs/            Research, requirements, architecture, experiments, and planning
scripts/         Project utilities
requirements/    Environment and dependency definitions