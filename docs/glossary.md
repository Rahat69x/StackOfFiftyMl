# Glossary of MLFORGE Terms (Appendix B)

- **`MLProject` Interface:** The base abstract class and contract every one of the 50 project modules implements so the shared engines can operate on them uniformly.
- **Model Card:** A standardized document describing a trained model's intended use, limitations, bias audits, and evaluation results.
- **Datasheet:** A document describing a dataset's provenance, collection method, known biases, and licensing terms.
- **Drift:** A change over time in the statistical distribution of input features or prediction outputs that can degrade model performance silently.
- **Responsible-Use Flag:** A registry tag marking a project as touching a sensitive domain (health, employment, elections, personal data, surveillance) that triggers heightened ethical disclosures.
- **Smoke Test:** A fast, lightweight verification test confirming a pipeline executes end-to-end without requiring expensive multi-epoch training or external dataset downloads.
- **Lineage:** Complete audit trail tracking the provenance, checksum, and transformation steps applied to a dataset before model ingestion.
- **Rollback:** The capability in the model registry to atomically revert the production active model pointer to a previously validated historical version.
