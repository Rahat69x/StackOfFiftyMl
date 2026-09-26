"""
MLFORGE Core — Shared Prediction Engine & Drift Detector
Executes real-time and batch inferences, tracks prediction latency,
and computes statistical distribution drift between inference inputs and training baselines.
"""

import time
import numpy as np
import pandas as pd
from typing import Any, Dict, List, Optional, Union
import logging

logger = logging.getLogger("mlforge.core.prediction_engine")


class PredictionEngine:
    """
    Standardized inference runner ensuring consistent response envelopes,
    latency tracking, and drift analysis.
    """

    def __init__(self):
        self.prediction_history: List[Dict[str, Any]] = []

    def run_prediction(
        self,
        project_instance: Any,
        inputs: Any,
        request_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Runs inference via project instance and captures latency."""
        start_time = time.time()
        
        # Check if project is trained or has model loaded
        if not getattr(project_instance, "is_trained", False):
            # Attempt to load model or train quick baseline
            loaded = project_instance.load_model()
            if not loaded:
                logger.info(f"Project {project_instance.project_id} model not loaded, running quick initialization...")
                project_instance.train()

        result = project_instance.predict(inputs)
        latency_ms = round((time.time() - start_time) * 1000, 2)
        
        # Explanation if requested
        explanation = project_instance.explain(inputs) if hasattr(project_instance, "explain") else None

        envelope = {
            "project_id": project_instance.project_id,
            "request_id": request_id or f"pred_{int(time.time()*1000)}",
            "prediction": result.get("prediction") if isinstance(result, dict) else result,
            "probabilities": result.get("probabilities") if isinstance(result, dict) else None,
            "explanation": explanation,
            "latency_ms": latency_ms,
            "timestamp": time.time(),
            "model_version": getattr(project_instance, "version", "1.0.0")
        }
        
        self.prediction_history.insert(0, envelope)
        if len(self.prediction_history) > 100:
            self.prediction_history.pop()
            
        return envelope

    def compute_drift(
        self,
        reference_data: np.ndarray,
        current_data: np.ndarray,
        threshold: float = 0.25
    ) -> Dict[str, Any]:
        """
        Computes Kolmogorov-Smirnov / Wasserstein proxy drift between reference baseline and incoming data.
        """
        ref = np.array(reference_data).ravel()
        curr = np.array(current_data).ravel()
        
        ref_mean, ref_std = float(np.mean(ref)), float(np.std(ref) + 1e-6)
        curr_mean, curr_std = float(np.mean(curr)), float(np.std(curr) + 1e-6)
        
        # Normalized mean shift
        mean_shift = abs(curr_mean - ref_mean) / ref_std
        std_ratio = curr_std / ref_std
        drift_score = round(float(0.7 * mean_shift + 0.3 * abs(std_ratio - 1.0)), 4)
        has_drift = drift_score > threshold

        return {
            "drift_score": drift_score,
            "threshold": threshold,
            "drift_detected": bool(has_drift),
            "reference_mean": round(ref_mean, 3),
            "current_mean": round(curr_mean, 3),
            "reference_std": round(ref_std, 3),
            "current_std": round(curr_std, 3),
            "status": "warning" if has_drift else "healthy"
        }

    def get_recent_predictions(self, limit: int = 20) -> List[Dict[str, Any]]:
        """Returns recent inference logs."""
        return self.prediction_history[:limit]


# Global singleton instance
prediction_engine = PredictionEngine()
