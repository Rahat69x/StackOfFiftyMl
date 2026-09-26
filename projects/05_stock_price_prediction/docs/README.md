# Stock Price Prediction (ML005)
**Category:** Time Series / Finance | **ML Type:** Time Series | **Platform:** MLFORGE

## 1. Overview
Financial time-series forecasting research module featuring technical indicator extraction, lagging windows, and historical backtesting.

## 2. Problem Type & Paradigm
- **Task:** Time Series
- **Domain:** Time Series / Finance
- **Baseline Architecture:** Gradient Boosting Regressor / LSTM Baseline with Backtesting

## 3. Dataset & License
- **Dataset Identifer:** `market_prices_sample`
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
mae, rmse, directional_accuracy, sharpe_ratio_simulation

## 6. Known Limitations
Financial markets follow stochastic non-stationary walks heavily influenced by macroeconomic shocks.

## 7. Responsible-Use Notes
FINANCIAL DISCLAIMER: Research and educational experimentation only. Absolutely not financial or investment advice.
