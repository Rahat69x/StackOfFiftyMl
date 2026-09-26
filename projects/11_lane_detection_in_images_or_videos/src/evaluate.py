"""
Evaluation module for Lane Detection In Images Or Videos (ML011).
"""
from core.evaluation_engine import evaluation_engine

def evaluate_model_performance(model, preprocessor, df_test):
    X, y = preprocessor.fit_transform(df_test)
    preds = model.predict(X)
    if hasattr(model, "predict_proba"):
        return evaluation_engine.evaluate_classification(y, preds)
    return evaluation_engine.evaluate_regression(y, preds)
