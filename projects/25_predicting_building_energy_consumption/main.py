"""
Concrete MLProject implementation for Predicting Building Energy Consumption (ML025).
"""
import os
import sys
import pandas as pd

_p_dir = os.path.dirname(os.path.abspath(__file__))
if _p_dir not in sys.path:
    sys.path.insert(0, _p_dir)

from core.project_base import MLProject
from src.preprocessing import Preprocessor
from src.model import build_model
from src.train import run_training
from src.evaluate import evaluate_model_performance
from src.predict import run_prediction

class ProjectML025(MLProject):
    def __init__(self, project_dir: str):
        super().__init__(project_dir)
        self.preprocessor = Preprocessor()

    def load_data(self, data_path: str = None):
        if data_path is None or not os.path.exists(data_path):
            data_path = os.path.join(self.project_dir, "data", "sample", "sample_data.csv")
        return pd.read_csv(data_path)

    def preprocess(self, data):
        return self.preprocessor.fit_transform(data)

    def build_model(self, hyperparameters=None):
        return build_model(hyperparameters)

    def train(self, data=None, hyperparameters=None):
        if data is None:
            data = self.load_data()
        self.model, self.preprocessor, metrics = run_training(data, hyperparameters)
        self.is_trained = True
        self.last_metrics = metrics
        return metrics

    def evaluate(self, test_data=None):
        if not self.is_trained:
            self.train()
        if test_data is None:
            test_data = self.load_data()
        return evaluate_model_performance(self.model, self.preprocessor, test_data)

    def predict(self, input_data):
        if not self.is_trained:
            self.train()
        return run_prediction(self.model, self.preprocessor, input_data)

def get_project_instance(project_dir: str):
    return ProjectML025(project_dir)
