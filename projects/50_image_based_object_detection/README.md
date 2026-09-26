# Image-Based Object Detection (ML050)
**Category:** Computer Vision | **ML Type:** Computer Vision | **Platform:** MLFORGE

## 1. Overview
Object detection computer-vision framework predicting 2D bounding boxes, confidence probabilities, and multi-class labels in digital imagery.

## 2. Problem Type & Paradigm
- **Task:** Computer Vision
- **Domain:** Computer Vision
- **Baseline Architecture:** Anchor-Free Object Detection Pipeline (YOLO/SSD Baseline)

## 3. Dataset & License
- **Dataset Identifer:** `annotated_bboxes_sample`
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
map_50, precision, recall, inference_fps

## 6. Known Limitations
Severe motion blur or small distant objects (<16x16 pixels) present lower detection recall.

## 7. Responsible-Use Notes
Ensure surveillance privacy regulations (e.g. GDPR, local biometrics acts) are strictly adhered to in real-world deployments.
