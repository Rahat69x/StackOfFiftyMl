# Fruits And Vegetables Image Classification (ML001)
**Category:** Computer Vision | **ML Type:** Classification | **Platform:** MLFORGE

## 1. Overview
Image classification system capable of classifying agricultural produce including fruits and vegetables with data augmentation, CNN baseline, and transfer learning.

## 2. Problem Type & Paradigm
- **Task:** Classification
- **Domain:** Computer Vision
- **Baseline Architecture:** CNN Baseline / MobileNetV2

## 3. Dataset & License
- **Dataset Identifer:** `fruits_vegetables_sample`
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
Performance may degrade under extreme occlusion, poor lighting, or rare produce cultivars.

## 7. Responsible-Use Notes
Not intended for critical toxicity screening or wild mushroom foraging verification.
