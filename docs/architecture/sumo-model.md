# SUMO Model

## Purpose

SUMO provides a reproducible closed-loop environment in which ARVEXA can vary traffic-state representation and observation reliability while keeping junction geometry and demand controlled.

## True state versus observed state

A central architectural rule is:

**SUMO true state ≠ controller observation**

The true state is retained as the reference. The controller receives a transformed observation. This allows exact calculation of what was lost, changed, or corrupted.

## TraCI

TraCI provides runtime communication between the controller and SUMO. The controller reads the configured traffic observation, computes an action, and sends the permitted signal command back to SUMO.

## Heterogeneous traffic

The model should represent relevant vehicle classes used by the research question, including mixed traffic such as two-wheelers, cars, autos, buses, and emergency vehicles where supported by the calibrated junction.

## Observation degradation

The observation layer can transform the true state using controlled mechanisms for missing data, noise, misclassification, and partial failure. The transformation must be logged.

## Calibration

The selected real-world junction should be calibrated against available traffic observations. Calibration parameters should be documented so that the simulation remains a grounded test environment rather than an arbitrary synthetic network.

## Scope

The project should prioritize a single well-characterized junction over a large number of poorly calibrated networks.
