# Emotional Text-To-Speech Synthesis (ML039)
**Category:** Audio / Generative AI | **ML Type:** Generative AI | **Platform:** MLFORGE

## 1. Overview
Expressive text-to-speech synthesis pipeline modulating vocal pitch, cadence, and prosody to reflect selected emotional styles.

## 2. Problem Type & Paradigm
- **Task:** Generative AI
- **Domain:** Audio / Generative AI
- **Baseline Architecture:** Emotion Conditioning Spectrogram Generator + Vocoder

## 3. Dataset & License
- **Dataset Identifer:** `expressive_speech_sample`
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
mel_cepstral_distortion, mos_proxy, latency_ms

## 6. Known Limitations
Synthesized voices may sound robotic or exhibit phoneme clipping on complex polysyllabic words.

## 7. Responsible-Use Notes
Synthesized audio must carry watermarking or synthetic speech identification to prevent voice cloning fraud.
