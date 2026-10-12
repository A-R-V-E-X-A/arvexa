# ARVEXA Option B: Novelty Falsification Update — 12 October 2026

## Decision summary

**Status: novelty is not established. The broad Option B claim is at high risk of being already covered.**

Candidate Option B: when camera-derived traffic estimates and connected-vehicle (V2X) observations disagree, estimate whether that disagreement can change the preferred signal action, and use that information to improve control over fixed fusion and reliability-weighted fusion.

This is a research hypothesis, not a novelty claim. The current evidence does not justify calling it highly novel or publication-ready.

## New high-risk prior art found

1. **Płaczek (2012), “Selective data collection in vehicular networks for traffic control applications,” Transportation Research Part C 23, 14–28.** The method explicitly estimates uncertainty in traffic-control decisions using predictive traffic simulation and requests new V2X data when the best control action is ambiguous. This substantially overlaps with the general idea of action-decision uncertainty guiding observation acquisition. ARVEXA must not claim that decision uncertainty for signal control, or requesting additional V2X information when decisions are uncertain, is new. DOI: https://doi.org/10.1016/j.trc.2011.12.007; preprint: https://arxiv.org/abs/1112.4620.

2. **Hong, “CIoT-PressLight: Smart Pole and V2X Assisted Multi-Agent Reinforcement Learning for Adaptive Urban Traffic Signal Control” (SSRN preprint; not peer reviewed according to the paper).** The described method fuses camera/radar/V2X observations, explicitly models sensing noise, message frequency, latency and packet loss, and uses reliability-weighted fusion in a multi-agent RL controller. This overlaps strongly with multimodal camera/V2X fusion and communications robustness. Source: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7434523. Reported performance is author-reported and has not been independently reproduced by ARVEXA.

3. **Bodagala & Bodagala, “Uncertainty-Aware Counterfactual Traffic Signal Control with Predictive Safety and Starvation-Avoidance Constraints Using Vision-Based Sensing” (UCATSC, 2026 preprint).** The paper uses belief-space counterfactual rollouts to evaluate candidate signal actions under vision uncertainty, with explicit safety and starvation constraints. This overlaps with evaluating alternative actions under uncertain traffic state. Source: https://arxiv.org/abs/2602.07784.

4. **Płaczek and UCATSC together make a simple “action-disagreement score” insufficient as a novelty argument.** A new metric name or combining belief-state action evaluation with camera/V2X fusion does not, by itself, demonstrate a new method.

## What the candidate contribution must become to survive

Investigate a narrower hypothesis:

> Under matched marginal perception error rates and matched information/compute budgets, do temporally correlated, vehicle-class-dependent errors and cross-source disagreement produce *predictable action-relevant failure modes* that are not captured by standard reliability-weighted fusion or generic belief-state action evaluation—and does a specific mitigation reduce those failures?

This wording remains provisional. It may also fail the full prior-art audit.

A defensible contribution would need to specify all of the following:
- A measurable failure mechanism, not only a new score.
- A causal experimental intervention that isolates error temporal structure and vehicle-class confusion at matched marginal error rates.
- A controller or estimator with a technically explicit difference from reliability weighting and belief-space counterfactual control.
- An improvement in a predeclared primary metric across paired seeds, with uncertainty intervals and practical effect size.
- No unacceptable regression in pedestrian constraints, emergency response, phase legality, runtime or fallback behavior.
- A complete comparison to closest prior work, including the 2012 decision-uncertainty data-collection method.

## Existing preliminary result — negative and non-publication-grade

A previously run standalone toy queueing pilot (not SUMO, not TraCI, and not an ARVEXA implementation) reported the following mean total queues:

| Scenario | Fixed fusion | Reliability-weighted fusion | First disagreement-aware heuristic |
|---|---:|---:|---:|
| Balanced clean | 3.77 | 3.57 | 4.00 |
| Persistent camera error | 3.90 | 3.69 | 4.13 |
| V2X loss/latency | 4.09 | 4.01 | 4.29 |
| Cross-source disagreement | 3.89 | 3.75 | 4.09 |

The first heuristic lost to reliability-weighted fusion in all four reported conditions. This is a negative pilot, not evidence for novelty. It must not be presented as a SUMO result or publication evidence. Re-run from version-controlled code before using it in any formal report.

## Falsification experiment plan

### Gate 0 — literature and claim audit

- Read full texts for Płaczek (2012), CIoT-PressLight, UCATSC, CAVLight/cooperative perception control, and robust RL under missing observations.
- Build a method-by-method matrix for observation sources, uncertainty representation, action evaluation, information acquisition, error models, safety constraints, simulator, and real-world validation.
- Search synonyms: decision uncertainty, action ambiguity, value of information, selective sensing, active perception, belief-space MPC, confidence-weighted fusion, sensor disagreement, perception-action coupling, V2X state estimation.
- Search patents separately before making any patentability statement.
- **Fail Gate 0** if an equivalent method already performs the same core mechanism. If it does, do not relabel it as novelty; change the question or make a clearly bounded replication/benchmarking contribution.

### Gate 1 — establish the environment and measurement validity

- Build and version-control one calibrated SUMO junction, route definitions, signal program, vehicle mix and demand profiles.
- Validate signal phase legality, yellow/all-red transitions, minimum green, pedestrian clearance, emergency request handling and metric calculations.
- Keep simulator ground truth out of policy inputs; use it only for offline measurement and error injection.
- Freeze evaluation scenarios and seeds before testing the candidate.

### Gate 2 — matched-error falsification

Compare independent errors with persistent errors at identical marginal rates; compare vehicle-class confusion while preserving counts where possible; separately test stale observations, missed detections, lane/movement assignment errors and combinations. Start with 0%, 10%, 25% and 50% injected error levels as experimental settings, not as claims about real-world detector rates.

Measure:
- Detection/count/class errors and temporal autocorrelation.
- Per-step action change relative to clean observation.
- Queue, delay, throughput, maximum queue and spillback.
- Pedestrian waiting and hard-constraint violations.
- Emergency-vehicle delay and priority response.
- Phase switches, fallback frequency and controller runtime.

If temporal structure and class confusion do not have repeatable downstream effects at matched marginal rates, reject the proposed mechanism.

### Gate 3 — fair controller comparison

At minimum compare:
1. Fixed-time or actuated controller.
2. A conventional RL controller with the same action and observation budget.
3. Fixed camera/V2X fusion.
4. Calibrated reliability-weighted fusion.
5. A simple confidence-threshold/fallback baseline.
6. A faithful implementation of the closest applicable method where feasible (or clearly label a simplified baseline as inspired, not reproduced).
7. The proposed method.

Match training budgets, legal actions, demand, seeds, observation access and wall-clock constraints. The clean-oracle controller is only a diagnostic upper bound, not a fair deployable baseline.

### Gate 4 — ablation and statistics

- Use paired seeds and identical demand scenarios across controllers.
- Use enough seeds to estimate uncertainty; begin with a smoke test, then expand based on confidence-interval width and a predeclared practical effect threshold.
- Report mean and 95% confidence intervals, paired effect sizes, and appropriate paired tests; correct for multiple comparisons when needed.
- Ablate the disagreement metric, temporal persistence model, class-aware model, V2X reliability, history/belief state and any extra-sensing gate individually.
- Compare against simpler predictors of action changes. If the proposed score adds no predictive value beyond confidence, variance, or action-margin baselines, simplify or abandon it.
- Report all scenarios and negative results, not only favorable seeds.

### Gate 5 — real-camera validation

Only after the controller survives simulation:
- Create a manually audited, privacy-compliant video sample with documented annotation protocol.
- Measure per-class precision/recall, count error by movement, tracking continuity, lane assignment, time synchronization and confidence calibration.
- Replay the observed error patterns into SUMO; do not claim field-level control validation merely because detector outputs were tested on video.
- Separate perception validation from live traffic-control validation.

## Predeclared decision rules

**Continue Option B only if all are true:**
1. The literature audit identifies a specific method-level distinction from the closest prior work.
2. The hypothesized failure mechanism is reproducible under controlled matched-error experiments.
3. The proposed method beats calibrated reliability fusion and a simple threshold/fallback baseline by a practically meaningful amount on the primary metric.
4. Benefits persist across demand regimes and paired seeds, with confidence intervals that exclude a trivial effect.
5. No material safety, pedestrian, emergency, legality or runtime regression occurs.

**Pivot or downgrade the claim if any fail:**
- If the mechanism exists but the mitigation does not win: contribute a careful negative/benchmarking study only if the study itself is rigorous and useful; do not claim a new controller.
- If the mechanism is not reproducible: abandon that hypothesis and return to a better-supported research question.
- If the method matches prior art: do not claim novelty; investigate a genuinely unaddressed boundary condition or focus on replication/real-world error characterization.
- If only real-camera perception results are strong: narrow the contribution to validated perception-error characterization and its control consequences.
- If pedestrian/emergency features are merely integrated: retain them as requirements and evaluation constraints, not novelty claims.

## Current verdict

**Novelty rating: unproven; high risk.** The next priority is not more components or a more elaborate project description. It is a full prior-art comparison and a reproducible, fair falsification experiment. No claim of “high novelty,” publication acceptance, or patentability is justified at this stage.
