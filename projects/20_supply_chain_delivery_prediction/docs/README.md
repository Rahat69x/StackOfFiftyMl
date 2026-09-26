# Supply Chain Delivery Prediction (ML020)
**Category:** Regression / Forecasting | **ML Type:** Regression | **Platform:** MLFORGE

## 1. Overview
Logistics delivery time predictor modeling shipping origin-destination distances, carrier reliability, weather, and seasonal peaks.

## 2. Problem Type & Paradigm
- **Task:** Regression
- **Domain:** Regression / Forecasting
- **Baseline Architecture:** Gradient Boosted Delivery Regressor

## 3. Dataset & License
- **Dataset Identifer:** `logistics_shipments_sample`
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
mae, rmse, r2_score, on_time_classification_accuracy

## 6. Known Limitations
Border customs delays, geopolitical blockades, and wild weather events present high outlier deviations.

## 7. Responsible-Use Notes
Designed for dispatch planning and transparent customer delivery windows.
