# Smart Home Energy Optimization (ML041)
**Category:** Forecasting / Optimization | **ML Type:** Regression | **Platform:** MLFORGE

## 1. Overview
IoT home energy management simulator scheduling deferrable loads (EV chargers, laundry, HVAC) during off-peak tariff periods.

## 2. Problem Type & Paradigm
- **Task:** Regression
- **Domain:** Forecasting / Optimization
- **Baseline Architecture:** Appliance Energy Regressor + Linear Peak-Shifting Optimizer

## 3. Dataset & License
- **Dataset Identifer:** `smart_home_appliances_sample`
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
mae, rmse, peak_shaving_percentage, cost_savings_estimated

## 6. Known Limitations
Resident override behavior and comfort constraints may limit theoretical cost savings.

## 7. Responsible-Use Notes
Enables home automation energy savings and carbon abatement.
