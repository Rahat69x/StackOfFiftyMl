"""
MLFORGE Core — Model Registry
Manages model versions, artifact serialization, metadata indexing,
lineage links, comparison, and lifecycle status (active, candidate, archived, deprecated).
"""

import os
import json
import time
import shutil
from typing import Any, Dict, List, Optional
import logging

logger = logging.getLogger("mlforge.core.model_registry")


class ModelRegistry:
    """
    Central repository for trained model artifacts and versions across all 50 projects.
    """

    def __init__(self, registry_dir: Optional[str] = None):
        if registry_dir is None:
            self.registry_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "models"))
        else:
            self.registry_dir = registry_dir
            
        os.makedirs(self.registry_dir, exist_ok=True)
        self.metadata_file = os.path.join(self.registry_dir, "registry_meta.json")
        self.records: Dict[str, List[Dict[str, Any]]] = self._load_records()

    def _load_records(self) -> Dict[str, List[Dict[str, Any]]]:
        if os.path.exists(self.metadata_file):
            try:
                with open(self.metadata_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                logger.error(f"Error loading model registry metadata: {e}")
        return {}

    def _save_records(self) -> None:
        with open(self.metadata_file, "w", encoding="utf-8") as f:
            json.dump(self.records, f, indent=2)

    def register_model(
        self,
        project_id: str,
        version: str,
        artifact_path: str,
        metrics: Dict[str, Any],
        parameters: Optional[Dict[str, Any]] = None,
        status: str = "active",
        lineage: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Registers a newly trained model version."""
        if project_id not in self.records:
            self.records[project_id] = []
            
        # If new model is active, archive previous active
        if status == "active":
            for m in self.records[project_id]:
                if m.get("status") == "active":
                    m["status"] = "archived"

        record = {
            "model_id": f"{project_id}_{version}_{int(time.time())}",
            "project_id": project_id,
            "version": version,
            "artifact_path": artifact_path,
            "metrics": metrics,
            "parameters": parameters or {},
            "status": status,
            "registered_at": time.time(),
            "registered_at_iso": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "lineage": lineage or {}
        }
        self.records[project_id].append(record)
        self._save_records()
        logger.info(f"Registered model {record['model_id']} for project {project_id}")
        return record

    def get_models_for_project(self, project_id: str) -> List[Dict[str, Any]]:
        """Returns all registered model versions for a given project."""
        return self.records.get(project_id, [])

    def get_active_model(self, project_id: str) -> Optional[Dict[str, Any]]:
        """Finds the currently active production model for a project."""
        models = self.records.get(project_id, [])
        for m in reversed(models):
            if m.get("status") == "active":
                return m
        return models[-1] if models else None

    def compare_models(self, project_id: str) -> Dict[str, Any]:
        """Compares metric variations across registered model versions for a project."""
        models = self.records.get(project_id, [])
        comparison = []
        for m in models:
            comparison.append({
                "model_id": m["model_id"],
                "version": m["version"],
                "status": m["status"],
                "registered_at": m.get("registered_at_iso"),
                "metrics": m.get("metrics", {})
            })
        return {
            "project_id": project_id,
            "versions_count": len(models),
            "versions": comparison
        }

    def rollback(self, project_id: str, target_version: str) -> Optional[Dict[str, Any]]:
        """Rolls back the active model to a previous version."""
        models = self.records.get(project_id, [])
        target_model = None
        for m in models:
            if m["version"] == target_version:
                target_model = m
                break
                
        if not target_model:
            return None
            
        for m in models:
            if m["version"] == target_version:
                m["status"] = "active"
            elif m["status"] == "active":
                m["status"] = "archived"
                
        self._save_records()
        logger.info(f"Project {project_id} rolled back to version {target_version}")
        return target_model

    def list_all_models(self) -> List[Dict[str, Any]]:
        """Flattens all models across all 50 projects."""
        all_models = []
        for p_id, m_list in self.records.items():
            all_models.extend(m_list)
        return all_models


# Global singleton instance
model_registry = ModelRegistry()
