# Model Card: Predicting Insurance Claims And Fraud (ML033)

## Model Details
- **Developer:** MLFORGE Team
- **Model Date:** September 2026
- **Model Version:** 1.0.0
- **Model Type:** Tweedie Claims Severity Regressor + Fraud Classifier
- **License:** MIT Research License

## Intended Use
- **Primary Intended Uses:** Research, benchmarking, educational exploration, and decision-support simulation.
- **Out of Scope Uses:** HIGH-IMPACT SENSITIVE: Never make automated insurance denial or price surging decisions without certified actuarial oversight.

## Factors, Metrics & Evaluation Data
- **Target Metrics:** mae, roc_auc, f1_score, gini_coefficient
- **Dataset:** `actuarial_claims_sample` with stratified splits and cross-validation.

## Ethical Considerations & Responsible AI
HIGH-IMPACT SENSITIVE: Never make automated insurance denial or price surging decisions without certified actuarial oversight.

## Caveats and Recommendations
Historical claim payouts reflect past settlement policies rather than absolute ground truth loss values.
