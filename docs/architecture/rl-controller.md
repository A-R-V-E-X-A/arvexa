# RL Controller Architecture

## Action

The controller jointly selects:

1. signal phase/action;
2. duration or permitted extension within the configured action space.

## Controller progression

### Controller 1 — Standard clean-observation RL

Tests adaptive control under clean R1/R2-style information.

### Controller 2 — Degradation-exposed RL

Uses the same basic controller while observations are intentionally degraded. Purpose: determine how much performance changes without giving the controller explicit reliability information.

### Controller 3 — Reliability-aware RL

Receives explicit observation-quality information and may learn or implement reduced reliance/fallback behavior. Purpose: determine whether knowing information quality changes robustness.

## State levels

- R1: counts, queues, signal state.
- R2: R1 + vehicle-type composition.
- R3: R2 + pedestrian/emergency state.
- R4: R3 + explicit reliability information.

## Reward

The reward should represent traffic efficiency, safety, emergency priority, and signal stability. Exact weights must be frozen for controlled comparisons or explicitly treated as an experimental variable.

## Safety boundary

RL output must pass through deterministic safety/priority validation before actuation.

## Required ablations

- richer state without degradation,
- richer state with degradation,
- degradation without explicit reliability,
- degradation with explicit reliability.
