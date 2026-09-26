"""
MLFORGE Database Engine & ORM Models
Defines all 16 required tables supporting PostgreSQL and SQLite fallback.
"""

import os
import time
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Float,
    Boolean,
    Text,
    DateTime,
    JSON,
    ForeignKey
)
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///./mlforge.db")

# Handle sqlite specific connect args
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# -----------------------------------------------------------------------------
# ORM MODEL DEFINITIONS (ALL TABLES)
# -----------------------------------------------------------------------------

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(64), unique=True, index=True, nullable=False)
    email = Column(String(128), unique=True, index=True, nullable=False)
    hashed_password = Column(String(256), nullable=False)
    role = Column(String(32), default="data_scientist")
    is_active = Column(Boolean, default=True)
    created_at = Column(Float, default=time.time)


class Project(Base):
    __tablename__ = "projects"
    id = Column(String(16), primary_key=True, index=True)  # e.g. ML001
    slug = Column(String(128), unique=True, index=True, nullable=False)
    name = Column(String(128), nullable=False)
    category = Column(String(64), index=True, nullable=False)
    type = Column(String(64), index=True, nullable=False)
    status = Column(String(32), default="ready")
    dataset = Column(String(128))
    model_name = Column(String(128))
    version = Column(String(16), default="1.0.0")
    description = Column(Text)
    limitations = Column(Text)
    responsible_use_notes = Column(Text)
    responsible_use_flags = Column(JSON, default=list)
    tags = Column(JSON, default=list)
    created_at = Column(Float, default=time.time)


class Dataset(Base):
    __tablename__ = "datasets"
    id = Column(String(64), primary_key=True, index=True)
    project_id = Column(String(16), ForeignKey("projects.id"))
    name = Column(String(128), nullable=False)
    format = Column(String(32), default="csv")
    filepath = Column(String(256))
    num_rows = Column(Integer, default=0)
    data_hash = Column(String(64))
    created_at = Column(Float, default=time.time)


class DatasetVersion(Base):
    __tablename__ = "dataset_versions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    dataset_id = Column(String(64), ForeignKey("datasets.id"))
    version = Column(String(16), default="1.0")
    data_hash = Column(String(64))
    transformations = Column(JSON, default=list)
    created_at = Column(Float, default=time.time)


class Experiment(Base):
    __tablename__ = "experiments"
    id = Column(String(64), primary_key=True, index=True)
    project_id = Column(String(16), ForeignKey("projects.id"))
    model_name = Column(String(128))
    status = Column(String(32), default="completed")
    duration_seconds = Column(Float, default=0.0)
    hyperparameters = Column(JSON, default=dict)
    random_seed = Column(Integer, default=42)
    git_commit_hash = Column(String(64))
    created_at = Column(Float, default=time.time)


class TrainingRun(Base):
    __tablename__ = "training_runs"
    id = Column(String(64), primary_key=True, index=True)
    experiment_id = Column(String(64), ForeignKey("experiments.id"))
    epoch = Column(Integer, default=1)
    loss = Column(Float, default=0.0)
    metrics_snapshot = Column(JSON, default=dict)
    timestamp = Column(Float, default=time.time)


class ModelArtifact(Base):
    __tablename__ = "models"
    id = Column(String(64), primary_key=True, index=True)
    project_id = Column(String(16), ForeignKey("projects.id"))
    version = Column(String(16), default="1.0.0")
    artifact_path = Column(String(256))
    status = Column(String(32), default="active")
    metrics = Column(JSON, default=dict)
    created_at = Column(Float, default=time.time)


class PredictionRecord(Base):
    __tablename__ = "predictions"
    id = Column(String(64), primary_key=True, index=True)
    project_id = Column(String(16), ForeignKey("projects.id"))
    model_version = Column(String(16))
    input_payload = Column(JSON)
    prediction_output = Column(JSON)
    latency_ms = Column(Float, default=0.0)
    created_at = Column(Float, default=time.time)


class MetricRecord(Base):
    __tablename__ = "metrics"
    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(String(16), ForeignKey("projects.id"))
    metric_name = Column(String(64), nullable=False)
    metric_value = Column(Float, nullable=False)
    model_version = Column(String(16))
    created_at = Column(Float, default=time.time)


class ReportRecord(Base):
    __tablename__ = "reports"
    id = Column(String(64), primary_key=True, index=True)
    project_id = Column(String(16), ForeignKey("projects.id"))
    title = Column(String(128))
    markdown_path = Column(String(256))
    json_path = Column(String(256))
    sections_data = Column(JSON)
    created_at = Column(Float, default=time.time)


class AuditLog(Base):
    __tablename__ = "audit_logs"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user = Column(String(64), default="system")
    action = Column(String(64), nullable=False)
    resource = Column(String(128), nullable=False)
    status = Column(String(32), default="success")
    details = Column(JSON, default=dict)
    created_at = Column(Float, default=time.time)


class NotificationRecord(Base):
    __tablename__ = "notifications"
    id = Column(String(64), primary_key=True, index=True)
    project_id = Column(String(16), default="SYSTEM")
    title = Column(String(128), nullable=False)
    message = Column(Text, nullable=False)
    type = Column(String(32), default="info")
    read = Column(Boolean, default=False)
    created_at = Column(Float, default=time.time)


class ModelCardRecord(Base):
    __tablename__ = "model_cards"
    id = Column(String(64), primary_key=True, index=True)  # project_id
    project_id = Column(String(16), ForeignKey("projects.id"), unique=True)
    card_data = Column(JSON, nullable=False)
    updated_at = Column(Float, default=time.time)


class ApiKey(Base):
    __tablename__ = "api_keys"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    key_hash = Column(String(64), unique=True, index=True)
    name = Column(String(64))
    rate_limit = Column(Integer, default=60)
    created_at = Column(Float, default=time.time)


class Role(Base):
    __tablename__ = "roles"
    name = Column(String(32), primary_key=True)
    description = Column(String(128))


class Permission(Base):
    __tablename__ = "permissions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    role_name = Column(String(32), ForeignKey("roles.name"))
    action = Column(String(64), nullable=False)


def init_db():
    """Initializes all database tables."""
    Base.metadata.create_all(bind=engine)


def get_db():
    """FastAPI DB session dependency generator."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
