# Anomaly Detection In IoT Sensor Data (ML049)
**Category:** Anomaly Detection / Sensor | **ML Type:** Anomaly Detection | **Platform:** MLFORGE

## 1. Overview
IoT time-series anomaly detection system establishing baseline operating envelopes and raising alerts on sensor drift or spikes.

## 2. Problem Type & Paradigm
- **Task:** Anomaly Detection
- **Domain:** Anomaly Detection / Sensor
- **Baseline Architecture:** Dynamic Threshold Isolation Forest + Exponential Moving Z-Score

## 3. Dataset & License
- **Dataset Identifer:** `iot_telemetry_stream_sample`
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
precision, recall, f1_score, roc_auc, alert_frequency

## 6. Known Limitations
Seasonal thermal cycles can trigger false positive alerts if static thresholds are used instead of dynamic baselines.

## 7. Responsible-Use Notes
Facilitates real-time industrial monitoring and equipment safety protection.
