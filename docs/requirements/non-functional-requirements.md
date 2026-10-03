# ARVEXA Non-Functional Requirements

## 1. Purpose

These requirements define the quality properties needed for ARVEXA to function as a reproducible research system.

## 2. Reproducibility

### NFR-01 — Experiment Reproducibility
Experiments shall record the configuration required to reproduce each run.

### NFR-02 — Random Seeds
Training and evaluation runs shall record random seeds where stochastic behavior affects results.

### NFR-03 — Version Traceability
Results shall identify the code, model, and configuration version used.

### NFR-04 — Scenario Isolation
Traffic scenarios shall be represented as configuration artifacts rather than hidden source-code constants.

## 3. Safety

### NFR-05 — Safety Constraints
The controller shall never intentionally bypass configured signal-safety constraints.

### NFR-06 — Invalid Action Handling
Invalid learned actions shall be rejected, masked, or transformed into a documented safe action.

### NFR-07 — Pedestrian Clearance
Configured pedestrian-clearance constraints shall be enforced independently of reward optimization.

### NFR-08 — Emergency Safety
Emergency priority shall not bypass required signal-transition safety intervals.

## 4. Modularity

### NFR-09 — Component Separation
The system shall maintain separate modules for state construction, action construction, reward calculation, RL policy, SUMO interaction, perception, and evaluation.

### NFR-10 — Replaceability
The RL algorithm should be replaceable without rewriting the SUMO model.

### NFR-11 — Perception Independence
The controller should consume a defined traffic-state interface rather than directly depending on a particular vision model.

## 5. Maintainability

### NFR-12 — Documentation
Non-obvious research decisions shall be documented.

### NFR-13 — Configuration Management
Hyperparameters, traffic scenarios, reward weights, safety limits, and sensor-failure settings shall be configurable.

### NFR-14 — Testability
Core state, action, reward, simulation, perception, and evaluation components shall have automated or reproducible tests appropriate to their role.

## 6. Performance

### NFR-15 — Simulation Performance
The controller shall operate fast enough for practical training and evaluation on the available research hardware. The exact target shall be measured rather than arbitrarily fixed.

### NFR-16 — Inference Latency
Controller decision latency shall be measurable.

### NFR-17 — Perception Throughput
Vision-processing throughput shall be measured for the selected model and hardware.

## 7. Robustness

### NFR-18 — Observation Robustness
The system shall continue producing a valid control state when supported observation channels are missing.

### NFR-19 — Failure Isolation
A degraded observation source should not cause an uncontrolled software failure.

### NFR-20 — Recovery
Where sensor restoration is modeled, the system shall support returning to normal observations without requiring a full controller restart.

## 8. Experiment Integrity

### NFR-21 — Baseline Consistency
Baseline and ARVEXA comparisons shall use equivalent traffic demand and scenario conditions.

### NFR-22 — Metric Consistency
The same metric definitions shall be used across controllers unless a documented methodological reason requires otherwise.

### NFR-23 — Multiple Runs
Stochastic experiments shall use enough independent runs to characterize variability. The exact number will be fixed in the experiment protocol.

### NFR-24 — No Selective Reporting
Unsuccessful runs, failed configurations, or exclusions shall be recorded with a documented reason.

## 9. Data Management

### NFR-25 — Raw Data Protection
Large raw videos and datasets shall not be committed directly to Git unless an approved storage strategy exists.

### NFR-26 — Data Provenance
Traffic datasets and camera observations shall record source, date/range, preprocessing, and applicable permissions.

### NFR-27 — Privacy
Personally identifiable information visible in camera footage shall be handled according to applicable institutional and legal requirements.

### NFR-28 — Derived Data
Derived traffic counts and calibration datasets shall be stored in reproducible formats with processing metadata.

## 10. Scientific Quality

### NFR-29 — Traceability
Each major result shall be traceable to research objective, requirement, architecture, experiment, metric, and result.

### NFR-30 — Statistical Reporting
Where stochastic variation is material, results shall report suitable measures of variability.

### NFR-31 — Ablation Evidence
Claims about individual ARVEXA components shall be supported by ablation or controlled comparison where feasible.

### NFR-32 — Limitations
The final analysis shall explicitly document limitations, threats to validity, and assumptions.

## 11. Security and Repository Hygiene

### NFR-33 — No Secrets
Credentials, private keys, tokens, and sensitive configuration shall never be committed.

### NFR-34 — Controlled Changes
Changes to the RL state, action space, reward function, safety constraints, and evaluation methodology require team review.

### NFR-35 — Stable Main
The main branch shall remain reproducible and should contain only reviewed changes.

## 12. Portability

### NFR-36 — Environment Definition
Required software versions and dependencies shall be documented.

### NFR-37 — Platform Documentation
The project shall document supported development and experiment environments.

### NFR-38 — Configuration Portability
Traffic scenarios and controller configurations should be portable across compatible experiment environments without manual source modification.

## 13. Observability

### NFR-39 — Experiment Logging
Training and evaluation runs shall produce structured logs sufficient to reconstruct major decisions.

### NFR-40 — Metric Logging
Metrics shall be stored in machine-readable form for later analysis.

### NFR-41 — Failure Logging
Simulation, perception, and experiment failures shall be logged with enough information for diagnosis.

## 14. Research Quality Gate

The system shall not be considered research-ready merely because it executes successfully.

A research-ready implementation must be reproducible, measurable, traceable, safe within the modeled constraints, testable, documented, and suitable for controlled comparison.
