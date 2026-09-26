# Model Card: Customer Review Topic Classification (ML024)

## Model Details
- **Developer:** MLFORGE Team
- **Model Date:** September 2026
- **Model Version:** 1.0.0
- **Model Type:** TF-IDF + Multinomial Naive Bayes / SGD Topic Classifier
- **License:** MIT Research License

## Intended Use
- **Primary Intended Uses:** Research, benchmarking, educational exploration, and decision-support simulation.
- **Out of Scope Uses:** Enables triage of operational pain points across cross-functional product departments.

## Factors, Metrics & Evaluation Data
- **Target Metrics:** accuracy, precision, recall, f1_score, confusion_matrix
- **Dataset:** `feedback_topics_sample` with stratified splits and cross-validation.

## Ethical Considerations & Responsible AI
Enables triage of operational pain points across cross-functional product departments.

## Caveats and Recommendations
Multi-topic reviews with conflicting sub-themes may be assigned only to the primary dominant keyword class.
