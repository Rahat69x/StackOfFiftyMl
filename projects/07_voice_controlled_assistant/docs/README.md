# Voice-Controlled Assistant (ML007)
**Category:** Audio / NLP | **ML Type:** Classification | **Platform:** MLFORGE

## 1. Overview
Voice-controlled ML assistant pipeline integrating audio spectrogram processing, intent classification, command routing, and text-to-speech output.

## 2. Problem Type & Paradigm
- **Task:** Classification
- **Domain:** Audio / NLP
- **Baseline Architecture:** Acoustic Spectrogram Featurizer + Intent Router + Speech Synthesis

## 3. Dataset & License
- **Dataset Identifer:** `voice_commands_sample`
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
intent_accuracy, wer_proxy, latency_ms

## 6. Known Limitations
Susceptible to ambient noise and non-standard dialects or accents.

## 7. Responsible-Use Notes
User audio data must not be stored without explicit permission; respect privacy controls.
