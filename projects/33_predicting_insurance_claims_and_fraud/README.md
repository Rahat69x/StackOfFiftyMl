# Predicting Insurance Claims And Fraud (ML033)
**Category:** Security / Fraud | **ML Type:** Classification | **Platform:** MLFORGE

## 1. Overview
Combined actuarial claims cost estimation and suspicious fraud pattern identification platform.

## 2. Problem Type & Paradigm
- **Task:** Classification
- **Domain:** Security / Fraud
- **Baseline Architecture:** Tweedie Claims Severity Regressor + Fraud Classifier

## 3. Dataset & License
- **Dataset Identifer:** `actuarial_claims_sample`
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
mae, roc_auc, f1_score, gini_coefficient

## 6. Known Limitations
Historical claim payouts reflect past settlement policies rather than absolute ground truth loss values.

## 7. Responsible-Use Notes
HIGH-IMPACT SENSITIVE: Never make automated insurance denial or price surging decisions without certified actuarial oversight.
