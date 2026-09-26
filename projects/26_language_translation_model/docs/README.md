# Language Translation Model (ML026)
**Category:** NLP | **ML Type:** NLP | **Platform:** MLFORGE

## 1. Overview
Machine translation research module translating phrases between language pairs using sequence-to-sequence neural architectures.

## 2. Problem Type & Paradigm
- **Task:** NLP
- **Domain:** NLP
- **Baseline Architecture:** Seq2Seq Encoder-Decoder with Bahdanau Attention Baseline

## 3. Dataset & License
- **Dataset Identifer:** `bilingual_sentences_sample`
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
bleu_score, chrf_score, exact_match_ratio

## 6. Known Limitations
Prone to hallucinations or literal mistranslations of cultural idioms and legal terminology.

## 7. Responsible-Use Notes
Not certified for official legal, diplomatic, or medical document translation without professional certified human translators.
