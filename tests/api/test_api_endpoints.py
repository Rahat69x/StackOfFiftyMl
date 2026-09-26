"""
API integration and contract tests using FastAPI TestClient.
"""

import pytest
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)


def test_health_endpoint():
    res = client.get("/api/health")
    assert res.status_code == 200
    json_data = res.json()
    assert json_data["status"] == "healthy"
    assert json_data["total_projects"] == 50


def test_system_metrics_endpoint():
    res = client.get("/api/metrics/system")
    assert res.status_code == 200
    assert "mlforge_system_cpu_usage" in res.text
    assert "mlforge_total_projects 50" in res.text


def test_list_projects_and_filter():
    res = client.get("/api/v1/projects")
    assert res.status_code == 200
    json_data = res.json()
    assert json_data["meta"]["total"] == 50
    assert len(json_data["data"]) > 0

    # Filter by category
    res_cat = client.get("/api/v1/projects?category=Computer+Vision")
    assert res_cat.status_code == 200
    for p in res_cat.json()["data"]:
        assert p["category"] == "Computer Vision"


def test_project_detail_and_model_card():
    res = client.get("/api/v1/projects/ML001")
    assert res.status_code == 200
    assert res.json()["data"]["id"] == "ML001"

    card_res = client.get("/api/v1/projects/ML001/model-card")
    assert card_res.status_code == 200
    assert card_res.json()["data"]["project_id"] == "ML001"


def test_prediction_api():
    payload = {"inputs": {"feature_1": 1.0, "feature_2": 2.5, "feature_3": 15.0, "feature_4": 3.0}}
    res = client.post("/api/v1/projects/ML001/predict", json=payload)
    assert res.status_code == 200
    data = res.json()["data"]
    assert "prediction" in data
    assert "latency_ms" in data


def test_categories_endpoint():
    res = client.get("/api/v1/categories")
    assert res.status_code == 200
    data = res.json()["data"]
    assert "categories" in data
    assert len(data["categories"]) > 0


def test_roadmap_endpoint():
    res = client.get("/api/v1/roadmap")
    assert res.status_code == 200
    data = res.json()["data"]
    assert len(data["phases"]) >= 13
    assert len(data["projects_checklist"]) == 50


def test_notifications_endpoint():
    res = client.get("/api/v1/notifications")
    assert res.status_code == 200
    assert "data" in res.json()


def test_auth_login_endpoint():
    payload = {"username": "admin", "password": "adminpassword"}
    res = client.post("/api/v1/auth/login", json=payload)
    assert res.status_code == 200
    data = res.json()["data"]
    assert "access_token" in data
    assert data["role"] == "admin"
