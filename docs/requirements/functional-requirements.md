# Functional Requirements

## State representation

- **FR-01:** The system shall support R1 basic traffic-state representation.
- **FR-02:** The system shall support R2 heterogeneous vehicle-type information.
- **FR-03:** The system shall support R3 pedestrian and emergency information.
- **FR-04:** The system shall support R4 explicit observation-quality/reliability information.
- **FR-05:** Each state representation shall be independently selectable for experiments.

## Observation degradation

- **FR-06:** The system shall preserve a reference true state in simulation.
- **FR-07:** The system shall generate controller observations from the reference state.
- **FR-08:** The system shall support missing observations.
- **FR-09:** The system shall support measurement noise.
- **FR-10:** The system shall support vehicle-type misclassification.
- **FR-11:** The system shall support partial channel failure.
- **FR-12:** Degradation severity shall be configurable.
- **FR-13:** Degradation configuration shall be logged for every experiment.

## Signal control

- **FR-14:** The RL controller shall select a signal phase.
- **FR-15:** The RL controller shall select an allowed duration/action extension.
- **FR-16:** The action space shall respect configured signal constraints.
- **FR-17:** The system shall record every controller action.

## Safety and priority

- **FR-18:** Pedestrian safety rules shall be represented explicitly.
- **FR-19:** Emergency-vehicle priority rules shall be represented explicitly.
- **FR-20:** A deterministic safety/priority layer shall validate or constrain RL actions.
- **FR-21:** Safety violations shall be recorded as evaluation events.

## Simulation

- **FR-22:** The system shall use SUMO for traffic simulation.
- **FR-23:** The controller shall communicate with SUMO through TraCI.
- **FR-24:** The junction geometry and demand configuration shall be version controlled.
- **FR-25:** Vehicle types shall be represented consistently with the selected experiment.

## Evaluation

- **FR-26:** Fixed-time control shall be evaluated.
- **FR-27:** Actuated control shall be evaluated where feasible.
- **FR-28:** A standard vehicle-only RL baseline shall be evaluated.
- **FR-29:** R1–R4 shall be evaluated under matched conditions.
- **FR-30:** All required degradation modes shall be evaluated.
- **FR-31:** Multiple severity levels shall be evaluated.
- **FR-32:** Multiple random seeds shall be used.
- **FR-33:** Efficiency metrics shall be recorded.
- **FR-34:** Pedestrian metrics shall be recorded.
- **FR-35:** Emergency response metrics shall be recorded.
- **FR-36:** Signal stability metrics shall be recorded.
- **FR-37:** Information Benefit shall be computed where applicable.
- **FR-38:** Degradation Ratio shall be computed where applicable.
- **FR-39:** Results shall support representation × reliability comparisons.

## Reliability-aware controller

- **FR-40:** R4 shall expose observation-quality information to the controller.
- **FR-41:** The reliability-aware mechanism shall be independently configurable.
- **FR-42:** The mechanism shall support fallback or reduced reliance on unreliable information where designed.

## Vision validation

- **FR-43:** The vision pipeline shall detect and classify relevant road users.
- **FR-44:** The pipeline shall estimate observation quality.
- **FR-45:** Camera-derived state shall be compared with reference/calibrated simulation state.
- **FR-46:** Camera data shall not be assumed perfect solely because they are real-world observations.
