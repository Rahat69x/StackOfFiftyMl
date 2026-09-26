"""
MLFORGE CLI Scaffolding Tool — Add Project 51+
Automates adding new machine learning projects into the master platform architecture.
"""

import os
import sys
import json
import argparse
import re

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CONFIG_PATH = os.path.join(ROOT_DIR, "platform.config.json")

def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"[\s_-]+", "_", text)

def get_next_project_id_and_number(projects):
    max_num = 0
    for p in projects:
        m = re.match(r"ML(\d+)", p["id"])
        if m:
            num = int(m.group(1))
            if num > max_num:
                max_num = num
    next_num = max_num + 1
    return f"ML{next_num:03d}", next_num

def main():
    parser = argparse.ArgumentParser(description="Scaffold a new project in MLFORGE (Project 51+)")
    parser.add_argument("name", help="Human-readable project title")
    parser.add_argument("--category", default="Computer Vision", help="Project category")
    parser.add_argument("--type", default="Classification", help="ML paradigm (Classification, Regression, NLP, etc.)")
    parser.add_argument("--complexity", default="intermediate", choices=["beginner", "intermediate", "advanced"])
    parser.add_argument("--description", default="", help="Short description of the ML project")
    parser.add_argument("--responsible-flags", nargs="*", default=[], help="Responsible AI flags (e.g. healthcare, finance, surveillance)")

    args = parser.parse_args()

    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        config = json.load(f)

    projects = config["projects"]
    pid, num = get_next_project_id_and_number(projects)
    slug = f"{num:02d}_{slugify(args.name)}"

    desc = args.description or f"Autonomous machine learning module for {args.name}."
    
    new_entry = {
        "id": pid,
        "slug": slug,
        "name": args.name,
        "category": args.category,
        "type": args.type,
        "status": "ready",
        "dataset": f"{slugify(args.name)}_sample",
        "model": "Ensemble / Baseline Architecture",
        "metrics": ["accuracy", "precision", "recall", "f1_score"] if args.type == "Classification" else ["mae", "rmse", "r2_score"],
        "version": "1.0.0",
        "owner": "MLForge Contributor",
        "tags": [slugify(args.category), slugify(args.type)],
        "complexity_level": args.complexity,
        "responsible_use_flags": args.responsible_flags,
        "demo_mode_available": True,
        "description": desc,
        "limitations": "Model performance is bounded by sample domain assumptions.",
        "responsible_use_notes": "Research and development demonstration only."
    }

    # Append to config and save
    projects.append(new_entry)
    config["total_projects"] = len(projects)
    if args.category not in config["categories"]:
        config["categories"].append(args.category)
        config["categories"].sort()

    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)

    # Now scaffold the directory using the master scaffolder logic
    from scaffold_all_projects import scaffold_project
    scaffold_project(new_entry)

    print(f"\n[SUCCESS] Scaffolded Project {pid}: '{args.name}'")
    print(f"Directory: projects/{slug}")
    print(f"Platform total projects: {len(projects)}")
    print("Run tests with:")
    print(f"  python -m pytest projects/{slug}/tests/\n")

if __name__ == "__main__":
    main()
