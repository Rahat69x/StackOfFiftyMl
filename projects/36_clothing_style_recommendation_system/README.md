# Clothing Style Recommendation System (ML036)
**Category:** Recommendation | **ML Type:** Recommendation | **Platform:** MLFORGE

## 1. Overview
Personalized wardrobe recommendation platform matching clothing cuts, color palettes, occasions, and personal preferences.

## 2. Problem Type & Paradigm
- **Task:** Recommendation
- **Domain:** Recommendation
- **Baseline Architecture:** Visual & Metadata Embedding Cosine Recommender

## 3. Dataset & License
- **Dataset Identifer:** `fashion_catalog_sample`
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
precision_at_k, ndcg, style_coherence

## 6. Known Limitations
Style trends evolve seasonally faster than static catalog retraining cycles.

## 7. Responsible-Use Notes
Promotes body-positive and culturally inclusive styling recommendations.
