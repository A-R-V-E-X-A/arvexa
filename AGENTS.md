# ARVEXA Development Guidelines

ARVEXA (Adaptive Resilient Vehicle–pedestrian eXchange Architecture) is a research project for adaptive traffic signal control using multi-objective reinforcement learning.

## Development rules

1. Work is organized into research objectives, requirements, sprints, and implementation slices.
2. Every implementation slice must have testable acceptance criteria.
3. Keep changes scoped to the assigned slice; avoid unrelated refactors.
4. Research experiments must be reproducible. Record configurations, scenarios, and random seeds where applicable.
5. Keep simulation configuration separate from source code.
6. Do not commit secrets, credentials, private data, or large generated artifacts.
7. Do not commit raw video or large datasets directly unless an appropriate storage mechanism is adopted.
8. Changes to the RL state, action space, reward function, safety constraints, or evaluation methodology require team review.
9. Results must identify the scenario, baseline, configuration, and metrics used.
10. Keep main stable and reproducible. Use feature branches and pull requests.
11. If a requirement or research decision is ambiguous, resolve it with the team before implementation.
12. Document non-obvious architectural and research decisions.

## Research traceability

Where applicable:

Research Objective ? Requirement ? Architecture Component ? Implementation Slice ? Experiment/Scenario ? Metric ? Result
