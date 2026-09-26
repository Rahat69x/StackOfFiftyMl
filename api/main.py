"""
MLFORGE Master Backend API
FastAPI application serving all 50 machine learning projects,
monitoring endpoints, documentation, and authentication.
"""

import time
import os
import uuid
import psutil
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
import logging

from core.project_registry import registry
from core.database import init_db
from api.routers import (
    projects,
    categories,
    datasets,
    models,
    notifications,
    auth,
    roadmap
)

# Configure logging
logging.basicConfig(
    level=os.environ.get("LOG_LEVEL", "INFO"),
    format='{"time": "%(asctime)s", "level": "%(levelname)s", "module": "%(name)s", "message": "%(message)s"}'
)
logger = logging.getLogger("mlforge.api")

app = FastAPI(
    title="MLFORGE — 50-in-1 Machine Learning Platform API",
    description="Unified API gateway for 50 modular, production-grade Machine Learning projects.",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json"
)

# CORS configuration
allowed_origins = os.environ.get("CORS_ALLOWED_ORIGINS", "http://localhost:3000,http://127.0.0.1:3000,http://localhost:3001").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins if allowed_origins != ["*"] else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def add_process_time_and_request_id(request: Request, call_next):
    request_id = request.headers.get("X-Request-ID", f"req_{uuid.uuid4().hex[:8]}")
    start_time = time.time()
    response: Response = await call_next(request)
    process_time = (time.time() - start_time) * 1000.0
    response.headers["X-Request-ID"] = request_id
    response.headers["X-Process-Time-Ms"] = f"{process_time:.2f}"
    return response


# Include routers under /api/v1
app.include_router(projects.router, prefix="/api/v1")
app.include_router(categories.router, prefix="/api/v1")
app.include_router(datasets.router, prefix="/api/v1")
app.include_router(models.router, prefix="/api/v1")
app.include_router(notifications.router, prefix="/api/v1")
app.include_router(auth.router, prefix="/api/v1")
app.include_router(roadmap.router, prefix="/api/v1")

# Also alias to unversioned /api/ for backward compatibility
app.include_router(projects.router, prefix="/api")
app.include_router(categories.router, prefix="/api")
app.include_router(datasets.router, prefix="/api")
app.include_router(models.router, prefix="/api")
app.include_router(notifications.router, prefix="/api")
app.include_router(auth.router, prefix="/api")
app.include_router(roadmap.router, prefix="/api")


@app.on_event("startup")
def on_startup():
    logger.info("Initializing MLFORGE databases and project registries...")
    try:
        init_db()
        registry.reload()
        logger.info(f"MLFORGE successfully started with {len(registry.get_all_projects())} projects.")
    except Exception as e:
        logger.error(f"Startup error: {e}")


@app.get("/api/health", tags=["System"])
@app.get("/health", tags=["System"])
def health_check():
    """System health check endpoint."""
    return {
        "status": "healthy",
        "platform": "MLFORGE",
        "version": "1.0.0",
        "total_projects": len(registry.get_all_projects()),
        "timestamp": time.time(),
        "database": "connected"
    }


@app.get("/api/metrics/system", response_class=PlainTextResponse, tags=["Monitoring"])
def prometheus_system_metrics():
    """Prometheus-compatible plaintext metrics export."""
    mem = psutil.virtual_memory()
    cpu = psutil.cpu_percent(interval=None)
    stats = registry.get_stats()
    
    metrics_lines = [
        "# HELP mlforge_system_cpu_usage System CPU utilization percentage",
        "# TYPE mlforge_system_cpu_usage gauge",
        f"mlforge_system_cpu_usage {cpu}",
        "",
        "# HELP mlforge_system_memory_used_bytes Memory currently utilized",
        "# TYPE mlforge_system_memory_used_bytes gauge",
        f"mlforge_system_memory_used_bytes {mem.used}",
        "",
        "# HELP mlforge_total_projects Number of registered ML projects",
        "# TYPE mlforge_total_projects gauge",
        f"mlforge_total_projects {stats.get('total_projects', 50)}",
        "",
        "# HELP mlforge_demo_ready_projects Number of projects with instant demo mode",
        "# TYPE mlforge_demo_ready_projects gauge",
        f"mlforge_demo_ready_projects {stats.get('demo_ready_count', 50)}",
        ""
    ]
    return "\n".join(metrics_lines)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api.main:app", host="127.0.0.1", port=8000, reload=True)
