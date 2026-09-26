# Model Card: Predicting Building Energy Consumption (ML025)

## Model Details
- **Developer:** MLFORGE Team
- **Model Date:** September 2026
- **Model Version:** 1.0.0
- **Model Type:** Multi-layer Perceptron / Ridge Regressor
- **License:** MIT Research License

## Intended Use
- **Primary Intended Uses:** Research, benchmarking, educational exploration, and decision-support simulation.
- **Out of Scope Uses:** Aids energy audits and carbon footprint reduction planning.

## Factors, Metrics & Evaluation Data
- **Target Metrics:** mae, rmse, r2_score, cv_rmse
- **Dataset:** `hvac_building_sample` with stratified splits and cross-validation.

## Ethical Considerations & Responsible AI
Aids energy audits and carbon footprint reduction planning.

## Caveats and Recommendations
Anomalous tenant behavior (e.g. unmonitored space heaters) can induce forecast skew.
