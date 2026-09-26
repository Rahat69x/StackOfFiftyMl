# Cancer Type Prediction From Medical Imaging (ML019)
**Category:** Computer Vision / Healthcare Research | **ML Type:** Classification | **Platform:** MLFORGE

## 1. Overview
Medical imaging oncology research classifier analyzing histopathological patterns with calibrated uncertainty metrics.

## 2. Problem Type & Paradigm
- **Task:** Classification
- **Domain:** Computer Vision / Healthcare Research
- **Baseline Architecture:** Pretrained CNN Feature Extractor + Calibrated Classifier

## 3. Dataset & License
- **Dataset Identifer:** `histopathology_imaging_sample`
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
sensitivity, specificity, precision, recall, roc_auc, confusion_matrix

## 6. Known Limitations
Staining differences across medical institutions can cause domain shift errors.

## 7. Responsible-Use Notes
STRICT MEDICAL DISCLAIMER: Research-only demonstrator. Under no circumstances should this be used for clinical diagnostic decision-making.
