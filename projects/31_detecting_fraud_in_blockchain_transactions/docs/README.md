# Detecting Fraud In Blockchain Transactions (ML031)
**Category:** Security / Fraud | **ML Type:** Anomaly Detection | **Platform:** MLFORGE

## 1. Overview
Cryptocurrency transaction fraud detection module identifying wash trading, mixing patterns, and illicit wallet interactions.

## 2. Problem Type & Paradigm
- **Task:** Anomaly Detection
- **Domain:** Security / Fraud
- **Baseline Architecture:** Graph Node Feature Aggregator + One-Class SVM

## 3. Dataset & License
- **Dataset Identifer:** `crypto_transactions_sample`
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
precision, recall, f1_score, roc_auc, anomaly_score

## 6. Known Limitations
Rapidly evolving cryptographic obfuscation mixers and cross-chain hops may evade single-chain heuristics.

## 7. Responsible-Use Notes
Supports AML (Anti-Money Laundering) compliance research; outputs require human forensic validation.
