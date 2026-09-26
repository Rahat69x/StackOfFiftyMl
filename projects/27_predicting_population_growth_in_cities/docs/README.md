# Predicting Population Growth In Cities (ML027)
**Category:** Time Series | **ML Type:** Regression | **Platform:** MLFORGE

## 1. Overview
Demographic forecasting module projecting municipal urban population growth from birth rates, migration velocity, and economic indicators.

## 2. Problem Type & Paradigm
- **Task:** Regression
- **Domain:** Time Series
- **Baseline Architecture:** Exponential Smoothing + Demographic Factor Regressor

## 3. Dataset & License
- **Dataset Identifer:** `demographic_census_sample`
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
mae, rmse, mape, r2_score

## 6. Known Limitations
Cannot predict sudden refugee influxes or mass outward relocations caused by natural disasters.

## 7. Responsible-Use Notes
Intended for municipal civil infrastructure capacity planning (schools, water, transit).
