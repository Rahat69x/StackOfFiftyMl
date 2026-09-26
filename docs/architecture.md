# MLFORGE Architecture Specification

## 1. High-Level System Overview
MLFORGE is a unified Machine Learning platform that operates on the **Shared Infrastructure / Modular Project** paradigm.

```
+-------------------------------------------------------------------------+
|                        MLFORGE DASHBOARD (Next.js)                      |
|  Projects Catalog | Model Cards | Live Demos | Lineage | Roadmap | Health|
+-------------------------------------------------------------------------+
                                   │ HTTP / JSON
                                   ▼
+-------------------------------------------------------------------------+
|                        FASTAPI MASTER GATEWAY                           |
|  /api/v1/projects  | /api/v1/models | /api/v1/datasets | /api/metrics   |
+-------------------------------------------------------------------------+
        │                       │                        │
        ▼                       ▼                        ▼
+----------------+      +----------------+       +----------------+
|  CORE ENGINES  |      |  DATABASE      |       |  STORAGE       |
|  - Registry    |      |  - 16 Tables   |       |  - Models/     |
|  - Data Engine |      |  - PostgreSQL  |       |  - Reports/    |
|  - Trainers    |      |    or SQLite   |       |  - Experiments/|
|  - Evaluators  |      +----------------+       +----------------+
|  - Security    |
+----------------+
        │
        ▼
+─────────────────────────────────────────────────────────────────────────+
|                          50 ML PROJECT MODULES                          |
|  01 Fruits/Veg -> 50 Object Detection (All standardized & runnable)     |
+─────────────────────────────────────────────────────────────────────────+
```

## 2. Core Engines Reference
- **`ProjectRegistry`**: Discovers and indexes projects from `platform.config.json`.
- **`DatasetManager`**: Ingests, hashes, and synthetically generates benchmarking datasets for offline CI runs.
- **`TrainingEngine`**: Reusable trainers across classification, regression, time series, NLP, vision, audio, and anomaly detection.
- **`EvaluationEngine`**: Unified metric calculation with confusion matrix generation.
- **`ModelRegistry`**: Versioning, metadata indexing, artifact saving, and rollbacks.
- **`ExperimentTracker`**: Full provenance logging (hyperparams, seeds, system resources).
- **`ReportingEngine`**: 16-section automated Markdown/JSON report synthesis.
- **`NotificationEngine`**: Live event bus for job completions and model drift warnings.
- **`SecurityPolicy`**: JWT token signing, RBAC permissions, and audit logging.
