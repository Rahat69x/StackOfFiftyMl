# Model Card: Detecting Fraud In Blockchain Transactions (ML031)

## Model Details
- **Developer:** MLFORGE Team
- **Model Date:** September 2026
- **Model Version:** 1.0.0
- **Model Type:** Graph Node Feature Aggregator + One-Class SVM
- **License:** MIT Research License

## Intended Use
- **Primary Intended Uses:** Research, benchmarking, educational exploration, and decision-support simulation.
- **Out of Scope Uses:** Supports AML (Anti-Money Laundering) compliance research; outputs require human forensic validation.

## Factors, Metrics & Evaluation Data
- **Target Metrics:** precision, recall, f1_score, roc_auc, anomaly_score
- **Dataset:** `crypto_transactions_sample` with stratified splits and cross-validation.

## Ethical Considerations & Responsible AI
Supports AML (Anti-Money Laundering) compliance research; outputs require human forensic validation.

## Caveats and Recommendations
Rapidly evolving cryptographic obfuscation mixers and cross-chain hops may evade single-chain heuristics.
