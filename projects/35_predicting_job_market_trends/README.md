# Predicting Job Market Trends (ML035)
**Category:** Forecasting / NLP | **ML Type:** Time Series | **Platform:** MLFORGE

## 1. Overview
Labor market analytics and forecasting engine tracking emergent technology skills, hiring demand, and regional salary trajectories.

## 2. Problem Type & Paradigm
- **Task:** Time Series
- **Domain:** Forecasting / NLP
- **Baseline Architecture:** Skill Frequency Extractor + Trend Forecaster

## 3. Dataset & License
- **Dataset Identifer:** `job_postings_sample`
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
mae, rmse, growth_rate_error

## 6. Known Limitations
Posting volume fluctuations can be skewed by duplicate aggregator postings and phantom job listings.

## 7. Responsible-Use Notes
Provides macro labor intelligence; must not be used to make discriminatory individual employment or compensation decisions.
