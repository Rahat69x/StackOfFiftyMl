# Predicting Weather Patterns (ML013)
**Category:** Time Series | **ML Type:** Regression | **Platform:** MLFORGE

## 1. Overview
Multivariate meteorological prediction module forecasting temperature, barometric pressure, humidity, and precipitation probability.

## 2. Problem Type & Paradigm
- **Task:** Regression
- **Domain:** Time Series
- **Baseline Architecture:** Multivariate Weather Regressor (LightGBM/RandomForest)

## 3. Dataset & License
- **Dataset Identifer:** `meteorological_obs_sample`
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
mae, rmse, r2_score

## 6. Known Limitations
Atmospheric chaos limits deterministic long-range forecasts past short-term horizons.

## 7. Responsible-Use Notes
Research forecasting module. For life-safety severe storm alerts, rely on national meteorological authorities.
