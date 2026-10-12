# ARVEXA Prior-Art Audit and Validation Protocol — 12 October 2026

## Status

**Novelty status: unproven; high overlap risk for the broad Option B claim.** This is a targeted, source-backed audit, not an exhaustive systematic review, patentability opinion, or freedom-to-operate analysis. Search results and abstracts are not substitutes for a claim-by-claim full-text review.

**Execution status:** no SUMO/TraCI binary or Python bindings were available in the execution environment. An attempt to install `eclipse-sumo` failed because this environment could not resolve the package index. Therefore no SUMO run, real-camera evaluation, controller comparison, or statistical result is claimed in this update.

## 1. Research question under test

Broad candidate (too close to prior art to claim as novel without a much more specific distinction):

> When camera-derived and connected-vehicle (V2X) observations disagree, estimate whether the disagreement could change the preferred signal action, then use that information to improve control over fixed and reliability-weighted fusion.

Narrower falsifiable hypothesis:

> Under matched marginal observation-error rates, temporal persistence and vehicle-class-dependent visual errors create reproducible control failures not adequately predicted by standard reliability-weighted fusion or existing belief-space/counterfactual control; a precisely specified mitigation reduces those failures under equal information, compute, and safety constraints.

This narrower statement is **not yet a novelty claim**. It may be falsified by prior art or experiments.

## 2. Method-by-method prior-art comparison

| Method / source | Observation and uncertainty model | Decision/control mechanism | Overlap with ARVEXA | Required distinction |
|---|---|---|---|---|
| Płaczek, “Selective data collection in vehicular networks for traffic control applications,” Transportation Research Part C 23 (2012), 14–28. DOI 10.1016/j.trc.2011.12.007; https://arxiv.org/abs/1112.4620 | V2X vehicle sensing; predictive traffic simulation estimates uncertainty in control decisions | Requests/transmits additional V2X data at selected times when uncertainty means the optimal action cannot be derived unambiguously | **Very high** for decision uncertainty driving information acquisition | Must differ beyond an action-ambiguity score or requesting more data under uncertain action. Compare the exact uncertainty calculation, predictive model, acquisition rule and objective from the full paper |
| Hong, “CIoT-PressLight: Smart Pole and V2X Assisted Multi-Agent Reinforcement Learning for Adaptive Urban Traffic Signal Control,” SSRN, posted 8 Sep 2026; https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7434523 | Camera/radar/V2X fusion; explicit sensing noise, message frequency, latency, packet loss and reliability-weighted fusion | Cognitive traffic pressure and decentralized MARL / value decomposition with neighbor attention | **Very high** for camera/V2X fusion, communication degradation and RL signal control | Establish whether ARVEXA's error dynamics, action-level failure diagnosis or mitigation is technically different and useful. The SSRN paper says it is not peer reviewed; reported results are author-reported and not reproduced by ARVEXA |
| Bodagala & Bodagala, UCATSC, “Uncertainty-Aware Counterfactual Traffic Signal Control with Predictive Safety and Starvation-Avoidance Constraints Using Vision-Based Sensing,” arXiv:2602.07784, https://arxiv.org/abs/2602.07784 | Vision uncertainty and partial observability represented in belief state | Belief-space counterfactual rollouts evaluate candidate actions and enforce predictive safety/starvation constraints | **High** for vision uncertainty and action evaluation under uncertainty | Compare exact belief update, rollout model, constraints and objective. A new disagreement score on top of counterfactual evaluation is not sufficient |
| Sulistiawan, Edbert & Fitrianah, “Evaluating the Robustness of Deep Q-Network Variants Against Visual Perception Errors in Traffic Signal Control,” ICSMech 2026, DOI 10.1109/icsmech69390.2026.11647148 | Visual perception inaccuracies associated with visibility/fog | Tests DQN variants/training modifications against fixed-time baseline under perception error | **High** for visual errors affecting RL signal control | Obtain full text and establish whether class confusion, temporal correlation, matched marginal error rates and action-level propagation are studied. Do not claim these are absent based on the abstract alone |
| T-REX, “Robustness of RL-based traffic signal control under incidents,” 2026, https://link.springer.com/article/10.1186/s12544-026-00841-1; code https://github.com/MLSM-at-DTU/T-REX | Traffic disruption / distribution shift, with robustness evaluation | Robustness benchmarking for RL signal control | Medium: strong precedent for disruption testing and reproducible robustness evaluation | Distinguish perception-specific error interventions from incident/distribution-shift conditions; inspect the implementation and metrics |
| Rodrigues & Azevedo, “Robust RL for Traffic Signal Control under Demand Surges, Incidents and Sensor Failures,” arXiv:1904.08353, https://arxiv.org/abs/1904.08353 | Traffic disruption and sensor failures | Robust RL signal control | High for general sensor-failure robustness | Generic sensor-failure tolerance is not a novelty claim |
| PedSLight (2026), https://doi.org/10.3389/ffutr.2026.1953597 | Pedestrian state/safety | Pedestrian-aware RL control | High overlap for pedestrian-aware multi-objective signal control | Keep pedestrian service as safety requirement/metric unless a specific distinct method is shown |
| DEEP, “The Decision Value of Perception Compute,” arXiv:2609.35910, https://arxiv.org/abs/2609.35910 | Perception uncertainty and compute cost in a downstream decision context | Allocates perception compute according to decision value | Adjacent-domain overlap for decision-relevant sensing/compute | If ARVEXA adds perception escalation, compare against fixed-budget and confidence-triggered escalation and explain the traffic-specific methodological advance |
| Patent CN116129632B, https://patents.google.com/patent/CN116129632B/en | Radar/vision fusion, vehicle state/queue features | Deep RL traffic-light control | Patent prior art against generic sensor-fusion + RL combinations | Read independent claims and family/citations; jurisdiction-specific legal analysis required |
| Patent US20220076571A1, https://patents.google.com/patent/US20220076571A1/en | Camera images and lane/direction congestion state | RL-based signal control apparatus | Patent prior art for camera-derived state + RL signal control | Claim-by-claim legal analysis required |
| Patent US20220270480A1, https://patents.google.com/patent/US20220270480A1/en | Images of multiple intersections; multi-agent RL | Multi-agent signal control from image-derived states | Patent prior art for camera + multi-agent RL | Claim-by-claim legal analysis required |
| Patent US20210142658A1, https://patents.google.com/patent/US20210142658A1/en | Vehicle/infrastructure communication, SPaT, camera-derived and vehicle data | Traffic signal management for connected/autonomous vehicle operation | Patent prior art for signal/vehicle communications and camera/vehicle data exchange | Claim-by-claim legal analysis required |
| Patent US20260045162A1, https://patents.google.com/patent/US20260045162A1/en | Lane flow state and road-network graph | RL signal control with spatiotemporal encoder and return-based action decoder | Patent prior art for modern RL signal-control architectures | Claim-by-claim legal analysis required |

### Audit interpretation

The combination of (a) camera/V2X fusion, (b) reliability weighting, (c) uncertain-state control, and (d) action ambiguity triggering data collection is not a safe novelty claim. The sources above cover these themes separately and in overlapping combinations.

The plausible remaining gap is narrower: **causal characterization of temporal and semantic structure in perception errors at matched marginal error rates, tracing those errors through state estimates to signal-action changes and downstream safety/efficiency; plus a specific mitigation shown to beat the strongest relevant baselines.** The current search does not establish that this gap is unaddressed by all prior work. Full-text and patent-claim review remains necessary.

## 3. Search and patent-audit method

Search terms to record and rerun in Google Scholar, IEEE Xplore, TRID/Transportation Research, Scopus/Web of Science if available, arXiv, Crossref, Google Patents, WIPO Patentscope, Espacenet, and the Indian Patent Advanced Search System:

- “traffic signal control” AND “decision uncertainty” / “action ambiguity” / “value of information”
- “selective sensing” / “selective data collection” / “active perception” AND traffic signal
- camera AND V2X AND “reliability-weighted fusion” AND signal control
- “belief-space” / “counterfactual rollout” / “partially observable” AND traffic signal
- “perception error” / “class confusion” / “missed detection” / “tracking loss” AND reinforcement learning AND traffic signal
- “temporally correlated observation noise” / “persistent errors” / “matched error rate” AND traffic control
- pedestrian safety, emergency priority, stale observations, sensor failure and communication latency with traffic signal control
- patents: “camera-based traffic signal control reinforcement learning”; “radar vision fusion traffic light”; “vehicle-to-infrastructure signal control”; “uncertainty-aware traffic signal”; “traffic control data acquisition decision uncertainty”

Record each query, date, database, screening reason, full-text status and exact claim it affects. Search patent families and citations; patent search results alone do not establish infringement, validity, or patentability. The above patent examples are preliminary search hits, not a completed legal analysis.

## 4. SUMO environment status and build requirements

Official installation references:
- SUMO downloads/install: https://sumo.dlr.de/docs/Downloads.php
- TraCI Python interface: https://sumo.dlr.de/docs/TraCI/Interfacing_TraCI_from_Python.html
- Traffic-light TraCI tutorial: https://sumo.dlr.de/docs/Tutorials/TraCI4Traffic_Lights.html
- Pedestrian crossing tutorial: https://sumo.dlr.de/docs/Tutorials/TraCIPedCrossing.html

SUMO's official documentation states that `eclipse-sumo` can be installed via pip, and that TraCI can be installed via `pip install traci`; this execution environment could not access the package index, so installation could not be completed here.

Before experiments, pin the SUMO and Python versions and record them in every result. Use a small, version-controlled junction first; do not call it Bengaluru-calibrated until geometry, lane connections, signal phases, demand, vehicle mix and turning movements are validated against an identified source dataset or field observations.

Minimum environment components:
- One four-arm junction with explicit legal phase plan, yellow/all-red clearance and minimum green.
- Separate vehicle types for two-wheelers, auto-rickshaws, cars and buses; document dimensions/speed/acceleration assumptions and avoid implying these are calibrated without data.
- Demand scenarios: low, near-capacity and oversaturated; turn ratios and arrival processes recorded.
- Pedestrian crossings with pedestrian arrivals and explicit crossing clearance.
- Emergency vehicle route/arrival injection and measurable priority response.
- Deterministic demand seed and independent controller/training seed; log both.
- A sensor abstraction that reads simulator ground truth, then injects errors to create observations. Ground truth must never leak into evaluated policy inputs.
- CSV/Parquet per episode with controller, scenario, seed, step, observed state, hidden truth for offline scoring only, selected action, legal-action filter, queues, delay, throughput, pedestrian waiting, emergency delay, violations, fallback, and runtime.
- Config, code commit, dependencies and full command stored with every run.

### Smoke-test acceptance gates

1. `sumo --version` succeeds and TraCI connects to a toy network.
2. Network validates and completes a short episode without teleports or unexpected deadlocks.
3. Signal transitions obey minimum green, yellow/all-red and pedestrian-clearance rules.
4. Repeating the same configuration and seed reproduces the same result within documented simulator tolerances.
5. Metric definitions pass hand-checks on a tiny deterministic test.
6. Injected errors match the requested marginal rates and temporal persistence statistics.
7. Baseline controllers all see the same allowed observation channels and legal actions.

Until these gates pass, no performance claims should be made.

## 5. Matched-error hypothesis experiment

### Hypotheses

- H1: At the same marginal miss rate, temporally persistent misses change signal actions/outcomes differently from independent misses.
- H2: At approximately the same total detected count, vehicle-class confusion changes actions/outcomes when vehicle classes have different control relevance.
- H3: The proposed mitigation adds practical value over calibrated reliability-weighted fusion and a simple confidence-threshold/fallback baseline.
- H0: Effects are small, inconsistent, explained by simpler baselines, or absent.

### Interventions

Use a predeclared initial grid of 0%, 10%, 25%, and 50% errors as experimental stress levels, not claims about real detector performance.

- E0 clean simulator observation (diagnostic oracle only).
- E1 independent missed detections.
- E2 temporally persistent missed detections matched to E1's marginal miss rate.
- E3 class-label confusion using a published or measured confusion matrix, preserving detected-object count where feasible.
- E4 temporally persistent class confusion matched to E3's marginal class-error rate.
- E5 stale observations at fixed delays.
- E6 wrong lane/movement assignment and tracking loss.
- E7 combinations only after single-error effects are understood.

For persistence, predefine a Markov or track-segment process and calibrate its parameters so its overall error frequency matches the independent condition. Report both marginal error rate and autocorrelation/persistence length. For class confusion, publish the matrix and per-class counts; do not hide changes in class balance.

### Outcomes

Perception: precision/recall, macro-F1, per-class recall, movement-level count MAE, class confusion, persistence duration, stale-frame rate, lane assignment error.

Decision propagation: fraction of steps whose selected phase differs from the clean-observation paired run, phase-duration difference, action-switch rate, time-to-recovery, safety-filter rejections, fallback rate.

Traffic: mean and 95th percentile delay, mean/maximum queue, throughput, spillback, stops.

Safety/service: pedestrian wait and maximum wait, crossing clearance violations, conflicting greens, minimum-green/clearance violations, emergency response delay and priority success.

Systems: controller wall-clock runtime per step, missed control deadlines, memory if feasible.

The clean-observation action is a diagnostic comparator, not automatically the optimal or safest action. Always report actual downstream outcomes as well.

## 6. Baseline ladder

1. Fixed-time controller with documented timing plan.
2. Vehicle-actuated baseline if implemented faithfully.
3. Conventional RL controller with the same phase/duration action space and same legal-action constraints.
4. Fixed camera/V2X fusion.
5. Calibrated reliability-weighted fusion. Calibrate sensor reliability on training/validation data only, not the test scenarios.
6. Confidence-threshold baseline with predeclared down-weight/fallback rule.
7. Proposed ARVEXA mitigation.
8. UCATSC reproduction if feasible and faithful; otherwise label an approximation “UCATSC-inspired” and explicitly list differences.
9. CIoT-PressLight reproduction if feasible and faithful; otherwise do not describe a simplified controller as reproducing the paper.
10. Płaczek-inspired decision-uncertainty-triggered data request only if the simulator supports a comparable V2X acquisition budget; label it inspired unless fully reproduced.

Fairness: identical demand scenarios, test seeds, action legality, simulation horizon, observation availability and training budget. Where a method inherently uses different compute or extra data, report that as a separate budgeted comparison. The oracle is not a deployable baseline.

## 7. Ablations, seeds and statistical analysis

Use a smoke test (3 seeds) only to debug the pipeline. For preliminary estimates, use at least 10 paired seeds; for publication-quality evidence, choose the final sample size from pilot variance and a predeclared minimum practically important effect, aiming for confidence intervals narrow enough to distinguish that effect. Ten seeds alone do not guarantee adequate power.

For each controller/scenario/seed, pair the same demand realization across methods. Report mean, standard deviation, median and 95% confidence intervals; paired differences and effect sizes; and paired tests appropriate to the outcome distribution. Use bootstrap confidence intervals if assumptions for parametric tests are doubtful. Correct for multiple comparisons when testing many conditions. Publish all seeds, failed runs and scenario-level results.

Predeclare:
- One primary metric (suggested: mean vehicle delay, with a non-inferiority safety gate).
- One minimum practically important improvement before running final evaluation.
- Safety gates that cannot be traded away for average delay.
- How missing/failed episodes are handled.
- Statistical method and multiple-comparison correction.

Ablate one component at a time: temporal-persistence estimator, class-aware state, reliability calibration, disagreement/action-margin feature, history/belief state, V2X latency handling and fallback gate. Also compare against simple predictors such as maximum sensor confidence, variance, disagreement magnitude and action-value margin. If the proposed feature adds no out-of-sample predictive value over these simpler measures, remove it or revise the claim.

## 8. Real camera validation

Real footage is a perception-validation dataset, not a live controller trial.

- Use footage with documented lawful access, privacy safeguards and provenance.
- Sample across day/night, occlusion, weather, camera angle and density where available.
- Annotate vehicles, class, movement/lane, timestamps and track identity with a documented protocol; double-annotate a subset and report inter-annotator agreement.
- Measure detection precision/recall, per-class metrics, count MAE by movement, track continuity, lane assignment, confidence calibration and temporal error persistence.
- Split by video/time/location, not random adjacent frames, to avoid leakage.
- Convert measured error traces into simulator observation perturbations; compare those replayed conditions against synthetic error models.
- State clearly that replaying real perception errors in SUMO validates control robustness under those errors, not real-world traffic-control efficacy.

## 9. Predeclared novelty decision rules

**Retain the candidate method-level novelty claim only if all conditions hold:**
1. Full-text audit identifies a specific technical difference from Płaczek, CIoT-PressLight and UCATSC, plus related visual-error robustness work.
2. Matched-error experiments reproduce the hypothesized structured-error effect.
3. The proposed method beats reliability-weighted fusion and confidence-threshold/fallback by a predeclared practically meaningful amount, with uncertainty intervals supporting the effect.
4. Improvement persists across demand regimes and independent paired seeds.
5. Ablations show the proposed mechanism—not a larger model, extra information or compute—causes the improvement.
6. Pedestrian/emergency constraints, signal legality and runtime do not materially regress.
7. The claim survives the full patent-family search; any legal conclusion is referred to qualified counsel.

**If any fail:**
- Prior art equivalent: withdraw the novelty claim; identify a real unresolved boundary condition or pivot to reproducible benchmarking/characterization.
- Error effect absent: reject the hypothesis.
- Effect present but mitigation loses: report the negative result only if the study's controlled characterization is independently valuable.
- Improvement disappears under fair budgets or paired-seed analysis: do not claim superiority.
- Safety regression: reject the method or redesign it with hard constraints.
- Only perception metrics are strong: narrow the contribution to real-camera error characterization and its control consequences.

## 10. Current conclusion

The most defensible present statement is:

> ARVEXA is investigating whether temporal and class-dependent perception errors have control consequences beyond what average sensor reliability captures, and whether a mitigation can improve traffic control under matched error and resource budgets.

Do not yet state that this is novel, that the method outperforms existing work, or that the system has been validated in SUMO or on real traffic. The current evidence supports a research hypothesis and an experimental protocol, not a high novelty verdict.
