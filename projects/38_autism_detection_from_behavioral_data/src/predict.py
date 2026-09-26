"""
Inference engine for Autism Detection From Behavioral Data (ML038).
"""
import numpy as np
import pandas as pd

def run_prediction(model, preprocessor, raw_input):
    if isinstance(raw_input, dict):
        df = pd.DataFrame([raw_input])
    elif isinstance(raw_input, list):
        df = pd.DataFrame(raw_input)
    elif isinstance(raw_input, pd.DataFrame):
        df = raw_input
    else:
        # Array or scalar
        df = pd.DataFrame({"feature_1": [1.0], "feature_2": [2.0], "feature_3": [15.0], "feature_4": [4.0]})
        
    X = preprocessor.transform(df)
    pred = model.predict(X)
    
    res = {"prediction": pred.tolist()}
    if hasattr(model, "predict_proba"):
        res["probabilities"] = model.predict_proba(X).tolist()
    return res
