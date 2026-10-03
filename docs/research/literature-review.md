# ARVEXA Literature Review

## 1. Review Purpose

The literature review establishes the technical and research foundation for ARVEXA.

The review was organized around:

1. reinforcement learning for adaptive traffic signal control;
2. multi-objective traffic-signal optimization;
3. pedestrian-aware signal control;
4. emergency-vehicle priority and signal preemption;
5. sensor failure, missing data, and robust control;
6. safe and interpretable reinforcement learning;
7. vision-based vehicle detection and counting;
8. SUMO, digital twins, and simulation-to-real validation.

The survey source reports an audit of 18 search themes, approximately 141 papers surfaced, and 113 papers curated into its bibliography.

## 2. Reinforcement Learning for Traffic Signal Control

RL traffic-signal control models an intersection as a sequential decision process. A controller observes traffic state, selects an action, receives feedback, and updates a policy.

Typical objectives include minimizing waiting time, queue length, travel time, and stops while increasing throughput.

The literature demonstrates the usefulness of RL and deep RL, but also highlights state representation, reward design, training stability, generalization, safety, sensing uncertainty, and simulation-to-real transfer as practical challenges.

The survey identifies Michailidis et al. (2025) as a broad recent review and Chu et al. (2019) as foundational multi-agent deep-RL work.

**ARVEXA implication:** RL is the adaptive decision layer, but the research extends the problem beyond traffic efficiency.

## 3. Multi-Objective Traffic Signal Control

Multi-objective RL has been used to combine efficiency with safety, emissions, fairness, and other objectives.

Zhang et al. (2024) is highlighted in the survey as a particularly relevant example combining safety, efficiency, and decarbonization.

The literature shows that objective weighting matters and that a single aggregate score can hide trade-offs.

**ARVEXA implication:** objective-specific metrics must be reported in addition to reward.

## 4. Pedestrian-Aware Traffic Signal Control

Pedestrian-aware research introduces pedestrian behavior, crossing demand, or pedestrian safety into traffic-signal optimization.

Relevant studies identified in the survey include Han et al. (2022), Yazdani et al. (2023), Xu et al. (2023), Ren et al. (2025), and Nam et al. (2026).

**Observed limitation:** pedestrian control is often treated as a dedicated objective or scenario rather than combined with sensor degradation and emergency priority.

**ARVEXA implication:** pedestrian demand and safety constraints should be part of the central controller.

## 5. Emergency-Vehicle Priority

Emergency traffic-signal research commonly uses rule-based preemption or learned priority/control policies.

The survey highlights EMVLight by Su et al. as a major reference for multi-agent emergency-vehicle routing and signal control and Cao et al. (2022) for conflicting-direction emergency vehicles.

The central trade-off is:

Emergency response versus delay imposed on other traffic.

**ARVEXA implication:** emergency priority should be measured independently and its effect on other traffic should also be reported.

## 6. Sensor Failure and Missing Data

The reviewed literature includes missing-data-aware RL, fault-tolerant control, observation reconstruction, robust MARL, distributionally robust control, and noisy traffic sensing.

The survey identifies Reinforcement Learning Approaches for Traffic Signal Control under Missing Data as a direct lineage and discusses recent robust-control work.

It also highlights İlyas et al. (2025) as a relevant example involving real data, a SUMO digital twin, sensor-failure fallback, and forecasting/RL components.

**ARVEXA implication:** evaluate whether degraded observations preserve the overall traffic-control objectives, not only whether missing data can be reconstructed.

## 7. Safe and Interpretable RL

The survey identifies Gu et al. (2024) on safe RL, Li et al. (2019) on formal methods and interpretable RL, Farzanegan et al. (2025) on safety-aware deep RL, and Glanois et al. (2021) on interpretable RL.

**ARVEXA implication:** signal safety should be enforced by explicit constraints around the learned policy. The project does not need to solve the entire theoretical safe-RL problem.

## 8. Vision-Based Vehicle Detection and Counting

Computer vision provides a practical mechanism for obtaining traffic observations from existing camera infrastructure.

The survey covers vehicle detection, classification, tracking, and counting and highlights Song et al. (2019) as an important reference.

Known limitations include occlusion, low light, dense traffic, viewpoint, and classification errors.

**ARVEXA implication:** the vision pipeline provides traffic statistics for calibration and validation, but its outputs should not automatically be treated as perfect ground truth.

## 9. SUMO and Simulation Validation

SUMO is widely used for reproducible traffic-signal experiments, but its value depends on model calibration.

The survey identifies simulation-to-real and digital-twin work including Sim2Signal (2026), Traffic Co-Simulation Framework Empowered by Infrastructure Camera Sensing and Reinforcement Learning (2024), and Digital Twins for Intelligent Intersections: A Literature Review (2025).

**ARVEXA implication:** calibrate the SUMO environment against observations from the selected real-world junction.

## 10. Heterogeneous Traffic

ARVEXA focuses on mixed traffic containing vehicle categories such as two-wheelers, cars, auto-rickshaws, buses, trucks, and emergency vehicles.

Different classes can affect lane occupancy, queue discharge, and intersection demand.

The survey identifies heterogeneous mixed traffic as underrepresented relative to standardized simulation environments.

**ARVEXA implication:** vehicle type should be represented in the state where data quality permits, and its contribution should be tested through ablation.

## 11. Literature Synthesis

| Research area | Maturity in reviewed literature | ARVEXA relevance |
|---|---|---|
| RL traffic signal control | High | Core control method |
| Multi-objective RL | High and active | Core optimization framework |
| Pedestrian-aware control | Active | Safety/service objective |
| Emergency priority | Active | Priority objective |
| Sensor-failure robustness | Emerging/active | Resilience objective |
| Safe RL | Mature in broader control | Safety layer |
| Vision-based counting | Mature but imperfect | Real-data observation |
| SUMO simulation | Widely used | Experimental environment |
| Sim-to-real validation | Less common | Validation contribution |
| Full integrated framework | Limited evidence | Main research gap |

## 12. Initial Core References

1. Chu et al. (2019), Multi-Agent Deep Reinforcement Learning for Large-Scale Traffic Signal Control.
2. Michailidis et al. (2025), Traffic Signal Control via Reinforcement Learning: A Review on Applications and Innovations.
3. Zhang et al. (2024), Multi-objective deep reinforcement learning approach for adaptive traffic signal control system with concurrent optimization of safety, efficiency, and decarbonization.
4. Su et al. (2021/2022), EMVLight: a Multi-agent Reinforcement Learning Framework for an Emergency Vehicle Decentralized Routing and Traffic Signal Control System.
5. Cao et al. (2022), A Gain With No Pain: Exploring Intelligent Traffic Signal Control for Emergency Vehicles.
6. Han et al. (2022), Deep Reinforcement Learning for Intersection Signal Control Considering Pedestrian Behavior.
7. Yazdani et al. (2023), Intelligent vehicle pedestrian light: A deep reinforcement learning approach for traffic signal control.
8. Ren et al. (2025), Two-step deep reinforcement learning for traffic signal control to improve pedestrian safety using connected vehicle data.
9. Gu et al. (2024), A Review of Safe Reinforcement Learning: Methods, Theories, and Applications.
10. Glanois et al. (2021), A survey on interpretable reinforcement learning.
11. Li et al. (2019), A formal methods approach to interpretable reinforcement learning for robotic planning.
12. Song et al. (2019), Vision-based vehicle detection and counting system using deep learning in highway scenes.
13. Reinforcement Learning Approaches for Traffic Signal Control under Missing Data (2023).
14. İlyas et al. (2025), traffic-management/digital-twin work involving sensor-failure fallback and RL.
15. Traffic Co-Simulation Framework Empowered by Infrastructure Camera Sensing and Reinforcement Learning (2024).
16. Sim2Signal: Sim-to-Real Benchmarks for Traffic Signal Control (2026).
17. Digital Twins for Intelligent Intersections: A Literature Review (2025).
18. SIGMA: Symmetry-aware, Intelligent, Geometric, Multi-objective Adaptive Control for Robust, Dependable Traffic Management (2026).

## 13. Review Limitations

The survey is a strong planning foundation but is not a guarantee of exhaustive literature coverage.

The audit records that one planned adversarial-robustness search was affected by a search quota and that subsequent searches used another source. Some recent sources are preprints.

Therefore:

- update the literature before publication;
- distinguish peer-reviewed papers from preprints;
- do not use citation counts as a quality score;
- recheck novelty against current literature.

## 14. Literature-to-ARVEXA Decision

The literature supports the following direction:

Literature → established RL methods → multi-objective control → explicit safety constraints → heterogeneous traffic → emergency priority → degraded sensing → real-data-grounded SUMO evaluation.

The contribution will ultimately be determined by the exact implementation and experimental evidence.
