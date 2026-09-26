"""
MLFORGE Core — Project Registry
Central registry managing all 50 ML projects, their metadata, categories, filters,
and dynamic lifecycle instantiation.
"""

import json
import os
import sys
import importlib
from typing import Any, Dict, List, Optional
import logging

logger = logging.getLogger("mlforge.core.project_registry")


class ProjectRegistry:
    """
    Central repository registry for MLFORGE.
    Loads and indexes project definitions from platform.config.json.
    """

    def __init__(self, platform_config_path: Optional[str] = None):
        if platform_config_path is None:
            root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
            platform_config_path = os.path.join(root_dir, "platform.config.json")
        
        self.config_path = platform_config_path
        self.root_dir = os.path.dirname(self.config_path)
        self.data: Dict[str, Any] = {}
        self.projects_by_id: Dict[str, Dict[str, Any]] = {}
        self.projects_by_slug: Dict[str, Dict[str, Any]] = {}
        self._instances: Dict[str, Any] = {}
        self.reload()

    def reload(self) -> None:
        """Reloads the platform configuration."""
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Platform config not found at: {self.config_path}")
        
        with open(self.config_path, "r", encoding="utf-8") as f:
            self.data = json.load(f)
        
        self.projects_by_id.clear()
        self.projects_by_slug.clear()
        
        for p in self.data.get("projects", []):
            self.projects_by_id[p["id"]] = p
            self.projects_by_slug[p["slug"]] = p
        
        logger.info(f"Loaded {len(self.projects_by_id)} projects into registry.")

    def get_all_projects(self) -> List[Dict[str, Any]]:
        """Returns all 50 projects."""
        return self.data.get("projects", [])

    def get_project(self, project_identifier: str) -> Optional[Dict[str, Any]]:
        """Finds project by ID (e.g. ML001) or slug (01_fruits_...)."""
        if project_identifier in self.projects_by_id:
            return self.projects_by_id[project_identifier]
        if project_identifier in self.projects_by_slug:
            return self.projects_by_slug[project_identifier]
        # Search by number prefix or name
        for p in self.data.get("projects", []):
            if p["id"].lower() == project_identifier.lower() or p["slug"].lower() == project_identifier.lower():
                return p
            if p["name"].lower() == project_identifier.lower():
                return p
        return None

    def search_and_filter(
        self,
        query: Optional[str] = None,
        category: Optional[str] = None,
        ml_type: Optional[str] = None,
        complexity: Optional[str] = None,
        responsible_flag: Optional[str] = None,
        status: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Filters projects matching all supplied criteria.
        """
        results = self.data.get("projects", [])
        
        if query:
            q = query.lower()
            results = [
                p for p in results
                if q in p["name"].lower()
                or q in p["description"].lower()
                or any(q in tag.lower() for tag in p.get("tags", []))
                or q in p["id"].lower()
            ]
        
        if category and category != "All":
            results = [p for p in results if p.get("category") == category]
            
        if ml_type and ml_type != "All":
            results = [p for p in results if p.get("type") == ml_type]
            
        if complexity and complexity != "All":
            results = [p for p in results if p.get("complexity_level") == complexity]
            
        if responsible_flag:
            results = [p for p in results if responsible_flag in p.get("responsible_use_flags", [])]
            
        if status and status != "All":
            results = [p for p in results if p.get("status") == status]
            
        return results

    def get_categories(self) -> List[str]:
        """Returns sorted distinct category list."""
        return sorted(list(set(p["category"] for p in self.data.get("projects", []))))

    def get_ml_types(self) -> List[str]:
        """Returns sorted distinct ML types."""
        return sorted(list(set(p["type"] for p in self.data.get("projects", []))))

    def get_stats(self) -> Dict[str, Any]:
        """Computes summary statistics across all registered projects."""
        projects = self.data.get("projects", [])
        total = len(projects)
        category_counts: Dict[str, int] = {}
        type_counts: Dict[str, int] = {}
        flagged_count = 0
        
        for p in projects:
            cat = p.get("category", "Other")
            category_counts[cat] = category_counts.get(cat, 0) + 1
            t = p.get("type", "Other")
            type_counts[t] = type_counts.get(t, 0) + 1
            if p.get("responsible_use_flags"):
                flagged_count += 1
                
        return {
            "total_projects": total,
            "category_distribution": category_counts,
            "type_distribution": type_counts,
            "responsible_use_flagged_count": flagged_count,
            "demo_ready_count": sum(1 for p in projects if p.get("demo_mode_available")),
            "status_distribution": {
                "ready": sum(1 for p in projects if p.get("status") == "ready"),
                "dataset_required": sum(1 for p in projects if p.get("status") == "dataset_required")
            }
        }

    def get_project_instance(self, project_identifier: str):
        """
        Dynamically imports and instantiates the project's MLProject class.
        """
        meta = self.get_project(project_identifier)
        if not meta:
            raise ValueError(f"Project '{project_identifier}' not found in registry.")
        
        project_id = meta["id"]
        if project_id in self._instances:
            return self._instances[project_id]
        
        slug = meta["slug"]
        project_dir = os.path.join(self.root_dir, "projects", slug)
        
        # Ensure project dir is in sys.path
        if project_dir not in sys.path:
            sys.path.insert(0, project_dir)
            
        main_file = os.path.join(project_dir, "main.py")
        if os.path.exists(main_file):
            spec = importlib.util.spec_from_file_location(f"project_{slug}", main_file)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            instance = mod.get_project_instance(project_dir)
            self._instances[project_id] = instance
            return instance
        else:
            raise FileNotFoundError(f"main.py not found in {project_dir}")


# Global singleton instance
registry = ProjectRegistry()
