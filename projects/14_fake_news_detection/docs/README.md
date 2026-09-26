# Fake News Detection (ML014)
**Category:** NLP | **ML Type:** Classification | **Platform:** MLFORGE

## 1. Overview
Text classification research system analyzing journalistic stylometry, sensationalist lexicon, and source credibility markers.

## 2. Problem Type & Paradigm
- **Task:** Classification
- **Domain:** NLP
- **Baseline Architecture:** TF-IDF + PassiveAggressiveClassifier / Explainable Logistic Regression

## 3. Dataset & License
- **Dataset Identifer:** `news_articles_sample`
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
accuracy, precision, recall, f1_score, roc_auc

## 6. Known Limitations
Subject to bias toward mainstream publication styles; can flag satire or unorthodox legitimate investigative reporting as anomalous.

## 7. Responsible-Use Notes
Probabilistic research tool only. Output must never be used as automated censorship or definitive truth arbitration.
