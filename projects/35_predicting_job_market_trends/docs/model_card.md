# Model Card: Predicting Job Market Trends (ML035)

## Model Details
- **Developer:** MLFORGE Team
- **Model Date:** September 2026
- **Model Version:** 1.0.0
- **Model Type:** Skill Frequency Extractor + Trend Forecaster
- **License:** MIT Research License

## Intended Use
- **Primary Intended Uses:** Research, benchmarking, educational exploration, and decision-support simulation.
- **Out of Scope Uses:** Provides macro labor intelligence; must not be used to make discriminatory individual employment or compensation decisions.

## Factors, Metrics & Evaluation Data
- **Target Metrics:** mae, rmse, growth_rate_error
- **Dataset:** `job_postings_sample` with stratified splits and cross-validation.

## Ethical Considerations & Responsible AI
Provides macro labor intelligence; must not be used to make discriminatory individual employment or compensation decisions.

## Caveats and Recommendations
Posting volume fluctuations can be skewed by duplicate aggregator postings and phantom job listings.
