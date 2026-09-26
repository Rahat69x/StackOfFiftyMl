# Analyzing Brain Signals For Cognitive States (ML040)
**Category:** Classification / Healthcare Research | **ML Type:** Classification | **Platform:** MLFORGE

## 1. Overview
Brain-computer interface research module extracting theta/alpha/beta frequency bandpowers from EEG channels to classify cognitive focus.

## 2. Problem Type & Paradigm
- **Task:** Classification
- **Domain:** Classification / Healthcare Research
- **Baseline Architecture:** Bandpower Spectral Featurizer + Support Vector Machine

## 3. Dataset & License
- **Dataset Identifer:** `eeg_channels_sample`
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
EEG leads capture substantial electromyographic muscle movement and ocular blink noise artifacts.

## 7. Responsible-Use Notes
RESEARCH ONLY: Strictly for exploratory BCI studies. Do not claim clinical diagnostic validity for neurological disorders.
