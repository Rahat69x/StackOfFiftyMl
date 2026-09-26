# Customer Review Topic Classification (ML024)
**Category:** NLP | **ML Type:** Classification | **Platform:** MLFORGE

## 1. Overview
Automated text topic categorization sorting incoming customer feedback into Product Quality, Shipping, Pricing, Customer Service, and Usability.

## 2. Problem Type & Paradigm
- **Task:** Classification
- **Domain:** NLP
- **Baseline Architecture:** TF-IDF + Multinomial Naive Bayes / SGD Topic Classifier

## 3. Dataset & License
- **Dataset Identifer:** `feedback_topics_sample`
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
Multi-topic reviews with conflicting sub-themes may be assigned only to the primary dominant keyword class.

## 7. Responsible-Use Notes
Enables triage of operational pain points across cross-functional product departments.
