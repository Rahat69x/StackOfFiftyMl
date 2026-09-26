"""
Model architecture definition for Traffic Prediction / Traffic Flow Prediction (ML023).
"""
from sklearn.ensemble import RandomForestRegressor

def build_model(hyperparameters=None):
    params = hyperparameters or {}
    return RandomForestRegressor(
        n_estimators=params.get("n_estimators", 30),
        max_depth=params.get("max_depth", 6),
        random_state=42
    )
