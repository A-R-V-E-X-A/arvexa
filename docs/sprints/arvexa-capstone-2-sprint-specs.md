# ARVEXA — Capstone-2 Sprint & Slice Specification

> **Phase 2 of 3 | ARVEXA Core Implementation**
> Sprints 5–8 | Slices C2-S01 to C2-S36

---

## Phase Overview

| Field | Value |
|---|---|
| **Capstone** | 2 |
| **Theme** | ARVEXA Core Implementation |
| **Sprint Range** | SPR-05 — SPR-08 |
| **Slice Range** | C2-S01 — C2-S36 |
| **Primary Deliverable** | Working ARVEXA RL controller evaluated in SUMO against baselines |

## Phase Entry Criteria

- All Capstone-1 exit criteria satisfied
- SUMO network and baseline controller are runnable and reproducible
- Architecture frozen: state representation, action space, reward architecture, constraint layer

## Phase Exit Criteria

- [ ] SUMO environment wrapper connects to TraCI and steps correctly
- [ ] Unified state builder produces a normalised observation from all configured state channels
- [ ] ARVEXA RL controller trains to convergence on at least the normal-demand scenario
- [ ] Multi-objective reward (≥ 5 components) is implemented and configurable
- [ ] Safety constraint layer is active and cannot be bypassed by the RL policy
- [ ] Emergency priority arbitration and pedestrian conflict handling are implemented
- [ ] ARVEXA outperforms fixed-time baseline on at least one traffic-efficiency metric in the normal scenario
- [ ] Sensor-resilience experiments cover all 4 degradation modes
- [ ] Statistical results are generated across ≥ 5 random seeds
- [ ] Ablation study removes each reward component in isolation

---

## Sprint 5 — SUMO & Traffic-State Pipeline

| Field | Value |
|---|---|
| **Sprint ID** | SPR-05 |
| **Capstone** | 2 |
| **Goal** | Build the environment layer that the RL controller will observe and interact with: SUMO wrapper, all state channels, and the unified state builder |
| **Entry Criteria** | Capstone-1 exit satisfied; SUMO network and demand files ready |
| **Exit Criteria** | `step()` returns a valid normalised state vector; all state channels are individually unit-tested |

---

### C2-S01 — SUMO Environment Wrapper

**Objective**
Implement a Python class that manages the SUMO process lifecycle (start, step, reset, close) via TraCI, providing a clean interface to the rest of the ARVEXA system.

**Inputs**
- `sumo/network/arvexa-junction.net.xml` (C1-S22)
- `sumo/demand/` files (C1-S23 to C1-S26)
- SUMO architecture spec (C1-S18)

**Outputs**
- `src/environment/sumo_env.py`
- Unit tests: `tests/test_sumo_env.py`

**Acceptance Criteria**
- [ ] `start()` launches a SUMO process via TraCI without error
- [ ] `step(action)` advances the simulation by one decision step and returns raw TraCI data
- [ ] `reset()` terminates and restarts the simulation with the configured seed
- [ ] `close()` terminates SUMO cleanly
- [ ] All 4 methods are unit-tested with a mock or live SUMO call

**Dependencies** — C1-S22, C1-S23, C1-S18

---

### C2-S02 — Vehicle Detection & State Extraction

**Objective**
Extract per-vehicle state data (position, speed, waiting time, lane) from the SUMO simulation using TraCI subscriptions for all vehicles within the junction influence area.

**Inputs**
- `src/environment/sumo_env.py` (C2-S01)
- State representation spec (C1-S14)

**Outputs**
- `src/environment/vehicle_detector.py`
- Vehicle state schema documentation (fields, types, units)

**Acceptance Criteria**
- [ ] Vehicle positions, speeds, and waiting times are retrieved via TraCI subscription (not polling)
- [ ] Detection is bounded to the junction influence area (configurable radius or lane list)
- [ ] Output is a dictionary keyed by vehicle ID
- [ ] Unit test validates detection output against a known SUMO scenario

**Dependencies** — C2-S01, C1-S14

---

### C2-S03 — Vehicle Classification / Type State

**Objective**
Extract the vehicle type category (car, truck, motorcycle, emergency) for each detected vehicle and include it as a state channel.

**Inputs**
- `src/environment/vehicle_detector.py` (C2-S02)
- `sumo/demand/vehicle-types.add.xml` (C1-S24)

**Outputs**
- Vehicle type field added to vehicle detector output
- Type-to-category mapping config

**Acceptance Criteria**
- [ ] Each detected vehicle carries a type category field
- [ ] Emergency vehicle type is reliably distinguishable from non-emergency types
- [ ] Mapping from SUMO vType to ARVEXA category is configurable (not hard-coded)
- [ ] Unit test covers each vehicle type category

**Dependencies** — C2-S02, C1-S24

---

### C2-S04 — Queue Estimation

**Objective**
Compute queue length (number of stopped or near-stopped vehicles) per lane and per approach from the vehicle detection output.

**Inputs**
- `src/environment/vehicle_detector.py` (C2-S02)
- State representation spec (C1-S14)

**Outputs**
- `src/environment/queue_estimator.py`
- Queue state: per-lane vehicle count at speed ≤ threshold

**Acceptance Criteria**
- [ ] Queue is computed per lane and aggregated per approach
- [ ] Stopped-vehicle threshold (speed ≤ X m/s) is configurable
- [ ] Output matches the queue state element specification in C1-S14
- [ ] Unit test validates queue count against a known scenario

**Dependencies** — C2-S02, C1-S14

---

### C2-S05 — Waiting-Time State

**Objective**
Extract and aggregate cumulative waiting time per lane and per approach from the SUMO vehicle data.

**Inputs**
- `src/environment/vehicle_detector.py` (C2-S02)
- State representation spec (C1-S14)

**Outputs**
- Waiting-time aggregation module (may be part of `queue_estimator.py` or separate)
- Waiting-time state elements: per-lane and per-approach totals

**Acceptance Criteria**
- [ ] Cumulative waiting time is summed across all detected vehicles per lane
- [ ] Output matches waiting-time state element specification in C1-S14
- [ ] Reset correctly zeroes waiting-time accumulators between episodes
- [ ] Unit test validates against a known stopped-vehicle scenario

**Dependencies** — C2-S02, C1-S14

---

### C2-S06 — Pedestrian State

**Objective**
Extract pedestrian presence, count, and waiting time at each crossing from SUMO and include them as state elements.

**Inputs**
- `src/environment/sumo_env.py` (C2-S01)
- Pedestrian model (C1-S25), state representation spec (C1-S14)

**Outputs**
- Pedestrian state channel in the detector/state pipeline
- Per-crossing pedestrian count and waiting time

**Acceptance Criteria**
- [ ] Pedestrian presence is detected per crossing via TraCI
- [ ] Pedestrian count and maximum waiting time are available as state elements
- [ ] Output matches pedestrian state element specification in C1-S14
- [ ] Unit test uses a scenario with pedestrians at a crossing

**Dependencies** — C2-S01, C1-S25, C1-S14

---

### C2-S07 — Emergency-Vehicle State

**Objective**
Detect and represent emergency vehicle presence, approach direction, and estimated time to junction in the state vector.

**Inputs**
- `src/environment/vehicle_detector.py` (C2-S02) with type classification (C2-S03)
- Emergency-vehicle model (C1-S26), state representation spec (C1-S14)

**Outputs**
- Emergency vehicle state channel: presence flag, approach lane, estimated time to junction

**Acceptance Criteria**
- [ ] Emergency vehicle is detected by type category (from C2-S03)
- [ ] Presence flag, approach lane ID, and distance/time to junction are populated
- [ ] Output matches emergency vehicle state element specification in C1-S14
- [ ] Unit test uses a scenario with an approaching emergency vehicle

**Dependencies** — C2-S02, C2-S03, C1-S26, C1-S14

---

### C2-S08 — Sensor-Health State

**Objective**
Generate a sensor availability/health indicator per state channel, reflecting whether that channel's data is currently reliable. This enables the controller to adapt to degraded inputs.

**Inputs**
- Sensor degradation model spec (C1-S20)
- State representation spec (C1-S14)

**Outputs**
- Sensor-health channel: per-state-element availability indicator (binary or continuous confidence)
- `src/environment/sensor_health.py`

**Acceptance Criteria**
- [ ] Health indicator exists for each sensor-dependent state element
- [ ] Health is set to 0 when a degradation mode drops that channel
- [ ] Health channel is injected into the unified state vector (C2-S09)
- [ ] Degradation modes from C1-S20 are all exercisable via config

**Dependencies** — C1-S20, C1-S14

---

### C2-S09 — Unified State Builder

**Objective**
Combine all state channels (vehicle queue, waiting time, pedestrian, emergency, sensor health) into a single normalised state vector ready for the RL controller.

**Inputs**
- C2-S04 (queue), C2-S05 (waiting time), C2-S06 (pedestrian), C2-S07 (emergency), C2-S08 (sensor health)
- State representation spec (C1-S14)

**Outputs**
- `src/environment/state_builder.py`
- Normalised numpy state vector matching the specification in C1-S14
- State schema validation test

**Acceptance Criteria**
- [ ] Output vector dimension matches the state spec in C1-S14 exactly
- [ ] All elements are normalised to a consistent range (e.g., [0, 1] or [-1, 1])
- [ ] Degradation mode injection is tested: degraded channel produces correct health indicator
- [ ] Schema validation raises an error if any element is out of range
- [ ] Integration test confirms end-to-end: SUMO step → state builder → vector

**Dependencies** — C2-S04, C2-S05, C2-S06, C2-S07, C2-S08, C1-S14

---

## Sprint 6 — RL Controller

| Field | Value |
|---|---|
| **Sprint ID** | SPR-06 |
| **Capstone** | 2 |
| **Goal** | Implement the Gym-compatible RL environment interface, action space, reward, training pipeline, and deterministic evaluation mode |
| **Entry Criteria** | Sprint 5 complete; unified state builder produces a valid normalised vector |
| **Exit Criteria** | ARVEXA trains to convergence on the normal-demand scenario; trained model can be loaded and evaluated deterministically |

---

### C2-S10 — RL Environment Interface

**Objective**
Implement the Gym-compatible environment class that wraps the SUMO wrapper and state builder, exposing the standard `reset()`, `step()`, `render()` interface to the RL training loop.

**Inputs**
- `src/environment/sumo_env.py` (C2-S01)
- `src/environment/state_builder.py` (C2-S09)

**Outputs**
- `src/environment/arvexa_env.py`
- Passes `gym.utils.env_checker.check_env()` or equivalent

**Acceptance Criteria**
- [ ] `reset()` returns an initial observation matching the state spec
- [ ] `step(action)` returns `(observation, reward, terminated, truncated, info)` tuple
- [ ] `render()` optionally renders the SUMO GUI (not required for training)
- [ ] Environment passes a standard Gym environment checker
- [ ] Seeding is supported via `reset(seed=N)`

**Dependencies** — C2-S01, C2-S09

---

### C2-S11 — State-Space Implementation

**Objective**
Implement the `observation_space` property in the Gym environment, matching the state vector specification from C1-S14.

**Inputs**
- `src/environment/arvexa_env.py` (C2-S10)
- State representation spec (C1-S14)

**Outputs**
- `observation_space` defined as `gym.spaces.Box` with correct bounds and dtype

**Acceptance Criteria**
- [ ] `observation_space` shape matches the state vector dimension from C1-S14
- [ ] Lower and upper bounds per element match the state spec
- [ ] Sample from observation space is always a valid state structure
- [ ] Unit test validates space shape and bounds

**Dependencies** — C2-S10, C1-S14

---

### C2-S12 — Phase Action Implementation

**Objective**
Implement the discrete phase selection dimension of the action space in the Gym environment, matching the action space specification from C1-S15.

**Inputs**
- `src/environment/arvexa_env.py` (C2-S10)
- Action space spec (C1-S15)

**Outputs**
- Phase component of `action_space` in `arvexa_env.py`

**Acceptance Criteria**
- [ ] `action_space` includes a discrete phase selection component
- [ ] Number of valid phases matches the action space spec from C1-S15
- [ ] Sampling from action space always returns a valid phase index
- [ ] Unit test covers each valid phase selection

**Dependencies** — C2-S10, C1-S15

---

### C2-S13 — Duration Action Implementation

**Objective**
Implement the green duration selection dimension of the action space, either as a discrete set of durations or a bounded continuous value.

**Inputs**
- `src/environment/arvexa_env.py` (C2-S10)
- Action space spec (C1-S15), safety requirements (C1-S08)

**Outputs**
- Duration component of `action_space` in `arvexa_env.py`

**Acceptance Criteria**
- [ ] Duration range is consistent with minimum and maximum green time from C1-S08
- [ ] Action type (discrete or continuous) is configurable
- [ ] Combined action space (phase + duration) is correctly defined
- [ ] Unit test confirms bound enforcement

**Dependencies** — C2-S10, C2-S12, C1-S15, C1-S08

---

### C2-S14 — Action Validity Constraints

**Objective**
Implement the constraint checker that intercepts RL policy outputs before they reach the SUMO actuator, masking or clipping any action that would violate a safety requirement.

**Inputs**
- `src/environment/arvexa_env.py` (C2-S10)
- Safety constraint layer spec (C1-S17), safety requirements (C1-S08)

**Outputs**
- `src/environment/action_validator.py`
- Modified `step()` in `arvexa_env.py` that calls the validator before execution

**Acceptance Criteria**
- [ ] Validator rejects (clips or masks) any phase duration below minimum green time
- [ ] Validator rejects any phase duration above maximum green time
- [ ] Validator prevents selection of a phase that is currently in intergreen
- [ ] All constraint violations are logged with a reason code
- [ ] Unit test demonstrates each constraint is enforced

**Dependencies** — C2-S10, C1-S17, C1-S08

---

### C2-S15 — Reward Implementation

**Objective**
Implement the reward function skeleton, computing a scalar reward from the current environment state after each step. Individual objective components are placeholders here; full components are added in Sprint 7.

**Inputs**
- `src/environment/arvexa_env.py` (C2-S10)
- Reward architecture spec (C1-S16)

**Outputs**
- `src/environment/reward.py`
- Reward component registry (dict of component_name → compute_fn)

**Acceptance Criteria**
- [ ] `compute_reward(state, action, info)` returns a scalar float
- [ ] Reward components are individually togglable via config
- [ ] Each component's contribution is logged separately in the `info` dict
- [ ] Unit test confirms reward is a finite float for a valid state/action pair

**Dependencies** — C2-S10, C1-S16

---

### C2-S16 — Training Pipeline

**Objective**
Set up the RL training loop, integrating the chosen algorithm with the ARVEXA environment. The algorithm choice is finalised here based on state/action/baseline feasibility from Sprint 5.

**Inputs**
- `src/environment/arvexa_env.py` (C2-S10)
- `src/environment/reward.py` (C2-S15)
- `config/experiment-defaults.yaml` (C1-S32)

**Outputs**
- `src/training/train.py`
- Training configuration (algorithm hyperparameters, episode length, max steps)

**Acceptance Criteria**
- [ ] Training script runs to completion on the normal-demand scenario
- [ ] Training progress is logged (episode reward, episode length, per-component reward)
- [ ] Algorithm and all hyperparameters are specified in a config file
- [ ] Training can be interrupted and resumed from the latest checkpoint

**Dependencies** — C2-S10, C2-S15, C1-S32

---

### C2-S17 — Model Checkpointing

**Objective**
Implement saving and loading of trained model checkpoints, including the model weights, training step, and associated config.

**Inputs**
- `src/training/train.py` (C2-S16)

**Outputs**
- Checkpoint save/load logic in `src/training/`
- `checkpoints/` directory structure with run-ID subdirectories

**Acceptance Criteria**
- [ ] Checkpoints are saved at configurable intervals (e.g., every N steps)
- [ ] Best checkpoint (by evaluation metric) is saved separately
- [ ] Loading a checkpoint and continuing training from it produces consistent behaviour
- [ ] Checkpoint includes: model weights, optimizer state, step count, config hash

**Dependencies** — C2-S16

---

### C2-S18 — Deterministic Evaluation Mode

**Objective**
Implement a script that loads a trained checkpoint and evaluates it deterministically (no exploration) across a specified set of scenarios, logging all metrics.

**Inputs**
- `src/training/train.py` (C2-S16), checkpoint system (C2-S17)
- Evaluation metrics spec (C1-S31)

**Outputs**
- `src/evaluation/evaluate.py`
- Evaluation output: per-episode metrics CSV, summary statistics

**Acceptance Criteria**
- [ ] Evaluation uses argmax / deterministic policy (no stochastic sampling)
- [ ] Running the same evaluation twice with the same checkpoint and seed produces identical results
- [ ] All metrics from C1-S31 are computed and logged
- [ ] Output is saved with run-ID tagging (C1-S32)

**Dependencies** — C2-S17, C1-S31, C1-S32

---

## Sprint 7 — Multi-Objective & Safety

| Field | Value |
|---|---|
| **Sprint ID** | SPR-07 |
| **Capstone** | 2 |
| **Goal** | Implement the multi-objective reward components and the safety/priority constraint layer that distinguish ARVEXA from a basic traffic RL controller |
| **Entry Criteria** | Sprint 6 complete; basic RL training loop is functional |
| **Exit Criteria** | All 5+ reward components active; safety constraints block all unsafe actions; emergency preemption and pedestrian protection are tested |

---

### C2-S19 — Traffic-Efficiency Objective

**Objective**
Implement the traffic efficiency reward component: a function of queue length, average waiting time, and/or intersection throughput that rewards the controller for reducing vehicle delay.

**Inputs**
- `src/environment/reward.py` (C2-S15)
- Queue estimator (C2-S04), waiting-time state (C2-S05)

**Outputs**
- `traffic_efficiency` component in `src/environment/reward.py`

**Acceptance Criteria**
- [ ] Reward decreases monotonically as total queue or waiting time increases
- [ ] Component formula matches the reward architecture spec (C1-S16)
- [ ] Component is logged separately in the `info` dict per step
- [ ] Unit test confirms correct sign and magnitude for a known queue scenario

**Dependencies** — C2-S15, C2-S04, C2-S05

---

### C2-S20 — Pedestrian-Safety Objective

**Objective**
Implement the pedestrian safety reward component: penalises excessive pedestrian waiting time and rewards timely pedestrian phase allocation.

**Inputs**
- `src/environment/reward.py` (C2-S15)
- Pedestrian state (C2-S06)

**Outputs**
- `pedestrian_safety` component in `src/environment/reward.py`

**Acceptance Criteria**
- [ ] Penalty increases with pedestrian waiting time beyond a configurable threshold
- [ ] Component formula matches the reward architecture spec (C1-S16)
- [ ] Logged separately in `info` dict
- [ ] Unit test confirms correct response to a waiting pedestrian scenario

**Dependencies** — C2-S15, C2-S06

---

### C2-S21 — Emergency-Priority Objective

**Objective**
Implement the emergency vehicle priority reward component: rewards rapid clearance of the emergency vehicle's approach and penalises delay.

**Inputs**
- `src/environment/reward.py` (C2-S15)
- Emergency vehicle state (C2-S07)

**Outputs**
- `emergency_priority` component in `src/environment/reward.py`

**Acceptance Criteria**
- [ ] Reward is triggered when an emergency vehicle is present in the state
- [ ] Reward is proportional to the speed of clearing the emergency vehicle's path
- [ ] Penalty applies per-step while an emergency vehicle is waiting
- [ ] Logged separately in `info` dict
- [ ] Unit test covers emergency vehicle present and absent scenarios

**Dependencies** — C2-S15, C2-S07

---

### C2-S22 — Stability / Signal-Switching Objective

**Objective**
Implement a penalty for excessive signal phase switching, discouraging the policy from oscillating phases rapidly in a way that would cause real-world operational issues.

**Inputs**
- `src/environment/reward.py` (C2-S15)

**Outputs**
- `stability` component in `src/environment/reward.py`

**Acceptance Criteria**
- [ ] Penalty is applied each time a phase change occurs within a configurable minimum interval
- [ ] Penalty magnitude is configurable
- [ ] Logged separately in `info` dict
- [ ] Unit test confirms penalty fires on rapid switching

**Dependencies** — C2-S15

---

### C2-S23 — Robustness Objective

**Objective**
Implement a reward shaping component that encourages consistent performance even under sensor-degraded conditions, discouraging over-reliance on any single sensor channel.

**Inputs**
- `src/environment/reward.py` (C2-S15)
- Sensor-health state (C2-S08)

**Outputs**
- `robustness` component in `src/environment/reward.py`

**Acceptance Criteria**
- [ ] Robustness bonus/penalty is a function of sensor health and resulting action variance
- [ ] Component does not dominate the total reward (weight is bounded)
- [ ] Logged separately in `info` dict
- [ ] Unit test confirms component responds correctly to a degraded sensor scenario

**Dependencies** — C2-S15, C2-S08

---

### C2-S24 — Multi-Objective Reward Aggregation

**Objective**
Implement the configurable weighted aggregation of all reward components into the scalar training signal used by the RL algorithm.

**Inputs**
- Components C2-S19 to C2-S23
- Reward architecture spec (C1-S16)

**Outputs**
- Updated `src/environment/reward.py` with weight configuration
- `config/reward-weights.yaml`

**Acceptance Criteria**
- [ ] Weights for all components are specified in a config file
- [ ] Total reward is a weighted sum (or other documented aggregation) of components
- [ ] Weights sum constraint is enforced or documented
- [ ] Changing weights via config changes training behaviour without code modification
- [ ] Integration test confirms all components contribute to the total

**Dependencies** — C2-S19, C2-S20, C2-S21, C2-S22, C2-S23, C1-S16

---

### C2-S25 — Safety Constraint Layer

**Objective**
Implement the constraint enforcement layer: the module that intercepts policy actions and enforces all safety requirements (minimum green, maximum green, all-red intergreen) unconditionally.

**Inputs**
- `src/environment/action_validator.py` (C2-S14)
- Safety constraint layer spec (C1-S17)

**Outputs**
- `src/safety/constraint_layer.py`
- Updated `arvexa_env.py` `step()` to route through constraint layer before SUMO command

**Acceptance Criteria**
- [ ] Every SR from C1-S08 is enforced and has a corresponding constraint
- [ ] Constraint layer is logically separate from the reward function and policy
- [ ] Constraint violations are logged with constraint ID and action modification
- [ ] No combination of RL policy output can produce a signal state that violates an SR
- [ ] Integration test confirms constraint fires on a policy that would otherwise violate an SR

**Dependencies** — C2-S14, C1-S17

---

### C2-S26 — Emergency Priority Arbitration

**Objective**
Implement emergency vehicle preemption logic in the constraint layer: when an emergency vehicle is detected, override the RL policy to grant immediate green on the EV's approach.

**Inputs**
- `src/safety/constraint_layer.py` (C2-S25)
- Emergency-vehicle state (C2-S07), emergency-vehicle requirements (C1-S10)

**Outputs**
- Emergency preemption logic embedded in `constraint_layer.py`

**Acceptance Criteria**
- [ ] Preemption triggers when emergency vehicle state flag is active
- [ ] Preemption grants green on the EV approach within the configured maximum delay
- [ ] Preemption overrides any conflicting RL policy action
- [ ] Post-priority recovery returns to normal policy control after EV clears
- [ ] All EVRs from C1-S10 are satisfied and annotated in the code

**Dependencies** — C2-S25, C2-S07, C1-S10

---

### C2-S27 — Pedestrian Conflict Handling

**Objective**
Implement pedestrian phase protection in the constraint layer: guarantee minimum crossing time and prevent pedestrian phases from being interrupted by vehicle phase preemption (unless emergency vehicle).

**Inputs**
- `src/safety/constraint_layer.py` (C2-S25)
- Pedestrian state (C2-S06), pedestrian requirements (C1-S11)

**Outputs**
- Pedestrian protection logic embedded in `constraint_layer.py`

**Acceptance Criteria**
- [ ] Active pedestrian phase cannot be terminated before minimum crossing time elapses
- [ ] RL policy cannot skip a pedestrian phase that has been waiting beyond a configurable threshold
- [ ] Emergency vehicle preemption during pedestrian phase respects the EVR-PR conflict rule from C1-S10 and C1-S11
- [ ] All PRs from C1-S11 are satisfied and annotated

**Dependencies** — C2-S25, C2-S06, C1-S11, C1-S10

---

## Sprint 8 — Sensor Resilience & Simulation Evaluation

| Field | Value |
|---|---|
| **Sprint ID** | SPR-08 |
| **Capstone** | 2 |
| **Goal** | Evaluate ARVEXA under all sensor degradation modes, generate comparative results against the fixed-time baseline, and produce the ablation study |
| **Entry Criteria** | Sprint 7 complete; trained ARVEXA controller ready for evaluation |
| **Exit Criteria** | All 4 degradation modes evaluated; baseline comparison complete; statistical results and ablation produced |

---

### C2-S28 — Missing Sensor Scenario

**Objective**
Run evaluation experiments where one or more entire state channels are dropped (simulating a failed sensor or camera that produces no output). Record ARVEXA performance vs baseline.

**Inputs**
- Sensor degradation model (C1-S20), mode: missing (dropout probability = 1.0 for affected channel)
- Trained ARVEXA controller (C2-S17), experiment scenarios (C1-S30)

**Outputs**
- Evaluation results CSV: `results/c2/missing-sensor/`
- Per-metric comparison: ARVEXA vs fixed-time baseline

**Acceptance Criteria**
- [ ] At least one complete sensor channel is dropped per run
- [ ] ARVEXA activates the missing-channel fallback (from SFR)
- [ ] Results include all metrics from C1-S31
- [ ] Experiments run across ≥ 3 scenarios from C1-S30

**Dependencies** — C1-S20, C2-S17, C2-S18, C1-S30, C1-S31

---

### C2-S29 — Noisy Sensor Scenario

**Objective**
Run evaluation experiments where Gaussian noise is added to one or more state channel values (simulating sensor measurement error or environmental interference).

**Inputs**
- Sensor degradation model (C1-S20), mode: noisy (σ configurable per channel)
- Trained ARVEXA controller (C2-S17), experiment scenarios (C1-S30)

**Outputs**
- Evaluation results CSV: `results/c2/noisy-sensor/`

**Acceptance Criteria**
- [ ] Noise level σ is varied across ≥ 3 values per channel
- [ ] Results include all metrics from C1-S31
- [ ] Noise parameters are logged with results
- [ ] ARVEXA is compared against fixed-time baseline under same noise conditions

**Dependencies** — C1-S20, C2-S17, C2-S18, C1-S30

---

### C2-S30 — Misclassification Scenario

**Objective**
Run evaluation experiments where vehicle type labels are randomly misclassified (e.g., trucks labelled as cars, emergency vehicle label suppressed). Assess impact on emergency priority and multi-objective behaviour.

**Inputs**
- Sensor degradation model (C1-S20), mode: misclassification (probability p configurable)
- Trained ARVEXA controller (C2-S17), experiment scenarios (C1-S30)

**Outputs**
- Evaluation results CSV: `results/c2/misclassification/`

**Acceptance Criteria**
- [ ] Misclassification probability p is varied across ≥ 3 values
- [ ] Emergency vehicle misclassification is explicitly tested (EV not detected)
- [ ] Impact on emergency priority metric is recorded
- [ ] Results include all relevant metrics from C1-S31

**Dependencies** — C1-S20, C2-S03, C2-S17, C2-S18, C1-S30

---

### C2-S31 — Partial Sensor Failure

**Objective**
Run evaluation experiments where a subset of junction approaches (lanes) lose sensor coverage, while others remain operational. Assess how ARVEXA adapts with partial observability.

**Inputs**
- Sensor degradation model (C1-S20), mode: partial (lane/approach subset)
- Trained ARVEXA controller (C2-S17)

**Outputs**
- Evaluation results CSV: `results/c2/partial-failure/`

**Acceptance Criteria**
- [ ] At least 2 different subsets of failed approaches are tested
- [ ] Sensor health state channel reflects failed approaches
- [ ] Results show performance degradation curve as more approaches lose coverage
- [ ] Fallback behaviour (from SFR) is active and logged

**Dependencies** — C1-S20, C2-S08, C2-S17, C2-S18, C1-S30

---

### C2-S32 — Degraded Observation Pipeline

**Objective**
Test combined degradation: multiple simultaneous failure modes active. Validate that the state builder's fallback handling and the safety constraint layer remain operational under worst-case sensor conditions.

**Inputs**
- C2-S08 (sensor health), C2-S09 (state builder), C2-S25 (constraint layer)
- Sensor degradation model (C1-S20)

**Outputs**
- Evaluation results CSV: `results/c2/combined-degradation/`
- Constraint layer activation log

**Acceptance Criteria**
- [ ] At least one combined scenario (noisy + partial) is evaluated
- [ ] Constraint layer does not produce unsafe outputs under any degradation combination
- [ ] State builder raises a clear warning (not a crash) when all channels for an approach are lost
- [ ] Safety requirements (C1-S08) are not violated in any combined degradation run

**Dependencies** — C2-S08, C2-S09, C2-S25, C1-S20

---

### C2-S33 — Baseline Comparison

**Objective**
Run the fixed-time baseline controller across all experiment scenarios used for ARVEXA evaluation, producing a complete baseline metrics dataset for comparison.

**Inputs**
- Fixed-time baseline controller (C1-S28)
- All experiment scenarios (C1-S30)
- Evaluation metrics (C1-S31), reproducibility config (C1-S32)

**Outputs**
- Baseline results CSV: `results/c2/baseline/`
- All metrics from C1-S31 populated for baseline

**Acceptance Criteria**
- [ ] Baseline is evaluated across all scenarios used for ARVEXA
- [ ] Baseline runs use the same demand files and seeds as ARVEXA runs
- [ ] All metrics from C1-S31 are present in baseline output
- [ ] Results are reproducible from run-ID

**Dependencies** — C1-S28, C1-S30, C1-S31, C1-S32

---

### C2-S34 — Repeated-Run Evaluation

**Objective**
Run ARVEXA evaluation across ≥ 5 independent random seeds to produce a distribution of performance results rather than a single point estimate.

**Inputs**
- Trained ARVEXA controller (C2-S17, best checkpoint)
- Reproducibility config (C1-S32), evaluation script (C2-S18)

**Outputs**
- Multi-seed results CSV: `results/c2/multi-seed/`
- Per-seed results for each scenario

**Acceptance Criteria**
- [ ] At least 5 seeds evaluated per scenario
- [ ] Each seed is logged and results are tagged with seed value
- [ ] Results show mean and variance across seeds
- [ ] Same procedure applied to baseline for fair comparison

**Dependencies** — C2-S17, C2-S18, C1-S32

---

### C2-S35 — Statistical Result Generation

**Objective**
Compute descriptive and inferential statistics across repeated runs: means, standard deviations, confidence intervals, and significance tests comparing ARVEXA to the fixed-time baseline.

**Inputs**
- Multi-seed results (C2-S34), baseline results (C2-S33)

**Outputs**
- `src/analysis/statistics.py`
- Statistical summary tables (mean ± std, 95% CI per metric per scenario)
- Significance test results (e.g., Mann-Whitney U or t-test)

**Acceptance Criteria**
- [ ] All metrics from C1-S31 have a statistical summary table
- [ ] At least one appropriate significance test is applied per metric comparison
- [ ] Effect size is reported alongside p-values
- [ ] Results are saved in a reproducible format (CSV + JSON)

**Dependencies** — C2-S34, C2-S33, C1-S31

---

### C2-S36 — Ablation Experiments

**Objective**
Systematically disable each reward component in isolation and evaluate the resulting performance to quantify each component's contribution to ARVEXA's behaviour.

**Inputs**
- Trained ARVEXA controller variants (retrained with each component removed)
- Multi-objective reward (C2-S24), evaluation script (C2-S18)

**Outputs**
- Ablation results CSV: `results/c2/ablation/`
- Ablation summary table: removed component → metric change vs full model

**Acceptance Criteria**
- [ ] Each of the 5+ reward components from C2-S19 to C2-S23 is ablated in isolation
- [ ] Each ablation variant is trained and evaluated using the same protocol as the full model
- [ ] Ablation table clearly shows the delta (Δ) for each metric vs the full model
- [ ] At least one ablation produces a statistically significant degradation

**Dependencies** — C2-S24, C2-S18, C2-S34, C2-S35

---

## Capstone-2 Exit Checklist

| ID | Item | Status |
|---|---|---|
| C2-EX-01 | SUMO environment wrapper connects via TraCI without errors | ☐ |
| C2-EX-02 | Unified state builder produces valid normalised vector for all degradation modes | ☐ |
| C2-EX-03 | ARVEXA trains to convergence on normal-demand scenario | ☐ |
| C2-EX-04 | All 5+ reward components implemented and configurable | ☐ |
| C2-EX-05 | Safety constraint layer blocks all unsafe actions | ☐ |
| C2-EX-06 | Emergency preemption tested and meeting EVRs | ☐ |
| C2-EX-07 | Pedestrian protection tested and meeting PRs | ☐ |
| C2-EX-08 | All 4 sensor degradation modes evaluated | ☐ |
| C2-EX-09 | Baseline comparison complete across all scenarios | ☐ |
| C2-EX-10 | Multi-seed results generated (≥ 5 seeds) | ☐ |
| C2-EX-11 | Statistical analysis complete with significance testing | ☐ |
| C2-EX-12 | Ablation study complete for all reward components | ☐ |
