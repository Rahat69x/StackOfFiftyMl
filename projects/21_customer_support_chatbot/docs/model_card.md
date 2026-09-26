# Model Card: Customer Support Chatbot (ML021)

## Model Details
- **Developer:** MLFORGE Team
- **Model Date:** September 2026
- **Model Version:** 1.0.0
- **Model Type:** Cosine Intent Embedder + Fallback Rule Engine
- **License:** MIT Research License

## Intended Use
- **Primary Intended Uses:** Research, benchmarking, educational exploration, and decision-support simulation.
- **Out of Scope Uses:** Must disclose to customers that they are conversing with an automated bot and provide an immediate human agent escalation button.

## Factors, Metrics & Evaluation Data
- **Target Metrics:** intent_accuracy, fallback_rate, average_confidence
- **Dataset:** `support_dialogues_sample` with stratified splits and cross-validation.

## Ethical Considerations & Responsible AI
Must disclose to customers that they are conversing with an automated bot and provide an immediate human agent escalation button.

## Caveats and Recommendations
Cannot understand complex multistep troubleshooting or handle angry customers effectively without human intervention.
