# ADR 001: Master Multi-Project Platform Architecture

## Status
Accepted

## Context
MLFORGE is designed as a unified Machine Learning laboratory housing 50 distinct, production-grade ML modules ranging from Computer Vision and NLP to Healthcare Research, Anomaly Detection, Time-Series Forecasting, and Reinforcement Learning. Rather than managing 50 disconnected repositories with redundant data loading, training loops, model stores, and reporting scripts, a unified shared architecture was required.

## Decision
1. **Shared Foundation:** All projects extend from `core.project_base.MLProject`. The platform provides uniform singletons for `DatasetManager`, `TrainingEngine`, `EvaluationEngine`, `ModelRegistry`, `ExperimentTracker`, `ReportingEngine`, `NotificationEngine`, and `SecurityPolicy`.
2. **Central Project Registry:** `platform.config.json` serves as the single source of truth for taxonomy, metadata, complexity levels, and ethical flags.
3. **Decoupled Yet Uniform Directory Structure:** Every project directory follows a standardized contract (`src/`, `api/`, `data/sample/`, `models/`, `tests/`, `docs/model_card.md`).
4. **Reproducibility Guarantee:** Every experiment logs random seeds, package versions, and dataset SHA-256 hashes.
5. **Responsible AI by Design:** Projects touching sensitive domains (healthcare, employment, surveillance, finance, elections) enforce model cards and clear non-clinical/non-binding disclaimers.

## Consequences
- Zero duplication of training and evaluation plumbing.
- Dynamic project discovery makes adding Project 51+ a single-command operation.
- Consistent API contracts and dashboard rendering across all 50 projects.
