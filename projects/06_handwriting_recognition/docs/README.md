# Handwriting Recognition (ML006)
**Category:** Computer Vision | **ML Type:** Classification | **Platform:** MLFORGE

## 1. Overview
Handwriting character and digit recognition system featuring grayscale normalizer, morphological cleaning, and deep CNN classifier.

## 2. Problem Type & Paradigm
- **Task:** Classification
- **Domain:** Computer Vision
- **Baseline Architecture:** Convolutional Neural Network (CNN)

## 3. Dataset & License
- **Dataset Identifer:** `handwritten_digits_chars_sample`
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
Accuracy degrades on cursive ligatures or degraded scanned documents.

## 7. Responsible-Use Notes
Ensure training covers diverse handwriting cultures and styles without systemic bias.
