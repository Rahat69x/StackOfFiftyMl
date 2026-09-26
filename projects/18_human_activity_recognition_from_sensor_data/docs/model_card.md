# Model Card: Human Activity Recognition From Sensor Data (ML018)

## Model Details
- **Developer:** MLFORGE Team
- **Model Date:** September 2026
- **Model Version:** 1.0.0
- **Model Type:** 1D-CNN + Random Forest on Tri-axial Signals
- **License:** MIT Research License

## Intended Use
- **Primary Intended Uses:** Research, benchmarking, educational exploration, and decision-support simulation.
- **Out of Scope Uses:** Fitness and research tracking only; not approved as an FDA-cleared fall detection medical device.

## Factors, Metrics & Evaluation Data
- **Target Metrics:** accuracy, precision, recall, f1_score, confusion_matrix
- **Dataset:** `inertial_sensor_readings_sample` with stratified splits and cross-validation.

## Ethical Considerations & Responsible AI
Fitness and research tracking only; not approved as an FDA-cleared fall detection medical device.

## Caveats and Recommendations
Device placement variation (pocket vs wrist) alters signal harmonics and reduces accuracy.
