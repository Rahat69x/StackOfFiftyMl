# Model Card: Cancer Type Prediction From Medical Imaging (ML019)

## Model Details
- **Developer:** MLFORGE Team
- **Model Date:** September 2026
- **Model Version:** 1.0.0
- **Model Type:** Pretrained CNN Feature Extractor + Calibrated Classifier
- **License:** MIT Research License

## Intended Use
- **Primary Intended Uses:** Research, benchmarking, educational exploration, and decision-support simulation.
- **Out of Scope Uses:** STRICT MEDICAL DISCLAIMER: Research-only demonstrator. Under no circumstances should this be used for clinical diagnostic decision-making.

## Factors, Metrics & Evaluation Data
- **Target Metrics:** sensitivity, specificity, precision, recall, roc_auc, confusion_matrix
- **Dataset:** `histopathology_imaging_sample` with stratified splits and cross-validation.

## Ethical Considerations & Responsible AI
STRICT MEDICAL DISCLAIMER: Research-only demonstrator. Under no circumstances should this be used for clinical diagnostic decision-making.

## Caveats and Recommendations
Staining differences across medical institutions can cause domain shift errors.
