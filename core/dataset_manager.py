"""
MLFORGE Core — Shared Data Engine
Handles ingestion, synthetic data generation, validation, splitting,
normalization, encoding, and lineage tracking for all 50 projects.
"""

import os
import json
import hashlib
import time
from typing import Any, Dict, List, Optional, Tuple, Union
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
from sklearn.impute import SimpleImputer
import logging

logger = logging.getLogger("mlforge.core.dataset_manager")


class DatasetManager:
    """
    Central dataset engine for MLFORGE.
    Supports CSV, JSON, Time-Series, NLP text, Image tensors, and synthetic data generators.
    """

    def __init__(self, base_data_dir: Optional[str] = None):
        if base_data_dir is None:
            self.base_data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
        else:
            self.base_data_dir = base_data_dir
        os.makedirs(self.base_data_dir, exist_ok=True)

    def compute_hash(self, data_or_path: Union[str, pd.DataFrame, np.ndarray]) -> str:
        """Computes SHA-256 fingerprint for dataset versioning."""
        hasher = hashlib.sha256()
        if isinstance(data_or_path, str) and os.path.exists(data_or_path):
            with open(data_or_path, "rb") as f:
                while chunk := f.read(8192):
                    hasher.update(chunk)
            return hasher.hexdigest()[:16]
        elif isinstance(data_or_path, pd.DataFrame):
            hasher.update(pd.util.hash_pandas_object(data_or_path).values)
            return hasher.hexdigest()[:16]
        elif isinstance(data_or_path, np.ndarray):
            hasher.update(data_or_path.tobytes())
            return hasher.hexdigest()[:16]
        else:
            hasher.update(str(data_or_path).encode("utf-8"))
            return hasher.hexdigest()[:16]

    def load_csv(self, filepath: str) -> pd.DataFrame:
        """Loads CSV dataset safely."""
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Dataset file not found: {filepath}")
        return pd.read_csv(filepath)

    def load_json(self, filepath: str) -> Any:
        """Loads JSON dataset."""
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"JSON dataset file not found: {filepath}")
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)

    def split_data(
        self,
        X: Union[pd.DataFrame, np.ndarray, List[Any]],
        y: Optional[Union[pd.Series, np.ndarray, List[Any]]] = None,
        test_size: float = 0.2,
        val_size: float = 0.0,
        random_state: int = 42,
        stratify: bool = False,
        shuffle: bool = True
    ) -> Dict[str, Any]:
        """
        Splits data into train, test, and optional validation sets.
        Preserves temporal order if shuffle=False (for time series).
        """
        strat = y if (stratify and y is not None and len(np.unique(y)) > 1) else None
        
        if val_size > 0.0:
            total_holdout = test_size + val_size
            X_train, X_rem, y_train, y_rem = train_test_split(
                X, y, test_size=total_holdout, random_state=random_state, shuffle=shuffle, stratify=strat
            )
            ratio = test_size / total_holdout
            rem_strat = y_rem if (stratify and y_rem is not None) else None
            X_val, X_test, y_val, y_test = train_test_split(
                X_rem, y_rem, test_size=ratio, random_state=random_state, shuffle=shuffle, stratify=rem_strat
            )
            return {
                "X_train": X_train, "y_train": y_train,
                "X_val": X_val, "y_val": y_val,
                "X_test": X_test, "y_test": y_test
            }
        else:
            if y is not None:
                X_train, X_test, y_train, y_test = train_test_split(
                    X, y, test_size=test_size, random_state=random_state, shuffle=shuffle, stratify=strat
                )
                return {"X_train": X_train, "y_train": y_train, "X_test": X_test, "y_test": y_test}
            else:
                X_train, X_test = train_test_split(
                    X, test_size=test_size, random_state=random_state, shuffle=shuffle
                )
                return {"X_train": X_train, "X_test": X_test}

    def clean_and_impute(
        self,
        df: pd.DataFrame,
        numeric_strategy: str = "median",
        categorical_strategy: str = "most_frequent"
    ) -> pd.DataFrame:
        """Handles missing values across numeric and categorical columns."""
        df_clean = df.copy()
        num_cols = df_clean.select_dtypes(include=[np.number]).columns
        cat_cols = df_clean.select_dtypes(exclude=[np.number]).columns
        
        if len(num_cols) > 0:
            imp_num = SimpleImputer(strategy=numeric_strategy)
            df_clean[num_cols] = imp_num.fit_transform(df_clean[num_cols])
            
        if len(cat_cols) > 0:
            imp_cat = SimpleImputer(strategy=categorical_strategy)
            df_clean[cat_cols] = imp_cat.fit_transform(df_clean[cat_cols])
            
        return df_clean

    def scale_features(
        self,
        train_features: np.ndarray,
        test_features: Optional[np.ndarray] = None,
        method: str = "standard"
    ) -> Tuple[np.ndarray, Optional[np.ndarray], Any]:
        """Scales numeric features using StandardScaler or MinMaxScaler."""
        scaler = StandardScaler() if method == "standard" else MinMaxScaler()
        train_scaled = scaler.fit_transform(train_features)
        test_scaled = scaler.transform(test_features) if test_features is not None else None
        return train_scaled, test_scaled, scaler

    def validate_dataset(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Inspects and returns metadata, missingness, and column statistics."""
        return {
            "num_rows": int(len(df)),
            "num_columns": int(len(df.columns)),
            "columns": list(df.columns),
            "column_types": {col: str(dtype) for col, dtype in df.dtypes.items()},
            "missing_values": {col: int(cnt) for col, cnt in df.isnull().sum().items()},
            "memory_usage_bytes": int(df.memory_usage(deep=True).sum()),
            "data_hash": self.compute_hash(df)
        }

    # =========================================================================
    # SYNTHETIC DATA GENERATORS FOR CI, SMOKE TESTS, AND DEMOS
    # =========================================================================

    def generate_tabular_classification(
        self, n_samples: int = 150, n_features: int = 6, n_classes: int = 3, random_state: int = 42
    ) -> Tuple[pd.DataFrame, pd.Series]:
        """Generates synthetic tabular classification dataset."""
        np.random.seed(random_state)
        X = np.random.randn(n_samples, n_features)
        weights = np.random.randn(n_features, n_classes)
        logits = np.dot(X, weights)
        probs = np.exp(logits) / np.sum(np.exp(logits), axis=1, keepdims=True)
        y = np.array([np.random.choice(n_classes, p=p) for p in probs])
        
        feature_names = [f"feature_{i+1}" for i in range(n_features)]
        df_X = pd.DataFrame(X, columns=feature_names)
        series_y = pd.Series(y, name="target")
        return df_X, series_y

    def generate_tabular_regression(
        self, n_samples: int = 150, n_features: int = 5, noise: float = 0.1, random_state: int = 42
    ) -> Tuple[pd.DataFrame, pd.Series]:
        """Generates synthetic regression dataset."""
        np.random.seed(random_state)
        X = np.random.randn(n_samples, n_features)
        weights = np.random.uniform(0.5, 3.0, size=n_features)
        y = np.dot(X, weights) + np.random.normal(0, noise, size=n_samples)
        
        feature_names = [f"predictor_{i+1}" for i in range(n_features)]
        df_X = pd.DataFrame(X, columns=feature_names)
        series_y = pd.Series(y, name="target")
        return df_X, series_y

    def generate_time_series(
        self, n_steps: int = 200, freq: str = "h", seasonal_period: int = 24, random_state: int = 42
    ) -> pd.DataFrame:
        """Generates synthetic time series dataset with trend, seasonality, and noise."""
        np.random.seed(random_state)
        t = np.arange(n_steps)
        trend = 0.05 * t
        seasonality = 10.0 * np.sin(2 * np.pi * t / seasonal_period)
        noise = np.random.normal(0, 1.5, size=n_steps)
        values = 50.0 + trend + seasonality + noise
        
        timestamps = pd.date_range(start="2026-01-01", periods=n_steps, freq=freq)
        return pd.DataFrame({"timestamp": timestamps, "value": values, "exog_var": np.random.uniform(10, 30, n_steps)})

    def generate_nlp_sentiment(self, n_samples: int = 120) -> pd.DataFrame:
        """Generates synthetic labeled sentiment reviews."""
        positive_templates = [
            "Outstanding quality and works wonderfully well!",
            "I absolutely love this product, highly recommended.",
            "Exceeded all my expectations. Fast delivery and great support.",
            "Superb performance, reliable and very well built.",
            "Five stars! Easy to use and sleek design."
        ]
        negative_templates = [
            "Terrible experience, arrived damaged and stopped working.",
            "Completely dissatisfied with the poor quality and customer service.",
            "Do not purchase this, total waste of money.",
            "Very buggy, crashes constantly and difficult to navigate.",
            "Subpar material, broke within two days of normal usage."
        ]
        neutral_templates = [
            "Average product, does the job but nothing extraordinary.",
            "Standard delivery time, package arrived intact. Okay value.",
            "Works as described in manual, neither great nor bad.",
            "Mediocre performance for this price point.",
            "Decent build quality, fulfills basic requirements."
        ]
        
        rows = []
        for i in range(n_samples):
            choice = i % 3
            if choice == 0:
                text = positive_templates[i % len(positive_templates)]
                label = "positive"
            elif choice == 1:
                text = negative_templates[i % len(negative_templates)]
                label = "negative"
            else:
                text = neutral_templates[i % len(neutral_templates)]
                label = "neutral"
            rows.append({"text": text, "sentiment": label, "review_id": f"REV_{i+1:04d}"})
        return pd.DataFrame(rows)

    def generate_synthetic_image_batch(
        self, n_samples: int = 20, channels: int = 3, height: int = 64, width: int = 64, n_classes: int = 4
    ) -> Tuple[np.ndarray, np.ndarray]:
        """Generates synthetic image tensors and class labels."""
        np.random.seed(42)
        images = np.random.uniform(0.0, 1.0, size=(n_samples, height, width, channels)).astype(np.float32)
        labels = np.random.randint(0, n_classes, size=(n_samples,))
        return images, labels


# Global singleton instance
dataset_manager = DatasetManager()
