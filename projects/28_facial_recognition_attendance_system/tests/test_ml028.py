"""
Pytest suite for Facial Recognition Attendance System (ML028).
Covers data loading, preprocessing, model init, training smoke test, and inference.
"""
import os
import sys
import pytest

_project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if _project_dir not in sys.path:
    sys.path.insert(0, _project_dir)

from main import get_project_instance

@pytest.fixture
def project():
    return get_project_instance(_project_dir)

def test_project_metadata(project):
    assert project.project_id == "ML028"
    assert project.name == "Facial Recognition Attendance System"

def test_load_sample_data(project):
    df = project.load_data()
    assert df is not None
    assert len(df) > 0

def test_train_and_predict(project):
    metrics = project.train()
    assert metrics is not None
    assert project.is_trained is True
    
    # Test inference
    pred = project.predict({"feature_1": 0.5, "feature_2": 1.2})
    assert "prediction" in pred

def test_model_card(project):
    card = project.get_model_card()
    assert card["project_id"] == "ML028"
    assert "reproducibility" in card
