.PHONY: help dev test lint up down scaffold-all new-project

help:
	@echo "MLFORGE Command Reference:"
	@echo "  make dev          - Install dependencies and prepare local environment"
	@echo "  make test         - Run full pytest suite across core and project modules"
	@echo "  make lint         - Run code linting and style checks"
	@echo "  make up           - Start multi-service environment via Docker Compose"
	@echo "  make down         - Stop Docker Compose services"
	@echo "  make scaffold-all - Re-scaffold all 50 projects"
	@echo "  make new-project  - Scaffold a new project (e.g. Project 51+)"

dev:
	pip install -e .[dev]
	python scripts/build_platform_config.py
	python -c "import core.database as db; db.init_db()"

test:
	pytest tests/

lint:
	python -m py_compile core/*.py api/*.py

up:
	docker compose up --build

down:
	docker compose down

scaffold-all:
	python scripts/scaffold_all_projects.py

new-project:
	@echo "Usage: python scripts/new_project.py \"Project Name\" --category \"Category\""
