# Generative Faces Using GANs (ML016)
**Category:** Generative AI | **ML Type:** Generative AI | **Platform:** MLFORGE

## 1. Overview
Controlled generative image modeling implementation synthesizing low-resolution face avatars with balanced generator-discriminator dynamics.

## 2. Problem Type & Paradigm
- **Task:** Generative AI
- **Domain:** Generative AI
- **Baseline Architecture:** Deep Convolutional GAN (DCGAN) Architecture

## 3. Dataset & License
- **Dataset Identifer:** `face_avatar_thumbnails_sample`
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
fid_score_proxy, generator_loss, discriminator_loss

## 6. Known Limitations
Susceptible to mode collapse and training artifacts without extensive multi-GPU hyperparameter tuning.

## 7. Responsible-Use Notes
All generated imagery must be visibly marked as synthetic AI-generated content. Strictly prohibited for deepfake impersonation.
