# Model Card: Identifying Recyclable Items From Images (ML029)

## Model Details
- **Developer:** MLFORGE Team
- **Model Date:** September 2026
- **Model Version:** 1.0.0
- **Model Type:** Fine-Tuned Transfer Learning CNN (MobileNet)
- **License:** MIT Research License

## Intended Use
- **Primary Intended Uses:** Research, benchmarking, educational exploration, and decision-support simulation.
- **Out of Scope Uses:** Aids automated robotic recycling sorting facilities and consumer education.

## Factors, Metrics & Evaluation Data
- **Target Metrics:** accuracy, precision, recall, f1_score, confusion_matrix
- **Dataset:** `waste_sorting_sample` with stratified splits and cross-validation.

## Ethical Considerations & Responsible AI
Aids automated robotic recycling sorting facilities and consumer education.

## Caveats and Recommendations
Crushed, soiled, or composite multi-material packaging (e.g. foil-lined cardboard) can lead to misclassification.
