# Predicting Building Energy Consumption (ML025)
**Category:** Regression / Forecasting | **ML Type:** Regression | **Platform:** MLFORGE

## 1. Overview
Building energy consumption forecasting tool combining architectural square footage, insulation ratings, weather, and occupancy trends.

## 2. Problem Type & Paradigm
- **Task:** Regression
- **Domain:** Regression / Forecasting
- **Baseline Architecture:** Multi-layer Perceptron / Ridge Regressor

## 3. Dataset & License
- **Dataset Identifer:** `hvac_building_sample`
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
mae, rmse, r2_score, cv_rmse

## 6. Known Limitations
Anomalous tenant behavior (e.g. unmonitored space heaters) can induce forecast skew.

## 7. Responsible-Use Notes
Aids energy audits and carbon footprint reduction planning.
