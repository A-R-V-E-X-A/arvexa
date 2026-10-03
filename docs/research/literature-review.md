# Literature Review

## 1. Review Purpose

This literature review establishes the research context for **ARVEXA (Adaptive Resilient Vehicle–pedestrian eXchange Architecture)** and identifies research gaps that directly inform its requirements, architecture, experiments, and evaluation.

The review focuses on adaptive traffic signal control using reinforcement learning, with particular attention to:

1. Reinforcement learning (RL) and deep/multi-agent RL for adaptive traffic signal control.
2. Multi-objective traffic signal control involving efficiency, safety, emissions, fairness, or related objectives.
3. Pedestrian and vulnerable-road-user-aware signal control.
4. Emergency-vehicle priority and signal preemption.
5. Sensor failure, missing data, noisy observations, and robustness.
6. Adversarial robustness and cybersecurity of RL traffic controllers.
7. Vision-based vehicle detection, classification, tracking, and counting.
8. SUMO, simulation-based evaluation, digital twins, and real-world grounding.

The supplied survey reports approximately **141 unique papers surfaced**, of which **113 were curated into the bibliography/database**.

> **Source note:** The counts and coverage statements in this document are derived from the supplied literature-survey material. They are not presented as an independently re-run systematic review.

---

## 2. Review Scope and Search Summary

The supplied survey records the following search activity:

- Searches executed: **18**
  - 7 Consensus searches
  - 1 failed Consensus search
  - 10 alphaXiv searches
- Successful searches: **17**
- Failed searches: **1**
  - Consensus search #8, where the monthly quota was exhausted
- Total unique papers surfaced: approximately **141**
  - 68 via Consensus
  - 74 via alphaXiv
  - 1 cross-listed
- Papers curated into the bibliography: **113**

The survey also notes that the alphaXiv results were predominantly recent **2024–2026 preprints**, and therefore many did not have established citation counts.

The survey identified **adversarial robustness/cybersecurity** as a relatively thin area: the corresponding search returned only four directly on-topic papers. The source material therefore recommends a later, more exhaustive peer-reviewed search for this theme.

---

## 3. Core RL and MARL for Traffic Signal Control

Reinforcement learning has become an established approach for adaptive traffic signal control because a controller can learn a policy that maps observed traffic conditions to control actions rather than relying exclusively on manually designed fixed-time schedules.

The reviewed literature includes both single-agent and multi-agent approaches. Multi-agent reinforcement learning (MARL) is particularly relevant to larger networks because signal controllers can be represented as interacting agents.

### Representative findings from the supplied survey

**Chu et al. (2019), “Multi-Agent Deep Reinforcement Learning for Large-Scale Traffic Signal Control”** is identified as a foundational reference for scalable/decentralized MARL-based traffic signal control. The work uses an actor-critic approach and is relevant to ARVEXA as a possible conceptual baseline for adaptive control.

The survey identifies an important limitation for ARVEXA's problem setting: the foundational efficiency-oriented approaches do not simultaneously address the project's combined requirements for pedestrian safety, emergency-vehicle priority, and sensor-failure tolerance.

**Miletić et al. (2022)** provides a review of reinforcement-learning applications in adaptive traffic signal control and is used by the survey to establish the broader development of RL-based ATSC.

**Michailidis et al. (2025)** reviews applications and innovations in RL-based traffic signal control. The survey notes the continuing emphasis on traffic efficiency while secondary objectives are increasingly being considered.

**Saadi et al. (2025)** surveys reinforcement and deep reinforcement learning for coordination in intelligent traffic-light control. The supplied survey highlights the limited use of real end-to-end traffic data in the reviewed literature, motivating ARVEXA's planned camera-based validation.

**Owais et al. (2026)** compares adaptive traffic signal control strategies using MARL. The supplied survey identifies this work as useful for designing a comparative baseline/evaluation methodology.

**Cai et al. (2024)** investigates enhanced deep RL for adaptive urban traffic signal control and includes robustness/noise-related evaluation. The survey identifies the remaining absence of a combined treatment of pedestrian requirements, emergency priority, and realistic sensor failure.

**Shabestary et al. (2022)** studies adaptive traffic signal control using deep RL with high-dimensional sensory inputs. The survey notes that this work does not provide the same explicit evaluation of missing/faulty observations required by ARVEXA.

### Implication for ARVEXA

The literature supports RL as a suitable foundation for adaptive signal control, but the supplied survey indicates a need to evaluate a broader integrated controller rather than treating traffic efficiency as the only objective.

---

## 4. Multi-Objective Traffic Signal Control

A major theme in the reviewed literature is the movement from single-objective efficiency optimization toward multi-objective traffic signal control.

Common objectives include:

- delay reduction,
- queue reduction,
- throughput,
- emissions or fuel consumption,
- safety,
- fairness,
- and service quality.

The supplied survey identifies **17 curated papers** in the multi-objective RL category.

### Relevance to ARVEXA

ARVEXA extends this direction by explicitly considering:

- vehicle traffic efficiency,
- pedestrian service and safety,
- emergency-vehicle priority,
- signal stability,
- and robustness to degraded sensing.

The research question is therefore not simply whether RL can improve traffic flow, but how multiple competing objectives can be represented, constrained, and evaluated within one controller.

The supplied literature does not establish that all of these dimensions have been jointly evaluated under the same experimental protocol. This is therefore treated as a research gap rather than as an assumption of novelty.

---

## 5. Pedestrian Safety and Vulnerable Road Users

The supplied survey identifies **14 curated papers** under pedestrian safety and vulnerable-road-user-aware signal control.

Pedestrian-aware signal control introduces requirements that are different from vehicle-only optimization. A controller must account for pedestrian demand, crossing service, clearance time, and potential conflicts between vehicle-flow objectives and pedestrian requirements.

For ARVEXA, this motivates explicit state variables and evaluation metrics for pedestrian activity rather than treating pedestrians as an external constraint.

The ARVEXA architecture therefore separates:

- pedestrian demand observation,
- pedestrian service/clearance requirements,
- safety constraints,
- and pedestrian-related evaluation metrics.

The literature review supports this as an important extension of vehicle-centric adaptive signal control.

---

## 6. Emergency-Vehicle Priority

The supplied survey identifies **9 curated papers** dealing with emergency-vehicle priority and signal preemption.

Emergency-vehicle requests introduce a priority-arbitration problem. A controller may need to give an ambulance, fire vehicle, or police vehicle priority while continuing to serve ordinary traffic and pedestrian requirements.

For ARVEXA, emergency priority is therefore modeled as an explicit controller objective/input rather than as a separate system operating independently of the adaptive signal controller.

A key research question is how conflicting priority requests should be handled and how the effect of priority decisions on ordinary traffic should be measured.

The supplied survey specifically identifies **conflicting priority request arbitration** as an important gap.

---

## 7. Sensor Failure, Missing Data, and Robustness

The supplied survey identifies **18 curated papers** under sensor failure, fault tolerance, and robustness to missing/noisy data.

This is particularly important for ARVEXA because a controller trained only on clean observations may behave unpredictably when traffic sensors produce:

- missing values,
- noisy counts,
- incorrect vehicle classifications,
- partially unavailable observations,
- or degraded sensor coverage.

The reviewed literature includes work on noise injection and robustness, but the survey identifies a distinction between generic noise robustness and systematic evaluation of realistic sensor failure modes.

### ARVEXA approach

ARVEXA models a separation between:

```text
True traffic state
       ↓
Observation / sensor model
       ↓
Ideal / noisy / missing / misclassified observation
       ↓
State representation
       ↓
RL controller
```

This allows the controller to be evaluated under controlled degradation rather than relying only on clean simulation observations.

---

## 8. Adversarial Robustness and Cybersecurity

The supplied survey records only **4 directly on-topic papers** in the adversarial robustness/cybersecurity category.

This is explicitly identified as a thin area in the supplied review. The survey recommends re-running this search after the search quota becomes available to obtain a more exhaustive peer-reviewed view.

For ARVEXA, this theme should therefore be treated carefully. The project can evaluate resilience to sensing failures and degraded observations without claiming to provide a complete cybersecurity solution.

Any stronger cybersecurity contribution would require additional literature coverage and a dedicated threat model.

---

## 9. Vision-Based Detection, Classification, Tracking, and Counting

ARVEXA plans to use real camera footage for validation through a vision pipeline.

The intended pipeline is:

```text
Camera footage
      ↓
Frame extraction / preprocessing
      ↓
Vehicle detection
      ↓
Vehicle classification
      ↓
Tracking
      ↓
Region / line definition
      ↓
Counting
      ↓
Time aggregation
      ↓
Traffic statistics
      ↓
SUMO calibration / validation
```

The supplied literature survey treats vision-based vehicle detection and counting as an important component for connecting simulated traffic control with real traffic observations.

The key methodological requirement is to distinguish between:

- **calibration data**, used to construct or tune the SUMO traffic model, and
- **validation data**, used to test whether the calibrated simulation reasonably represents observed traffic.

This separation reduces the risk of using the same observations both to tune and to validate the model.

The review also highlights uncertainty in detection/classification/counting as an important consideration when transferring real observations into simulation.

---

## 10. SUMO, Simulation, Digital Twins, and Real-World Grounding

SUMO provides the controlled experimental environment for ARVEXA.

The supplied survey includes literature on:

- SUMO-based RL traffic control,
- traffic co-simulation,
- digital twins,
- traffic-control simulation,
- and connections between simulation and real-world observations.

The reviewed literature supports simulation as a practical environment for repeatable RL experimentation, but simulation results do not automatically establish real-world validity.

ARVEXA therefore treats real-world grounding as a separate research requirement:

```text
Real junction observations
        ↓
Vision-based traffic statistics
        ↓
SUMO network / demand calibration
        ↓
Controlled RL experiments
        ↓
Baseline comparison
        ↓
Validation against held-out real observations
```

The supplied review identifies this real-world grounding as a meaningful area where existing RL traffic-signal studies can be strengthened.

---

## 11. Emerging LLM and Agentic Traffic-Signal Research

The supplied literature database contains an **Emerging Paradigm: LLM & Agentic Control for Traffic Signals** category with **8 curated papers**.

These papers are relevant as an emerging research direction, but they should not automatically be treated as replacements for established RL approaches.

For ARVEXA, the current architecture remains centered on reinforcement learning and explicit safety/control mechanisms. LLM/agentic approaches may be monitored as related future work rather than introduced into the core controller without evidence that they satisfy the project's safety, reproducibility, and control requirements.

---

## 12. Consolidated Research Gaps

The supplied literature review identifies the following gaps as particularly relevant to ARVEXA:

| Gap | Description | ARVEXA relevance |
|---|---|---|
| G1 | Integrated multi-objective adaptive control | Combines traffic efficiency, pedestrian service/safety, emergency priority, and robustness |
| G2 | Safety constraints alongside learned optimization | Places a safety/action layer between RL decisions and signal commands |
| G3 | Joint pedestrian + emergency + sensor-resilience treatment | Evaluates these requirements within one controller |
| G4 | Priority arbitration under conflicting demands | Studies emergency requests without ignoring normal traffic and pedestrian service |
| G5 | Robustness to degraded observations | Evaluates missing, noisy, misclassified, and partial observations |
| G6 | Heterogeneous mixed-traffic context | Includes vehicle classes relevant to mixed urban traffic |
| G7 | Real-world grounding of SUMO evaluation | Uses real camera observations for calibration/validation |
| G8 | Vision failure and uncertainty | Treats detection/counting uncertainty as part of the real-to-simulation pipeline |
| G9 | Evidence for multi-objective trade-offs | Reports objective-specific metrics rather than relying on one aggregate score |

These gaps should be understood as **research directions identified from the supplied review**, not as universal claims that no other study has addressed any of them.

---

## 13. Representative References

The following references are representative of the supplied survey and literature database. The complete structured bibliography is maintained in:

`docs/sources/literature/literature-database.xlsx`

Representative entries include:

1. Chu et al. (2019), *Multi-Agent Deep Reinforcement Learning for Large-Scale Traffic Signal Control*, IEEE Transactions on Intelligent Transportation Systems.
2. Miletić et al. (2022), *A review of reinforcement learning applications in adaptive traffic signal control*, IET Intelligent Transport Systems.
3. Shabestary et al. (2022), *Adaptive Traffic Signal Control With Deep Reinforcement Learning and High Dimensional Sensory Inputs*, IEEE Transactions on Intelligent Transportation Systems.
4. Cai et al. (2024), *Adaptive urban traffic signal control based on enhanced deep reinforcement learning*, Scientific Reports.
5. Michailidis et al. (2025), *Traffic Signal Control via Reinforcement Learning: A Review on Applications and Innovations*, Infrastructures.
6. Saadi et al. (2025), *A survey of reinforcement and deep reinforcement learning for coordination in intelligent traffic light control*, Journal of Big Data.
7. Owais et al. (2026), *Adaptive Traffic Signal Control Using Multi-Agent Reinforcement Learning: A Comparison of Control Strategies*, Sustainability.

The complete database contains the additional papers, metadata, relevance notes, and project-specific implementable gaps captured during the supplied survey.

---

## 14. Limitations of the Current Review

The supplied survey identifies several limitations:

1. The search was not fully exhaustive.
2. One Consensus search failed because its monthly quota was exhausted.
3. The adversarial-robustness/cybersecurity area was thin and requires another search pass.
4. Many recent alphaXiv sources are preprints and may not yet have established citation records.
5. The literature should be updated before final publication of the ARVEXA research work.
6. Novelty claims should be rechecked against the latest peer-reviewed literature.

Accordingly, this document should be treated as the **current research-planning literature review**, not as the final publication-grade systematic literature review.

---

## 15. Relationship to ARVEXA Research Planning

The literature review directly informs the ARVEXA research-planning chain:

```text
Literature
    ↓
Research Gap
    ↓
Research Questions
    ↓
Research Objectives
    ↓
System Requirements
    ↓
Architecture
    ↓
Implementation Slices
    ↓
Experiments
    ↓
Metrics
    ↓
Results
```

The literature database provides the evidence base for the research-gap and requirement documents, while the experiment plan should use the identified gaps to define controlled comparisons, ablations, failure scenarios, and real-world validation.

---

## 16. Provenance

Primary source for this document:

- Supplied ARVEXA literature-survey document: `Adaptive_Traffic_Signal_RL_Literature_Review.docx`
- Supplied structured bibliography: `Traffic_signal_RL_literature_list (1).xlsx`

The structured bibliography is preserved without replacing its source data in:

`docs/sources/literature/literature-database.xlsx`
