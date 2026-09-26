# Predicting Disease Outbreaks (ML004)
**Category:** Time Series / Healthcare Research | **ML Type:** Time Series | **Platform:** MLFORGE

## 1. Overview
Time-series predictive analytics research system for epidemiological trend forecasting with confidence intervals and uncertainty quantification.

## 2. Problem Type & Paradigm
- **Task:** Time Series
- **Domain:** Time Series / Healthcare Research
- **Baseline Architecture:** ARIMA / Ridge Autoregressor with Uncertainty Bounds

## 3. Dataset & License
- **Dataset Identifer:** `disease_surveillance_sample`
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
mae, rmse, mape, prediction_intervals

## 6. Known Limitations
Outbreak dynamics are sensitive to unreported cases, policy interventions, and sudden genomic mutations.

## 7. Responsible-Use Notes
RESEARCH ONLY: Strictly for research and decision-support simulation. NEVER present predictions as a medical authority or clinical mandate.
