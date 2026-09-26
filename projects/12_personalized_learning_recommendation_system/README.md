# Personalized Learning Recommendation System (ML012)
**Category:** Recommendation | **ML Type:** Recommendation | **Platform:** MLFORGE

## 1. Overview
Educational recommendation platform providing adaptive study topics, difficulty levels, and personalized remedial materials.

## 2. Problem Type & Paradigm
- **Task:** Recommendation
- **Domain:** Recommendation
- **Baseline Architecture:** Knowledge Tracing + Content Recommender

## 3. Dataset & License
- **Dataset Identifer:** `student_curriculum_sample`
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
precision_at_k, ndcg, curriculum_coverage

## 6. Known Limitations
Cannot assess neurodivergent learning modalities or external socioeconomic stressors affecting test completion.

## 7. Responsible-Use Notes
Avoid making unsupported judgments about a student's innate ability or educational worth.
