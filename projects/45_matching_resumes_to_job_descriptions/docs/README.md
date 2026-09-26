# Matching Resumes To Job Descriptions (ML045)
**Category:** NLP | **ML Type:** NLP | **Platform:** MLFORGE

## 1. Overview
Talent matching NLP module parsing candidate resumes, matching semantic skill requirements against job postings with explainable rationale.

## 2. Problem Type & Paradigm
- **Task:** NLP
- **Domain:** NLP
- **Baseline Architecture:** Bi-Encoder Semantic Similarity Matcher + Skill Overlap Highlighter

## 3. Dataset & License
- **Dataset Identifer:** `resumes_jobs_sample`
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
top_5_match_precision, cosine_similarity_avg, explainable_feature_weights

## 6. Known Limitations
Keyword stuffing and unconventional career journeys can distort match scores.

## 7. Responsible-Use Notes
STRICT LABOR FAIRNESS: Must not make final hiring or screening elimination decisions; provides non-binding assistance to human recruiters.
