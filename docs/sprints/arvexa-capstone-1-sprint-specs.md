# ARVEXA — Capstone-1 Sprint & Slice Specification

> **Phase 1 of 3 | Research, Requirements & System Design**
> Sprints 1–4 | Slices C1-S01 to C1-S32

---

## Phase Overview

| Field | Value |
|---|---|
| **Capstone** | 1 |
| **Theme** | Research, Requirements & System Design |
| **Sprint Range** | SPR-01 — SPR-04 |
| **Slice Range** | C1-S01 — C1-S32 |
| **Primary Deliverable** | Frozen research specification + runnable SUMO baseline |

## Phase Exit Criteria

The following must be satisfied before Capstone-2 may begin:

- [ ] Problem definition, research questions and objectives are reviewed and frozen by supervisor
- [ ] All requirement categories (FR, NFR, SR, SFR, EVR, PR) are documented and baselined
- [ ] Requirements traceability matrix links every requirement to at least one RO
- [ ] All architecture documents (system, RL, SUMO, vision, constraints) are reviewed
- [ ] A real-world junction is selected and a SUMO network runs without errors
- [ ] Fixed-time baseline controller produces valid signal outputs in SUMO
- [ ] Experiment scenarios, metrics and reproducibility configuration are frozen

---

## Sprint 1 — Research Foundation

| Field | Value |
|---|---|
| **Sprint ID** | SPR-01 |
| **Capstone** | 1 |
| **Goal** | Establish a clear, evidence-based problem definition, research questions and objectives that anchor the entire ARVEXA project |
| **Entry Criteria** | Existing literature notes and initial problem intuition available |
| **Exit Criteria** | RQs, ROs and scope are peer-reviewed and frozen; literature evidence is cross-referenced to RQs |

---

### C1-S01 — Problem Definition

**Objective**
Document the traffic signal control problem ARVEXA addresses. Articulate the limitations of current systems (fixed-time, single-objective, sensor-dependent) and why an RL-based multi-modal approach is warranted. The statement must be precise enough to anchor all subsequent requirements.

**Inputs**
- Existing problem notes or drafts
- Literature on fixed-time and conventional adaptive signal control
- Domain knowledge of the study environment

**Outputs**
- `docs/research/problem-definition.md`

**Acceptance Criteria**
- [ ] Problem statement is expressed in ≤ 3 paragraphs, unambiguously
- [ ] At least 3 concrete limitations of current signal control systems are enumerated
- [ ] Affected stakeholder groups (commuters, pedestrians, emergency services) are identified
- [ ] Document is reviewed and approved by the project supervisor

**Dependencies** — None

---

### C1-S02 — Research Questions

**Objective**
Derive 3–6 focused, answerable research questions (RQs) directly from the problem definition. Each RQ must be narrow enough to be addressed by a defined experiment with an observable outcome.

**Inputs**
- `docs/research/problem-definition.md` (C1-S01)
- Literature on open problems in adaptive traffic signal control

**Outputs**
- `docs/research/research-questions.md`
- RQ list with IDs: RQ-01 … RQ-N

**Acceptance Criteria**
- [ ] Each RQ is a question, not a hypothesis or objective statement
- [ ] Each RQ is traceable to at least one stated limitation in C1-S01
- [ ] Each RQ specifies what would constitute an answer (observable outcome or metric)
- [ ] RQ list is reviewed and frozen by supervisor

**Dependencies** — C1-S01

---

### C1-S03 — Research Objectives

**Objective**
Convert each research question into one or more concrete research objectives (ROs). Each RO describes what will be built, measured, or demonstrated to answer the corresponding RQ.

**Inputs**
- `docs/research/research-questions.md` (C1-S02)

**Outputs**
- `docs/requirements/research-objectives.md`
- RO list with IDs: RO-01 … RO-N, each linked to its parent RQ

**Acceptance Criteria**
- [ ] Every RQ has at least one corresponding RO
- [ ] Each RO is measurable (specifies what artefact or evidence is produced)
- [ ] ROs do not prescribe implementation details (remain at research level)
- [ ] RQ → RO mapping is explicitly documented in the file

**Dependencies** — C1-S02

---

### C1-S04 — Scope, Assumptions and Exclusions

**Objective**
Explicitly bound what ARVEXA will and will not address. Document the assumptions the project relies on (e.g., simulation fidelity, camera availability) and the exclusions that are out of scope (e.g., multi-junction coordination, V2I communication).

**Inputs**
- `docs/research/problem-definition.md` (C1-S01)
- `docs/research/research-questions.md` (C1-S02)

**Outputs**
- `docs/research/scope-assumptions-exclusions.md`

**Acceptance Criteria**
- [ ] In-scope items are listed with justification referencing an RQ or RO
- [ ] Out-of-scope items are listed with justification for exclusion
- [ ] At least 5 explicit assumptions are documented
- [ ] No exclusion contradicts an active research objective
- [ ] Reviewed and approved by supervisor

**Dependencies** — C1-S01, C1-S02

---

### C1-S05 — Literature Evidence Organisation

**Objective**
Reorganise the existing literature database so each source is linked to the specific RQ or RO it evidences. The goal is a traceable evidence base rather than a reading list.

**Inputs**
- Existing `docs/research/literature-review.md` and `docs/research/references.md`
- RQ and RO lists from C1-S02, C1-S03

**Outputs**
- Updated `docs/research/literature-review.md` with per-source RQ/RO tags
- `docs/research/evidence-map.md` — matrix mapping each source to the RQ/RO it evidences

**Acceptance Criteria**
- [ ] Every RQ is supported by at least 3 cited sources
- [ ] Every RO is supported by at least 1 cited source or analogous prior work
- [ ] All references follow a consistent citation format
- [ ] Evidence map is accessible and version-controlled

**Dependencies** — C1-S02, C1-S03

---

## Sprint 2 — Requirements & Traceability

| Field | Value |
|---|---|
| **Sprint ID** | SPR-02 |
| **Capstone** | 1 |
| **Goal** | Convert the frozen research problem into a baselined, traceable system specification covering all requirement categories |
| **Entry Criteria** | Sprint 1 complete; RQs, ROs, scope and literature all frozen |
| **Exit Criteria** | All requirement categories documented; RTM links every requirement to an RO; baseline signed off by supervisor |

---

### C1-S06 — Functional Requirements

**Objective**
Document what ARVEXA must do: its observable behaviours, the functions it must perform, and the conditions under which it must perform them. Each FR must be atomic and independently testable.

**Inputs**
- `docs/requirements/research-objectives.md` (C1-S03)
- `docs/research/scope-assumptions-exclusions.md` (C1-S04)

**Outputs**
- `docs/requirements/functional-requirements.md`
- FR list with IDs: FR-001 … FR-N

**Acceptance Criteria**
- [ ] Each FR uses "shall" language: "The system shall …"
- [ ] Each FR is atomic — it tests exactly one behaviour
- [ ] Each FR is linked to at least one RO
- [ ] No FR describes an implementation mechanism (what, not how)
- [ ] At least 30 FRs covering: signal control, vehicle detection, classification, pedestrian handling, emergency preemption, sensor degradation response

**Dependencies** — C1-S03, C1-S04

---

### C1-S07 — Non-Functional Requirements

**Objective**
Document the quality constraints ARVEXA must satisfy: performance, reliability, reproducibility, maintainability, and portability. These constrain how the system performs its functions, not what it does.

**Inputs**
- `docs/requirements/functional-requirements.md` (C1-S06)
- Academic reproducibility standards

**Outputs**
- `docs/requirements/non-functional-requirements.md`
- NFR list with IDs: NFR-001 … NFR-N

**Acceptance Criteria**
- [ ] Each NFR specifies a measurable threshold (e.g., "training run reproducible within ±2% metric across 5 seeds")
- [ ] NFRs cover: simulation performance, training reproducibility, evaluation portability, code maintainability, experiment auditability
- [ ] Each NFR is linked to at least one FR or RO
- [ ] At least 10 NFRs documented

**Dependencies** — C1-S06

---

### C1-S08 — Safety Requirements

**Objective**
Identify and document requirements that prevent ARVEXA from issuing signals that would endanger road users. These constrain controller output unconditionally, regardless of the RL policy's recommendation.

**Inputs**
- `docs/requirements/functional-requirements.md` (C1-S06)
- Traffic signal safety standards (minimum green time, all-red clearance intervals)

**Outputs**
- `docs/requirements/safety-requirements.md`
- SR list with IDs: SR-001 … SR-N

**Acceptance Criteria**
- [ ] All-red clearance interval constraints are documented with minimum duration
- [ ] Minimum green time per phase is specified
- [ ] Maximum green time per phase is specified
- [ ] Conflicting phase activation is explicitly prohibited
- [ ] Every SR is marked unconditional — no RL policy output may bypass it

**Dependencies** — C1-S06

---

### C1-S09 — Sensor-Failure Requirements

**Objective**
Document requirements governing ARVEXA's behaviour when sensor inputs are degraded, missing, or unreliable. The system must degrade gracefully with a defined fallback for every failure mode.

**Inputs**
- `docs/requirements/functional-requirements.md` (C1-S06)
- `docs/requirements/safety-requirements.md` (C1-S08)

**Outputs**
- `docs/requirements/sensor-failure-requirements.md`
- SFR list with IDs: SFR-001 … SFR-N

**Acceptance Criteria**
- [ ] Requirements cover: total sensor dropout, partial sensor loss, noisy readings, vehicle misclassification
- [ ] A defined fallback behaviour is specified for each failure mode
- [ ] No fallback behaviour violates any SR
- [ ] Maximum detection latency for sensor failure is specified
- [ ] At least 8 SFRs documented

**Dependencies** — C1-S06, C1-S08

---

### C1-S10 — Emergency-Vehicle Requirements

**Objective**
Document requirements governing ARVEXA's behaviour when an emergency vehicle is detected approaching or passing through the controlled junction.

**Inputs**
- `docs/requirements/functional-requirements.md` (C1-S06)
- `docs/requirements/safety-requirements.md` (C1-S08)

**Outputs**
- `docs/requirements/emergency-vehicle-requirements.md`
- EVR list with IDs: EVR-001 … EVR-N

**Acceptance Criteria**
- [ ] Priority preemption trigger conditions are specified (detection threshold, distance)
- [ ] Priority clearance behaviour is specified (which phase is granted, duration)
- [ ] Maximum permissible emergency vehicle delay is defined
- [ ] Post-priority recovery behaviour (returning to normal control) is specified
- [ ] Conflict with active pedestrian phase is addressed
- [ ] At least 6 EVRs documented

**Dependencies** — C1-S06, C1-S08

---

### C1-S11 — Pedestrian Requirements

**Objective**
Document requirements governing ARVEXA's handling of pedestrian demand, pedestrian phase scheduling, and minimum crossing-time protection.

**Inputs**
- `docs/requirements/functional-requirements.md` (C1-S06)
- `docs/requirements/safety-requirements.md` (C1-S08)

**Outputs**
- `docs/requirements/pedestrian-requirements.md`
- PR list with IDs: PR-001 … PR-N

**Acceptance Criteria**
- [ ] Minimum pedestrian crossing time is specified per crossing
- [ ] Pedestrian demand detection requirements are stated
- [ ] Conditions under which a pedestrian phase may be deferred are stated (if any)
- [ ] Pedestrian vs. vehicle phase priority arbitration rules are stated
- [ ] Conflict with emergency-vehicle preemption is explicitly addressed
- [ ] At least 5 PRs documented

**Dependencies** — C1-S06, C1-S08, C1-S10

---

### C1-S12 — Requirements Traceability Matrix

**Objective**
Produce the authoritative matrix linking every requirement upward to its RO and RQ, and noting the architectural component responsible for satisfying it. This is the single traceability artefact for the project.

**Inputs**
- All requirement documents: C1-S06 to C1-S11
- `docs/requirements/research-objectives.md` (C1-S03)

**Outputs**
- `docs/requirements/requirements-traceability-matrix.md` (or `.csv`)
- Columns: Req ID | Summary | Type | Parent RO | Parent RQ | Architecture Component | Sprint | Status

**Acceptance Criteria**
- [ ] Every requirement has exactly one row
- [ ] Every requirement is linked to at least one RO
- [ ] Every RO is linked to at least one RQ
- [ ] No orphan requirements exist (requirement with no RO)
- [ ] RTM is version-controlled and updated as architecture is defined in Sprint 3

**Dependencies** — C1-S03, C1-S06, C1-S07, C1-S08, C1-S09, C1-S10, C1-S11

---

## Sprint 3 — Architecture & Experimental Design

| Field | Value |
|---|---|
| **Sprint ID** | SPR-03 |
| **Capstone** | 1 |
| **Goal** | Define how ARVEXA works architecturally — state, action, reward, constraints, SUMO integration, vision pipeline — before any implementation begins |
| **Entry Criteria** | Sprint 2 complete; all requirements baselined and RTM populated |
| **Exit Criteria** | All architecture documents reviewed; architecture is internally consistent and satisfies all requirement categories |

---

### C1-S13 — Overall System Architecture

**Objective**
Produce a top-level architecture document and diagram showing all ARVEXA subsystems (RL controller, SUMO environment, vision pipeline, safety constraint layer, state builder) and the interfaces between them.

**Inputs**
- All requirements documents (C1-S06 to C1-S11)
- Existing architecture notes

**Outputs**
- `docs/architecture/system-architecture.md`
- Top-level architecture diagram (C4 Level 2 or equivalent)
- Interface table: subsystem → subsystem | data type | direction | frequency

**Acceptance Criteria**
- [ ] All major subsystems are identified and named
- [ ] All inter-subsystem interfaces are described (data format, direction, update frequency)
- [ ] Architecture is consistent with all FRs and NFRs
- [ ] No implementation-level detail (no specific library choices forced without justification)
- [ ] Reviewed and approved by supervisor

**Dependencies** — C1-S06, C1-S07, C1-S12

---

### C1-S14 — RL State Representation

**Objective**
Define exactly what information the RL agent observes at each decision step, how each element is represented numerically, and how each element maps to a sensor or SUMO output.

**Inputs**
- `docs/architecture/system-architecture.md` (C1-S13)
- Functional requirements (C1-S06), sensor-failure requirements (C1-S09)

**Outputs**
- `docs/architecture/rl-state-representation.md`
- State vector specification table: Element Name | Type | Range | Source | Sensor Dependency | Failure Impact

**Acceptance Criteria**
- [ ] Every state element is named, typed and range-bounded
- [ ] Every state element has an identified source (SUMO subscription or sensor)
- [ ] Impact of each sensor failure mode on state elements is documented
- [ ] Total state dimension count is stated
- [ ] State is consistent with all SFRs

**Dependencies** — C1-S13, C1-S09

---

### C1-S15 — Action Space

**Objective**
Define the complete set of decisions the ARVEXA controller may take at each step: which signal phases may be selected and what duration values are permitted.

**Inputs**
- `docs/architecture/rl-state-representation.md` (C1-S14)
- Safety requirements (C1-S08)

**Outputs**
- `docs/architecture/action-space.md`
- Action space specification: type (discrete/continuous) | dimensions | valid range | constraints

**Acceptance Criteria**
- [ ] All valid signal phases are enumerated
- [ ] Duration action space is defined (range, step size or continuous bound)
- [ ] Every action is consistent with all SRs (minimum green times enforced)
- [ ] Invalid action handling policy is stated (masking, clipping, or penalty)
- [ ] Total action space size is documented

**Dependencies** — C1-S14, C1-S08

---

### C1-S16 — Reward & Objective Architecture

**Objective**
Define the reward function structure: the individual objective components (traffic efficiency, pedestrian safety, emergency priority, stability, robustness), how each is measured, and how they are aggregated into a training signal.

**Inputs**
- Functional requirements (C1-S06), pedestrian requirements (C1-S11), emergency requirements (C1-S10)

**Outputs**
- `docs/architecture/reward-architecture.md`
- Reward component table: Component | Formula | Measurement Source | Range | Weight Placeholder

**Acceptance Criteria**
- [ ] At least 5 distinct reward components are defined
- [ ] Each component is measurable from simulation state
- [ ] Aggregation method is specified (weighted sum, Pareto front, or alternatives with decision criteria)
- [ ] Component range is documented for each element
- [ ] Reward architecture is consistent with all FRs and priority requirements

**Dependencies** — C1-S14, C1-S15

---

### C1-S17 — Safety & Action Constraint Layer

**Objective**
Specify the constraint layer that sits between the RL policy output and the signal actuator, ensuring no unsafe action is ever executed regardless of policy recommendations.

**Inputs**
- `docs/architecture/action-space.md` (C1-S15)
- Safety requirements (C1-S08), emergency requirements (C1-S10), pedestrian requirements (C1-S11)

**Outputs**
- `docs/architecture/safety-constraint-layer.md`
- Constraint specification table: Trigger Condition | Enforced Action | Overrides | Parent SR/EVR/PR

**Acceptance Criteria**
- [ ] Every SR maps to at least one constraint in the layer
- [ ] Emergency priority preemption logic is specified in full
- [ ] Pedestrian minimum crossing protection is specified
- [ ] Constraint layer is described as logically separate from the RL policy
- [ ] No RL policy output may bypass the constraint layer under any condition

**Dependencies** — C1-S15, C1-S08, C1-S10, C1-S11

---

### C1-S18 — SUMO Architecture

**Objective**
Define how SUMO is configured as the simulation backbone: network structure, vehicle types, signal control interface (TraCI), and how ARVEXA connects to it.

**Inputs**
- `docs/architecture/system-architecture.md` (C1-S13)
- SUMO and TraCI documentation

**Outputs**
- `docs/architecture/sumo-architecture.md`
- SUMO integration diagram: ARVEXA ↔ TraCI ↔ SUMO Network

**Acceptance Criteria**
- [ ] TraCI interface is specified (commands and subscriptions to be used)
- [ ] SUMO simulation step size and ARVEXA decision-step relationship are defined
- [ ] Signal phase → SUMO TLS state mapping is documented
- [ ] Vehicle type configuration approach is specified
- [ ] Headless/batch execution approach is described (for reproducible experiments)

**Dependencies** — C1-S13, C1-S15

---

### C1-S19 — Vision Pipeline Architecture

**Objective**
Define the architecture of the computer vision subsystem that will process real camera footage to extract traffic state information in Capstone-3. This is a design document only; implementation is deferred.

**Inputs**
- `docs/architecture/system-architecture.md` (C1-S13)
- `docs/architecture/rl-state-representation.md` (C1-S14)

**Outputs**
- `docs/architecture/vision-pipeline-architecture.md`
- Pipeline diagram: Camera → Frames → Detection → Classification → Tracking → Counting → Traffic State

**Acceptance Criteria**
- [ ] Each pipeline stage is named and its input/output types are defined
- [ ] Output of each stage maps to specific state elements from C1-S14
- [ ] Failure modes of each stage are identified
- [ ] Interface between vision pipeline output and ARVEXA state builder is specified
- [ ] Document clearly notes that full implementation is deferred to Capstone-3

**Dependencies** — C1-S13, C1-S14

---

### C1-S20 — Sensor Degradation Model

**Objective**
Define a formal model of how sensor degradation will be simulated in ARVEXA evaluations: the degradation types, the parameters controlling severity, and their mapping to sensor-failure requirements.

**Inputs**
- `docs/requirements/sensor-failure-requirements.md` (C1-S09)
- `docs/architecture/rl-state-representation.md` (C1-S14)

**Outputs**
- `docs/architecture/sensor-degradation-model.md`
- Degradation mode table: Mode ID | Affected State Elements | Control Parameter | Range | Parent SFR

**Acceptance Criteria**
- [ ] At least 4 degradation modes defined: missing (dropout), noisy (additive noise), misclassified (type error), partial (lane/approach loss)
- [ ] Each mode specifies which state elements are affected
- [ ] Each mode specifies its control parameter and range (e.g., dropout probability p ∈ [0,1], noise σ ∈ [0, σ_max])
- [ ] Model is implementable as a wrapper around the state builder (no SUMO modification required)
- [ ] Each mode is linked to its parent SFR

**Dependencies** — C1-S09, C1-S14

---

## Sprint 4 — SUMO Baseline & Experiment Plan

| Field | Value |
|---|---|
| **Sprint ID** | SPR-04 |
| **Capstone** | 1 |
| **Goal** | Deliver a runnable SUMO model with a fixed-time baseline, a frozen experiment plan, and reproducibility configuration ready to support Capstone-2 |
| **Entry Criteria** | Sprint 3 complete; all architecture documents reviewed and approved |
| **Exit Criteria** | SUMO runs without errors; baseline produces valid outputs; experiment plan, metrics and reproducibility config are frozen |

---

### C1-S21 — Junction Selection

**Objective**
Select and justify the real-world junction that will serve as the ARVEXA study site. It must be representative of the target problem, accessible for camera data collection in Capstone-3, and of sufficient complexity.

**Inputs**
- `docs/research/scope-assumptions-exclusions.md` (C1-S04)
- Local geographic knowledge; camera placement accessibility assessment

**Outputs**
- `docs/experiments/junction-selection.md`
- Junction specification: GPS coordinates, junction type (4-way / T-junction etc.), geometry, existing phase plan

**Acceptance Criteria**
- [ ] Junction is identified with GPS coordinates and name
- [ ] Junction type and physical geometry are described
- [ ] Existing signal phase plan (if any) is documented or noted as absent
- [ ] Camera placement feasibility is assessed (line of sight, mounting options)
- [ ] Justification references at least one research objective

**Dependencies** — C1-S04

---

### C1-S22 — SUMO Network Construction

**Objective**
Build the SUMO network file for the selected junction: lanes, geometry, turn movements, and signal phase placeholders. The network must match the real junction geometry.

**Inputs**
- Junction specification (C1-S21)
- OpenStreetMap export or manual geometry survey

**Outputs**
- `sumo/network/arvexa-junction.net.xml`
- Lane topology diagram
- `docs/sumo/network-construction-notes.md`

**Acceptance Criteria**
- [ ] Network loads in SUMO without errors or warnings
- [ ] All lane connections are correct (no disconnected approaches)
- [ ] Lane counts per approach match the real junction
- [ ] Turn restrictions match the real junction geometry
- [ ] Network file is committed to version control

**Dependencies** — C1-S21

---

### C1-S23 — Traffic Demand Model

**Objective**
Define vehicle flow rates (vehicles/hour per approach and movement) for each experiment scenario. These form the input demand for all SUMO simulations.

**Inputs**
- Junction specification (C1-S21)
- Available traffic count data or engineering estimates

**Outputs**
- `sumo/demand/traffic-demand.rou.xml`
- `docs/experiments/traffic-demand-model.md`
- Demand table: Approach × Movement × Scenario × Flow Rate (veh/hr)

**Acceptance Criteria**
- [ ] At least 3 demand levels defined: low, medium, high
- [ ] Demand covers all junction approaches
- [ ] Demand file loads in SUMO without errors
- [ ] Demand parameters are version-controlled and not hard-coded

**Dependencies** — C1-S22

---

### C1-S24 — Vehicle-Type Model

**Objective**
Define the vehicle types present in SUMO simulations (at minimum: car, truck/bus, motorcycle, emergency vehicle) with SUMO-compatible length, speed, and acceleration parameters.

**Inputs**
- SUMO vehicle type documentation
- Functional requirements (C1-S06)

**Outputs**
- `sumo/demand/vehicle-types.add.xml`
- Vehicle type table: ID | Category | SUMO Parameters | Type Proportion

**Acceptance Criteria**
- [ ] At least 4 vehicle types defined
- [ ] Emergency vehicle type is distinguishable via vType attribute or name prefix
- [ ] Vehicle type file loads in SUMO without errors
- [ ] Type distribution proportions per scenario are documented

**Dependencies** — C1-S22

---

### C1-S25 — Pedestrian Model

**Objective**
Configure pedestrian movement in SUMO: crossing locations, pedestrian flow rates per scenario, and correct interaction with vehicle signal phases.

**Inputs**
- `sumo/network/arvexa-junction.net.xml` (C1-S22)
- Pedestrian requirements (C1-S11)

**Outputs**
- Updated network or additional file with pedestrian crossings and walkways
- `sumo/demand/pedestrian-demand.rou.xml`

**Acceptance Criteria**
- [ ] Pedestrian crossings exist at all relevant junction approaches
- [ ] Pedestrian flow rates are defined per demand scenario
- [ ] Pedestrians interact correctly with vehicle signal phases in SUMO
- [ ] Minimum crossing time from PR is enforceable by phase duration
- [ ] Simulation runs with pedestrians without errors

**Dependencies** — C1-S22, C1-S11

---

### C1-S26 — Emergency-Vehicle Model

**Objective**
Configure how emergency vehicles are represented and triggered in SUMO simulations, including their insertion logic and the observable state that ARVEXA will receive.

**Inputs**
- `sumo/demand/vehicle-types.add.xml` (C1-S24)
- Emergency-vehicle requirements (C1-S10)

**Outputs**
- Emergency vehicle route/trigger configuration file
- `docs/sumo/emergency-vehicle-simulation-notes.md`

**Acceptance Criteria**
- [ ] Emergency vehicles can be inserted on demand (scripted or on-schedule)
- [ ] Emergency vehicle route traverses the study junction
- [ ] TraCI can detect emergency vehicle presence and distance from junction
- [ ] A test run demonstrates detection and logging without errors

**Dependencies** — C1-S24, C1-S10

---

### C1-S27 — Signal-Phase Model

**Objective**
Define the complete signal phase structure for the SUMO junction: valid signal states, intergreen logic, and the TraCI interface through which ARVEXA will command phase changes.

**Inputs**
- Junction specification (C1-S21)
- `docs/architecture/action-space.md` (C1-S15)

**Outputs**
- Signal phase definition (`.add.xml` or embedded in `.net.xml`)
- Phase diagram showing all valid signal states and transitions
- TraCI command mapping document

**Acceptance Criteria**
- [ ] All valid signal phases are defined and enumerated
- [ ] All-red intergreen transitions are included between conflicting phases
- [ ] Phase can be changed via a TraCI command in a standalone test script
- [ ] Phase definitions are consistent with the action space architecture (C1-S15)

**Dependencies** — C1-S22, C1-S15

---

### C1-S28 — Baseline Fixed-Time Controller

**Objective**
Implement a fixed-time signal controller as the primary comparison baseline. The controller cycles through phases on a fixed schedule regardless of traffic state.

**Inputs**
- Signal-phase model (C1-S27)
- Junction timing plan (real-world or engineered)
- Reproducibility config (C1-S32 draft)

**Outputs**
- `src/baselines/fixed_time_controller.py`
- Baseline timing plan documented in config file

**Acceptance Criteria**
- [ ] Controller completes a full simulation run without errors
- [ ] Phase sequence and timing are configurable via config file, not hard-coded
- [ ] Per-step metrics (queue length, waiting time, throughput) are logged
- [ ] At least one complete run is committed with output logs
- [ ] Re-running with the same config and seed produces identical output

**Dependencies** — C1-S22, C1-S23, C1-S24, C1-S25, C1-S26, C1-S27

---

### C1-S29 — SUMO Calibration Plan

**Objective**
Define the process to be used in Capstone-3 to calibrate the SUMO simulation against real traffic observations. This is a planning document; implementation is deferred.

**Inputs**
- `docs/architecture/sumo-architecture.md` (C1-S18)
- `docs/experiments/traffic-demand-model.md` (C1-S23)

**Outputs**
- `docs/experiments/sumo-calibration-plan.md`
- Calibration parameter list; calibration metric definition

**Acceptance Criteria**
- [ ] Calibration parameters are listed (demand flow rates, headway distributions, speed distributions)
- [ ] Calibration metric is defined (e.g., GEH statistic ≤ 5 for ≥ 85% of flows, RMSE on flow)
- [ ] Step-by-step calibration process is described
- [ ] Calibration and validation datasets are distinguished (no data leakage)

**Dependencies** — C1-S22, C1-S23

---

### C1-S30 — Experiment Scenarios

**Objective**
Define the complete set of simulation scenarios for ARVEXA evaluation. Each scenario specifies demand level, vehicle composition, pedestrian demand, sensor condition, and any special events.

**Inputs**
- `docs/experiments/traffic-demand-model.md` (C1-S23)
- Sensor-failure requirements (C1-S09), sensor degradation model (C1-S20)

**Outputs**
- `docs/experiments/experiment-scenarios.md`
- Scenario table: ID | Demand | Composition | Pedestrian Level | Sensor Condition | Special Events

**Acceptance Criteria**
- [ ] At least 6 distinct scenarios defined
- [ ] Scenarios cover: normal operation, high-demand, sensor-degraded, emergency vehicle, pedestrian-heavy
- [ ] Each scenario has a unique ID: SCN-01 … SCN-N
- [ ] Each scenario is linked to at least one RQ
- [ ] Scenario table is frozen before Capstone-2 begins

**Dependencies** — C1-S23, C1-S09, C1-S20

---

### C1-S31 — Evaluation Metrics

**Objective**
Define the exact metrics used to evaluate ARVEXA performance, including their formulae, collection methods, and the baselines against which they will be compared.

**Inputs**
- `docs/requirements/research-objectives.md` (C1-S03)
- Experiment scenarios (C1-S30)

**Outputs**
- `docs/experiments/evaluation-metrics.md`
- Metric table: ID | Name | Formula | Unit | Collection Method | Comparison Baseline

**Acceptance Criteria**
- [ ] At least 8 metrics defined
- [ ] Metrics cover: vehicle queue length, average waiting time, intersection throughput, pedestrian wait time, emergency vehicle clearance time, signal switching frequency
- [ ] Each metric maps to at least one RO
- [ ] Collection method is specified (TraCI subscription, log parsing, post-processing script)
- [ ] Metric list is frozen before Capstone-2 begins

**Dependencies** — C1-S03, C1-S30

---

### C1-S32 — Reproducibility Configuration

**Objective**
Establish configuration management, random seeding, and run-logging conventions that make all ARVEXA experiment results reproducible across team members and evaluation sessions.

**Inputs**
- Non-functional requirements (C1-S07)
- Existing repository structure

**Outputs**
- `config/experiment-defaults.yaml`
- `docs/experiments/reproducibility-guide.md`
- Seeding convention documented; run-ID scheme defined

**Acceptance Criteria**
- [ ] A single YAML config controls all tunable experiment parameters
- [ ] Random seeds are set explicitly and logged for every run
- [ ] Each run produces a unique run ID embedded in all output files and logs
- [ ] A README section documents how to reproduce any result from its run ID alone
- [ ] The baseline run from C1-S28 is reproducible using this system

**Dependencies** — C1-S28, C1-S07

---

## Capstone-1 Exit Checklist

Before handing off to Capstone-2, verify all items below:

| ID | Item | Status |
|---|---|---|
| C1-EX-01 | Problem definition frozen and supervisor-approved | ☐ |
| C1-EX-02 | Research questions frozen | ☐ |
| C1-EX-03 | Research objectives frozen and linked to RQs | ☐ |
| C1-EX-04 | All FRs, NFRs, SRs, SFRs, EVRs, PRs baselined | ☐ |
| C1-EX-05 | RTM fully populated | ☐ |
| C1-EX-06 | System architecture reviewed and approved | ☐ |
| C1-EX-07 | RL state, action, reward, and constraint layer architecture frozen | ☐ |
| C1-EX-08 | SUMO architecture documented | ☐ |
| C1-EX-09 | Vision pipeline architecture documented (design only) | ☐ |
| C1-EX-10 | SUMO junction network runs without errors | ☐ |
| C1-EX-11 | Fixed-time baseline controller produces reproducible results | ☐ |
| C1-EX-12 | Experiment scenarios and metrics frozen | ☐ |
| C1-EX-13 | Reproducibility configuration in place | ☐ |

## Research Direction Alignment — Reliability-Aware Study

These sprint/slice activities must remain aligned with the current ARVEXA research anchor:

> Does more traffic information always improve adaptive traffic-signal control when the reliability of that information varies?

The research should treat state richness and observation reliability as explicit experimental variables. R1–R4 representations, controlled degradation modes, matched comparisons, safety/priority constraints, and reproducible evaluation should follow the authoritative documents:

- `docs/research/research-direction.md`
- `docs/architecture/rl-state-representation.md`
- `docs/experiments/research-evaluation-protocol.md`

Do not present pedestrian handling, emergency priority, sensor failure, computer vision, heterogeneous traffic, or RL individually as the novelty. Their role is to create and evaluate the information–reliability decision-making problem.
