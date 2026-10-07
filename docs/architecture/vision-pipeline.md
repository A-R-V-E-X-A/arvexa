# Vision Pipeline

## Purpose

The vision pipeline provides a real-world check on the assumptions used by the simulated observation model.

## Pipeline

`camera/video` → `detection` → `classification` → `tracking` → `counting` → `traffic-state extraction` → `observation-quality estimation` → `SUMO calibration/validation`

## Detection and classification

Relevant road users are detected and assigned the semantic classes required by the ARVEXA state representation. Classification is especially important because it can be wrong even when total detected vehicle count is approximately correct.

## Tracking and counting

Tracking reduces duplicate counts and supports movement/queue estimation.

## Observation quality

The pipeline should estimate quality rather than assume every detection is correct. Possible signals include confidence distributions, missing tracks, inconsistent class assignments, temporal discontinuities, and detection coverage.

## Integration rule

Camera-derived observations should enter the same conceptual observation/state-building layer used in simulation. Raw camera frames are not directly fed to the RL policy.

## Validation role

The camera system primarily tests whether simulated observation errors are realistic, whether vehicle-type information is obtainable with acceptable reliability, and whether the calibrated SUMO traffic state resembles observed traffic.
