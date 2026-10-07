# Non-Functional Requirements

## Reproducibility

- Experiments shall use documented seeds.
- Configuration files shall identify state representation, degradation mode, severity, demand, and controller.
- Metrics shall be generated from repeatable evaluation procedures.

## Observation integrity

The true simulated state and controller observation shall remain distinguishable. Degradation must not overwrite the reference state.

## Safety

The RL policy shall not be the sole authority for hard safety constraints. Safety and emergency rules shall remain explicit and testable.

## Experiment integrity

Comparisons shall use matched junction, demand, duration, reward, and action constraints wherever the research question requires a controlled comparison.

## Modularity

State construction, degradation, RL policy, safety validation, simulation, and metrics should remain separable modules.

## Scientific quality

The project shall report negative and null results rather than selecting only successful configurations. Hypotheses shall be stated before the corresponding experiment.

## Privacy

Camera validation should use legally and ethically appropriate footage. Personally identifying information is not required for traffic-state extraction and should not be retained unnecessarily.

## Repository hygiene

Large datasets and generated experiment outputs should not be committed unnecessarily. Configurations, schemas, scripts, and reproducible metadata should be version controlled.
