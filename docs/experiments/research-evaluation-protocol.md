# Research Evaluation Protocol

## 1. Objective

Measure how the performance benefit of richer traffic-state representations changes as observation reliability deteriorates.

## 2. Baselines

1. Fixed-time.
2. Actuated control where feasible.
3. Standard vehicle-only RL.
4. R1/R2/R3 adaptive representations.
5. R4 reliability-aware representation/controller.

## 3. Experimental matrix

For each applicable representation evaluate clean observations plus missing observations, measurement noise, vehicle-type misclassification, and partial channel failure.

Recommended severity levels: `0%, 10%, 25%, 50%, 75%`.

## 4. Matched conditions

Keep junction, traffic demand, vehicle mix, simulation horizon, signal constraints, reward definition, evaluation procedure, and seed set constant for controlled comparisons.

## 5. Random seeds

Use at least five seeds for final comparisons where computationally feasible. Report mean and dispersion rather than a single best run.

## 6. Metrics

### Efficiency

Throughput, average delay, queue length, and travel time where available.

### Safety

Pedestrian waiting/timeliness, supported conflict/violation indicators, and safety-rule violations.

### Emergency

Emergency response delay, waiting time, and priority completion indicators.

### Stability

Phase changes, unnecessary switching, and action oscillation.

## 7. Information Benefit

For richer representation Rx against reference Rref:

`IB = [J(Rx,ρ) - J(Rref,ρ)] / |J(Rref,ρ)|`

The selected utility J and directionality must be defined consistently.

## 8. Degradation Ratio

For a metric/utility where higher is better:

`DR = [J(clean) - J(degraded)] / |J(clean)|`

For lower-is-better metrics, use a directionally consistent formulation.

## 9. Signature output

Produce an information–robustness curve or heatmap showing representation richness, observation reliability/degradation, and performance. The expected outcome is not predetermined.

## 10. Controller progression

A. Establish clean baselines and R1–R3.

B. Apply degradation to R1–R3 without explicit reliability information.

C. Quantify information benefit and failure regimes.

D. Introduce R4 reliability-aware control.

E. Evaluate safety/emergency stress cases.

F. Validate observation assumptions with camera-derived states.

## 11. Required ablations

- R1 vs R2 under clean observations;
- R2 vs R3 under clean observations;
- R2 under clean vs degraded observations;
- R3 under clean vs degraded observations;
- degraded rich state without reliability information;
- degraded rich state with reliability information.

## 12. Statistical reporting

Report mean, standard deviation or confidence interval, seed count, degradation configuration, and effect size where practical. Avoid reporting only the best run.

## 13. Reproducibility record

Every experiment should identify controller, state representation, degradation type, degradation severity, seed, demand configuration, junction/network version, reward configuration, evaluation horizon, and software/configuration version.

## 14. Failure-regime analysis

Explicitly identify conditions where richer information helps, has negligible benefit, harms performance, or where reliability-aware control recovers performance. These regimes are central research outputs.
