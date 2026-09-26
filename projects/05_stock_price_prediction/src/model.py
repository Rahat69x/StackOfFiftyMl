"""
Model architecture definition for Stock Price Prediction (ML005).
"""
from sklearn.ensemble import RandomForestRegressor

def build_model(hyperparameters=None):
    params = hyperparameters or {}
    return RandomForestRegressor(
        n_estimators=params.get("n_estimators", 30),
        max_depth=params.get("max_depth", 6),
        random_state=42
    )
