# Model Card: Predicting Population Growth In Cities (ML027)

## Model Details
- **Developer:** MLFORGE Team
- **Model Date:** September 2026
- **Model Version:** 1.0.0
- **Model Type:** Exponential Smoothing + Demographic Factor Regressor
- **License:** MIT Research License

## Intended Use
- **Primary Intended Uses:** Research, benchmarking, educational exploration, and decision-support simulation.
- **Out of Scope Uses:** Intended for municipal civil infrastructure capacity planning (schools, water, transit).

## Factors, Metrics & Evaluation Data
- **Target Metrics:** mae, rmse, mape, r2_score
- **Dataset:** `demographic_census_sample` with stratified splits and cross-validation.

## Ethical Considerations & Responsible AI
Intended for municipal civil infrastructure capacity planning (schools, water, transit).

## Caveats and Recommendations
Cannot predict sudden refugee influxes or mass outward relocations caused by natural disasters.
