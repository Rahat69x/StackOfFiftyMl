# Traffic Prediction / Traffic Flow Prediction (ML023)
**Category:** Time Series / Forecasting | **ML Type:** Regression | **Platform:** MLFORGE

## 1. Overview
Urban traffic density and vehicle speed forecasting engine leveraging spatial road graph nodes and temporal rush-hour cycles.

## 2. Problem Type & Paradigm
- **Task:** Regression
- **Domain:** Time Series / Forecasting
- **Baseline Architecture:** Spatio-Temporal Lagged Regressor

## 3. Dataset & License
- **Dataset Identifer:** `road_sensors_traffic_sample`
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
mae, rmse, r2_score

## 6. Known Limitations
Immediate impacts of sudden unrecorded traffic accidents or construction detours require real-time telemetry updates.

## 7. Responsible-Use Notes
Supports civil municipal traffic light timing and commuter navigation optimization.
