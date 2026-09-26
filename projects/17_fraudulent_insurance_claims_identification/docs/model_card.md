# Model Card: Fraudulent Insurance Claims Identification (ML017)

## Model Details
- **Developer:** MLFORGE Team
- **Model Date:** September 2026
- **Model Version:** 1.0.0
- **Model Type:** Cost-Sensitive Random Forest + SMOTE / Permutation Explainability
- **License:** MIT Research License

## Intended Use
- **Primary Intended Uses:** Research, benchmarking, educational exploration, and decision-support simulation.
- **Out of Scope Uses:** STRICT ETHICAL NOTICE: Never automatically deny claims based solely on model scores; requires human claims adjustor review.

## Factors, Metrics & Evaluation Data
- **Target Metrics:** precision, recall, f1_score, roc_auc, pr_auc
- **Dataset:** `insurance_claims_sample` with stratified splits and cross-validation.

## Ethical Considerations & Responsible AI
STRICT ETHICAL NOTICE: Never automatically deny claims based solely on model scores; requires human claims adjustor review.

## Caveats and Recommendations
New fraudulent syndicates deliberately alter claims patterns to circumvent static rules.
