# Autism Detection From Behavioral Data (ML038)
**Category:** Classification / Healthcare Research | **ML Type:** Classification | **Platform:** MLFORGE

## 1. Overview
Research-oriented behavioral indicator analysis module evaluating developmental screening questionnaire responses.

## 2. Problem Type & Paradigm
- **Task:** Classification
- **Domain:** Classification / Healthcare Research
- **Baseline Architecture:** Interpretable Logistic Regression / Support Vector Classifier

## 3. Dataset & License
- **Dataset Identifer:** `autism_screening_sample`
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
sensitivity, specificity, f1_score, roc_auc, demographic_parity

## 6. Known Limitations
Screening inventories are culturally calibrated and cannot replace neurodevelopmental clinical observation.

## 7. Responsible-Use Notes
STRICT CLINICAL DISCLAIMER: Research demo only. Under no circumstances does this provide clinical diagnosis or diagnostic classification.
