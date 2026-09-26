# Model Card: Electricity Consumption Forecasting (ML008)

## Model Details
- **Developer:** MLFORGE Team
- **Model Date:** September 2026
- **Model Version:** 1.0.0
- **Model Type:** Multi-Horizon Lagged Regressor (XGBoost/RandomForest)
- **License:** MIT Research License

## Intended Use
- **Primary Intended Uses:** Research, benchmarking, educational exploration, and decision-support simulation.
- **Out of Scope Uses:** Intended to assist grid balancing simulations and energy conservation strategies.

## Factors, Metrics & Evaluation Data
- **Target Metrics:** mae, rmse, r2_score, mape
- **Dataset:** `grid_consumption_sample` with stratified splits and cross-validation.

## Ethical Considerations & Responsible AI
Intended to assist grid balancing simulations and energy conservation strategies.

## Caveats and Recommendations
Unprecedented grid outages and unannounced industrial shutdowns cannot be anticipated from historical cyclical data alone.
