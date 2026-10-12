"""Seeded perception-error primitives for ARVEXA's falsification experiments.

These functions perturb offline candidate detections; only their returned
records may be exposed to a controller. This is a testable starting point,
not a validated detector/error model. For persistence, records must be in
timestamp order and include each candidate track/frame before error injection.
"""
from __future__ import annotations

import random
from typing import Any, Iterable


def independent_missed_detections(
    records: Iterable[dict[str, Any]], miss_rate: float, seed: int
) -> list[dict[str, Any]]:
    """Drop each candidate detection independently at the requested probability."""
    _validate_rate(miss_rate)
    rng = random.Random(seed)
    return [dict(r) for r in records if rng.random() >= miss_rate]


def persistent_missed_detections(
    records: Iterable[dict[str, Any]],
    miss_rate: float,
    persistence: float,
    seed: int,
) -> list[dict[str, Any]]:
    """Apply a two-state Markov error process per vehicle ID.

    persistence = P(error_t | error_(t-1)). The stationary error probability
    is approximately miss_rate when the process is observed in stationarity:
    p_enter = miss_rate * (1 - persistence) / (1 - miss_rate).
    The input must contain candidate records for each track/frame, including
    candidates that the simulated detector could miss. Never expose this
    candidate list or simulator IDs to the evaluated policy.
    """
    _validate_rate(miss_rate)
    if not 0 <= persistence < 1:
        raise ValueError("persistence must be in [0, 1)")
    if miss_rate == 0:
        return [dict(r) for r in records]
    if miss_rate == 1:
        return []
    p_enter = miss_rate * (1 - persistence) / (1 - miss_rate)
    if p_enter > 1:
        raise ValueError("miss_rate and persistence imply an invalid transition probability")

    rng = random.Random(seed)
    in_error: dict[str, bool] = {}
    output = []
    for record in records:
        key = str(record.get("vehicle_id", "unknown"))
        was_error = in_error.get(key, False)
        now_error = (rng.random() < persistence) if was_error else (rng.random() < p_enter)
        in_error[key] = now_error
        if not now_error:
            output.append(dict(record))
    return output


def class_confusion(
    records: Iterable[dict[str, Any]],
    confusion: dict[str, dict[str, float]],
    seed: int,
) -> list[dict[str, Any]]:
    """Change class labels using a row-stochastic confusion matrix.

    Each row maps the input class to observed-label probabilities. Record count
    is preserved. Prefer a matrix measured on held-out camera footage; synthetic
    matrices are stress tests, not empirical claims.
    """
    rng = random.Random(seed)
    output = []
    for record in records:
        row = confusion.get(str(record.get("vehicle_class", "")))
        changed = dict(record)
        if row:
            _validate_distribution(row)
            draw = rng.random()
            cumulative = 0.0
            for label, probability in row.items():
                cumulative += probability
                if draw <= cumulative:
                    changed["vehicle_class"] = label
                    break
        output.append(changed)
    return output


def _validate_rate(rate: float) -> None:
    if not 0 <= rate <= 1:
        raise ValueError("error rate must be in [0, 1]")


def _validate_distribution(row: dict[str, float]) -> None:
    if not row or any(p < 0 for p in row.values()) or abs(sum(row.values()) - 1.0) > 1e-8:
        raise ValueError("each confusion-matrix row must be non-empty and sum to 1")
