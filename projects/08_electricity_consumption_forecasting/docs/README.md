# Electricity Consumption Forecasting (ML008)
**Category:** Time Series | **ML Type:** Regression | **Platform:** MLFORGE

## 1. Overview
Time-series forecasting system for electrical load and grid consumption incorporating temporal cyclic features and weather indicators.

## 2. Problem Type & Paradigm
- **Task:** Regression
- **Domain:** Time Series
- **Baseline Architecture:** Multi-Horizon Lagged Regressor (XGBoost/RandomForest)

## 3. Dataset & License
- **Dataset Identifer:** `grid_consumption_sample`
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
mae, rmse, r2_score, mape

## 6. Known Limitations
Unprecedented grid outages and unannounced industrial shutdowns cannot be anticipated from historical cyclical data alone.

## 7. Responsible-Use Notes
Intended to assist grid balancing simulations and energy conservation strategies.
