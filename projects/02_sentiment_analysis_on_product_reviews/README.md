# Sentiment Analysis On Product Reviews (ML002)
**Category:** NLP | **ML Type:** Classification | **Platform:** MLFORGE

## 1. Overview
NLP sentiment analysis system for customer reviews providing positive, negative, and neutral polarity detection.

## 2. Problem Type & Paradigm
- **Task:** Classification
- **Domain:** NLP
- **Baseline Architecture:** TF-IDF + LogisticRegression / Transformer Baseline

## 3. Dataset & License
- **Dataset Identifer:** `product_reviews_sample`
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
accuracy, precision, recall, f1_score, confusion_matrix

## 6. Known Limitations
Sarcasm, colloquialisms, and multilingual text may reduce classification accuracy.

## 7. Responsible-Use Notes
Do not use solely to suppress negative customer feedback or penalize support staff.
