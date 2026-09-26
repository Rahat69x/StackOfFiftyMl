# Security Policy

## Supported Versions
| Version | Supported |
| --- | --- |
| 1.0.x | Yes |
| < 1.0 | No |

## Reporting a Vulnerability
The MLFORGE engineering team takes security and algorithmic safety seriously. If you discover a vulnerability or sensitive data leakage risk:
1. Please do not create a public issue.
2. Email `security@mlforge.internal` with reproduction steps and impacted modules.
3. Our team will acknowledge receipt within 24 hours and issue a coordinated disclosure plan.

## Responsible ML & Algorithmic Governance
For projects involving healthcare, biometrics, financial risk, or employment (e.g. Projects 04, 17, 19, 28, 37, 38, 44, 46):
- All models operate in **research and decision-support simulation** mode only.
- Strict human oversight is mandatory before any high-stakes operational actions.
- Rate limiting and audit logging are actively enforced on inference endpoints.
