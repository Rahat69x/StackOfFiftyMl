# Contributing to MLFORGE

Thank you for contributing to MLFORGE!

## Adding Project 51+
MLFORGE is engineered for seamless horizontal expansion. To add a new project:

1. Run the scaffolding CLI:
   ```bash
   python scripts/new_project.py "Your Project Name" --category "Your Category" --type "Classification"
   ```
2. Populate specific domain preprocessing in `projects/51_your_project/src/preprocessing.py`.
3. Configure model architecture in `src/model.py`.
4. Add real or benchmark datasets into `data/sample/`.
5. Run the test suite:
   ```bash
   pytest projects/51_your_project/tests/
   ```
6. Update documentation and model card in `projects/51_your_project/docs/`.

## PR Quality Checklist
- [ ] No secrets or credentials committed (use `.env`).
- [ ] Tests pass (`pytest tests/`).
- [ ] Code formatted according to `pyproject.toml`.
- [ ] Model card updated if adding or modifying responsible-use flagged domains.
