# ARVEXA — Capstone-3 Sprint & Slice Specification

> **Phase 3 of 3 | Real-World Grounding, Validation & Final System**
> Sprints 9–12 | Slices C3-S01 to C3-S40

---

## Phase Overview

| Field | Value |
|---|---|
| **Capstone** | 3 |
| **Theme** | Validation, Integration & Final Evaluation |
| **Sprint Range** | SPR-09 — SPR-12 |
| **Slice Range** | C3-S01 — C3-S40 |
| **Primary Deliverable** | Validated ARVEXA system + full research results + thesis/report |

## Phase Guiding Question

> *Does the system designed and evaluated in Capstone-2 remain meaningful when grounded in real traffic observations?*

This phase is not an opportunity to add more RL features. It answers the grounding question through a computer vision pipeline, a rigorous real-to-SUMO calibration process, end-to-end integration, and final statistical evaluation.

## Phase Entry Criteria

- All Capstone-2 exit criteria satisfied
- Trained and evaluated ARVEXA controller checkpoint available
- Camera access to the selected junction (C1-S21) confirmed for Capstone-3

## Phase Exit Criteria

- [ ] Computer vision pipeline processes real camera footage end-to-end
- [ ] SUMO simulation is calibrated against real traffic observations (calibration metric satisfied)
- [ ] Calibration and validation datasets are separate and documented
- [ ] Vision pipeline output is connected to the ARVEXA state builder
- [ ] End-to-end pipeline (camera → state → controller → signal command) runs without errors
- [ ] Final baseline and ARVEXA experiments cover all scenarios
- [ ] Multi-objective trade-off, sensor-failure, pedestrian-safety, and emergency-priority evaluations are complete
- [ ] Final ablation study is complete
- [ ] Statistical analysis with significance testing is complete
- [ ] All results are reproducible from a submitted reproducibility package
- [ ] Thesis/report is submitted

---

## Sprint 9 — Computer Vision Pipeline

| Field | Value |
|---|---|
| **Sprint ID** | SPR-09 |
| **Capstone** | 3 |
| **Goal** | Build the camera-to-traffic-statistics pipeline: ingest real video footage and produce per-approach vehicle counts and type distributions |
| **Entry Criteria** | Capstone-2 exit satisfied; camera footage of the selected junction is available |
| **Exit Criteria** | Pipeline processes video end-to-end and produces per-approach flow statistics with quantified detection accuracy |

---

### C3-S01 — Video Ingestion

**Objective**
Implement a module that loads video files or live camera streams and emits a sequence of frames for downstream processing, with configurable frame-rate subsampling.

**Inputs**
- Recorded camera footage from the selected junction (C1-S21)
- Camera metadata (resolution, frame rate — to be produced in C3-S10)

**Outputs**
- `src/vision/video_ingestor.py`
- Frame generator interface (yields frames with timestamps)

**Acceptance Criteria**
- [ ] Accepts both file path and RTSP/stream URL inputs
- [ ] Frame-rate subsampling is configurable (process every N-th frame)
- [ ] Timestamp is attached to each emitted frame
- [ ] Module handles end-of-stream gracefully (no crash, emits termination signal)
- [ ] Unit test processes a short sample video clip without error

**Dependencies** — C1-S21

---

### C3-S02 — Frame Preprocessing

**Objective**
Implement frame preprocessing: resizing to model input dimensions, normalisation, and an optional quality/blur check to skip uninformative frames.

**Inputs**
- `src/vision/video_ingestor.py` (C3-S01)
- Detection model input requirements (C3-S03 forward reference)

**Outputs**
- `src/vision/frame_preprocessor.py`
- Preprocessed frame tensors ready for detection

**Acceptance Criteria**
- [ ] Output frame dimensions match the configured model input size
- [ ] Pixel values are normalised to [0, 1] or model-expected range
- [ ] Frames below a configurable blur score are flagged and optionally skipped
- [ ] Processing rate is logged (frames/second)

**Dependencies** — C3-S01

---

### C3-S03 — Vehicle Detection

**Objective**
Integrate a pre-trained object detection model to locate vehicles in each frame, producing bounding boxes with confidence scores.

**Inputs**
- `src/vision/frame_preprocessor.py` (C3-S02)
- Detection model (e.g., YOLOv8 or equivalent) and weights

**Outputs**
- `src/vision/vehicle_detector.py`
- Per-frame detection output: list of (bbox, confidence, raw_class_id)

**Acceptance Criteria**
- [ ] Model is loaded from a local weights file (not downloaded at runtime)
- [ ] Detections below a configurable confidence threshold are filtered
- [ ] Output schema is documented: (x1, y1, x2, y2, confidence, class_id)
- [ ] Inference runs on CPU and optionally GPU; device is configurable
- [ ] Unit test runs on a sample frame with at least one vehicle present

**Dependencies** — C3-S02

---

### C3-S04 — Vehicle Classification

**Objective**
Map raw detection class IDs to the ARVEXA vehicle type categories (car, truck/bus, motorcycle, emergency vehicle) used by the state representation.

**Inputs**
- `src/vision/vehicle_detector.py` (C3-S03)
- Vehicle-type model (C1-S24): ARVEXA category definitions

**Outputs**
- Vehicle classification output: each detection now carries an ARVEXA category label
- `config/vision/class-mapping.yaml`: raw model class → ARVEXA category

**Acceptance Criteria**
- [ ] Class mapping is fully configurable via YAML (no hard-coded label strings)
- [ ] Emergency vehicle category is mapped (e.g., from ambulance, fire truck classes)
- [ ] Unknown/unmapped class IDs are logged as 'unknown' and not silently dropped
- [ ] Unit test covers each ARVEXA category mapping

**Dependencies** — C3-S03, C1-S24

---

### C3-S05 — Vehicle Tracking

**Objective**
Implement multi-object tracking to maintain consistent vehicle IDs across frames, enabling counting of unique vehicles rather than per-frame detections.

**Inputs**
- `src/vision/vehicle_detector.py` (C3-S03), classification (C3-S04)
- Tracking algorithm (e.g., ByteTrack, SORT, or BoT-SORT)

**Outputs**
- `src/vision/vehicle_tracker.py`
- Per-frame tracked object list: (track_id, bbox, category, confidence)

**Acceptance Criteria**
- [ ] Each tracked vehicle maintains a consistent ID across frames
- [ ] Track ID is created on first detection and terminated after a configurable number of missed frames
- [ ] Tracker is configurable: maximum age, minimum hits before confirmation
- [ ] Unit test demonstrates consistent ID assignment across 10 consecutive frames

**Dependencies** — C3-S03, C3-S04

---

### C3-S06 — Region & Counting Line Definition

**Objective**
Define counting lines and regions of interest (ROIs) for each junction approach using the camera's perspective of the junction geometry.

**Inputs**
- Junction geometry (C1-S21): approach lanes and directions
- Camera metadata (C3-S10 — prepare early draft): field of view, mounting position

**Outputs**
- `config/vision/counting-lines.yaml`: per-approach line coordinates in image space
- Visual confirmation overlay image showing lines on a sample frame

**Acceptance Criteria**
- [ ] At least one counting line per junction approach
- [ ] Counting lines are defined in pixel coordinates and are camera-specific
- [ ] Direction of crossing (inbound/outbound) is defined per line
- [ ] Visual overlay confirms correct placement on a sample frame

**Dependencies** — C3-S05, C1-S21

---

### C3-S07 — Vehicle Counting

**Objective**
Count vehicles crossing each defined counting line per time interval and direction, using the tracking output to avoid double-counting a single vehicle.

**Inputs**
- `src/vision/vehicle_tracker.py` (C3-S05)
- Counting line definitions (C3-S06)

**Outputs**
- `src/vision/vehicle_counter.py`
- Per-interval count: (approach, direction, vehicle_category, count, timestamp)

**Acceptance Criteria**
- [ ] Each unique track ID is counted at most once per crossing per line
- [ ] Counts are aggregated per configurable time interval (e.g., 30 s, 5 min)
- [ ] Category-level counts (car, truck, emergency) are available alongside total
- [ ] Counts are logged to CSV with timestamps

**Dependencies** — C3-S05, C3-S06

---

### C3-S08 — Traffic-Statistics Aggregation

**Objective**
Aggregate per-crossing vehicle counts into traffic flow statistics (vehicles/hour per approach) and type distributions. Output must be compatible with the ARVEXA state builder interface.

**Inputs**
- `src/vision/vehicle_counter.py` (C3-S07)
- State representation spec (C1-S14): required state elements sourced from vision

**Outputs**
- `src/vision/traffic_statistics.py`
- Traffic statistics output: per-approach flow (veh/hr), type distribution, aggregation interval

**Acceptance Criteria**
- [ ] Output fields match the state elements that the vision pipeline is intended to supply (from C1-S14)
- [ ] Aggregation interval is configurable
- [ ] Output is in a format directly consumable by the vision-state adapter (C3-S18)
- [ ] Output is logged to CSV per aggregation interval

**Dependencies** — C3-S07, C1-S14

---

### C3-S09 — Detection Accuracy Evaluation

**Objective**
Evaluate the vision pipeline's vehicle detection and classification accuracy on a labelled sample, providing empirical evidence of pipeline reliability.

**Inputs**
- `src/vision/vehicle_detector.py` (C3-S03), classification (C3-S04)
- Manually labelled ground truth set (minimum 200 frames with bounding boxes and categories)

**Outputs**
- `src/analysis/vision_accuracy.py`
- Detection metrics: Precision, Recall, mAP@0.5, mAP@0.5:0.95
- Classification metrics: per-category accuracy, confusion matrix

**Acceptance Criteria**
- [ ] Ground truth annotation format is documented
- [ ] Precision ≥ 0.80 and Recall ≥ 0.75 at the configured confidence threshold (or alternative thresholds justified)
- [ ] Per-category performance is reported (car, truck, emergency)
- [ ] Emergency vehicle detection performance is specifically highlighted

**Dependencies** — C3-S03, C3-S04

---

## Sprint 10 — Real-to-SUMO Calibration & Validation

| Field | Value |
|---|---|
| **Sprint ID** | SPR-10 |
| **Capstone** | 3 |
| **Goal** | Connect real camera observations to the SUMO simulation through a rigorous calibration process, with calibration and validation datasets kept strictly separate |
| **Entry Criteria** | Sprint 9 complete; at least 2 hours of camera footage processed by the vision pipeline |
| **Exit Criteria** | SUMO calibrated to meet the defined calibration metric; validation dataset prepared and held out; calibration/validation split documented |

---

### C3-S10 — Camera Metadata Preparation

**Objective**
Document the physical camera setup at the selected junction: position, mounting height, angle, field of view, resolution, and frame rate. This metadata underpins counting-line placement and calibration.

**Inputs**
- Physical camera installation at the junction (C1-S21)

**Outputs**
- `docs/vision/camera-metadata.md`
- Per-camera config YAML: position (GPS + height), angle, resolution, frame rate

**Acceptance Criteria**
- [ ] GPS coordinates and mounting height are recorded for each camera
- [ ] Field of view (horizontal and vertical degrees) is estimated or measured
- [ ] Resolution and frame rate are documented
- [ ] Metadata is sufficient to reconstruct counting-line placement (C3-S06)

**Dependencies** — C1-S21

---

### C3-S11 — Real Traffic Demand Extraction

**Objective**
Process the vision pipeline output to produce a time-series dataset of vehicle flow counts per junction approach from the real camera footage.

**Inputs**
- Traffic statistics output (C3-S08)
- Camera footage (calibration period)

**Outputs**
- `data/real-traffic/flow-counts.csv`: timestamp | approach | direction | category | count
- `docs/data/real-traffic-dataset-notes.md`

**Acceptance Criteria**
- [ ] Flow counts cover at least 1 hour of representative traffic
- [ ] All junction approaches are represented
- [ ] Vehicle category breakdown (car, truck, motorcycle, emergency) is included
- [ ] Dataset is version-controlled and checksum-logged for reproducibility

**Dependencies** — C3-S08

---

### C3-S12 — Vehicle-Type Distribution Extraction

**Objective**
Compute the proportion of each vehicle type in the real traffic flow from the camera dataset. This will be used to calibrate SUMO's vehicle type mix.

**Inputs**
- `data/real-traffic/flow-counts.csv` (C3-S11)
- Classification output (C3-S04)

**Outputs**
- `data/real-traffic/vehicle-type-distribution.csv`: approach | category | proportion
- Distribution documented per time period (AM peak, PM peak, off-peak)

**Acceptance Criteria**
- [ ] Type proportions sum to 1.0 per approach per period
- [ ] At least 3 time periods are analysed if sufficient footage is available
- [ ] Distribution is compared to the assumed distribution in C1-S24 (with delta noted)

**Dependencies** — C3-S11, C3-S04

---

### C3-S13 — Traffic-Flow Calibration

**Objective**
Adjust the SUMO demand files to match the real observed vehicle flow rates from the camera dataset. This is the primary demand-level calibration step.

**Inputs**
- `data/real-traffic/flow-counts.csv` (C3-S11)
- `sumo/demand/traffic-demand.rou.xml` (C1-S23)
- SUMO calibration plan (C1-S29)

**Outputs**
- `sumo/demand/traffic-demand-calibrated.rou.xml`
- Calibration report: observed flow vs simulated flow per approach (before and after)

**Acceptance Criteria**
- [ ] Calibrated demand file is distinct from the original (version-controlled separately)
- [ ] Calibration report includes GEH statistic or RMSE per approach
- [ ] Calibration metric from C1-S29 is evaluated and reported
- [ ] Calibration is documented step-by-step (reproducible without the researcher)

**Dependencies** — C3-S11, C1-S23, C1-S29

---

### C3-S14 — SUMO Parameter Calibration

**Objective**
Adjust SUMO microscopic behavioural parameters (headway distribution, speed distribution, driver aggressiveness) to match real observed traffic behaviour beyond flow counts.

**Inputs**
- `data/real-traffic/flow-counts.csv` (C3-S11)
- `data/real-traffic/vehicle-type-distribution.csv` (C3-S12)
- SUMO vehicle type file (C1-S24), calibration plan (C1-S29)

**Outputs**
- `sumo/demand/vehicle-types-calibrated.add.xml`
- Parameter calibration report: parameter | original value | calibrated value | justification

**Acceptance Criteria**
- [ ] At least 3 behavioural parameters are adjusted (e.g., τ (headway), σ (speed deviation), accel)
- [ ] Each change is justified by an observable difference between real and simulated behaviour
- [ ] Calibrated vehicle type file is version-controlled separately from original

**Dependencies** — C3-S12, C1-S24, C1-S29

---

### C3-S15 — Real-vs-SUMO Traffic Comparison

**Objective**
Compare simulated traffic metrics (post-calibration) against real traffic observations to quantify how well the calibrated SUMO model represents reality.

**Inputs**
- Calibrated demand (C3-S13) and parameters (C3-S14)
- `data/real-traffic/flow-counts.csv` (C3-S11)
- Evaluation metrics (C1-S31)

**Outputs**
- `docs/experiments/calibration-comparison-report.md`
- Comparison table: metric | real value | simulated value | GEH / RMSE / % error

**Acceptance Criteria**
- [ ] GEH ≤ 5 for ≥ 85% of directional flows (or alternative threshold justified)
- [ ] Per-approach comparison is presented
- [ ] Residual errors are analysed and their potential impact on ARVEXA evaluation is discussed
- [ ] Report is sufficient evidence of calibration quality for the thesis

**Dependencies** — C3-S13, C3-S14, C3-S11

---

### C3-S16 — Validation Dataset Preparation

**Objective**
Prepare a held-out traffic dataset from a different time period (not used in calibration) to validate the calibrated SUMO model independently.

**Inputs**
- Camera footage from a different time period than the calibration footage

**Outputs**
- `data/real-traffic/validation-flow-counts.csv`
- Dataset notes: time period, duration, traffic conditions

**Acceptance Criteria**
- [ ] Validation footage covers a different time period than calibration footage
- [ ] Validation dataset includes at least 30 minutes of traffic
- [ ] Dataset is version-controlled and checksummed
- [ ] No data from the validation set was used in any calibration step

**Dependencies** — C3-S11

---

### C3-S17 — Calibration / Validation Separation

**Objective**
Document and enforce the strict separation between calibration and validation datasets. Produce a provenance record that makes the split auditable for academic review.

**Inputs**
- C3-S13 (calibration dataset), C3-S16 (validation dataset)

**Outputs**
- `docs/experiments/calibration-validation-protocol.md`
- Dataset provenance record: file | period | role (calibration/validation) | checksum

**Acceptance Criteria**
- [ ] Calibration and validation files are stored in separate directories
- [ ] No flow observation appears in both datasets
- [ ] Provenance record includes timestamps of data collection for each dataset
- [ ] Protocol document is referenced in the thesis as evidence of separation

**Dependencies** — C3-S13, C3-S16

---

## Sprint 11 — Full ARVEXA Integration

| Field | Value |
|---|---|
| **Sprint ID** | SPR-11 |
| **Capstone** | 3 |
| **Goal** | Connect the vision pipeline to the ARVEXA state builder and produce a single end-to-end runnable pipeline from camera input to signal command output |
| **Entry Criteria** | Sprint 10 complete; calibrated SUMO model and vision pipeline both functional |
| **Exit Criteria** | End-to-end pipeline runs without errors; experiment automation produces results for all scenarios; reproducibility pipeline passes a cold-start test |

---

### C3-S18 — Vision → Traffic-State Interface

**Objective**
Implement the adapter that converts the vision pipeline's traffic statistics output into the ARVEXA state element format consumed by the state builder.

**Inputs**
- `src/vision/traffic_statistics.py` (C3-S08)
- State representation spec (C1-S14)
- `src/environment/state_builder.py` (C2-S09)

**Outputs**
- `src/integration/vision_state_adapter.py`
- Mapping table: vision statistic → state element (documented in code and in `docs/architecture/`)

**Acceptance Criteria**
- [ ] All state elements sourced from vision have a corresponding adapter mapping
- [ ] Adapter output is type-compatible with the state builder input interface
- [ ] No state element is silently dropped or left unset if vision pipeline is running
- [ ] Unit test confirms correct mapping for a sample traffic statistics input

**Dependencies** — C3-S08, C2-S09, C1-S14

---

### C3-S19 — Sensor Uncertainty Propagation

**Objective**
Pass detection confidence scores from the vision pipeline through the state builder as uncertainty signals, updating the sensor-health state channel to reflect vision pipeline confidence.

**Inputs**
- `src/vision/vehicle_detector.py` (C3-S03): per-detection confidence
- `src/environment/sensor_health.py` (C2-S08)
- `src/integration/vision_state_adapter.py` (C3-S18)

**Outputs**
- Confidence-aware health channel: sensor health is a function of mean detection confidence in the current interval
- Updated `vision_state_adapter.py`

**Acceptance Criteria**
- [ ] Sensor health channel reflects current vision pipeline confidence (not a fixed value)
- [ ] Low-confidence frames produce reduced health indicator values
- [ ] Health channel changes are reflected in the state vector consumed by the controller
- [ ] Unit test demonstrates health channel response to varying confidence levels

**Dependencies** — C3-S18, C2-S08, C3-S03

---

### C3-S20 — Vision Degradation Handling

**Objective**
Implement fallback behaviour in the vision-state adapter when the vision pipeline produces no detections, produces below-threshold confidence, or fails entirely.

**Inputs**
- `src/integration/vision_state_adapter.py` (C3-S18)
- Sensor degradation model (C1-S20), sensor-failure requirements (C1-S09)

**Outputs**
- Fallback logic in `vision_state_adapter.py`
- Fallback modes: last-known-value, zero-fill, or fixed-default (configurable per element)

**Acceptance Criteria**
- [ ] Fallback mode for each state element is configurable (not hard-coded)
- [ ] Fallback does not violate any SR (safety requirements still enforced)
- [ ] Fallback activation is logged with reason code and timestamp
- [ ] All SFRs from C1-S09 are satisfied and referenced in code comments

**Dependencies** — C3-S18, C1-S20, C1-S09

---

### C3-S21 — Emergency-Vehicle Detection / Input

**Objective**
Connect the vision pipeline's emergency vehicle classification to the ARVEXA emergency vehicle state channel, enabling real-world emergency priority triggering.

**Inputs**
- `src/vision/vehicle_tracker.py` (C3-S05), classification (C3-S04): emergency category
- Emergency-vehicle state channel (C2-S07)
- Emergency-vehicle requirements (C1-S10)

**Outputs**
- Emergency vehicle state populated from vision pipeline in `vision_state_adapter.py`

**Acceptance Criteria**
- [ ] Emergency vehicle presence flag is set when a tracked vehicle is classified as emergency
- [ ] Approach lane and distance estimate are populated from tracker output
- [ ] False negative test: if EV is misclassified, fallback behaviour is logged
- [ ] Integration test confirms preemption is triggered when EV is detected via vision

**Dependencies** — C3-S18, C2-S07, C3-S05, C3-S04, C1-S10

---

### C3-S22 — Pedestrian Input Integration

**Objective**
Connect pedestrian detection/counting from the vision pipeline to the ARVEXA pedestrian state channel.

**Inputs**
- Pedestrian detection (requires extension of vision pipeline or separate pedestrian model)
- Pedestrian state channel (C2-S06)
- Pedestrian requirements (C1-S11)

**Outputs**
- Pedestrian state sourced from vision pipeline in `vision_state_adapter.py`
- Documentation of any pedestrian detection model used

**Acceptance Criteria**
- [ ] Pedestrian count per crossing is populated from vision output
- [ ] If pedestrian detection is not available, a documented fallback is used and justified
- [ ] Pedestrian state update respects the minimum crossing time requirement (from C1-S11)
- [ ] Unit test confirms pedestrian count is correctly mapped to state elements

**Dependencies** — C3-S18, C2-S06, C1-S11

---

### C3-S23 — End-to-End Controller Integration

**Objective**
Connect all components into a single runnable pipeline: camera footage or stream → vision pipeline → state builder → ARVEXA controller → SUMO signal command.

**Inputs**
- `src/vision/` (C3-S01 to C3-S08)
- `src/integration/vision_state_adapter.py` (C3-S18 to C3-S22)
- `src/environment/arvexa_env.py` (C2-S10)
- Trained controller checkpoint (C2-S17)

**Outputs**
- `src/integration/arvexa_pipeline.py`
- End-to-end integration test script

**Acceptance Criteria**
- [ ] Pipeline runs from a video file input to a SUMO simulation step without manual intervention
- [ ] All components are connected via documented interfaces (no direct imports across layers)
- [ ] Pipeline completes a 15-minute simulation without crashing
- [ ] Output matches the expected format from C1-S31 evaluation metrics

**Dependencies** — C3-S18, C3-S19, C3-S20, C3-S21, C3-S22, C2-S10, C2-S17

---

### C3-S24 — Experiment Automation

**Objective**
Implement scripts to run the full ARVEXA experiment suite automatically across all scenario configs, without manual intervention between scenarios.

**Inputs**
- Experiment scenarios (C1-S30)
- Reproducibility config (C1-S32)
- End-to-end pipeline (C3-S23), evaluation script (C2-S18)

**Outputs**
- `scripts/run_experiments.py`
- Experiment batch config: `config/experiments/batch.yaml`

**Acceptance Criteria**
- [ ] A single command runs all scenarios for both ARVEXA and all baselines
- [ ] Each run is tagged with a unique run-ID and scenario ID
- [ ] Failed runs are logged with error messages and do not abort the batch
- [ ] Estimated total runtime is documented so resource planning is possible

**Dependencies** — C3-S23, C1-S30, C1-S32, C2-S18

---

### C3-S25 — Configuration Management

**Objective**
Consolidate all experiment, model, vision, and pipeline configuration into a clean, hierarchical config structure that eliminates ambiguity about which configuration was used for any given run.

**Inputs**
- All config files from prior sprints (environment, reward, training, vision, experiment)

**Outputs**
- `config/` reorganised into: `environment/`, `model/`, `experiments/`, `vision/`, `safety/`
- `config/README.md` describing each config file and its parameters

**Acceptance Criteria**
- [ ] No tunable parameter is hard-coded anywhere in `src/`
- [ ] Every config file is documented (parameter name, type, default, description)
- [ ] Config version is embedded in all run outputs
- [ ] A config diff between two run outputs is sufficient to explain any performance difference

**Dependencies** — All prior config-producing slices

---

### C3-S26 — Result Logging

**Objective**
Implement structured result logging that produces a complete, self-contained result record per run: metrics, config snapshot, run ID, timestamps, and seed.

**Inputs**
- Reproducibility config (C1-S32)
- Experiment automation (C3-S24), evaluation script (C2-S18)

**Outputs**
- `src/logging/result_logger.py`
- `results/` directory structure: `results/{run_id}/{scenario_id}/metrics.json`

**Acceptance Criteria**
- [ ] Every run produces a `metrics.json` containing all metrics from C1-S31
- [ ] `metrics.json` includes: run_id, scenario_id, seed, config_hash, start_time, end_time
- [ ] Results directory is self-contained (can be archived and inspected without running code)
- [ ] Logger does not raise on disk-full or permission errors (logs warning instead)

**Dependencies** — C3-S24, C1-S31, C1-S32

---

### C3-S27 — Reproducibility Pipeline

**Objective**
Document and validate the complete pipeline for reproducing all results from scratch: from a clean environment install to final metrics output.

**Inputs**
- C3-S24 (automation), C3-S25 (config), C3-S26 (logging), C1-S32 (reproducibility config)

**Outputs**
- `docs/experiments/reproducibility-guide.md` (final, complete version)
- README section with exact commands to reproduce any run from its run-ID
- Cold-start test: fresh environment → all results passing

**Acceptance Criteria**
- [ ] A team member who has not run the code before can reproduce any result following the guide
- [ ] Cold-start test passes: clean virtual environment → `run_experiments.py` → results match logged checksums
- [ ] All data dependencies (model weights, demand files, calibrated SUMO configs) are documented
- [ ] Reproducibility guide is ready for inclusion in the thesis

**Dependencies** — C3-S24, C3-S25, C3-S26, C1-S32

---

## Sprint 12 — Final Evaluation & Capstone-3

| Field | Value |
|---|---|
| **Sprint ID** | SPR-12 |
| **Capstone** | 3 |
| **Goal** | Produce the complete final research evidence: all experiments, statistical analysis, visualisations, reproducibility package, and submitted thesis/report |
| **Entry Criteria** | Sprint 11 complete; end-to-end pipeline validated; experiment automation tested |
| **Exit Criteria** | All experiment results collected; statistical analysis complete; thesis submitted; reproducibility package submitted |

---

### C3-S28 — Final Baseline Experiments

**Objective**
Run all baseline controllers (fixed-time and any additional baselines from Capstone-2) across all final experiment scenarios using the calibrated SUMO model and the reproducibility pipeline.

**Inputs**
- Fixed-time baseline (C1-S28)
- Final experiment scenarios (C1-S30, using calibrated demand from C3-S13)
- Experiment automation (C3-S24), result logging (C3-S26)

**Outputs**
- `results/final/baseline/` — complete baseline results for all scenarios and seeds

**Acceptance Criteria**
- [ ] All scenarios from C1-S30 are covered
- [ ] At least 5 seeds per scenario
- [ ] All metrics from C1-S31 are recorded per run
- [ ] Results are tagged with run-IDs and reproducible

**Dependencies** — C1-S28, C1-S30, C3-S13, C3-S24, C3-S26

---

### C3-S29 — Final ARVEXA Experiments

**Objective**
Run the final ARVEXA controller evaluation across all experiment scenarios using the calibrated SUMO model, the end-to-end integration pipeline, and the reproducibility system.

**Inputs**
- Trained ARVEXA checkpoint (C2-S17, best model)
- End-to-end pipeline (C3-S23)
- All experiment scenarios (C1-S30), result logging (C3-S26)

**Outputs**
- `results/final/arvexa/` — complete ARVEXA results for all scenarios and seeds

**Acceptance Criteria**
- [ ] All scenarios from C1-S30 are covered
- [ ] At least 5 seeds per scenario
- [ ] All metrics from C1-S31 are recorded per run
- [ ] Emergency vehicle and pedestrian scenarios are included

**Dependencies** — C2-S17, C3-S23, C1-S30, C3-S24, C3-S26, C3-S28

---

### C3-S30 — Multi-Objective Trade-Off Analysis

**Objective**
Analyse the relationship between competing objectives in ARVEXA's results: traffic efficiency vs pedestrian safety vs emergency priority. Determine whether gains in one metric come at a cost to others.

**Inputs**
- Final ARVEXA results (C3-S29)
- Reward weight configurations (C2-S24)

**Outputs**
- `docs/results/multi-objective-tradeoff-analysis.md`
- Trade-off plots: metric pairs plotted against each other across scenarios and weight configurations

**Acceptance Criteria**
- [ ] At least 3 metric pairs are analysed for trade-off (e.g., throughput vs pedestrian wait, throughput vs EV delay)
- [ ] Results are presented for at least 2 different reward weight configurations if available
- [ ] Conclusions reference the multi-objective reward architecture (C1-S16)
- [ ] Analysis is suitable for inclusion in the thesis discussion section

**Dependencies** — C3-S29, C2-S24, C1-S16

---

### C3-S31 — Sensor-Failure Evaluation (Final)

**Objective**
Produce the final sensor-failure evaluation results using the complete integrated pipeline, replicating and extending the Capstone-2 sensor resilience experiments under the calibrated scenario.

**Inputs**
- Final ARVEXA pipeline (C3-S23)
- Sensor degradation model (C1-S20)
- Capstone-2 sensor resilience results (C2-S28 to C2-S32) for reference

**Outputs**
- `results/final/sensor-failure/` — results for all 4 degradation modes under final evaluation setup

**Acceptance Criteria**
- [ ] All 4 degradation modes (missing, noisy, misclassification, partial) are evaluated
- [ ] Each mode is evaluated across ≥ 3 severity levels
- [ ] Results extend Capstone-2 findings with calibrated scenario context
- [ ] All SFRs from C1-S09 are verified in the final configuration

**Dependencies** — C3-S29, C1-S20, C2-S28, C2-S31

---

### C3-S32 — Pedestrian-Safety Evaluation (Final)

**Objective**
Evaluate ARVEXA's pedestrian safety performance: pedestrian waiting times, pedestrian phase allocation frequency, and compliance with all PRs.

**Inputs**
- Final ARVEXA results (C3-S29)
- Pedestrian requirements (C1-S11)
- Evaluation metrics for pedestrian performance (C1-S31)

**Outputs**
- `docs/results/pedestrian-safety-evaluation.md`
- Pedestrian metrics summary vs baseline

**Acceptance Criteria**
- [ ] Average and maximum pedestrian waiting time are reported per scenario
- [ ] Pedestrian phase minimum crossing time compliance rate is reported
- [ ] PR compliance is explicitly checked for all PRs from C1-S11
- [ ] Results are compared to fixed-time baseline on all pedestrian metrics

**Dependencies** — C3-S29, C1-S11, C1-S31

---

### C3-S33 — Emergency-Priority Evaluation (Final)

**Objective**
Evaluate ARVEXA's emergency vehicle clearance performance: time from EV detection to green phase grant, EV waiting time, and EVR compliance.

**Inputs**
- Final ARVEXA results (C3-S29), emergency vehicle scenarios (C1-S30)
- Emergency-vehicle requirements (C1-S10), evaluation metrics (C1-S31)

**Outputs**
- `docs/results/emergency-priority-evaluation.md`
- EV clearance time distribution (mean, 95th percentile)
- EVR compliance report

**Acceptance Criteria**
- [ ] EV detection-to-green latency is reported (mean ± std)
- [ ] EV waiting time is compared to fixed-time baseline
- [ ] Maximum EV delay from EVR is verified as satisfied in ≥ 95% of events
- [ ] Analysis covers scenarios with and without concurrent pedestrian phase

**Dependencies** — C3-S29, C1-S10, C1-S30, C1-S31

---

### C3-S34 — Ablation Study (Final)

**Objective**
Produce the final ablation study, removing each ARVEXA component in isolation and measuring the performance impact, using the fully integrated and calibrated final pipeline.

**Inputs**
- Final ARVEXA pipeline (C3-S23)
- Ablation variants from Capstone-2 (C2-S36) or retrained variants
- Statistical analysis (C3-S35 forward dependency)

**Outputs**
- `results/final/ablation/` — ablation variant results under final setup
- Ablation table: removed component | Δ metric | statistical significance

**Acceptance Criteria**
- [ ] Each reward component from C2-S19 to C2-S23 is ablated
- [ ] At least one architectural component is ablated (e.g., safety constraint layer removed)
- [ ] Ablation results are statistically analysed (significance tested)
- [ ] Table is thesis-ready

**Dependencies** — C3-S23, C2-S36, C3-S29

---

### C3-S35 — Statistical Analysis (Final)

**Objective**
Apply appropriate inferential statistics to the final experiment results, comparing ARVEXA against baselines across all scenarios and degradation modes.

**Inputs**
- Final ARVEXA results (C3-S29), baseline results (C3-S28)
- Ablation results (C3-S34)

**Outputs**
- `src/analysis/final_statistics.py`
- Full statistical report: per-metric summary tables with mean ± std, 95% CI, p-value, effect size

**Acceptance Criteria**
- [ ] Appropriate test selected per metric (parametric if normality confirmed, otherwise non-parametric)
- [ ] Multiple comparison correction applied if testing across many scenarios
- [ ] Effect size (Cohen's d or rank-biserial r) reported alongside p-values
- [ ] All statistical decisions and assumptions are documented in the thesis

**Dependencies** — C3-S29, C3-S28, C3-S34

---

### C3-S36 — Final Result Visualisation

**Objective**
Produce all charts and figures for the thesis/report: bar charts, box plots, learning curves, trade-off plots, degradation curves, and ablation heatmaps.

**Inputs**
- C3-S28 to C3-S35 (all final results)

**Outputs**
- `figures/` directory: all publication-ready figures as PDF/SVG
- `src/analysis/plot_results.py`: reproducible plotting script

**Acceptance Criteria**
- [ ] All figures are generated by a single script run (not manual copy-paste)
- [ ] Every figure used in the thesis has a corresponding entry in the plotting script
- [ ] Figures include: metric comparison bar charts, sensor degradation curves, ablation heatmap, EV/pedestrian performance plots
- [ ] All axes are labelled with units; all legends are present; colour scheme is consistent

**Dependencies** — C3-S28, C3-S29, C3-S30, C3-S31, C3-S32, C3-S33, C3-S34, C3-S35

---

### C3-S37 — Reproducibility Package

**Objective**
Package the complete ARVEXA system — code, trained model weights, calibrated SUMO configs, datasets, and result logs — into a submission-ready archive with exact reproduction instructions.

**Inputs**
- All `src/`, `config/`, `sumo/`, `data/`, `results/`, `figures/` directories
- `docs/experiments/reproducibility-guide.md` (C3-S27)

**Outputs**
- `reproducibility/` directory or `arvexa-reproducibility-package.zip`
- `reproducibility/README.md`: step-by-step instructions from clean install to final results
- Checksums for all data files

**Acceptance Criteria**
- [ ] Package is self-contained: no internet access required after install
- [ ] Step-by-step reproduction instructions are verified by a team member who did not write them
- [ ] All trained model weights are included
- [ ] All result CSVs match the figures in the thesis (verified by checksum)
- [ ] Package size is documented and any large files are noted

**Dependencies** — C3-S27, C3-S36, C3-S26

---

### C3-S38 — Final Documentation

**Objective**
Complete all code documentation, API docstrings, architecture notes, and inline comments so the codebase is understandable by a reader who is unfamiliar with it.

**Inputs**
- All `src/` modules
- `docs/` directory

**Outputs**
- Complete docstrings on all public functions, classes, and modules
- `docs/architecture/` updated to reflect final implementation
- `docs/vision/`, `docs/integration/`, `docs/analysis/` populated

**Acceptance Criteria**
- [ ] Every public function has a docstring with parameters, returns, and a usage example
- [ ] Architecture documents accurately reflect the final implementation (no stale diagrams)
- [ ] A new team member can understand the purpose of each `src/` module from its docstring alone
- [ ] Documentation is verified by at least one team member not responsible for the module

**Dependencies** — C3-S23 (final pipeline state), C3-S25 (final config state)

---

### C3-S39 — Thesis / Report

**Objective**
Write and submit the complete capstone thesis or final report documenting the ARVEXA research: problem, methodology, implementation, experiments, results, and conclusions.

**Inputs**
- All research documents from Capstone-1 (`docs/research/`, `docs/requirements/`, `docs/architecture/`)
- All result documents and figures from Capstone-2 and Capstone-3
- C3-S35 (statistical analysis), C3-S36 (figures), C3-S38 (documentation)

**Outputs**
- `thesis/arvexa-thesis.pdf` (or institutional submission format)

**Acceptance Criteria**
- [ ] Thesis covers: Introduction, Literature Review, Methodology, System Architecture, Experiments, Results, Discussion, Conclusion
- [ ] Every figure and table is numbered and referenced in the text
- [ ] Every statistical claim is backed by a test result from C3-S35
- [ ] All requirement categories (FR, SR, SFR, EVR, PR) are referenced in the evaluation
- [ ] Reproducibility package is cited with access instructions
- [ ] Submitted by institutional deadline

**Dependencies** — C3-S30, C3-S31, C3-S32, C3-S33, C3-S34, C3-S35, C3-S36

---

### C3-S40 — Final Demonstration

**Objective**
Prepare and deliver the final project demonstration showing the end-to-end ARVEXA system: camera footage → vision pipeline → controller → SUMO simulation with signal commands.

**Inputs**
- End-to-end pipeline (C3-S23)
- Sample camera footage or live camera feed
- Result figures and thesis (C3-S36, C3-S39)

**Outputs**
- Demonstration presentation (slides + live demo)
- Demo setup instructions (so the demo can be reproduced on any machine)

**Acceptance Criteria**
- [ ] Demonstration runs end-to-end without manual intervention
- [ ] SUMO visualisation (SUMO-GUI) is shown with ARVEXA controlling signals in real time
- [ ] Key results (metric improvements over baseline) are presented clearly
- [ ] Emergency vehicle and pedestrian scenarios are demonstrated
- [ ] Demo can be set up from scratch in ≤ 30 minutes using the demo instructions

**Dependencies** — C3-S23, C3-S36, C3-S39

---

## Capstone-3 Exit Checklist

| ID | Item | Status |
|---|---|---|
| C3-EX-01 | Vision pipeline processes real footage end-to-end without errors | ☐ |
| C3-EX-02 | Detection accuracy ≥ stated threshold on labelled sample | ☐ |
| C3-EX-03 | SUMO calibration metric satisfied (GEH ≤ 5 for ≥ 85% of flows or equivalent) | ☐ |
| C3-EX-04 | Calibration and validation datasets strictly separated and documented | ☐ |
| C3-EX-05 | End-to-end pipeline runs without errors for a full scenario | ☐ |
| C3-EX-06 | Final baseline experiments complete across all scenarios and seeds | ☐ |
| C3-EX-07 | Final ARVEXA experiments complete across all scenarios and seeds | ☐ |
| C3-EX-08 | Multi-objective trade-off analysis complete | ☐ |
| C3-EX-09 | Sensor-failure evaluation complete (all 4 modes) | ☐ |
| C3-EX-10 | Pedestrian-safety evaluation complete with PR compliance check | ☐ |
| C3-EX-11 | Emergency-priority evaluation complete with EVR compliance check | ☐ |
| C3-EX-12 | Final ablation study complete with statistical significance | ☐ |
| C3-EX-13 | Full statistical analysis with effect sizes complete | ☐ |
| C3-EX-14 | All figures reproducible by a single script run | ☐ |
| C3-EX-15 | Reproducibility package verified by cold-start test | ☐ |
| C3-EX-16 | Thesis / report submitted | ☐ |
| C3-EX-17 | Final demonstration delivered | ☐ |
