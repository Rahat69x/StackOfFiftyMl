"""
Unit tests for MLFORGE Core Engines.
"""

import pytest
import numpy as np
import pandas as pd
from core.dataset_manager import dataset_manager
from core.training_engine import training_engine
from core.evaluation_engine import evaluation_engine
from core.model_registry import model_registry
from core.experiment_tracker import experiment_tracker
from core.notification_engine import notification_engine
from core.security_policy import security_policy
from core.project_registry import registry


def test_registry_contains_all_50_projects():
    projects = registry.get_all_projects()
    assert len(projects) == 50
    ids = [p["id"] for p in projects]
    for i in range(1, 51):
        expected_id = f"ML{i:03d}"
        assert expected_id in ids, f"Missing project {expected_id}"


def test_dataset_manager_generators_and_split():
    X, y = dataset_manager.generate_tabular_classification(n_samples=50, n_features=4, n_classes=2)
    assert len(X) == 50
    assert len(y) == 50
    splits = dataset_manager.split_data(X, y, test_size=0.2)
    assert len(splits["X_train"]) == 40
    assert len(splits["X_test"]) == 10


def test_training_and_evaluation_engine():
    X = np.random.randn(60, 4)
    y = np.random.choice([0, 1], size=60)
    model, metrics = training_engine.train_classifier(X, y)
    assert "accuracy" in metrics
    assert "precision" in metrics
    assert "recall" in metrics
    assert "confusion_matrix" in metrics


def test_model_registry_and_rollback():
    rec = model_registry.register_model(
        project_id="ML001",
        version="1.0.0",
        artifact_path="/tmp/model.joblib",
        metrics={"accuracy": 0.85},
        status="active"
    )
    assert rec["version"] == "1.0.0"
    active = model_registry.get_active_model("ML001")
    assert active is not None


def test_experiment_tracker():
    rec = experiment_tracker.log_run(
        project_id="ML001",
        model_name="RandomForest",
        hyperparameters={"n_estimators": 10},
        metrics={"accuracy": 0.88},
        duration_seconds=0.5
    )
    assert rec["status"] == "completed"
    assert "resource_usage" in rec


def test_notification_engine():
    notif = notification_engine.emit(
        title="Test Notification",
        message="Smoke test notification",
        notif_type="info"
    )
    assert notif["read"] is False
    notification_engine.mark_as_read(notif["id"])
    assert notif["read"] is True


def test_security_policy_jwt_and_rbac():
    token = security_policy.create_access_token("admin_user", role="admin")
    decoded = security_policy.decode_token(token)
    assert decoded["sub"] == "admin_user"
    assert decoded["role"] == "admin"
    assert security_policy.check_permission("admin", "can_train") is True
    assert security_policy.check_permission("viewer", "can_train") is False
