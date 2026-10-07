# ARVEXA Research Direction

## 1. Research anchor

ARVEXA is centered on one question:

> **Does more traffic information always improve adaptive traffic-signal control when the reliability of that information varies?**

The project therefore studies the relationship:

**state richness × observation reliability → control performance**

The key research object is not a particular RL algorithm. The key object is the **control value of traffic-state information under imperfect observation**.

## 2. Why this is a research problem

Adaptive signal control can use progressively richer information. However, richer information also creates more opportunities for incorrect, missing, noisy, stale, or semantically wrong observations.

For example, a controller may know the total number of vehicles accurately while receiving incorrect vehicle-type labels. A richer representation can therefore contain more information in principle but less trustworthy information in practice.

ARVEXA asks whether the benefit of additional state information remains positive as observation reliability falls.

## 3. State richness ladder

| Level | Representation | Purpose |
|---|---|---|
| R1 | Counts, queues, signal state | Establish basic adaptive control |
| R2 | R1 + vehicle-type composition | Test value of heterogeneous traffic semantics |
| R3 | R2 + pedestrian/emergency state | Test safety and priority context |
| R4 | R3 + explicit reliability/quality information | Test reliability-aware decision making |

The levels must be evaluated under matched traffic demand and geometry.

## 4. Observation degradation

The experiment should distinguish at least four degradation modes:

1. **Missing observations** — information is unavailable.
2. **Measurement noise** — values deviate from the underlying state.
3. **Misclassification** — the total observation may be available while semantic vehicle labels are incorrect.
4. **Partial failure** — selected observation channels become unavailable or unreliable.

Recommended severity levels are 0%, 10%, 25%, 50%, and 75%, subject to feasibility and calibration.

The exact degradation mechanism must be documented so every experiment is reproducible.

## 5. Main hypothesis

> Richer state representations improve control under reliable observations, but the marginal benefit of richer information decreases as observation reliability deteriorates and may become negative under sufficiently severe degradation.

Both confirmation and rejection of this hypothesis are scientifically useful results.

## 6. Signature analysis

ARVEXA should produce an **information–robustness curve** showing control performance as a function of:

- representation richness,
- observation reliability,
- degradation type,
- degradation severity.

### Information Benefit

`IB(Rx, Rref, ρ) = [J(Rx,ρ) - J(Rref,ρ)] / |J(Rref,ρ)|`

where `J` is the selected performance utility and `ρ` represents observation reliability.

### Degradation Ratio

`DR = [J(clean) - J(degraded)] / |J(clean)|`

The sign and interpretation must be defined consistently for the chosen metric. For metrics where lower is better, the formulation must be adjusted.

## 7. Reliability-aware controller

R4 should not simply append a reliability number without testing its value.

The reliability-aware branch should investigate whether the controller can use observation-quality information to:

- reduce reliance on unreliable state components,
- fall back to safer/coarser information,
- preserve action stability,
- avoid overreacting to corrupted observations.

The exact mechanism should remain modular so it can be compared against the non-reliability-aware controller.

## 8. Safety boundary

Pedestrian safety and emergency priority are not treated as claims of novelty by themselves.

They define constraints and decision contexts that must remain valid while information quality changes.

The architecture therefore separates:

**RL decision generation → deterministic safety/priority validation → signal actuation**

The deterministic layer is authoritative for hard safety rules.

## 9. Heterogeneous traffic

Vehicle-type information is especially important because semantic errors can occur even when aggregate counts remain approximately correct.

This enables a meaningful experiment:

> Does semantic richness remain useful when semantic reliability is poor?

This is one of the strongest ARVEXA-specific experimental cases.

## 10. Planned contribution

The intended contribution is:

1. A controlled state-richness ladder for adaptive signal control.
2. A reproducible observation-degradation model.
3. A systematic evaluation of richness × reliability interaction.
4. Quantification of when additional information helps, saturates, or becomes harmful.
5. Evaluation of an explicit reliability-aware controller against matched baselines.
6. Camera-derived observation quality used to test whether simulation assumptions are realistic.

## 11. Novelty wording

Use:

> “Our review did not identify a study that systematically evaluates the interaction between state-representation richness and multiple observation-error modes under heterogeneous mixed traffic.”

Avoid unsupported claims such as:

- “first ever,”
- “no previous work exists,”
- “the first RL controller to handle sensor failure,”
- “novel because it combines pedestrians, emergency vehicles and computer vision.”

## 12. Patent investigation direction

If patent protection is pursued, the potentially protectable direction should focus on a technical control mechanism rather than the broad combination of known technologies.

A candidate mechanism is:

**observation-quality estimation → reliability-aware information selection/weighting/fallback → adaptive signal action generation → safety/priority validation**

Patentability is not established by this document. A formal patent prior-art search and professional legal assessment are required, and public disclosure timing should be considered before filing.

## 13. Experimental progression

The minimum defensible progression is:

1. Fixed-time and actuated baselines.
2. Standard vehicle-only RL.
3. R1–R3 state representations under clean observations.
4. R1–R3 under controlled degradation.
5. Information–robustness analysis.
6. R4 reliability-aware controller.
7. Safety/emergency stress tests.
8. Camera-based observation validation.

R4 should follow successful completion of R1–R3 experiments.
