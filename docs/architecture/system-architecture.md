# System Architecture

## High-level pipeline

`SUMO true state` → `observation/degradation model` → `state builder + reliability vector` → `RL controller` → `deterministic safety/priority boundary` → `TraCI` → `SUMO` → `metrics`

## Layer 1 — Simulation truth

SUMO provides the reference traffic state. This state is not automatically assumed to be the controller's observation.

## Layer 2 — Observation model

The observation model converts the reference state into what a controller would actually observe. It can introduce missing data, noise, semantic misclassification, and partial sensor failure.

## Layer 3 — State builder

The state builder converts observations into R1–R4 representations and, for R4, produces explicit quality/reliability information.

Conceptually: `ρ = [ρ_count, ρ_type, ρ_ped, ρ_emergency, ...]`

## Layer 4 — RL controller

The policy receives the selected state and chooses signal phase and allowed duration/action extension within configured signal constraints.

## Layer 5 — Safety/priority boundary

A deterministic layer validates or constrains actions according to pedestrian and emergency requirements. This boundary is authoritative for hard safety rules.

## Layer 6 — TraCI

TraCI transfers controller decisions between the Python control system and SUMO during closed-loop simulation.

## Layer 7 — Evaluation

The evaluator compares controllers under matched conditions and records efficiency, safety, emergency response, stability, Information Benefit, and Degradation Ratio.

## Research separation

The architecture deliberately separates:

**what is true → what is observed → how reliable it is → what the controller decides → what safety allows**

This separation is essential for studying information reliability rather than accidentally evaluating only the RL algorithm.
