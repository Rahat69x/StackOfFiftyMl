# Model Card: Anomaly Detection In IoT Sensor Data (ML049)

## Model Details
- **Developer:** MLFORGE Team
- **Model Date:** September 2026
- **Model Version:** 1.0.0
- **Model Type:** Dynamic Threshold Isolation Forest + Exponential Moving Z-Score
- **License:** MIT Research License

## Intended Use
- **Primary Intended Uses:** Research, benchmarking, educational exploration, and decision-support simulation.
- **Out of Scope Uses:** Facilitates real-time industrial monitoring and equipment safety protection.

## Factors, Metrics & Evaluation Data
- **Target Metrics:** precision, recall, f1_score, roc_auc, alert_frequency
- **Dataset:** `iot_telemetry_stream_sample` with stratified splits and cross-validation.

## Ethical Considerations & Responsible AI
Facilitates real-time industrial monitoring and equipment safety protection.

## Caveats and Recommendations
Seasonal thermal cycles can trigger false positive alerts if static thresholds are used instead of dynamic baselines.
