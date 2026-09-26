# Model Card: Matching Resumes To Job Descriptions (ML045)

## Model Details
- **Developer:** MLFORGE Team
- **Model Date:** September 2026
- **Model Version:** 1.0.0
- **Model Type:** Bi-Encoder Semantic Similarity Matcher + Skill Overlap Highlighter
- **License:** MIT Research License

## Intended Use
- **Primary Intended Uses:** Research, benchmarking, educational exploration, and decision-support simulation.
- **Out of Scope Uses:** STRICT LABOR FAIRNESS: Must not make final hiring or screening elimination decisions; provides non-binding assistance to human recruiters.

## Factors, Metrics & Evaluation Data
- **Target Metrics:** top_5_match_precision, cosine_similarity_avg, explainable_feature_weights
- **Dataset:** `resumes_jobs_sample` with stratified splits and cross-validation.

## Ethical Considerations & Responsible AI
STRICT LABOR FAIRNESS: Must not make final hiring or screening elimination decisions; provides non-binding assistance to human recruiters.

## Caveats and Recommendations
Keyword stuffing and unconventional career journeys can distort match scores.
