# Responsible AI & Ethical Machine Learning Framework

## Overview
MLFORGE embeds responsible AI governance directly into the platform architecture. Every project is evaluated for sensitive domain interactions and tagged accordingly.

## Flagged Sensitive Domains
- **Healthcare & Clinical Research (Projects 04, 19, 38, 40, 44):**
  - **Mandatory Disclaimer:** strictly research and decision-support simulation. Under no circumstances should predictions be interpreted as clinical diagnoses or medical advice.
- **Finance & Insurance (Projects 05, 17, 31, 33):**
  - **No Automated Adverse Action:** Systems must never automatically deny claims, reject loans, or execute live financial trades without certified human adjustor/analyst oversight.
- **Employment & HR Analytics (Projects 35, 37, 45):**
  - **Disparate Impact Auditing:** Mitigates hiring and wage discrimination. Prohibited from making automated termination or screening rejection choices.
- **Biometrics & Surveillance (Projects 16, 28, 50):**
  - **Consent & Right to be Forgotten:** Project 28 enforces an explicit revocable consent flow before facial enrollment and provides instantaneous deletion of stored face embeddings.
- **Civic & Electoral Forecasting (Project 46):**
  - **Strict Neutrality:** Prohibited from generating voter persuasion, political targeting, candidate ranking, or claiming deterministic future election outcomes.

## Model Cards & Datasheets
Every flagged project ships with a standardized Mitchell-et-al model card in `projects/<name>/docs/model_card.md` specifying:
- Intended Use & Target Users
- Out-of-Scope High-Impact Applications
- Evaluation Data & Demographic Factors
- Caveats, Biases, and Recommendations
