# Anomaly Detection In Network Traffic (ML010)
**Category:** Security / Anomaly Detection | **ML Type:** Anomaly Detection | **Platform:** MLFORGE

## 1. Overview
Cybersecurity anomaly detection engine analyzing packet headers, flow rates, and protocol behaviors to flag intrusions.

## 2. Problem Type & Paradigm
- **Task:** Anomaly Detection
- **Domain:** Security / Anomaly Detection
- **Baseline Architecture:** Isolation Forest + Robust Scaler / Autoencoder

## 3. Dataset & License
- **Dataset Identifer:** `network_packets_sample`
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
precision, recall, f1_score, roc_auc, anomaly_ratio

## 6. Known Limitations
Zero-day network attacks mimicking legitimate high-bandwidth services may produce false negatives.

## 7. Responsible-Use Notes
Automated security alerts must be reviewed by security operations analysts before enacting automated network cutoffs.
