# Lane Detection In Images Or Videos (ML011)
**Category:** Computer Vision | **ML Type:** Computer Vision | **Platform:** MLFORGE

## 1. Overview
Autonomous vehicle computer-vision module isolating road lanes, curvature polynomial fitting, and lane departure warnings.

## 2. Problem Type & Paradigm
- **Task:** Computer Vision
- **Domain:** Computer Vision
- **Baseline Architecture:** Canny Edge + Hough Transform Pipeline / Segmentation CNN

## 3. Dataset & License
- **Dataset Identifer:** `road_lane_frames_sample`
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
iou, detection_accuracy, latency_ms

## 6. Known Limitations
Degrades severely under heavy snow, unpaved terrain, faded lane markings, or direct blinding sunlight.

## 7. Responsible-Use Notes
RESEARCH DEMO ONLY: Under no circumstances should this software be connected to actual steering or motor actuators in real motor vehicles.
