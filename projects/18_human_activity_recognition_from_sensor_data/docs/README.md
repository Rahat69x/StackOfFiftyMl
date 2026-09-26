# Human Activity Recognition From Sensor Data (ML018)
**Category:** Classification / Sensor | **ML Type:** Classification | **Platform:** MLFORGE

## 1. Overview
Wearable sensor processing system recognizing human physical activities (walking, ascending stairs, sitting, standing) from accelerometer and gyroscope streams.

## 2. Problem Type & Paradigm
- **Task:** Classification
- **Domain:** Classification / Sensor
- **Baseline Architecture:** 1D-CNN + Random Forest on Tri-axial Signals

## 3. Dataset & License
- **Dataset Identifer:** `inertial_sensor_readings_sample`
- **Sample Benchmark:** Ships with lightweight synthetic verification benchmark in `data/sample/sample_data.csv`.
- **License:** MIT / Permissive Research Use.

## 4. How to Run
```bash
# Execute standalone training smoke run
python -c "from main import get_project_instance; p = get_project_instance('.'); p.train(); print('Metrics:', p.last_metrics)"

# Run test suite
pytest tests/
```

## 5. Metrics Produced
accuracy, precision, recall, f1_score, confusion_matrix

## 6. Known Limitations
Device placement variation (pocket vs wrist) alters signal harmonics and reduces accuracy.

## 7. Responsible-Use Notes
Fitness and research tracking only; not approved as an FDA-cleared fall detection medical device.
