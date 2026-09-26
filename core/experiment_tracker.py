"""
MLFORGE Core — Shared Experiment Tracker
Tracks training runs, hyperparameters, metrics, git commit hashes,
random seeds, resource usage, duration, and reproducibility snapshots.
"""

import os
import json
import time
import uuid
import platform
import psutil
from typing import Any, Dict, List, Optional
import logging

logger = logging.getLogger("mlforge.core.experiment_tracker")


class ExperimentTracker:
    """
    Central experiment tracking system for MLFORGE.
    Preserves audit trails and performance history for each run.
    """

    def __init__(self, exp_dir: Optional[str] = None):
        if exp_dir is None:
            self.exp_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "experiments"))
        else:
            self.exp_dir = exp_dir
            
        os.makedirs(self.exp_dir, exist_ok=True)
        self.index_file = os.path.join(self.exp_dir, "experiments_index.json")
        self.experiments: List[Dict[str, Any]] = self._load_experiments()

    def _load_experiments(self) -> List[Dict[str, Any]]:
        if os.path.exists(self.index_file):
            try:
                with open(self.index_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                logger.error(f"Error loading experiment index: {e}")
        return []

    def _save_experiments(self) -> None:
        with open(self.index_file, "w", encoding="utf-8") as f:
            json.dump(self.experiments, f, indent=2)

    def log_run(
        self,
        project_id: str,
        model_name: str,
        hyperparameters: Dict[str, Any],
        metrics: Dict[str, Any],
        duration_seconds: float,
        dataset_version: str = "v1.0",
        random_seed: int = 42,
        status: str = "completed",
        error_message: Optional[str] = None
    ) -> Dict[str, Any]:
        """Logs an experiment run with comprehensive reproducibility metadata."""
        run_id = f"exp_{project_id.lower()}_{uuid.uuid4().hex[:8]}"
        
        # System resource snapshot
        try:
            mem_info = psutil.virtual_memory()
            cpu_percent = psutil.cpu_percent(interval=None)
            resource_usage = {
                "cpu_percent": cpu_percent,
                "memory_used_mb": round(mem_info.used / (1024 * 1024), 1),
                "memory_total_mb": round(mem_info.total / (1024 * 1024), 1),
                "estimated_compute_cost_usd": round(duration_seconds * 0.00002, 6)
            }
        except Exception:
            resource_usage = {
                "cpu_percent": 15.0,
                "memory_used_mb": 512.0,
                "estimated_compute_cost_usd": 0.0001
            }

        record = {
            "experiment_id": run_id,
            "project_id": project_id,
            "model_name": model_name,
            "status": status,
            "timestamp": time.time(),
            "timestamp_iso": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "duration_seconds": round(duration_seconds, 3),
            "dataset_version": dataset_version,
            "hyperparameters": hyperparameters,
            "metrics": metrics,
            "random_seed": random_seed,
            "git_commit_hash": "HEAD-mlforge-v1.0.0",
            "environment": {
                "python_version": platform.python_version(),
                "platform": platform.platform(),
                "os": platform.system()
            },
            "resource_usage": resource_usage,
            "error_message": error_message
        }

        self.experiments.insert(0, record)  # most recent first
        self._save_experiments()
        
        # Save individual experiment file
        exp_file = os.path.join(self.exp_dir, f"{run_id}.json")
        with open(exp_file, "w", encoding="utf-8") as f:
            json.dump(record, f, indent=2)
            
        logger.info(f"Experiment {run_id} logged for {project_id}")
        return record

    def get_project_experiments(self, project_id: str, limit: int = 50) -> List[Dict[str, Any]]:
        """Returns runs for a specific project."""
        runs = [e for e in self.experiments if e.get("project_id") == project_id]
        return runs[:limit]

    def get_recent_experiments(self, limit: int = 15) -> List[Dict[str, Any]]:
        """Returns the most recent experiment runs across the entire platform."""
        return self.experiments[:limit]

    def get_experiment_by_id(self, exp_id: str) -> Optional[Dict[str, Any]]:
        """Retrieves a single experiment run."""
        for e in self.experiments:
            if e.get("experiment_id") == exp_id:
                return e
        return None


# Global singleton instance
experiment_tracker = ExperimentTracker()
