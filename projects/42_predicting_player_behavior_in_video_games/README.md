# Predicting Player Behavior In Video Games (ML042)
**Category:** Clustering / Classification | **ML Type:** Classification | **Platform:** MLFORGE

## 1. Overview
Player analytics framework clustering player archetypes (achiever, explorer, socializer) and predicting in-game engagement drop-offs.

## 2. Problem Type & Paradigm
- **Task:** Classification
- **Domain:** Clustering / Classification
- **Baseline Architecture:** K-Means Archetype Clustering + Churn/Purchase Classifier

## 3. Dataset & License
- **Dataset Identifer:** `gameplay_sessions_sample`
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
silhouette_score, accuracy, precision, recall, f1_score

## 6. Known Limitations
Aggressive monetizing optimizations risk harming long-term player sentiment.

## 7. Responsible-Use Notes
Maintain fair play and ethical game design; do not design manipulative dark-pattern loops.
