# Predicting Employee Performance (ML037)
**Category:** Regression / Classification | **ML Type:** Regression | **Platform:** MLFORGE

## 1. Overview
HR analytics research module modeling employee project velocity with explicit algorithmic bias and disparate impact fairness constraints.

## 2. Problem Type & Paradigm
- **Task:** Regression
- **Domain:** Regression / Classification
- **Baseline Architecture:** Constrained Fair Linear Model + Disparate Impact Auditor

## 3. Dataset & License
- **Dataset Identifer:** `hr_evaluations_sample`
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
mae, r2_score, disparate_impact_ratio, equal_opportunity_diff

## 6. Known Limitations
Standard quantitative metrics cannot capture mentorship, team morale contributions, or unrecorded collaborative assistance.

## 7. Responsible-Use Notes
STRICT ETHICS & LABOR POLICY: Strictly prohibited from making automated hiring, promotion, salary, or termination decisions.
