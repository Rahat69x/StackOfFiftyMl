# Fraudulent Insurance Claims Identification (ML017)
**Category:** Security / Fraud | **ML Type:** Classification | **Platform:** MLFORGE

## 1. Overview
Insurance fraud anomaly detection model targeting severe class imbalance with interpretable feature contributions.

## 2. Problem Type & Paradigm
- **Task:** Classification
- **Domain:** Security / Fraud
- **Baseline Architecture:** Cost-Sensitive Random Forest + SMOTE / Permutation Explainability

## 3. Dataset & License
- **Dataset Identifer:** `insurance_claims_sample`
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
precision, recall, f1_score, roc_auc, pr_auc

## 6. Known Limitations
New fraudulent syndicates deliberately alter claims patterns to circumvent static rules.

## 7. Responsible-Use Notes
STRICT ETHICAL NOTICE: Never automatically deny claims based solely on model scores; requires human claims adjustor review.
