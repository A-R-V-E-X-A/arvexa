# ARVEXA Literature References

This file provides a human-readable reference index for the ARVEXA research project.

The complete structured literature database is maintained in:

`docs/sources/literature/literature-database.xlsx`

The entries below are representative references explicitly identified in the supplied literature survey. The complete 113-paper dataset should be treated as the authoritative structured bibliography for the current research-planning stage.

## Core Reinforcement Learning and Adaptive Traffic Signal Control

### Chu et al. (2019)

**Title:** Multi-Agent Deep Reinforcement Learning for Large-Scale Traffic Signal Control  
**Venue:** IEEE Transactions on Intelligent Transportation Systems  
**Year:** 2019  
**Relevance to ARVEXA:** Foundational scalable/decentralized MARL approach for traffic signal control. Relevant as a conceptual baseline for adaptive control.  
**Gap identified in supplied survey:** Does not jointly address fault tolerance, pedestrian requirements, and emergency-vehicle priority in the ARVEXA problem setting.

### Miletić et al. (2022)

**Title:** A review of reinforcement learning applications in adaptive traffic signal control  
**Venue:** IET Intelligent Transport Systems  
**Year:** 2022  
**Relevance to ARVEXA:** Provides broad review context for RL-based adaptive traffic signal control.  
**Gap identified in supplied survey:** Supports the need to investigate combinations of safety, robustness, and priority handling.

### Shabestary et al. (2022)

**Title:** Adaptive Traffic Signal Control With Deep Reinforcement Learning and High Dimensional Sensory Inputs  
**Venue:** IEEE Transactions on Intelligent Transportation Systems  
**Year:** 2022  
**Relevance to ARVEXA:** Relevant to high-dimensional traffic-state representation for adaptive signal control.  
**Gap identified in supplied survey:** Does not provide the same explicit missing/faulty sensor evaluation planned for ARVEXA.

### Cai et al. (2024)

**Title:** Adaptive urban traffic signal control based on enhanced deep reinforcement learning  
**Venue:** Scientific Reports  
**Year:** 2024  
**Relevance to ARVEXA:** Relevant to enhanced DRL and robustness/noise evaluation in adaptive urban traffic signal control.  
**Gap identified in supplied survey:** Does not jointly evaluate realistic sensor failure, pedestrian requirements, and emergency-vehicle priority.

### Michailidis et al. (2025)

**Title:** Traffic Signal Control via Reinforcement Learning: A Review on Applications and Innovations  
**Venue:** Infrastructures  
**Year:** 2025  
**Relevance to ARVEXA:** Review of RL traffic-signal-control applications and emerging innovations.  
**Gap identified in supplied survey:** Highlights the continued emphasis on traffic efficiency while secondary objectives are increasingly explored.

### Saadi et al. (2025)

**Title:** A survey of reinforcement and deep reinforcement learning for coordination in intelligent traffic light control  
**Venue:** Journal of Big Data  
**Year:** 2025  
**Relevance to ARVEXA:** Provides survey-level context for coordinated RL-based traffic-light control.  
**Gap identified in supplied survey:** Limited real end-to-end traffic-data validation motivates ARVEXA's camera-grounded validation.

### Owais et al. (2026)

**Title:** Adaptive Traffic Signal Control Using Multi-Agent Reinforcement Learning: A Comparison of Control Strategies  
**Venue:** Sustainability  
**Year:** 2026  
**Relevance to ARVEXA:** Relevant to comparative evaluation of MARL/control strategies and baseline design.

---

## Literature Themes Represented in the Full Database

The supplied structured bibliography groups the curated literature into the following major themes:

| Theme | Curated papers |
|---|---:|
| Core DRL & MARL Traffic Signal Control (Foundations) | 15 |
| Emerging Paradigm: LLM & Agentic Control for Traffic Signals | 8 |
| Multi-Objective RL (Efficiency + Safety + Emissions + Fairness) | 17 |
| Pedestrian Safety & Vulnerable Road User (VRU)-Aware Signal Control | 14 |
| Emergency Vehicle Priority & Signal Preemption | 9 |
| Sensor Failure, Fault Tolerance & Robustness to Missing/Noisy Data | 18 |
| Adversarial Robustness & Cybersecurity of RL Traffic Controllers | 4 |

The supplied survey reports **113 curated papers overall**. The complete workbook should be consulted for the remaining entries and their source-specific metadata.

---

## Reference Metadata Policy

For each paper, the structured literature database records, where available:

- Paper number
- Sub-area
- Title
- Authors
- Publication year
- Venue
- Citation count reported by the source
- Search source
- URL
- Relevance note
- Implementable research gap for ARVEXA
- Gap importance

Citation counts are retained as reported in the supplied source and should not be interpreted as current live citation counts.

---

## Research-Use Categories

The literature is used in ARVEXA for four purposes:

### 1. Research context

Establish the development of RL-based adaptive traffic signal control and related traffic-management methods.

### 2. Gap identification

Identify limitations and under-explored combinations relevant to ARVEXA, particularly:

- integrated multi-objective control,
- pedestrian safety,
- emergency priority,
- sensor degradation,
- heterogeneous traffic,
- real-world grounding,
- and robustness.

### 3. Design decisions

Inform the selection of:

- state variables,
- action representation,
- reward/objective design,
- safety constraints,
- sensor-degradation scenarios,
- baselines,
- and evaluation metrics.

### 4. Experimental justification

Provide evidence for why ARVEXA should compare multiple objectives, failure scenarios, and baseline controllers rather than reporting only a single average traffic-efficiency result.

---

## Important Source-Quality Note

The supplied survey combines peer-reviewed publications and recent preprints. In particular, the audit notes that many alphaXiv sources are recent 2024–2026 preprints.

Before using this bibliography for a final academic publication, the team should:

1. verify publication status,
2. verify DOI/official publisher information,
3. update citation metadata,
4. remove duplicates where necessary,
5. perform the missing adversarial-robustness/cybersecurity search,
6. and re-check novelty claims against current peer-reviewed literature.

---

## Full Structured Bibliography

For the full 113-paper structured bibliography, use:

`docs/sources/literature/literature-database.xlsx`

The workbook is intentionally retained as the machine-readable/project-working reference rather than duplicating all 113 entries manually in this Markdown file.
