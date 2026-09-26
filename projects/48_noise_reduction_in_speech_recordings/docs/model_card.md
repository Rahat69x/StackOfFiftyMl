# Model Card: Noise Reduction In Speech Recordings (ML048)

## Model Details
- **Developer:** MLFORGE Team
- **Model Date:** September 2026
- **Model Version:** 1.0.0
- **Model Type:** Spectral Subtraction / Masking U-Net Autoencoder
- **License:** MIT Research License

## Intended Use
- **Primary Intended Uses:** Research, benchmarking, educational exploration, and decision-support simulation.
- **Out of Scope Uses:** Enhances speech clarity in videoconferencing and assistive hearing devices.

## Factors, Metrics & Evaluation Data
- **Target Metrics:** snr_improvement_db, pesq_proxy, latency_ms
- **Dataset:** `noisy_speech_spectrograms_sample` with stratified splits and cross-validation.

## Ethical Considerations & Responsible AI
Enhances speech clarity in videoconferencing and assistive hearing devices.

## Caveats and Recommendations
Extreme non-stationary noise can induce musical artifacts or phase distortions in the output audio.
