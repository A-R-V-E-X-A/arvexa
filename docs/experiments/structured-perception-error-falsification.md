# Structured Perception-Error Falsification Protocol

## Status

**Pre-registration-style protocol; no experiment has been run and no results are claimed.** This protocol tests whether structured perception errors create control effects that average detector error rates alone fail to explain. It is a small falsification pilot, not the final evaluation.

## 1. Research question

At a fixed average observation error rate, do temporally correlated and vehicle-class-dependent perception errors change adaptive signal-control decisions and outcomes differently from independent errors? If so, does explicit reliability information or a simple mitigation improve outcomes against strong baselines?

## 2. Hypotheses

- **H1 (error-structure effect):** at matched marginal error rates, temporally persistent errors cause different control outcomes from independent errors.
- **H2 (semantic effect):** vehicle-class confusion can harm control even when total vehicle counts remain approximately correct.
- **H3 (mitigation value):** a reliability-aware method improves a predeclared robustness/safety/efficiency measure relative to a non-reliability-aware policy and simple confidence-threshold baseline.
- **H0 / falsification:** differences are negligible or inconsistent across seeds/demand regimes, or the proposed mitigation fails to beat simple baselines.

Do not assume H1–H3 are true. Report null or negative findings.

## 3. Minimum pilot scope

Start with one calibrated SUMO junction and a small, fixed scenario set. Use at least three demand regimes (low, near-capacity, and oversaturated) and at least five paired random seeds if compute allows. For a cheaper initial smoke test, use three seeds, but do not use that reduced pilot as publication-grade evidence.

Use the same junction, route demand, vehicle mix, controller training budget, action constraints, reward, episode horizon, and evaluation seeds for each paired comparison. Keep training and test scenarios separate. Do not use hidden SUMO ground truth as an input to the deployed/evaluated policy; it may be retained by the experiment harness only to quantify observation error and calculate outcomes.

## 4. Observation-error conditions

Test the following conditions separately before combining them:

| ID | Error mode | Controlled intervention |
|---|---|---|
| E0 | Clean oracle observation | Ground-truth simulator observation; diagnostic upper-bound only |
| E1 | Independent missed detections | Randomly remove vehicle observations at a specified marginal rate |
| E2 | Persistent missed detections | Use a temporally persistent process so the same lane/class/movement can remain under-observed across consecutive frames |
| E3 | Vehicle-class confusion | Apply a documented confusion matrix while preserving detected-object count where possible |
| E4 | Persistent class confusion | Keep class-label errors correlated across consecutive frames/track segments |
| E5 | Stale observations | Delay or reuse a prior observation for a defined number of frames |
| E6 | Tracking loss / lane assignment error | Drop tracks or assign observations to the wrong movement using controlled probabilities |
| E7 | Combined realistic errors | Combine only error modes whose individual effects are understood |

Suggested initial marginal severity levels: 0%, 10%, 25%, and 50%. Add 75% only if the junction/controller remains meaningful at that severity. These are experimental settings, not claimed real-world detector rates.

For E2/E4, document the persistence model and parameters. Compare against E1/E3 at the same marginal error rate. Otherwise, any effect could be caused by more errors rather than error correlation.

## 5. Controller and baseline ladder

Use a feasible subset in the pilot, then expand if H1/H2 survive.

1. **Fixed-time or actuated baseline** — establishes practical reference performance.
2. **R1 controller** — counts, queues and signal state.
3. **R2 controller** — R1 plus vehicle-type composition.
4. **R3 controller** — R2 plus pedestrian/emergency state where these features are implemented and validated.
5. **R4 reliability-aware controller** — R3 plus explicitly defined observation-quality features.
6. **Confidence-threshold baseline** — use a simple predeclared confidence rule to ignore, down-weight or fall back from low-confidence channels.
7. **Uncertainty-aware baseline** — compare against UCATSC if a faithful implementation is feasible; otherwise label any simpler adaptation clearly as “UCATSC-inspired,” not as a reproduction.
8. **Perception-escalation baseline** — only if the system actually has a cheap/expensive perception path. Compare fixed escalation and confidence-triggered escalation before any proposed decision-value gate.

The clean oracle is a diagnostic ceiling, not a fair deployable baseline. Do not compare methods with different observation access or training budgets without clearly labeling the mismatch.

## 6. Primary measurements

### Perception and state error

- Detection recall/precision where ground truth is available.
- Vehicle-class confusion matrix, macro-F1 and per-class recall.
- Count error by movement and vehicle class.
- Error persistence duration and autocorrelation.
- Staleness and lane/movement assignment error rates.

### Decision propagation

- Fraction of control steps where degraded observations change the selected phase relative to the same controller under clean observations.
- Phase-duration deviation from the paired clean-observation run.
- Unsafe/inadmissible action attempts before the safety filter, if present.
- Action oscillation, unnecessary switching and minimum-green/clearance constraint violations.
- Error-to-action lag and duration of harmful action changes.

The clean-observation action is a comparison reference, not automatically the “correct” action. Also report actual downstream outcomes.

### Traffic outcomes

- Mean and percentile vehicle delay.
- Queue length and maximum queue.
- Throughput and travel time.
- Vehicle-type-stratified delay where the simulator supports reliable measurement.

### Safety and priority outcomes

- Pedestrian waiting and service/clearance compliance.
- Emergency-vehicle waiting/response delay.
- Explicit safety-constraint violations.
- Starvation/fairness measures for low-volume movements.

Use only metrics that are implemented and operationally defined. Do not infer real-world crash risk directly from a proxy metric.

### Runtime

- Controller inference time and, if applicable, perception time.
- Median and p95 end-to-end decision latency.
- Deadline misses and fallback frequency.
- Additional compute or escalation calls.

## 7. Analysis plan

1. Generate paired scenarios with identical demand and simulator seeds across methods.
2. Report mean, dispersion and 95% confidence intervals; use paired comparisons where the design supports them.
3. Plot performance against marginal error severity, separately for independent and persistent errors.
4. Plot class-specific effects so aggregate vehicle counts do not hide semantic failure.
5. Report the interaction between representation level (R1/R2/R3/R4), error mode, and severity.
6. Separate average performance from tail outcomes and safety-constraint violations.
7. Run ablations: remove reliability features; remove temporal persistence modeling; remove class-specific handling; disable fallback/escalation.
8. Evaluate on held-out demand patterns after choosing any thresholds on validation scenarios only.
9. Preserve all configs, seeds, source revisions and raw result summaries.

Do not choose thresholds using the final test set. Avoid selecting only favorable seeds or reporting only the best run.

## 8. Falsification and go/no-go criteria

Before running, set a minimum practically meaningful effect size for the primary outcome with the project supervisor/team. Do not choose it after viewing results.

**Continue the research direction only if:**

- persistent/class-dependent errors produce a reproducible effect beyond independent errors at matched marginal rates;
- the effect is visible in downstream control outcomes, not just model confidence;
- the proposed mitigation improves at least one predeclared primary metric over the confidence-threshold baseline, with uncertainty reported;
- no unacceptable increase occurs in safety violations, pedestrian delay, emergency delay, or deadline misses;
- the result generalizes to held-out demand and multiple seeds.

**Stop or revise the claim if:**

- the error-structure effect vanishes when marginal rates are matched;
- effects are smaller than the predeclared practical threshold or inconsistent across seeds;
- a simpler baseline matches or beats the proposed method;
- performance gains rely on oracle information unavailable to the controller;
- latency or safety costs outweigh any efficiency improvement.

## 9. Reproducibility record

For every run, store:

- experiment ID and source commit;
- network/config/route identifiers and version hashes;
- demand regime and vehicle-class distribution;
- controller, state representation and trained checkpoint;
- observation-error type, marginal rate, persistence parameters and random seed;
- training/evaluation seed separation;
- reward, action constraints and safety-filter configuration;
- metrics, runtime and logs;
- exclusions, failures and deviations from this protocol.

Do not commit raw camera footage or large generated artifacts to Git. Store compact configs, code, metadata and summarized results; use an approved storage location for large artifacts.

## 10. Execution sequence

1. Validate the junction, controller and clean observation baseline.
2. Implement deterministic, unit-tested observation corruption functions.
3. Verify each corruption function against its requested marginal rate and persistence.
4. Run a small smoke test and inspect logs.
5. Run paired pilot scenarios for E1–E4.
6. Analyze H1/H2 before implementing a complex mitigation.
7. Only if the effect survives, compare R4/confidence-threshold/uncertainty-aware alternatives.
8. Record a go/no-go decision before updating the official problem statement or novelty claim.
