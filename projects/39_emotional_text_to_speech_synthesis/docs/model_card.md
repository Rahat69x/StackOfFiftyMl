# Model Card: Emotional Text-To-Speech Synthesis (ML039)

## Model Details
- **Developer:** MLFORGE Team
- **Model Date:** September 2026
- **Model Version:** 1.0.0
- **Model Type:** Emotion Conditioning Spectrogram Generator + Vocoder
- **License:** MIT Research License

## Intended Use
- **Primary Intended Uses:** Research, benchmarking, educational exploration, and decision-support simulation.
- **Out of Scope Uses:** Synthesized audio must carry watermarking or synthetic speech identification to prevent voice cloning fraud.

## Factors, Metrics & Evaluation Data
- **Target Metrics:** mel_cepstral_distortion, mos_proxy, latency_ms
- **Dataset:** `expressive_speech_sample` with stratified splits and cross-validation.

## Ethical Considerations & Responsible AI
Synthesized audio must carry watermarking or synthetic speech identification to prevent voice cloning fraud.

## Caveats and Recommendations
Synthesized voices may sound robotic or exhibit phoneme clipping on complex polysyllabic words.
