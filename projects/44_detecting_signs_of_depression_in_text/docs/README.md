# Detecting Signs Of Depression In Text (ML044)
**Category:** NLP / Healthcare Research | **ML Type:** Classification | **Platform:** MLFORGE

## 1. Overview
Affective computing research module analyzing linguistic indicators, self-referential pronoun density, and depressive sentiment markers.

## 2. Problem Type & Paradigm
- **Task:** Classification
- **Domain:** NLP / Healthcare Research
- **Baseline Architecture:** Psycholinguistic Lexicon + Regularized Logistic Classifier

## 3. Dataset & License
- **Dataset Identifer:** `affective_text_sample`
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
sensitivity, specificity, precision, recall, f1_score, roc_auc

## 6. Known Limitations
Humor, coping mechanisms, and contextual nuance cannot be adequately judged by automated NLP parsers.

## 7. Responsible-Use Notes
CRITICAL HEALTHCARE WARNING: THIS IS NOT A DIAGNOSTIC TOOL. Under no circumstances infer or label a real individual's clinical mental health from their writings.
