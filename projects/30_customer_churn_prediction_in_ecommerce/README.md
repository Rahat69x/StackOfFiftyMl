# Customer Churn Prediction In E-Commerce (ML030)
**Category:** Classification | **ML Type:** Classification | **Platform:** MLFORGE

## 1. Overview
E-commerce customer retention engine predicting churn likelihood from RFM (Recency, Frequency, Monetary) purchase statistics and engagement drop-offs.

## 2. Problem Type & Paradigm
- **Task:** Classification
- **Domain:** Classification
- **Baseline Architecture:** Gradient Boosted Classifier + SHAP Explainability

## 3. Dataset & License
- **Dataset Identifer:** `ecommerce_churn_sample`
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
Does not observe external competitor promotions or offline life events driving customer disengagement.

## 7. Responsible-Use Notes
Empowers customer success teams to offer proactive retention incentives.
