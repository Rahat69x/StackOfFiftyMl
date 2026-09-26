# Identifying Recyclable Items From Images (ML029)
**Category:** Computer Vision | **ML Type:** Classification | **Platform:** MLFORGE

## 1. Overview
Waste categorization computer vision model identifying paper, plastic, glass, metal, and organic compostable materials.

## 2. Problem Type & Paradigm
- **Task:** Classification
- **Domain:** Computer Vision
- **Baseline Architecture:** Fine-Tuned Transfer Learning CNN (MobileNet)

## 3. Dataset & License
- **Dataset Identifer:** `waste_sorting_sample`
- **Sample Benchmark:** Ships with lightweight synthetic verification benchmark in `data/sample/sample_data.csv`.
- **License:** MIT / Permissive Research Use.

## 4. How to Run
```bash
# Execute standalone training smoke run
python -c "from main import get_project_instance; p = get_project_instance('.'); p.train(); print('Metrics:', p.last_metrics)"

# Run test suite
pytest tests/
```

## 5. Metrics Produced
accuracy, precision, recall, f1_score, confusion_matrix

## 6. Known Limitations
Crushed, soiled, or composite multi-material packaging (e.g. foil-lined cardboard) can lead to misclassification.

## 7. Responsible-Use Notes
Aids automated robotic recycling sorting facilities and consumer education.
