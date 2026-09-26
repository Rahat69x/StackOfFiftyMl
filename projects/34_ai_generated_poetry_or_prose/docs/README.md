# AI-Generated Poetry Or Prose (ML034)
**Category:** Generative AI | **ML Type:** Generative AI | **Platform:** MLFORGE

## 1. Overview
Controlled generative language module crafting rhythmic verse and prose with configurable temperature, top-k, and style seeds.

## 2. Problem Type & Paradigm
- **Task:** Generative AI
- **Domain:** Generative AI
- **Baseline Architecture:** Character / Word-level Recurrent & Transformer Text Generator

## 3. Dataset & License
- **Dataset Identifer:** `literary_corpus_sample`
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
perplexity, token_entropy, repetition_penalty

## 6. Known Limitations
Can produce semantic repetition or nonsensical metaphors when conditioned on ultra-long horizons.

## 7. Responsible-Use Notes
All generated creative prose must be explicitly identified as AI-synthesized.
