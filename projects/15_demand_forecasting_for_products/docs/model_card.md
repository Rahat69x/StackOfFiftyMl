# Model Card: Demand Forecasting For Products (ML015)

## Model Details
- **Developer:** MLFORGE Team
- **Model Date:** September 2026
- **Model Version:** 1.0.0
- **Model Type:** Poisson/Gamma Regressor + Seasonal Decomposition
- **License:** MIT Research License

## Intended Use
- **Primary Intended Uses:** Research, benchmarking, educational exploration, and decision-support simulation.
- **Out of Scope Uses:** Provides decision support for supply chain logistics managers.

## Factors, Metrics & Evaluation Data
- **Target Metrics:** mae, rmse, wmape, r2_score
- **Dataset:** `retail_sales_sample` with stratified splits and cross-validation.

## Ethical Considerations & Responsible AI
Provides decision support for supply chain logistics managers.

## Caveats and Recommendations
Black swan events and abrupt macroeconomic supply shocks cannot be inferred from historical sales records alone.
