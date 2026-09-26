"""
Model architecture definition for Facial Recognition Attendance System (ML028).
"""
from sklearn.ensemble import RandomForestClassifier

def build_model(hyperparameters=None):
    params = hyperparameters or {}
    return RandomForestClassifier(
        n_estimators=params.get("n_estimators", 30),
        max_depth=params.get("max_depth", 6),
        random_state=42
    )
