# Movie Or Book Recommendation System (ML003)
**Category:** Recommendation | **ML Type:** Recommendation | **Platform:** MLFORGE

## 1. Overview
Recommendation engine supporting content-based filtering, collaborative filtering, similarity matrices, and Top-N recommendation ranking.

## 2. Problem Type & Paradigm
- **Task:** Recommendation
- **Domain:** Recommendation
- **Baseline Architecture:** Hybrid Content-Based + Collaborative Filtering (Cosine / SVD)

## 3. Dataset & License
- **Dataset Identifer:** `media_ratings_sample`
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
precision_at_k, recall_at_k, ndcg, map

## 6. Known Limitations
Subject to cold-start challenges for newly released items and users with zero historical interactions.

## 7. Responsible-Use Notes
Mitigate filter-bubble bias and maintain diversity in recommendations.
