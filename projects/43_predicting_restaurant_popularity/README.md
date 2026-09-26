# Predicting Restaurant Popularity (ML043)
**Category:** Regression / Forecasting | **ML Type:** Regression | **Platform:** MLFORGE

## 1. Overview
Hospitality business intelligence module forecasting table footfall, reservation demand, and review velocity for dining venues.

## 2. Problem Type & Paradigm
- **Task:** Regression
- **Domain:** Regression / Forecasting
- **Baseline Architecture:** Spatial Density + Cuisine Sentiment Gradient Booster

## 3. Dataset & License
- **Dataset Identifer:** `dining_venues_sample`
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
Sudden health inspections or local viral social media posts produce sharp discontinuities.

## 7. Responsible-Use Notes
Provides decision support for restaurateurs and culinary entrepreneurs.
