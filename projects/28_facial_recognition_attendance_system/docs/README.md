# Facial Recognition Attendance System (ML028)
**Category:** Computer Vision | **ML Type:** Classification | **Platform:** MLFORGE

## 1. Overview
Controlled biometric attendance verification research system matching face embeddings with privacy and explicit consent safeguards.

## 2. Problem Type & Paradigm
- **Task:** Classification
- **Domain:** Computer Vision
- **Baseline Architecture:** Haar Cascade / FaceNet Embedding Matcher with Cosine Distance

## 3. Dataset & License
- **Dataset Identifer:** `face_embeddings_sample`
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
verification_accuracy, far, frr, threshold_distance

## 6. Known Limitations
Performance skews across different demographic lighting conditions and age variations.

## 7. Responsible-Use Notes
STRICT ETHICS & PRIVACY: Requires explicit written consent, non-reversible encrypted embeddings, right-to-be-forgotten deletion flow, and prohibition of covert public surveillance.
