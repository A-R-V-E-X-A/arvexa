# ARVEXA Novelty Falsification Audit — October 2026

## Status and purpose

**Status: provisional research audit; novelty not established.** This document records the strongest overlaps found in the current search and defines what must be tested before ARVEXA changes its official research claim. It is not a systematic review, exhaustive patent search, or legal opinion.

The current project question remains:

> When observation reliability varies, does adding richer traffic-state information continue to improve adaptive signal-control performance, or can additional unreliable information reduce control quality?

The more specific candidate question is whether *temporally correlated, vehicle-class-dependent visual errors* propagate differently through state representation and signal decisions than independent errors with the same average error rate—and whether an explicit mitigation improves control under real-time constraints.

## 1. Closest overlaps and implications

| Prior work | Overlap with ARVEXA | What it means for novelty |
|---|---|---|
| Bodagala & Bodagala, **UCATSC** (2026), [arXiv:2602.07784](https://arxiv.org/abs/2602.07784) | Vision-based partial observability, belief state, uncertainty-aware signal decisions, predictive safety and starvation constraints | Strong direct overlap with generic uncertainty-aware traffic control. ARVEXA must not present “use uncertainty in signal control” or a safety filter alone as novel. Compare its assumptions, state variables, action evaluation and constraints directly before choosing a distinct method. |
| Sulistiawan et al., **Evaluating the Robustness of Deep Q-Network Variants Against Visual Perception Errors in Traffic Signal Control** (ICSMech 2026), [DOI:10.1109/icsmech69390.2026.11647148](https://doi.org/10.1109/icsmech69390.2026.11647148) | Tests RL traffic controllers under visual-perception errors associated with visibility/fog | Directly overlaps with the broad claim that visual errors affect RL signal control. The publicly surfaced abstract is insufficient to establish whether it studies class-dependent errors, temporal persistence, matched error rates, or error propagation into action changes. Obtain the full paper before making a distinction claim. |
| T-REX, **Robustness of RL-based traffic signal control under incidents** (2026), [paper](https://link.springer.com/article/10.1186/s12544-026-00841-1), [code](https://github.com/MLSM-at-DTU/T-REX) | Open SUMO framework and robustness metrics for disruption-induced distribution shifts | Generic robustness benchmarking, reproducibility and degradation metrics are not novel. T-REX focuses on network incidents and driver response, not necessarily camera-semantic errors; verify the code and paper scope before treating it as a baseline. |
| PAIR-VLA, **What to Ignore, What to React** (2026), [arXiv:2605.13105](https://arxiv.org/abs/2605.13105) | Uses paired visual variants and action invariance/sensitivity objectives in RL fine-tuning | Action invariance under visual changes is not a new idea in general. This is robotics/VLA rather than traffic signal control, but it is relevant adjacent prior art. ARVEXA must define a traffic-specific contribution beyond “keep actions stable under visual perturbations.” |
| DEEP, **The Decision Value of Perception Compute** (2026), [arXiv:2609.35910](https://arxiv.org/abs/2609.35910) | Values additional perception computation by its downstream decision impact under a budget | Generic decision-value-based perception escalation is not novel. A deadline-aware escalation gate needs a distinct, measurable traffic-control contribution and comparison against a DEEP-inspired baseline. |
| PedSLight (2026), [Frontiers article](https://doi.org/10.3389/ffutr.2026.1953597) | Pedestrian-aware RL signal control and vehicle/pedestrian safety-efficiency trade-offs | Pedestrian-aware multi-objective RL is not a standalone novelty claim. Keep pedestrian service and safety as constraints/evaluation dimensions unless a specific new result is demonstrated. |
| Rodrigues & Azevedo, **Robust RL for TSC under demand surges, incidents, sensor failures** (2019), [arXiv:1904.08353](https://arxiv.org/abs/1904.08353) | Robustness to disruptions and sensor failures | Generic sensor-failure tolerance is established prior art. |

## 2. Current novelty assessment

### Claims that are not defensible by themselves

- Combining RL, computer vision, heterogeneous traffic, pedestrian safety and emergency priority.
- Testing a signal controller under noisy or missing observations in general.
- Adding an observation-confidence/reliability vector to the state.
- Using action stability or confidence thresholds as a standalone mechanism.
- Evaluating robustness in SUMO without a distinct method or carefully controlled evidence.

### Candidate distinction to investigate—not yet claim

> **The interaction between structured visual-error dynamics and traffic-state semantics:** at the same average observation error rate, do temporally persistent errors and vehicle-class confusion cause different downstream signal-action changes and safety/efficiency outcomes than independent errors? Can a simple reliability-aware state representation or mitigation detect and reduce this effect without unacceptable latency or safety trade-offs?

This candidate is narrower than the original integrated-system claim. It is a *testable hypothesis*, not a validated literature gap.

## 3. What remains unknown

The current search does not yet establish whether the closest traffic-control studies already include all of the following:

1. A separate confusion model for vehicle classes relevant to heterogeneous traffic.
2. Temporal persistence/correlation of missed detections, class confusion, tracking loss, stale frames or lane/movement assignment errors.
3. Comparisons at matched average error rates so temporal structure is not confounded with overall error severity.
4. Measurement of the propagation chain from perception error to state representation, chosen phase/duration, and downstream outcome.
5. Matched comparisons of a reliability-aware method against simple confidence thresholds and uncertainty-aware control.
6. Explicit latency/deadline accounting alongside traffic and safety outcomes.

These are the exact items to verify in full texts, supplements, and code. Absence from an abstract is not evidence of absence from a paper.

## 4. Required prior-art audit before final novelty wording

For each closest paper, record:

- Full bibliographic details and publication status.
- Exact observation/state representation.
- Error types, temporal model, severity calibration and whether errors are correlated.
- Controller and action space.
- Safety constraints and pedestrian/emergency treatment.
- Junction/network, traffic mix, camera assumptions and evaluation scenarios.
- Baselines, seeds, metrics, ablations and statistical analysis.
- Available implementation and whether it can be run or faithfully approximated.
- What ARVEXA would test that is genuinely not already tested.

For patents, search claims—not only titles or abstracts—for sensor-error modeling, reliability-aware information selection, adaptive signal decisions and fallback behavior. This audit is not a patentability or freedom-to-operate opinion.

## 5. Go/no-go decision

**Proceed with the candidate gap only if all conditions hold:**

1. Full-text/code inspection finds a specific distinction not already evaluated by the closest traffic-control work.
2. A pilot reproduces the claimed phenomenon under matched error rates and paired scenario seeds.
3. The phenomenon changes a meaningful control outcome—not merely an internal representation or action-distribution statistic.
4. A proposed mitigation beats strong simple baselines on predeclared metrics, or produces a useful Pareto trade-off.
5. Improvements persist across multiple seeds and held-out demand conditions, with confidence intervals/effect sizes reported.
6. Gains do not depend on hidden access to simulator ground truth at decision time.

**Change direction or narrow the claim** if an existing method already evaluates the same error dynamics, the effect disappears under matched comparisons, or the mitigation does not outperform simpler baselines.

## 6. Public sources checked

- UCATSC: https://arxiv.org/abs/2602.07784
- Visual-perception error study: https://doi.org/10.1109/icsmech69390.2026.11647148
- T-REX paper: https://link.springer.com/article/10.1186/s12544-026-00841-1
- T-REX code: https://github.com/MLSM-at-DTU/T-REX
- PAIR-VLA: https://arxiv.org/abs/2605.13105
- DEEP: https://arxiv.org/abs/2609.35910
- PedSLight: https://doi.org/10.3389/ffutr.2026.1953597
- Robust RL under disruptions/sensor failures: https://arxiv.org/abs/1904.08353

**Important:** URLs and abstracts are discovery evidence, not a substitute for a full-text review. Recheck publication status and versions at the time of final submission.
