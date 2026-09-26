#!/usr/bin/env bash
# MLFORGE CLI Scaffolder Shell Wrapper
set -e

if [ -z "$1" ]; then
    echo "Usage: ./scripts/new_project.sh \"Project Title\" [--category \"Category\"] [--type \"Classification\"]"
    exit 1
fi

python scripts/new_project.py "$@"
