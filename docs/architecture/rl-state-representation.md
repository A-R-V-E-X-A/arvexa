# RL State Representation

## Research purpose

The state representation is an experimental variable, not merely an implementation detail.

| Level | Included information | Research purpose |
|---|---|---|
| R1 | vehicle counts, queues, signal state | Basic adaptive control |
| R2 | R1 + vehicle-type composition | Value of heterogeneous semantic information |
| R3 | R2 + pedestrian/emergency state | Safety and priority context |
| R4 | R3 + observation reliability/quality | Reliability-aware decision making |

## Reliability vector

A conceptual R4 representation can expose:

`ρ = [ρ_count, ρ_type, ρ_ped, ρ_emergency, ...]`

Each element represents the estimated reliability of the corresponding information channel. The vector should only contain quantities that can be defined and measured reproducibly.

## Important experiment

Vehicle-type misclassification is a particularly informative degradation mode. Aggregate count can remain approximately correct while class labels are corrupted, directly testing whether richer semantic information remains useful when semantic reliability deteriorates.

## Fair comparison

When comparing R1–R4, use the same traffic demand, junction, action constraints, evaluation horizon, and seed set where appropriate; change only the intended representation/degradation variable.

## R4 caution

Adding a reliability vector is not itself evidence of novelty. Its value must be demonstrated through matched experiments showing whether explicit reliability information changes robustness.
