# MLFORGE Installation & Onboarding Guide

## Quickstart (Section 33)

Follow these steps to get MLFORGE running locally in minutes:

### 1. Prerequisites
- Python 3.10+ (tested on Python 3.11, 3.12, 3.13)
- Node.js 18+ and npm
- Docker and Docker Compose (optional for containerized deployment)

### 2. Local Setup
```bash
# 1. Clone repository
git clone https://github.com/mlforge/mlforge.git
cd mlforge

# 2. Configure environment
cp .env.example .env

# 3. Install Python dependencies
pip install -e .[dev]

# 4. Initialize database and project registry
python scripts/build_platform_config.py
python -c "import core.database as db; db.init_db()"

# 5. Run tests to verify setup
pytest tests/unit/ tests/api/
```

### 3. Launching the Backend API
```bash
uvicorn api.main:app --host 127.0.0.1 --port 8000 --reload
```
Access interactive OpenAPI documentation at: `http://localhost:8000/api/docs`.

### 4. Launching the Next.js Dashboard
```bash
cd dashboard
npm install
npm run dev
```
Visit `http://localhost:3000` to browse all 50 projects!

### 5. Multi-Container Production Run
```bash
docker compose up --build
```
This spins up API, Dashboard, PostgreSQL, Redis, MLflow, Prometheus, and Grafana.
