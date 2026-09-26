import json
import os

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
config_path = os.path.join(root_dir, "platform.config.json")
out_path = os.path.join(root_dir, "dashboard", "src", "data", "projectsData.ts")

os.makedirs(os.path.dirname(out_path), exist_ok=True)

with open(config_path, "r", encoding="utf-8") as f:
    config = json.load(f)

content = f"""// AUTO-GENERATED FROM platform.config.json
export interface ProjectItem {{
  id: string;
  slug: string;
  name: string;
  category: string;
  type: string;
  status: string;
  dataset: string;
  model: string;
  metrics: string[];
  version: string;
  owner: string;
  tags: string[];
  complexity_level: 'beginner' | 'intermediate' | 'advanced';
  responsible_use_flags: string[];
  demo_mode_available: boolean;
  description: string;
  limitations: string;
  responsible_use_notes: string;
}}

export const PLATFORM_INFO = {json.dumps({
    "name": config["platform_name"],
    "tagline": config["tagline"],
    "version": config["version"],
    "description": config["description"],
    "total_projects": config["total_projects"],
    "categories": config["categories"],
    "ml_types": config["ml_types"]
}, indent=2)};

export const ALL_PROJECTS: ProjectItem[] = {json.dumps(config["projects"], indent=2)};
"""

with open(out_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Exported {len(config['projects'])} projects to {out_path}")
