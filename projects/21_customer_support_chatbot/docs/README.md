# Customer Support Chatbot (ML021)
**Category:** NLP | **ML Type:** NLP | **Platform:** MLFORGE

## 1. Overview
Conversational customer service agent providing FAQ retrieval, context tracking, confidence thresholds, and human handoff routing.

## 2. Problem Type & Paradigm
- **Task:** NLP
- **Domain:** NLP
- **Baseline Architecture:** Cosine Intent Embedder + Fallback Rule Engine

## 3. Dataset & License
- **Dataset Identifer:** `support_dialogues_sample`
- **Sample Benchmark:** Ships with lightweight synthetic verification benchmark in `data/sample/sample_data.csv`.
- **License:** MIT / Permissive Research Use.

## 4. How to Run
```bash
# Execute standalone training smoke run
python -c "from main import get_project_instance; p = get_project_instance('.'); p.train(); print('Metrics:', p.last_metrics)"

# Run test suite
pytest tests/
```

## 5. Metrics Produced
intent_accuracy, fallback_rate, average_confidence

## 6. Known Limitations
Cannot understand complex multistep troubleshooting or handle angry customers effectively without human intervention.

## 7. Responsible-Use Notes
Must disclose to customers that they are conversing with an automated bot and provide an immediate human agent escalation button.
