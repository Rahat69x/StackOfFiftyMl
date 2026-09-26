# Predicting Customer Churn In Marketing (ML047)
**Category:** Classification | **ML Type:** Classification | **Platform:** MLFORGE

## 1. Overview
Marketing campaign analytics engine identifying customer churn risks based on email open rates, loyalty points, and campaign decay.

## 2. Problem Type & Paradigm
- **Task:** Classification
- **Domain:** Classification
- **Baseline Architecture:** Calibrated Logistic Regression / Random Forest Classifier

## 3. Dataset & License
- **Dataset Identifer:** `marketing_campaigns_sample`
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
precision, recall, f1_score, roc_auc, lift_score

## 6. Known Limitations
Privacy changes in email tracking (e.g. proxy caching) introduce noise into open-rate features.

## 7. Responsible-Use Notes
Empowers marketing teams to optimize communication frequency and avoid customer fatigue.
