# Demand Forecasting For Products (ML015)
**Category:** Time Series / Forecasting | **ML Type:** Regression | **Platform:** MLFORGE

## 1. Overview
Supply chain product demand forecasting tool modeling promotional lifts, seasonality, and stocking requirements.

## 2. Problem Type & Paradigm
- **Task:** Regression
- **Domain:** Time Series / Forecasting
- **Baseline Architecture:** Poisson/Gamma Regressor + Seasonal Decomposition

## 3. Dataset & License
- **Dataset Identifer:** `retail_sales_sample`
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
mae, rmse, wmape, r2_score

## 6. Known Limitations
Black swan events and abrupt macroeconomic supply shocks cannot be inferred from historical sales records alone.

## 7. Responsible-Use Notes
Provides decision support for supply chain logistics managers.
