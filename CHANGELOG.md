# Changelog

All notable changes to the MLFORGE platform will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-09-26

### Added
- **Core Architecture:**
  - Standardized `MLProject` base interface across all 50 machine learning projects.
  - Central `ProjectRegistry` dynamic loading and taxonomy index.
  - Shared `DatasetManager` supporting tabular, time-series, NLP, and computer vision data.
  - Shared `TrainingEngine` and `EvaluationEngine` supporting uniform cross-paradigm metrics.
  - Central `ModelRegistry` with semantic versioning, artifact persistence, and rollback controls.
  - Shared `ExperimentTracker` capturing hyperparams, commit hashes, random seeds, and compute resource metrics.
  - Shared `ReportingEngine` generating 16-section reports in Markdown and JSON.
  - Shared `NotificationEngine` for live job completion and drift alerts.
  - Shared `SecurityPolicy` with JWT authentication, RBAC (admin/data_scientist/viewer), and audit logging.
- **50-in-1 Project Modules:**
  - All 50 machine learning project modules scaffolded with standardized folders, preprocessing, models, test suites, sample benchmark data, and model cards.
- **Master Backend API:**
  - FastAPI `/api/v1` routes with OpenAPI documentation, Prometheus metrics export (`/api/metrics/system`), and health checks.
- **Scaffolding CLI:**
  - `scripts/new_project.py` enabling one-command generation of Project 51+ and beyond.
- **Interactive Dashboard:**
  - Next.js / Tailwind CSS / Recharts interactive dashboard with search, category filtering, model cards, live training and prediction demos, and roadmap tracking.
