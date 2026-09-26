"""
Training module for Game-Playing Model Training (ML009).
"""
import time
import os
import sys

_p_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if _p_dir not in sys.path:
    sys.path.insert(0, _p_dir)

from src.preprocessing import Preprocessor
from src.model import build_model
from core.evaluation_engine import evaluation_engine

def run_training(df, hyperparameters=None):
    start = time.time()
    preprocessor = Preprocessor()
    X, y = preprocessor.fit_transform(df)
    
    split_idx = int(len(X) * 0.8)
    X_train, X_test = X[:split_idx], X[split_idx:]
    y_train, y_test = y[:split_idx], y[split_idx:]
    
    model = build_model(hyperparameters)
    model.fit(X_train, y_train)
    duration = time.time() - start
    
    preds = model.predict(X_test)
    if hasattr(model, "predict_proba"):
        metrics = evaluation_engine.evaluate_classification(y_test, preds)
    else:
        metrics = evaluation_engine.evaluate_regression(y_test, preds)
        
    metrics["training_duration_seconds"] = round(duration, 3)
    return model, preprocessor, metrics
