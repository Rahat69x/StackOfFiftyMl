# Model Card: Fake News Detection (ML014)

## Model Details
- **Developer:** MLFORGE Team
- **Model Date:** September 2026
- **Model Version:** 1.0.0
- **Model Type:** TF-IDF + PassiveAggressiveClassifier / Explainable Logistic Regression
- **License:** MIT Research License

## Intended Use
- **Primary Intended Uses:** Research, benchmarking, educational exploration, and decision-support simulation.
- **Out of Scope Uses:** Probabilistic research tool only. Output must never be used as automated censorship or definitive truth arbitration.

## Factors, Metrics & Evaluation Data
- **Target Metrics:** accuracy, precision, recall, f1_score, roc_auc
- **Dataset:** `news_articles_sample` with stratified splits and cross-validation.

## Ethical Considerations & Responsible AI
Probabilistic research tool only. Output must never be used as automated censorship or definitive truth arbitration.

## Caveats and Recommendations
Subject to bias toward mainstream publication styles; can flag satire or unorthodox legitimate investigative reporting as anomalous.
