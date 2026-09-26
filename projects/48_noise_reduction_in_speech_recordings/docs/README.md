# Noise Reduction In Speech Recordings (ML048)
**Category:** Audio | **ML Type:** Audio | **Platform:** MLFORGE

## 1. Overview
Audio signal enhancement pipeline isolating human voice waveforms and attenuating background acoustic noise using spectral subtraction.

## 2. Problem Type & Paradigm
- **Task:** Audio
- **Domain:** Audio
- **Baseline Architecture:** Spectral Subtraction / Masking U-Net Autoencoder

## 3. Dataset & License
- **Dataset Identifer:** `noisy_speech_spectrograms_sample`
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
snr_improvement_db, pesq_proxy, latency_ms

## 6. Known Limitations
Extreme non-stationary noise can induce musical artifacts or phase distortions in the output audio.

## 7. Responsible-Use Notes
Enhances speech clarity in videoconferencing and assistive hearing devices.
