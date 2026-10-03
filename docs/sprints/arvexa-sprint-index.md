# ARVEXA — Sprint & Slice Master Index

> 3 Capstone Phases | 12 Sprints | 72 Slices

---

## Quick Reference

| Phase | Capstone | Sprint | ID Range | Slices | Theme |
|---|---|---|---|---|---|
| 1 | C1 | SPR-01 | C1-S01–S05 | 5 | Research Foundation |
| 1 | C1 | SPR-02 | C1-S06–S12 | 7 | Requirements & Traceability |
| 1 | C1 | SPR-03 | C1-S13–S20 | 8 | Architecture & Experimental Design |
| 1 | C1 | SPR-04 | C1-S21–S32 | 12 | SUMO Baseline & Experiment Plan |
| 2 | C2 | SPR-05 | C2-S01–S09 | 9 | SUMO & Traffic-State Pipeline |
| 2 | C2 | SPR-06 | C2-S10–S18 | 9 | RL Controller |
| 2 | C2 | SPR-07 | C2-S19–S27 | 9 | Multi-Objective & Safety |
| 2 | C2 | SPR-08 | C2-S28–S36 | 9 | Sensor Resilience & Simulation Evaluation |
| 3 | C3 | SPR-09 | C3-S01–S09 | 9 | Computer Vision Pipeline |
| 3 | C3 | SPR-10 | C3-S10–S17 | 8 | Real-to-SUMO Calibration & Validation |
| 3 | C3 | SPR-11 | C3-S18–S27 | 10 | Full ARVEXA Integration |
| 3 | C3 | SPR-12 | C3-S28–S40 | 13 | Final Evaluation & Thesis |

---

## Files

| File | Contents |
|---|---|
| `arvexa-capstone-1-sprint-specs.md` | Sprints 1–4 | Full slice specs for C1-S01 to C1-S32 |
| `arvexa-capstone-2-sprint-specs.md` | Sprints 5–8 | Full slice specs for C2-S01 to C2-S36 |
| `arvexa-capstone-3-sprint-specs.md` | Sprints 9–12 | Full slice specs for C3-S01 to C3-S40 |

Each slice contains: Objective · Inputs · Outputs (with file paths) · Acceptance Criteria (checkboxes) · Dependencies

---

## Full Slice List

### Capstone 1

| ID | Slice Title | Sprint |
|---|---|---|
| C1-S01 | Problem Definition | SPR-01 |
| C1-S02 | Research Questions | SPR-01 |
| C1-S03 | Research Objectives | SPR-01 |
| C1-S04 | Scope, Assumptions & Exclusions | SPR-01 |
| C1-S05 | Literature Evidence Organisation | SPR-01 |
| C1-S06 | Functional Requirements | SPR-02 |
| C1-S07 | Non-Functional Requirements | SPR-02 |
| C1-S08 | Safety Requirements | SPR-02 |
| C1-S09 | Sensor-Failure Requirements | SPR-02 |
| C1-S10 | Emergency-Vehicle Requirements | SPR-02 |
| C1-S11 | Pedestrian Requirements | SPR-02 |
| C1-S12 | Requirements Traceability Matrix | SPR-02 |
| C1-S13 | Overall System Architecture | SPR-03 |
| C1-S14 | RL State Representation | SPR-03 |
| C1-S15 | Action Space | SPR-03 |
| C1-S16 | Reward & Objective Architecture | SPR-03 |
| C1-S17 | Safety & Action Constraint Layer | SPR-03 |
| C1-S18 | SUMO Architecture | SPR-03 |
| C1-S19 | Vision Pipeline Architecture | SPR-03 |
| C1-S20 | Sensor Degradation Model | SPR-03 |
| C1-S21 | Junction Selection | SPR-04 |
| C1-S22 | SUMO Network Construction | SPR-04 |
| C1-S23 | Traffic Demand Model | SPR-04 |
| C1-S24 | Vehicle-Type Model | SPR-04 |
| C1-S25 | Pedestrian Model | SPR-04 |
| C1-S26 | Emergency-Vehicle Model | SPR-04 |
| C1-S27 | Signal-Phase Model | SPR-04 |
| C1-S28 | Baseline Fixed-Time Controller | SPR-04 |
| C1-S29 | SUMO Calibration Plan | SPR-04 |
| C1-S30 | Experiment Scenarios | SPR-04 |
| C1-S31 | Evaluation Metrics | SPR-04 |
| C1-S32 | Reproducibility Configuration | SPR-04 |

### Capstone 2

| ID | Slice Title | Sprint |
|---|---|---|
| C2-S01 | SUMO Environment Wrapper | SPR-05 |
| C2-S02 | Vehicle Detection & State Extraction | SPR-05 |
| C2-S03 | Vehicle Classification / Type State | SPR-05 |
| C2-S04 | Queue Estimation | SPR-05 |
| C2-S05 | Waiting-Time State | SPR-05 |
| C2-S06 | Pedestrian State | SPR-05 |
| C2-S07 | Emergency-Vehicle State | SPR-05 |
| C2-S08 | Sensor-Health State | SPR-05 |
| C2-S09 | Unified State Builder | SPR-05 |
| C2-S10 | RL Environment Interface | SPR-06 |
| C2-S11 | State-Space Implementation | SPR-06 |
| C2-S12 | Phase Action Implementation | SPR-06 |
| C2-S13 | Duration Action Implementation | SPR-06 |
| C2-S14 | Action Validity Constraints | SPR-06 |
| C2-S15 | Reward Implementation | SPR-06 |
| C2-S16 | Training Pipeline | SPR-06 |
| C2-S17 | Model Checkpointing | SPR-06 |
| C2-S18 | Deterministic Evaluation Mode | SPR-06 |
| C2-S19 | Traffic-Efficiency Objective | SPR-07 |
| C2-S20 | Pedestrian-Safety Objective | SPR-07 |
| C2-S21 | Emergency-Priority Objective | SPR-07 |
| C2-S22 | Stability / Signal-Switching Objective | SPR-07 |
| C2-S23 | Robustness Objective | SPR-07 |
| C2-S24 | Multi-Objective Reward Aggregation | SPR-07 |
| C2-S25 | Safety Constraint Layer | SPR-07 |
| C2-S26 | Emergency Priority Arbitration | SPR-07 |
| C2-S27 | Pedestrian Conflict Handling | SPR-07 |
| C2-S28 | Missing Sensor Scenario | SPR-08 |
| C2-S29 | Noisy Sensor Scenario | SPR-08 |
| C2-S30 | Misclassification Scenario | SPR-08 |
| C2-S31 | Partial Sensor Failure | SPR-08 |
| C2-S32 | Degraded Observation Pipeline | SPR-08 |
| C2-S33 | Baseline Comparison | SPR-08 |
| C2-S34 | Repeated-Run Evaluation | SPR-08 |
| C2-S35 | Statistical Result Generation | SPR-08 |
| C2-S36 | Ablation Experiments | SPR-08 |

### Capstone 3

| ID | Slice Title | Sprint |
|---|---|---|
| C3-S01 | Video Ingestion | SPR-09 |
| C3-S02 | Frame Preprocessing | SPR-09 |
| C3-S03 | Vehicle Detection | SPR-09 |
| C3-S04 | Vehicle Classification | SPR-09 |
| C3-S05 | Vehicle Tracking | SPR-09 |
| C3-S06 | Region & Counting Line Definition | SPR-09 |
| C3-S07 | Vehicle Counting | SPR-09 |
| C3-S08 | Traffic-Statistics Aggregation | SPR-09 |
| C3-S09 | Detection Accuracy Evaluation | SPR-09 |
| C3-S10 | Camera Metadata Preparation | SPR-10 |
| C3-S11 | Real Traffic Demand Extraction | SPR-10 |
| C3-S12 | Vehicle-Type Distribution Extraction | SPR-10 |
| C3-S13 | Traffic-Flow Calibration | SPR-10 |
| C3-S14 | SUMO Parameter Calibration | SPR-10 |
| C3-S15 | Real-vs-SUMO Traffic Comparison | SPR-10 |
| C3-S16 | Validation Dataset Preparation | SPR-10 |
| C3-S17 | Calibration / Validation Separation | SPR-10 |
| C3-S18 | Vision → Traffic-State Interface | SPR-11 |
| C3-S19 | Sensor Uncertainty Propagation | SPR-11 |
| C3-S20 | Vision Degradation Handling | SPR-11 |
| C3-S21 | Emergency-Vehicle Detection / Input | SPR-11 |
| C3-S22 | Pedestrian Input Integration | SPR-11 |
| C3-S23 | End-to-End Controller Integration | SPR-11 |
| C3-S24 | Experiment Automation | SPR-11 |
| C3-S25 | Configuration Management | SPR-11 |
| C3-S26 | Result Logging | SPR-11 |
| C3-S27 | Reproducibility Pipeline | SPR-11 |
| C3-S28 | Final Baseline Experiments | SPR-12 |
| C3-S29 | Final ARVEXA Experiments | SPR-12 |
| C3-S30 | Multi-Objective Trade-Off Analysis | SPR-12 |
| C3-S31 | Sensor-Failure Evaluation (Final) | SPR-12 |
| C3-S32 | Pedestrian-Safety Evaluation (Final) | SPR-12 |
| C3-S33 | Emergency-Priority Evaluation (Final) | SPR-12 |
| C3-S34 | Ablation Study (Final) | SPR-12 |
| C3-S35 | Statistical Analysis (Final) | SPR-12 |
| C3-S36 | Final Result Visualisation | SPR-12 |
| C3-S37 | Reproducibility Package | SPR-12 |
| C3-S38 | Final Documentation | SPR-12 |
| C3-S39 | Thesis / Report | SPR-12 |
| C3-S40 | Final Demonstration | SPR-12 |

---

## Critical Dependency Chains

The following chains represent the longest dependency paths through the project. Delays here cascade across all downstream slices.

```
C1-S01 (Problem Definition)
  └─ C1-S02 (RQs)
       └─ C1-S03 (ROs)
            └─ C1-S06 (FRs)
                 └─ C1-S08 (Safety Reqs)
                      └─ C1-S17 (Constraint Layer Spec)
                           └─ C2-S25 (Constraint Layer Implementation)
                                └─ C2-S26 (Emergency Arbitration)
                                └─ C2-S27 (Pedestrian Handling)

C1-S14 (State Representation)
  └─ C2-S09 (Unified State Builder)
       └─ C2-S10 (RL Env Interface)
            └─ C2-S16 (Training Pipeline)
                 └─ C2-S17 (Checkpointing)
                      └─ C2-S18 (Evaluation)
                           └─ C3-S29 (Final ARVEXA Experiments)

C1-S22 (SUMO Network)
  └─ C1-S28 (Fixed-Time Baseline)
  └─ C1-S23 (Traffic Demand)
       └─ C3-S13 (Calibration)
            └─ C3-S28 (Final Baseline Experiments)

C3-S03 (Vehicle Detection)
  └─ C3-S04 (Classification)
       └─ C3-S05 (Tracking)
            └─ C3-S07 (Counting)
                 └─ C3-S08 (Traffic Statistics)
                      └─ C3-S18 (Vision-State Interface)
                           └─ C3-S23 (End-to-End Pipeline)
```

---

## Requirement Category Coverage Map

| Slice | FR | NFR | SR | SFR | EVR | PR |
|---|---|---|---|---|---|---|
| C1-S06 | ✓ | | | | | |
| C1-S07 | | ✓ | | | | |
| C1-S08 | | | ✓ | | | |
| C1-S09 | | | | ✓ | | |
| C1-S10 | | | | | ✓ | |
| C1-S11 | | | | | | ✓ |
| C2-S14 | | | ✓ | | | |
| C2-S25 | | | ✓ | | | |
| C2-S26 | | | | | ✓ | |
| C2-S27 | | | | | | ✓ |
| C2-S08 | | | | ✓ | | |
| C2-S28–32 | | | | ✓ | | |
| C3-S20 | | | | ✓ | | |
| C3-S21 | | | | | ✓ | |
| C3-S22 | | | | | | ✓ |
| C3-S31 | | | | ✓ | | |
| C3-S32 | | | | | | ✓ |
| C3-S33 | | | | | ✓ | |
