# Crop Disease Detection From Images (ML032)
**Category:** Computer Vision | **ML Type:** Classification | **Platform:** MLFORGE

## 1. Overview
Agricultural vision system detecting foliar diseases, blights, and fungal infections on crop leaves.

## 2. Problem Type & Paradigm
- **Task:** Classification
- **Domain:** Computer Vision
- **Baseline Architecture:** Plant Disease CNN Classifier (ResNet / MobileNet)

## 3. Dataset & License
- **Dataset Identifer:** `plant_pathology_sample`
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
Nutrient deficiencies and pest damage can visually mimic viral/fungal symptoms.

## 7. Responsible-Use Notes
AGRICULTURAL NOTICE: Educational research tool. Always consult certified local agronomists before applying chemical fungicides or treatments.
