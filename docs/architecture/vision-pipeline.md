# ARVEXA Vision Pipeline Architecture

## 1. Purpose

The ARVEXA vision pipeline converts real traffic-camera footage into structured traffic observations that support SUMO calibration and validation.

The vision pipeline is a measurement system, not the RL controller itself.

## 2. Pipeline Overview

Camera footage → frame extraction → preprocessing → vehicle detection → classification → tracking → region/line association → counting → temporal aggregation → traffic statistics → SUMO calibration and validation.

## 3. Input

The pipeline should support recorded camera footage.

Where available, record:

- camera identifier;
- location;
- recording date/time;
- frame rate;
- resolution;
- camera viewpoint;
- weather/lighting conditions;
- observation interval.

Raw footage should not be committed to Git unless an approved storage strategy exists.

## 4. Frame Processing

Frames may be sampled at a configurable rate.

The processing rate should balance detection accuracy, tracking quality, computational cost, and temporal resolution.

Original timestamps should be preserved.

## 5. Vehicle Detection

The detector identifies vehicles in each processed frame.

Potential output:

- timestamp;
- bounding box;
- class;
- confidence.

The selected model must be evaluated for the actual camera viewpoint rather than assuming benchmark performance transfers directly.

## 6. Vehicle Classification

The classifier should map detections into categories required by the SUMO model.

Possible categories:

- two-wheeler;
- car;
- auto-rickshaw;
- bus;
- truck;
- emergency vehicle.

If a class cannot be reliably distinguished, it should be grouped or marked unknown rather than forcing an incorrect label.

## 7. Tracking

Tracking associates detections across frames.

Purposes include:

- avoiding repeated counting;
- estimating movement;
- associating vehicles with approaches or lanes;
- supporting queue and flow measurements where feasible.

Tracking quality should be monitored under occlusion and dense traffic.

## 8. Counting

Counting should use clearly defined counting regions or virtual lines.

For each interval, produce counts indexed by time, approach, and vehicle type where the camera geometry permits.

## 9. Temporal Aggregation

Raw detections should be aggregated into fixed intervals such as 30 seconds, 1 minute, or 5 minutes.

The final interval should be selected according to traffic demand and calibration needs.

## 10. Quality Control

Identify:

- low-confidence detections;
- missing frames;
- tracking interruptions;
- duplicate counts;
- implausible count spikes;
- camera obstruction.

Quality flags should accompany derived statistics.

## 11. Manual Validation

A representative sample should be manually reviewed where feasible.

Compare:

- detected count with manual count;
- detected class with manual class.

Useful metrics include precision, recall, counting error, and classification accuracy.

## 12. Camera Limitations

Known limitations include:

- low light;
- glare;
- rain;
- occlusion;
- dense traffic;
- camera vibration;
- poor viewpoint;
- overlapping vehicles;
- unusual vehicle appearance.

These limitations must be recorded because camera-derived statistics are used to calibrate the simulation.

## 13. Real-to-SUMO Mapping

Vision output → quality filtering → temporal aggregation → approach/movement mapping → vehicle-type distribution → traffic demand → SUMO configuration.

Every mapping assumption must be documented.

## 14. Calibration Data vs Validation Data

Where enough footage is available, separate:

### Calibration data

Used to construct and tune the SUMO environment.

### Validation data

Used to evaluate how well the calibrated model reproduces traffic characteristics not used during calibration.

Reusing exactly the same observations for both should be avoided where practical.

## 15. Vision and RL Separation

The RL controller should not directly depend on raw image frames.

Camera → vision → structured traffic state → state adapter → RL controller.

This provides modularity, reproducibility, easier testing, and the ability to replace the detector.

## 16. Perception Uncertainty

Where possible, preserve uncertainty information such as:

- traffic count;
- confidence/quality level;
- source;
- observation interval.

This information can later support the sensor-health state.

## 17. Validation Outputs

The pipeline should produce machine-readable outputs containing:

- timestamp;
- approach/lane where measurable;
- vehicle type;
- count;
- confidence/quality flag;
- processing configuration.

These outputs can generate calibration summaries without storing raw video in the repository.

## 18. Research Use

The vision subsystem supports:

### V1 — Traffic characterization

Determine traffic composition and temporal variation.

### V2 — SUMO calibration

Provide observations for traffic-demand and vehicle-composition calibration.

### V3 — Simulation validation

Compare simulated traffic characteristics with observations not used directly for calibration.

The pipeline is therefore part of the validation methodology rather than a separate AI demonstration.

## 19. Acceptance Criteria

The vision subsystem is research-ready when:

1. it processes selected footage reproducibly;
2. it produces time-indexed vehicle counts;
3. it produces required vehicle classes where detection quality permits;
4. it records quality/confidence information;
5. a manually reviewed sample estimates counting/classification quality;
6. outputs can be mapped into SUMO demand/configuration;
7. calibration and validation datasets are distinguishable;
8. known perception limitations are documented.

## 20. Future Extensions

Possible extensions include pedestrian detection, emergency-vehicle recognition, lane-level trajectory estimation, queue-length estimation, night-time robustness evaluation, and multi-camera fusion.

These are not mandatory for the core ARVEXA implementation unless required by the selected junction and research questions.
